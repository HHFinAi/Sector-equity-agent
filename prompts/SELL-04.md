### SELL-04  Single-Name Thesis Post-Mortem

```yaml
id: SELL-04
title: Single-Name Thesis Post-Mortem
tags: [#sell-discipline, #post-mortem, #cross-sector, #senior-judgment, #pm-level]
use_when: "After exiting a position at a loss, holding a winner past the thesis horizon, or any outcome where the outcome materially differed from the original thesis. Run within two weeks of exit while details are still fresh."
reasoning: "reconstruct thesis → classify error → extract lesson → update framework"
inputs: "Original initiation or entry memo; complete holding-period timeline including earnings prints and catalysts; exit rationale if documented; original KPI tracker; sell discipline scorecard updates during the holding period."
output: "Structured post-mortem with error classification, transferable lesson, and sell discipline framework update."
```

**Reasoning scaffold:** reconstruct thesis → classify error → extract lesson → update framework

**Prompt:**
```
Conduct a thesis post-mortem on [TICKER], exited on [date] at [price] after [entry price, holding period]. The goal is not to assign blame but to extract transferable lessons. (1) Original thesis reconstruction — pull the initiation memo or entry rationale verbatim. Do not rewrite with hindsight. State the thesis pillars, the variant perception, the catalysts relied upon, the risks I acknowledged, and the position size and rationale. (2) What actually happened — a factual timeline of operational events (earnings prints, catalysts, management changes, competitive developments) and share-price reaction during the holding period. Separate price action from fundamentals. (3) Pillar-by-pillar verdict — for each original thesis pillar, mark as confirmed, intact but irrelevant (true but did not drive the stock), weakened, broken, or untested. The ‘intact but irrelevant’ category is the most important diagnostic — it identifies the thesis claim that was correct in substance but wrong in thesis relevance. (4) Error classification — place the outcome into one of five categories: (a) thesis was wrong in substance (my analysis of the business was incorrect); (b) thesis was correct but the market cared about different things (variant perception was right but immaterial); (c) thesis was correct but timing was wrong (horizon mismatch); (d) sizing was wrong for the conviction level (risk-reward was mispriced relative to my own expressed view); (e) process error (I did not follow my own sell discipline signals). Each category implies a different lesson. (5) Signal forensics — identify the one operational or market signal that, if I had noticed it in real time, would have forced a different decision. Where was it disclosed? Was it in my KPI tracker? Did I see it and dismiss it? (6) Transferable lesson — state in one sentence the rule I will apply to similar situations in the future. The rule must be operational (‘when MLR exceeds X, I will re-underwrite’) rather than aspirational (‘I will be more disciplined’). (7) Update the sell discipline scorecard template — if the lesson implies a new signal to monitor or a new threshold to respect, encode it into SELL-02 for the rest of the book. End with confidence score and an honest note on whether the lesson generalises or is specific to this situation.
```

---

