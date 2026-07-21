import importlib.util
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
STREAMDECK = ROOT / "StreamDeck"
SCRIPT = STREAMDECK / "tools" / "run_prompt_qa.py"
LIVE_SCRIPT = STREAMDECK / "tools" / "run_prompt_qa_live.py"
GENERATOR = STREAMDECK / "tools" / "generate_v3.py"
sys.path.insert(0, str(SCRIPT.parent))


def load_runner():
    spec = importlib.util.spec_from_file_location("run_prompt_qa", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_v3", GENERATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_live_runner():
    spec = importlib.util.spec_from_file_location("run_prompt_qa_live", LIVE_SCRIPT)
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


def without_live_runs(matrix):
    cleaned = json.loads(json.dumps(matrix))
    for row in cleaned["rows"]:
        for case in row["test_cases"]:
            case.pop("live_runs", None)
    cleaned["live_run_count"] = 0
    return cleaned


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


def test_api_and_live_runners_share_deterministic_checks():
    runner = load_runner()
    live = load_live_runner()

    assert runner.evaluate_response is live.evaluate_response
    assert runner.QaInput is live.QaInput


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


def test_tls_context_uses_system_bundle_when_python_has_no_default_ca(monkeypatch):
    runner = load_runner()
    expected_context = object()
    calls = []
    monkeypatch.setattr(
        runner.ssl,
        "get_default_verify_paths",
        lambda: SimpleNamespace(cafile=None, capath=None),
    )
    monkeypatch.setattr(
        runner.Path,
        "is_file",
        lambda path: path == runner.Path("/etc/ssl/cert.pem"),
    )

    def fake_create_default_context(*, cafile=None):
        calls.append(cafile)
        return expected_context

    monkeypatch.setattr(runner.ssl, "create_default_context", fake_create_default_context)

    assert runner.tls_context() is expected_context
    assert calls == ["/etc/ssl/cert.pem"]


def test_resume_selects_only_cases_not_executed_by_provider():
    runner = load_runner()
    matrix = {
        "rows": [
            {
                "prompt_id": "example",
                "test_cases": [
                    {"case": "normal", "status": "EXECUTED", "provider": "google"},
                    {"case": "missing_context_or_evidence", "status": "EXECUTED", "provider": "openai"},
                    {"case": "unsafe_or_ambiguous", "status": "NOT RUN"},
                ],
            }
        ]
    }

    assert runner.completed_case_keys(matrix, "google") == {("example", "normal")}


def test_generator_preserves_only_matching_executed_qa_results():
    generator = load_generator()
    generated_rows = [
        {
            "prompt_id": "same-version",
            "prompt_version": "1.0.0",
            "prompt_hash": "a" * 64,
            "test_cases": [
                {"case": "normal", "status": "NOT RUN", "expected": "current contract"},
                {"case": "unsafe_or_ambiguous", "status": "NOT RUN", "expected": "current refusal"},
            ],
        },
        {
            "prompt_id": "new-version",
            "prompt_version": "2.0.0",
            "prompt_hash": "b" * 64,
            "test_cases": [{"case": "normal", "status": "NOT RUN", "expected": "new contract"}],
        },
    ]
    existing = {
        "rows": [
            {
                "prompt_id": "same-version",
                "prompt_version": "1.0.0",
                "prompt_hash": "a" * 64,
                "test_cases": [
                    {
                        "case": "normal",
                        "status": "EXECUTED",
                        "expected": "old contract",
                        "provider": "google",
                        "observed_verdict": "pass",
                    },
                    {"case": "unsafe_or_ambiguous", "status": "NOT RUN", "expected": "old refusal"},
                ],
            },
            {
                "prompt_id": "new-version",
                "prompt_version": "1.0.0",
                "prompt_hash": "b" * 64,
                "test_cases": [
                    {"case": "normal", "status": "EXECUTED", "expected": "old contract"}
                ],
            },
        ]
    }

    assert generator.preserve_executed_qa_results(generated_rows, existing) == 1
    assert generated_rows[0]["test_cases"][0] == {
        "case": "normal",
        "status": "EXECUTED",
        "expected": "current contract",
        "provider": "google",
        "observed_verdict": "pass",
    }
    assert generated_rows[0]["test_cases"][1]["status"] == "NOT RUN"
    assert generated_rows[1]["test_cases"][0]["status"] == "NOT RUN"


def test_generator_preserves_live_runs_without_replacing_api_fields():
    generator = load_generator()
    live_run = {
        "provider": "chatgpt_web",
        "model_id": "UI model",
        "executed_at": "2026-07-15T00:00:00Z",
    }
    generated = [{"prompt_id": "example", "prompt_version": "1.0.0", "prompt_hash": "a" * 64, "test_cases": [{"case": "normal", "status": "NOT RUN", "expected": "current"}]}]
    existing = {"rows": [{"prompt_id": "example", "prompt_version": "1.0.0", "prompt_hash": "a" * 64, "test_cases": [{"case": "normal", "status": "EXECUTED", "expected": "old", "provider": "google", "live_runs": [live_run]}]}]}

    assert generator.preserve_executed_qa_results(generated, existing) == 1
    assert generated[0]["test_cases"][0]["provider"] == "google"
    assert generated[0]["test_cases"][0]["expected"] == "current"
    assert generated[0]["test_cases"][0]["live_runs"] == [live_run]


def test_generator_does_not_preserve_results_for_changed_prompt_body():
    generator = load_generator()
    generated = [{
        "prompt_id": "example",
        "prompt_version": "1.0.0",
        "prompt_hash": "b" * 64,
        "test_cases": [{"case": "normal", "status": "NOT RUN", "expected": "current"}],
    }]
    existing = {"rows": [{
        "prompt_id": "example",
        "prompt_version": "1.0.0",
        "prompt_hash": "a" * 64,
        "test_cases": [{"case": "normal", "status": "EXECUTED", "expected": "old"}],
    }]}

    assert generator.preserve_executed_qa_results(generated, existing) == 0
    assert generated[0]["test_cases"][0]["status"] == "NOT RUN"


def test_live_runner_uses_project_knowledge_only_for_normal_and_persists_no_raw(tmp_path: Path):
    live = load_live_runner()
    registry, matrix, _ = load_sources()
    matrix = without_live_runs(matrix)
    prompt = registry["prompts"][0]
    inputs = [
        live.QaInput(prompt["prompt_id"], prompt["prompt_version"], case, prompt["body"], tuple(prompt["output_schema"]), "unused")
        for case in live.CASE_NAMES
    ]

    class MockBrowser:
        def __init__(self):
            self.calls = []

        def run_project_prompt(self, **kwargs):
            self.calls.append(kwargs)
            headings = "\n".join(f"## {label.split(':', 1)[0]}\nblocked / NOT RUN" for label in prompt["output_schema"])
            return live.BrowserResult(headings, "GPT UI test model")

    browser = MockBrowser()
    output = tmp_path / "matrix.json"
    updated, failures = live.run_live_qa(
        browser, registry, matrix, inputs, matrix_path=output, manifest_path=None,
        checkpoint_every=2, retries=0, retry_base_seconds=0,
    )

    assert failures == []
    assert [call["use_project_knowledge"] for call in browser.calls] == [True, False, False]
    assert all(call["insertion_method"] == "clipboard_paste" for call in browser.calls)
    assert all("Ignore earlier chat turns and outputs" in call["request_text"] for call in browser.calls)
    assert "SYNTHETIC QA CONTEXT" not in browser.calls[0]["request_text"]
    assert all("SYNTHETIC QA CONTEXT" in call["request_text"] for call in browser.calls[1:])
    assert all("do not use Project Knowledge" in call["request_text"] for call in browser.calls[1:])
    row = next(item for item in updated["rows"] if item["prompt_id"] == prompt["prompt_id"])
    assert updated["live_run_count"] == 3
    for case in row["test_cases"]:
        run = case["live_runs"][0]
        assert set(run) == {"provider", "model_id", "executed_at", "response_sha256", "response_chars", "deterministic_checks", "observed_verdict"}
        assert not ({"response", "raw_response", "request", "request_text", "api_key"} & set(run))


def test_live_resume_uses_prompt_and_case_key():
    live = load_live_runner()
    matrix = {"rows": [{"prompt_id": "example", "test_cases": [{"case": "normal", "live_runs": [{"provider": "chatgpt_web"}]}, {"case": "unsafe_or_ambiguous"}]}]}

    assert live.completed_live_case_keys(matrix) == {("example", "normal")}
    assert live.browser_project("[LLM] / Judge") == "[LLM]"
    assert live.browser_project("[Analytics]") == "[Analytics]"


def test_live_cli_next_and_record_use_stdin_without_persisting_raw(tmp_path: Path):
    registry, matrix, _ = load_sources()
    matrix = without_live_runs(matrix)
    matrix_path = tmp_path / "matrix.json"
    matrix_path.write_text(json.dumps(matrix, ensure_ascii=False), encoding="utf-8")

    next_result = subprocess.run(
        [sys.executable, str(LIVE_SCRIPT), "--next", "--matrix", str(matrix_path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert next_result.returncode == 0, next_result.stderr
    work = json.loads(next_result.stdout)
    assert work["prompt_id"] == registry["prompts"][0]["prompt_id"]
    assert work["case"] == "normal"
    assert work["insertion_method"] == "clipboard_paste"

    response = "\n".join(
        f"## {label.split(':', 1)[0]}\nblocked / NOT RUN"
        for label in registry["prompts"][0]["output_schema"]
    )
    record_result = subprocess.run(
        [
            sys.executable,
            str(LIVE_SCRIPT),
            "--record",
            "--record-prompt-id",
            work["prompt_id"],
            "--record-case",
            work["case"],
            "--model-id",
            "GPT UI test model",
            "--matrix",
            str(matrix_path),
        ],
        cwd=ROOT,
        input=response,
        check=False,
        capture_output=True,
        text=True,
    )
    assert record_result.returncode == 0, record_result.stderr
    stored_text = matrix_path.read_text(encoding="utf-8")
    stored = json.loads(stored_text)
    assert response not in stored_text
    assert stored["live_run_count"] == 1
    row = next(item for item in stored["rows"] if item["prompt_id"] == work["prompt_id"])
    assert row["test_cases"][0]["live_runs"][0]["model_id"] == "GPT UI test model"


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
    matrix = without_live_runs(matrix)
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
