import json
import unittest
from pathlib import Path

class TestClimateResilienceContract(unittest.TestCase):
    def test_templates_remain_explicitly_unverified(self):
        doc=json.loads((Path(__file__).resolve().parents[1]/"examples/climate-resilience-screen-template.json").read_text())
        self.assertEqual(len(doc["categories"]),7)
        self.assertEqual(doc["research_mode"],"NEEDS_DATA")
        self.assertEqual(doc["issuer_record_template"]["outcome"],"NEEDS_DATA")
        self.assertIsNone(doc["issuer_record_template"]["as_of_market_price_utc"])
        self.assertFalse(doc["issuer_record_template"]["asset_locations_verified"])
        self.assertEqual({x["study"] for x in doc["candidate_cohorts"]},
                         {"cooling_hvac","resilient_power","resilient_urban"})

if __name__=="__main__": unittest.main()
