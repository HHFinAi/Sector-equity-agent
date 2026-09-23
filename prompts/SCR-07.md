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

