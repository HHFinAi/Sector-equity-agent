### MGMT-02  What Has Already Been Asked? Filter

```yaml
id: MGMT-02
title: What Has Already Been Asked? Filter
tags: [#mgmt-meeting, #cross-sector, #transcripts, #junior-task]
use_when: "To avoid burning meeting time on already-answered questions."
reasoning: "compare transcripts → detect language drift → surface to model → flag signal"
inputs: "Draft questions; transcripts."
output: "Question-by-question audit table."
```

**Reasoning scaffold:** compare transcripts → detect language drift → surface to model → flag signal

**Prompt:**
```
For each of my draft questions, search last four earnings calls and three conference appearances: (1) has it been asked; (2) management answer; (3) specific or hand-wave; (4) re-frame or drop.
```

---

