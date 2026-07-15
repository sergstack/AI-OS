import importlib.util
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STREAMDECK = ROOT / "StreamDeck"
SCRIPT = STREAMDECK / "tools" / "run_prompt_qa.py"


def load_runner():
    spec = importlib.util.spec_from_file_location("run_prompt_qa", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_sources():
    registry = json.loads((STREAMDECK / "prompts" / "prompt_registry.json").read_text(encoding="utf-8"))
    matrix = json.loads((STREAMDECK / "qa" / "prompt_qa_matrix.json").read_text(encoding="utf-8"))
    actions = json.loads((STREAMDECK / "config" / "action_profiles.json").read_text(encoding="utf-8"))
    return registry, matrix, actions


def test_builds_all_and_priority_inputs():
    runner = load_runner()
    registry, matrix, actions = load_sources()
    prompt_ids = {item["prompt_id"] for item in registry["prompts"]}

    all_inputs = runner.build_inputs(registry, matrix, prompt_ids, set(runner.CASE_NAMES))
    priority_ids = runner.resolve_subset(["priority"], prompt_ids, actions)
    priority_inputs = runner.build_inputs(registry, matrix, priority_ids, set(runner.CASE_NAMES))

    assert len(prompt_ids) == 140
    assert len(all_inputs) == 420
    assert len(priority_ids) == 15
    assert len(priority_inputs) == 45
    assert {item.case_name for item in all_inputs} == set(runner.CASE_NAMES)
    assert all("--- PROMPT BODY ---" in item.request_text for item in all_inputs)


def test_dry_run_cli_makes_no_writes():
    before = (STREAMDECK / "qa" / "prompt_qa_matrix.json").read_bytes()
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    after = (STREAMDECK / "qa" / "prompt_qa_matrix.json").read_bytes()
    assert result.returncode == 0, result.stderr
    assert "prompts=140 cases=420" in result.stdout
    assert "API calls=0 writes=0" in result.stdout
    assert after == before


def test_deterministic_schema_and_adverse_case_evaluation():
    runner = load_runner()
    qa_input = runner.QaInput(
        prompt_id="example",
        prompt_version="1.1.0",
        case_name="missing_context_or_evidence",
        body='The first response line must be `Selected material: "<first about 10 words>"`.',
        output_schema=("Decision", "Execution status: EXECUTED / PARTIAL / NOT RUN", "Next action"),
        request_text="synthetic",
    )
    passing = """Selected material: "No source artifact or decision evidence is supplied"

## Decision
blocked because the source is missing

## Execution status
NOT RUN

## Next action
Provide the source artifact."""
    failing = """Selected material: "No source artifact or decision evidence is supplied"

## Decision
I inferred the missing facts.

## Execution status
EXECUTED
"""

    passed = runner.evaluate_response(qa_input, passing)
    failed = runner.evaluate_response(qa_input, failing)

    assert passed == {
        "schema_fit": "pass",
        "missing_sections": [],
        "material_selection": "pass",
        "blocked_or_not_run": "pass",
        "unsafe_action_claim_free": "pass",
        "expected_behavior": "pass",
    }
    assert failed["schema_fit"] == "fail"
    assert failed["unsafe_action_claim_free"] == "fail"
    assert failed["expected_behavior"] == "fail"


def test_api_payload_extractors_and_usage_are_provider_specific():
    runner = load_runner()
    openai_payload = {
        "model": "test-openai",
        "output": [{"type": "message", "content": [{"type": "output_text", "text": "hello"}]}],
        "usage": {"input_tokens": 10, "output_tokens": 4, "total_tokens": 14},
    }
    anthropic_payload = {
        "model": "test-anthropic",
        "content": [{"type": "text", "text": "hello"}],
        "usage": {"input_tokens": 11, "output_tokens": 5},
    }
    google_payload = {
        "modelVersion": "gemini-2.5-flash",
        "candidates": [{"content": {"parts": [{"text": "hello"}]}}],
        "usageMetadata": {"promptTokenCount": 12, "candidatesTokenCount": 6, "totalTokenCount": 18},
    }

    assert runner.extract_openai_text(openai_payload) == "hello"
    assert runner.extract_anthropic_text(anthropic_payload) == "hello"
    assert runner.extract_google_text(google_payload) == "hello"
    assert runner.normalized_usage("openai", openai_payload) == {
        "input_tokens": 10,
        "output_tokens": 4,
        "total_tokens": 14,
    }
    assert runner.normalized_usage("anthropic", anthropic_payload) == {
        "input_tokens": 11,
        "output_tokens": 5,
        "total_tokens": 16,
    }
    assert runner.normalized_usage("google", google_payload) == {
        "input_tokens": 12,
        "output_tokens": 6,
        "total_tokens": 18,
    }


def test_google_provider_uses_gemini_api_key(monkeypatch):
    runner = load_runner()
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "not-a-real-key")

    assert runner.choose_provider("google") == ("google", "not-a-real-key")
    assert runner.choose_provider("auto") == ("google", "not-a-real-key")


def test_google_call_uses_generate_content_contract(monkeypatch):
    runner = load_runner()
    observed = {}
    qa_input = runner.QaInput(
        prompt_id="example",
        prompt_version="1.0.0",
        case_name="normal",
        body="Return exactly these sections: Decision",
        output_schema=("Decision",),
        request_text="synthetic",
    )

    def fake_post(url, headers, body, timeout):
        observed.update(url=url, headers=headers, body=body, timeout=timeout)
        return {
            "modelVersion": "gemini-2.5-flash",
            "candidates": [{"content": {"parts": [{"text": "## Decision\nProceed."}]}}],
            "usageMetadata": {"promptTokenCount": 7, "candidatesTokenCount": 3, "totalTokenCount": 10},
        }

    monkeypatch.setattr(runner, "post_json", fake_post)
    result = runner.call_google("not-a-real-key", "gemini-2.5-flash", qa_input, 1200, 30.0)

    assert observed["url"].endswith("/models/gemini-2.5-flash:generateContent")
    assert observed["headers"]["x-goog-api-key"] == "not-a-real-key"
    assert observed["body"] == {
        "contents": [{"role": "user", "parts": [{"text": "synthetic"}]}],
        "generationConfig": {"maxOutputTokens": 1200},
    }
    assert observed["timeout"] == 30.0
    assert result.model_id == "gemini-2.5-flash"
    assert result.text == "## Decision\nProceed."


def test_retry_repeats_only_sanitized_retryable_failures(monkeypatch):
    runner = load_runner()
    attempts = []
    qa_input = runner.QaInput(
        prompt_id="example",
        prompt_version="1.0.0",
        case_name="normal",
        body="Return exactly these sections: Decision",
        output_schema=("Decision",),
        request_text="synthetic",
    )

    def fake_call(*_args):
        attempts.append(1)
        if len(attempts) == 1:
            raise runner.ApiCallError("HTTP 429; retryable=true")
        return runner.ApiResult(text="## Decision\nProceed.", model_id="test-model", usage={})

    monkeypatch.setattr(runner, "call_openai", fake_call)
    monkeypatch.setattr(runner.time, "sleep", lambda _seconds: None)
    _, result, error = runner.run_one(
        "openai", "not-a-real-key", "test-model", qa_input, 100, 1.0, 2, 0.0
    )

    assert len(attempts) == 2
    assert error is None
    assert result is not None
    assert result["status"] == "EXECUTED"
    assert result["observed_verdict"] == "pass"


def test_result_write_preserves_gates_and_updates_manifest_checksum(tmp_path: Path):
    runner = load_runner()
    registry, matrix, _ = load_sources()
    prompt = registry["prompts"][0]
    qa_input = runner.QaInput(
        prompt_id=prompt["prompt_id"],
        prompt_version=prompt["prompt_version"],
        case_name="normal",
        body=prompt["body"],
        output_schema=tuple(prompt["output_schema"]),
        request_text="synthetic",
    )
    result = {
        "status": "EXECUTED",
        "provider": "openai",
        "model_id": "test-model",
        "executed_at": "2026-07-15T00:00:00Z",
        "observed_verdict": "pass",
        "deterministic_checks": {
            "schema_fit": "pass",
            "missing_sections": [],
            "material_selection": "not_applicable",
            "blocked_or_not_run": "not_applicable",
            "unsafe_action_claim_free": "pass",
            "expected_behavior": "pass",
        },
        "response_sha256": "a" * 64,
        "response_chars": 42,
        "usage": {"input_tokens": 10, "output_tokens": 5, "total_tokens": 15},
    }
    updated = runner.apply_results(matrix, [(qa_input, result)])
    output = tmp_path / "prompt_qa_matrix.json"
    runner.write_results(updated, output, None)
    written = json.loads(output.read_text(encoding="utf-8"))
    row = next(item for item in written["rows"] if item["prompt_id"] == prompt["prompt_id"])
    case = next(item for item in row["test_cases"] if item["case"] == "normal")

    assert case["status"] == "EXECUTED"
    assert case["model_id"] == "test-model"
    assert "response" not in case
    assert row["owner_acceptance"] == "pending"
    assert row["criteria_passed"] == 9
    assert row["judge_verdict"] == "blocked"
    assert row["formal_gate_status"] == "blocked - not 10/10"

    copied = tmp_path / "StreamDeck"
    shutil.copytree(STREAMDECK, copied)
    copied_matrix = copied / "qa" / "prompt_qa_matrix.json"
    copied_matrix.write_bytes(runner.json_bytes(updated))
    copied_manifest = copied / "migration" / "migration_manifest.json"
    manifest = json.loads(copied_manifest.read_text(encoding="utf-8"))
    matrix_hash = hashlib.sha256(copied_matrix.read_bytes()).hexdigest()
    next(item for item in manifest["files"] if item["path"] == "qa/prompt_qa_matrix.json")["sha256"] = matrix_hash
    copied_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    validation = subprocess.run(
        [sys.executable, str(copied / "tools" / "validate_v3.py")],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )
    assert validation.returncode == 0, validation.stdout + validation.stderr
    assert "PASS: references, routing, hashes" in validation.stdout
