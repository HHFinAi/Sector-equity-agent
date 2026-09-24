# All-sector coverage

The agent covers all eleven major equity sectors on equal footing. The 79 groupings below are custom research subsectors, not the complete official GICS or SASB taxonomy. Each has its own economic lens, four KPI checks and a valuation-method allow-list in `sector_agent/sector_data.py`. Sector packs also define transmission tests, sources, sustainability materiality, analytical traps and diligence questions.

Export a workflow with `python -m sector_agent plan --brief examples/brief-template.json --out runs/plan` to obtain full standalone specialist prompts. `python -m sector_agent catalog` prints supported IDs.

## Energy — `energy`

Underwrite commodity exposure, the asset cost curve, production durability, capital discipline and cash returns. Separate resource economics from infrastructure contracts and service-cycle operating leverage.

**Research subsector IDs:** `exploration-production`, `integrated-oil-gas`, `refining-marketing`, `midstream-lng`, `oilfield-services`, `energy-equipment`, `coal-consumable-fuels`

## Materials — `materials`

Map global capacity, resource grade, conversion spreads, regional cost positions and replacement economics. Separate structural scarcity from temporary restocking.

**Research subsector IDs:** `diversified-mining`, `precious-metals`, `steel-aluminum`, `commodity-chemicals`, `specialty-chemicals`, `fertilizers-agriculture`, `industrial-gases`, `packaging-forest-products`, `construction-materials`

## Industrials — `industrials`

Distinguish orders, delivered output, installed-base service revenue and cash conversion. Underwrite cyclical operating leverage separately from recurring infrastructure economics.

**Research subsector IDs:** `aerospace-defense`, `machinery-automation`, `electrical-equipment`, `construction-engineering`, `building-products`, `airlines`, `transport-logistics`, `commercial-professional-services`, `waste-environmental-services`

## Consumer Discretionary — `consumer-discretionary`

Underwrite disposable-income sensitivity, customer cohorts, unit economics and brand/distribution advantage. Separate demand growth from promotional share gains.

**Research subsector IDs:** `automobiles-components`, `retail-ecommerce`, `apparel-luxury`, `restaurants`, `hotels-leisure`, `homebuilders-durables`, `travel-gaming`

## Consumer Staples — `consumer-staples`

Disaggregate price, volume and mix; test distribution strength, elasticity and sustainable cash generation rather than assuming defensive earnings.

**Research subsector IDs:** `food-beverages`, `household-personal-care`, `staples-retail-distribution`, `tobacco-nicotine`, `agricultural-processing`

## Health Care — `healthcare`

Connect clinical or service utility, reimbursement, adoption and capital needs to cash flows. Healthcare is one peer sector, not the default mandate.

**Research subsector IDs:** `biotech`, `pharma`, `medtech`, `services-payors`, `tools-diagnostics`, `digital-health`, `drug-distribution`, `cro-cdmo`

## Financials — `financials`

Separate balance-sheet intermediation from fee businesses. Underwrite capital adequacy, liquidity, credit losses and distributable equity earnings; do not force bank debt into industrial EV/EBITDA.

**Research subsector IDs:** `banks`, `consumer-finance`, `property-casualty-insurance`, `life-insurance`, `asset-wealth-management`, `exchanges-data`, `payments`, `brokers-investment-banks`

## Information Technology — `information-technology`

Underwrite technological bottlenecks, customer economics, monetization, replacement cycles and capital intensity. Separate business adoption from valuation already capitalizing that adoption.

**Research subsector IDs:** `semiconductors`, `semiconductor-equipment`, `software`, `it-services`, `hardware-devices`, `communications-equipment`, `electronic-components`

## Communication Services — `communication-services`

Disaggregate subscription, advertising, content and network economics. Test engagement monetization and distribution power against capital intensity and audience fragmentation.

**Research subsector IDs:** `telecom`, `broadband-cable`, `interactive-platforms`, `media-advertising`, `streaming-entertainment`, `gaming-content`

## Utilities — `utilities`

Separate regulated return recovery, merchant commodity exposure and contracted generation. Translate capital plans into financed, permitted assets and per-share distributable earnings.

**Research subsector IDs:** `regulated-electric-gas`, `water-utilities`, `merchant-power`, `renewable-generation`, `multi-utilities`

## Real Estate — `real-estate`

Underwrite property-level NOI, lease economics, capital needs and refinancing. Distinguish market appraisal, equity cash flow and development option value.

**Research subsector IDs:** `residential-reits`, `industrial-logistics-reits`, `retail-reits`, `office-reits`, `specialty-reits`, `diversified-reits`, `real-estate-services`, `developers-operators`

## Important boundaries

Company sector tags must be supplied and verified; a catalog does not identify issuer membership automatically. Multi-segment conglomerate exposures are not the same as an issuer classification. Coverage of all major sectors does not imply coverage of all securities, countries or official sub-industries. Source requests are not installed connectors. Method allow-lists are safeguards, not proof of valuation suitability.
