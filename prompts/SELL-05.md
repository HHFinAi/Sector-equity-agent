### SELL-05  Book-Wide Annual Post-Mortem and Process Audit

```yaml
id: SELL-05
title: Book-Wide Annual Post-Mortem and Process Audit
tags: [#sell-discipline, #post-mortem, #portfolio, #pm-level]
use_when: "Annually, ideally in January after the calendar year closes, to audit the year's decisions across the entire book rather than name-by-name."
reasoning: "aggregate post-mortems → cluster patterns → calibrate base rates → commit framework updates"
inputs: "Full year's worth of initiation memos, post-print notes, sell discipline scorecards, single-name post-mortems, and portfolio performance attribution."
output: "Year-end audit report with error pattern analysis, base rate updates, process discipline scorecard, and committed framework updates for the year ahead."
```

**Reasoning scaffold:** aggregate post-mortems → cluster patterns → calibrate base rates → commit framework updates

**Prompt:**
```
Conduct an annual post-mortem on my healthcare sleeve for [year]. The scope is the full book of positions, not any single name. (1) Performance attribution by decision type — decompose total return into: conviction positions held through volatility (top 5 names), opportunistic trades (positions held less than 90 days), hedges, shorts, and cash drag. Identify which decision categories added or subtracted value. (2) Error pattern recognition — review the single-name post-mortems from SELL-04 conducted during the year and cluster them. Are the errors concentrated in a particular decision category (e.g. I am consistently late to exit clinical-stage biotech after failed readouts), a particular sub-sector (e.g. my tools and diagnostics work is weaker than my biotech work), a particular market regime (e.g. I underperformed during risk-off periods), or a particular process failure (e.g. I override my own sell discipline scorecard too often)? (3) Base rate calibration — did the base rates I assumed (Phase III success at approximately 50 per cent, biosimilar uptake curves, MA bid cycle outcomes) hold in the actual year? Where they did not, update the base rates I apply going forward. (4) Process discipline scorecard — how often did I complete the full earnings workflow (EARN-01 through EARN-04) on my positions versus skipping steps? How often did I run the full sell discipline scorecard at quarter-end versus deferring? Process discipline is an input to performance; measure it directly. (5) Sizing audit — were my largest positions my highest-conviction positions in retrospect, or did sizing drift toward positions I had grown comfortable with rather than positions where the risk-reward was best? (6) External-to-me lessons — what happened in the year that I did not anticipate and could not reasonably have anticipated, versus what I should have anticipated but did not? The honest distinction between these two matters for confidence calibration. (7) Framework updates — for v[N+1] of my own process, what specifically changes in my watchlist thresholds, my sizing rules, my base rates, or my KPI tracker? Commit to the changes in writing. End with confidence score.
```

---

