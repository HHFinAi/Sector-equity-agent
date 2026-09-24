# Validation — v3.0.0, 24 September 2026

**77 offline unit/regression tests passed.** The all-sector synthetic demo completed **25 stages**, exercised **11 company valuation models**, produced the sector matrix and claim ledger, and verified a **59-file artifact manifest**. All twelve workflows were tested for expanded all-sector prompt export. This is software validation, not a live investment-research quality score.

The suite retains 43 earlier contract/math/runtime/provider tests and adds 34 cross-sector tests. New coverage includes all eleven sectors and 79 distinct research lenses, single/multi/all routing, no healthcare default, incorrect sector/subsector assignments, missing and unknown evidence scope, explicit global-context limits, specialist source/company isolation, exclusion of sibling first-pass judgments, scoped manual prompt exports, preserving missing-sector blocks despite an optimistic model response, cross-sector citation leakage, sector-matrix tampering and model-source relevance.

Valuation tests cover business-model method rejection, bank equity values without a second debt/cash adjustment, P/E, property NAV and other claims, cap-rate bounds, duplicate properties, FFO/AFFO per-share inputs, dividend discount, negative-earnings rejection, scenario weights and source identifiers. Existing tests cover operating DCF, simplified rNPV and reverse valuation. All example companies and inputs are explicitly fictional.

## Reproduce

```bash
sh ci/test.sh
```

This runs all tests, the complete synthetic demo, hash verification and all-sector prompt export with temporary output paths. It does not call a network provider. GitHub Actions is not enabled by this change; the script can run in an approved CI environment.

## Not established

No live LLM inference, source retrieval integration, paid data, real security valuation, semantic citation validation, factor backtest, investment alpha, analyst accuracy, probability calibration, independent audit or production-security certification was evaluated. Mocked API requests establish request handling, not end-to-end provider compatibility. Local review is self-attestation, not authenticated approval.

Before investment reliance, evaluate representative real cases across the intended sectors, including missing-data and conflicting-source cases. Record primary-source fidelity, correct issuer/segment classification, financial normalization, model tie-out, point-in-time consistency, cross-sector causal reasoning, sustainability-materiality separation and thesis falsification quality. No software pass substitutes for those analyst judgments.
