### EARN-07  Managed Care MLR Bridge

```yaml
id: EARN-07
title: Managed Care MLR Bridge
tags: [#earnings-post, #services-payors, #sec-filings, #cms, #senior-judgment]
use_when: "Each quarter for payors where MLR is the central driver."
reasoning: "parse transcript → detect language shifts → quantify tone → signal-flag"
inputs: "Release, supplement, transcript, prior-year prints."
output: "MLR bridge, drivers, forward-look, peer cross-read."
```

**Reasoning scaffold:** parse transcript → detect language shifts → quantify tone → signal-flag

**Prompt:**
```
MLR bridge for [TICKER] for [Q]. (1) MLR by segment vs prior year/consensus; (2) drivers — utilisation, unit cost, mix, prior period, one-offs; (3) risk adjustment dynamics (RADV, V28, Stars); (4) forward colour; (5) full-year guide implication; (6) peer cross-read.
```

---

