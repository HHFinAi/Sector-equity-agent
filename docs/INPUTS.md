# Input and output contract

## Research brief

`examples/brief-template.json` is an intentionally incomplete intake template. `examples/demo-all-sectors.json` is a complete **synthetic** all-sector test packet, not a source of investment facts.

Required brief fields: `schema_version` (`1.0`), `question`, `as_of` (`YYYY-MM-DD`), `workflow`, `sector`, `geography`, `benchmark`, `horizon`, `universe` and `sources`. Universe entries need a stable `id`, company `name` and a `subsector` from the selected sector pack. Use `sector: "all"`, a supported major-sector ID, or `sector: "multi"` with a `sectors` list. Multi/all universe entries must also have an explicit `sector` field. Run `python -m sector_agent catalog` for IDs. Use explicit `none` where no benchmark is appropriate; do not leave the research horizon implicit. A maximum of 100 entities and 150 curated source records is supported. Whole input JSON is capped at 2 MB. Duplicate JSON keys are rejected.

## Evidence record

```json
{
  "id": "S1",
  "title": "Exact public document title",
  "kind": "filing",
  "url": "https://example.org/replace-with-the-actual-primary-document",
  "published_at": "2026-09-20",
  "retrieved_at": "2026-09-24",
  "period": "Specify exact quarter, fiscal year or observation period",
  "locator": "Exact page, table, paragraph, section or record identifier",
  "public": true,
  "max_age_days": 120,
  "sector_ids": ["information-technology"],
  "entity_ids": ["REPLACE"],
  "content": "Insert the relevant original evidence excerpt, not an invented summary."
}
```

The dates and URL above are **format examples**, not real evidence. Source kinds: `filing`, `regulatory`, `clinical`, `company`, `market`, `research`, or `synthetic` (demo only). Source IDs must be unique, including case-insensitively for report anchors. `public: true` is the analyst's attestation that the excerpt is public or appropriately redistributable to the selected provider; the software cannot determine licensing or confidentiality from text.

Publication date cannot exceed the research cut-off. Retrieval date must be after publication and no later than today. Retrieval after the cut-off produces a warning because a current webpage may have changed; the analyst must supply/verify the historical version. Dates are day-level, **not intraday market timestamps**. Use a documented appropriate `max_age_days` for each observation; a default of 120 days is an input policy, not a claim that all financial or regulatory facts remain fresh that long. The runtime checks dates, not whether a source has been superseded. Refresh prices, regulatory decisions and event windows separately.

Excerpts are capped at 30,000 characters each and should be tightly relevant. Include sufficient context and source locators to verify meaning. Do not submit full copyrighted research reports, patient information, MNPI or secrets. Never put an API credential into a source URL. The Python runtime stores the supplied record and does not download or verify its URL.

## Evidence scope

Source records may declare `sector_ids`, `entity_ids` and boolean `global_context`. IDs must be selected/known and unique. In a multi/all run, unscoped sources are not automatically assigned to every sector. Explicit global context is available to specialists but does not substitute for sector-scoped primary evidence. Each selected sector needs a supplied company and primary-source record to clear the structural coverage gate; this is a minimum, not proof of exhaustive or semantically sufficient evidence. Legacy single-sector briefs can use unscoped sources.

## Valuation models

`valuation_models` is optional. Without it, no numerical target is manufactured. Workflows requiring valuation should return an evidence gap when inputs are missing.

For the operating-company methods (`multiple`, `dcf`, `rnpv`), each model requires `entity`, `method`, `currency`, `units: "millions"`, `basis: "as_of_present_value"`, `price`, `price_as_of`, `diluted_shares`, `cash`, `debt`, `source_ids`, `assumptions_note`, and exactly three named `scenarios`: bear/base/bull with probabilities summing to one. Input source IDs trace the model packet, not an automatic field-by-field source tie-out: document each key assumption and source in `assumptions_note`. Cash, debt, revenue, FCF and shares are in millions; price/value per share is in currency units. Prices must fall within seven days before the cut-off. A seven-day software bound does not make a stale quote investment-ready.

Methods and scenario-specific fields:

| Method | Required fields | Convention |
|---|---|---|
| `multiple` | `revenue`, `ebitda_margin`, `ev_ebitda` | Present-value forward-multiple convention, not an undiscounted future exit value. |
| `dcf` | `cash_flows`, `discount_rate`, `terminal_growth` | Annual year-end unlevered FCF, first entry one year from as-of; Gordon terminal value. |
| `rnpv` | `cash_flows`, `occurrence_probabilities`, `discount_rate` | Annual expected net FCF, separate probability of occurrence for each supplied period; no terminal value. |

DCF requires discount rate > terminal growth, positive discount rate and nonnegative terminal FCF. Do not force a Gordon model onto a runoff asset. rNPV requires one 0–1 occurrence probability per annual net cash flow. Unavoidable committed spend should not be down-weighted by approval probability; split/stage cash flows appropriately. This simple helper cannot independently model trial-path branching, within-year timing, correlated assets, changing royalties or cost contingencies. It is not a complete Pharmagellan valuation model. Do not double-risk cash flow already probability-adjusted.

The three operating-company methods above bridge EV + cash − debt to equity, floor equity at zero, and divide by supplied diluted shares. There is no preferred-stock, minority-interest, lease or debt-restructuring waterfall, no share-count forecast and no tax normalization. Supply an economically complete EV and consistent bridge yourself; the floor is not an insolvency recovery model. Scenario values must order bear ≤ base ≤ bull.

For `multiple`, reverse valuation solves:

```text
market-implied revenue = (price × diluted shares + debt − cash)
                         / (base EBITDA margin × base EV/EBITDA multiple)
```

This is a conditional algebraic backsolve, **not observed analyst consensus**. Comparability, forecast quality and assumptions remain analyst judgments.

## Stage output and human review

The JSON schema is defined in `sector_agent/contracts.py` and exported by `plan`. Each stage returns summary, claims, gaps, thesis_breakers and decision. Claims require IDs, topic, kind, text, source_ids and confidence. Facts and inferences require valid evidence IDs; assumptions may be uncited but must be explicitly labeled. Confidence is a model self-assessment, not a calibrated statistic. Unresolved gaps require `needs_data`. The challenge stage must include a thesis-breaker. The final gate checks **all** stages, so synthesis cannot silently erase an earlier missing-data condition.

`run` writes frozen inputs, selected prompts, plan, sector pack, stage JSON, valuation workpaper, report, result, audit and manifest. `verify` checks artifact hashes and file set. `approve` requires a completed non-demo run and explicit human self-attestation. Changes require a new run, not editing the frozen report and retaining an old approval.


## Equity and property methods in v3

All methods use the common `entity`, `currency`, `units: "millions"`, `basis: "as_of_present_value"`, `price`, `price_as_of`, `diluted_shares`, `source_ids`, `assumptions_note` and exactly three weighted bear/base/bull scenarios. The source packet must include evidence scoped to the model entity's sector. The active dispatcher rejects methods outside the research subsector's allow-list; passing it does not establish valuation suitability.

| Method | Scenario fields | Value basis |
|---|---|---|
| `pe` | `eps`, `multiple` | EPS × P/E, per diluted share. Requires positive normalized earnings. |
| `ptbv` | `tangible_book_per_share`, `multiple` | Tangible book/share × P/TBV. Requires positive tangible book. |
| `ffo` | `ffo_per_share`, `multiple` | Reconciled FFO/share × multiple. |
| `affo` | `affo_per_share`, `multiple` | Issuer-defined and reconciled AFFO/share × multiple. |
| `ddm` | `dividends_per_share`, `cost_of_equity`, `terminal_growth` | Annual year-end dividends with Gordon terminal; cost of equity > growth. |
| `nav` | `properties` with unique `name`, `noi`, `cap_rate`; plus `other_assets`, `cash`, `debt`, `other_claims` | Sum of ownership-adjusted cash NOI/cap rates + other assets + cash − debt − other claims, divided by diluted shares. |

P/E, P/TBV, P/FFO, P/AFFO and DDM value **equity directly**: they do not receive another cash/debt adjustment. Their enterprise-value output is `null`, displayed as not applicable. Property NAV uses ownership-adjusted cash NOI and all required claims in the same currency/millions; positive cap rates must be below 1. It does not forecast occupancy, independently appraise properties, model joint ventures or infer recurring capex. NAV's asset value is not normalized corporate earnings.

The code does not forecast bank regulatory capital, insurer reserves, reinvestment, future dilution, commodity curves or financial-statement adjustments. Negative earnings are not forced into a P/E model. No residual-income, full SOTP, asset-level commodity reserve or regulatory rate-base valuation engine is claimed; those can be scoped in a prompt but need separate verified calculations.

## Additional v3 exports

`coverage.json` records selected-sector company/source coverage. `sector-matrix.csv` stores sector IDs, selected entities, scoped primary sources, gaps, specialist decisions and summaries. `claim-ledger.csv` exports stage/claim IDs, kinds, text, sources and self-assessed confidence. These tables are research workpapers, not quantitative attractiveness rankings or measured factor exposures. CSV text beginning with a spreadsheet formula trigger is neutralized. Both tables and coverage records are included in the artifact manifest.
