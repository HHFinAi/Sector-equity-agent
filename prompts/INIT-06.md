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

