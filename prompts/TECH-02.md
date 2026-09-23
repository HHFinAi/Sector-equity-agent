### TECH-02  Bloomberg Catalyst and Event Calendar Query

```yaml
id: TECH-02
title: Bloomberg Catalyst and Event Calendar Query
tags: [#data-extraction, #biotech, #bloomberg, #bql, #senior-judgment]
use_when: "When building or refreshing a catalyst calendar from Bloomberg data."
reasoning: "schema design → pipeline build → validate → deploy"
inputs: "Coverage universe tickers; date window."
output: "BQL query or terminal navigation with structured output."
```

**Reasoning scaffold:** schema design → pipeline build → validate → deploy

**Prompt:**
```
Generate a BQL query to extract the upcoming catalyst calendar for my healthcare coverage universe, specifically filtering for: (1) FDA Advisory Committee (AdCom) meetings in the next 90 days; (2) PDUFA dates in the next 180 days; (3) Phase 3 trial readout windows from Bloomberg BI DRUG <GO> or equivalent; (4) CMS rate notice and final rule dates. Output as a structured table with ticker, event type, expected date, and Bloomberg event ID. If a BQL approach is limited, provide the alternative Bloomberg terminal navigation (BI, EVTS, DRUG <GO>) with the specific screen settings.
```

---

