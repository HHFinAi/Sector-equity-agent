### INTL-01  European HTA Pathway Mapping

```yaml
id: INTL-01
title: European HTA Pathway Mapping
tags: [#international, #pharma, #biotech, #medtech, #senior-judgment]
use_when: "When assessing European commercial potential for a new drug or device launch, given the fragmentation of national HTA bodies and the forthcoming EU Joint Clinical Assessment (JCA)."
reasoning: "EU JCA scope → national HTA map → revenue bridge → thesis delta"
inputs: "EMA filing status, company European strategy disclosure, comparable-product HTA precedent, NICE/G-BA/HAS recent decisions in the therapeutic area."
output: "European HTA pathway map with country-level timing, reimbursement scenarios, and revenue bridge."
```

**Reasoning scaffold:** EU JCA scope → national HTA map → revenue bridge → thesis delta

**Prompt:**
```
Map the European HTA pathway for [TICKER]'s [asset] in [indication]. (1) EU Joint Clinical Assessment — is the asset in scope for the EU JCA regulation (oncology and ATMPs from 2025; orphan drugs from 2028; all new medicines from 2030)? If in scope, identify the likely JCA timeline, the comparator selection under the JCA framework, and the outcomes most likely to be weighted. (2) National HTA bodies of first order — for each of NICE (UK), G-BA/IQWiG (Germany), HAS/Transparency Commission (France), AIFA (Italy), and NIPN/CDF (Spain), state the typical time from EMA approval to national reimbursement decision, the evidence bar for a positive recommendation, and the most recent precedent decision in the therapeutic area. (3) Germany specifically — the AMNOG process governs launch pricing; a negative G-BA additional benefit assessment triggers price negotiation at or near comparator level, materially affecting the European revenue mix. State the realistic additional benefit category (major, considerable, minor, non-quantifiable, no additional benefit, less benefit) and its pricing implication. (4) England specifically — NICE cost-effectiveness threshold (£20,000–£30,000 per QALY base case, higher for end-of-life or highly specialised technologies), Cancer Drugs Fund eligibility for oncology, and the NHS England commercial negotiation process. (5) Revenue bridge — translate the HTA outcomes into a European revenue forecast, explicit on the country-level price, volume, and time-to-reimbursement. Model the realistic scenario where one or two major markets reach a restrictive HTA outcome and the others follow, because HTA outcomes often cluster. (6) Thesis delta — how does the European HTA pathway position affect the global peak sales assumption, the Europe-as-share-of-total forecast, and the launch cadence? Flag any name where a negative European outcome would materially change the investment case. End with confidence score.
```

---

