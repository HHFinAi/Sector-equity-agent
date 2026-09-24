# Architecture and trust boundaries

## Execution model

This is a bounded sequential **workflow agent**, not nine independently trained models and not an unrestricted autonomous browser. The selected workflow supplies the stage order. Each specialist prompt receives the same frozen source packet, selected sector pack, deterministic model outputs and validated prior-stage responses. In live mode each stage makes a structured-output LLM request through one adapter. Roles represent analytical responsibilities; they do not prove independent judgment.

1. Validate mandate, sector/universe, source IDs, dates and declared public-data eligibility.
2. Compute optional analyst-input valuation scenarios deterministically.
3. Snapshot the brief, plan, sector pack and stage prompts.
4. Run each stage with bounded context/output/request counts.
5. Validate schema, claim kinds, known citations, confidence bounds, gap/decision consistency and challenge output.
6. Render the memo and underlying workpapers; create a file-hash manifest and audit trail.
7. Stop at DEMO, BLOCKED or NEEDS_HUMAN_REVIEW. Only the separate human command records local sign-off.

An invalid model response stops the run and records `error.json`; no final research status is produced. Incomplete/refused LLM responses are never accepted. A valid response with evidence gaps can continue as a partial analysis, but the final run remains BLOCKED and the CLI returns exit code 2. Invalid input/provider failures return code 1. Successful demo or structurally complete output returns code 0; that is not an investment approval.

## Modules

`contracts.py` owns data validation and the stage schema. `models.py` owns simplified deterministic math. `provider.py` owns the no-network fixture and explicit opt-in OpenAI adapter. `engine.py` owns plan export, orchestration, rendering, snapshots, hash verification and review. `__main__.py` exposes plan/validate/run/verify/approve.

## Provider and source boundaries

The OpenAI adapter uses the fixed HTTPS Responses API endpoint, structured JSON output, an environment-held key, a 120-second per-request timeout, at most two retries for selected rate-limit/server errors, and a total HTTP-request budget including retries. Redirects are refused; credentials are not forwarded to another host. There are no arbitrary HTTP tools, source crawlers, shell tools or trading APIs available to the model. Input character limits fail instead of silently truncating evidence. API timeouts may incur provider charges even without an accepted result; request limits are not dollar budgets.

The live request body follows OpenAI's documented structured-output interface. Official implementation reference, checked 24 September 2026: https://developers.openai.com/api/docs/guides/structured-outputs . A user-selected model must support the requested API capabilities. `store=false` is a request setting, not a zero-retention guarantee or substitute for organizational policy.

For richer source access, a separate authorized host can retrieve filings, trials, regulator/CMS records and market data, then construct the evidence packet. This repository does not package those host connectors. Exported prompts can guide that host; they do not grant permissions. New adapters should preserve the `generate(stage, instructions, context)` contract and return validated JSON. Do not wire credentials or provider-specific claims into prompts.

## Limits of controls

Source-ID validation catches nonexistent references but not fabricated text attributed to a real source. Date checks cannot verify website history, superseding disclosures or intraday availability. Public flags are user attestations, not classifiers. Prompt-injection instructions reduce risk but are not a proof of immunity; the hard boundary is that model text cannot execute tools or change workflow code.

Artifact hashes detect changes relative to a local manifest. They are not signed, externally timestamped or protected against an attacker replacing both files and manifest. Reviewer identity is self-declared. This is not a multi-user authorization system, compliance platform, order-management system or validated clinical tool.
