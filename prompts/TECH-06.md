### TECH-06  ClinicalTrials.gov Agent Query Construction

```yaml
id: TECH-06
title: ClinicalTrials.gov Agent Query Construction
tags: [#data-extraction, #biotech, #ctgov, #senior-judgment]
use_when: "When extracting structured clinical trial data programmatically."
reasoning: "FQL construct → test → deploy ownership or estimate workflow"
inputs: "Condition, intervention, sponsor, or NCT numbers."
output: "API query URL and JSON output schema."
```

**Reasoning scaffold:** FQL construct → test → deploy ownership or estimate workflow

**Prompt:**
```
Build a resilient query for ClinicalTrials.gov that bypasses fragile DOM selectors. (1) Construct the API query URL (using the v2 API: https://clinicaltrials.gov/api/v2/studies) to extract: NCTId, BriefTitle, Condition, InterventionName, Phase, OverallStatus, StartDate, PrimaryCompletionDate, StudySponsor. (2) Filter for multiple statuses simultaneously (e.g. ‘RECRUITING’ and ‘ACTIVE_NOT_RECRUITING’). (3) Filter by condition, intervention type, or sponsor. (4) Construct a comparative query for [TICKER]’s lead asset vs all competing trials in the same indication/mechanism. (5) Output as structured JSON for downstream analysis. (6) If using an AI agent framework (e.g. AgentQL), provide the natural-language extraction query. My query: [describe the trial data needed].
```

---

