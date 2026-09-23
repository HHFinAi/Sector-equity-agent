### INTL-02  Japanese Reimbursement Cycle and Price Revision Analysis

```yaml
id: INTL-02
title: Japanese Reimbursement Cycle and Price Revision Analysis
tags: [#international, #pharma, #biotech, #medtech, #senior-judgment]
use_when: "When Japan represents a material share of revenue or launch optionality for a drug or device, given Japan's distinctive biennial price revision cycle and foreign-price referencing system."
reasoning: "PMDA status → biennial revision → forecast → monitor"
inputs: "Company Japan-segment disclosure, PMDA filing status, NHI price list, prior biennial revision history, Chuikyo minutes for medtech."
output: "Japan reimbursement analysis with price revision forecast, asset-level exposure, and revenue trajectory."
```

**Reasoning scaffold:** PMDA status → biennial revision → forecast → monitor

**Prompt:**
```
Analyse [TICKER]'s Japan exposure. (1) PMDA approval and NHI listing — for each marketed or pipeline asset with Japanese exposure, the PMDA approval status, the time from PMDA approval to National Health Insurance (NHI) price listing (typically 60–90 days), and the premium or discount vs international reference prices at launch. (2) Biennial price revision — Japan revises NHI prices every two years (April in even years), with revisions driven by market-expansion redetermination (a price cut triggered when actual sales exceed forecast by defined thresholds), foreign average price adjustment, and the generic-substitution promotion mechanism. For each Japanese-exposed asset, estimate the next revision's directional impact and magnitude. The market-expansion redetermination is particularly relevant for oncology and orphan drugs where actual uptake exceeds the forecast embedded in the original price. (3) G1/G2 long-listed products — for legacy assets past their initial exclusivity period, model the accelerated price decline under the G1/G2 reclassification. (4) Cost-effectiveness programme — Japan's HTA mechanism applies to a subset of high-cost products (generally JPY 10B+ annual sales). Identify any asset entering the scope and the realistic cost-effectiveness outcome. (5) Medtech pricing — Japan's reimbursement for devices operates on a separate cycle via the Chuikyo process, with foreign average price comparison driving periodic adjustments. For medtech names with Japan exposure, state the equivalent exposure. (6) Japan-as-share-of-total — current Japan contribution to revenue, and how the biennial revision cycle affects the forward trajectory. Japan tends to step down revenue predictably; the surprise comes when it steps down faster than consensus models. End with confidence score.
```

---

