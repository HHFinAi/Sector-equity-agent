### TECH-04  FactSet Document Search for Transcript Mining

```yaml
id: TECH-04
title: FactSet Document Search for Transcript Mining
tags: [#data-extraction, #cross-sector, #factset, #fql, #senior-judgment]
use_when: "When mining earnings transcripts for specific themes across the coverage universe."
reasoning: "registry query → filter results → analyse → monitor"
inputs: "Topic; universe; quarter."
output: "Transcript mining results with source links and cross-read."
```

**Reasoning scaffold:** registry query → filter results → analyse → monitor

**Prompt:**
```
Command the FactSet Document Search (GenAI-powered) to extract specific commentary from healthcare earnings transcripts. (1) Construct the query to search for [topic — e.g. ‘GLP-1 cost impact’, ‘supply chain bottlenecks’, ‘pricing pressure’, ‘biosimilar competition’] across the most recent quarter’s transcripts for [universe]. (2) Filter by section (prepared remarks vs Q&A) if the topic is more likely to surface in one or the other. (3) Request source-linked results so each excerpt maps back to a specific transcript, speaker, and timestamp. (4) Summarise the results as: company, relevant quote, sentiment (positive/negative/neutral), and cross-read implication for my coverage.
```

---

