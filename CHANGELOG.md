# Changelog

All notable changes to the Healthcare Equity Analyst Prompt Library are documented in this file. The library follows semantic versioning where major version increments indicate structural reorganisation, minor version increments indicate substantive additions to content or governance, and patch version increments indicate corrections and refinements.

## v1.4 — 2026-04

### Added

A coverage matrix now sits at the start of the library, showing how the 113 prompts distribute across the 16 workflow categories and seven sub-sector dimensions plus international. The matrix serves as a navigation aid for the analyst and a visual summary of library scope.

Every prompt now carries a one-line reasoning scaffold documenting the analytical movement the prompt produces. Examples include "parse consensus → identify swing factors → pre-commit scenarios" for EARN-01 and "expected label vs actual → commercial unlock → peak-sales delta → precedent" for SUB-BIO-08. The scaffolds appear in both the prompt's YAML metadata header and as a dedicated field in the markdown and PDF output.

Appendix D — Prompt Engineering Guidance — provides operational guidance across seven sections: temperature settings, reasoning style, tool routing, context management, output structure, model selection, and confidence score discipline.

The standing instructions gain a new paragraph titled "Workflow-mapped entry points" that maps the general source hierarchy to workflow type. Screening prompts start with Bloomberg and FactSet; model-building prompts with SEC filings; clinical prompts with ClinicalTrials.gov, FDA, and EMA; reimbursement prompts with CMS.

The worked examples companion document now includes mock source snippets (Bloomberg consensus, FactSet metadata, SEC 8-K excerpts, CMS disclosures, ClinicalTrials.gov records) preceding each rendered output, so users can see both what inputs to gather and how to format them.

### Changed

The library now totals 113 prompts across 16 categories with 11 workflow chains and four appendices (up from three).

## v1.3 — 2026-04

### Added

Eleven new prompts filling methodological gaps identified in a reviewer audit:

- **MOD-10** — Scenario Construction as a Discipline, treating scenarios as a transferable skill rather than a one-off output
- **SELL-04** — Single-Name Thesis Post-Mortem, with a five-category error classification framework
- **SELL-05** — Book-Wide Annual Post-Mortem and Process Audit
- **EN-04** — Expert-Management Divergence Triangulation, with MNPI guardrails and pre-committed decision rules
- **PORT-05** — Constructive Disagreement with Portfolio Manager on Sizing or Thesis
- **PORT-06** — Defending a Contrarian Thesis at Investment Committee
- **ESG-05** — Healthcare Climate Risk and Decarbonisation Pathway Assessment (TCFD, IFRS S2, CSRD-aligned)
- **INTL-01** — European HTA Pathway Mapping, including the EU Joint Clinical Assessment
- **INTL-02** — Japanese Reimbursement Cycle and Price Revision Analysis
- **INTL-03** — Chinese Biotech Licensing Economics and BIOSECURE Pass-Through
- **INTL-04** — UK-Specific Healthcare Dynamics for a London-Based Global Mandate

Two new workflow chains: Global Name International Exposure Chain and Annual Review and Learning Chain.

A compact variant of the standing instructions is now available alongside the full version.

Workflow chains in the markdown output are hyperlinked to the prompts they reference.

A companion worked-examples document shows four prompts executed against illustrative scenarios.

An authorship line on the cover page and in the readme opening paragraph establishes the library's practitioner origin: authored by a senior buy-side healthcare equity analyst with 7+ years of institutional research experience.

### Changed

The library grew from 102 to 113 prompts, and gained a new Category 16 for international coverage.

## v1.2 — 2026-04

### Added

Standing instructions now precede every prompt in the library, establishing a five-tier source hierarchy (filings first, regulatory records second, vendor data third, sell-side for triangulation only, expert network as single data points), eight required behaviours (including fact-inference separation, time-stamping, source-conflict reconciliation, MNPI guardrails, and confidence scoring between 0.00 and 1.00), and a default eight-element output skeleton.

Appendix C — Source-Data Fidelity Caveats — documents eight operationally relevant limitations: FDALabel versus Drugs@FDA, 13F lag and extraction error, conference embargo schedules, CMS file update cycles, ClinicalTrials.gov registry lag, Bloomberg SPLC gaps, consensus divergence, and sell-side structural biases.

Two new prompts: SUB-BIO-08 (Post-Approval Label Delta Analyser) and SUB-TLS-05 (Companion Diagnostic Linkage and Precision Medicine Coupling).

YAML metadata headers in the markdown output support programmatic ingestion into skill bases and knowledge management systems.

### Changed

The library grew from 100 to 102 prompts. The governance layer transformed the library from a structured catalogue into a behaviourally consistent system.

## v1.1 — 2026-03

### Added

A new Category 15 — Technical System Integration — with six prompts covering Bloomberg BQL, FactSet FQL, SEC EDGAR, and ClinicalTrials.gov API query construction.

Three compliance prompts in Category 13 for pre-publication review, post-distribution audit, and MNPI scrubbing.

Eighteen sub-sector extensions across biotech, pharma, medtech, tools and diagnostics, services and payors, digital health, and screening.

Quantitative anchors embedded in prompts (for example, GPA above 0.20, LTV:CAC above 3:1, approximately 65 to 70 per cent gross margin for mature razor-blade models, approximately 70 per cent Phase II and 50 per cent Phase III failure rates).

MNPI guardrails embedded in expert network and compliance prompts.

### Changed

The library grew from 56 to 100 prompts.

## v1.0 — 2026-03

### Added

Initial 56-prompt library across 14 categories covering initiation, earnings workflows, management meeting preparation, modelling and valuation, thesis development, sell discipline, sell-side synthesis, expert network, screening, thematic research, portfolio construction, ESG integration, client communication, and sub-sector deep dives.

Four-dimensional tag taxonomy across workflow, sub-sector, data source, and complexity.

Prescriptive prompt structure with seven to twelve numbered analytical steps per prompt.

---

*Maintained at [github.com/HHFinAi](https://github.com/HHFinAi).*
