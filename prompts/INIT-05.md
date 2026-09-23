### INIT-05  Bull / Base / Bear Decomposition with Probability Weights

```yaml
id: INIT-05
title: Bull / Base / Bear Decomposition with Probability Weights
tags: [#initiation, #modeling, #thesis, #cross-sector, #senior-judgment]
use_when: "When constructing the formal scenario set for a price target, avoiding mechanical interpolation."
reasoning: "frame scenarios → quantify paths → weight probabilities → decide"
inputs: "Current operating model, base assumptions, consensus PT range."
output: "Structured scenario matrix with probability-weighted PT and sensitivity note."
```

**Reasoning scaffold:** frame scenarios → quantify paths → weight probabilities → decide

**Prompt:**
```
For [TICKER], construct three scenarios — bull, base, bear — that are qualitatively distinct rather than linear interpolations. Each must be driven by a different dominant causal mechanism. For each: (1) dominant mechanism in one sentence; (2) three to five operational assumptions; (3) 5-year P&L sketch; (4) appropriate valuation method and equity value per share; (5) subjective probability with reasoning, ensuring the residual ‘unknown unknown’ bucket is not zero; (6) leading indicator that would shift probability weighting. End with a probability-weighted PT and a flag if the modal scenario differs materially from the weighted average.
```

---

