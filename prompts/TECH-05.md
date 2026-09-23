### TECH-05  SEC EDGAR Autonomous Agent Configuration

```yaml
id: TECH-05
title: SEC EDGAR Autonomous Agent Configuration
tags: [#data-extraction, #cross-sector, #sec-filings, #senior-judgment]
use_when: "When setting up automated monitoring of SEC filings for thesis-relevant events."
reasoning: "BQL construct → test output → deploy screen"
inputs: "Coverage universe CIK numbers; filing types; keyword list."
output: "Agent configuration with API endpoints and JSON schema."
```

**Reasoning scaffold:** BQL construct → test output → deploy screen

**Prompt:**
```
Configure an autonomous agent to monitor SEC EDGAR filings across my coverage universe. (1) Form 4 insider trading — flag any open-market purchase >$100K by C-suite or board members, cross-referenced against upcoming catalyst calendar. (2) 8-K current reports — parse for keywords: ‘Complete Response Letter’, ‘CRL’, ‘accelerated approval’, ‘voluntary recall’, ‘consent decree’, ‘executive departure’, and any material definitive agreement. (3) 13F institutional holdings — quarterly delta for the top 20 healthcare-focused funds. (4) Output as structured JSON mapped to predefined schemas: {ticker, form_type, filing_date, key_event, relevance_score}. (5) Provide the EDGAR XBRL API endpoint structure and the query parameters for each filing type.
```

---

