### SCR-06  13F Institutional Ownership Delta Scanner

```yaml
id: SCR-06
title: 13F Institutional Ownership Delta Scanner
tags: [#screen, #cross-sector, #sec-filings, #senior-judgment]
use_when: "Quarterly after 13F filings."
reasoning: "activist signal scan → target fit → outcome scenarios → position"
inputs: "13F data; my portfolio."
output: "Ownership delta table with conviction, contrarian, and crowding flags."
```

**Reasoning scaffold:** activist signal scan → target fit → outcome scenarios → position

**Prompt:**
```
Extract 13F data for top 20 healthcare funds. (1) Net buying/selling by name; (2) conviction signals (3+ funds initiating); (3) contrarian signals; (4) crowding risk (>40% of float); (5) my portfolio ownership delta.
```

---

