# Validation record — 24 September 2026

**43 offline unit/regression tests passed locally** on the delivered source. The synthetic nine-stage end-to-end demo completed with status DEMO, and its 24-file artifact manifest verified. All six workflow prompt exports were exercised by tests. The OpenAI request/response contract was tested with mocked transport only.

## Tested controls

Input tests cover synthetic/live separation, missing evidence, future publication/look-ahead, future as-of, stale evidence, duplicate sources/JSON keys, private-input flags, credentials in URLs, unsafe IDs, invalid numbers, unknown/absent citations, unresolved-gap decisions and confidence bounds.

Math tests cover known DCF/rNPV calculations, invalid terminal assumptions, negative terminal FCF, probability bounds, scenario weights, zero shares, stale/future prices, inverted cases, empty models and conditional reverse valuation. The synthetic probability-weighted per-share value is 29.0075; it is an invented software fixture, not a security price or forecast.

Runtime tests cover all workflow exports, demo labeling and approval rejection, explicit human attestation, report/file-set tampering, overwrite refusal, failure artifacts and carrying upstream evidence gaps through final synthesis. Provider tests cover no-network default, missing keys, incomplete/refused output, response parsing, refused redirects, request shape, input limits and retry-budget accounting.

## Not validated

No live LLM inference, paid provider, live market data, source retrieval connector, semantic entailment classifier, real investment research conclusion, production deployment, backtest, trading performance or multi-user security control was tested. A mocked request is not an end-to-end API verification. Prompt quality still requires real analyst evaluation across representative cases.

## Reproduce

```bash
sh ci/test.sh
```

The CI script uses only Python's standard library and a temporary output directory. GitHub Actions is not enabled by this release; run the script in your approved CI environment. Source-date examples use a fixed research cut-off, so do not reinterpret old fixtures as current market data.

## Analyst evaluation rubric before live reliance

Inspect a representative sample in each intended subsector. Score primary-source fidelity, numerical tie-out, point-in-time correctness, sector-to-company transmission, variant-view specificity, falsification quality and restraint under missing data. Record errors and revisions; do not advertise accuracy, calibration or investment performance without measured evidence. Never treat the software's confidence field as a validated probability of an investment or clinical outcome.
