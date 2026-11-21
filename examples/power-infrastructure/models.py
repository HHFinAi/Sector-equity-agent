"""Explicit issuer-specific *illustrative* cash-flow bridges for AI-power research.

Do not describe this as BE or EQIX guidance, contractual economics, or a
whole-company valuation. Inputs must be explicitly synthetic; live research
passes through the existing sector-agent primary-evidence gates.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASSIFICATION = "SYNTHETIC_TEST_ECONOMICS_NOT_ISSUER_FORECAST"


def num(row, key, *, fraction=False, positive=False):
    value = row.get(key)
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError(f"{key}: finite numeric input required")
    if value < 0 or (positive and value <= 0) or (fraction and value > 1):
        raise ValueError(f"{key}: invalid range")
    return float(value)


def check_label(row):
    if not isinstance(row, dict) or row.get("classification") != CLASSIFICATION:
        raise ValueError("Synthetic classification mandatory; issuer facts need separate workflow")


def bloom_order_to_fcf(row):
    """Orders -> shipment constraints -> product/service GP -> cash contribution.

    End-of-period installed-base additions are not assumed to create a
    full additional year of service revenue immediately.
    """
    check_label(row)
    orders = num(row, "orders_gw")
    conversion = num(row, "order_conversion_fraction", fraction=True)
    capacity = num(row, "manufacturing_capacity_gw")
    supplier = num(row, "supplier_available_gw")
    price = num(row, "price_usd_m_per_gw")
    product_margin = num(row, "product_gross_margin", fraction=True)
    base = num(row, "beginning_installed_base_gw")
    service_price = num(row, "service_revenue_usd_m_per_installed_gw_year")
    service_margin = num(row, "service_gross_margin", fraction=True)
    cash_opex = num(row, "cash_opex_usd_m")
    capex = num(row, "capital_expenditure_usd_m")
    working_capital = num(row, "working_capital_increase_usd_m")
    taxes = num(row, "cash_taxes_usd_m")
    eligible = orders * conversion
    delivered = min(eligible, capacity, supplier)
    product_sales = delivered * price
    service_sales = base * service_price
    gross = product_sales * product_margin + service_sales * service_margin
    cash_contribution = gross - cash_opex - capex - working_capital - taxes
    denominator = delivered * product_margin
    required_price = ((cash_opex + capex + working_capital + taxes - service_sales * service_margin)
                      / denominator if denominator > 0 else None)
    return {
        "classification": CLASSIFICATION, "company_lens": "fuel_cell_manufacturer",
        "deliveries_gw": delivered,
        "unconverted_orders_gw": orders * (1 - conversion),
        "converted_but_unshipped_gw": eligible - delivered,
        "product_revenue_usd_m": product_sales,
        "beginning_base_service_revenue_usd_m": service_sales,
        "gross_profit_usd_m": gross,
        "operating_cash_contribution_before_financing_usd_m": cash_contribution,
        "cash_break_even_price_usd_m_per_gw": max(0, required_price) if required_price is not None else None,
        "valuation_status": "NO_MARKET_VALUE_OR_ISSUER_FORECAST",
    }


def equinix_development_to_affo(row):
    """Separate project operating contribution, AFFO/share and funding capex."""
    check_label(row)
    base_affo = num(row, "baseline_affo_usd_m")
    shares = num(row, "baseline_diluted_shares_m", positive=True)
    commissioned = num(row, "commissioned_mw")
    lease = num(row, "leased_fraction", fraction=True)
    year = num(row, "in_service_year_fraction", fraction=True)
    noi_per_mw = num(row, "annual_cash_noi_usd_m_per_leased_mw")
    maint = num(row, "incremental_maintenance_capex_usd_m")
    corporate = num(row, "incremental_corporate_cash_cost_usd_m")
    interest = num(row, "incremental_cash_interest_usd_m")
    taxes = num(row, "incremental_cash_taxes_usd_m")
    additional_shares = num(row, "additional_diluted_shares_m")
    development_capex = num(row, "development_capex_usd_m")
    leased = commissioned * lease
    incremental_noi = leased * year * noi_per_mw
    incremental_affo = incremental_noi - maint - corporate - interest - taxes
    before = base_affo / shares
    after = (base_affo + incremental_affo) / (shares + additional_shares)
    return {
        "classification": CLASSIFICATION, "company_lens": "data_center_reit",
        "new_commissioned_mw": commissioned,
        "new_leased_mw": leased,
        "incremental_cash_noi_usd_m": incremental_noi,
        "incremental_affo_usd_m": incremental_affo,
        "baseline_affo_per_share_usd": before,
        "pro_forma_affo_per_share_usd": after,
        "change_affo_per_share_usd": after - before,
        "development_capex_separate_from_affo_usd_m": development_capex,
        "funding_and_nav_unresolved": True,
        "valuation_status": "NO_MARKET_VALUE_OR_ISSUER_FORECAST",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="evaluate fictional test fixture")
    args = parser.parse_args()
    if not args.demo:
        parser.error("Only --demo is supported; live issuer analysis requires verified sources")
    case = json.loads((HERE / "synthetic-inputs.json").read_text(encoding="utf-8"))
    output = {
        "notice": "FICTIONAL UNIT-ECONOMICS DEMONSTRATION; not BE/EQIX forecasts",
        "manufacturer": bloom_order_to_fcf(case["manufacturer"]),
        "reit": equinix_development_to_affo(case["reit"]),
    }
    print(json.dumps(output, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
