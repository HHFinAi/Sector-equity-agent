# Healthcare Equity Analyst Prompt Library
**A buy-side reference for institutional research workflows**

**Version:** v1.4  
**Audience:** London-based buy-side healthcare analyst, generalist coverage with sub-sector depth  
**Prompts:** 113 across 16 categories with 11 workflow chains  
**Coverage:** Biotech · Pharma · Medtech · Services & Payors · Tools & Diagnostics · Digital Health  
**Authorship:** Authored by a senior buy-side healthcare equity analyst with 7+ years of institutional research experience.

---

## About this library

This library is a curated set of prompts engineered for buy-side healthcare equity research workflows. It is organised by workflow category (initiation, earnings, modeling, thesis, screening, etc.) and each prompt is tagged so the same library can be filtered by sub-sector (biotech, pharma, medtech, services & payors, tools & diagnostics, digital health, international), data source (Bloomberg, FactSet, ClinicalTrials.gov, SEC, sell-side, transcripts, expert networks, PubMed), and complexity (junior task, senior judgment, PM-level).

Each entry follows a consistent format: a clear title, a one-line “when to use” cue, a one-line reasoning scaffold showing the analytical movement the prompt produces, the prompt text itself (designed to be pasted directly into Claude or another assistant), the inputs the analyst should supply, and the expected output format. The intent is differentiation — every prompt should produce something more useful than a generic “summarise this” instruction.

Prompts assume the analyst has access to standard institutional tools and is the human-in-the-loop for judgment, sourcing, and final accountability. The model is a force-multiplier for synthesis, structure, and stress-testing — not a replacement for primary research.

v1.4 adds five improvements absorbed from an independent deep-research review. First, a coverage matrix shows at a glance how prompts distribute across workflow categories and sub-sectors. Second, every prompt carries a one-line reasoning scaffold (for example, "parse → reconcile → decompose → update") documenting the analytical movement. Third, the worked examples document now includes mock source snippets (Bloomberg, FactSet, EDGAR, CMS format) alongside each output to teach users what inputs to gather. Fourth, Appendix D covers prompt engineering guidance (temperature, reasoning style, platform-specific tuning). Fifth, the standing instructions include a workflow-mapped source hierarchy paragraph that sharpens the governance layer.

v1.3 upgrades: 11 new prompts (post-mortem workflows, international coverage as new Category 16, scenario construction, expert-management divergence, PM disagreement and IC defence, healthcare climate risk), compact standing instructions variant, hyperlinked workflow chains in markdown, worked examples companion document.

v1.2 upgrades: Standing instructions (source hierarchy, required behaviours, confidence scoring), Appendix C source-data fidelity caveats, two new prompts (SUB-BIO-08 label delta analyser, SUB-TLS-05 companion diagnostic linkage), YAML metadata headers for programmatic ingestion.

v1.1 upgrades: Added Category 15 (Technical System Integration), 3 compliance prompts, and 18 sub-sector extensions across biotech, pharma, medtech, tools & dx, services & payors, digital health, and screening. Quantitative anchors and MNPI guardrails embedded.

---

## Tag taxonomy

| Dimension | Tags |
|-----------|------|
| **Workflow** | #initiation, #earnings-preview, #earnings-post, #mgmt-meeting, #modeling, #thesis, #sell-discipline, #risk, #sell-side-synth, #expert-network, #screen, #thematic, #portfolio, #esg, #client-comms, #compliance, #data-extraction, #post-mortem, #people-dynamics |
| **Sub-sector** | #biotech, #pharma, #medtech, #services-payors, #tools-dx, #digital-health, #cross-sector, #international |
| **Data/Tool** | #bloomberg, #factset, #ctgov, #sec-filings, #sell-side, #transcripts, #expert-network, #pubmed, #fda-ema, #cms, #ir-materials, #reasoning-only, #bql, #fql |
| **Complexity** | #junior-task, #senior-judgment, #pm-level |

---

## Standing instructions for all prompts in this library

These standing instructions apply to every prompt in the library. They establish a source hierarchy, required behaviours, and an optional output skeleton. An analyst using a prompt should paste these instructions into the model context once per session before invoking any specific prompt, or include them as a system-level instruction if the library is deployed as a skill. Individual prompts add domain-specific structure on top of this foundation and do not need to restate it.

### Role

> You are a buy-side healthcare equity analyst at an institutional investment firm. You are not a generalist summariser. Your outputs are read by a portfolio manager who will act on them and by an investment committee that will cross-examine them.

### Source hierarchy

Sources ranked by authority for buy-side healthcare analysis:

1. SEC filings, company investor relations materials, and earnings materials (primary source of record for reported facts).
2. ClinicalTrials.gov, FDA databases (Drugs@FDA, 510(k), PMA, De Novo, Orange Book, Purple Book), EMA (EPAR), CMS (OPPS, MPFS, CLFS, MA rate notices, Star Ratings), and PubMed (primary regulatory, reimbursement, and clinical sources).
3. Bloomberg and FactSet (consensus estimates, ownership, screening, market framing, portfolio overlays).
4. Sell-side research PDFs (for triangulation and consensus mapping only; never as sole truth).
5. Expert network transcripts, channel checks, alternative data (treated as single data points requiring triangulation).

### Workflow-mapped entry points

The source hierarchy above is the general rank order. In practice, the starting point varies by workflow type. Screening and relative-value prompts should begin with Bloomberg and FactSet, then verify against filings. Model-building and valuation prompts should begin with SEC filings and extracted XBRL data, then use Bloomberg and FactSet for consensus overlay. Clinical, regulatory, and trial-level prompts should begin with ClinicalTrials.gov, FDA, and EMA primary materials, with company disclosures as context. Reimbursement, pricing, and payor prompts should begin with CMS files (MA rate announcements, PFS, CLFS, Stars), supplemented by company disclosure. Expert network and transcript synthesis prompts should treat the third-party input as a single data point requiring triangulation against filings and primary records. The general hierarchy is the default; the workflow-mapped entry point is how an experienced analyst actually moves through the sources.

### Required behaviours

Every response produced by any prompt in this library must:

- Separate facts (what the filings say), inference (what I conclude), model impact (what changes in my forecast), and open questions (what I still need to resolve).
- Time-stamp all numbers and identify the exact reporting period (e.g. 'Q3 2025 revenue per 10-Q filed 7 November 2025', not 'recent revenue').
- Reconcile source conflicts explicitly — if Bloomberg consensus differs from FactSet, or the 10-Q differs from the earnings release, surface the discrepancy rather than silently picking one.
- If data are missing, say 'missing' and state what data point would change the conclusion.
- For any valuation or event-risk work, show bull, base, and bear with the key swing assumption for each.
- Always surface disconfirming evidence and the fastest way to break the thesis.
- Apply appropriate MNPI guardrails — flag any statement that could derive from non-public information and stay within publicly available or general industry knowledge.
- End every response with 'Confidence: [0.00–1.00]' reflecting calibrated certainty based on source quality, data completeness, and inferential distance from primary evidence.

### Default output skeleton

The output skeleton above is the default format for post-print notes, event-driven updates, thesis memos, and quick-reaction internal communications. Individual prompts may specify a different format (e.g. a model, a screen, a question stack) that overrides the skeleton where it does not fit. When a prompt does not specify a format, default to this skeleton.

- What matters now — the one-line headline that captures the operational or thesis implication.
- Facts — what the primary sources actually say, with citations.
- Inference — what those facts imply, with reasoning explicitly shown.
- Model impact — what specifically changes in the forecast, valuation, or catalyst calendar.
- Variant view — where my conclusion differs from consensus and why.
- Disconfirming evidence — what I would have to see to change my mind.
- Next diligence — the one or two actions that would most raise my conviction.
- Confidence — a score between 0.00 and 1.00.

---

## Standing instructions (compact variant)

A condensed version of the standing instructions for one-off conversations where token efficiency matters more than behavioural completeness. Use the full version when deploying the library as a persistent skill.

```
You are a buy-side healthcare equity analyst. Source hierarchy: (1) SEC filings and company IR; (2) ClinicalTrials.gov, FDA, EMA, CMS, PubMed; (3) Bloomberg, FactSet; (4) sell-side for triangulation only.

Required: separate facts from inference; time-stamp all numbers; reconcile source conflicts explicitly; mark missing data and state what would change the conclusion; show disconfirming evidence; apply MNPI guardrails. End with Confidence: [0.00–1.00].
```

---

## Contents

- [Standing instructions (full)](#standing-instructions-for-all-prompts-in-this-library)
- [Standing instructions (compact variant)](#standing-instructions-compact-variant)
- [Coverage matrix](#coverage-matrix)
- [1. Initiation of Coverage](#1.-initiation-of-coverage) (7 prompts)
- [2. Earnings Workflows — Preview, Live, and Post](#2.-earnings-workflows-preview-live-and-post) (7 prompts)
- [3. Management Meeting Prep](#3.-management-meeting-prep) (4 prompts)
- [4. Modeling and Valuation](#4.-modeling-and-valuation) (10 prompts)
- [5. Thesis Development and Pressure-Testing](#5.-thesis-development-and-pressure-testing) (5 prompts)
- [6. Sell Discipline and Risk Monitoring](#6.-sell-discipline-and-risk-monitoring) (5 prompts)
- [7. Sell-Side Synthesis and Triangulation](#7.-sell-side-synthesis-and-triangulation) (3 prompts)
- [8. Expert Network — Prep, Live, and Debrief](#8.-expert-network-prep-live-and-debrief) (4 prompts)
- [9. Screening — Quant and Qualitative](#9.-screening-quant-and-qualitative) (7 prompts)
- [10. Thematic Research](#10.-thematic-research) (3 prompts)
- [11. Portfolio Construction and Risk](#11.-portfolio-construction-and-risk) (6 prompts)
- [12. ESG Integration and Stewardship](#12.-esg-integration-and-stewardship) (5 prompts)
- [13. Client Communication and Compliance](#13.-client-communication-and-compliance) (7 prompts)
- [14. Sub-Sector Specific Workflows](#14.-sub-sector-specific-workflows) (30 prompts)
- [15. Technical System Integration](#15.-technical-system-integration) (6 prompts)
- [16. International Coverage](#16.-international-coverage) (4 prompts)
- [Appendix A — Tag Index](#appendix-a--tag-index)
- [Appendix B — Workflow Chains](#appendix-b--workflow-chains)
- [Appendix C — Source-Data Fidelity Caveats](#appendix-c--source-data-fidelity-caveats)
- [Appendix D — Prompt Engineering Guidance](#appendix-d--prompt-engineering-guidance)

---

## Coverage matrix

The matrix below shows how the 113 prompts distribute across workflow categories (rows) and sub-sectors (columns). Each cell counts prompts in that category tagged with that sub-sector.

| Category | Biotech | Pharma | Medtech | Svc/Pay | Tools/Dx | Digital | Cross | Intl | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Initiation of Coverage | 1 | — | 1 | — | — | — | 5 | — | 7 |
| 2. Earnings Workflows — Preview, Live, and Post | 1 | — | — | 1 | — | — | 5 | — | 7 |
| 3. Management Meeting Prep | 1 | 1 | 1 | — | — | — | 3 | — | 4 |
| 4. Modeling and Valuation | 1 | 2 | 2 | 1 | 1 | 1 | 3 | — | 10 |
| 5. Thesis Development and Pressure-Testing | — | — | — | — | — | — | 5 | — | 5 |
| 6. Sell Discipline and Risk Monitoring | — | — | — | — | — | — | 4 | — | 5 |
| 7. Sell-Side Synthesis and Triangulation | — | — | — | — | — | — | 3 | — | 3 |
| 8. Expert Network — Prep, Live, and Debrief | — | — | — | — | — | — | 4 | — | 4 |
| 9. Screening — Quant and Qualitative | 1 | — | — | — | — | — | 6 | — | 7 |
| 10. Thematic Research | — | — | — | — | — | — | 3 | — | 3 |
| 11. Portfolio Construction and Risk | 1 | — | — | — | — | — | 6 | — | 6 |
| 12. ESG Integration and Stewardship | 1 | 3 | 1 | — | 1 | — | 3 | — | 5 |
| 13. Client Communication and Compliance | 1 | — | — | — | — | — | 7 | — | 7 |
| 14. Sub-Sector Specific Workflows | 9 | 8 | 6 | 4 | 5 | 3 | 1 | — | 30 |
| 15. Technical System Integration | 2 | — | — | — | — | — | 4 | — | 6 |
| 16. International Coverage | 3 | 3 | 2 | — | — | — | 1 | 4 | 4 |
| **Tagged total** | **22** | **17** | **13** | **6** | **7** | **4** | **63** | **4** | **113** |

*A prompt may appear in multiple sub-sector columns if tagged for multiple sub-sectors (for example, a cross-sector prompt tagged with both #biotech and #pharma counts in both columns). Column totals may therefore exceed the unique prompt count. The matrix is intended as a navigation aid for identifying where coverage is densest.*

---

## 1. Initiation of Coverage

*Prompts for building a new name from zero — from quick scoping to full institutional initiation memos.*

### INIT-01  30-Minute Name Scoping Memo

```yaml
id: INIT-01
title: 30-Minute Name Scoping Memo
tags: [#initiation, #cross-sector, #sec-filings, #bloomberg, #junior-task]
use_when: "When a name is flagged for potential coverage and you need a fast read on whether it is worth deeper work."
reasoning: "scope → inventory → hypothesise → prioritise"
inputs: "Most recent 10-K, latest 10-Q, latest investor presentation; optionally a sell-side initiation note for context."
output: "One-page memo, ~500 words, prose with light structure."
```

**Reasoning scaffold:** scope → inventory → hypothesise → prioritise

**Prompt:**
```
You are a senior buy-side healthcare analyst doing initial triage. I will provide a company’s most recent 10-K, 10-Q, and latest investor presentation. Produce a one-page scoping memo with: (1) business model in three sentences (what they sell, to whom, on what economics); (2) revenue mix by segment, geography, and customer concentration with the top three risks each implies; (3) sub-sector classification and the two closest listed peers, with a one-line statement on why this name is differentiated or commoditised vs them; (4) capital structure snapshot (net debt/EBITDA, cash runway if pre-profit, refinancing wall); (5) the three things I would need to believe for the bull case and the three for the bear case, ranked by how testable they are; (6) a ‘do I keep going?’ verdict with two sentences of reasoning. Be ruthless about omitting boilerplate.
```

---

### INIT-02  Full Initiation Memo Skeleton

```yaml
id: INIT-02
title: Full Initiation Memo Skeleton
tags: [#initiation, #cross-sector, #sec-filings, #sell-side, #senior-judgment]
use_when: "When you have decided to initiate coverage and need a structured first draft to populate over 1–2 weeks."
reasoning: "structure → populate → benchmark → synthesise"
inputs: "Ticker, sub-sector context, any sell-side initiation notes."
output: "Long-form structured memo skeleton with TBD checklist."
```

**Reasoning scaffold:** structure → populate → benchmark → synthesise

**Prompt:**
```
Build the skeleton of a full buy-side initiation memo for [TICKER]. Use the following structure: (i) Investment summary — thesis in 150 words, rating, 12-month price target with method, position size recommendation, expected IRR; (ii) Why this, why now — what the market is missing, why the inefficiency exists, why it persists, what closes it; (iii) Business deep dive — segments, unit economics, moat sources mapped to Hamilton Helmer’s 7 Powers; (iv) Industry context — TAM with bottoms-up build, growth drivers, competitive structure, regulatory regime; (v) Management and capital allocation — track record on R&D ROI, M&A, buybacks, insider alignment; (vi) Financial model summary — 5-year P&L, FCF bridge, balance sheet, key KPIs; (vii) Valuation — primary method with cross-checks; (viii) Catalysts — next 6, 12, 24 months with probabilities; (ix) Risks — ranked, with monitoring metrics; (x) Engagement plan — questions for management, expert network priorities, KOL diligence list. Leave numbered placeholders [TBD-1, TBD-2…] for primary research.
```

---

### INIT-03  Variant Perception Generator

```yaml
id: INIT-03
title: Variant Perception Generator
tags: [#initiation, #thesis, #cross-sector, #sell-side, #pm-level, #senior-judgment]
use_when: "When consensus is well-formed and you need to identify where you can have a differentiated view."
reasoning: "catalogue consensus → identify variance → hypothesise variant → falsify"
inputs: "Consensus summary or 3–5 sell-side notes; current price target distribution."
output: "Structured matrix followed by ranked top-three list with falsification tests."
```

**Reasoning scaffold:** catalogue consensus → identify variance → hypothesise variant → falsify

**Prompt:**
```
I am initiating on [TICKER]. Below is the consensus view from the most recent five sell-side notes. Act as an adversarial adjudicator — refuse to simply average the bull and bear cases or split the difference. For each dimension — (a) revenue growth trajectory, (b) gross margin durability, (c) opex leverage, (d) terminal value assumptions, (e) competitive intensity, (f) regulatory or reimbursement risk, (g) management quality — state: the consensus assumption, the strongest contrary view I could defend, the specific evidence required, and where I would source it. Categorise each bear argument into structural vulnerabilities vs theoretical vulnerabilities lacking empirical support. Rank dimensions by price-target impact. End with the top three variant perceptions and the falsification test for each.
```

---

### INIT-04  Industry Primer in 90 Minutes

```yaml
id: INIT-04
title: Industry Primer in 90 Minutes
tags: [#initiation, #thematic, #cross-sector, #reasoning-only, #junior-task]
use_when: "When entering an unfamiliar sub-segment and you need a working model of the industry."
reasoning: "map industry → catalogue players → benchmark → identify levers"
inputs: "Segment name; optionally a recent industry conference deck."
output: "Long-form primer, 1,500–2,500 words, written as prose."
```

**Reasoning scaffold:** map industry → catalogue players → benchmark → identify levers

**Prompt:**
```
Write a primer on the [sub-segment, e.g. CDMO, CGM, PBM, ADC bioconjugation, NGS instruments] industry as if briefing a new buy-side analyst with healthcare fluency but no segment-specific background. Cover: (1) what the industry does and where it sits in the value chain; (2) unit economics of a typical participant — gross margins, capital intensity, cash conversion, working capital quirks; (3) two or three structural growth drivers and what could break them; (4) competitive structure and how it has evolved; (5) regulatory and reimbursement regime and the most plausible policy shocks; (6) listed pure-plays, diversified players with material exposure, and key private competitors; (7) the three pieces of jargon that signal someone actually understands the space.
```

---

### INIT-05  Bull / Base / Bear Decomposition with Probability Weights

```yaml
id: INIT-05
title: Bull / Base / Bear Decomposition with Probability Weights
tags: [#initiation, #modeling, #thesis, #cross-sector, #senior-judgment]
use_when: "When constructing the formal scenario set for a price target, avoiding mechanical interpolation."
reasoning: "frame scenarios → quantify paths → weight probabilities → decide"
inputs: "Current operating model, base assumptions, consensus PT range."
output: "Structured scenario matrix with probability-weighted PT and sensitivity note."
```

**Reasoning scaffold:** frame scenarios → quantify paths → weight probabilities → decide

**Prompt:**
```
For [TICKER], construct three scenarios — bull, base, bear — that are qualitatively distinct rather than linear interpolations. Each must be driven by a different dominant causal mechanism. For each: (1) dominant mechanism in one sentence; (2) three to five operational assumptions; (3) 5-year P&L sketch; (4) appropriate valuation method and equity value per share; (5) subjective probability with reasoning, ensuring the residual ‘unknown unknown’ bucket is not zero; (6) leading indicator that would shift probability weighting. End with a probability-weighted PT and a flag if the modal scenario differs materially from the weighted average.
```

---

### INIT-06  Biotech-Specific Initiation Layer

```yaml
id: INIT-06
title: Biotech-Specific Initiation Layer
tags: [#initiation, #biotech, #ctgov, #fda-ema, #pubmed, #senior-judgment]
use_when: "When initiating on a clinical-stage biotech and the standard template needs the science layer."
reasoning: "map pipeline → risk-weight assets → bridge to valuation → recommend"
inputs: "Pipeline page, investor deck, ClinicalTrials.gov entries, recent abstracts."
output: "Structured clinical layer, 1,500–2,500 words."
```

**Reasoning scaffold:** map pipeline → risk-weight assets → bridge to valuation → recommend

**Prompt:**
```
I am initiating on [TICKER], a clinical-stage biotech with a lead asset in [indication, mechanism]. Build the science and clinical layer: (1) mechanism of action at generalist PM level; (2) standard of care, unmet need quantified, realistic addressable population; (3) competitive landscape — every asset in development ranked by stage and probability; (4) lead asset’s clinical package — trial design, endpoints, readouts, statistical robustness, criticisms a short would raise; (5) next two readouts with timing and quantitative success thresholds (note: ~70% of Phase II and ~50% of Phase III trials fail to meet primary endpoints — use indication-specific rates where available); (6) regulatory pathway — Breakthrough, Fast Track, Priority Review, AdCom likelihood, PDUFA; (7) probability of success using transparent decomposition (technical PoS × regulatory PoS × commercial PoS).
```

---

### INIT-07  Medtech-Specific Initiation Layer

```yaml
id: INIT-07
title: Medtech-Specific Initiation Layer
tags: [#initiation, #medtech, #cms, #ir-materials, #senior-judgment]
use_when: "When initiating on a medical device or capital equipment company."
reasoning: "decompose device → reimbursement-test → unit-economics → conclude"
inputs: "Company filings, IR deck, reimbursement schedule, peer notes."
output: "Structured layer, 1,200–2,000 words."
```

**Reasoning scaffold:** decompose device → reimbursement-test → unit-economics → conclude

**Prompt:**
```
Build the procedure, reimbursement, and adoption layer for [TICKER] with primary exposure to [device category]. Cover: (1) procedure or use case — patient pathway, decision-maker, site of service, competing options; (2) US reimbursement — CPT codes, ICD-10, CMS payment rates (OPPS, ASC, physician fee schedule), prior auth, pending NCD/LCD changes; (3) ex-US reimbursement; (4) adoption curve — penetration, pace by site, bottleneck; (5) capital equipment dynamics if relevant — placement model, installed base, utilisation, consumables pull-through; (6) competitive set ranked by share and evidence; (7) three operational KPIs the company will be judged on quarterly.
```

---

## 2. Earnings Workflows — Preview, Live, and Post

*Prompts for the earnings cycle, from preview note to live-call triage to post-print thesis update.*

### EARN-01  Earnings Preview Note (T-7)

```yaml
id: EARN-01
title: Earnings Preview Note (T-7)
tags: [#earnings-preview, #cross-sector, #sell-side, #transcripts, #senior-judgment]
use_when: "Seven days ahead of a print."
reasoning: "parse consensus → identify swing factors → pre-commit scenarios → set prep"
inputs: "Prior four transcripts, consensus, my model, sell-side notes, options data."
output: "Preview note, 1,000–1,500 words, with pre-commit action plan."
```

**Reasoning scaffold:** parse consensus → identify swing factors → pre-commit scenarios → set prep

**Prompt:**
```
Build an earnings preview for [TICKER] for [Q quarter year]. Structure: (1) consensus snapshot — top-line, segments, margins, EPS, key KPIs; (2) my model vs consensus with deltas and drivers; (3) buy-side whisper from sell-side tone; (4) three questions the print must answer for thesis; (5) anticipated management tone based on prior four prints; (6) trade setup — historical reaction, IV vs realised, asymmetry; (7) action plan — add / trim / exit triggers.
```

---

### EARN-02  Buy-Side KPI Tracker Build

```yaml
id: EARN-02
title: Buy-Side KPI Tracker Build
tags: [#earnings-preview, #cross-sector, #sec-filings, #transcripts, #junior-task]
use_when: "When systematising operational metrics beyond headline P&L."
reasoning: "pre-read prior quarters → prioritise KPIs → anticipate tone → stage follow-ups"
inputs: "Eight quarters of releases and transcripts; investor day decks."
output: "KPI table with 12-quarter rolling view and narrative on KPI selection."
```

**Reasoning scaffold:** pre-read prior quarters → prioritise KPIs → anticipate tone → stage follow-ups

**Prompt:**
```
Build a KPI tracker for [TICKER] covering last 8 quarters and forecasting next 4. Identify 8–12 operational KPIs that drive the thesis. For each: define precisely, source from disclosure, show trend, note disclosure changes, forecast with reasoning. Flag KPIs the company has stopped disclosing.
```

---

### EARN-03  Live-Call Triage Sheet

```yaml
id: EARN-03
title: Live-Call Triage Sheet
tags: [#earnings-post, #cross-sector, #transcripts, #senior-judgment]
use_when: "On the call itself, to structure live note-taking."
reasoning: "compare actuals → diagnose drivers → assess management tone → update model"
inputs: "My preview note; prior transcripts."
output: "One-page triage sheet."
```

**Reasoning scaffold:** compare actuals → diagnose drivers → assess management tone → update model

**Prompt:**
```
Generate a live-call triage sheet for [TICKER]’s [Q] call. Four columns: thesis question (top 5), management answer (blank), tone read, thesis impact. Add ‘red flag word list’ (8–10 phrases). Q&A section: 3–4 sell-side analysts likely to ask well, what they’ll ask, surprising answer.
```

---

### EARN-04  Post-Print Thesis Update Memo

```yaml
id: EARN-04
title: Post-Print Thesis Update Memo
tags: [#earnings-post, #cross-sector, #transcripts, #sec-filings, #senior-judgment]
use_when: "Within 24 hours of a print."
reasoning: "reconstruct pillars → apply outcome → classify delta → recommend action"
inputs: "Release, transcript, preview note, KPI tracker, model."
output: "1,500-word memo with clear action."
```

**Reasoning scaffold:** reconstruct pillars → apply outcome → classify delta → recommend action

**Prompt:**
```
Post-print thesis update for [TICKER] following [Q]. (1) Result vs my expectation vs consensus; (2) earnings quality assessment; (3) management tone delta; (4) thesis verdict per pillar (confirmed/intact/weakened/broken); (5) model changes with new PT bridge; (6) action with justification; (7) lessons learned.
```

---

### EARN-05  Guide Decomposition and Path-to-Number Test

```yaml
id: EARN-05
title: Guide Decomposition and Path-to-Number Test
tags: [#earnings-post, #modeling, #cross-sector, #transcripts, #senior-judgment]
use_when: "When management has issued or revised guidance."
reasoning: "track guide deltas → triangulate sources → extract pattern → forecast next print"
inputs: "Guidance release, slides, transcript, prior guide history."
output: "Bridge tables with verdict and model recommendation."
```

**Reasoning scaffold:** track guide deltas → triangulate sources → extract pattern → forecast next print

**Prompt:**
```
Decompose [TICKER]’s [FY] guidance. (1) Top-line bridge by segment; (2) margin bridge; (3) capex and FCF; (4) historical guide-in vs deliver; (5) verdict — conservative/achievable/stretch; (6) model positioning.
```

---

### EARN-06  Biotech Quarterly Cash and Catalyst Refresh

```yaml
id: EARN-06
title: Biotech Quarterly Cash and Catalyst Refresh
tags: [#earnings-post, #biotech, #sec-filings, #ctgov, #senior-judgment]
use_when: "Each quarter for clinical-stage names."
reasoning: "isolate segment → attribute surprise → reconcile guide → update"
inputs: "Press release, 10-Q, MD&A, transcript, prior catalyst calendar."
output: "Cash bridge, catalyst table, financing scenarios."
```

**Reasoning scaffold:** isolate segment → attribute surprise → reconcile guide → update

**Prompt:**
```
Refresh cash and catalyst for [TICKER] following [Q]. (1) Cash position with runway to named catalyst. Distinguish gross burn (total operating cash spent) from net burn (after collaborative revenue). (2) Burn quality — R&D by programme, G&A, non-cash. (3) Catalyst calendar — next 18 months, flag slippage. (4) Financing risk — equity raise, royalty, partnership scenarios. (5) Pipeline prioritisation signal.
```

---

### EARN-07  Managed Care MLR Bridge

```yaml
id: EARN-07
title: Managed Care MLR Bridge
tags: [#earnings-post, #services-payors, #sec-filings, #cms, #senior-judgment]
use_when: "Each quarter for payors where MLR is the central driver."
reasoning: "parse transcript → detect language shifts → quantify tone → signal-flag"
inputs: "Release, supplement, transcript, prior-year prints."
output: "MLR bridge, drivers, forward-look, peer cross-read."
```

**Reasoning scaffold:** parse transcript → detect language shifts → quantify tone → signal-flag

**Prompt:**
```
MLR bridge for [TICKER] for [Q]. (1) MLR by segment vs prior year/consensus; (2) drivers — utilisation, unit cost, mix, prior period, one-offs; (3) risk adjustment dynamics (RADV, V28, Stars); (4) forward colour; (5) full-year guide implication; (6) peer cross-read.
```

---

## 3. Management Meeting Prep

*Prompts for 1-on-1s, conferences, site visits, and KOL events. Make every question earn its 30-minute slot.*

### MGMT-01  1-on-1 Question Stack

```yaml
id: MGMT-01
title: 1-on-1 Question Stack
tags: [#mgmt-meeting, #cross-sector, #transcripts, #sec-filings, #senior-judgment]
use_when: "Before a 30–45 minute 1-on-1 with management."
reasoning: "tier questions → anticipate evasion → design follow-ups → score answers"
inputs: "Last four transcripts, conference appearances, thesis memo."
output: "Three-tier question stack with follow-up scripts."
```

**Reasoning scaffold:** tier questions → anticipate evasion → design follow-ups → score answers

**Prompt:**
```
Build a tiered question stack for a 30-minute meeting with [TICKER]’s [role]. Tier 1 (must-ask, 5) — thesis-moving, hard to deflect. Tier 2 (good-to-ask, 5) — competitive/capital allocation tests. Tier 3 (colour, 5) — culture, talent, leading indicators. For Tier 1: exact wording, boilerplate answer, follow-up, informative answer. Avoid questions with public answers.
```

---

### MGMT-02  What Has Already Been Asked? Filter

```yaml
id: MGMT-02
title: What Has Already Been Asked? Filter
tags: [#mgmt-meeting, #cross-sector, #transcripts, #junior-task]
use_when: "To avoid burning meeting time on already-answered questions."
reasoning: "compare transcripts → detect language drift → surface to model → flag signal"
inputs: "Draft questions; transcripts."
output: "Question-by-question audit table."
```

**Reasoning scaffold:** compare transcripts → detect language drift → surface to model → flag signal

**Prompt:**
```
For each of my draft questions, search last four earnings calls and three conference appearances: (1) has it been asked; (2) management answer; (3) specific or hand-wave; (4) re-frame or drop.
```

---

### MGMT-03  Site Visit Brief

```yaml
id: MGMT-03
title: Site Visit Brief
tags: [#mgmt-meeting, #cross-sector, #sec-filings, #senior-judgment]
use_when: "Before a manufacturing site visit, R&D centre tour, or hospital site visit."
reasoning: "structure call → track signals → capture commitments → assign ownership"
inputs: "Site location, capex announcements, quality history."
output: "One-page brief with post-visit template."
```

**Reasoning scaffold:** structure call → track signals → capture commitments → assign ownership

**Prompt:**
```
Build a brief for visiting [TICKER]’s [site]. (1) What official agenda looks like and what they won’t show; (2) five operational tells; (3) three questions for site lead; (4) safety/quality/culture signals; (5) post-visit synthesis template.
```

---

### MGMT-04  KOL Day / Capital Markets Day Pre-Read

```yaml
id: MGMT-04
title: KOL Day / Capital Markets Day Pre-Read
tags: [#mgmt-meeting, #biotech, #pharma, #medtech, #ir-materials, #senior-judgment]
use_when: "Before a KOL day, R&D day, or capital markets day."
reasoning: "debrief capture → extract decision-useful → update thesis → store for audit"
inputs: "Agenda, prior materials, KOL bios."
output: "Pre-read brief, 1,000–1,500 words."
```

**Reasoning scaffold:** debrief capture → extract decision-useful → update thesis → store for audit

**Prompt:**
```
Pre-read for [TICKER]’s [event] on [date]. (1) Agenda mapped to thesis; (2) prior precedent credibility scorecard; (3) expected new disclosures with ranges; (4) featured KOLs — bios, conflicts, questions; (5) peer cross-reads; (6) one-page note plan.
```

---

## 4. Modeling and Valuation

*Prompts for building, stress-testing, and cross-checking financial models with healthcare-specific methodologies.*

### MOD-01  DCF Stress Test and Reverse-Engineer

```yaml
id: MOD-01
title: DCF Stress Test and Reverse-Engineer
tags: [#modeling, #cross-sector, #senior-judgment]
use_when: "When you have a working DCF and need to know what the market prices."
reasoning: "decompose revenue → build KPI bridge → stress-test → link to thesis"
inputs: "DCF assumptions."
output: "Stress-test summary, market-implied scenario, prioritised diligence task."
```

**Reasoning scaffold:** decompose revenue → build KPI bridge → stress-test → link to thesis

**Prompt:**
```
I will paste my DCF assumptions for [TICKER]. (1) Stress-test: three most sensitive assumptions, aggressive vs mid-point positioning, terminal value share sanity check. (2) Reverse-engineer current price: what terminal margin and growth is the market pricing, is it internally consistent? End with the single assumption to pressure-test.
```

---

### MOD-02  Sum-of-the-Parts for Diversified Pharma or Medtech

```yaml
id: MOD-02
title: Sum-of-the-Parts for Diversified Pharma or Medtech
tags: [#modeling, #pharma, #medtech, #senior-judgment]
use_when: "For diversified large-caps where consolidated multiples obscure segment value."
reasoning: "benchmark margins → calibrate trajectory → sensitivity-test → conclude"
inputs: "Segment disclosure, peer multiples, balance sheet."
output: "SOTP table with discount commentary and divestiture optionality."
```

**Reasoning scaffold:** benchmark margins → calibrate trajectory → sensitivity-test → conclude

**Prompt:**
```
Build SOTP for [TICKER]. (1) Natural segments with proposed analytical split; (2) 5-year forecast per segment with peer-derived multiples; (3) balance sheet adjustments; (4) per-share value and conglomerate discount; (5) divestiture optionality; (6) sensitivity.
```

---

### MOD-03  Risk-Adjusted NPV (rNPV) Model for a Biotech Asset

```yaml
id: MOD-03
title: Risk-Adjusted NPV (rNPV) Model for a Biotech Asset
tags: [#modeling, #biotech, #ctgov, #fda-ema, #pubmed, #senior-judgment]
use_when: "When valuing a single drug asset or building a clinical-stage biotech sum-of-pipelines."
reasoning: "asset-by-asset rNPV → probability-weight → aggregate → triangulate to EV"
inputs: "Asset details, epidemiology, comparable launches."
output: "Full rNPV with funnel, P&L, PoS, DCF, sensitivities."
```

**Reasoning scaffold:** asset-by-asset rNPV → probability-weight → aggregate → triangulate to EV

**Prompt:**
```
Build rNPV for [asset] in [indication]. (1) Patient funnel; (2) pricing by geography; (3) peak sales and time to peak; (4) COGS, R&D, SG&A, royalties; (5) LOE timing and decay; (6) PoS decomposition (phase transition × regulatory × commercial) with BIO/PhRMA base rates; (7) discount rate; (8) rNPV per share with PoS and peak share sensitivity.
```

---

### MOD-04  Patent Cliff and LOE Bridge for Large-Cap Pharma

```yaml
id: MOD-04
title: Patent Cliff and LOE Bridge for Large-Cap Pharma
tags: [#modeling, #pharma, #sec-filings, #senior-judgment]
use_when: "For mature pharma where LOE vs pipeline replenishment drives the next decade."
reasoning: "model LOE erosion → map launch offsets → bridge revenue → reconcile guidance"
inputs: "10-K product disclosures, pipeline page, sell-side LOE notes."
output: "LOE bridge by year, pipeline contribution, gap-to-consensus."
```

**Reasoning scaffold:** model LOE erosion → map launch offsets → bridge revenue → reconcile guidance

**Prompt:**
```
LOE bridge for [TICKER] 2025–2032. (1) Each franchise >5% revenue: molecule, revenue, LOE date, post-LOE trajectory (SM: 80–90% loss in 18 months; biologics: 30–50% over 3–5 years); (2) at-risk revenue by year; (3) pipeline contribution bridge; (4) organic revenue trajectory; (5) gap-to-consensus; (6) M&A burden.
```

---

### MOD-05  Medtech Razor-Blade Model

```yaml
id: MOD-05
title: Medtech Razor-Blade Model
tags: [#modeling, #medtech, #sec-filings, #senior-judgment]
use_when: "For capital equipment + consumables companies."
reasoning: "separate razor from blade → sensitise installed base → unit economics → conclude"
inputs: "Installed base history, placement guidance, consumables disclosure, peer benchmarks."
output: "Two-engine forecast with sensitivity."
```

**Reasoning scaffold:** separate razor from blade → sensitise installed base → unit economics → conclude

**Prompt:**
```
Razor-blade model for [TICKER]. Benchmark: mature razor/blade models target 65–70% gross margin vs 50–60% for capital-equipment-only. (1) Installed base build; (2) utilisation trend; (3) placement forecast; (4) consumables forecast; (5) mix shift and margin trajectory; (6) sensitivity to placement slowdown vs utilisation drop; (7) cross-check vs management target.
```

---

### MOD-06  Tools and Diagnostics Capex-Cycle Model

```yaml
id: MOD-06
title: Tools and Diagnostics Capex-Cycle Model
tags: [#modeling, #tools-dx, #sec-filings, #senior-judgment]
use_when: "For life sciences tools where end-market capex cycles drive instrument revenue."
reasoning: "parse SaaS KPIs → stress-test retention → unit economics → valuation framework"
inputs: "End-market disclosure, NIH outlook, biotech funding, peer commentary."
output: "End-market forecast feeding revenue split."
```

**Reasoning scaffold:** parse SaaS KPIs → stress-test retention → unit economics → valuation framework

**Prompt:**
```
End-market capex cycle model for [TICKER]. (1) Revenue by end-market; (2) cycle drivers and indicators per end-market; (3) forecast with indicator linkage; (4) instrument/consumables/services split; (5) margin mix consequence; (6) peak-to-trough sensitivity.
```

---

### MOD-07  MA Star Ratings and Bid Cycle Model

```yaml
id: MOD-07
title: MA Star Ratings and Bid Cycle Model
tags: [#modeling, #services-payors, #cms, #senior-judgment]
use_when: "For Medicare Advantage operators."
reasoning: "MA bid mechanics → scenario rates → Stars impact → multiple translation"
inputs: "CMS Stars, rate notice, segment detail, bid commentary."
output: "Plan-year-forward model with sensitivities."
```

**Reasoning scaffold:** MA bid mechanics → scenario rates → Stars impact → multiple translation

**Prompt:**
```
MA Star/bid cycle model for [TICKER]. (1) Membership by contract with Stars; (2) quality bonus exposure; (3) bid cycle dynamics (V28, IRA Part D, benchmark); (4) member growth scenarios; (5) revenue and MLR for next two plan years; (6) Stars and utilisation stress tests; (7) peer comparison.
```

---

### MOD-08  Digital Health Unit Economics Stress Test

```yaml
id: MOD-08
title: Digital Health Unit Economics Stress Test
tags: [#modeling, #digital-health, #sec-filings, #senior-judgment]
use_when: "For digital health names where unit economics at scale are questioned."
reasoning: "cohort separation → retention analysis → contribution margin → multiple"
inputs: "Cohort disclosures, S-1, investor day decks, peer benchmarks."
output: "Per-unit P&L, CAC/LTV table, FCF path, short-thesis pressure point."
```

**Reasoning scaffold:** cohort separation → retention analysis → contribution margin → multiple

**Prompt:**
```
Stress-test unit economics for [TICKER]. (1) Per-unit P&L; (2) CAC by channel with payback; (3) LTV with retention and expansion; (4) LTV/CAC by cohort — flag below the 3:1 sustainability threshold; (5) path to FCF; (6) reality check vs SaaS/consumer health comps; (7) smart short’s first attack.
```

---

### MOD-09  Working Capital and Cash Conversion Forensics

```yaml
id: MOD-09
title: Working Capital and Cash Conversion Forensics
tags: [#modeling, #cross-sector, #sec-filings, #senior-judgment]
use_when: "When FCF conversion is deteriorating or quality issues are suspected."
reasoning: "DCF construct → comp triangulate → decide anchor → sensitivity"
inputs: "12 quarters of 10-Qs and 10-Ks, cash flow statements, footnotes."
output: "Working capital walk, divergence map, quality verdict."
```

**Reasoning scaffold:** DCF construct → comp triangulate → decide anchor → sensitivity

**Prompt:**
```
Working capital forensics on [TICKER] for 12 quarters. (1) DSO, DIO, DPO, cash conversion cycle; (2) FCF/NI vs 5-year average with divergence flags; (3) plausible explanations for divergences; (4) MD&A and footnote cross-check; (5) earnings quality verdict.
```

---

### MOD-10  Scenario Construction as a Discipline

```yaml
id: MOD-10
title: Scenario Construction as a Discipline
tags: [#modeling, #thesis, #cross-sector, #senior-judgment, #pm-level]
use_when: "When the analyst needs to build scenarios for a decision (valuation, hedge construction, position sizing) and wants to avoid the default failure modes of linear interpolation and missed-scenario bias."
reasoning: "frame decision → generate mechanisms → audit missing scenarios → probability-weight → decide"
inputs: "Decision to be made; current consensus and market-implied positioning; relevant operational, competitive, regulatory and macro context."
output: "Scenario set with distinct mechanisms, calibrated probabilities, early signals, and a decision rule."
```

**Reasoning scaffold:** frame decision → generate mechanisms → audit missing scenarios → probability-weight → decide

**Prompt:**
```
Teach me to construct scenarios for [TICKER / decision] as a discipline, not just an output. (1) Decision frame — state the decision the scenarios must serve (set a price target; size a position; construct a hedge; assess portfolio fit). The number of scenarios should match the decision: two for binary (hedge or no hedge), three or four for sizing, more only if decision resolution requires it. (2) Mechanism-distinct generation — for each scenario, state the single dominant causal mechanism in one sentence. Two scenarios with the same mechanism operating at different magnitudes are not two scenarios; they are one scenario with a sensitivity band. (3) Missing-scenario audit — before accepting the scenario set, explicitly ask: what scenario would a smart short describe that I have not included? What scenario would a long-duration holder describe? What scenario does the options market appear to be pricing that I have not articulated? Any scenario identified here and absent from my set is evidence of a blind spot. (4) Probability discipline — assign probabilities that sum to 1.00 with a residual ‘unknown unknown’ bucket of at least 5 per cent. If the residual is zero, the scenario set is overconfident. Use round numbers (e.g. 40 / 30 / 20 / 10) rather than false-precision decimals. (5) Early-signal identification — for each scenario, the single operational or market signal that, if observed, would cause me to shift probability mass toward it. This is what makes scenarios actionable rather than academic. (6) Decision rule — state in advance how the probability-weighted output maps to the decision, so the decision is made by the analysis rather than re-made after the fact. (7) Premortem — if the scenario I am weighting least turns out to be correct, what failure in my generator allowed me to underweight it? End with the scenario set, probabilities, early signals, decision, and confidence score.
```

---

## 5. Thesis Development and Pressure-Testing

*Prompts for sharpening, attacking, and defending an investment thesis. The goal is to be right, not confirmed.*

### THES-01  Pre-Mortem on a Long Thesis

```yaml
id: THES-01
title: Pre-Mortem on a Long Thesis
tags: [#thesis, #cross-sector, #senior-judgment, #pm-level]
use_when: "Before sizing up or initiating a long."
reasoning: "pre-mortem → identify break conditions → monitor signals → pre-commit action"
inputs: "Thesis memo and entry rationale."
output: "Three-path failure map with monitoring signals."
```

**Reasoning scaffold:** pre-mortem → identify break conditions → monitor signals → pre-commit action

**Prompt:**
```
Imagine 24 months from today the long thesis on [TICKER] has failed — stock down 40%. Write the post-mortem. (1) Three most likely paths to failure; (2) operational signals in months 3–9; (3) disconfirming question for each quarterly check-in; (4) re-underwrite trigger level. Favour name-specific failure modes.
```

---

### THES-02  Steel-Man the Short Case

```yaml
id: THES-02
title: Steel-Man the Short Case
tags: [#thesis, #risk, #cross-sector, #sell-side, #senior-judgment]
use_when: "When the bull case feels obvious."
reasoning: "crowding audit → contrarian test → re-underwrite → action"
inputs: "Long thesis; short reports if any."
output: "Steel-manned short memo, 800–1,200 words."
```

**Reasoning scaffold:** crowding audit → contrarian test → re-underwrite → action

**Prompt:**
```
I am long [TICKER] with thesis [paste]. Steel-man the short as if running a tactical short book. (1) Central mechanism in two sentences; (2) supporting data ranked by recency; (3) catalysts for downward revision; (4) time horizon and holding cost; (5) bull response and rebuttal — two layers deep; (6) 90-day evidence to look for. Demand mechanism, not valuation alone.
```

---

### THES-03  Thesis Decomposition into Testable Claims

```yaml
id: THES-03
title: Thesis Decomposition into Testable Claims
tags: [#thesis, #cross-sector, #senior-judgment]
use_when: "When a thesis feels right but you cannot articulate falsification."
reasoning: "articulate variant → test falsifiability → size commit → monitor"
inputs: "Thesis memo."
output: "Claim-by-claim decomposition with bias flags."
```

**Reasoning scaffold:** articulate variant → test falsifiability → size commit → monitor

**Prompt:**
```
Decompose thesis on [TICKER] into claims. For each: (1) one-sentence claim; (2) classify as factual/forecast/judgment; (3) confirmation source; (4) leading indicator and change threshold; (5) alternative judgments; (6) load-bearing rank; (7) claims asserted without basis — that’s where bias hides.
```

---

### THES-04  Regime Map Stress Test

```yaml
id: THES-04
title: Regime Map Stress Test
tags: [#thesis, #thematic, #cross-sector, #pm-level, #senior-judgment]
use_when: "When thesis depends on macro or policy regime continuity."
reasoning: "map regimes → probability-weight → hedge construct → monitor transition"
inputs: "Thesis, sub-sector context, macro environment."
output: "Regime matrix with exit triggers."
```

**Reasoning scaffold:** map regimes → probability-weight → hedge construct → monitor transition

**Prompt:**
```
Regime map for [TICKER]. Define 4 distinct world-states, each with a different dominant mechanism. For each: probability, 3-year path, equity value, early signal. Do NOT assign ‘wins in every scenario’. End with probability-weighted value and the regime forcing exit.
```

---

### THES-05  Disconfirming Evidence Search Plan

```yaml
id: THES-05
title: Disconfirming Evidence Search Plan
tags: [#thesis, #risk, #cross-sector, #expert-network, #senior-judgment]
use_when: "When formalising the search for evidence against your thesis."
reasoning: "audit thesis → refresh pillars → identify staleness → action"
inputs: "Thesis claims, expert network coverage, subscriptions."
output: "30-day calendar with prioritisation."
```

**Reasoning scaffold:** audit thesis → refresh pillars → identify staleness → action

**Prompt:**
```
30-day disconfirmation plan for [TICKER]. Top 5 claims: (1) falsifying evidence type; (2) source; (3) cost; (4) prioritisation. Output a 30-day calendar with escalation rule.
```

---

## 6. Sell Discipline and Risk Monitoring

*Prompts for knowing when to exit, when to add, and what would break the thesis.*

### SELL-01  Sell Discipline Scorecard

```yaml
id: SELL-01
title: Sell Discipline Scorecard
tags: [#sell-discipline, #risk, #cross-sector, #pm-level]
use_when: "Quarterly review of every name against a consistent exit framework."
reasoning: "define triggers → set thresholds → pre-commit actions → operationalise"
inputs: "Thesis, recent prints, peer comparison, entry memo."
output: "Six-line scorecard with verdict."
```

**Reasoning scaffold:** define triggers → set thresholds → pre-commit actions → operationalise

**Prompt:**
```
Scorecard for [TICKER]. Score 0–3: (1) thesis intact; (2) execution; (3) competitive trend; (4) valuation vs entry; (5) better alternatives; (6) conviction calibration — am I in love with the story? Sum: 14–18 hold/add, 9–13 trim, <9 exit-by-default.
```

---

### SELL-02  Thesis-Breaking Signal Watchlist

```yaml
id: SELL-02
title: Thesis-Breaking Signal Watchlist
tags: [#sell-discipline, #risk, #cross-sector, #senior-judgment]
use_when: "After establishing a position, to lock in disconfirming signals before drift."
reasoning: "score positions → quarterly audit → detect exceptions → trigger review"
inputs: "Thesis, KPIs, competitive set, regulatory calendar."
output: "Categorised watchlist with pre-committed actions."
```

**Reasoning scaffold:** score positions → quarterly audit → detect exceptions → trigger review

**Prompt:**
```
Watchlist for [TICKER]. 8–10 signals by category: (1) fundamental KPI thresholds; (2) competitive events; (3) regulatory decisions; (4) management behavioural signals; (5) market structure. For each: threshold, source, frequency, pre-committed action.
```

---

### SELL-03  Position Sizing Sanity Check

```yaml
id: SELL-03
title: Position Sizing Sanity Check
tags: [#portfolio, #risk, #cross-sector, #pm-level]
use_when: "Before adding or doubling down."
reasoning: "attribute performance → pattern-detect errors → update rules → commit"
inputs: "Sizing, portfolio context, scenarios, factor exposures."
output: "Sizing recommendation with reasoning."
```

**Reasoning scaffold:** attribute performance → pattern-detect errors → update rules → commit

**Prompt:**
```
Test sizing for [TICKER]. (1) Expected 12-month return and implied Sharpe; (2) marginal correlation to top 5; (3) drawdown at bear case; (4) information vs mood driver; (5) 90-day justification forward. Clear recommendation.
```

---

### SELL-04  Single-Name Thesis Post-Mortem

```yaml
id: SELL-04
title: Single-Name Thesis Post-Mortem
tags: [#sell-discipline, #post-mortem, #cross-sector, #senior-judgment, #pm-level]
use_when: "After exiting a position at a loss, holding a winner past the thesis horizon, or any outcome where the outcome materially differed from the original thesis. Run within two weeks of exit while details are still fresh."
reasoning: "reconstruct thesis → classify error → extract lesson → update framework"
inputs: "Original initiation or entry memo; complete holding-period timeline including earnings prints and catalysts; exit rationale if documented; original KPI tracker; sell discipline scorecard updates during the holding period."
output: "Structured post-mortem with error classification, transferable lesson, and sell discipline framework update."
```

**Reasoning scaffold:** reconstruct thesis → classify error → extract lesson → update framework

**Prompt:**
```
Conduct a thesis post-mortem on [TICKER], exited on [date] at [price] after [entry price, holding period]. The goal is not to assign blame but to extract transferable lessons. (1) Original thesis reconstruction — pull the initiation memo or entry rationale verbatim. Do not rewrite with hindsight. State the thesis pillars, the variant perception, the catalysts relied upon, the risks I acknowledged, and the position size and rationale. (2) What actually happened — a factual timeline of operational events (earnings prints, catalysts, management changes, competitive developments) and share-price reaction during the holding period. Separate price action from fundamentals. (3) Pillar-by-pillar verdict — for each original thesis pillar, mark as confirmed, intact but irrelevant (true but did not drive the stock), weakened, broken, or untested. The ‘intact but irrelevant’ category is the most important diagnostic — it identifies the thesis claim that was correct in substance but wrong in thesis relevance. (4) Error classification — place the outcome into one of five categories: (a) thesis was wrong in substance (my analysis of the business was incorrect); (b) thesis was correct but the market cared about different things (variant perception was right but immaterial); (c) thesis was correct but timing was wrong (horizon mismatch); (d) sizing was wrong for the conviction level (risk-reward was mispriced relative to my own expressed view); (e) process error (I did not follow my own sell discipline signals). Each category implies a different lesson. (5) Signal forensics — identify the one operational or market signal that, if I had noticed it in real time, would have forced a different decision. Where was it disclosed? Was it in my KPI tracker? Did I see it and dismiss it? (6) Transferable lesson — state in one sentence the rule I will apply to similar situations in the future. The rule must be operational (‘when MLR exceeds X, I will re-underwrite’) rather than aspirational (‘I will be more disciplined’). (7) Update the sell discipline scorecard template — if the lesson implies a new signal to monitor or a new threshold to respect, encode it into SELL-02 for the rest of the book. End with confidence score and an honest note on whether the lesson generalises or is specific to this situation.
```

---

### SELL-05  Book-Wide Annual Post-Mortem and Process Audit

```yaml
id: SELL-05
title: Book-Wide Annual Post-Mortem and Process Audit
tags: [#sell-discipline, #post-mortem, #portfolio, #pm-level]
use_when: "Annually, ideally in January after the calendar year closes, to audit the year's decisions across the entire book rather than name-by-name."
reasoning: "aggregate post-mortems → cluster patterns → calibrate base rates → commit framework updates"
inputs: "Full year's worth of initiation memos, post-print notes, sell discipline scorecards, single-name post-mortems, and portfolio performance attribution."
output: "Year-end audit report with error pattern analysis, base rate updates, process discipline scorecard, and committed framework updates for the year ahead."
```

**Reasoning scaffold:** aggregate post-mortems → cluster patterns → calibrate base rates → commit framework updates

**Prompt:**
```
Conduct an annual post-mortem on my healthcare sleeve for [year]. The scope is the full book of positions, not any single name. (1) Performance attribution by decision type — decompose total return into: conviction positions held through volatility (top 5 names), opportunistic trades (positions held less than 90 days), hedges, shorts, and cash drag. Identify which decision categories added or subtracted value. (2) Error pattern recognition — review the single-name post-mortems from SELL-04 conducted during the year and cluster them. Are the errors concentrated in a particular decision category (e.g. I am consistently late to exit clinical-stage biotech after failed readouts), a particular sub-sector (e.g. my tools and diagnostics work is weaker than my biotech work), a particular market regime (e.g. I underperformed during risk-off periods), or a particular process failure (e.g. I override my own sell discipline scorecard too often)? (3) Base rate calibration — did the base rates I assumed (Phase III success at approximately 50 per cent, biosimilar uptake curves, MA bid cycle outcomes) hold in the actual year? Where they did not, update the base rates I apply going forward. (4) Process discipline scorecard — how often did I complete the full earnings workflow (EARN-01 through EARN-04) on my positions versus skipping steps? How often did I run the full sell discipline scorecard at quarter-end versus deferring? Process discipline is an input to performance; measure it directly. (5) Sizing audit — were my largest positions my highest-conviction positions in retrospect, or did sizing drift toward positions I had grown comfortable with rather than positions where the risk-reward was best? (6) External-to-me lessons — what happened in the year that I did not anticipate and could not reasonably have anticipated, versus what I should have anticipated but did not? The honest distinction between these two matters for confidence calibration. (7) Framework updates — for v[N+1] of my own process, what specifically changes in my watchlist thresholds, my sizing rules, my base rates, or my KPI tracker? Commit to the changes in writing. End with confidence score.
```

---

## 7. Sell-Side Synthesis and Triangulation

*Prompts for extracting differentiated signal from the wall of sell-side notes and transcripts.*

### SS-01  Multi-Broker Note Triangulation

```yaml
id: SS-01
title: Multi-Broker Note Triangulation
tags: [#sell-side-synth, #cross-sector, #sell-side, #senior-judgment]
use_when: "When 3+ notes drop on the same name."
reasoning: "aggregate broker views → detect consensus → identify fade-or-align → action"
inputs: "3–8 sell-side notes; my model."
output: "Triangulation note, 600–1,000 words."
```

**Reasoning scaffold:** aggregate broker views → detect consensus → identify fade-or-align → action

**Prompt:**
```
Triangulate [N] sell-side notes on [TICKER]. (1) Consensus map with dispersion; (2) differentiated takes per broker; (3) coverage gap; (4) reading priority; (5) source attribution. Extract signal, not paraphrase.
```

---

### SS-02  Initiation Note Decoder

```yaml
id: SS-02
title: Initiation Note Decoder
tags: [#sell-side-synth, #initiation, #cross-sector, #sell-side, #junior-task]
use_when: "When a sell-side initiation drops and you want the analytical core without 80 pages."
reasoning: "triangulate broker vs filings → identify gaps → build variant → falsify"
inputs: "Sell-side initiation PDF."
output: "One-page decoded summary."
```

**Reasoning scaffold:** triangulate broker vs filings → identify gaps → build variant → falsify

**Prompt:**
```
Distil initiation note on [TICKER]. (1) Central thesis in two sentences; (2) PT method and weakest assumption; (3) three differentiated insights; (4) three weakest claims; (5) unique data sources; (6) analyst rigour read; (7) what I’d push back on in 10 minutes.
```

---

### SS-03  Conference Call Cross-Read

```yaml
id: SS-03
title: Conference Call Cross-Read
tags: [#sell-side-synth, #earnings-post, #cross-sector, #transcripts, #senior-judgment]
use_when: "After a peer’s earnings call, to extract signal for your names."
reasoning: "map analyst biases → discount appropriately → use as triangulation → decide"
inputs: "Peer transcript; my ticker’s thesis."
output: "Cross-read note, 400–600 words."
```

**Reasoning scaffold:** map analyst biases → discount appropriately → use as triangulation → decide

**Prompt:**
```
[Peer] just reported. I cover [my ticker]. (1) Direct read-across; (2) indirect signals; (3) their view on my name; (4) one quote for my next update; (5) action recommendation.
```

---

## 8. Expert Network — Prep, Live, and Debrief

*Prompts for getting more out of the $1,500 per 60-minute expert call.*

### EN-01  Expert Call Prep Brief

```yaml
id: EN-01
title: Expert Call Prep Brief
tags: [#expert-network, #cross-sector, #senior-judgment]
use_when: "Before any expert network call."
reasoning: "hypothesise → design questions → elicit → triangulate"
inputs: "Expert profile; thesis question."
output: "Prep brief with MNPI-safe question stack."
```

**Reasoning scaffold:** hypothesise → design questions → elicit → triangulate

**Prompt:**
```
Prep brief for [60]-minute call with [expert background]. Working on [TICKER / thesis]. (1) 5 questions only this expert can credibly answer; (2) wrong vs right answer for each; (3) calibration question; (4) question order for candour; (5) follow-up if hand-wave; (6) adjacent question worth one slot. MNPI guardrail: flag questions that could elicit material non-public information and rephrase to stay within public or general industry knowledge.
```

---

### EN-02  Post-Call Debrief and Triangulation

```yaml
id: EN-02
title: Post-Call Debrief and Triangulation
tags: [#expert-network, #cross-sector, #senior-judgment]
use_when: "Within 24 hours of an expert call."
reasoning: "synthesise across calls → rank claims → re-underwrite → flag remaining gaps"
inputs: "Raw notes; thesis."
output: "Debrief memo, 600–1,000 words, with MNPI audit."
```

**Reasoning scaffold:** synthesise across calls → rank claims → re-underwrite → flag remaining gaps

**Prompt:**
```
Debrief from call on [TICKER / topic]. (1) 3–5 insights with confidence scores; (2) 1–2 surprises vs my prior; (3) gap analysis; (4) credibility scorecard; (5) thesis update; (6) next call to triangulate; (7) one anonymised quote for client comms. MNPI audit: flag any insight that appears to stem from non-public information for compliance review.
```

---

### EN-03  Expert Network Scoping Plan

```yaml
id: EN-03
title: Expert Network Scoping Plan
tags: [#expert-network, #cross-sector, #senior-judgment, #pm-level]
use_when: "When designing the expert network arc strategically."
reasoning: "compliance-check topic → frame question carefully → avoid MNPI → extract insight"
inputs: "Thesis sketch; budget; network coverage."
output: "8-week plan with sequencing and stop triggers."
```

**Reasoning scaffold:** compliance-check topic → frame question carefully → avoid MNPI → extract insight

**Prompt:**
```
Expert plan for [TICKER] over 8 weeks. (1) Map questions to expert profiles; (2) sequence for broad→specialist→thesis-specific; (3) budget and prioritisation; (4) conviction-shifting question per call; (5) stop trigger; (6) two calls for cross-triangulation.
```

---

### EN-04  Expert-Management Divergence Triangulation

```yaml
id: EN-04
title: Expert-Management Divergence Triangulation
tags: [#expert-network, #thesis, #cross-sector, #senior-judgment, #pm-level]
use_when: "When an expert network call surfaces information that contradicts or materially differs from management's public statements, and the analyst must decide which source to weight and how to act."
reasoning: "specify divergence → audit credibility → verify independently → pre-commit action"
inputs: "Expert call notes; relevant management statements (transcripts, slides, filings); any adjacent channel or alternative data."
output: "Divergence triangulation with credibility scores, verification path, pre-committed decision rule, and follow-up call design."
```

**Reasoning scaffold:** specify divergence → audit credibility → verify independently → pre-commit action

**Prompt:**
```
An expert call on [TICKER / topic] has surfaced information that diverges from management's public statements. Triangulate the divergence. (1) Specify the divergence precisely — what did the expert say, what has management said publicly (cite the specific call, slide, or filing), and in what dimension do they differ (fact, forecast, interpretation, sequencing)? Not all divergences are equivalent. (2) Expert credibility audit — how recent is the expert's direct experience? How specific is their claim (a concrete mechanism-level detail vs a general impression)? Is the claim within their verifiable scope of work or adjacent to it? Is the claim consistent with other independent data points I have gathered? Score the expert's claim on a 0–3 scale for recency, specificity, scope, and consistency. (3) Management incentive audit — what would management's incentive be to understate or overstate this specific dimension? Is the divergence in a direction consistent with known management tells (e.g. consistent under-promising on margin, consistent optimism on pipeline timing)? Prior guide-in vs deliver history matters here. (4) MNPI guardrail — if the expert's information would constitute material non-public information if sourced from management, I cannot act on it regardless of credibility. Flag this explicitly. If the divergence reflects the expert's opinion or synthesis of public information rather than non-public insider knowledge, it is tradeable. (5) Verification path — identify the independent data point that would confirm or refute the expert's claim without requiring another expert call. Channel data, competitor disclosure, regulatory filing, alternative data, or medical literature. Define the specific data and the threshold that would resolve the divergence. (6) Decision rule — in advance of verification, define what action the resolved divergence would trigger. If the expert is right, what do I do? If management is right, what do I do? Pre-committing to action prevents rationalisation after the fact. (7) Second expert call — design a follow-up call with a different expert whose scope of work could independently speak to the divergence, and specify the one question that would most efficiently resolve it. End with the action plan, the verification path, and the confidence score.
```

---

## 9. Screening — Quant and Qualitative

*Prompts for surfacing new ideas systematically with both Bloomberg/FactSet quant screens and qualitative thematic screens.*

### SCR-01  Bloomberg / FactSet Healthcare Idea Screen Builder

```yaml
id: SCR-01
title: Bloomberg / FactSet Healthcare Idea Screen Builder
tags: [#screen, #cross-sector, #bloomberg, #factset, #senior-judgment]
use_when: "When designing a screen with analytically grounded filters."
reasoning: "define criteria → filter universe → rank candidates → validate top names"
inputs: "Thesis or theme; syntax preferences."
output: "Screen design with triage process."
```

**Reasoning scaffold:** define criteria → filter universe → rank candidates → validate top names

**Prompt:**
```
Design a Bloomberg EQS or FactSet screen for [thesis]. (1) Universe; (2) 4–7 filter criteria with thresholds and reasoning; (3) field codes; (4) expected hit count and triage; (5) the one filter to loosen for long-tail ideas; (6) post-screen workflow.
```

---

### SCR-02  Catalyst Calendar Screen

```yaml
id: SCR-02
title: Catalyst Calendar Screen
tags: [#screen, #biotech, #fda-ema, #ctgov, #senior-judgment]
use_when: "Quarterly catalyst review for event-driven ideas."
reasoning: "build signal stack → validate components → rank opportunities → diligence next"
inputs: "Universe; ClinicalTrials.gov, FDA AdCom calendar."
output: "Calendar with prioritised idea list."
```

**Reasoning scaffold:** build signal stack → validate components → rank opportunities → diligence next

**Prompt:**
```
Catalyst calendar for next 6 months. Per catalyst: (1) ticker, asset, event type; (2) date window; (3) base rate; (4) prior data and success threshold; (5) implied vs fundamental move; (6) preliminary take; (7) top 5 for deeper work.
```

---

### SCR-03  Hidden Compounder Screen

```yaml
id: SCR-03
title: Hidden Compounder Screen
tags: [#screen, #cross-sector, #bloomberg, #senior-judgment, #pm-level]
use_when: "When generic quality screens are too crowded."
reasoning: "theme-filter → candidate-test → prioritise → add to watchlist"
inputs: "Universe; screening subscription."
output: "Ranked candidate list."
```

**Reasoning scaffold:** theme-filter → candidate-test → prioritise → add to watchlist

**Prompt:**
```
Design screen for ‘hidden compounders’. (1) 5-year organic CC growth >8%; (2) stable/expanding gross margin; (3) ROIC > WACC 4 of 5 years; (4) GPA > 0.20 to filter speculative pre-revenue; (5) exclude >40% M&A-driven growth; (6) capex/sales >4%; (7) insider >5%; (8) sell-side <10 analysts. Surface 8–12 names with one-line rationale.
```

---

### SCR-04  Thematic Beneficiary Screen

```yaml
id: SCR-04
title: Thematic Beneficiary Screen
tags: [#screen, #thematic, #cross-sector, #senior-judgment]
use_when: "When mapping a theme to listed-equity beneficiaries."
reasoning: "screen catalyst calendar → rank by event quality → score asymmetry → build book"
inputs: "Theme; transcripts; sector knowledge."
output: "Supply chain map, ranked basket, substantiation."
```

**Reasoning scaffold:** screen catalyst calendar → rank by event quality → score asymmetry → build book

**Prompt:**
```
Theme: [X]. Map supply chain. Per node: (1) value chain role; (2) listed exposure; (3) mechanism (volume, price, mix, share, optionality); (4) cost-bearer flag; (5) earnings call substantiation. Rank by pass-through quality. Candidate basket of 8–12 names.
```

---

### SCR-05  Activist Investor Target Screen

```yaml
id: SCR-05
title: Activist Investor Target Screen
tags: [#screen, #cross-sector, #sec-filings, #senior-judgment]
use_when: "When screening for potential activist targets in healthcare."
reasoning: "short-interest filter → borrow-cost check → asymmetry audit → prioritise"
inputs: "Screening data; 13D filings; proxy statements."
output: "Ranked list with playbook and uplift per name."
```

**Reasoning scaffold:** short-interest filter → borrow-cost check → asymmetry audit → prioritise

**Prompt:**
```
Screen for activist targets. Criteria: (1) market cap >$1B; (2) operating margin declining 3 years; (3) cash/investments >30% of EV; (4) R&D productivity below peer median; (5) exec comp disconnected from TSR; (6) board tenure >10 years or <3 independent with sector expertise; (7) recent 13D filings. Per hit: likely playbook and uplift estimate.
```

---

### SCR-06  13F Institutional Ownership Delta Scanner

```yaml
id: SCR-06
title: 13F Institutional Ownership Delta Scanner
tags: [#screen, #cross-sector, #sec-filings, #senior-judgment]
use_when: "Quarterly after 13F filings."
reasoning: "activist signal scan → target fit → outcome scenarios → position"
inputs: "13F data; my portfolio."
output: "Ownership delta table with conviction, contrarian, and crowding flags."
```

**Reasoning scaffold:** activist signal scan → target fit → outcome scenarios → position

**Prompt:**
```
Extract 13F data for top 20 healthcare funds. (1) Net buying/selling by name; (2) conviction signals (3+ funds initiating); (3) contrarian signals; (4) crowding risk (>40% of float); (5) my portfolio ownership delta.
```

---

### SCR-07  Cross-Sector Correlation Identifier

```yaml
id: SCR-07
title: Cross-Sector Correlation Identifier
tags: [#screen, #portfolio, #cross-sector, #bloomberg, #senior-judgment]
use_when: "When portfolio has hidden macro linkages."
reasoning: "ownership-delta screen → flow interpretation → thesis implication"
inputs: "Holdings; macro index data."
output: "Correlation matrix with scenario analysis."
```

**Reasoning scaffold:** ownership-delta screen → flow interpretation → thesis implication

**Prompt:**
```
5-year rolling correlation between healthcare holdings and: (1) tools vs SOXX; (2) payors vs 10Y yield; (3) hospitals vs employment; (4) biotech vs XBI/R2000; (5) digital health vs WCLD. Per pair: correlation, R², scenario for spike or breakdown. Flag unintended macro bets.
```

---

## 10. Thematic Research

*Prompts for going from theme hypothesis to investable basket.*

### THM-01  Theme Validation Framework

```yaml
id: THM-01
title: Theme Validation Framework
tags: [#thematic, #cross-sector, #senior-judgment, #pm-level]
use_when: "Before investing 3 weeks in a thematic deep-dive."
reasoning: "define theme → size opportunity → identify winners/losers → prioritise"
inputs: "Theme; universe; recent literature."
output: "Validation memo, 800–1,200 words, with verdict."
```

**Reasoning scaffold:** define theme → size opportunity → identify winners/losers → prioritise

**Prompt:**
```
Theme: [paste]. (1) Is it real — empirical evidence? (2) Is it durable — 3 sustaining forces? (3) Differentiated from consensus? (4) Investable — listed pure-plays? (5) Time horizon vs fund? (6) Verdict: full work / basket / pass.
```

---

### THM-02  TAM Bottoms-Up Build

```yaml
id: THM-02
title: TAM Bottoms-Up Build
tags: [#thematic, #cross-sector, #senior-judgment]
use_when: "When a theme depends on a TAM claim."
reasoning: "map value chain → identify choke points → rank beneficiaries → construct basket"
inputs: "TAM claim; epidemiology/market data."
output: "TAM table, gap analysis, basket implication."
```

**Reasoning scaffold:** map value chain → identify choke points → rank beneficiaries → construct basket

**Prompt:**
```
TAM claim: [$XB by YYYY]. (1) Bottoms-up population→use case→addressable→price→penetration; (2) compare to claim; (3) gap driver; (4) historical analogues; (5) verdict; (6) basket implication.
```

---

### THM-03  Thematic Basket Construction

```yaml
id: THM-03
title: Thematic Basket Construction
tags: [#thematic, #portfolio, #cross-sector, #pm-level]
use_when: "When theme is validated and you need an investable expression."
reasoning: "parse regulatory shift → commercial translation → investment construct"
inputs: "Validated theme; candidate names; portfolio constraints."
output: "Basket proposal with weights, factor map, rebalance and kill rules."
```

**Reasoning scaffold:** parse regulatory shift → commercial translation → investment construct

**Prompt:**
```
6–10 name basket for theme [X]. (1) Purity map; (2) quality map; (3) weights with 1–2 pair shorts; (4) factor exposure; (5) rebalance trigger; (6) kill switch.
```

---

## 11. Portfolio Construction and Risk

*Prompts for sector positioning, factor exposures, concentration analysis.*

### PORT-01  Healthcare Sleeve Positioning Review

```yaml
id: PORT-01
title: Healthcare Sleeve Positioning Review
tags: [#portfolio, #cross-sector, #pm-level]
use_when: "Quarterly positioning review."
reasoning: "map sleeve → identify concentration → rebalance logic → commit"
inputs: "Sleeve composition; benchmark; macro view."
output: "Sleeve review, 1,000–1,500 words, with action list."
```

**Reasoning scaffold:** map sleeve → identify concentration → rebalance logic → commit

**Prompt:**
```
Review healthcare sleeve. (1) Sub-sector mix vs benchmark; (2) factor exposure; (3) concentration; (4) coherence test; (5) liquidity; (6) 2 trims, 2 adds, 1 missing exposure.
```

---

### PORT-02  Catalyst Concentration and Path Dependence Map

```yaml
id: PORT-02
title: Catalyst Concentration and Path Dependence Map
tags: [#portfolio, #risk, #biotech, #cross-sector, #pm-level]
use_when: "When multiple binary catalysts cluster."
reasoning: "size by conviction → factor overlay → risk budget → recommend"
inputs: "Sleeve; catalyst calendar."
output: "Catalyst map with hedges."
```

**Reasoning scaffold:** size by conviction → factor overlay → risk budget → recommend

**Prompt:**
```
Map all catalysts in next 90 days. (1) Calendar concentration; (2) factor concentration; (3) worst/best P&L scenarios; (4) hedge suggestions; (5) pre-trim vs hold/add per event.
```

---

### PORT-03  Pair Trade Construction

```yaml
id: PORT-03
title: Pair Trade Construction
tags: [#portfolio, #thesis, #cross-sector, #senior-judgment]
use_when: "When expressing a relative-value insight."
reasoning: "hedge construct → cost-benefit → execute → monitor"
inputs: "Two tickers; rationale; spread."
output: "Pair trade memo, 600–1,000 words."
```

**Reasoning scaffold:** hedge construct → cost-benefit → execute → monitor

**Prompt:**
```
Long [A] / Short [B]. (1) Relative-value mechanism; (2) beta/factor neutralisation; (3) catalyst alignment; (4) borrow cost and squeeze risk; (5) entry/target/stop; (6) carry.
```

---

### PORT-04  Borrow, Float, and Short Interest Analysis

```yaml
id: PORT-04
title: Borrow, Float, and Short Interest Analysis
tags: [#portfolio, #risk, #cross-sector, #bloomberg, #senior-judgment]
use_when: "Before initiating or sizing a short."
reasoning: "catalyst overlap audit → stress-test → rebalance → monitor"
inputs: "SI data, borrow rates, float details, catalyst calendar."
output: "Short setup report with sizing recommendation."
```

**Reasoning scaffold:** catalyst overlap audit → stress-test → rebalance → monitor

**Prompt:**
```
Short setup for [TICKER]. (1) SI as % float and days-to-cover; (2) borrow availability/cost; (3) float dynamics; (4) squeeze risk catalysts; (5) retail/momentum signals; (6) structural vs tactical; (7) sizing recommendation.
```

---

### PORT-05  Constructive Disagreement with Portfolio Manager on Sizing or Thesis

```yaml
id: PORT-05
title: Constructive Disagreement with Portfolio Manager on Sizing or Thesis
tags: [#portfolio, #people-dynamics, #cross-sector, #senior-judgment]
use_when: "When the analyst's view on sizing, entry, exit, or thesis materially differs from the PM's, and the analyst needs to structure the disagreement so it improves the decision rather than damaging the relationship."
reasoning: "separate disagreement components → steel-man PM → offer falsification → document"
inputs: "My thesis or sizing recommendation; PM's stated view; any context on book-level factors the PM may be weighting."
output: "Structured approach to the disagreement with steel-man, minimum viable argument, falsification test, and documentation plan."
```

**Reasoning scaffold:** separate disagreement components → steel-man PM → offer falsification → document

**Prompt:**
```
I have a material disagreement with my PM on [TICKER / decision]. My view: [state view]. PM view: [state view]. Structure my approach to this disagreement. (1) Separate the disagreement into components — is the divergence about (a) the underlying facts and what the filings say, (b) the interpretation of those facts into thesis claims, (c) the probabilities attached to scenarios, (d) the sizing implications given a shared thesis, or (e) the risk tolerance of the book? Each component calls for a different kind of conversation. A factual disagreement is resolvable by returning to primary sources; a risk-tolerance disagreement is not. (2) Steel-man the PM's position — before preparing my argument, write out the strongest version of the PM's case in at least 200 words, including any information advantage the PM may have (other names in the book, factor exposures I cannot see, client constraints, prior experience with similar situations). If I cannot articulate the PM's view charitably, I am not ready to argue my own. (3) Identify the minimum viable argument — what is the smallest claim I need the PM to accept for my recommended action to follow? Arguing for the full maximalist thesis is a losing strategy if a narrower claim is sufficient. (4) Identify the falsification test I would accept — what would I have to see to change my mind toward the PM's view? Offering a specific falsification condition in advance both signals good faith and forces my own calibration. (5) Structure the conversation — lead with the shared assumption (where we agree), then the narrow divergence (where we differ), then the falsification test, then the recommended action. Avoid building the case chronologically or walking through my entire reasoning; the PM does not have time. (6) Commit-and-review rule — if the PM decides against my recommendation, define in advance the observable signal that would make me return to the topic (a specific KPI miss, a specific data point) versus accepting the decision and moving on. This avoids both repeated re-litigation and quiet resentment. (7) Document the disagreement — a short written note (one paragraph) capturing my view, the PM's view, and what I will watch. This serves both my own learning (SELL-04 post-mortem later) and professional record if the decision matters. End with my action for the conversation.
```

---

### PORT-06  Defending a Contrarian Thesis at Investment Committee

```yaml
id: PORT-06
title: Defending a Contrarian Thesis at Investment Committee
tags: [#portfolio, #people-dynamics, #client-comms, #cross-sector, #senior-judgment, #pm-level]
use_when: "Before presenting a thesis to IC where the mood is running the opposite direction (bullish into a scepticism-dominant IC or bearish into a consensus long), and the analyst needs to defend the view without becoming defensive."
reasoning: "anticipate attacks → prepare rebuttals → emotional regulation → pre-commit exit"
inputs: "Thesis memo; IC member views where known; recent IC track record for similar decisions; my own history at IC."
output: "IC defence plan with anticipated attacks, evidence hierarchy, emotional regulation, calibrated confidence, and verbatim opening."
```

**Reasoning scaffold:** anticipate attacks → prepare rebuttals → emotional regulation → pre-commit exit

**Prompt:**
```
I am presenting [TICKER] to IC on [date]. My view: [long / short / contrarian hold]. IC mood appears to be: [opposite direction]. Prepare me to defend the view. (1) Anticipate the three sharpest attacks — for each, state the attack in the IC member's own voice (not my charitable reframing), the strongest rebuttal I have, and the point at which the rebuttal becomes weak. Prepare the concession language for the weak points in advance. Acknowledging a real weakness strengthens credibility more than denying it. (2) Evidence hierarchy — identify the single piece of evidence most likely to shift a sceptical IC member's view, and the piece most likely to be dismissed. Lead with the former; hold the latter in reserve. (3) Emotional regulation plan — what is the most likely emotional failure mode for me in this specific IC? Defensiveness, over-elaboration, conceding too readily, or doubling down too hard? Pre-commit to the counter-move. If I feel defensiveness rising, slow down and ask what specifically the challenger would need to see. If I feel the urge to over-elaborate, cut the explanation at 30 seconds and ask if more detail would help. (4) Calibrated confidence — state my confidence level (0.00–1.00) up front rather than defending the view uniformly. A confident statement of moderate confidence is more credible than an uncertain statement of high confidence. Distinguish the parts of the thesis I hold with high confidence (specific facts) from the parts I hold with moderate confidence (inferences) from the parts I hold with low confidence (forward estimates). (5) The one question I want IC to answer — what is the specific question I need the IC to weigh in on, as distinct from the overall rating? IC's time is best spent on the judgment calls I cannot resolve independently. Frame the question to focus IC attention there. (6) Exit conditions in advance — state the observable conditions under which I would reverse this view. Pre-committing to exit conditions both strengthens the initial case and protects against anchoring if the thesis breaks. (7) Post-IC plan — if the IC concludes against my view, what do I do next? Accept the decision? Return to it in 60 days if a specific signal arrives? Maintain a smaller position? Clarity on this before the IC prevents post-meeting ambiguity. End with the opening 90 seconds of my presentation, verbatim.
```

---

## 12. ESG Integration and Stewardship

*Prompts for ESG materiality and stewardship without descending into checklist ESG.*

### ESG-01  Healthcare Materiality Map

```yaml
id: ESG-01
title: Healthcare Materiality Map
tags: [#esg, #cross-sector, #senior-judgment]
use_when: "When initiating coverage and need materiality beyond MSCI/Sustainalytics."
reasoning: "materiality assess → peer benchmark → integrate to thesis → monitor"
inputs: "Sustainability report, 10-K, proxy, ESG ratings."
output: "Materiality map with forward flags."
```

**Reasoning scaffold:** materiality assess → peer benchmark → integrate to thesis → monitor

**Prompt:**
```
Materiality map for [TICKER] per SASB/IFRS S1-S2 and CSRD double-materiality. E: scope 1-2-3, decarbonisation, water/waste. S: drug pricing/access, product safety, trial diversity, workforce. G: capital allocation, comp alignment, board, audit. Per item: financial materiality, disclosure quality, performance. 2–3 forward-looking materiality flags.
```

---

### ESG-02  Stewardship Engagement Plan

```yaml
id: ESG-02
title: Stewardship Engagement Plan
tags: [#esg, #mgmt-meeting, #cross-sector, #senior-judgment, #pm-level]
use_when: "When designing an engagement arc on an ESG-material issue."
reasoning: "screen exposure → quantify impact → engage management → commit action"
inputs: "Issue; company position; position size."
output: "Engagement plan with escalation and reporting."
```

**Reasoning scaffold:** screen exposure → quantify impact → engage management → commit action

**Prompt:**
```
Engage [TICKER] on [issue]. (1) Financial materiality case; (2) specific ask; (3) counterparty sequencing; (4) 12–24 month milestones; (5) escalation; (6) coalition; (7) reporting (SFDR Art 9, UK Stewardship Code).
```

---

### ESG-03  Drug Pricing and IRA Exposure Map

```yaml
id: ESG-03
title: Drug Pricing and IRA Exposure Map
tags: [#esg, #pharma, #biotech, #cms, #senior-judgment]
use_when: "For branded pharma/biotech assessing IRA and pricing reform exposure."
reasoning: "map IRA impact → quantify negotiation risk → translate to revenue → action"
inputs: "Product disclosure, management commentary, IRA timelines."
output: "Asset-by-asset exposure table with thesis impact."
```

**Reasoning scaffold:** map IRA impact → quantify negotiation risk → translate to revenue → action

**Prompt:**
```
Map [TICKER]’s IRA exposure. (1) Asset-by-asset negotiation exposure (9y SM / 13y biologic thresholds); (2) Part D redesign impact; (3) 340B exposure; (4) inflation rebate; (5) mitigations; (6) net thesis impact vs consensus.
```

---

### ESG-04  Access to Medicine Index and EM Pricing Strategy Review

```yaml
id: ESG-04
title: Access to Medicine Index and EM Pricing Strategy Review
tags: [#esg, #pharma, #senior-judgment]
use_when: "Annual review for pharma where access is commercially material."
reasoning: "stewardship engage → track commitments → escalate or accept → report"
inputs: "AtMI scorecard, sustainability report, EM strategy."
output: "Access strategy review with peer benchmark."
```

**Reasoning scaffold:** stewardship engage → track commitments → escalate or accept → report

**Prompt:**
```
Access review for [TICKER]. (1) AtMI scorecard; (2) assets where access shapes TAM; (3) peer comparison; (4) LMIC commercial upside; (5) engagement opportunity.
```

---

### ESG-05  Healthcare Climate Risk and Decarbonisation Pathway Assessment

```yaml
id: ESG-05
title: Healthcare Climate Risk and Decarbonisation Pathway Assessment
tags: [#esg, #cross-sector, #pharma, #medtech, #tools-dx, #senior-judgment]
use_when: "When integrating climate physical and transition risk into healthcare investment work, particularly for CSRD-reporting companies and as part of the TCFD/IFRS S2 disclosure regime."
reasoning: "physical risk inventory → transition risk assess → score materiality → engage"
inputs: "Company sustainability report, CSRD statement or TCFD disclosure, CDP submission if available, facility location data, supplier disclosure, peer benchmarks."
output: "Climate risk map with physical and transition risk inventory, pathway credibility assessment, financial materiality scoring, and engagement opportunity."
```

**Reasoning scaffold:** physical risk inventory → transition risk assess → score materiality → engage

**Prompt:**
```
Map [TICKER]'s exposure to climate physical risk and transition risk as material to the investment case, consistent with TCFD, IFRS S2, and EU CSRD double-materiality reporting. (1) Physical risk inventory — manufacturing and R&D sites by location, with exposure to acute hazards (flooding, wildfire, tropical storm) and chronic hazards (heat stress, water scarcity, sea-level rise). Pharma and biologics manufacturing is particularly exposed because of dependence on water-intensive processes, cold-chain logistics, and single-source facilities. Quantify using the company's disclosure under CSRD ESRS E1 or equivalent if available, supplemented by public facility location data. (2) Supply chain physical risk — API manufacturing concentration (India, China for small-molecule; US, EU, Puerto Rico for biologics), single-source supplier exposure, and the realistic disruption scenario. The 2017 Hurricane Maria IV bag shortage is the canonical precedent. (3) Transition risk — decarbonisation pathway credibility. Pharma scope 1 and 2 emissions are manageable (facility electrification, renewable power purchasing); scope 3 dominates and is driven by supplier emissions (APIs, excipients, packaging, distribution). Credible pathways require supplier engagement programmes, not just own-operation targets. Medtech transition risk concentrates in single-use disposables and device take-back. (4) Product-level carbon footprint — is the company disclosing product carbon footprint (PCF) for major products? NHS and several European procurement bodies are beginning to factor PCF into formulary decisions. This is an emerging commercial exposure, not just a disclosure exercise. (5) Regulatory exposure — EU CSRD Article 8 implementation timeline for the company's size class, UK-specific TCFD and SDR requirements, and the SEC climate disclosure rule status. (6) Financial materiality score — rank physical, transition, and regulatory risk from 0 to 3 on financial materiality over a 3-year and 10-year horizon. The 10-year score often differs materially from the 3-year score, and both matter for long-duration holders. (7) Engagement opportunity — if climate disclosure or pathway credibility is materially weaker than peers, is this an engagement priority? Reference to CA100+ targets or the IIGCC Net Zero Investment Framework where applicable. End with confidence score.
```

---

## 13. Client Communication and Compliance

*Prompts for internal memos, IC briefings, client letters, quick-reaction notes, and compliance guardrails.*

### COMM-01  IC Memo Draft

```yaml
id: COMM-01
title: IC Memo Draft
tags: [#client-comms, #cross-sector, #senior-judgment, #pm-level]
use_when: "Before presenting to investment committee."
reasoning: "structure memo → compress argument → tailor to audience → polish"
inputs: "Thesis memo, model, valuation."
output: "IC-ready memo, ≤1,000 words."
```

**Reasoning scaffold:** structure memo → compress argument → tailor to audience → polish

**Prompt:**
```
IC memo for [TICKER]. (1) Recommendation in three bullets; (2) 100-word thesis; (3) variant perception; (4) three catalysts; (5) three risks; (6) sizing logic; (7) single chart; (8) two open questions. Under 1,000 words.
```

---

### COMM-02  Quarterly Letter Section Draft

```yaml
id: COMM-02
title: Quarterly Letter Section Draft
tags: [#client-comms, #cross-sector, #senior-judgment]
use_when: "Drafting the healthcare section for the quarterly LP letter."
reasoning: "extract highlights → narrative arc → anchor to thesis → polish"
inputs: "Performance, attribution, thesis evolutions."
output: "Polished 600-word section."
```

**Reasoning scaffold:** extract highlights → narrative arc → anchor to thesis → polish

**Prompt:**
```
Healthcare section. (1) Macro context; (2) top 3 contributors/detractors with operational attribution; (3) one position update; (4) what we got wrong; (5) next-quarter theme. 600 words, confident and honest.
```

---

### COMM-03  Quick-Reaction Internal Note

```yaml
id: COMM-03
title: Quick-Reaction Internal Note
tags: [#client-comms, #earnings-post, #cross-sector, #senior-judgment]
use_when: "Within 60 minutes of a print or event."
reasoning: "pre-publication compliance → flag MNPI risk → redact → clear"
inputs: "Press release, headlines, transcript if available."
output: "200-word internal note."
```

**Reasoning scaffold:** pre-publication compliance → flag MNPI risk → redact → clear

**Prompt:**
```
Quick-reaction on [TICKER]’s [event]. (1) One-line headline; (2) three things that matter; (3) thesis verdict; (4) action; (5) one open question. Under 200 words.
```

---

### COMM-04  Translate Technical Biology for Generalist PMs

```yaml
id: COMM-04
title: Translate Technical Biology for Generalist PMs
tags: [#client-comms, #biotech, #cross-sector, #senior-judgment]
use_when: "When generalist PMs need to engage with biotech science."
reasoning: "post-distribution audit → identify issues → remediation plan"
inputs: "Asset details, mechanism, endpoints."
output: "500-word generalist explainer."
```

**Reasoning scaffold:** post-distribution audit → identify issues → remediation plan

**Prompt:**
```
Translate [asset/mechanism/readout] for a generalist PM. (1) Disease in two sentences; (2) SOC and failure; (3) mechanism with accurate analogy; (4) clinical endpoint in concrete terms; (5) FDA/clinician success criteria; (6) two reasons statistical positive could be clinically irrelevant. ~500 words.
```

---

### COMM-05  MNPI Scrubbing Audit for Client Communications

```yaml
id: COMM-05
title: MNPI Scrubbing Audit for Client Communications
tags: [#compliance, #client-comms, #cross-sector, #senior-judgment]
use_when: "Before sending any outbound communication where you’ve had recent expert calls or management meetings."
reasoning: "translate to client → anchor to portfolio impact → action-frame → polish"
inputs: "Draft; list of recent expert/management interactions."
output: "Marked-up document with MNPI flags and actions."
```

**Reasoning scaffold:** translate to client → anchor to portfolio impact → action-frame → polish

**Prompt:**
```
Audit draft [type] for MNPI risk. (1) Flag statements derived from non-public sources; (2) identify unreported financial data references; (3) flag implied references; (4) recommend: remove / rephrase with attribution / retain with compliance review; (5) confirm conflict disclosures current. Err on caution.
```

---

### COMM-06  Disclosure and Conflict of Interest Check

```yaml
id: COMM-06
title: Disclosure and Conflict of Interest Check
tags: [#compliance, #client-comms, #cross-sector, #junior-task]
use_when: "Before publishing any communication naming specific equities."
reasoning: "annual letter draft → performance narrative → lessons → forward view"
inputs: "Draft; holdings; personal account declarations."
output: "Disclosure checklist with pass/fail."
```

**Reasoning scaffold:** annual letter draft → performance narrative → lessons → forward view

**Prompt:**
```
Disclosure audit. (1) Position (long/short/none) per equity; (2) personal holdings flagged; (3) recent meeting/call notes; (4) past PTs dated; (5) standard disclaimer. Checklist output.
```

---

### COMM-07  Public Speaking and Conference Pre-Flight

```yaml
id: COMM-07
title: Public Speaking and Conference Pre-Flight
tags: [#compliance, #client-comms, #cross-sector, #senior-judgment]
use_when: "Before any public-facing presentation or media appearance."
reasoning: "prospect deck → edge articulation → process transparency → close"
inputs: "Talking points; restricted list; trade blotter."
output: "Pre-flight checklist with rephrasings."
```

**Reasoning scaffold:** prospect deck → edge articulation → process transparency → close

**Prompt:**
```
Pre-flight for [event] on [topic]. (1) Position disclosure confirmed; (2) forward statements grounded in public data; (3) investment advice boundary check; (4) restricted window check; (5) rephrasings for borderline statements; (6) disclaimer included.
```

---

## 14. Sub-Sector Specific Workflows

*Prompts that go deeper into each healthcare sub-sector’s analytical demands.*

### SUB-BIO-01  Phase 3 Readout Pre-Mortem

```yaml
id: SUB-BIO-01
title: Phase 3 Readout Pre-Mortem
tags: [#biotech, #thesis, #ctgov, #pubmed, #senior-judgment]
use_when: "2–4 weeks ahead of a Phase 3 readout."
reasoning: "trial design assess → effect-size distribution → outcome scenarios → sizing"
inputs: "Protocol, Phase 2 pub, KOL commentary, options market."
output: "Pre-mortem, 1,000–1,500 words, with positioning."
```

**Reasoning scaffold:** trial design assess → effect-size distribution → outcome scenarios → sizing

**Prompt:**
```
Pre-mortem for [TICKER]’s Phase 3 in [indication]. (1) Trial design; (2) Phase 2→3 base rate (note: ~70% Ph2 and ~50% Ph3 fail); (3) comparator; (4) outcome distribution with probabilities; (5) stock implications including ‘wins but disappoints’; (6) positioning.
```

---

### SUB-BIO-02  FDA AdCom Prep

```yaml
id: SUB-BIO-02
title: FDA AdCom Prep
tags: [#biotech, #fda-ema, #senior-judgment]
use_when: "Ahead of an AdCom."
reasoning: "label expectation set → commercial translation → payor receptivity → peak sales"
inputs: "FDA materials, panelists, class precedent."
output: "AdCom prep with positioning."
```

**Reasoning scaffold:** label expectation set → commercial translation → payor receptivity → peak sales

**Prompt:**
```
AdCom prep for [asset] on [date]. (1) Expected discussion topics; (2) panel composition and voting history; (3) three likely FDA questions and vote split; (4) stock-impact mapping; (5) positioning.
```

---

### SUB-BIO-03  Conference Abstract Triage

```yaml
id: SUB-BIO-03
title: Conference Abstract Triage
tags: [#biotech, #pharma, #pubmed, #senior-judgment]
use_when: "When abstract titles drop ahead of a major medical conference."
reasoning: "AdCom precedent → panel framing → vote distribution → position"
inputs: "Abstract titles; coverage universe."
output: "Triage table."
```

**Reasoning scaffold:** AdCom precedent → panel framing → vote distribution → position

**Prompt:**
```
Triage for [conference]. Per covered name: (1) what abstract reports; (2) prior data bar; (3) stock-moving likelihood; (4) session timing; (5) competing assets to watch; (6) top 3 for detailed read.
```

---

### SUB-BIO-04  Target Product Profile (TPP) Interrogation

```yaml
id: SUB-BIO-04
title: Target Product Profile (TPP) Interrogation
tags: [#biotech, #fda-ema, #senior-judgment]
use_when: "When the commercial value depends on meeting a specific product profile."
reasoning: "regulatory history parse → pattern-detect → forecast next interaction"
inputs: "Corporate presentation, protocol, comparator data, payer readouts."
output: "TPP competitive assessment."
```

**Reasoning scaffold:** regulatory history parse → pattern-detect → forecast next interaction

**Prompt:**
```
Interrogate TPP for [TICKER]’s [asset]. (1) Dosing/route vs SOC and competitors; (2) comparator endpoint design; (3) safety differentiation; (4) label breadth; (5) payor reimbursement readiness; (6) verdict — differentiated or me-too.
```

---

### SUB-BIO-05  CMC and COGS Scalability Check

```yaml
id: SUB-BIO-05
title: CMC and COGS Scalability Check
tags: [#biotech, #modeling, #senior-judgment]
use_when: "When manufacturing path from clinical to commercial scale is thesis-relevant."
reasoning: "pipeline prioritise → capital allocate → rank assets → recommend"
inputs: "Filings, manufacturing disclosures, CDMO contracts."
output: "CMC assessment with COGS and margin."
```

**Reasoning scaffold:** pipeline prioritise → capital allocate → rank assets → recommend

**Prompt:**
```
Evaluate CMC readiness and COGS for [TICKER]’s [asset]. (1) Modality and scale-up complexity; (2) manufacturing setup; (3) specific bottleneck; (4) COGS at peak volume vs benchmarks; (5) gross margin implication; (6) CMC regulatory risk.
```

---

### SUB-BIO-06  Freedom to Operate (FTO) IP Analysis

```yaml
id: SUB-BIO-06
title: Freedom to Operate (FTO) IP Analysis
tags: [#biotech, #thesis, #senior-judgment]
use_when: "When IP exclusivity is thesis-critical."
reasoning: "label compare post-approval → commercial translate → model delta"
inputs: "Patent databases, SEC disclosures, Para IV filings."
output: "IP risk assessment with thesis implications."
```

**Reasoning scaffold:** label compare post-approval → commercial translate → model delta

**Prompt:**
```
FTO analysis for [TICKER]’s [asset]. (1) Core IP estate by type and geography; (2) Orange/Purple Book listing; (3) third-party blocking IP; (4) IPR challenge durability; (5) lifecycle management; (6) net assessment: strong/adequate/fragile.
```

---

### SUB-BIO-07  FDA Meeting History Risk Extraction

```yaml
id: SUB-BIO-07
title: FDA Meeting History Risk Extraction
tags: [#biotech, #fda-ema, #senior-judgment]
use_when: "When evaluating regulatory risk beyond generic projections."
reasoning: "CMC risk assess → manufacturing scale → approval impact → monitor"
inputs: "SEC filings, presentations, FDA correspondence, Drugs@FDA."
output: "Regulatory risk assessment with evidence."
```

**Reasoning scaffold:** CMC risk assess → manufacturing scale → approval impact → monitor

**Prompt:**
```
Regulatory history for [TICKER]’s [asset]. (1) Type A/B/C meeting outcomes; (2) friction signals; (3) pathway viability; (4) CRL history for class; (5) AdCom likelihood; (6) net risk: low/medium/high.
```

---

### SUB-BIO-08  Post-Approval Label Delta Analyser

```yaml
id: SUB-BIO-08
title: Post-Approval Label Delta Analyser
tags: [#biotech, #pharma, #fda-ema, #senior-judgment]
use_when: "Within 48 hours of FDA or EMA approval, when the exact label language materially affects peak sales and payor reception."
reasoning: "expected label vs actual → commercial unlock → peak-sales delta → precedent"
inputs: "Drugs@FDA approval letter and label, FDA review documents if posted, company press release, pre-approval sell-side peak sales forecasts for bridge construction."
output: "Structured label delta analysis with model bridge and precedent implications."
```

**Reasoning scaffold:** expected label vs actual → commercial unlock → peak-sales delta → precedent

**Prompt:**
```
Analyse the approved label and approval package for [TICKER]'s [asset]. Use Drugs@FDA for the official label text, the FDA approval letter, and the review documents (cross-disciplinary review, medical officer review, statistical review, CMC review) where posted. Do not use FDALabel for exact language; use it only as a navigation aid. Output: (1) Expected vs actual label — a side-by-side of the label language the company and street expected vs what the FDA actually granted. Cover indication scope, line of therapy, patient population subsetting (biomarker, age, comorbidity), dosing, monitoring requirements, black-box warnings, contraindications, and post-marketing commitments (PMCs) or post-marketing requirements (PMRs). (2) Commercial unlock — what does the label enable that a narrower label would not? Quantify in patient populations addressable and in payor coverage likelihood. (3) Commercial restriction — what does the label still restrict? REMS programs, specialty pharmacy channels, prior-auth burden, step-therapy eligibility. (4) Peak-sales model delta — recalculate peak sales under the actual label and bridge vs the prior model. Show the sensitivity to each label element. (5) Post-marketing overhang — any confirmatory trial requirement, safety study, or subpopulation study that could materially affect the label over the next 24–36 months. (6) Precedent implications — does this label set a precedent useful for another asset in the pipeline or the competitive set? End with the confidence score from the standing instructions.
```

---

### SUB-PHA-01  Pipeline Replenishment Audit

```yaml
id: SUB-PHA-01
title: Pipeline Replenishment Audit
tags: [#pharma, #thesis, #sec-filings, #ir-materials, #senior-judgment]
use_when: "Annual pharma pipeline assessment."
reasoning: "patent parse → generic entry model → revenue bridge → offset map"
inputs: "Pipeline, BD history, balance sheet, sell-side LOE notes."
output: "Replenishment audit, 1,500 words."
```

**Reasoning scaffold:** patent parse → generic entry model → revenue bridge → offset map

**Prompt:**
```
Audit [TICKER]’s replenishment over 7 years. (1) LOE revenue at risk; (2) Phase 3/filed PoS-adjusted pipeline; (3) BD gap; (4) capital capacity; (5) M&A track record; (6) self-funder vs transformative deal verdict.
```

---

### SUB-PHA-02  GLP-1 Class Dynamics Map

```yaml
id: SUB-PHA-02
title: GLP-1 Class Dynamics Map
tags: [#pharma, #thematic, #senior-judgment]
use_when: "For any name with GLP-1 exposure."
reasoning: "GTN decompose → channel mix → model impact → monitor"
inputs: "NN/LLY commentary, payor data, KOL views."
output: "GLP-1 memo, 2,000 words, with adjacent-name map."
```

**Reasoning scaffold:** GTN decompose → channel mix → model impact → monitor

**Prompt:**
```
GLP-1 dynamics for 36 months. (1) On-market players; (2) late-stage challengers; (3) indication expansion; (4) pricing trajectory; (5) compounded grey market; (6) adjacent-name impact; (7) regime shift signals.
```

---

### SUB-PHA-03  TRx vs NRx Divergence Monitor

```yaml
id: SUB-PHA-03
title: TRx vs NRx Divergence Monitor
tags: [#pharma, #earnings-post, #senior-judgment]
use_when: "When assessing true commercial momentum."
reasoning: "IRA exposure → negotiation scenarios → revenue impact → hedge"
inputs: "IQVIA, Bloomberg BI, company disclosures."
output: "Volume monitor with divergence flags."
```

**Reasoning scaffold:** IRA exposure → negotiation scenarios → revenue impact → hedge

**Prompt:**
```
Scan prescription data for [TICKER]’s key franchises. (1) TRx and NRx with trends; (2) divergence flags; (3) market share; (4) revenue run-rate implication; (5) model revision flags.
```

---

### SUB-PHA-04  Gross-to-Net (GTN) Margin Erosion Analysis

```yaml
id: SUB-PHA-04
title: Gross-to-Net (GTN) Margin Erosion Analysis
tags: [#pharma, #modeling, #senior-judgment]
use_when: "When net revenue growth lags volume growth."
reasoning: "BD portfolio assess → rationale audit → execution risk → model"
inputs: "Filings, IQVIA, IRA timelines, PBM commentary."
output: "GTN analysis with peer benchmark and model adjustment."
```

**Reasoning scaffold:** BD portfolio assess → rationale audit → execution risk → model

**Prompt:**
```
GTN analysis for [TICKER]. (1) Implied net price per unit over 8 quarters; (2) GTN discount trajectory; (3) driver decomposition; (4) peer comparison; (5) forward net revenue CAGR; (6) model adjustment.
```

---

### SUB-PHA-05  Biosimilar Erosion Curve Modeller

```yaml
id: SUB-PHA-05
title: Biosimilar Erosion Curve Modeller
tags: [#pharma, #modeling, #senior-judgment]
use_when: "When a biologic faces biosimilar entry."
reasoning: "emerging market → pricing dynamics → volume forecast → margin"
inputs: "Patent data, biosimilar tracker, historical curves, defensive commentary."
output: "Erosion model with revenue bridge and sensitivity."
```

**Reasoning scaffold:** emerging market → pricing dynamics → volume forecast → margin

**Prompt:**
```
Biosimilar erosion for [TICKER]’s [franchise]. (1) Entry timing; (2) biologic-specific decay (50–70% retained for 3–5 years vs 80–90% SM loss); (3) contracting/rebating dynamics; (4) geographic phasing; (5) year-by-year revenue bridge; (6) sensitivity to uptake speed.
```

---

### SUB-MED-01  Procedure Volume Recovery Tracker

```yaml
id: SUB-MED-01
title: Procedure Volume Recovery Tracker
tags: [#medtech, #cross-sector, #cms, #sell-side, #junior-task]
use_when: "Monthly tracker for medtech where US procedure volumes drive earnings."
reasoning: "pathway classify → evidence burden → timing estimate → risk-flag"
inputs: "CMS data, hospital operator commentary, device prints."
output: "Tracker with forward outlook and name implications."
```

**Reasoning scaffold:** pathway classify → evidence burden → timing estimate → risk-flag

**Prompt:**
```
Procedure tracker for [category]. Benchmark vs industry 3–5% volume growth. (1) CMS/private claims data; (2) hospital operator commentary; (3) site-of-service shift; (4) capacity constraints; (5) 4-quarter forward outlook; (6) leveraged names.
```

---

### SUB-MED-02  Reimbursement and Coding Change Impact

```yaml
id: SUB-MED-02
title: Reimbursement and Coding Change Impact
tags: [#medtech, #cms, #senior-judgment]
use_when: "When CMS rule changes affect a medtech name."
reasoning: "procedure volumes → adoption curve → revenue build → sensitivity"
inputs: "Rule text, CMS analysis, company commentary."
output: "Impact analysis with thesis delta and engagement."
```

**Reasoning scaffold:** procedure volumes → adoption curve → revenue build → sensitivity

**Prompt:**
```
Impact analysis for [event] on [TICKER]. (1) Rule details; (2) dollar impact per procedure; (3) volume impact; (4) competitive impact; (5) implementation timeline; (6) thesis delta; (7) engagement plan.
```

---

### SUB-MED-03  510(k) Predicate Validity Check

```yaml
id: SUB-MED-03
title: 510(k) Predicate Validity Check
tags: [#medtech, #fda-ema, #senior-judgment]
use_when: "When the 510(k) predicate choice is thesis-relevant."
reasoning: "ASP trajectory → mix shift → margin implications → monitor"
inputs: "FDA 510(k) database, classification, regulatory disclosures."
output: "Predicate risk assessment."
```

**Reasoning scaffold:** ASP trajectory → mix shift → margin implications → monitor

**Prompt:**
```
Evaluate predicate for [TICKER]’s [device]. (1) Predicate identity and clearance date; (2) validity — is it outdated or under different standards; (3) substantial equivalence argument; (4) rejection risk; (5) De Novo/PMA cost and timeline if forced; (6) thesis impact.
```

---

### SUB-MED-04  De Novo vs PMA Regulatory Pathway Risk

```yaml
id: SUB-MED-04
title: De Novo vs PMA Regulatory Pathway Risk
tags: [#medtech, #fda-ema, #senior-judgment]
use_when: "For novel devices where pathway choice is material."
reasoning: "tariff exposure → sourcing audit → margin impact → scenario"
inputs: "FDA classification, regulatory strategy, recent decisions."
output: "Pathway risk with timeline and NPV sensitivity."
```

**Reasoning scaffold:** tariff exposure → sourcing audit → margin impact → scenario

**Prompt:**
```
De Novo vs PMA for [TICKER]’s [device]. (1) Classification; (2) De Novo requirements and timeline; (3) PMA requirements if escalated; (4) competitive moat implications; (5) revenue delay NPV impact; (6) recent comparables.
```

---

### SUB-MED-05  Average Selling Price (ASP) Deflation Analysis

```yaml
id: SUB-MED-05
title: Average Selling Price (ASP) Deflation Analysis
tags: [#medtech, #modeling, #senior-judgment]
use_when: "When the thesis depends on pricing stability."
reasoning: "recall assess → liability quantify → model impact → monitor"
inputs: "Filings, hospital purchasing data, GPO data, peer pricing."
output: "ASP deflation analysis with model implications."
```

**Reasoning scaffold:** recall assess → liability quantify → model impact → monitor

**Prompt:**
```
ASP analysis for [TICKER]. (1) Historical ASP trend from revenue/units; (2) GPO/IDN contract dynamics; (3) competitive pricing pressure; (4) technology cycle premium vs commoditisation; (5) COGS offset; (6) forward model at current deflation rate.
```

---

### SUB-SVC-01  Hospital Operator Earnings Cross-Read

```yaml
id: SUB-SVC-01
title: Hospital Operator Earnings Cross-Read
tags: [#services-payors, #medtech, #earnings-post, #transcripts, #senior-judgment]
use_when: "After hospital operator earnings."
reasoning: "MA bid cycle → rate impact → revenue/margin → multiple"
inputs: "Hospital operator transcripts; coverage list."
output: "Cross-read, 800–1,000 words."
```

**Reasoning scaffold:** MA bid cycle → rate impact → revenue/margin → multiple

**Prompt:**
```
Cross-read [HCA/THC/UHS] for [Q]. (1) Procedure volumes by category; (2) acuity mix; (3) capex; (4) labour cost; (5) payor mix; (6) drug expense/340B; (7) synthesis — top 3 medtech, 2 pharma, 1 payor implication.
```

---

### SUB-SVC-02  Medicare Advantage Bid Cycle Tracker

```yaml
id: SUB-SVC-02
title: Medicare Advantage Bid Cycle Tracker
tags: [#services-payors, #cms, #senior-judgment, #pm-level]
use_when: "Annual bid cycle window."
reasoning: "Stars map → bonus implication → forecast → position"
inputs: "CMS notices, managed care transcripts, broker commentary, KFF."
output: "Bid cycle tracker through each milestone."
```

**Reasoning scaffold:** Stars map → bonus implication → forecast → position

**Prompt:**
```
[Year] MA bid cycle. (1) Rate notice components; (2) industry benefit design response; (3) bid aggressiveness by issuer; (4) preliminary AEP indicators; (5) final AEP results; (6) next-year implications by name.
```

---

### SUB-SVC-03  Vertical Integration MLR Shifting

```yaml
id: SUB-SVC-03
title: Vertical Integration MLR Shifting
tags: [#services-payors, #modeling, #senior-judgment]
use_when: "For vertically integrated insurers (UNH, CVS, ELV, CI)."
reasoning: "MLR decompose → cost trend → margin forecast"
inputs: "Segment disclosures, elimination notes, peer MLR, regulatory commentary."
output: "Vertical integration margin analysis with regulatory risk."
```

**Reasoning scaffold:** MLR decompose → cost trend → margin forecast

**Prompt:**
```
Analyse [TICKER]’s vertical integration profit shifting. (1) Segment map and intercompany flows; (2) transfer pricing vs third-party benchmarks; (3) MLR with vs without market-rate repricing; (4) regulatory risk; (5) disclosure transparency; (6) margin sustainability.
```

---

### SUB-SVC-04  Value-Based Care Capitation Tracking

```yaml
id: SUB-SVC-04
title: Value-Based Care Capitation Tracking
tags: [#services-payors, #modeling, #senior-judgment]
use_when: "When evaluating provider groups transitioning to risk-bearing contracts."
reasoning: "hospital operator → payer mix → margin → monitor"
inputs: "Segment disclosures, VBC contract details, quality metrics."
output: "Capitation tracking with margin trajectory."
```

**Reasoning scaffold:** hospital operator → payer mix → margin → monitor

**Prompt:**
```
Risk-bearing exposure for [TICKER]. (1) Revenue mix: capitated/full-risk/shared-savings vs fee-for-service over 8 quarters; (2) risk corridor and stop-loss; (3) medical cost ratio on risk contracts; (4) patient attribution stability; (5) quality incentive attainment; (6) VBC revenue growth vs FFS trajectory; (7) margin implication at current transition pace.
```

---

### SUB-TLS-01  Bioprocessing Cycle Tracker

```yaml
id: SUB-TLS-01
title: Bioprocessing Cycle Tracker
tags: [#tools-dx, #thematic, #senior-judgment]
use_when: "Quarterly bioprocessing demand assessment."
reasoning: "bioprocessing cycle → demand signals → pricing → forecast"
inputs: "Bioprocessing transcripts, biotech funding, China policy."
output: "Cycle tracker with positioning calls."
```

**Reasoning scaffold:** bioprocessing cycle → demand signals → pricing → forecast

**Prompt:**
```
Track bioprocessing cycle for [companies]. (1) Backlog and book-to-bill; (2) customer commentary; (3) inventory normalisation credibility; (4) gene/cell therapy optionality; (5) China dynamics; (6) cycle stage; (7) cohort positioning.
```

---

### SUB-TLS-02  NGS Instrument vs Consumables Mix Forecast

```yaml
id: SUB-TLS-02
title: NGS Instrument vs Consumables Mix Forecast
tags: [#tools-dx, #modeling, #senior-judgment]
use_when: "For NGS names where instrument cycle and consumables flywheel diverge."
reasoning: "NGS platform → share trajectory → recurring revenue → model"
inputs: "Installed base data, transcripts, peer commentary."
output: "Two-engine forecast with margin trajectory."
```

**Reasoning scaffold:** NGS platform → share trajectory → recurring revenue → model

**Prompt:**
```
NGS forecast for [TICKER], 8 quarters. (1) Installed base by platform; (2) utilisation trend; (3) end-market mix; (4) gross margin trajectory; (5) competitive impact; (6) cross-check vs management targets.
```

---

### SUB-TLS-03  LDT Regulatory Oversight Impact

```yaml
id: SUB-TLS-03
title: LDT Regulatory Oversight Impact
tags: [#tools-dx, #fda-ema, #senior-judgment]
use_when: "When FDA’s Laboratory Developed Test rule materially affects a diagnostics name."
reasoning: "lab test volume → reimbursement → forecast"
inputs: "Company disclosures, FDA LDT final rule, competitive landscape."
output: "LDT regulatory impact with compliance cost and margin effect."
```

**Reasoning scaffold:** lab test volume → reimbursement → forecast

**Prompt:**
```
LDT oversight impact for [TICKER]. (1) Current LDT revenue as % of total and which tests are affected; (2) FDA’s phased enforcement timeline and current status; (3) compliance cost — 510(k) or PMA filing for each at-risk test; (4) competitive impact — do large IVD manufacturers gain vs lab-specific LDTs; (5) margin impact at full compliance; (6) legal challenge status and probability of enforcement delay.
```

---

### SUB-TLS-04  IVD Reagent Pull-Through Rate Calculator

```yaml
id: SUB-TLS-04
title: IVD Reagent Pull-Through Rate Calculator
tags: [#tools-dx, #modeling, #senior-judgment]
use_when: "For IVD instrument/consumables names where menu breadth utilisation is the margin driver."
reasoning: "IVD reagent → installed base → pull-through → model"
inputs: "Company disclosures, assay menu data, peer benchmarks."
output: "Pull-through analysis with menu utilisation and margin sensitivity."
```

**Reasoning scaffold:** IVD reagent → installed base → pull-through → model

**Prompt:**
```
Reagent pull-through for [TICKER]. (1) Installed IVD instruments by platform; (2) assay menu breadth (number of approved tests per platform); (3) reagent revenue per instrument per year; (4) menu utilisation rate (tests actually run vs tests available); (5) menu expansion pipeline; (6) competitive pull-through benchmarks; (7) gross margin sensitivity to utilisation changes.
```

---

### SUB-TLS-05  Companion Diagnostic Linkage and Precision Medicine Coupling

```yaml
id: SUB-TLS-05
title: Companion Diagnostic Linkage and Precision Medicine Coupling
tags: [#tools-dx, #biotech, #pharma, #senior-judgment]
use_when: "When evaluating a precision medicine therapy where a companion diagnostic governs use, or a diagnostics name whose revenue depends on therapy-test coupling."
reasoning: "therapy-test couple → volume attribution → revenue translate"
inputs: "FDA approval letter and label for the therapy, CDx approval letter, clinical practice guidelines, peer commentary on testing patterns, company disclosures on testing volumes or partnerships."
output: "Therapy-diagnostic coupling analysis with volume flow, revenue translation, and model implications for both names."
```

**Reasoning scaffold:** therapy-test couple → volume attribution → revenue translate

**Prompt:**
```
Map the therapy-to-test linkage for [therapy TICKER] and [diagnostic TICKER]. (1) Regulatory coupling — is the companion diagnostic mandatory per the FDA label (CDx specified in the indications or dosing section), supportive but not required, or unapproved but commonly used? Cite the exact label language from Drugs@FDA. (2) CDx status — is the diagnostic FDA-approved as a CDx, CE-marked, or operating as a Laboratory Developed Test (LDT); which sponsor holds the approval and what testing platforms are covered. (3) Competing tests — list every test validated against the same biomarker, including LDTs from major reference labs (Quest, Labcorp, academic centres); rank by clinical adoption and by payor reimbursement; identify which test will actually capture volume in practice. (4) Volume flow — given the therapy's expected label, patient population, and testing cascade, what diagnostic test volume is realistically attributable to therapy uptake vs other indications testing the same biomarker? (5) Revenue translation — for the diagnostic company, the revenue contribution from this specific therapy launch; for the therapy company, the risk that test availability, turnaround time, or cost constrains prescription; for both, the scenario where LDT competition erodes the approved CDx's pricing. (6) Adoption acceleration or constraint — does the CDx accelerate therapy uptake (by defining an eligible population clearly) or constrain it (by adding diagnostic friction before prescribing)? (7) Model implications for both names. End with the confidence score.
```

---

### SUB-DIG-01  Enterprise Health-Tech Sales Cycle Diligence

```yaml
id: SUB-DIG-01
title: Enterprise Health-Tech Sales Cycle Diligence
tags: [#digital-health, #expert-network, #senior-judgment]
use_when: "When bookings and renewal economics matter more than reported revenue."
reasoning: "regulatory classify → reimbursement → adoption path"
inputs: "Filings, IR commentary, peer commentary."
output: "Enterprise motion diligence with expert plan."
```

**Reasoning scaffold:** regulatory classify → reimbursement → adoption path

**Prompt:**
```
Enterprise sales diligence for [TICKER]. (1) Customer segmentation; (2) sales cycle stages and conversion; (3) renewal dynamics; (4) net revenue retention; (5) competitive bake-offs; (6) deterioration tells; (7) expert call list.
```

---

### SUB-DIG-02  AI/ML in Healthcare Investability Test

```yaml
id: SUB-DIG-02
title: AI/ML in Healthcare Investability Test
tags: [#digital-health, #thematic, #thesis, #senior-judgment, #pm-level]
use_when: "When filtering genuine AI moat from buzzword."
reasoning: "PMPM economics → retention stress-test → margin forecast"
inputs: "Company materials, clinical evidence, regulatory status."
output: "Investability assessment with verdict."
```

**Reasoning scaffold:** PMPM economics → retention stress-test → margin forecast

**Prompt:**
```
Investability test for [TICKER]. (1) Use-case specificity with evidence; (2) data moat; (3) regulatory pathway (SaMD, CE mark); (4) reimbursement (CPT, NTAP); (5) distribution; (6) unit economics; (7) verdict: conviction / basket / pass.
```

---

### SUB-DIG-03  Health Equity and Digital Divide Assessment

```yaml
id: SUB-DIG-03
title: Health Equity and Digital Divide Assessment
tags: [#digital-health, #esg, #senior-judgment]
use_when: "When evaluating whether a digital health platform’s architecture limits its realistic TAM."
reasoning: "employer channel → enterprise sales → ramp forecast"
inputs: "Platform architecture docs, clinical study demographics, CMS programme eligibility."
output: "Health equity TAM assessment with competitive implication."
```

**Reasoning scaffold:** employer channel → enterprise sales → ramp forecast

**Prompt:**
```
Assess [TICKER]’s health equity profile. (1) Platform accessibility — minimum bandwidth, hardware requirements, language support, literacy assumptions; (2) Medicaid population reach — can the platform serve low-income, rural, or elderly populations where government-sponsored healthcare is the primary payor? (3) Clinical validation diversity — were clinical studies conducted across representative demographics? (4) Regulatory tailwinds — does the platform qualify for CMS innovation centre programmes, FQHC funding, or state Medicaid waivers? (5) TAM implication — if the platform cannot serve Medicaid/dual-eligible populations, what percentage of the claimed TAM is effectively inaccessible? (6) Competitive positioning — are competitors specifically targeting underserved populations, creating a flanking risk?
```

---

## 15. Technical System Integration

*Prompts for generating executable syntax for Bloomberg BQL, FactSet FQL, SEC EDGAR, and ClinicalTrials.gov — the data systems that power institutional healthcare research.*

### TECH-01  Bloomberg BQL Syntax Generator for Healthcare

```yaml
id: TECH-01
title: Bloomberg BQL Syntax Generator for Healthcare
tags: [#data-extraction, #cross-sector, #bloomberg, #bql, #junior-task]
use_when: "When you need executable Bloomberg BQL syntax for healthcare-specific data queries."
reasoning: "query construct → validate output → deploy"
inputs: "Natural-language data query; target securities; output format (Excel or Python)."
output: "Executable BQL string ready to paste into Excel or Python."
```

**Reasoning scaffold:** query construct → validate output → deploy

**Prompt:**
```
Translate my natural-language query into executable BQL syntax for Excel or Python. (1) Construct the =BQL() formula using get(<field>) for(<security>) with(<parameters>). (2) Define parameters (dates, periods, fill rules). (3) For fiscal-period data, format calculated periods correctly (e.g. FA_PERIOD_REFERENCE, FA_PERIOD_TYPE=LTM). (4) For healthcare-specific fields, use the correct BQL field names for R&D expense, pipeline data, patent expiry via PTNT <GO>, catalyst calendar. (5) Output validation — verify parentheses and nesting. (6) If Python, provide the bql.Execute() syntax with proper DataFrame handling. My query: [describe the data needed].
```

---

### TECH-02  Bloomberg Catalyst and Event Calendar Query

```yaml
id: TECH-02
title: Bloomberg Catalyst and Event Calendar Query
tags: [#data-extraction, #biotech, #bloomberg, #bql, #senior-judgment]
use_when: "When building or refreshing a catalyst calendar from Bloomberg data."
reasoning: "schema design → pipeline build → validate → deploy"
inputs: "Coverage universe tickers; date window."
output: "BQL query or terminal navigation with structured output."
```

**Reasoning scaffold:** schema design → pipeline build → validate → deploy

**Prompt:**
```
Generate a BQL query to extract the upcoming catalyst calendar for my healthcare coverage universe, specifically filtering for: (1) FDA Advisory Committee (AdCom) meetings in the next 90 days; (2) PDUFA dates in the next 180 days; (3) Phase 3 trial readout windows from Bloomberg BI DRUG <GO> or equivalent; (4) CMS rate notice and final rule dates. Output as a structured table with ticker, event type, expected date, and Bloomberg event ID. If a BQL approach is limited, provide the alternative Bloomberg terminal navigation (BI, EVTS, DRUG <GO>) with the specific screen settings.
```

---

### TECH-03  FactSet Universal Screening for Healthcare

```yaml
id: TECH-03
title: FactSet Universal Screening for Healthcare
tags: [#data-extraction, #cross-sector, #factset, #fql, #senior-judgment]
use_when: "When building a quant screen in FactSet with healthcare-specific criteria."
reasoning: "data source audit → API construct → integrate → maintain"
inputs: "Screen criteria; output format preference."
output: "FactSet screening formula and API payload."
```

**Reasoning scaffold:** data source audit → API construct → integrate → maintain

**Prompt:**
```
Build a FactSet Universal Screening formula for [screen description]. (1) Assign correct data library prefixes — FF_ for FactSet Fundamentals, FG_ for Global Constituents. (2) Apply relative date parameters: (0) for most recent, (-1) for prior year. (3) Map to the correct API endpoint if programmatic extraction is needed — /metrics for income statement items, OFDB for non-portfolio databases. (4) For healthcare-specific criteria, include: therapeutic area classification, pipeline stage filters, patent expiry windows, and clinical trial event flags. (5) Output the screen as both a FactSet workstation formula and a JSON payload for the FactSet Fundamentals API. My screen: [describe criteria].
```

---

### TECH-04  FactSet Document Search for Transcript Mining

```yaml
id: TECH-04
title: FactSet Document Search for Transcript Mining
tags: [#data-extraction, #cross-sector, #factset, #fql, #senior-judgment]
use_when: "When mining earnings transcripts for specific themes across the coverage universe."
reasoning: "registry query → filter results → analyse → monitor"
inputs: "Topic; universe; quarter."
output: "Transcript mining results with source links and cross-read."
```

**Reasoning scaffold:** registry query → filter results → analyse → monitor

**Prompt:**
```
Command the FactSet Document Search (GenAI-powered) to extract specific commentary from healthcare earnings transcripts. (1) Construct the query to search for [topic — e.g. ‘GLP-1 cost impact’, ‘supply chain bottlenecks’, ‘pricing pressure’, ‘biosimilar competition’] across the most recent quarter’s transcripts for [universe]. (2) Filter by section (prepared remarks vs Q&A) if the topic is more likely to surface in one or the other. (3) Request source-linked results so each excerpt maps back to a specific transcript, speaker, and timestamp. (4) Summarise the results as: company, relevant quote, sentiment (positive/negative/neutral), and cross-read implication for my coverage.
```

---

### TECH-05  SEC EDGAR Autonomous Agent Configuration

```yaml
id: TECH-05
title: SEC EDGAR Autonomous Agent Configuration
tags: [#data-extraction, #cross-sector, #sec-filings, #senior-judgment]
use_when: "When setting up automated monitoring of SEC filings for thesis-relevant events."
reasoning: "BQL construct → test output → deploy screen"
inputs: "Coverage universe CIK numbers; filing types; keyword list."
output: "Agent configuration with API endpoints and JSON schema."
```

**Reasoning scaffold:** BQL construct → test output → deploy screen

**Prompt:**
```
Configure an autonomous agent to monitor SEC EDGAR filings across my coverage universe. (1) Form 4 insider trading — flag any open-market purchase >$100K by C-suite or board members, cross-referenced against upcoming catalyst calendar. (2) 8-K current reports — parse for keywords: ‘Complete Response Letter’, ‘CRL’, ‘accelerated approval’, ‘voluntary recall’, ‘consent decree’, ‘executive departure’, and any material definitive agreement. (3) 13F institutional holdings — quarterly delta for the top 20 healthcare-focused funds. (4) Output as structured JSON mapped to predefined schemas: {ticker, form_type, filing_date, key_event, relevance_score}. (5) Provide the EDGAR XBRL API endpoint structure and the query parameters for each filing type.
```

---

### TECH-06  ClinicalTrials.gov Agent Query Construction

```yaml
id: TECH-06
title: ClinicalTrials.gov Agent Query Construction
tags: [#data-extraction, #biotech, #ctgov, #senior-judgment]
use_when: "When extracting structured clinical trial data programmatically."
reasoning: "FQL construct → test → deploy ownership or estimate workflow"
inputs: "Condition, intervention, sponsor, or NCT numbers."
output: "API query URL and JSON output schema."
```

**Reasoning scaffold:** FQL construct → test → deploy ownership or estimate workflow

**Prompt:**
```
Build a resilient query for ClinicalTrials.gov that bypasses fragile DOM selectors. (1) Construct the API query URL (using the v2 API: https://clinicaltrials.gov/api/v2/studies) to extract: NCTId, BriefTitle, Condition, InterventionName, Phase, OverallStatus, StartDate, PrimaryCompletionDate, StudySponsor. (2) Filter for multiple statuses simultaneously (e.g. ‘RECRUITING’ and ‘ACTIVE_NOT_RECRUITING’). (3) Filter by condition, intervention type, or sponsor. (4) Construct a comparative query for [TICKER]’s lead asset vs all competing trials in the same indication/mechanism. (5) Output as structured JSON for downstream analysis. (6) If using an AI agent framework (e.g. AgentQL), provide the natural-language extraction query. My query: [describe the trial data needed].
```

---

## 16. International Coverage

*Prompts for the ex-US healthcare dynamics that a global mandate requires: European HTA pathways, Japanese reimbursement cycles, Chinese biotech licensing economics, and UK-specific considerations. Applies particularly to London-based analysts covering global names.*

### INTL-01  European HTA Pathway Mapping

```yaml
id: INTL-01
title: European HTA Pathway Mapping
tags: [#international, #pharma, #biotech, #medtech, #senior-judgment]
use_when: "When assessing European commercial potential for a new drug or device launch, given the fragmentation of national HTA bodies and the forthcoming EU Joint Clinical Assessment (JCA)."
reasoning: "EU JCA scope → national HTA map → revenue bridge → thesis delta"
inputs: "EMA filing status, company European strategy disclosure, comparable-product HTA precedent, NICE/G-BA/HAS recent decisions in the therapeutic area."
output: "European HTA pathway map with country-level timing, reimbursement scenarios, and revenue bridge."
```

**Reasoning scaffold:** EU JCA scope → national HTA map → revenue bridge → thesis delta

**Prompt:**
```
Map the European HTA pathway for [TICKER]'s [asset] in [indication]. (1) EU Joint Clinical Assessment — is the asset in scope for the EU JCA regulation (oncology and ATMPs from 2025; orphan drugs from 2028; all new medicines from 2030)? If in scope, identify the likely JCA timeline, the comparator selection under the JCA framework, and the outcomes most likely to be weighted. (2) National HTA bodies of first order — for each of NICE (UK), G-BA/IQWiG (Germany), HAS/Transparency Commission (France), AIFA (Italy), and NIPN/CDF (Spain), state the typical time from EMA approval to national reimbursement decision, the evidence bar for a positive recommendation, and the most recent precedent decision in the therapeutic area. (3) Germany specifically — the AMNOG process governs launch pricing; a negative G-BA additional benefit assessment triggers price negotiation at or near comparator level, materially affecting the European revenue mix. State the realistic additional benefit category (major, considerable, minor, non-quantifiable, no additional benefit, less benefit) and its pricing implication. (4) England specifically — NICE cost-effectiveness threshold (£20,000–£30,000 per QALY base case, higher for end-of-life or highly specialised technologies), Cancer Drugs Fund eligibility for oncology, and the NHS England commercial negotiation process. (5) Revenue bridge — translate the HTA outcomes into a European revenue forecast, explicit on the country-level price, volume, and time-to-reimbursement. Model the realistic scenario where one or two major markets reach a restrictive HTA outcome and the others follow, because HTA outcomes often cluster. (6) Thesis delta — how does the European HTA pathway position affect the global peak sales assumption, the Europe-as-share-of-total forecast, and the launch cadence? Flag any name where a negative European outcome would materially change the investment case. End with confidence score.
```

---

### INTL-02  Japanese Reimbursement Cycle and Price Revision Analysis

```yaml
id: INTL-02
title: Japanese Reimbursement Cycle and Price Revision Analysis
tags: [#international, #pharma, #biotech, #medtech, #senior-judgment]
use_when: "When Japan represents a material share of revenue or launch optionality for a drug or device, given Japan's distinctive biennial price revision cycle and foreign-price referencing system."
reasoning: "PMDA status → biennial revision → forecast → monitor"
inputs: "Company Japan-segment disclosure, PMDA filing status, NHI price list, prior biennial revision history, Chuikyo minutes for medtech."
output: "Japan reimbursement analysis with price revision forecast, asset-level exposure, and revenue trajectory."
```

**Reasoning scaffold:** PMDA status → biennial revision → forecast → monitor

**Prompt:**
```
Analyse [TICKER]'s Japan exposure. (1) PMDA approval and NHI listing — for each marketed or pipeline asset with Japanese exposure, the PMDA approval status, the time from PMDA approval to National Health Insurance (NHI) price listing (typically 60–90 days), and the premium or discount vs international reference prices at launch. (2) Biennial price revision — Japan revises NHI prices every two years (April in even years), with revisions driven by market-expansion redetermination (a price cut triggered when actual sales exceed forecast by defined thresholds), foreign average price adjustment, and the generic-substitution promotion mechanism. For each Japanese-exposed asset, estimate the next revision's directional impact and magnitude. The market-expansion redetermination is particularly relevant for oncology and orphan drugs where actual uptake exceeds the forecast embedded in the original price. (3) G1/G2 long-listed products — for legacy assets past their initial exclusivity period, model the accelerated price decline under the G1/G2 reclassification. (4) Cost-effectiveness programme — Japan's HTA mechanism applies to a subset of high-cost products (generally JPY 10B+ annual sales). Identify any asset entering the scope and the realistic cost-effectiveness outcome. (5) Medtech pricing — Japan's reimbursement for devices operates on a separate cycle via the Chuikyo process, with foreign average price comparison driving periodic adjustments. For medtech names with Japan exposure, state the equivalent exposure. (6) Japan-as-share-of-total — current Japan contribution to revenue, and how the biennial revision cycle affects the forward trajectory. Japan tends to step down revenue predictably; the surprise comes when it steps down faster than consensus models. End with confidence score.
```

---

### INTL-03  Chinese Biotech Licensing Economics and BIOSECURE Pass-Through

```yaml
id: INTL-03
title: Chinese Biotech Licensing Economics and BIOSECURE Pass-Through
tags: [#international, #biotech, #pharma, #senior-judgment]
use_when: "When evaluating a Chinese biotech, a Western company that has licensed an asset from a Chinese biotech, or the downstream effects of the US BIOSECURE Act on Chinese contract services."
reasoning: "licensing economics → NMPA status → BIOSECURE exposure → model"
inputs: "Licensing deal terms if disclosed, NMPA approval history, BIOSECURE Act final text and enforcement status, NRDL negotiation outcomes, Hong Kong or ADR listing documentation."
output: "China exposure analysis with licensing economics, regulatory pathway, BIOSECURE pass-through, and competitive dynamics."
```

**Reasoning scaffold:** licensing economics → NMPA status → BIOSECURE exposure → model

**Prompt:**
```
Analyse [TICKER]'s exposure to China biotech dynamics. (1) Licensing economics — if the asset is licensed in or out of China, state the deal structure: upfront, milestones, royalty rate, territory split, development cost responsibility. Compare to comparable deals in the therapeutic area. Chinese biotech licensing-out to Western partners has become a materially larger source of innovation since 2022; quantify if relevant. (2) NMPA approval dynamics — for Chinese-origin assets pursuing US or EU approval, state the NMPA approval status, the quality of the Chinese clinical package, and the realistic probability that FDA or EMA will accept the Chinese data. The FDA's position on single-country trials from China has evolved materially (the 2022 Innovent/LLY sintilimab precedent). Recent FDA guidance and AdCom outcomes should anchor the expectation. (3) BIOSECURE Act pass-through — for any Western company with exposure to named Chinese entities (WuXi AppTec, WuXi Biologics, BGI, MGI, Complete Genomics), quantify the revenue, capacity, or R&D dependency and the realistic transition timeline. The act's enforcement mechanism is procurement restriction, not a blanket ban. (4) China domestic market exposure — for assets marketed in China, state the NRDL inclusion status, the price negotiation outcome (Chinese NRDL negotiation typically extracts 50–70 per cent price discount vs international markets), and the volume commitment that comes with NRDL inclusion. (5) Competitive landscape in China — Chinese domestic biotech development has accelerated in oncology, immunology, and metabolic disease. For Western names competing in China, quantify the share loss risk. (6) Currency and capital flow — for Chinese-origin names listed in Hong Kong or via VIE structures in the US, the PCAOB audit resolution, HFCAA delisting risk, and USD repatriation constraints. End with confidence score.
```

---

### INTL-04  UK-Specific Healthcare Dynamics for a London-Based Global Mandate

```yaml
id: INTL-04
title: UK-Specific Healthcare Dynamics for a London-Based Global Mandate
tags: [#international, #cross-sector, #senior-judgment]
use_when: "When a London-based analyst needs to assess UK-specific healthcare dynamics for either a UK-listed name or a global name with material UK exposure, particularly given Brexit-era regulatory divergence and NHS-specific purchasing dynamics."
reasoning: "MHRA-EMA divergence → NHS dynamics → VPAG rebate → listing context"
inputs: "Company UK segment disclosure, NICE/SMC decisions, VPAG rebate provisions, MHRA approval documentation, NHS Supply Chain contracts if public."
output: "UK exposure analysis with regulatory pathway, HTA position, NHS commercial dynamics, sustainability exposure, and listing considerations."
```

**Reasoning scaffold:** MHRA-EMA divergence → NHS dynamics → VPAG rebate → listing context

**Prompt:**
```
Assess [TICKER]'s UK-specific healthcare exposure. (1) MHRA vs EMA divergence — since Brexit, the MHRA operates as an independent regulator. For drug approvals, the MHRA has introduced the International Recognition Procedure (IRP) relying on approvals from FDA, EMA, Health Canada, TGA, Swissmedic, MFDS, and Singapore HSA. Identify the approval route the company has pursued and any UK-specific label divergence. For devices, the UKCA mark regime (initially scheduled to replace CE, then extended to accept CE until 2028 or 2030 depending on class) creates temporary regulatory duality. (2) NICE and SMC — England and Wales HTA runs through NICE; Scotland runs through SMC. Both are internationally referenced and influential beyond the UK market, particularly in Commonwealth countries. A negative NICE outcome has commercial consequences materially larger than the UK alone. (3) NHS purchasing dynamics — for drugs, the NHS Commercial Medicines Unit and the Voluntary Scheme for Pricing and Access (VPAS/VPAG) govern volume-price relationships; the VPAG successor scheme introduced from 2024 caps total branded medicine sales growth at 2 per cent with rebates for excess. Quantify the company's VPAG rebate exposure. For devices, the NHS Supply Chain procurement approach is increasingly centralised. (4) NHS capacity and waitlist dynamics — elective procedure waitlists have structural implications for medtech and for some specialty pharma (cancer, cardiovascular). Current NHS England elective waitlist status and the Elective Recovery Plan trajectory affect procedure-driven volumes. (5) UK sustainability and net-zero NHS — NHS England's target for a net-zero NHS by 2040 (for emissions the NHS controls directly) is influencing procurement via carbon footprint considerations. This is a commercial consideration for energy-intensive manufacturing and single-use devices. (6) Listing and tax — for UK-listed healthcare companies, the recent FTSE healthcare delisting trend (AstraZeneca-to-US speculation, AVEVA, Arm), LSE reforms, and UK pension fund mandate reform (Mansion House reforms) affect liquidity and valuation multiples. End with confidence score.
```

---

## Appendix A — Tag Index

### Workflow

**#initiation** — **INIT-01** 30-Minute Name Scoping Memo, **INIT-02** Full Initiation Memo Skeleton, **INIT-03** Variant Perception Generator, **INIT-04** Industry Primer in 90 Minutes, **INIT-05** Bull / Base / Bear Decomposition with Probability Weights, **INIT-06** Biotech-Specific Initiation Layer, **INIT-07** Medtech-Specific Initiation Layer, **SS-02** Initiation Note Decoder

**#earnings-preview** — **EARN-01** Earnings Preview Note (T-7), **EARN-02** Buy-Side KPI Tracker Build

**#earnings-post** — **EARN-03** Live-Call Triage Sheet, **EARN-04** Post-Print Thesis Update Memo, **EARN-05** Guide Decomposition and Path-to-Number Test, **EARN-06** Biotech Quarterly Cash and Catalyst Refresh, **EARN-07** Managed Care MLR Bridge, **SS-03** Conference Call Cross-Read, **COMM-03** Quick-Reaction Internal Note, **SUB-PHA-03** TRx vs NRx Divergence Monitor, **SUB-SVC-01** Hospital Operator Earnings Cross-Read

**#mgmt-meeting** — **MGMT-01** 1-on-1 Question Stack, **MGMT-02** What Has Already Been Asked? Filter, **MGMT-03** Site Visit Brief, **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **ESG-02** Stewardship Engagement Plan

**#modeling** — **INIT-05** Bull / Base / Bear Decomposition with Probability Weights, **EARN-05** Guide Decomposition and Path-to-Number Test, **MOD-01** DCF Stress Test and Reverse-Engineer, **MOD-02** Sum-of-the-Parts for Diversified Pharma or Medtech, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **MOD-04** Patent Cliff and LOE Bridge for Large-Cap Pharma, **MOD-05** Medtech Razor-Blade Model, **MOD-06** Tools and Diagnostics Capex-Cycle Model, **MOD-07** MA Star Ratings and Bid Cycle Model, **MOD-08** Digital Health Unit Economics Stress Test, **MOD-09** Working Capital and Cash Conversion Forensics, **MOD-10** Scenario Construction as a Discipline, **SUB-BIO-05** CMC and COGS Scalability Check, **SUB-PHA-04** Gross-to-Net (GTN) Margin Erosion Analysis, **SUB-PHA-05** Biosimilar Erosion Curve Modeller, **SUB-MED-05** Average Selling Price (ASP) Deflation Analysis, **SUB-SVC-03** Vertical Integration MLR Shifting, **SUB-SVC-04** Value-Based Care Capitation Tracking, **SUB-TLS-02** NGS Instrument vs Consumables Mix Forecast, **SUB-TLS-04** IVD Reagent Pull-Through Rate Calculator

**#thesis** — **INIT-03** Variant Perception Generator, **INIT-05** Bull / Base / Bear Decomposition with Probability Weights, **MOD-10** Scenario Construction as a Discipline, **THES-01** Pre-Mortem on a Long Thesis, **THES-02** Steel-Man the Short Case, **THES-03** Thesis Decomposition into Testable Claims, **THES-04** Regime Map Stress Test, **THES-05** Disconfirming Evidence Search Plan, **EN-04** Expert-Management Divergence Triangulation, **PORT-03** Pair Trade Construction, **SUB-BIO-01** Phase 3 Readout Pre-Mortem, **SUB-BIO-06** Freedom to Operate (FTO) IP Analysis, **SUB-PHA-01** Pipeline Replenishment Audit, **SUB-DIG-02** AI/ML in Healthcare Investability Test

**#sell-discipline** — **SELL-01** Sell Discipline Scorecard, **SELL-02** Thesis-Breaking Signal Watchlist, **SELL-04** Single-Name Thesis Post-Mortem, **SELL-05** Book-Wide Annual Post-Mortem and Process Audit

**#risk** — **THES-02** Steel-Man the Short Case, **THES-05** Disconfirming Evidence Search Plan, **SELL-01** Sell Discipline Scorecard, **SELL-02** Thesis-Breaking Signal Watchlist, **SELL-03** Position Sizing Sanity Check, **PORT-02** Catalyst Concentration and Path Dependence Map, **PORT-04** Borrow, Float, and Short Interest Analysis

**#sell-side-synth** — **SS-01** Multi-Broker Note Triangulation, **SS-02** Initiation Note Decoder, **SS-03** Conference Call Cross-Read

**#expert-network** — **THES-05** Disconfirming Evidence Search Plan, **EN-01** Expert Call Prep Brief, **EN-02** Post-Call Debrief and Triangulation, **EN-03** Expert Network Scoping Plan, **EN-04** Expert-Management Divergence Triangulation, **SUB-DIG-01** Enterprise Health-Tech Sales Cycle Diligence

**#screen** — **SCR-01** Bloomberg / FactSet Healthcare Idea Screen Builder, **SCR-02** Catalyst Calendar Screen, **SCR-03** Hidden Compounder Screen, **SCR-04** Thematic Beneficiary Screen, **SCR-05** Activist Investor Target Screen, **SCR-06** 13F Institutional Ownership Delta Scanner, **SCR-07** Cross-Sector Correlation Identifier

**#thematic** — **INIT-04** Industry Primer in 90 Minutes, **THES-04** Regime Map Stress Test, **SCR-04** Thematic Beneficiary Screen, **THM-01** Theme Validation Framework, **THM-02** TAM Bottoms-Up Build, **THM-03** Thematic Basket Construction, **SUB-PHA-02** GLP-1 Class Dynamics Map, **SUB-TLS-01** Bioprocessing Cycle Tracker, **SUB-DIG-02** AI/ML in Healthcare Investability Test

**#portfolio** — **SELL-03** Position Sizing Sanity Check, **SELL-05** Book-Wide Annual Post-Mortem and Process Audit, **SCR-07** Cross-Sector Correlation Identifier, **THM-03** Thematic Basket Construction, **PORT-01** Healthcare Sleeve Positioning Review, **PORT-02** Catalyst Concentration and Path Dependence Map, **PORT-03** Pair Trade Construction, **PORT-04** Borrow, Float, and Short Interest Analysis, **PORT-05** Constructive Disagreement with Portfolio Manager on Sizing or Thesis, **PORT-06** Defending a Contrarian Thesis at Investment Committee

**#esg** — **ESG-01** Healthcare Materiality Map, **ESG-02** Stewardship Engagement Plan, **ESG-03** Drug Pricing and IRA Exposure Map, **ESG-04** Access to Medicine Index and EM Pricing Strategy Review, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **SUB-DIG-03** Health Equity and Digital Divide Assessment

**#client-comms** — **PORT-06** Defending a Contrarian Thesis at Investment Committee, **COMM-01** IC Memo Draft, **COMM-02** Quarterly Letter Section Draft, **COMM-03** Quick-Reaction Internal Note, **COMM-04** Translate Technical Biology for Generalist PMs, **COMM-05** MNPI Scrubbing Audit for Client Communications, **COMM-06** Disclosure and Conflict of Interest Check, **COMM-07** Public Speaking and Conference Pre-Flight

**#compliance** — **COMM-05** MNPI Scrubbing Audit for Client Communications, **COMM-06** Disclosure and Conflict of Interest Check, **COMM-07** Public Speaking and Conference Pre-Flight

**#data-extraction** — **TECH-01** Bloomberg BQL Syntax Generator for Healthcare, **TECH-02** Bloomberg Catalyst and Event Calendar Query, **TECH-03** FactSet Universal Screening for Healthcare, **TECH-04** FactSet Document Search for Transcript Mining, **TECH-05** SEC EDGAR Autonomous Agent Configuration, **TECH-06** ClinicalTrials.gov Agent Query Construction

**#post-mortem** — **SELL-04** Single-Name Thesis Post-Mortem, **SELL-05** Book-Wide Annual Post-Mortem and Process Audit

**#people-dynamics** — **PORT-05** Constructive Disagreement with Portfolio Manager on Sizing or Thesis, **PORT-06** Defending a Contrarian Thesis at Investment Committee

### Sub-sector

**#biotech** — **INIT-06** Biotech-Specific Initiation Layer, **EARN-06** Biotech Quarterly Cash and Catalyst Refresh, **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **SCR-02** Catalyst Calendar Screen, **PORT-02** Catalyst Concentration and Path Dependence Map, **ESG-03** Drug Pricing and IRA Exposure Map, **COMM-04** Translate Technical Biology for Generalist PMs, **SUB-BIO-01** Phase 3 Readout Pre-Mortem, **SUB-BIO-02** FDA AdCom Prep, **SUB-BIO-03** Conference Abstract Triage, **SUB-BIO-04** Target Product Profile (TPP) Interrogation, **SUB-BIO-05** CMC and COGS Scalability Check, **SUB-BIO-06** Freedom to Operate (FTO) IP Analysis, **SUB-BIO-07** FDA Meeting History Risk Extraction, **SUB-BIO-08** Post-Approval Label Delta Analyser, **SUB-TLS-05** Companion Diagnostic Linkage and Precision Medicine Coupling, **TECH-02** Bloomberg Catalyst and Event Calendar Query, **TECH-06** ClinicalTrials.gov Agent Query Construction, **INTL-01** European HTA Pathway Mapping, **INTL-02** Japanese Reimbursement Cycle and Price Revision Analysis, **INTL-03** Chinese Biotech Licensing Economics and BIOSECURE Pass-Through

**#pharma** — **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **MOD-02** Sum-of-the-Parts for Diversified Pharma or Medtech, **MOD-04** Patent Cliff and LOE Bridge for Large-Cap Pharma, **ESG-03** Drug Pricing and IRA Exposure Map, **ESG-04** Access to Medicine Index and EM Pricing Strategy Review, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **SUB-BIO-03** Conference Abstract Triage, **SUB-BIO-08** Post-Approval Label Delta Analyser, **SUB-PHA-01** Pipeline Replenishment Audit, **SUB-PHA-02** GLP-1 Class Dynamics Map, **SUB-PHA-03** TRx vs NRx Divergence Monitor, **SUB-PHA-04** Gross-to-Net (GTN) Margin Erosion Analysis, **SUB-PHA-05** Biosimilar Erosion Curve Modeller, **SUB-TLS-05** Companion Diagnostic Linkage and Precision Medicine Coupling, **INTL-01** European HTA Pathway Mapping, **INTL-02** Japanese Reimbursement Cycle and Price Revision Analysis, **INTL-03** Chinese Biotech Licensing Economics and BIOSECURE Pass-Through

**#medtech** — **INIT-07** Medtech-Specific Initiation Layer, **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **MOD-02** Sum-of-the-Parts for Diversified Pharma or Medtech, **MOD-05** Medtech Razor-Blade Model, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **SUB-MED-01** Procedure Volume Recovery Tracker, **SUB-MED-02** Reimbursement and Coding Change Impact, **SUB-MED-03** 510(k) Predicate Validity Check, **SUB-MED-04** De Novo vs PMA Regulatory Pathway Risk, **SUB-MED-05** Average Selling Price (ASP) Deflation Analysis, **SUB-SVC-01** Hospital Operator Earnings Cross-Read, **INTL-01** European HTA Pathway Mapping, **INTL-02** Japanese Reimbursement Cycle and Price Revision Analysis

**#services-payors** — **EARN-07** Managed Care MLR Bridge, **MOD-07** MA Star Ratings and Bid Cycle Model, **SUB-SVC-01** Hospital Operator Earnings Cross-Read, **SUB-SVC-02** Medicare Advantage Bid Cycle Tracker, **SUB-SVC-03** Vertical Integration MLR Shifting, **SUB-SVC-04** Value-Based Care Capitation Tracking

**#tools-dx** — **MOD-06** Tools and Diagnostics Capex-Cycle Model, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **SUB-TLS-01** Bioprocessing Cycle Tracker, **SUB-TLS-02** NGS Instrument vs Consumables Mix Forecast, **SUB-TLS-03** LDT Regulatory Oversight Impact, **SUB-TLS-04** IVD Reagent Pull-Through Rate Calculator, **SUB-TLS-05** Companion Diagnostic Linkage and Precision Medicine Coupling

**#digital-health** — **MOD-08** Digital Health Unit Economics Stress Test, **SUB-DIG-01** Enterprise Health-Tech Sales Cycle Diligence, **SUB-DIG-02** AI/ML in Healthcare Investability Test, **SUB-DIG-03** Health Equity and Digital Divide Assessment

**#cross-sector** — **INIT-01** 30-Minute Name Scoping Memo, **INIT-02** Full Initiation Memo Skeleton, **INIT-03** Variant Perception Generator, **INIT-04** Industry Primer in 90 Minutes, **INIT-05** Bull / Base / Bear Decomposition with Probability Weights, **EARN-01** Earnings Preview Note (T-7), **EARN-02** Buy-Side KPI Tracker Build, **EARN-03** Live-Call Triage Sheet, **EARN-04** Post-Print Thesis Update Memo, **EARN-05** Guide Decomposition and Path-to-Number Test, **MGMT-01** 1-on-1 Question Stack, **MGMT-02** What Has Already Been Asked? Filter, **MGMT-03** Site Visit Brief, **MOD-01** DCF Stress Test and Reverse-Engineer, **MOD-09** Working Capital and Cash Conversion Forensics, **MOD-10** Scenario Construction as a Discipline, **THES-01** Pre-Mortem on a Long Thesis, **THES-02** Steel-Man the Short Case, **THES-03** Thesis Decomposition into Testable Claims, **THES-04** Regime Map Stress Test, **THES-05** Disconfirming Evidence Search Plan, **SELL-01** Sell Discipline Scorecard, **SELL-02** Thesis-Breaking Signal Watchlist, **SELL-03** Position Sizing Sanity Check, **SELL-04** Single-Name Thesis Post-Mortem, **SS-01** Multi-Broker Note Triangulation, **SS-02** Initiation Note Decoder, **SS-03** Conference Call Cross-Read, **EN-01** Expert Call Prep Brief, **EN-02** Post-Call Debrief and Triangulation, **EN-03** Expert Network Scoping Plan, **EN-04** Expert-Management Divergence Triangulation, **SCR-01** Bloomberg / FactSet Healthcare Idea Screen Builder, **SCR-03** Hidden Compounder Screen, **SCR-04** Thematic Beneficiary Screen, **SCR-05** Activist Investor Target Screen, **SCR-06** 13F Institutional Ownership Delta Scanner, **SCR-07** Cross-Sector Correlation Identifier, **THM-01** Theme Validation Framework, **THM-02** TAM Bottoms-Up Build, **THM-03** Thematic Basket Construction, **PORT-01** Healthcare Sleeve Positioning Review, **PORT-02** Catalyst Concentration and Path Dependence Map, **PORT-03** Pair Trade Construction, **PORT-04** Borrow, Float, and Short Interest Analysis, **PORT-05** Constructive Disagreement with Portfolio Manager on Sizing or Thesis, **PORT-06** Defending a Contrarian Thesis at Investment Committee, **ESG-01** Healthcare Materiality Map, **ESG-02** Stewardship Engagement Plan, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **COMM-01** IC Memo Draft, **COMM-02** Quarterly Letter Section Draft, **COMM-03** Quick-Reaction Internal Note, **COMM-04** Translate Technical Biology for Generalist PMs, **COMM-05** MNPI Scrubbing Audit for Client Communications, **COMM-06** Disclosure and Conflict of Interest Check, **COMM-07** Public Speaking and Conference Pre-Flight, **SUB-MED-01** Procedure Volume Recovery Tracker, **TECH-01** Bloomberg BQL Syntax Generator for Healthcare, **TECH-03** FactSet Universal Screening for Healthcare, **TECH-04** FactSet Document Search for Transcript Mining, **TECH-05** SEC EDGAR Autonomous Agent Configuration, **INTL-04** UK-Specific Healthcare Dynamics for a London-Based Global Mandate

**#international** — **INTL-01** European HTA Pathway Mapping, **INTL-02** Japanese Reimbursement Cycle and Price Revision Analysis, **INTL-03** Chinese Biotech Licensing Economics and BIOSECURE Pass-Through, **INTL-04** UK-Specific Healthcare Dynamics for a London-Based Global Mandate

### Data/Tool

**#bloomberg** — **INIT-01** 30-Minute Name Scoping Memo, **SCR-01** Bloomberg / FactSet Healthcare Idea Screen Builder, **SCR-03** Hidden Compounder Screen, **SCR-07** Cross-Sector Correlation Identifier, **PORT-04** Borrow, Float, and Short Interest Analysis, **TECH-01** Bloomberg BQL Syntax Generator for Healthcare, **TECH-02** Bloomberg Catalyst and Event Calendar Query

**#factset** — **SCR-01** Bloomberg / FactSet Healthcare Idea Screen Builder, **TECH-03** FactSet Universal Screening for Healthcare, **TECH-04** FactSet Document Search for Transcript Mining

**#ctgov** — **INIT-06** Biotech-Specific Initiation Layer, **EARN-06** Biotech Quarterly Cash and Catalyst Refresh, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **SCR-02** Catalyst Calendar Screen, **SUB-BIO-01** Phase 3 Readout Pre-Mortem, **TECH-06** ClinicalTrials.gov Agent Query Construction

**#sec-filings** — **INIT-01** 30-Minute Name Scoping Memo, **INIT-02** Full Initiation Memo Skeleton, **EARN-02** Buy-Side KPI Tracker Build, **EARN-04** Post-Print Thesis Update Memo, **EARN-06** Biotech Quarterly Cash and Catalyst Refresh, **EARN-07** Managed Care MLR Bridge, **MGMT-01** 1-on-1 Question Stack, **MGMT-03** Site Visit Brief, **MOD-04** Patent Cliff and LOE Bridge for Large-Cap Pharma, **MOD-05** Medtech Razor-Blade Model, **MOD-06** Tools and Diagnostics Capex-Cycle Model, **MOD-08** Digital Health Unit Economics Stress Test, **MOD-09** Working Capital and Cash Conversion Forensics, **SCR-05** Activist Investor Target Screen, **SCR-06** 13F Institutional Ownership Delta Scanner, **SUB-PHA-01** Pipeline Replenishment Audit, **TECH-05** SEC EDGAR Autonomous Agent Configuration

**#sell-side** — **INIT-02** Full Initiation Memo Skeleton, **INIT-03** Variant Perception Generator, **EARN-01** Earnings Preview Note (T-7), **THES-02** Steel-Man the Short Case, **SS-01** Multi-Broker Note Triangulation, **SS-02** Initiation Note Decoder, **SUB-MED-01** Procedure Volume Recovery Tracker

**#transcripts** — **EARN-01** Earnings Preview Note (T-7), **EARN-02** Buy-Side KPI Tracker Build, **EARN-03** Live-Call Triage Sheet, **EARN-04** Post-Print Thesis Update Memo, **EARN-05** Guide Decomposition and Path-to-Number Test, **MGMT-01** 1-on-1 Question Stack, **MGMT-02** What Has Already Been Asked? Filter, **SS-03** Conference Call Cross-Read, **SUB-SVC-01** Hospital Operator Earnings Cross-Read

**#expert-network** — **THES-05** Disconfirming Evidence Search Plan, **EN-01** Expert Call Prep Brief, **EN-02** Post-Call Debrief and Triangulation, **EN-03** Expert Network Scoping Plan, **EN-04** Expert-Management Divergence Triangulation, **SUB-DIG-01** Enterprise Health-Tech Sales Cycle Diligence

**#pubmed** — **INIT-06** Biotech-Specific Initiation Layer, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **SUB-BIO-01** Phase 3 Readout Pre-Mortem, **SUB-BIO-03** Conference Abstract Triage

**#fda-ema** — **INIT-06** Biotech-Specific Initiation Layer, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **SCR-02** Catalyst Calendar Screen, **SUB-BIO-02** FDA AdCom Prep, **SUB-BIO-04** Target Product Profile (TPP) Interrogation, **SUB-BIO-07** FDA Meeting History Risk Extraction, **SUB-BIO-08** Post-Approval Label Delta Analyser, **SUB-MED-03** 510(k) Predicate Validity Check, **SUB-MED-04** De Novo vs PMA Regulatory Pathway Risk, **SUB-TLS-03** LDT Regulatory Oversight Impact

**#cms** — **INIT-07** Medtech-Specific Initiation Layer, **EARN-07** Managed Care MLR Bridge, **MOD-07** MA Star Ratings and Bid Cycle Model, **ESG-03** Drug Pricing and IRA Exposure Map, **SUB-MED-01** Procedure Volume Recovery Tracker, **SUB-MED-02** Reimbursement and Coding Change Impact, **SUB-SVC-02** Medicare Advantage Bid Cycle Tracker

**#ir-materials** — **INIT-07** Medtech-Specific Initiation Layer, **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **SUB-PHA-01** Pipeline Replenishment Audit

**#reasoning-only** — **INIT-04** Industry Primer in 90 Minutes

**#bql** — **TECH-01** Bloomberg BQL Syntax Generator for Healthcare, **TECH-02** Bloomberg Catalyst and Event Calendar Query

**#fql** — **TECH-03** FactSet Universal Screening for Healthcare, **TECH-04** FactSet Document Search for Transcript Mining

### Complexity

**#junior-task** — **INIT-01** 30-Minute Name Scoping Memo, **INIT-04** Industry Primer in 90 Minutes, **EARN-02** Buy-Side KPI Tracker Build, **MGMT-02** What Has Already Been Asked? Filter, **SS-02** Initiation Note Decoder, **COMM-06** Disclosure and Conflict of Interest Check, **SUB-MED-01** Procedure Volume Recovery Tracker, **TECH-01** Bloomberg BQL Syntax Generator for Healthcare

**#senior-judgment** — **INIT-02** Full Initiation Memo Skeleton, **INIT-03** Variant Perception Generator, **INIT-05** Bull / Base / Bear Decomposition with Probability Weights, **INIT-06** Biotech-Specific Initiation Layer, **INIT-07** Medtech-Specific Initiation Layer, **EARN-01** Earnings Preview Note (T-7), **EARN-03** Live-Call Triage Sheet, **EARN-04** Post-Print Thesis Update Memo, **EARN-05** Guide Decomposition and Path-to-Number Test, **EARN-06** Biotech Quarterly Cash and Catalyst Refresh, **EARN-07** Managed Care MLR Bridge, **MGMT-01** 1-on-1 Question Stack, **MGMT-03** Site Visit Brief, **MGMT-04** KOL Day / Capital Markets Day Pre-Read, **MOD-01** DCF Stress Test and Reverse-Engineer, **MOD-02** Sum-of-the-Parts for Diversified Pharma or Medtech, **MOD-03** Risk-Adjusted NPV (rNPV) Model for a Biotech Asset, **MOD-04** Patent Cliff and LOE Bridge for Large-Cap Pharma, **MOD-05** Medtech Razor-Blade Model, **MOD-06** Tools and Diagnostics Capex-Cycle Model, **MOD-07** MA Star Ratings and Bid Cycle Model, **MOD-08** Digital Health Unit Economics Stress Test, **MOD-09** Working Capital and Cash Conversion Forensics, **MOD-10** Scenario Construction as a Discipline, **THES-01** Pre-Mortem on a Long Thesis, **THES-02** Steel-Man the Short Case, **THES-03** Thesis Decomposition into Testable Claims, **THES-04** Regime Map Stress Test, **THES-05** Disconfirming Evidence Search Plan, **SELL-02** Thesis-Breaking Signal Watchlist, **SELL-04** Single-Name Thesis Post-Mortem, **SS-01** Multi-Broker Note Triangulation, **SS-03** Conference Call Cross-Read, **EN-01** Expert Call Prep Brief, **EN-02** Post-Call Debrief and Triangulation, **EN-03** Expert Network Scoping Plan, **EN-04** Expert-Management Divergence Triangulation, **SCR-01** Bloomberg / FactSet Healthcare Idea Screen Builder, **SCR-02** Catalyst Calendar Screen, **SCR-03** Hidden Compounder Screen, **SCR-04** Thematic Beneficiary Screen, **SCR-05** Activist Investor Target Screen, **SCR-06** 13F Institutional Ownership Delta Scanner, **SCR-07** Cross-Sector Correlation Identifier, **THM-01** Theme Validation Framework, **THM-02** TAM Bottoms-Up Build, **PORT-03** Pair Trade Construction, **PORT-04** Borrow, Float, and Short Interest Analysis, **PORT-05** Constructive Disagreement with Portfolio Manager on Sizing or Thesis, **PORT-06** Defending a Contrarian Thesis at Investment Committee, **ESG-01** Healthcare Materiality Map, **ESG-02** Stewardship Engagement Plan, **ESG-03** Drug Pricing and IRA Exposure Map, **ESG-04** Access to Medicine Index and EM Pricing Strategy Review, **ESG-05** Healthcare Climate Risk and Decarbonisation Pathway Assessment, **COMM-01** IC Memo Draft, **COMM-02** Quarterly Letter Section Draft, **COMM-03** Quick-Reaction Internal Note, **COMM-04** Translate Technical Biology for Generalist PMs, **COMM-05** MNPI Scrubbing Audit for Client Communications, **COMM-07** Public Speaking and Conference Pre-Flight, **SUB-BIO-01** Phase 3 Readout Pre-Mortem, **SUB-BIO-02** FDA AdCom Prep, **SUB-BIO-03** Conference Abstract Triage, **SUB-BIO-04** Target Product Profile (TPP) Interrogation, **SUB-BIO-05** CMC and COGS Scalability Check, **SUB-BIO-06** Freedom to Operate (FTO) IP Analysis, **SUB-BIO-07** FDA Meeting History Risk Extraction, **SUB-BIO-08** Post-Approval Label Delta Analyser, **SUB-PHA-01** Pipeline Replenishment Audit, **SUB-PHA-02** GLP-1 Class Dynamics Map, **SUB-PHA-03** TRx vs NRx Divergence Monitor, **SUB-PHA-04** Gross-to-Net (GTN) Margin Erosion Analysis, **SUB-PHA-05** Biosimilar Erosion Curve Modeller, **SUB-MED-02** Reimbursement and Coding Change Impact, **SUB-MED-03** 510(k) Predicate Validity Check, **SUB-MED-04** De Novo vs PMA Regulatory Pathway Risk, **SUB-MED-05** Average Selling Price (ASP) Deflation Analysis, **SUB-SVC-01** Hospital Operator Earnings Cross-Read, **SUB-SVC-02** Medicare Advantage Bid Cycle Tracker, **SUB-SVC-03** Vertical Integration MLR Shifting, **SUB-SVC-04** Value-Based Care Capitation Tracking, **SUB-TLS-01** Bioprocessing Cycle Tracker, **SUB-TLS-02** NGS Instrument vs Consumables Mix Forecast, **SUB-TLS-03** LDT Regulatory Oversight Impact, **SUB-TLS-04** IVD Reagent Pull-Through Rate Calculator, **SUB-TLS-05** Companion Diagnostic Linkage and Precision Medicine Coupling, **SUB-DIG-01** Enterprise Health-Tech Sales Cycle Diligence, **SUB-DIG-02** AI/ML in Healthcare Investability Test, **SUB-DIG-03** Health Equity and Digital Divide Assessment, **TECH-02** Bloomberg Catalyst and Event Calendar Query, **TECH-03** FactSet Universal Screening for Healthcare, **TECH-04** FactSet Document Search for Transcript Mining, **TECH-05** SEC EDGAR Autonomous Agent Configuration, **TECH-06** ClinicalTrials.gov Agent Query Construction, **INTL-01** European HTA Pathway Mapping, **INTL-02** Japanese Reimbursement Cycle and Price Revision Analysis, **INTL-03** Chinese Biotech Licensing Economics and BIOSECURE Pass-Through, **INTL-04** UK-Specific Healthcare Dynamics for a London-Based Global Mandate

**#pm-level** — **INIT-03** Variant Perception Generator, **MOD-10** Scenario Construction as a Discipline, **THES-01** Pre-Mortem on a Long Thesis, **THES-04** Regime Map Stress Test, **SELL-01** Sell Discipline Scorecard, **SELL-03** Position Sizing Sanity Check, **SELL-04** Single-Name Thesis Post-Mortem, **SELL-05** Book-Wide Annual Post-Mortem and Process Audit, **EN-03** Expert Network Scoping Plan, **EN-04** Expert-Management Divergence Triangulation, **SCR-03** Hidden Compounder Screen, **THM-01** Theme Validation Framework, **THM-03** Thematic Basket Construction, **PORT-01** Healthcare Sleeve Positioning Review, **PORT-02** Catalyst Concentration and Path Dependence Map, **PORT-06** Defending a Contrarian Thesis at Investment Committee, **ESG-02** Stewardship Engagement Plan, **COMM-01** IC Memo Draft, **SUB-SVC-02** Medicare Advantage Bid Cycle Tracker, **SUB-DIG-02** AI/ML in Healthcare Investability Test

---

## Appendix B — Workflow Chains

Suggested prompt sequences for end-to-end workflows. Prompt IDs are hyperlinked to their full definitions.

### New Coverage Initiation Chain

1. [INIT-01](#init-01-30-minute-name-scoping-memo) (scope in 30 minutes)
2. [INIT-04](#init-04-industry-primer-in-90-minutes) (industry primer if unfamiliar)
3. [INIT-02](#init-02-full-initiation-memo-skeleton) (full memo skeleton)
4. [INIT-06](#init-06-biotech-specific-initiation-layer) or [INIT-07](#init-07-medtech-specific-initiation-layer) (sub-sector layer)
5. [MOD-03](#mod-03-risk-adjusted-npv-rnpv-model-for-a-biotech-asset) / [MOD-04](#mod-04-patent-cliff-and-loe-bridge-for-large-cap-pharma) / [MOD-05](#mod-05-medtech-razor-blade-model) / [MOD-07](#mod-07-ma-star-ratings-and-bid-cycle-model) / [MOD-08](#mod-08-digital-health-unit-economics-stress-test) (sub-sector model)
6. [INIT-03](#init-03-variant-perception-generator) (variant perception)
7. [INIT-05](#init-05-bull-base-bear-decomposition-with-probability-weights) (scenarios)
8. [ESG-01](#esg-01-healthcare-materiality-map) (materiality)
9. [COMM-01](#comm-01-ic-memo-draft) (IC memo)

### Quarterly Earnings Cycle Chain

1. [EARN-02](#earn-02-buy-side-kpi-tracker-build) (KPI tracker — once)
2. [EARN-01](#earn-01-earnings-preview-note-t-7) (preview T-7)
3. [EARN-03](#earn-03-live-call-triage-sheet) (live triage sheet on call)
4. [EARN-04](#earn-04-post-print-thesis-update-memo) (post-print thesis update)
5. [EARN-05](#earn-05-guide-decomposition-and-path-to-number-test) (guide decomposition if revised)
6. [EARN-06](#earn-06-biotech-quarterly-cash-and-catalyst-refresh) or [EARN-07](#earn-07-managed-care-mlr-bridge) (sub-sector quarterly refresh)
7. [COMM-03](#comm-03-quick-reaction-internal-note) (quick-reaction internal note)

### Biotech Catalyst Workflow

1. [SCR-02](#scr-02-catalyst-calendar-screen) (catalyst calendar)
2. [SUB-BIO-01](#sub-bio-01-phase-3-readout-pre-mortem) (Phase 3 pre-mortem)
3. [SUB-BIO-02](#sub-bio-02-fda-adcom-prep) (AdCom prep if applicable)
4. [SUB-BIO-03](#sub-bio-03-conference-abstract-triage) (conference triage if relevant)
5. [MOD-03](#mod-03-risk-adjusted-npv-rnpv-model-for-a-biotech-asset) (rNPV update)
6. [PORT-02](#port-02-catalyst-concentration-and-path-dependence-map) (catalyst concentration check)
7. [COMM-04](#comm-04-translate-technical-biology-for-generalist-pms) (translate for generalist PMs)

### Management Meeting Workflow

1. [MGMT-02](#mgmt-02-what-has-already-been-asked?-filter) (filter what’s already public)
2. [MGMT-01](#mgmt-01-1-on-1-question-stack) (build 1-on-1 question stack)
3. [EN-01](#en-01-expert-call-prep-brief) (parallel expert call to triangulate)
4. [MGMT-04](#mgmt-04-kol-day-capital-markets-day-pre-read) (KOL/CMD pre-read if applicable)
5. [EN-02](#en-02-post-call-debrief-and-triangulation) (post-meeting debrief)
6. [EARN-04](#earn-04-post-print-thesis-update-memo) (thesis update if material)

### Thematic Idea Generation Chain

1. [THM-01](#thm-01-theme-validation-framework) (theme validation)
2. [THM-02](#thm-02-tam-bottoms-up-build) (TAM bottoms-up)
3. [SCR-04](#scr-04-thematic-beneficiary-screen) (thematic beneficiary screen)
4. [THM-03](#thm-03-thematic-basket-construction) (basket construction)
5. [PORT-01](#port-01-healthcare-sleeve-positioning-review) (sleeve fit check)
6. [COMM-02](#comm-02-quarterly-letter-section-draft) (quarterly letter section)

### Sell Discipline Quarterly Chain

1. [SELL-01](#sell-01-sell-discipline-scorecard) (scorecard)
2. [SELL-02](#sell-02-thesis-breaking-signal-watchlist) (thesis-breaking watchlist refresh)
3. [THES-01](#thes-01-pre-mortem-on-a-long-thesis) (pre-mortem)
4. [THES-02](#thes-02-steel-man-the-short-case) (steel-man short)
5. [PORT-01](#port-01-healthcare-sleeve-positioning-review) (sleeve review)
6. [PORT-02](#port-02-catalyst-concentration-and-path-dependence-map) (catalyst concentration)

### Data System Setup Chain

1. [TECH-01](#tech-01-bloomberg-bql-syntax-generator-for-healthcare) (BQL syntax for core data pulls)
2. [TECH-03](#tech-03-factset-universal-screening-for-healthcare) (FactSet screening setup)
3. [TECH-05](#tech-05-sec-edgar-autonomous-agent-configuration) (SEC EDGAR monitoring agent)
4. [TECH-06](#tech-06-clinicaltrials.gov-agent-query-construction) (ClinicalTrials.gov agent)
5. [TECH-02](#tech-02-bloomberg-catalyst-and-event-calendar-query) (catalyst calendar query)
6. [TECH-04](#tech-04-factset-document-search-for-transcript-mining) (transcript mining setup)

### Compliance Pre-Publication Chain

1. [COMM-05](#comm-05-mnpi-scrubbing-audit-for-client-communications) (MNPI scrub)
2. [COMM-06](#comm-06-disclosure-and-conflict-of-interest-check) (disclosure and conflict check)
3. [COMM-07](#comm-07-public-speaking-and-conference-pre-flight) (public speaking pre-flight if applicable)

### Late-Stage Biotech Diligence Chain

1. [INIT-06](#init-06-biotech-specific-initiation-layer) (biotech initiation layer)
2. [SUB-BIO-04](#sub-bio-04-target-product-profile-tpp-interrogation) (TPP interrogation)
3. [SUB-BIO-05](#sub-bio-05-cmc-and-cogs-scalability-check) (CMC/COGS scalability)
4. [SUB-BIO-06](#sub-bio-06-freedom-to-operate-fto-ip-analysis) (FTO IP analysis)
5. [SUB-BIO-07](#sub-bio-07-fda-meeting-history-risk-extraction) (FDA meeting history)
6. [SUB-BIO-01](#sub-bio-01-phase-3-readout-pre-mortem) (Phase 3 pre-mortem)
7. [MOD-03](#mod-03-risk-adjusted-npv-rnpv-model-for-a-biotech-asset) (rNPV model)
8. [EN-01](#en-01-expert-call-prep-brief) (KOL expert call)
9. [COMM-04](#comm-04-translate-technical-biology-for-generalist-pms) (translate for generalist PMs)

### Global Name International Exposure Chain

1. [INIT-01](#init-01-30-minute-name-scoping-memo) (scope in 30 minutes)
2. [INIT-02](#init-02-full-initiation-memo-skeleton) (full memo skeleton)
3. [INTL-01](#intl-01-european-hta-pathway-mapping) (European HTA pathway mapping)
4. [INTL-02](#intl-02-japanese-reimbursement-cycle-and-price-revision-analysis) (Japanese reimbursement cycle)
5. [INTL-03](#intl-03-chinese-biotech-licensing-economics-and-biosecure-pass-through) (China exposure if relevant)
6. [INTL-04](#intl-04-uk-specific-healthcare-dynamics-for-a-london-based-global-mandate) (UK-specific dynamics for LDN mandate)
7. [MOD-10](#mod-10-scenario-construction-as-a-discipline) (scenario construction with regional outcomes)
8. [COMM-01](#comm-01-ic-memo-draft) (IC memo integrating regional view)

### Annual Review and Learning Chain

1. [SELL-01](#sell-01-sell-discipline-scorecard) (quarterly scorecards for the full book)
2. [SELL-04](#sell-04-single-name-thesis-post-mortem) (single-name post-mortems for material exits)
3. [SELL-05](#sell-05-book-wide-annual-post-mortem-and-process-audit) (book-wide annual post-mortem)
4. [THES-01](#thes-01-pre-mortem-on-a-long-thesis) (pre-mortem on carried-forward positions)
5. [PORT-01](#port-01-healthcare-sleeve-positioning-review) (sleeve positioning review for next year)
6. [COMM-02](#comm-02-quarterly-letter-section-draft) (annual letter section)

---

## Appendix C — Source-Data Fidelity Caveats

Primary sources are authoritative but not infallible. The caveats below document operationally relevant limitations of the data sources this library relies on. Every prompt that touches these sources should carry the appropriate caveat in its output, and every analyst using the library should internalise them.

### FDA drug labelling

FDALabel is useful for full-text label search but its SPL-based records can differ from the most recent FDA-approved labelling. For any analysis where exact label language matters (post-approval label delta work, indication scope, black-box warning phrasing, contraindication wording), prefer Drugs@FDA official approval documents and the approval letter itself. Treat FDALabel as a search index, not as the authoritative text.

### SEC Form 13F institutional ownership

13F filings are lagged by 45 days after quarter-end and reflect holdings only, not short positions. The SEC itself warns that structured 13F datasets are derived from filer submissions and may contain extraction errors or misclassifications. Cross-reference against Bloomberg HDS and FactSet ownership for current-period context, and treat any 13F-derived conclusion about current positioning as directional rather than precise.

### Medical conference abstracts and data releases

Conference materials are embargoed on defined schedules. AACR states abstracts remain confidential until publication in its proceedings workflow. ASCO releases abstract titles ahead of the meeting but full data is held until the poster or oral presentation. ESMO follows similar staged disclosure. Every conference-related output should time-stamp exactly what is public at the moment of analysis and distinguish title-level information from full-data disclosures.

### CMS reimbursement and quality files

CMS files are periodically updated. MA rate notices (Advance Notice in February, Final Rate Notice in April), Star Ratings (released October), the Physician Fee Schedule (annual final rule November), OPPS (annual final rule November), the Clinical Laboratory Fee Schedule, and telehealth service lists all have publication cycles. Every CMS-derived output should carry the retrieval date and identify the vintage of the underlying file.

### ClinicalTrials.gov registry and results

ClinicalTrials.gov captures protocol registration and summary results fields, but sponsor updates can lag. Primary completion date slippage is common and often informative. Outcome measure definitions and statistical analysis plans occasionally change mid-trial without the registry fully reflecting the amendment. For late-stage trials, cross-reference against the sponsor's SEC filings and the published protocol where available.

### Bloomberg SPLC and supply chain data

SPLC supplier and customer relationships are derived from public disclosures and may lag or omit undisclosed relationships, particularly in private-company supply chains and where customer concentration falls below the 10 per cent disclosure threshold. Treat SPLC as a directional map rather than a complete picture.

### Consensus estimates

Bloomberg and FactSet consensus can diverge meaningfully, particularly for smaller-cap or biotech names with thin analyst coverage. When building a 'vs consensus' view, specify which consensus source is being used and note where the other source differs. For names with fewer than five contributing analysts, treat consensus as a central tendency rather than a binding reference.

### Sell-side research

Sell-side notes are a triangulation input, not a primary source. Analyst models reflect their firms' incentive structures (banking relationships, trading priorities, commission models). Ratings distributions are structurally biased toward buy. Any prompt that references sell-side material should mark it as triangulation and independently verify against filings and primary regulatory records.

---

## Appendix D — Prompt Engineering Guidance

The prompts in this library are designed to work across frontier LLMs, but output quality can be materially improved by tuning a small number of model settings and by following vendor-recommended prompting practice. The guidance below is synthesised from OpenAI and Anthropic prompting documentation and the practical experience of running this library across Claude, GPT-4/5, and Gemini.

### Temperature

For analytical work — earnings analysis, valuation, thesis memos, post-mortems, compliance reviews — use temperature 0 to 0.2. This produces consistent, repeatable output and minimises the risk that the model hallucinates quantitative anchors or substitutes plausible-sounding but unsourced language for real analysis. For ideation work — variant perception generation, thematic brainstorming, scenario construction — a modestly higher temperature of 0.3 to 0.5 can surface non-obvious framings. Temperatures above 0.7 should be avoided for this library; the prompts are structured and benefit from determinism rather than creativity.

### Reasoning style

Ask for an auditable scaffold rather than a sprawling narrative. The default output skeleton in the standing instructions (What matters now, Facts, Inference, Model impact, Variant view, Disconfirming evidence, Next diligence, Confidence) is designed to expose where judgment enters the process without bloating the output. When invoking a prompt, resist the urge to add 'and explain your reasoning in detail.' The numbered steps inside each prompt already specify the analytical movement; asking for additional reasoning narrative tends to produce verbose rather than clearer output.

### Tool routing

When working with a model that has tool use (web search, code execution, document retrieval), specify which tools to call and in what order as part of the prompt invocation. For example: 'Use web search to pull the latest 10-Q, then execute the prompt EARN-04 against it.' Models left to decide tool order tend to over-search or under-search. The standing instructions' source hierarchy can be restated as a tool-calling sequence when tool use is available.

### Context management

For persistent sessions (Claude Projects, Custom GPTs, Gems), load the standing instructions once and upload the library as a knowledge file. For one-off conversations, use the compact standing instructions variant to reduce token overhead. When analysing multiple source documents (earnings release plus transcript plus 10-Q), paste or attach them before invoking the prompt; models that must integrate attachments into an already-active reasoning chain produce weaker outputs than models given the full context upfront.

### Output structure

Where the prompt specifies an output format, accept that format; avoid asking the model to 'rewrite as a table' or 'make it shorter' in the same conversation because the re-render often loses quantitative precision. If a different format is needed, start a new conversation with the adjusted instruction.

### Model selection

The library has been tested on Claude Opus, GPT-4o, GPT-5, and Gemini 1.5 Pro. Claude's long context window and Artifacts feature suit the longest analytical workflows (full initiation memos, annual post-mortems). GPT-5 handles complex multi-document synthesis particularly well. Gemini's 2M token context is distinctive for workflows that need to consume an entire coverage universe of filings or transcripts at once. For simple screening or mechanical tasks, smaller or faster models are adequate. For institutional output quality, use frontier models.

### Confidence score discipline

The required confidence score at the end of every output is the single most important calibration tool in this library. A score of 0.85 or above indicates high-quality primary-source evidence and limited inferential distance. A score of 0.60 to 0.84 indicates solid analysis with acknowledged uncertainty. A score below 0.60 signals the output should be treated as a structured hypothesis rather than a conclusion. Analysts using the library regularly develop an intuition for when a model is over-confident and should calibrate accordingly.

---

*Healthcare Equity Analyst Prompt Library v1.4 — 113 prompts across 16 categories*