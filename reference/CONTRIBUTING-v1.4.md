# Contributing to the Healthcare Equity Analyst Prompt Library

Contributions are welcome. This library is designed to evolve as buy-side healthcare workflows evolve, and proposed additions from practising analysts are particularly valuable.

## What kinds of contributions are welcome

New prompts that fill genuine workflow gaps are the highest-value contribution. A prompt fills a gap when there is a recurring analytical task in institutional buy-side healthcare research that the existing 113 prompts do not already address. Refinements to existing prompts — sharper quantitative anchors, updated source references, better-calibrated reasoning scaffolds — are also welcome. Corrections to factual errors, outdated regulatory references, or stale quantitative anchors are always welcome and should be raised via GitHub issues.

Contributions that are not a fit include generic prompt-engineering experiments that do not address healthcare workflow specifics, prompts that encourage behaviours contrary to the standing instructions (ignoring source hierarchy, suppressing disconfirming evidence, omitting confidence scores), and sell-side or investment banking content, which is outside the library's buy-side mandate.

## Prompt schema

Every prompt in the library follows a consistent schema. New prompts should follow the same schema to maintain library consistency and to support programmatic ingestion via the YAML metadata headers.

```yaml
id: CAT-XX               # Category prefix + two-digit number (e.g. EARN-08, SUB-BIO-09)
title: "Descriptive title matching library conventions"
tags:                    # Four-dimensional taxonomy
  - "#workflow-tag"      # One of: initiation, earnings, modeling, thesis, sell-discipline, etc.
  - "#subsector-tag"     # One of: biotech, pharma, medtech, services-payors, tools-dx, digital-health, cross-sector, international
  - "#data-source-tag"   # One or more: bloomberg, factset, sec, clinicaltrials-gov, fda-ema, cms, expert-network, sell-side
  - "#complexity-tag"    # One of: junior-task, senior-judgment, pm-level
use_when: "One-sentence cue describing exactly when the analyst should invoke this prompt."
reasoning: "parse \u2192 diagnose \u2192 synthesise \u2192 recommend"   # One-line analytical movement
inputs: "List of inputs the analyst should provide: filings, transcripts, consensus, etc."
output: "What the prompt produces: a memo, a scorecard, a question stack, etc."
```

The prompt body itself should follow the prescriptive multi-step pattern established in the existing library. A strong prompt typically contains seven to twelve numbered analytical steps, each of which directs the model to a specific component of the analysis. Embed quantitative anchors where they provide calibration (for example, base rates for Phase 3 trial success, typical gross margin ranges for mature razor-blade medtech, expected Phase 2 to Phase 3 effect-size attenuation). Apply MNPI guardrails where relevant.

## Proposal process

To propose a new prompt, open a GitHub issue describing the workflow gap the prompt addresses, the proposed prompt ID and tags, and a draft of the prompt body. For small refinements to existing prompts, a pull request with the specific edit and a brief rationale is sufficient.

Contributions will be reviewed for consistency with the library's governance layer (standing instructions, required behaviours, confidence scoring), for factual accuracy of any regulatory or reimbursement references, and for whether the prompt genuinely extends coverage rather than duplicating existing functionality.

## Authorship and attribution

Contributors retain authorship credit for their contributions. The library is released under the MIT License, which preserves attribution while allowing use, modification, and redistribution.

---

*Healthcare Equity Analyst Prompt Library — Maintained at [github.com/HHFinAi](https://github.com/HHFinAi).*
