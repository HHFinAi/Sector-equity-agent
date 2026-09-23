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

