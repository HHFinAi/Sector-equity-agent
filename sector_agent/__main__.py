"""Run from the repository root: python -m sector_agent --help."""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path
from .contracts import ValidationError, load_json, validate_brief, canonical
from .engine import approve, export_plan, run, verify
from .models import valuations
from .provider import DemoProvider, OpenAIProvider


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Healthcare-first, evidence-gated Sector Research Agent")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("plan", "validate", "run"):
        child = sub.add_parser(command)
        child.add_argument("--brief", required=True, type=Path)
        if command in {"plan", "run"}:
            child.add_argument("--out", required=True, type=Path, help="New directory; existing directories are never overwritten")
        if command == "validate":
            child.add_argument("--demo", action="store_true")
        if command == "run":
            child.add_argument("--provider", choices=["demo", "openai"], default="demo")
            child.add_argument("--allow-network", action="store_true")
            child.add_argument("--model", default=os.environ.get("OPENAI_MODEL", ""))
            child.add_argument("--max-calls", type=int, default=16)
            child.add_argument("--max-input-chars", type=int, default=180_000)
            child.add_argument("--max-output-tokens", type=int, default=5000)
    for command in ("verify", "approve"):
        child = sub.add_parser(command)
        child.add_argument("--run", required=True, type=Path)
        if command == "approve":
            child.add_argument("--reviewer", required=True)
            child.add_argument("--note", required=True)
            child.add_argument("--acknowledge-evidence", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "verify":
            print(canonical(verify(args.run)))
        elif args.command == "approve":
            print(canonical(approve(args.run, args.reviewer, args.note, args.acknowledge_evidence)))
        else:
            brief = load_json(args.brief)
            if args.command == "plan":
                print(canonical(export_plan(brief, args.out)))
            elif args.command == "validate":
                warnings = validate_brief(brief, demo=args.demo)
                values = valuations(brief)
                print(canonical({"valid": True, "warnings": warnings, "valuation_models": len(values)}))
            else:
                provider = DemoProvider() if args.provider == "demo" else OpenAIProvider(
                    model=args.model, allow_network=args.allow_network, max_calls=args.max_calls,
                    max_input_chars=args.max_input_chars, max_output_tokens=args.max_output_tokens)
                result = run(brief, provider, args.out)
                print(canonical({"status": result["status"], "report": str(args.out / "report.md"),
                                 "stages": len(result["stages"])}))
                return 2 if result["status"] == "BLOCKED" else 0
        return 0
    except (ValidationError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
