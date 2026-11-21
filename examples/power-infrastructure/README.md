# AI power / data-centre issuers: research intake and unit-economics bridges

**21 November 2026 | Work-in-progress | BE / EQIX named research cases, NOT security forecasts.**

This scoped extension uses the current full-sector workflow, not a new agent.
Bloom Energy (BE) is provisionally mapped to Industrials / electrical equipment;
Equinix (EQIX) to Real Estate / specialty REITs. Verify classifications and
segment exposures against current filings. A two-sector [research brief](brief.json)
uses the existing cross-sector comparison route with **no source records**.
That means planning may execute but live valuation **must be blocked** until
dated, suitably licensed primary evidence has been registered.

## Two distinct cash-flow questions

**Bloom Energy: orders → qualified deliverable GW → product revenue and
gross profit → cash contribution.** Supply-chain-available capacity and
manufacturing throughput are separate from customer shipments. The service
base is opening installed capacity, not same-year newly delivered orders.
Actual services, contractual payments, CCS/45Q eligibility, gross margin,
production yields, replacement/retrofit rights and the equity bridge all
require issuer evidence.

**Equinix: commissioned MW → leased MW → realized cash NOI → incremental
AFFO/share.** Model the fraction of the year a campus is operating, cash
maintenance, financing and dilution. Development capex is exposed separately:
it is not automatically the same thing as an AFFO deduction. Project/phase
MW must not be equated with an entire campus or summed across overlapping
announcements. Current stock price, EV and market-implied AFFO require
additional dated observations.

These are intentionally **different accounting bridges**. An equipment maker
must not be valued on a REIT AFFO multiple; a REIT should not have its
development outlay double-charged in AFFO and financing.

## Run a plan or fictional arithmetic demo

~~~bash
python -m sector_agent plan --brief examples/power-infrastructure/brief.json --out runs/be-eqix-plan
python examples/power-infrastructure/models.py --demo
python -m unittest discover -s tests -p 'test_power_infrastructure.py' -v
~~~

The tiny [fixture](synthetic-inputs.json) consists entirely of imaginary
values chosen to test the bridge. The [watchlist](catalysts.json) is *unverified
and unscored*, NOT an ex ante probability register, backtest or scheduled
monitor. The local scripts perform no web retrieval or trading.

## Verification gates and report provenance

Morgan Stanley's 19 November 2026 *Clean Tech & Data Center Infrastructure –
SF Bus Tour Roundup* informed the research questions (contracting, buildout,
service, capital recovery and hybrid power). The sell-side document is not
redistributed and its observations are **not** represented here as
independently authenticated company records.

Next ingest public, dated issuer filings, earnings materials, data-centre
development disclosures, power/permit approvals, service contracts where
available, and synchronized market prices/estimates. Distinguish announced
orders, backlog, firm contract, shipment, installation, service commencement,
company revenue and consolidated FCF. Event probabilities should not be
fabricated from management confidence.

The two arithmetic bridges are stand-alone *preliminary scaffolds*. No
whole-company DCF, observed upside, validated execution probability, analyst
approval or alpha is claimed. The live sector agent already has separate
primary-source validation, claim ledgers, company initiation, earnings
read-through and catalyst-review routes: use those before issuer conclusions.
