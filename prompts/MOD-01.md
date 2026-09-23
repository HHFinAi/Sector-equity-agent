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

