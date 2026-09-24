"""Deterministic, explicitly simplified valuation math; no LLM-generated inputs."""
from __future__ import annotations
from datetime import timedelta
from .contracts import require, number, text, iso_date


def dcf(cash_flows: list[float], discount_rate: float, terminal_growth: float) -> float:
    require(isinstance(cash_flows, list) and bool(cash_flows), "DCF needs annual unlevered cash flows")
    r = number(discount_rate, "discount_rate")
    g = number(terminal_growth, "terminal_growth")
    require(r > g and r > 0 and g > -1, "DCF requires discount_rate > terminal_growth, r > 0, g > -1")
    flows = [number(x, "cash_flow") for x in cash_flows]
    require(flows[-1] >= 0, "Negative terminal FCF: use explicit runoff or a different valuation method")
    terminal = flows[-1] * (1 + g) / (r - g)
    return sum(cf / (1 + r) ** t for t, cf in enumerate(flows, 1)) + terminal / (1 + r) ** len(flows)


def rnpv(cash_flows: list[float], probabilities: list[float], discount_rate: float) -> float:
    require(isinstance(cash_flows, list) and isinstance(probabilities, list) and
            0 < len(cash_flows) == len(probabilities), "rNPV requires aligned annual net FCF and occurrence probabilities")
    r = number(discount_rate, "discount_rate")
    require(r > 0, "rNPV discount_rate must be positive")
    result = 0.0
    for t, (cash, probability) in enumerate(zip(cash_flows, probabilities), 1):
        p = number(probability, "occurrence_probability")
        require(0 <= p <= 1, "Occurrence probability outside [0,1]")
        result += number(cash, "cash_flow") * p / (1 + r) ** t
    return result


def valuations(brief: dict) -> list[dict]:
    """Value bear/base/bull scenarios on a consistent as-of basis and equity bridge."""
    models = brief.get("valuation_models", [])
    require(isinstance(models, list), "valuation_models must be a list")
    entities = {x["id"] for x in brief["universe"]}
    source_ids = {x["id"] for x in brief.get("sources", [])}
    results = []
    seen = set()
    for model in models:
        require(isinstance(model, dict), "Valuation model must be an object")
        entity = model.get("entity")
        require(entity in entities and entity not in seen, "Unknown or duplicate valuation entity")
        seen.add(entity)
        text(model.get("currency"), "currency")
        require(model.get("units") == "millions", "Use millions for cash/revenue/FCF/debt and shares; price per share")
        require(model.get("basis") == "as_of_present_value", "Model values must use as_of_present_value basis")
        text(model.get("assumptions_note"), "assumptions_note")
        ids = model.get("source_ids")
        require(isinstance(ids, list) and bool(ids) and all(isinstance(x, str) for x in ids)
                and set(ids) <= source_ids, "Valuation requires valid input source IDs")
        price_date = iso_date(model.get("price_as_of"), "price_as_of")
        as_of = iso_date(brief["as_of"], "as_of")
        require(as_of - timedelta(days=7) <= price_date <= as_of, "Price is after cut-off or older than 7 days")
        price = number(model.get("price"), "price")
        shares = number(model.get("diluted_shares"), "diluted_shares")
        cash = number(model.get("cash"), "cash")
        debt = number(model.get("debt"), "debt")
        require(price > 0 and shares > 0 and cash >= 0 and debt >= 0, "Invalid price/shares/cash/debt")
        cases = model.get("scenarios")
        require(isinstance(cases, list) and len(cases) == 3 and
                all(isinstance(c, dict) for c in cases), "Exactly three scenarios required")
        require({c.get("name") for c in cases} == {"bear", "base", "bull"}, "Need unique bear/base/bull")
        probability_sum = 0.0
        values = []
        method = model.get("method")
        require(method in {"multiple", "dcf", "rnpv"}, "Unknown valuation method")
        for case in cases:
            p = number(case.get("probability"), "scenario probability")
            require(0 <= p <= 1, "Scenario probability outside [0,1]")
            probability_sum += p
            if method == "multiple":
                revenue = number(case.get("revenue"), "revenue")
                margin = number(case.get("ebitda_margin"), "ebitda_margin")
                multiple = number(case.get("ev_ebitda"), "ev_ebitda")
                require(revenue >= 0 and 0 < margin <= 1 and multiple > 0,
                        "EV/EBITDA requires positive EBITDA and multiple")
                ev = revenue * margin * multiple
            elif method == "dcf":
                ev = dcf(case.get("cash_flows"), case.get("discount_rate"), case.get("terminal_growth"))
            else:
                ev = rnpv(case.get("cash_flows"), case.get("occurrence_probabilities"), case.get("discount_rate"))
            equity = max(0.0, ev + cash - debt)
            fair_value = equity / shares
            values.append({"name": case["name"], "probability": p, "enterprise_value": ev,
                           "equity_value": equity, "value_per_share": fair_value,
                           "upside": fair_value / price - 1})
        require(abs(probability_sum - 1) <= 1e-8, "Scenario probabilities must sum to 1")
        ordered = {c["name"]: c["value_per_share"] for c in values}
        require(ordered["bear"] <= ordered["base"] <= ordered["bull"], "Scenario values are not bear <= base <= bull")
        expected = sum(c["probability"] * c["value_per_share"] for c in values)
        reverse = None
        if method == "multiple":
            base = next(c for c in cases if c["name"] == "base")
            market_ev = price * shares + debt - cash
            reverse = {"metric": "implied_revenue_at_base_margin_and_multiple",
                       "value": market_ev / (base["ebitda_margin"] * base["ev_ebitda"])}
        results.append({"entity": entity, "method": method, "currency": model["currency"],
                        "units": model["units"], "price_as_of": model["price_as_of"],
                        "scenarios": values, "expected_value_per_share": expected,
                        "expected_upside": expected / price - 1, "reverse_valuation": reverse,
                        "source_ids": ids, "assumptions_note": model["assumptions_note"],
                        "limitations": "Illustrative model; no automatic financial normalization, tax model, "
                        "dilution forecast, asset correlation or debt waterfall. Scenario weights are analyst assumptions."})
    return results
