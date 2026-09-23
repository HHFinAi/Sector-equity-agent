### TECH-01  Bloomberg BQL Syntax Generator for Healthcare

```yaml
id: TECH-01
title: Bloomberg BQL Syntax Generator for Healthcare
tags: [#data-extraction, #cross-sector, #bloomberg, #bql, #junior-task]
use_when: "When you need executable Bloomberg BQL syntax for healthcare-specific data queries."
reasoning: "query construct → validate output → deploy"
inputs: "Natural-language data query; target securities; output format (Excel or Python)."
output: "Executable BQL string ready to paste into Excel or Python."
```

**Reasoning scaffold:** query construct → validate output → deploy

**Prompt:**
```
Translate my natural-language query into executable BQL syntax for Excel or Python. (1) Construct the =BQL() formula using get(<field>) for(<security>) with(<parameters>). (2) Define parameters (dates, periods, fill rules). (3) For fiscal-period data, format calculated periods correctly (e.g. FA_PERIOD_REFERENCE, FA_PERIOD_TYPE=LTM). (4) For healthcare-specific fields, use the correct BQL field names for R&D expense, pipeline data, patent expiry via PTNT <GO>, catalyst calendar. (5) Output validation — verify parentheses and nesting. (6) If Python, provide the bql.Execute() syntax with proper DataFrame handling. My query: [describe the data needed].
```

---

