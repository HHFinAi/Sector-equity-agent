"""Explicit opt-in LLM adapter; never crawls source URLs or executes model text."""
from __future__ import annotations
import json
import os
import time
import urllib.error
import urllib.request
from .contracts import STAGE_SCHEMA, ValidationError, require


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValidationError("LLM endpoint redirect refused; credentials were not forwarded")


def parse_response(value: dict) -> dict:
    require(value.get("status") == "completed", "LLM response incomplete or failed; no result accepted")
    parts = []
    for item in value.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if part.get("type") == "refusal":
                raise ValidationError("LLM refused the request; no result accepted")
            if part.get("type") == "output_text":
                parts.append(part.get("text", ""))
    require(bool(parts), "LLM returned no output text")
    try:
        return json.loads("".join(parts))
    except (ValueError, TypeError) as exc:
        raise ValidationError("LLM did not return valid JSON") from exc


class OpenAIProvider:
    """Responses API. Environment-held key; fixed HTTPS host; bounded calls and output."""
    name = "openai"

    def __init__(self, *, model: str, allow_network: bool, max_calls: int = 48,
                 max_input_chars: int = 750_000, max_output_tokens: int = 5000):
        require(allow_network, "Live mode requires --allow-network: public evidence will be sent to OpenAI")
        require(bool(model.strip()), "Set --model or OPENAI_MODEL to an available model ID")
        key = os.environ.get("OPENAI_API_KEY", "")
        require(bool(key.strip()), "OPENAI_API_KEY is not set")
        require(1 <= max_calls <= 100, "max_calls must be 1-100")
        require(1000 <= max_input_chars <= 1_000_000, "Invalid max_input_chars")
        require(256 <= max_output_tokens <= 32_000, "Invalid max_output_tokens")
        self.model, self._key = model, key
        self.max_calls, self.calls = max_calls, 0
        self.max_input_chars, self.max_output_tokens = max_input_chars, max_output_tokens
        self.usage = []
        self.opener = urllib.request.build_opener(NoRedirect())

    def generate(self, stage: str, instructions: str, context: dict) -> dict:
        content = json.dumps(context, ensure_ascii=False, allow_nan=False)
        require(len(content) + len(instructions) <= self.max_input_chars,
                "Context exceeds configured character limit; curate sources instead of silently truncating")
        body = {"model": self.model, "store": False, "instructions": instructions,
                "input": content, "max_output_tokens": self.max_output_tokens,
                "text": {"format": {"type": "json_schema", "name": "research_stage",
                                     "strict": True, "schema": STAGE_SCHEMA}}}
        request = urllib.request.Request("https://api.openai.com/v1/responses",
            data=json.dumps(body, allow_nan=False).encode(), method="POST",
            headers={"Authorization": f"Bearer {self._key}", "Content-Type": "application/json"})
        for attempt in range(3):
            require(self.calls < self.max_calls, "LLM HTTP request budget exhausted")
            self.calls += 1
            try:
                with self.opener.open(request, timeout=120) as response:
                    raw = response.read(2_000_001)
                require(len(raw) <= 2_000_000, "LLM response exceeds 2 MB limit")
                value = json.loads(raw)
                result = parse_response(value)
                self.usage.append({"stage": stage, "response_id": value.get("id"),
                                   "usage": value.get("usage", {}), "http_calls_total": self.calls})
                return result
            except urllib.error.HTTPError as exc:
                if exc.code in {429, 500, 502, 503, 504} and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise ValidationError(f"LLM HTTP {exc.code}; response body omitted to avoid leaking data") from exc
            except urllib.error.URLError as exc:
                raise ValidationError("LLM network failure; no automatic retry after ambiguous delivery") from exc
        raise ValidationError("LLM retry budget exhausted")


class DemoProvider:
    """Synthetic test harness, deliberately NOT an LLM or investment analysis."""
    name = "demo"
    model = "deterministic-fixture-not-an-llm"

    def __init__(self):
        self.calls = 0
        self.usage = []

    def generate(self, stage: str, instructions: str, context: dict) -> dict:
        sources = context["brief"]["sources"]
        if not sources:
            return {"summary": "DEMO ONLY: no scoped evidence supplied", "claims": [],
                    "gaps": ["Missing scoped evidence"], "thesis_breakers": ["No investment thesis in a fixture"],
                    "decision": "needs_data"}
        source = sources[0]
        return {
            "summary": f"DEMO ONLY: {stage} contract executed; no live research or model inference.",
            "claims": [{"id": f"{stage}-fixture", "topic": "fixture-validation",
                        "kind": "assumption", "text": "Synthetic fixture used to exercise evidence routing and review gates.",
                        "source_ids": [source["id"]], "confidence": 0.0}],
            "gaps": ["Replace synthetic inputs and use a live provider for actual research."],
            "thesis_breakers": ["No investable thesis exists in this demonstration."],
            "decision": "needs_data"
        }
