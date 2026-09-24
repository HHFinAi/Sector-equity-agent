# Healthcare Equity Analyst Prompt Library — Worked Examples

**Companion document to v1.4**

This document shows four prompts from the library executed against illustrative scenarios. Tickers are fictional but the underlying analytical patterns and data types are drawn from real-world buy-side healthcare workflows. The outputs below reflect institutional-quality buy-side analysis as practiced by senior analysts with 7+ years of healthcare equity research experience at dedicated investment platforms. These examples are published for educational purposes to show what the library produces. Nothing below constitutes investment advice or recommendation.

Each example includes the prompt that was invoked, the mock source snippets that the analyst supplied to the model (formatted as they would appear from Bloomberg, FactSet, SEC EDGAR, CMS, and other primary sources), the context the analyst provided, and the output the library produces when executed against those inputs with the standing instructions applied. Showing the source inputs alongside the output is intentional — it teaches users what inputs to gather and how to format them, which is often the weakest link in getting high-quality output from prompt libraries.

---

## Example 1 — Post-Print Thesis Update (EARN-04)

**Scenario.** A mid-cap diabetes-focused biotech, Solstice Biosciences (fictional ticker SOLX), has just reported Q3 2025 results. The analyst entered the position six months ago on a thesis that the company's GLP-1/GIP dual agonist would take share from incumbents in the post-Mounjaro landscape.

**Prompt invoked.** EARN-04: Post-Print Thesis Update Memo, with standing instructions applied.

**Reasoning scaffold.** Reconstruct pillars → apply outcome → classify delta → recommend action.

**Source snippets supplied to the model:**

```text
SEC 8-K / Earnings Release (4 November 2025)
Revenue: $142.0M (consensus $128M, beat 10.9%)
Gross margin: 71.2% (vs 74.1% Q2, 73.8% Y/Y)
Operating margin: 18.4% (vs 21.2% Q2)
New patient starts: 47,000 (vs 38,000 Q2)
Full-year guide unchanged at $540-560M
Cash: $890M, burn neutral
```

```text
Q3 earnings call transcript excerpts
CFO: "Channel mix shift accounted for approximately 180bps of margin compression"
CFO: "Manufacturing ramp costs contributed an additional 110bps"
CFO (in response to sell-side question on sustainability): "We expect these dynamics to persist into Q4 but normalise through 2026"
CEO: "We are not revising full-year guidance given the Q4 timing of several large PBM formulary resets"
```

```text
Bloomberg consensus (pre-print)
Revenue $128M (range $120-135M, 14 analysts)
Gross margin 73.5% (range 72.8-74.5%, 11 analysts)
EPS $(0.45) (range $(0.50)-$(0.40))
2026 revenue consensus $720M, 2026 gross margin 76.0%
```

```text
Original thesis memo (May 2025) — pillar summary
Pillar 1: GLP-1/GIP dual mechanism drives share from single-target incumbents
Pillar 2: Margin expansion from scale to 78% by 2027 (long-term target)
Pillar 3: Payor coverage builds meaningfully in 2026-2027 launches
```

**Output.**

### SOLX Q3 2025 Post-Print Thesis Update

**What matters now.** The top-line beat masks a gross margin reset and an unchanged guide that together imply H2 deceleration or conservatism; thesis pillar two (margin expansion from scale) is now in question.

**Facts.** Revenue of $142M (Q3 2025 earnings release, 4 November 2025) beat consensus of $128M by 10.9%, driven by new-patient starts of 47,000 vs 38,000 prior quarter. Gross margin of 71.2% vs 74.1% in Q2 and 73.8% year-ago. Operating margin of 18.4% vs 21.2% Q2. Full-year revenue guide unchanged at $540–560M implying Q4 of $130–150M, i.e. implied sequential deceleration given Q3 of $142M. Cash position $890M, quarterly burn neutral.

**Inference.** Three threads. First, the volume beat is real (patient starts up 24% sequential) and validates demand thesis pillar one. Second, the gross margin compression is the material negative — management attributed 180bps to "channel mix shift" and 110bps to "manufacturing ramp costs," but did not quantify the sustainability of either in a way that fully supports the 2026 normalisation narrative. If ramp costs persist into 2026, the path to the 78% long-term margin target is materially longer. Third, the unchanged guide despite the beat signals either conservatism (consistent with this management team's prior pattern of guiding to beat by 3–5%) or a Q4 headwind not yet disclosed. The PBM formulary reset reference argues for the latter.

**Model impact.** Revising 2026 gross margin assumption from 76% to 74%, flowing through to a $2.10 EPS cut (~8%). Revenue forecast unchanged; 2026 PT moves from $52 to $48. Thesis pillar two (margin expansion) is reclassified from confirmed to intact-but-at-risk.

**Variant view.** Consensus is likely to take this print bullishly on volume and ignore the margin signal, based on sell-side pre-release framing. My variant is that the margin compression is structurally relevant because channel mix in GLP-1 is unlikely to revert — payor rebate pressure is structural, not cyclical. I expect consensus 2026 numbers to rise on volume then have to come down in six months when margin is explicit.

**Disconfirming evidence.** If Q4 gross margin recovers to 73%+ and management quantifies the ramp costs as one-time in the Q4 call, the margin concern is resolved and the thesis returns to full strength. A second confirming signal would be any commentary on formulary wins at the major PBMs that validate the volume trajectory independently of channel mix.

**Next diligence.** Expert call with a regional payor contracting lead to pressure-test the channel mix explanation. Review competitor prints (Lilly and Novo Q3 transcripts) for any read on GLP-1 class gross-to-net trajectory. IQVIA TRx data weekly for four weeks to confirm volume trajectory sustains post-Q3.

**Action.** Hold at current weight. Not adding until margin trajectory clarifies in Q4. Would trim if next print shows further 100bps+ gross margin erosion without a one-time explanation.

**Confidence: 0.72.**

---

## Example 2 — Phase 3 Readout Pre-Mortem (SUB-BIO-01)

**Scenario.** Meridian Therapeutics (fictional ticker MRDN) has an upcoming Phase 3 readout for its anti-IL-23 asset in moderate-to-severe ulcerative colitis, with top-line data expected in late November 2025. The analyst has a medium-sized long position.

**Prompt invoked.** SUB-BIO-01: Phase 3 Readout Pre-Mortem, with standing instructions applied.

**Reasoning scaffold.** Trial design assess → effect-size distribution → outcome scenarios → sizing.

**Source snippets supplied to the model:**

```text
ClinicalTrials.gov NCT05XXXXXX — REGENCY-2 Trial
Indication: Moderate-to-severe ulcerative colitis
N=680, randomised 1:1:1 (MRDN-224 low dose, MRDN-224 high dose, placebo)
Primary endpoint: Clinical remission at week 12 (Mayo score ≤2, no subscore >1)
Power: 90% to detect 20% placebo-adjusted treatment effect, alpha 0.05
Historical placebo remission rate (class benchmark): ~10%
Study start: March 2023; primary completion: October 2025
```

```text
Phase 2 results (MRDN corporate presentation, March 2024)
Placebo-adjusted clinical remission: 42% at high dose, 38% at low dose
Safety: no dose-limiting toxicity; injection-site reactions 8%
Subgroup analysis: effect preserved in biologic-experienced and biologic-naive
```

```text
Class precedent data
Skyrizi UC Phase 3 (2022): 34% placebo-adjusted remission
Tremfya UC Phase 3 (2024): 30% placebo-adjusted remission
Stelara UC Phase 3 (2019): 12% placebo-adjusted remission
```

```text
Bloomberg sell-side consensus
Coverage: 7 Buy, 2 Hold, 0 Sell
Mean PT: $68 (current $51, 33% upside)
Base case PoS implied by valuation: approximately 75-80% for P3 success
```

```text
Options market — MRDN
Weekly straddle implied move into readout window: 38%
Open interest heavily skewed to upside strikes
```

**Output.**

### MRDN Phase 3 Readout Pre-Mortem — REGENCY-2 Trial

**What matters now.** Trial design is well-matched to the mechanism's Phase 2 signal but the non-inferiority margin vs Skyrizi is tight; the likely failure mode is a statistical hit that underwhelms clinically relative to the incumbent.

**Facts.** REGENCY-2 (ClinicalTrials.gov NCT05XXXXXX) enrolls 680 patients with moderate-to-severe UC, randomised 1:1:1 to two MRDN-224 doses and placebo at week 12 induction, with re-randomisation into maintenance. Primary endpoint is clinical remission at week 12 (Mayo score ≤2, no subscore >1), historical placebo rate approximately 10%. Phase 2 effect size was 42% placebo-adjusted clinical remission; statistical assumptions power the trial at 90% to detect a 20% placebo-adjusted treatment effect with alpha 0.05.

**Phase 2 → Phase 3 attenuation.** Base rate for IL-23 class in UC: Phase 2 to Phase 3 attenuation of approximately 25–30% in effect size is typical based on the Skyrizi and Tremfya precedents. Applied to MRDN's 42% Phase 2 signal, realistic Phase 3 expectation is 28–32% placebo-adjusted, which is clinically competitive but below the 34% Skyrizi delivered in its UC Phase 3.

**Outcome distribution (subjective).** Clear hit above 32% placebo-adjusted (best-in-class): 20%. Statistical hit 22–32% (competitive but not best-in-class): 45%. Marginal hit 15–22% (disappointing): 20%. Statistical miss: 15%. The probability of the "wins but disappoints" scenario — where the market re-rates lower despite a technical success — is the largest single bucket.

**Stock implications.** Clear hit: +35% to +50% based on comparable class precedent. Competitive hit: +5% to +15% (likely fade from initial relief rally). Marginal hit: –15% to –25% as the market recognises the competitive positioning gap. Statistical miss: –60% to –70% given limited pipeline depth.

**Variant view.** Sell-side is positioned for the clear hit scenario (consensus rating is 7 buys, 2 holds, 0 sells; average PT implies 34% upside). Options market is pricing a 38% implied move, which captures the tail scenarios but not the "wins but disappoints" intermediate case. My variant is that the "wins but disappoints" scenario is underweighted — the base-rate-adjusted effect size argues for a competitive but not best-in-class outcome, which is materially different from consensus framing.

**Disconfirming evidence.** If recent MRDN investor day commentary on baseline characteristics of enrolled patients implies a less severe population than Phase 2 (which would raise placebo rate and compress the effect size), my probability distribution should shift toward the marginal hit bucket.

**Positioning recommendation.** Trim to half size pre-readout. The asymmetric upside from a clear hit is still meaningful but the weighted expected return at current size is negative given the 45% weight on the "competitive hit" outcome with modest stock reaction and the 20% weight on material downside.

**Next diligence.** KOL call with a UC-focused gastroenterologist on how the community weights 28% vs 34% placebo-adjusted remission. Options market implied move vs my subjective distribution.

**Confidence: 0.65.** Effect-size prediction carries genuine uncertainty; probability distribution is subjective and should be treated as a framework rather than a forecast.

---

## Example 3 — 1-on-1 Management Question Stack (MGMT-01)

**Scenario.** The analyst has a 30-minute meeting scheduled with the CFO of Apex Medtech (fictional ticker APXM), a structural heart device company, at a healthcare conference. The thesis hinges on the ramp of the company's next-generation TAVR valve, launched 14 months ago.

**Prompt invoked.** MGMT-01: 1-on-1 Question Stack, with standing instructions applied.

**Reasoning scaffold.** Tier questions → anticipate evasion → design follow-ups → score answers.

**Source snippets supplied to the model:**

```text
APXM 10-Q (Q3 2025, filed 30 October 2025)
Structural Heart segment revenue: $412M (+18% Y/Y)
New-generation valve share of segment revenue: ~45% (disclosed at Q2)
Legacy valve inventory reserve: $40M at Q2 (no update provided)
Gross margin: 67.2% (vs 69.1% Y/Y)
Q3 earnings call (from transcript)
CFO: "Continuing to see strong momentum on the next-generation platform"
CEO: "European transition to the new generation is now substantially complete"
CFO: "We expect gross margin recovery to approach 70% by year-end 2026"
```

```text
Competitor (EDWRDS) Q3 transcript excerpt
"We are seeing continued payor coverage tightening on TAVR in low-risk patients.
Low-risk volume growth has plateaued in our US case mix since Q1."
```

```text
FactSet consensus
Q4 2025 segment revenue: $428M
2026 segment growth: +14%
2026 gross margin: 68.9%
```

```text
KOL call transcript (October 2025, structural heart cardiologist)
"Per-centre utilization has been running flat in mature EU centres for about three quarters.
US accounts that are 18+ months into the new generation platform are showing similar patterns."
```

**Output.**

### APXM CFO Meeting — Question Stack

**Tier 1 (must-ask, 5 questions).**

1. **"Your new-generation valve has been in market for 14 months. At what installed-base penetration does the mix shift stop being a tailwind to average selling price?"** *Boilerplate answer: "we continue to see strong momentum." Follow-up: "What per cent of installed base is now on the new generation — roughly — and what was ASP in Q3 vs Q1?" Informative answer: a specific penetration rate and the associated ASP trajectory.*

2. **"The prior generation was discontinued in Europe last quarter. When do you expect the same decision for the US, and what does that imply for remaining legacy inventory?"** *Boilerplate: "we'll make that decision based on customer readiness." Follow-up: "Is the legacy inventory reserve on the balance sheet — approximately $40M as of Q2 — sized for a 2026 discontinuation or a 2027 discontinuation?" Informative answer: clarification on the inventory write-down path.*

3. **"Edwards' Q3 transcript referenced payor coverage tightening on TAVR in low-risk patients. What are you seeing in your own case mix by risk category?"** *Boilerplate: "we have not seen any meaningful change." Follow-up: "If I look at your case mix shift over the last four quarters, is the low-risk share still growing — or has it plateaued?" Informative answer: direct acknowledgment of a plateau or continued growth with a specific data point.*

4. **"Gross margin in Q3 was 67%, down from 69% a year ago. Your guidance assumes recovery to 70% by year-end 2026. What is the single largest driver of that recovery, and what is its timing?"** *Boilerplate: "manufacturing productivity." Follow-up: "Is the next-generation valve more or less costly to manufacture at scale than the legacy product?" Informative answer: specific cost mechanism, ideally with a bps attribution.*

5. **"Your installed base in the EU has now been on the new valve for over two years. What has utilisation per centre done over the last four quarters?"** *Boilerplate: "we are seeing strong utilisation." Follow-up: "Is per-centre volume in the mature EU cohort accelerating, flat, or decelerating?" Informative answer: directional clarity on the utilisation trend, which is the single best indicator for US trajectory over the next 18 months. The KOL channel suggests the answer here is "flat," which would materially change the mid-cycle growth expectation.*

**Tier 2 (good-to-ask, 5 questions).** Omitted for brevity — would cover competitive response to the launch, capital allocation priorities given the pending cash build, the sales force productivity ramp, international pricing dynamics, and the strategic logic of the recent tuck-in acquisition.

**Tier 3 (colour, 5 questions).** Omitted for brevity — would cover CFO's read on the Street's framing of the story, the internal KPIs the management team watches most closely, succession thinking, talent retention in the commercial organisation, and culture under new CEO leadership.

**Confidence: 0.80.** Question stack is calibrated to the specific thesis; actual conversation may generate higher-leverage follow-ups based on CFO's volunteered comments.

---

## Example 4 — IC Memo Draft (COMM-01)

**Scenario.** The analyst wants to add a new long position in Lumen Diagnostics (fictional ticker LUMD), a liquid biopsy company, at a 2% initial weight. The IC meets Thursday.

**Prompt invoked.** COMM-01: IC Memo Draft, with standing instructions applied.

**Reasoning scaffold.** Structure memo → compress argument → tailor to audience → polish.

**Source snippets supplied to the model:**

```text
CMS National Coverage Determination (Final Memorandum, September 2025)
Coverage for multi-cancer early detection (MCED) testing in asymptomatic
Medicare beneficiaries aged 65-85, subject to shared decision-making documentation.
First CMS coverage decision for the MCED category.
```

```text
LUMD 10-Q (Q3 2025) and company materials
Medicare coverage effective 1 January 2026
Commercial payor coverage: 12M covered lives contracted, 60M addressable
Q3 2025 revenue $87M (+34% Y/Y)
Installed referral base: 4,100 physician practices
Cash: $640M, sufficient runway through 2027
```

```text
FactSet consensus
2026E MCED market size: $3.8B (low case) to $6.5B (high case)
LUMD 2028 market share consensus: 35%
Peer coverage: Exact Sciences, Grail (Illumina), Natera (adjacent)
```

```text
KOL calls (three sessions, October 2025)
Oncology practice administrator: "Once referrals move to one MCED provider,
the practice workflow makes switching effortful. We picked based on reimbursement
and trust in validation, not price."
Former payor contracting VP: "Medicare NCD materially shifts commercial
payor negotiations; typically commercial follows Medicare within 12-18 months."
```

```text
Competitor catalyst calendar (Bloomberg)
Exact Sciences Cologuard-Plus MCED expansion filing expected Q2 2026
Grail ongoing pivotal confirmation data expected H2 2026
```

**Output.**

### Lumen Diagnostics (LUMD) — IC Memo

**Recommendation.** Buy, initiating at 2% weight. 12-month target $38 (current $27, 41% upside). Expected IRR 32% at base case.

**Thesis (100 words).** LUMD's multi-cancer early detection (MCED) assay is the first to achieve Medicare coverage via an NCD-equivalent pathway, ahead of the two larger listed competitors. The Medicare coverage is the single binary that unlocks the real TAM — 60M annual covered lives — and the coverage decision de-risks the commercial model from "evidence-dependent" to "adoption-dependent." The market is pricing LUMD as if coverage is a modest advantage; my work suggests it is a 12–18 month head-start that translates into a durable share lead in a market where first-to-reimbursement has historically been decisive.

**Variant perception.** Consensus models 35% share of the MCED market for LUMD by 2028. My base case is 48% share, driven by Medicare coverage first-mover advantage, physician education infrastructure already built through the company's complementary colorectal screening franchise, and payor contracting leverage from the combined test menu. Supporting evidence: three KOL calls confirm referral-base switching is sticky once established; a former payor contracting VP confirmed that the Medicare NCD materially shifts commercial payor negotiation dynamics.

**Catalysts.** Q1 2026 marks the first full quarter of Medicare-reimbursed volume. Mid-2026 brings expected commercial payor coverage decisions following Medicare precedent. Late 2026 will see the competitor (Exact Sciences) expected MCED approval and reimbursement challenge.

**Risks.** Competitor catches up on reimbursement in 2026 — monitoring metric is quarterly commercial coverage tracker. Volume ramp disappoints — monitoring metric is sensor utilisation per centre vs company guide. Technology obsolescence from methylation-based assay improvement — monitoring metric is competitive clinical data at ASCO 2026.

**Sizing logic.** 2% reflects medium conviction and binary dependence on execution of a known opportunity. Would move to 4% on one clean quarterly print post-Medicare coverage confirming volume trajectory. Would exit at 15% stock decline from entry or on loss of market share lead indicator.

**Open questions for IC.** Is the Medicare coverage precedent genuinely durable, or is there political risk around MCED coverage under a different administration that I am underweighting? At 2% starting weight, am I leaving conviction on the table given the asymmetric upside?

**Confidence: 0.74.**

---

## Closing notes

These four examples span different workflow types (earnings, catalyst, management meeting, investment committee) and different sub-sectors (biotech, medtech, diagnostics). Each output follows the standing instructions' required behaviours: facts separated from inference, numbers time-stamped, disconfirming evidence surfaced, confidence score calibrated at the end. None of the outputs exceeds 700 words; the library is designed to compress analytical work, not expand it.

The source snippets shown above illustrate the format and density of inputs the library assumes. In practice, an analyst would paste or attach more comprehensive source material — a full 10-Q, the complete earnings transcript, the full sell-side note — rather than the condensed excerpts shown here. The examples use condensed snippets to illustrate the principle: structured, source-attributed inputs produce substantially better outputs than loose summaries or vague context.

The analyst using the library should expect to edit and supplement these outputs with primary research. The library's role is to impose structure and discipline, not to replace the analyst's judgment. The confidence score at the end of each output is the most important single element: it forces calibration and signals to the reader how much weight to place on the analysis.

*Healthcare Equity Analyst Prompt Library v1.4 — Worked Examples companion document*
