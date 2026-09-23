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

