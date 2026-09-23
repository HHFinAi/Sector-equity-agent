### MOD-10  Scenario Construction as a Discipline

```yaml
id: MOD-10
title: Scenario Construction as a Discipline
tags: [#modeling, #thesis, #cross-sector, #senior-judgment, #pm-level]
use_when: "When the analyst needs to build scenarios for a decision (valuation, hedge construction, position sizing) and wants to avoid the default failure modes of linear interpolation and missed-scenario bias."
reasoning: "frame decision → generate mechanisms → audit missing scenarios → probability-weight → decide"
inputs: "Decision to be made; current consensus and market-implied positioning; relevant operational, competitive, regulatory and macro context."
output: "Scenario set with distinct mechanisms, calibrated probabilities, early signals, and a decision rule."
```

**Reasoning scaffold:** frame decision → generate mechanisms → audit missing scenarios → probability-weight → decide

**Prompt:**
```
Teach me to construct scenarios for [TICKER / decision] as a discipline, not just an output. (1) Decision frame — state the decision the scenarios must serve (set a price target; size a position; construct a hedge; assess portfolio fit). The number of scenarios should match the decision: two for binary (hedge or no hedge), three or four for sizing, more only if decision resolution requires it. (2) Mechanism-distinct generation — for each scenario, state the single dominant causal mechanism in one sentence. Two scenarios with the same mechanism operating at different magnitudes are not two scenarios; they are one scenario with a sensitivity band. (3) Missing-scenario audit — before accepting the scenario set, explicitly ask: what scenario would a smart short describe that I have not included? What scenario would a long-duration holder describe? What scenario does the options market appear to be pricing that I have not articulated? Any scenario identified here and absent from my set is evidence of a blind spot. (4) Probability discipline — assign probabilities that sum to 1.00 with a residual ‘unknown unknown’ bucket of at least 5 per cent. If the residual is zero, the scenario set is overconfident. Use round numbers (e.g. 40 / 30 / 20 / 10) rather than false-precision decimals. (5) Early-signal identification — for each scenario, the single operational or market signal that, if observed, would cause me to shift probability mass toward it. This is what makes scenarios actionable rather than academic. (6) Decision rule — state in advance how the probability-weighted output maps to the decision, so the decision is made by the analysis rather than re-made after the fact. (7) Premortem — if the scenario I am weighting least turns out to be correct, what failure in my generator allowed me to underweight it? End with the scenario set, probabilities, early signals, decision, and confidence score.
```

---

