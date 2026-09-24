# Architecture: a full all-sector workflow agent

## Scope and planning

The runtime supports a named major sector, `multi` with an explicit `sectors` list, or `all` for all eleven. No sector is silently assumed. The catalog has 79 original research subsectors, each with a business-model lens, KPIs and method allow-list. Its sector-level mandates add transmission mechanisms, primary-source requests, materiality tests, traps and diligence questions. Catalog membership is not verified issuer classification or full market coverage.

`workflows/catalog.json` contains twelve ordered workflows. `routing.resolve` selects packs; `expand_stages` turns `$specialists` into one stage per selected sector. The full all-sector comparison runs 25 stages: 14 common analytical stages plus eleven dedicated sector specialists. Shorter workflows retain challenge and synthesis at the end.

`plan` exports the expanded prompts, frozen mandate and stage-response schema. Sector-specialist exports are scoped to that specialist's companies, evidence and pack just as live calls are. Manual host use still requires manual source acquisition and response checks; exported prompts do not grant tools or enforce the Python validator in another interface.

## Runtime

1. Validate the mandate, universe, sector/subsector assignments, sources, dates and scope.
2. Route analyst-supplied model inputs through business-model-specific valuation checks and deterministic calculations.
3. Snapshot the plan, evidence brief, selected sector packs and coverage inventory.
4. Execute scoped specialist/common stages with fixed prompts and structured JSON responses.
5. Validate citation identifiers against the evidence actually available to each stage, claim types, confidence bounds and missing-data decisions.
6. Preserve unresolved gaps and independent coverage gaps in final status. A later synthesis cannot erase an earlier gap.
7. Export the memo, per-stage workpapers, source/claim references, sector matrix, valuation workpaper and audit log; hash the run artifacts.
8. Require explicit human source/model review before local self-attestation.

Specialists receive their own company universe, scoped evidence and explicitly marked global context. Other specialists' outputs are excluded from their first-pass context. Common comparison stages can read the validated workpapers. These are sequential roles using one configured model adapter, not independently trained or independently verified agents.

## Code ownership

`sector_data.py` is the original catalog. `routing.py` handles sectors, prompts, evidence scope and coverage. `contracts.py` validates the packet and stage schema. `valuation.py` owns active method dispatch, new equity/NAV math and business-model/source guardrails; `models.py` supplies existing deterministic operating-company DCF, EV/EBITDA and simplified rNPV helpers. `provider.py` contains demo and opt-in OpenAI adapters. `engine.py` owns orchestration, reports, CSV ledgers, manifests and review. `__main__.py` exposes `catalog`, `plan`, `validate`, `run`, `verify` and `approve`.

## States and exits

A demo is always `DEMO` and cannot be approved. A non-demo run with any stage or coverage gap is `BLOCKED`, with CLI exit code 2. A structurally complete non-demo run is `NEEDS_HUMAN_REVIEW`, not approved research. Invalid inputs or model responses fail closed and return code 1; an interrupted run records `error.json` rather than a successful result. Exit code 0 only means the command completed, not that investment conclusions are correct.

## Provider and security boundaries

The adapter uses the fixed HTTPS OpenAI Responses endpoint, environment-held credentials, structured JSON, bounded input/output and request attempts, refused redirects and no source-browsing or shell tools. It requests `store=false`, which is not a zero-retention guarantee. The default 48 HTTP attempts include retries; a 750,000-character context limit is not a token-window or dollar-cost guarantee. Users must select a compatible available model and apply their provider's data policy. Official implementation reference: [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs), checked 2026-09-24.

Source acquisition occurs outside the runtime through an analyst or an authorized tool-enabled host. The source-routing catalog describes needed evidence, not implemented third-party connectors. No live provider or paid-data connection was tested in this release.

Hashes detect artifact changes relative to a local manifest; they are not externally signed or timestamped. Reviewer identity is self-declared. Evidence-ID and scope checks do not prove semantic support or data completeness. Public-data flags are analyst attestations, not confidentiality classifiers. Prompt-injection instructions are not immunity; the hard boundary is that model text cannot execute tools or change the workflow. This is not an order-management, compliance-certification or multi-user authorization system.
