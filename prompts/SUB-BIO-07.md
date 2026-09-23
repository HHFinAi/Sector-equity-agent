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

