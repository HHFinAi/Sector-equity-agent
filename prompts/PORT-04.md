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

