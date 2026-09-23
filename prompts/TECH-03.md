### TECH-03  FactSet Universal Screening for Healthcare

```yaml
id: TECH-03
title: FactSet Universal Screening for Healthcare
tags: [#data-extraction, #cross-sector, #factset, #fql, #senior-judgment]
use_when: "When building a quant screen in FactSet with healthcare-specific criteria."
reasoning: "data source audit → API construct → integrate → maintain"
inputs: "Screen criteria; output format preference."
output: "FactSet screening formula and API payload."
```

**Reasoning scaffold:** data source audit → API construct → integrate → maintain

**Prompt:**
```
Build a FactSet Universal Screening formula for [screen description]. (1) Assign correct data library prefixes — FF_ for FactSet Fundamentals, FG_ for Global Constituents. (2) Apply relative date parameters: (0) for most recent, (-1) for prior year. (3) Map to the correct API endpoint if programmatic extraction is needed — /metrics for income statement items, OFDB for non-portfolio databases. (4) For healthcare-specific criteria, include: therapeutic area classification, pipeline stage filters, patent expiry windows, and clinical trial event flags. (5) Output the screen as both a FactSet workstation formula and a JSON payload for the FactSet Fundamentals API. My screen: [describe criteria].
```

---

