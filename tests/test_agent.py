"""Offline regression tests. No test reaches an external service."""
import copy
import io
import json
import os
import tempfile
import unittest
import urllib.error
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

from sector_agent.contracts import (ROOT, ValidationError, canonical, load_json, number,
                                    validate_brief, validate_stage)
from sector_agent.engine import approve, build_plan, export_plan, run, verify
from sector_agent.models import dcf, rnpv, valuations
from sector_agent.provider import DemoProvider, NoRedirect, OpenAIProvider, parse_response


def fixture():
    data = load_json(ROOT / "examples" / "demo-brief.json")
    # Tests remain valid after the checked-in example's date without changing its cut-off.
    return copy.deepcopy(data)


def public_fixture():
    data = fixture()
    for source in data["sources"]:
        source["kind"] = "company"
        source["url"] = "https://example.org/test-fixture-not-real-evidence"
    return data


def valid_stage():
    return {"summary": "Test-only summary", "claims": [
        {"id": "test-1", "topic": "unit-test", "kind": "fact", "text": "Test-only claim",
         "source_ids": ["SYN1"], "confidence": 0.5}], "gaps": [],
         "thesis_breakers": ["Test-only falsification condition"], "decision": "continue"}


class ScriptedProvider:
    name = "scripted-test"
    model = "not-a-live-model"
    calls = 0
    usage = []
    def generate(self, stage, instructions, context):
        return valid_stage()


class ContractTests(unittest.TestCase):
    def test_demo_input_valid(self):
        self.assertEqual(validate_brief(fixture(), demo=True), [])

    def test_synthetic_rejected_live(self):
        with self.assertRaisesRegex(ValidationError, "synthetic"):
            validate_brief(fixture())

    def test_no_sources_rejected_but_plan_allowed(self):
        data = fixture(); data["sources"] = []
        with self.assertRaisesRegex(ValidationError, "No sources"):
            validate_brief(data)
        self.assertIn("specialist_healthcare", build_plan(data)["stages"])

    def test_future_publication_rejected(self):
        data = fixture(); data["sources"][0]["published_at"] = "2026-09-25"
        with self.assertRaisesRegex(ValidationError, "look-ahead"):
            validate_brief(data, demo=True)

    def test_future_as_of_rejected(self):
        data = fixture(); data["as_of"] = (date.today() + timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValidationError, "future"):
            validate_brief(data, demo=True)

    def test_stale_source_rejected(self):
        data = fixture(); data["sources"][0]["published_at"] = "2025-01-01"
        with self.assertRaisesRegex(ValidationError, "stale"):
            validate_brief(data, demo=True)

    def test_duplicate_sources_rejected(self):
        data = fixture(); data["sources"].append(data["sources"][0])
        with self.assertRaisesRegex(ValidationError, "Duplicate source"):
            validate_brief(data, demo=True)

    def test_private_input_rejected(self):
        data = fixture(); data["sources"][0]["public"] = False
        with self.assertRaisesRegex(ValidationError, "public"):
            validate_brief(data, demo=True)

    def test_credentials_in_source_url_rejected(self):
        data = public_fixture(); data["sources"][0]["url"] = "https://user:secret@example.org"
        with self.assertRaisesRegex(ValidationError, "credentials"):
            validate_brief(data)

    def test_path_traversal_rejected(self):
        data = fixture(); data["sector"] = "../../secret"
        with self.assertRaisesRegex(ValidationError, "unsafe ID"):
            build_plan(data)

    def test_bool_and_nan_are_not_numbers(self):
        for value in (True, float("nan"), float("inf"), "4"):
            with self.subTest(value=value), self.assertRaises(ValidationError):
                number(value, "test")

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.json"; path.write_text('{"x":1,"x":2}')
            with self.assertRaisesRegex(ValidationError, "Duplicate JSON key"):
                load_json(path)

    def test_unknown_citation_rejected(self):
        stage = valid_stage(); stage["claims"][0]["source_ids"] = ["INVENTED"]
        with self.assertRaisesRegex(ValidationError, "unknown source"):
            validate_stage(stage, {"SYN1"})

    def test_uncited_fact_and_inference_rejected(self):
        for kind in ("fact", "inference"):
            stage = valid_stage(); stage["claims"][0].update(kind=kind, source_ids=[])
            with self.subTest(kind=kind), self.assertRaisesRegex(ValidationError, "require source"):
                validate_stage(stage, {"SYN1"})

    def test_unresolved_gap_cannot_continue(self):
        stage = valid_stage(); stage["gaps"] = ["Missing source"]
        with self.assertRaisesRegex(ValidationError, "needs_data"):
            validate_stage(stage, {"SYN1"})

    def test_invalid_confidence_rejected(self):
        stage = valid_stage(); stage["claims"][0]["confidence"] = 1.5
        with self.assertRaisesRegex(ValidationError, "confidence"):
            validate_stage(stage, {"SYN1"})


class ModelTests(unittest.TestCase):
    def test_dcf_known_value(self):
        self.assertAlmostEqual(dcf([100], 0.1, 0), 1000)

    def test_invalid_terminal_growth_rejected(self):
        with self.assertRaises(ValidationError):
            dcf([100], 0.03, 0.04)

    def test_negative_terminal_flow_rejected(self):
        with self.assertRaises(ValidationError):
            dcf([-100], 0.1, 0.02)

    def test_rnpv_weights_cost_and_revenue_separately_by_period(self):
        self.assertAlmostEqual(rnpv([-100, 300], [1, 0.5], 0.1), -100/1.1 + 150/(1.1**2))

    def test_rnpv_invalid_probability_rejected(self):
        with self.assertRaises(ValidationError):
            rnpv([100], [1.2], 0.1)

    def test_scenario_math_and_reverse_valuation(self):
        model = valuations(fixture())[0]
        self.assertAlmostEqual(model["expected_value_per_share"], 29.0075)
        self.assertAlmostEqual(model["reverse_valuation"]["value"], 2050/(0.22*12))

    def test_invalid_scenario_weights_rejected(self):
        data = fixture(); data["valuation_models"][0]["scenarios"][0]["probability"] = 0.9
        with self.assertRaisesRegex(ValidationError, "sum to 1"):
            valuations(data)

    def test_zero_shares_rejected(self):
        data = fixture(); data["valuation_models"][0]["diluted_shares"] = 0
        with self.assertRaises(ValidationError):
            valuations(data)

    def test_future_or_stale_price_rejected(self):
        for price_date in ("2026-09-25", "2026-09-01"):
            data = fixture(); data["valuation_models"][0]["price_as_of"] = price_date
            with self.subTest(date=price_date), self.assertRaises(ValidationError):
                valuations(data)

    def test_inverted_scenarios_rejected(self):
        data = fixture(); data["valuation_models"][0]["scenarios"][0]["revenue"] = 10000
        with self.assertRaisesRegex(ValidationError, "bear <= base <= bull"):
            valuations(data)

    def test_no_model_means_no_invented_numbers(self):
        data = fixture(); data["valuation_models"] = []
        self.assertEqual(valuations(data), [])


class RuntimeTests(unittest.TestCase):
    def test_all_workflows_export(self):
        catalog = load_json(ROOT / "workflows" / "catalog.json")
        with tempfile.TemporaryDirectory() as tmp:
            for flow in catalog:
                data = fixture(); data["workflow"] = flow
                out = Path(tmp) / flow
                plan = export_plan(data, out)
                self.assertEqual(plan["stages"][-1], "synthesis")
                self.assertEqual(len(list(out.glob("*.md"))), len(plan["stages"]))

    def test_demo_is_marked_and_not_approvable(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"
            result = run(fixture(), DemoProvider(), out)
            self.assertEqual(result["status"], "DEMO")
            self.assertTrue(verify(out)["verified"])
            self.assertIn("SYNTHETIC DEMONSTRATION", (out/"report.md").read_text())
            with self.assertRaisesRegex(ValidationError, "Cannot approve"):
                approve(out, "test-reviewer", "test only", True)

    def test_completed_workflow_requires_explicit_human_attestation(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"
            result = run(public_fixture(), ScriptedProvider(), out)
            self.assertEqual(result["status"], "NEEDS_HUMAN_REVIEW")
            with self.assertRaisesRegex(ValidationError, "acknowledge"):
                approve(out, "test-reviewer", "test only", False)
            approve(out, "test-reviewer", "Test-only attestation, not real research review", True)
            self.assertTrue(verify(out)["reviewed"])
            with self.assertRaisesRegex(ValidationError, "already"):
                approve(out, "test-reviewer", "test only", True)

    def test_edit_after_run_invalidates_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"; run(fixture(), DemoProvider(), out)
            (out / "report.md").write_text("changed")
            with self.assertRaisesRegex(ValidationError, "Changed run artifact"):
                verify(out)

    def test_extra_file_invalidates_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"; run(fixture(), DemoProvider(), out)
            (out / "extra.txt").write_text("unexpected")
            with self.assertRaisesRegex(ValidationError, "file set"):
                verify(out)

    def test_existing_output_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileExistsError):
                run(fixture(), DemoProvider(), Path(tmp))

    def test_invalid_stage_stops_and_records_failure(self):
        class InvalidProvider(ScriptedProvider):
            def generate(self, *args):
                value = valid_stage(); value["claims"][0]["source_ids"] = ["FAKE"]
                return value
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"
            with self.assertRaises(ValidationError):
                run(public_fixture(), InvalidProvider(), out)
            self.assertTrue((out / "error.json").exists())
            self.assertFalse((out / "result.json").exists())
            self.assertTrue(verify(out)["verified"])

    def test_prior_stages_cannot_hide_gaps(self):
        class GapProvider(ScriptedProvider):
            def generate(self, stage, instructions, context):
                value = valid_stage()
                if stage == "evidence":
                    value.update(gaps=["Evidence missing"], decision="needs_data")
                return value
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"
            result = run(public_fixture(), GapProvider(), out)
            self.assertEqual(result["status"], "BLOCKED")
            with self.assertRaisesRegex(ValidationError, "Cannot approve"):
                approve(out, "test", "test only", True)


class ProviderTests(unittest.TestCase):
    def test_network_requires_opt_in(self):
        with self.assertRaisesRegex(ValidationError, "allow-network"):
            OpenAIProvider(model="test-model", allow_network=False)

    def test_missing_key_fails_before_network(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValidationError, "API_KEY"):
            OpenAIProvider(model="test-model", allow_network=True)

    def test_refusal_and_incomplete_outputs_fail_closed(self):
        for response in ({"status":"incomplete"}, {"status":"completed", "output":[
            {"type":"message", "content":[{"type":"refusal", "refusal":"test"}]}]}):
            with self.subTest(response=response), self.assertRaises(ValidationError):
                parse_response(response)

    def test_parse_response(self):
        response = {"status":"completed", "output":[{"type":"message", "content":[
            {"type":"output_text", "text":json.dumps(valid_stage())}]}]}
        self.assertEqual(parse_response(response), valid_stage())

    def test_redirects_refused(self):
        with self.assertRaisesRegex(ValidationError, "redirect refused"):
            NoRedirect().redirect_request(None, None, 302, None, None, "https://example.org")

    def test_live_request_contract_without_network(self):
        payload = {"status":"completed", "id":"mock-response", "usage":{}, "output":[
            {"type":"message", "content":[{"type":"output_text", "text":json.dumps(valid_stage())}]}]}
        with patch.dict(os.environ, {"OPENAI_API_KEY":"test-key-not-a-secret"}):
            provider = OpenAIProvider(model="test-model", allow_network=True)
        response = io.BytesIO(json.dumps(payload).encode())
        with patch.object(provider.opener, "open", return_value=response) as mock:
            self.assertEqual(provider.generate("evidence", "test instructions", {}), valid_stage())
            request = mock.call_args.args[0]
            body = json.loads(request.data)
            self.assertEqual(request.full_url, "https://api.openai.com/v1/responses")
            self.assertFalse(body["store"])
            self.assertTrue(body["text"]["format"]["strict"])
            self.assertNotIn("tools", body)
            self.assertEqual(provider.calls, 1)

    def test_character_limit_prevents_network(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY":"test-key"}):
            provider = OpenAIProvider(model="test", allow_network=True, max_input_chars=1000)
        with patch.object(provider.opener, "open") as mock, self.assertRaisesRegex(ValidationError, "Context exceeds"):
            provider.generate("test", "x"*1100, {})
        mock.assert_not_called()

    def test_retry_budget_counts_http_attempts(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY":"test-key"}):
            provider = OpenAIProvider(model="test", allow_network=True, max_calls=1)
        error = urllib.error.HTTPError("https://api.openai.com", 429, "mock", {}, None)
        with patch.object(provider.opener, "open", side_effect=error), patch("time.sleep"), self.assertRaisesRegex(ValidationError, "budget exhausted"):
            provider.generate("test", "test", {})
        self.assertEqual(provider.calls, 1)


if __name__ == "__main__":
    unittest.main()
