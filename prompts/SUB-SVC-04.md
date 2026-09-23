### SUB-SVC-04  Value-Based Care Capitation Tracking

```yaml
id: SUB-SVC-04
title: Value-Based Care Capitation Tracking
tags: [#services-payors, #modeling, #senior-judgment]
use_when: "When evaluating provider groups transitioning to risk-bearing contracts."
reasoning: "hospital operator → payer mix → margin → monitor"
inputs: "Segment disclosures, VBC contract details, quality metrics."
output: "Capitation tracking with margin trajectory."
```

**Reasoning scaffold:** hospital operator → payer mix → margin → monitor

**Prompt:**
```
Risk-bearing exposure for [TICKER]. (1) Revenue mix: capitated/full-risk/shared-savings vs fee-for-service over 8 quarters; (2) risk corridor and stop-loss; (3) medical cost ratio on risk contracts; (4) patient attribution stability; (5) quality incentive attainment; (6) VBC revenue growth vs FFS trajectory; (7) margin implication at current transition pace.
```

---

