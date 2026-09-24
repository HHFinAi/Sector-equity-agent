"""Bounded orchestration, frozen inputs, inspectable output and local review gates."""
from __future__ import annotations

import html
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from . import __version__
from .contracts import (ROOT, STAGE_SCHEMA, canonical, digest, load_json, require,
                        text, validate_brief, validate_stage, workflow)
from .valuation import value_models as valuations
from .routing import stage_prompt, context_for, coverage


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def save(path: Path, value: object) -> None:
    path.write_text(canonical(value), encoding="utf-8")


def safe(value: object) -> str:
    return html.escape(str(value), quote=False).replace("[", "\\[").replace("]", "\\]")


def build_plan(brief: dict) -> dict:
    validate_brief(brief, plan_only=True)
    flow, pack = workflow(brief)
    stages = flow["stages"]
    require(len(stages) == len(set(stages)), "Workflow contains duplicate stages")
    require(stages[-2:] == ["challenge", "synthesis"],
            "Every workflow must finish with challenge followed by synthesis")
    for stage in stages:
        stage_prompt(stage, pack)
    return {"version": __version__, "workflow": brief["workflow"], "purpose": flow["purpose"],
            "question": brief["question"], "as_of": brief["as_of"],
            "sector": brief["sector"], "stages": stages,
            "source_requests": pack["source_requests"], "required_outputs": flow["outputs"],
            "review_gate": "Human must verify claims, primary sources, model inputs and compliance before use."}


def export_plan(brief: dict, out: Path) -> dict:
    plan = build_plan(brief)
    out.mkdir(parents=True, exist_ok=False)
    save(out / "plan.json", plan)
    save(out / "stage-response.schema.json", STAGE_SCHEMA)
    system = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
    _, pack = workflow(brief)
    for index, stage in enumerate(plan["stages"], 1):
        prompt = stage_prompt(stage, pack)
        scope = context_for(stage, brief, pack, [], {})
        content = system + "\n\n" + prompt + "\n\n## Mandate\n```json\n" + canonical(scope["brief"]) + "```\n"
        content += "\n## Sector pack\n```json\n" + canonical(scope["sector_pack"]) + "```\n"
        content += "\nAttach validated prior-stage outputs and sources; never invent missing tool access.\n"
        (out / f"{index:02d}-{stage}.md").write_text(content, encoding="utf-8")
    return plan


def render(result: dict, brief: dict) -> str:
    lines = ["# Sector Research Agent | Research memo", "",
             f"**Status: {result['status']}** | As of: {brief['as_of']} | Version: {__version__}", "",
             f"**Question:** {safe(brief['question'])}", "",
             f"**Scope:** {safe(brief['sector'])}; {safe(brief['geography'])}; "
             f"benchmark {safe(brief['benchmark'])}; horizon {safe(brief['horizon'])}.", "",
             "This is analyst decision support, not an executed trade or a clinical recommendation. "
             "Citation checks validate identifiers, not whether a source entails a claim. "
             "Confidence values are model self-assessments, not calibrated probabilities.", ""]
    if result["provider"] == "demo":
        lines += ["> SYNTHETIC DEMONSTRATION. No live data, no LLM inference, no investment conclusion.", ""]
    if result["warnings"]:
        lines += ["## Source cautions", ""] + [f"- {safe(w)}" for w in result["warnings"]] + [""]
    if result.get("coverage"):
        lines += ["## Cross-sector scope and evidence coverage", "",
                  "Counts describe this packet only, not the full market or semantic evidence quality.", "",
                  "| Sector | Supplied companies | Scoped primary records | Missing coverage |",
                  "|---|---:|---:|---|"]
        for sid, row in result["coverage"].items():
            lines.append(f"| {sid} | {len(row['entity_ids'])} | {len(row['primary_source_ids'])} | "
                         f"{safe('; '.join(row['gaps']) or 'None structurally detected')} |")
        lines += [""]
    # Show the final answer first, then the underlying workpapers.
    stages = result["stages"]
    order = ["synthesis"] + [s for s in stages if s != "synthesis"]
    for stage in order:
        if stage not in stages:
            continue
        item = stages[stage]
        lines += [f"## {stage.replace('_', ' ').title()}", "", safe(item["summary"]), ""]
        for claim in item["claims"]:
            refs = " ".join(f"[{sid}](#source-{sid.lower()})" for sid in claim["source_ids"])
            lines += [f"**{safe(claim['topic'])} | {claim['kind']} | confidence {claim['confidence']:.2f}**",
                      f"{safe(claim['text'])} {refs}", ""]
        if item["gaps"]:
            lines += ["**Unresolved evidence gaps**", ""] + [f"- {safe(g)}" for g in item["gaps"]] + [""]
        if item["thesis_breakers"]:
            lines += ["**Thesis breakers**", ""] + [f"- {safe(t)}" for t in item["thesis_breakers"]] + [""]
    lines += ["## Deterministic valuation workpaper", ""]
    if not result["valuations"]:
        lines += ["Not supplied. No target prices, expected returns or numerical rankings were manufactured.", ""]
    for model in result["valuations"]:
        lines += [f"### {safe(model['entity'])}: {model['method']} ({safe(model['currency'])})", "",
                  "| Case | Analyst weight | EV (millions) | Value/share | Upside |",
                  "|---|---:|---:|---:|---:|"]
        for case in model["scenarios"]:
            lines.append(f"| {case['name']} | {case['probability']:.0%} | {format(case['enterprise_value'], '.2f') if case['enterprise_value'] is not None else 'Not applicable'} | "
                         f"{case['value_per_share']:.2f} | {case['upside']:.1%} |")
        lines += ["", f"Probability-weighted value/share: **{model['expected_value_per_share']:.2f}**; "
                  f"upside: **{model['expected_upside']:.1%}**.", "", safe(model["assumptions_note"]), "",
                  safe(model["limitations"]), ""]
        if model["reverse_valuation"]:
            lines += [f"Reverse valuation: {safe(model['reverse_valuation']['metric'])} = "
                      f"{model['reverse_valuation']['value']:.2f} million. This is an algebraic conditional "
                      "backsolve, not observed consensus.", ""]
    lines += ["## Source ledger", ""]
    for source in brief["sources"]:
        url = quote(source.get("url", ""), safe=":/?=&%#-_.~")
        title = safe(source["title"])
        label = f"[{title}]({url})" if source["kind"] != "synthetic" else title + " (synthetic)"
        lines += [f"### Source {source['id']}", "", label, "",
                  f"Kind: {source['kind']} | published: {source['published_at']} | "
                  f"retrieved: {source['retrieved_at']} | period: {safe(source['period'])}",
                  f"Locator: {safe(source['locator'])}", ""]
    lines += ["## Review and next use", "",
              "Verify every material factual assertion against the frozen evidence, review model definitions "
              "and missing data, and check licensing and firm compliance. A separate review.json records "
              "local analyst sign-off; this report itself remains an immutable draft. No execution tools exist.", ""]
    return "\n".join(lines)


def make_manifest(out: Path) -> dict:
    files = {}
    for path in sorted(out.rglob("*")):
        if path.is_file() and path.name not in {"manifest.json", "review.json"}:
            require(not path.is_symlink(), "Symlinks not permitted in a run bundle")
            files[path.relative_to(out).as_posix()] = digest(path.read_bytes())
    manifest = {"version": __version__, "created_at": now(), "files": files}
    save(out / "manifest.json", manifest)
    return manifest


def run(brief: dict, provider, out: Path) -> dict:
    demo = provider.name == "demo"
    warnings = validate_brief(brief, demo=demo)
    plan = build_plan(brief)
    computed = valuations(brief)
    _, pack = workflow(brief)
    out.mkdir(parents=True, exist_ok=False)
    (out / "prompts").mkdir()
    save(out / "brief.json", brief)
    save(out / "plan.json", plan)
    save(out / "sector-pack.json", pack)
    scoped_coverage = coverage(brief, pack)
    save(out / "coverage.json", scoped_coverage)
    save(out / "valuation.json", computed)
    system = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
    result = {"version": __version__, "created_at": now(), "provider": provider.name,
              "model": provider.model, "status": "RUNNING", "warnings": warnings,
              "stages": {}, "valuations": computed, "coverage": scoped_coverage}
    ids = {source["id"] for source in brief["sources"]}
    audit = out / "audit.jsonl"
    def event(kind: str, **details):
        with audit.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"at": now(), "event": kind, **details}, allow_nan=False) + "\n")
    event("run_started", provider=provider.name, model=provider.model)
    try:
        for stage in plan["stages"]:
            instructions = system + "\n\n" + stage_prompt(stage, pack)
            (out / "prompts" / f"{stage}.md").write_text(instructions, encoding="utf-8")
            event("stage_started", stage=stage)
            context = context_for(stage, brief, pack, computed, result["stages"])
            response = provider.generate(stage, instructions, context)
            save(out / f"{stage}.json", response)
            validate_stage(response, {source["id"] for source in context["brief"]["sources"]})
            if stage == "challenge":
                require(bool(response["thesis_breakers"]), "Challenge stage must specify a falsification test")
            result["stages"][stage] = response
            event("stage_validated", stage=stage, decision=response["decision"])
        blocked = (any(s["decision"] == "needs_data" for s in result["stages"].values())
                   or any(c["gaps"] for c in scoped_coverage.values()))
        result["status"] = "DEMO" if demo else "BLOCKED" if blocked else "NEEDS_HUMAN_REVIEW"
        result["usage"] = provider.usage
        export_ledgers(out, result, pack)
        save(out / "result.json", result)
        (out / "report.md").write_text(render(result, brief), encoding="utf-8")
        event("run_finished", status=result["status"], http_calls=provider.calls)
        make_manifest(out)
        return result
    except Exception as exc:
        # Do not persist raw exception bodies: providers may include sensitive requests.
        save(out / "error.json", {"status": "FAILED", "type": type(exc).__name__,
                                   "message": "Run stopped. Inspect the local terminal and validated stage files."})
        event("run_failed", error_type=type(exc).__name__)
        make_manifest(out)
        raise


def verify(out: Path) -> dict:
    require(not out.is_symlink(), "Run root cannot be a symlink")
    manifest_path = out / "manifest.json"
    require(not manifest_path.is_symlink(), "Manifest cannot be a symlink")
    manifest = load_json(manifest_path)
    declared = manifest.get("files")
    require(isinstance(declared, dict) and bool(declared), "Empty or invalid manifest")
    actual = set()
    for path in out.rglob("*"):
        require(not path.is_symlink(), "Symlink detected in run bundle")
        if path.is_file() and path.relative_to(out).as_posix() not in {"manifest.json", "review.json"}:
            actual.add(path.relative_to(out).as_posix())
    require(actual == set(declared), "Run file set differs from manifest")
    for name, expected in declared.items():
        path = (out / name).resolve()
        require(path.is_relative_to(out.resolve()), "Manifest path escapes the run directory")
        require(digest(path.read_bytes()) == expected, f"Changed run artifact: {name}")
    if (out / "review.json").exists():
        review = load_json(out / "review.json")
        require(review.get("manifest_sha256") == digest(manifest_path.read_bytes()), "Review does not match run manifest")
    return {"verified": True, "files": len(actual), "reviewed": (out / "review.json").exists()}


def approve(out: Path, reviewer: str, note: str, acknowledge: bool) -> dict:
    verify(out)
    require(acknowledge, "Explicit --acknowledge-evidence is required after manual verification")
    text(reviewer, "reviewer")
    text(note, "review note")
    result = load_json(out / "result.json")
    require(result.get("status") == "NEEDS_HUMAN_REVIEW" and result.get("provider") != "demo",
            "Cannot approve a demo, failed run, or a run with unresolved gaps")
    require(not (out / "review.json").exists(), "This immutable run already has a review record")
    review = {"decision": "approved_for_analyst_use", "reviewer": reviewer, "note": note,
              "reviewed_at": now(), "manifest_sha256": digest((out / "manifest.json").read_bytes()),
              "disclaimer": "Local self-attestation, not authenticated identity or compliance authorization."}
    save(out / "review.json", review)
    return review


def export_ledgers(out: Path, result: dict, pack: dict) -> None:
    """Export inspectable CSVs; neutralize spreadsheet formula injection in text cells."""
    def cell(value):
        value = str(value)
        return "'" + value if value.lstrip().startswith(('=', '+', '-', '@')) else value
    with (out / 'sector-matrix.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['sector_id','sector_name','entity_ids','primary_source_ids','coverage_gaps','specialist_decision','specialist_summary'])
        for sid, cov in result['coverage'].items():
            specialist = result['stages'].get('specialist_' + sid, {})
            writer.writerow([cell(x) for x in [sid,pack['sectors'][sid]['name'], '; '.join(cov['entity_ids']),
                '; '.join(cov['primary_source_ids']), '; '.join(cov['gaps']), specialist.get('decision','not_run'),specialist.get('summary','')]])
    with (out / 'claim-ledger.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['stage','claim_id','topic','kind','claim','source_ids','self_assessed_confidence'])
        for stage, item in result['stages'].items():
            for claim in item['claims']:
                writer.writerow([cell(x) for x in [stage,claim['id'],claim['topic'],claim['kind'],claim['text'],
                    '; '.join(claim['source_ids']),claim['confidence']]])
