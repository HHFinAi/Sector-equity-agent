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

