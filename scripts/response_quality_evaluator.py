#!/usr/bin/env python3
"""Evaluate curated response fixtures without calling an LLM or storing live output.

The input is a reviewed synthetic fixture.  The evaluator enforces the
deterministic portion of the LLM quality contract and combines it with an
already-observed Judge verdict.  It deliberately does not infer factual
support from prose: unsupported claims must be supplied as an explicit review
finding by the fixture author or an independent Judge.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


RESPONSE_CLASSES = {"direct", "evidence_sensitive", "codex_handoff"}
VERDICTS = {"pass", "revise", "blocked", "not_run"}


class ContractError(ValueError):
    """Raised when a reviewed fixture is incomplete or internally inconsistent."""


@dataclass(frozen=True)
class QualityResult:
    case_id: str
    response_class: str
    deterministic_findings: tuple[str, ...]
    unsupported_claims: tuple[str, ...]
    judge_verdict: str
    revision_count: int
    final_quality_status: str


def _string_list(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ContractError(f"{field} must be a list of strings")
    return value


def _required_groups(value: Any) -> list[list[str]]:
    if not isinstance(value, list) or any(
        not isinstance(group, list) or not group or any(not isinstance(item, str) for item in group)
        for group in value
    ):
        raise ContractError("required_groups must be a list of non-empty string lists")
    return value


def validate_case(case: dict[str, Any]) -> None:
    required = {
        "case_id",
        "response_class",
        "response",
        "required_groups",
        "forbidden_phrases",
        "unsupported_claims",
        "judge_required",
        "judge_verdict",
        "revision_count",
        "unresolved_material_findings",
        "expected_verdict",
    }
    missing = sorted(required - case.keys())
    if missing:
        raise ContractError(f"case missing fields: {', '.join(missing)}")
    if not isinstance(case["case_id"], str) or not case["case_id"].strip():
        raise ContractError("case_id must be a non-empty string")
    if case["response_class"] not in RESPONSE_CLASSES:
        raise ContractError("invalid response_class")
    if not isinstance(case["response"], str) or not case["response"].strip():
        raise ContractError("response must be a non-empty synthetic string")
    _required_groups(case["required_groups"])
    for field in ("forbidden_phrases", "unsupported_claims", "unresolved_material_findings"):
        _string_list(case[field], field)
    if not isinstance(case["judge_required"], bool):
        raise ContractError("judge_required must be boolean")
    if case["judge_verdict"] not in VERDICTS:
        raise ContractError("invalid judge_verdict")
    if not isinstance(case["revision_count"], int) or case["revision_count"] < 0:
        raise ContractError("revision_count must be a non-negative integer")
    if case["expected_verdict"] not in VERDICTS - {"not_run"}:
        raise ContractError("invalid expected_verdict")


def evaluate_case(case: dict[str, Any]) -> QualityResult:
    validate_case(case)
    response = case["response"].casefold()
    findings: list[str] = []
    for group in _required_groups(case["required_groups"]):
        if not any(marker.casefold() in response for marker in group):
            findings.append(f"missing required marker group: {' | '.join(group)}")
    for phrase in _string_list(case["forbidden_phrases"], "forbidden_phrases"):
        if phrase.casefold() in response:
            findings.append(f"forbidden phrase present: {phrase}")

    unsupported = tuple(_string_list(case["unsupported_claims"], "unsupported_claims"))
    unresolved = _string_list(case["unresolved_material_findings"], "unresolved_material_findings")
    judge_verdict = str(case["judge_verdict"])
    if case["judge_required"] and judge_verdict == "not_run":
        final = "blocked"
    elif judge_verdict == "blocked" or unresolved or case["revision_count"] > 1:
        final = "blocked"
    elif findings or unsupported or judge_verdict == "revise":
        final = "revise"
    else:
        final = "pass"
    return QualityResult(
        case_id=case["case_id"],
        response_class=case["response_class"],
        deterministic_findings=tuple(findings),
        unsupported_claims=unsupported,
        judge_verdict=judge_verdict,
        revision_count=case["revision_count"],
        final_quality_status=final,
    )


def record_for(case: dict[str, Any]) -> dict[str, Any]:
    result = evaluate_case(case)
    if result.final_quality_status != case["expected_verdict"]:
        raise ContractError(
            f"{result.case_id}: expected {case['expected_verdict']}, got {result.final_quality_status}"
        )
    return {
        "schema_version": "response-quality-eval-v1",
        "case_id": result.case_id,
        "response_class": result.response_class,
        "response_sha256": hashlib.sha256(case["response"].encode("utf-8")).hexdigest(),
        "deterministic_findings": list(result.deterministic_findings),
        "unsupported_claims": list(result.unsupported_claims),
        "judge_verdict": result.judge_verdict,
        "revision_count": result.revision_count,
        "final_quality_status": result.final_quality_status,
        "limitations": [
            "Fixture response is synthetic and does not establish live Project behaviour.",
            "Unsupported claims are explicit review findings; this evaluator does not infer factual support.",
        ],
    }


def evaluate_fixture(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        raise ContractError("fixture must be an object with a cases list")
    case_ids = [case.get("case_id") for case in payload["cases"] if isinstance(case, dict)]
    if len(case_ids) != len(payload["cases"]) or len(set(case_ids)) != len(case_ids):
        raise ContractError("fixture case_id values must be unique strings")
    return [record_for(case) for case in payload["cases"] if isinstance(case, dict)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path, help="reviewed synthetic JSON fixture")
    args = parser.parse_args()
    try:
        print(json.dumps({"records": evaluate_fixture(args.fixture)}, ensure_ascii=False, indent=2))
    except (ContractError, json.JSONDecodeError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
