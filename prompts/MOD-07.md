### MOD-07  MA Star Ratings and Bid Cycle Model

```yaml
id: MOD-07
title: MA Star Ratings and Bid Cycle Model
tags: [#modeling, #services-payors, #cms, #senior-judgment]
use_when: "For Medicare Advantage operators."
reasoning: "MA bid mechanics → scenario rates → Stars impact → multiple translation"
inputs: "CMS Stars, rate notice, segment detail, bid commentary."
output: "Plan-year-forward model with sensitivities."
```

**Reasoning scaffold:** MA bid mechanics → scenario rates → Stars impact → multiple translation

**Prompt:**
```
MA Star/bid cycle model for [TICKER]. (1) Membership by contract with Stars; (2) quality bonus exposure; (3) bid cycle dynamics (V28, IRA Part D, benchmark); (4) member growth scenarios; (5) revenue and MLR for next two plan years; (6) Stars and utilisation stress tests; (7) peer comparison.
```

---

