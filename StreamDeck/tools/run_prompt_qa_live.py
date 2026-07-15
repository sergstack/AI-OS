#!/usr/bin/env python3
"""Coordinate Prompt QA through Codex browser automation and ChatGPT Projects.

The browser adapter is supplied by the authenticated Codex browser session. This
module never reads credentials, session tokens, or browser storage, and never
persists raw prompts or responses. Multiline insertion must use clipboard paste.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from qa_checks import CASE_NAMES, SYNTHETIC_CONTEXTS, QaInput, evaluate_response
from run_prompt_qa import (
    DEFAULT_MATRIX,
    DEFAULT_REGISTRY,
    STREAMDECK,
    build_inputs,
    load_json,
    resolve_subset,
    utc_now,
    write_results,
)


PROVIDER = "chatgpt_web"
INSERTION_METHOD = "clipboard_paste"
PROJECT_ALIASES = {
    "[LLM] / Judge": "[LLM]",
    "[LLM] / Local AI": "[LLM]",
    "[LLM] / Memo": "[LLM]",
    "[LLM] / Revisor": "[LLM]",
}


@dataclass(frozen=True)
class BrowserResult:
    """Ephemeral result observed in the ChatGPT UI; response_text is never persisted."""

    response_text: str
    model_id: str


class BrowserAdapter(Protocol):
    """Adapter implemented by Codex's already-authenticated browser automation."""

    def run_project_prompt(
        self,
        *,
        owner_project: str,
        request_text: str,
        insertion_method: str,
        use_project_knowledge: bool,
    ) -> BrowserResult: ...


def build_live_request_text(body: str, case_name: str) -> str:
    prefix = (
        "Run this Prompt QA case in the current ChatGPT Project. Follow the exact Stream Deck prompt body "
        "below; do not claim unobserved execution.\n\n--- PROMPT BODY ---\n"
        f"{body}"
    )
    if case_name == "normal":
        return (
            f"{prefix}\n\n--- QA CONTEXT ---\n"
            "Use only the current Project Knowledge and the prompt body as source material. "
            "Do not invent missing facts; mark unavailable evidence NOT RUN or blocked."
        )
    return (
        f"{prefix}\n\n--- SYNTHETIC QA CONTEXT ---\n"
        "For this adverse case, do not use Project Knowledge; use only the synthetic context below.\n"
        f"{SYNTHETIC_CONTEXTS[case_name]}"
    )


def browser_project(owner_project: str) -> str:
    return PROJECT_ALIASES.get(owner_project, owner_project)


def with_live_request(qa_input: QaInput) -> QaInput:
    return QaInput(
        prompt_id=qa_input.prompt_id,
        prompt_version=qa_input.prompt_version,
        case_name=qa_input.case_name,
        body=qa_input.body,
        output_schema=qa_input.output_schema,
        request_text=build_live_request_text(qa_input.body, qa_input.case_name),
    )


def live_result(qa_input: QaInput, observed: BrowserResult, executed_at: str | None = None) -> dict[str, Any]:
    if not observed.response_text:
        raise ValueError("empty ChatGPT response")
    if not observed.model_id.strip():
        raise ValueError("model_id was not observed in the ChatGPT UI")
    checks = evaluate_response(qa_input, observed.response_text)
    return {
        "provider": PROVIDER,
        "model_id": observed.model_id.strip(),
        "executed_at": executed_at or utc_now(),
        "response_sha256": hashlib.sha256(observed.response_text.encode("utf-8")).hexdigest(),
        "response_chars": len(observed.response_text),
        "deterministic_checks": checks,
        "observed_verdict": "pass" if checks["expected_behavior"] == "pass" else "revise",
    }


def apply_live_result(
    matrix: dict[str, Any], qa_input: QaInput, result: dict[str, Any]
) -> dict[str, Any]:
    updated = copy.deepcopy(matrix)
    row = next(item for item in updated["rows"] if item["prompt_id"] == qa_input.prompt_id)
    case = next(item for item in row["test_cases"] if item["case"] == qa_input.case_name)
    case.setdefault("live_runs", []).append(result)
    updated["live_run_count"] = sum(
        len(item.get("live_runs", []))
        for matrix_row in updated["rows"]
        for item in matrix_row["test_cases"]
    )
    return updated


def completed_live_case_keys(matrix: dict[str, Any]) -> set[tuple[str, str]]:
    return {
        (row["prompt_id"], case["case"])
        for row in matrix["rows"]
        for case in row["test_cases"]
        if any(run.get("provider") == PROVIDER for run in case.get("live_runs", []))
    }


def run_live_qa(
    browser: BrowserAdapter,
    registry: dict[str, Any],
    matrix: dict[str, Any],
    qa_inputs: list[QaInput],
    *,
    matrix_path: Path,
    manifest_path: Path | None,
    checkpoint_every: int = 10,
    retries: int = 2,
    retry_base_seconds: float = 1.0,
) -> tuple[dict[str, Any], list[tuple[QaInput, str]]]:
    if checkpoint_every < 1 or retries < 0 or retry_base_seconds < 0:
        raise ValueError("invalid checkpoint or retry setting")
    projects = {
        item["prompt_id"]: browser_project(item["owner_project"])
        for item in registry["prompts"]
    }
    working = matrix
    failures: list[tuple[QaInput, str]] = []
    completed_since_checkpoint = 0
    for base_input in qa_inputs:
        qa_input = with_live_request(base_input)
        error = "browser call failed"
        for attempt in range(retries + 1):
            try:
                observed = browser.run_project_prompt(
                    owner_project=projects[qa_input.prompt_id],
                    request_text=qa_input.request_text,
                    insertion_method=INSERTION_METHOD,
                    use_project_knowledge=qa_input.case_name == "normal",
                )
                working = apply_live_result(working, qa_input, live_result(qa_input, observed))
                completed_since_checkpoint += 1
                break
            except Exception as exc:  # browser adapters expose implementation-specific errors
                error = f"{type(exc).__name__}: {exc}"
                if attempt < retries:
                    time.sleep(retry_base_seconds * (2**attempt))
        else:
            failures.append((qa_input, error))
        if completed_since_checkpoint >= checkpoint_every:
            write_results(working, matrix_path, manifest_path)
            completed_since_checkpoint = 0
    if completed_since_checkpoint:
        write_results(working, matrix_path, manifest_path)
    return working, failures


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="assemble browser work without opening ChatGPT")
    parser.add_argument("--resume", action="store_true", help="skip cases with an existing chatgpt_web live run")
    parser.add_argument("--subset", action="append")
    parser.add_argument("--case", action="append", choices=CASE_NAMES)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    args = parser.parse_args(argv)
    if not args.dry_run:
        parser.error("run this driver from Codex with a BrowserAdapter; standalone live browser execution is unavailable")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        registry = load_json(args.registry)
        matrix = load_json(args.matrix)
        actions = load_json(STREAMDECK / "config" / "action_profiles.json")
        prompt_ids = {item["prompt_id"] for item in registry["prompts"]}
        selected_ids = resolve_subset(args.subset, prompt_ids, actions)
        qa_inputs = build_inputs(registry, matrix, selected_ids, set(args.case or CASE_NAMES))
        if args.resume:
            completed = completed_live_case_keys(matrix)
            qa_inputs = [item for item in qa_inputs if (item.prompt_id, item.case_name) not in completed]
    except (OSError, KeyError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(
        f"DRY RUN: prompts={len({item.prompt_id for item in qa_inputs})} cases={len(qa_inputs)}; "
        f"provider={PROVIDER} insertion={INSERTION_METHOD} browser calls=0 writes=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
