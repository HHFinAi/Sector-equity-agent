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

