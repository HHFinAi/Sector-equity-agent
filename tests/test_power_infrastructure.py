"""Smoke and economic-invariant tests for the November BE/EQIX research scaffold."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from sector_agent.contracts import validate_brief

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "examples/power-infrastructure"
SPEC = importlib.util.spec_from_file_location("power_bridges", HERE / "models.py")
BRIDGES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BRIDGES)


class PowerInfrastructureResearch(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((HERE / "synthetic-inputs.json").read_text())

    def test_bloom_orders_supplier_and_manufacturing_constraints(self):
        a = BRIDGES.bloom_order_to_fcf(self.data["manufacturer"])
        self.assertAlmostEqual(a["deliveries_gw"], 0.6)
        self.assertAlmostEqual(a["product_revenue_usd_m"], 1200)
        self.assertAlmostEqual(a["beginning_base_service_revenue_usd_m"], 30)
        changed = copy.deepcopy(self.data["manufacturer"])
        changed["supplier_available_gw"] = 0.2
        b = BRIDGES.bloom_order_to_fcf(changed)
        self.assertAlmostEqual(b["deliveries_gw"], 0.2)
        self.assertLess(b["operating_cash_contribution_before_financing_usd_m"],
                        a["operating_cash_contribution_before_financing_usd_m"])

    def test_shipments_do_not_create_same_year_service_revenue(self):
        a = copy.deepcopy(self.data["manufacturer"])
        base = BRIDGES.bloom_order_to_fcf(a)
        a["orders_gw"] *= 2
        b = BRIDGES.bloom_order_to_fcf(a)
        self.assertEqual(base["beginning_base_service_revenue_usd_m"],
                         b["beginning_base_service_revenue_usd_m"])

    def test_eqix_affo_and_dilution(self):
        x = BRIDGES.equinix_development_to_affo(self.data["reit"])
        self.assertEqual(x["new_leased_mw"], 32)
        self.assertAlmostEqual(x["incremental_cash_noi_usd_m"], 48)
        self.assertAlmostEqual(x["incremental_affo_usd_m"], 19)
        self.assertAlmostEqual(x["pro_forma_affo_per_share_usd"], 1019 / 102)
        self.assertLess(x["change_affo_per_share_usd"], 0)

    def test_development_capex_not_double_charged_to_affo(self):
        a = copy.deepcopy(self.data["reit"])
        before = BRIDGES.equinix_development_to_affo(a)
        a["development_capex_usd_m"] += 100
        after = BRIDGES.equinix_development_to_affo(a)
        self.assertEqual(before["incremental_affo_usd_m"], after["incremental_affo_usd_m"])
        self.assertEqual(after["development_capex_separate_from_affo_usd_m"], 350)

    def test_fake_numbers_cannot_silently_be_relabelled(self):
        for model, sample in ((BRIDGES.bloom_order_to_fcf, self.data["manufacturer"]),
                              (BRIDGES.equinix_development_to_affo, self.data["reit"])):
            a = copy.deepcopy(sample)
            a["classification"] = "ISSUER_FORECAST"
            with self.assertRaises(ValueError):
                model(a)
            a = copy.deepcopy(sample)
            a[next(k for k in a if k not in ("classification",) and isinstance(a[k], (int, float)))] = float("nan")
            with self.assertRaises(ValueError):
                model(a)

    def test_brief_plans_but_cannot_run_without_primary_sources(self):
        b = json.loads((HERE / "brief.json").read_text())
        self.assertEqual(validate_brief(b, plan_only=True), [])
        with self.assertRaisesRegex(ValueError, "No sources"):
            validate_brief(b)
        self.assertEqual({x["id"] for x in b["universe"]}, {"BE", "EQIX"})

    def test_watchlist_not_false_probabilities(self):
        events = json.loads((HERE / "catalysts.json").read_text())
        self.assertIn("UNVERIFIED", events["status"])
        self.assertTrue(all(e["status"] == "NEEDS_PRIMARY_SOURCE" and "probability" not in e
                            for e in events["items"]))


if __name__ == "__main__":
    unittest.main()
