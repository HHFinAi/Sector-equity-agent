### SUB-TLS-05  Companion Diagnostic Linkage and Precision Medicine Coupling

```yaml
id: SUB-TLS-05
title: Companion Diagnostic Linkage and Precision Medicine Coupling
tags: [#tools-dx, #biotech, #pharma, #senior-judgment]
use_when: "When evaluating a precision medicine therapy where a companion diagnostic governs use, or a diagnostics name whose revenue depends on therapy-test coupling."
reasoning: "therapy-test couple → volume attribution → revenue translate"
inputs: "FDA approval letter and label for the therapy, CDx approval letter, clinical practice guidelines, peer commentary on testing patterns, company disclosures on testing volumes or partnerships."
output: "Therapy-diagnostic coupling analysis with volume flow, revenue translation, and model implications for both names."
```

**Reasoning scaffold:** therapy-test couple → volume attribution → revenue translate

**Prompt:**
```
Map the therapy-to-test linkage for [therapy TICKER] and [diagnostic TICKER]. (1) Regulatory coupling — is the companion diagnostic mandatory per the FDA label (CDx specified in the indications or dosing section), supportive but not required, or unapproved but commonly used? Cite the exact label language from Drugs@FDA. (2) CDx status — is the diagnostic FDA-approved as a CDx, CE-marked, or operating as a Laboratory Developed Test (LDT); which sponsor holds the approval and what testing platforms are covered. (3) Competing tests — list every test validated against the same biomarker, including LDTs from major reference labs (Quest, Labcorp, academic centres); rank by clinical adoption and by payor reimbursement; identify which test will actually capture volume in practice. (4) Volume flow — given the therapy's expected label, patient population, and testing cascade, what diagnostic test volume is realistically attributable to therapy uptake vs other indications testing the same biomarker? (5) Revenue translation — for the diagnostic company, the revenue contribution from this specific therapy launch; for the therapy company, the risk that test availability, turnaround time, or cost constrains prescription; for both, the scenario where LDT competition erodes the approved CDx's pricing. (6) Adoption acceleration or constraint — does the CDx accelerate therapy uptake (by defining an eligible population clearly) or constrain it (by adding diagnostic friction before prescribing)? (7) Model implications for both names. End with the confidence score.
```

---

