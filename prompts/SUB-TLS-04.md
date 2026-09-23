### SUB-TLS-04  IVD Reagent Pull-Through Rate Calculator

```yaml
id: SUB-TLS-04
title: IVD Reagent Pull-Through Rate Calculator
tags: [#tools-dx, #modeling, #senior-judgment]
use_when: "For IVD instrument/consumables names where menu breadth utilisation is the margin driver."
reasoning: "IVD reagent → installed base → pull-through → model"
inputs: "Company disclosures, assay menu data, peer benchmarks."
output: "Pull-through analysis with menu utilisation and margin sensitivity."
```

**Reasoning scaffold:** IVD reagent → installed base → pull-through → model

**Prompt:**
```
Reagent pull-through for [TICKER]. (1) Installed IVD instruments by platform; (2) assay menu breadth (number of approved tests per platform); (3) reagent revenue per instrument per year; (4) menu utilisation rate (tests actually run vs tests available); (5) menu expansion pipeline; (6) competitive pull-through benchmarks; (7) gross margin sensitivity to utilisation changes.
```

---

