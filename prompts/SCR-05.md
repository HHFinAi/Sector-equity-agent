### SCR-05  Activist Investor Target Screen

```yaml
id: SCR-05
title: Activist Investor Target Screen
tags: [#screen, #cross-sector, #sec-filings, #senior-judgment]
use_when: "When screening for potential activist targets in healthcare."
reasoning: "short-interest filter → borrow-cost check → asymmetry audit → prioritise"
inputs: "Screening data; 13D filings; proxy statements."
output: "Ranked list with playbook and uplift per name."
```

**Reasoning scaffold:** short-interest filter → borrow-cost check → asymmetry audit → prioritise

**Prompt:**
```
Screen for activist targets. Criteria: (1) market cap >$1B; (2) operating margin declining 3 years; (3) cash/investments >30% of EV; (4) R&D productivity below peer median; (5) exec comp disconnected from TSR; (6) board tenure >10 years or <3 independent with sector expertise; (7) recent 13D filings. Per hit: likely playbook and uplift estimate.
```

---

