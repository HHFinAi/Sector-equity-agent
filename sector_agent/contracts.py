"""Input and model-output contracts. Structural checks are not fact verification."""
from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,79}$")


class ValidationError(ValueError):
    """A fail-closed data or output contract violation."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def text(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{label}: nonempty string required")
    return value


def number(value: object, label: str) -> float:
    require(type(value) in (int, float) and math.isfinite(value), f"{label}: finite number required")
    return float(value)


def iso_date(value: object, label: str) -> date:
    require(isinstance(value, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)),
            f"{label}: use YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{label}: invalid date") from exc


def identifier(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(IDENTIFIER.fullmatch(value)), f"{label}: unsafe ID")
    return value


def load_json(path: Path) -> dict:
    require(path.stat().st_size <= 2_000_000, f"{path}: input exceeds 2 MB limit")
    def no_constant(value: str):
        raise ValidationError(f"Non-finite JSON constant: {value}")
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    value = json.loads(path.read_text(encoding="utf-8"), parse_constant=no_constant,
                       object_pairs_hook=unique_keys)
    require(isinstance(value, dict), "Top-level JSON must be an object")
    return value


def canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n"


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def workflow(brief: dict) -> tuple[dict, dict]:
    name = identifier(brief.get("workflow"), "workflow")
    sector = identifier(brief.get("sector"), "sector")
    flows = load_json(ROOT / "workflows" / "catalog.json")
    require(name in flows, f"Unknown workflow: {name}")
    pack_path = ROOT / "sectors" / f"{sector}.json"
    require(pack_path.is_file(), f"Unknown sector pack: {sector}")
    pack = load_json(pack_path)
    return flows[name], pack


def validate_brief(brief: dict, *, demo: bool = False, plan_only: bool = False) -> list[str]:
    require(brief.get("schema_version") == "1.0", "schema_version must be 1.0")
    for key in ("question", "geography", "benchmark", "horizon"):
        text(brief.get(key), key)
    as_of = iso_date(brief.get("as_of"), "as_of")
    require(as_of <= date.today(), "as_of cannot be in the future")
    _, pack = workflow(brief)
    universe = brief.get("universe")
    require(isinstance(universe, list) and 0 < len(universe) <= 100, "universe: 1-100 entities required")
    seen = set()
    for entity in universe:
        require(isinstance(entity, dict), "universe entries must be objects")
        entity_id = identifier(entity.get("id"), "entity.id")
        require(entity_id not in seen, f"Duplicate entity: {entity_id}")
        seen.add(entity_id)
        text(entity.get("name"), "entity.name")
        require(entity.get("subsector") in pack["subsectors"], "Entity subsector not in selected sector pack")
    sources = brief.get("sources", [])
    require(isinstance(sources, list) and len(sources) <= 150, "sources must be a list of at most 150 records")
    if plan_only:
        return []
    require(bool(sources), "No sources: run plan, collect evidence, then run analysis")
    seen = set()
    warnings = []
    for source in sources:
        require(isinstance(source, dict), "source must be an object")
        sid = identifier(source.get("id"), "source.id")
        require(sid.lower() not in seen, f"Duplicate source ID: {sid}")
        seen.add(sid.lower())
        for key in ("title", "content", "period", "locator"):
            text(source.get(key), f"{sid}.{key}")
        require(len(source["content"]) <= 30_000, f"{sid}: excerpt exceeds 30,000 characters")
        kind = source.get("kind")
        require(kind in {"filing", "regulatory", "clinical", "company", "market", "research", "synthetic"},
                f"{sid}: unknown source kind")
        require(source.get("public") is True, f"{sid}: only public/redistributable inputs permitted in this version")
        if kind == "synthetic":
            require(demo, f"{sid}: synthetic source is allowed only in demo mode")
        else:
            url = urlparse(text(source.get("url"), f"{sid}.url"))
            require(url.scheme == "https" and bool(url.hostname) and not url.username and not url.password,
                    f"{sid}: source locator must be an HTTPS URL without credentials")
        published = iso_date(source.get("published_at"), f"{sid}.published_at")
        retrieved = iso_date(source.get("retrieved_at"), f"{sid}.retrieved_at")
        require(published <= as_of, f"{sid}: publication is after the research cut-off (look-ahead)")
        require(published <= retrieved <= date.today(), f"{sid}: invalid retrieval date")
        max_age = source.get("max_age_days", 120)
        require(type(max_age) is int and 0 <= max_age <= 3650, f"{sid}: invalid max_age_days")
        require((as_of - published).days <= max_age, f"{sid}: stale under its declared freshness policy")
        if retrieved > as_of:
            warnings.append(f"{sid}: retrieved after cut-off; analyst must verify an archived, point-in-time version")
        if kind in {"market", "research"}:
            warnings.append(f"{sid}: verify licensing and distinguish consensus/opinion from a primary-source fact")
    require(any(s["kind"] in {"filing", "regulatory", "clinical", "company", "synthetic"} for s in sources),
            "At least one primary-source record is required")
    return warnings


CLAIM_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "id": {"type": "string"}, "topic": {"type": "string"},
        "kind": {"type": "string", "enum": ["fact", "inference", "assumption"]},
        "text": {"type": "string"},
        "source_ids": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "number"}
    }
}
CLAIM_SCHEMA["required"] = list(CLAIM_SCHEMA["properties"])
STAGE_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "summary": {"type": "string"},
        "claims": {"type": "array", "items": CLAIM_SCHEMA},
        "gaps": {"type": "array", "items": {"type": "string"}},
        "thesis_breakers": {"type": "array", "items": {"type": "string"}},
        "decision": {"type": "string", "enum": ["continue", "needs_data"]}
    }
}
STAGE_SCHEMA["required"] = list(STAGE_SCHEMA["properties"])


def validate_stage(value: dict, source_ids: set[str]) -> None:
    require(isinstance(value, dict) and set(value) == set(STAGE_SCHEMA["required"]),
            "Stage output does not match required fields")
    text(value["summary"], "summary")
    require(value["decision"] in {"continue", "needs_data"}, "Invalid stage decision")
    require(isinstance(value["claims"], list), "claims must be a list")
    seen = set()
    for claim in value["claims"]:
        require(isinstance(claim, dict) and set(claim) == set(CLAIM_SCHEMA["required"]), "Invalid claim fields")
        cid = identifier(claim["id"], "claim.id")
        require(cid not in seen, f"Duplicate claim ID: {cid}")
        seen.add(cid)
        for key in ("topic", "text"):
            text(claim[key], f"{cid}.{key}")
        require(claim["kind"] in {"fact", "inference", "assumption"}, f"{cid}: invalid claim kind")
        ids = claim["source_ids"]
        require(isinstance(ids, list) and all(isinstance(s, str) for s in ids), f"{cid}: invalid citations")
        require(set(ids) <= source_ids, f"{cid}: unknown source citation")
        if claim["kind"] in {"fact", "inference"}:
            require(bool(ids), f"{cid}: factual and inferential claims require source IDs")
        score = number(claim["confidence"], f"{cid}.confidence")
        require(0 <= score <= 1, f"{cid}: confidence outside [0, 1]")
    for key in ("gaps", "thesis_breakers"):
        require(isinstance(value[key], list), f"{key} must be a list")
        for item in value[key]:
            text(item, key)
    if value["decision"] == "continue":
        require(bool(value["claims"]), "A continuing stage must contain evidence-linked analysis")
        require(not value["gaps"], "An unresolved gap must set decision=needs_data")
