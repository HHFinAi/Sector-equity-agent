# Sector Research Agent

**Healthcare-first equity research: evidence → sector structure → company economics → valuation → falsifiable thesis.**

Version **2.0.0** · **6 workflows** · **9 specialist stages** · **6 healthcare subsectors** · **43 offline regression tests**

Sector Research Agent replaces this repository's prompt-library-only interface with an executable, evidence-gated research workflow. It supports a human buy-side analyst researching sector structure, thematic opportunities, company exposures, earnings cross-reads and catalysts. Its central question is not simply *what is growing?* but *where do changing fundamentals differ from the expectations already reflected in price?*

The project remains in the existing `HHFinAi/healthcare-equity-prompt-library` repository. This migration changes the contents and project identity, **not the GitHub repository name or visibility**. The original 113-prompt v1.4 library is preserved under [`reference/`](reference/) and in Git history.

## What is implemented

| Layer | Delivered capability |
|---|---|
| Analyst prompts | Governing prompt plus nine ordered specialist-stage prompts with evidence and handoff contracts. |
| Workflow engine | Six selectable workflows; frozen input, source and prompt snapshots; structured stage outputs; bounded model calls. |
| Sector knowledge | Biotech, pharma, medtech, services/payors, tools/diagnostics and digital health; general-sector customization template. |
| Evidence controls | Required source IDs, dated records, freshness checks, look-ahead checks, primary-source minimum, public-data attestation and explicit missing-data states. |
| Valuation | Deterministic scenario math: EV/EBITDA, simplified DCF and probability-weighted cash-flow rNPV; equity bridge and conditional reverse-revenue valuation. |
| Output and review | Markdown memo, JSON workpapers, audit log, SHA-256 artifact manifest and explicit local human-review attestation. |
| Execution modes | No-key synthetic demo; optional OpenAI Responses API adapter; exported prompts for manual/tool-enabled host use. |

**Important boundary:** the Python agent analyzes an explicitly supplied evidence packet. It does **not** autonomously browse, connect to Bloomberg/FactSet/SEC/FDA/ClinicalTrials.gov, trade, send messages or run a monitoring service. Source acquisition is an analyst or tool-enabled host step. The LLM adapter is implemented and mock-tested, but no live LLM or paid data call was used to validate this release. Citation-ID checks do not establish that a source semantically supports a claim.

## Research flow

```text
Mandate → Evidence review → Sector map → Drivers → Company crosswalk
        → Valuation → Catalysts → Independent challenge → Synthesis
                                                        ↓
                                       Human source/model review
```

Evidence flows forward with its original IDs. The challenge stage tests the thesis; it does not replace the original source. Any unresolved material gap keeps the output **BLOCKED**. A demo is always **DEMO**, never approved research. A complete non-demo run becomes **NEEDS_HUMAN_REVIEW**; it cannot approve itself.

## Start with the no-key demo

Requires **Python 3.11 or later**, using the standard library only. Run commands from the repository checkout; no package installation is needed. Each output path must be new.

```bash
git clone https://github.com/HHFinAi/healthcare-equity-prompt-library.git
cd healthcare-equity-prompt-library
python -m unittest discover -s tests -v
python -m sector_agent run --brief examples/demo-brief.json --out runs/demo
python -m sector_agent verify --run runs/demo
```

Open `runs/demo/report.md`. All companies, inputs and numbers in this demonstration are fictional. The demo is a deterministic software harness, **not an LLM-generated research sample**. It exercises the nine stages, calculations, artifacts and review controls without credentials or network access.

## Use the prompts without an API key

```bash
python -m sector_agent plan --brief examples/brief-template.json --out runs/research-plan
```

This exports the ordered, expanded prompts and source requests. Edit the template's question, as-of date, universe, geography, benchmark and horizon first for a real mandate. In a tool-enabled research host, retrieve the required public/authorized evidence, apply `prompts/system.md`, then execute the selected stage prompts in order. Explicitly tell the host which tools it can use. A prompt export does not itself connect those tools or validate manually copied responses.

## Run with a live LLM

Create a research brief using [`docs/INPUTS.md`](docs/INPUTS.md). The blank template intentionally has no evidence and cannot run analysis until populated. Do not send proprietary, embargoed, personal or non-redistributable data.

```bash
# POSIX shell. Set secrets locally, never in a tracked file.
export OPENAI_API_KEY="YOUR_LOCAL_KEY"
export OPENAI_MODEL="YOUR_AVAILABLE_MODEL_ID"
python -m sector_agent validate --brief data/my-brief.json
python -m sector_agent run --brief data/my-brief.json \
  --provider openai --allow-network --out runs/my-research \
  --max-calls 16 --max-output-tokens 5000
```

`--allow-network` explicitly authorizes sending the supplied evidence to the configured OpenAI endpoint. The model ID is user-selected rather than hard-coded. The adapter uses structured JSON output and requests `store=false`; that flag is **not a promise of zero provider retention**. Apply your organization's provider policy. Model access, cost and end-to-end live behavior must be verified in your environment. Limits bound HTTP attempts/output tokens and context characters, not a guaranteed dollar spend.

## Human review

Read the source snapshots, stage workpapers, model assumptions and report; resolve material gaps in a **new run**. Verify the immutable bundle before attesting:

```bash
python -m sector_agent verify --run runs/my-research
python -m sector_agent approve --run runs/my-research \
  --reviewer "HHFinAi" --note "Describe the source, model and compliance checks performed" \
  --acknowledge-evidence
```

Approval writes a separate `review.json` bound to the artifact manifest; it does not rewrite the report. This is **local self-attestation**, not authenticated identity, a digital signature or firm compliance authorization. Hashes detect accidental changes relative to the manifest, not malicious replacement of both artifacts and manifest.

## Select a workflow

| Workflow ID | Main use |
|---|---|
| `sector-deep-dive` | Sector structure, drivers, company exposures, valuation and catalysts. |
| `idea-screen` | Research-priority watchlist; no forced numerical ranking or trade sizing. |
| `company-initiation` | Industry context and a source-linked company underwriting case. |
| `earnings-readthrough` | Supplied results, expectations, peer cross-reads and model impact. |
| `catalyst-review` | Clinical, regulatory, reimbursement, policy or commercial event research. |
| `thesis-monitor` | One-shot comparison of a supplied prior thesis and new evidence; no scheduler. |

Change `workflow` in the brief. Change `sector` to `general` and `subsector` to `general` to use the generic framework, or create a reviewed pack in `sectors/`. Healthcare is the developed domain pack; the general template is not a claim of expert coverage across every sector.

## Repository guide

```text
AGENTS.md                 Instructions for coding and research hosts
prompts/                  Governing policy + 9 stage prompts
workflows/catalog.json    Six ordered workflow definitions
sectors/                  Healthcare pack and general-sector template
sector_agent/             CLI, contracts, orchestration, provider and math
examples/                 Synthetic demo and blank intake template
tests/                    43 offline regression tests
ci/test.sh                Portable local/CI validation script
docs/                     Input contract, architecture, limitations, migration
reference/                Original v1.4 prompt library and examples
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/INPUTS.md`](docs/INPUTS.md), [`docs/VALIDATION.md`](docs/VALIDATION.md) and [`docs/MIGRATION.md`](docs/MIGRATION.md).

## Ownership, license and scope

Created for **HHFinAi**. The existing MIT license is retained. This is analyst decision-support software, not autonomous investment management, personalized investment advice, medical advice or a claim of investment performance. Human users remain responsible for source accuracy, clinical interpretation, investment judgment and applicable compliance requirements.
