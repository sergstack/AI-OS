#!/usr/bin/env python3
"""Advisory semantic validator for Autonomous Execution Standard (AES) records.

Phase 6 (scoped, advisory only). This script checks the cross-field semantic
invariants documented in `AUTONOMOUS_EXECUTION_STANDARD.md` Section 12
("Validation responsibility matrix") that Phase 1's declarative JSON Schema
(`schemas/autonomous_execution_record.schema.json`) deliberately does not
enforce, because JSON Schema alone cannot express cross-field invariants.

Scope and non-goals (see `AUTONOMOUS_EXECUTION_STANDARD.md` Section 0.1 and
Section 17):

- This script is pure additive, advisory, and read-only. It never mutates an
  execution record.
- It is NOT wired into any CI workflow. It must be run manually or from
  local pytest. Wiring it into `.github/workflows/*` is a deliberately
  separate, not-yet-authorized step (see Section 17: "a blocking CI gate").
- It implements a fixed, documented subset of semantic rules (SEM-001
  through SEM-008 below). It is not a full implementation of every semantic
  case referenced in
  `docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md`.

Exit code: 0 when every scanned record has zero violations, 1 otherwise (or
when a record cannot be parsed as JSON).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_GLOB = "docs/autonomous_execution/examples/**/*.json"

EXEC_ID_PATTERN = re.compile(r"^exec-[a-z0-9][a-z0-9-]*$")

# Requirement statuses that are acceptable as the *final* status of a
# mandatory requirement when overall_delivery: pass (Section 8.2, rule 2).
TERMINAL_OK_STATUSES = {"passed", "blocked", "not_applicable"}
REASONED_STATUSES = {"blocked", "not_applicable"}

OPEN_DEFECT_STATUSES = {"open", "correcting"}
BLOCKING_DEFECT_SEVERITIES = {"recoverable", "needs_check"}


@dataclass
class Violation:
    record_path: str
    rule_id: str
    message: str


@dataclass
class RecordReport:
    record_path: str
    violations: list[Violation] = field(default_factory=list)
    parse_error: str | None = None


def _add(violations: list[Violation], record_path: str, rule_id: str, message: str) -> None:
    violations.append(Violation(record_path=record_path, rule_id=rule_id, message=message))


# ---------------------------------------------------------------------------
# SEM-001: overall_delivery: pass requires every mandatory requirement to be
# passed, or blocked/not_applicable with a stated reason. A mandatory
# requirement left at any other status (including failed) forbids
# overall_delivery: pass.
# Source: AUTONOMOUS_EXECUTION_STANDARD.md Section 8.2 rules 2, 3, 5;
# Section 10.2.
# ---------------------------------------------------------------------------
def check_sem_001(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    if record.get("overall_delivery") != "pass":
        return violations
    for req in record.get("requirements", []):
        if not req.get("mandatory"):
            continue
        status = req.get("status")
        req_id = req.get("requirement_id", "<unknown>")
        if status == "failed":
            _add(
                violations,
                record_path,
                "SEM-001",
                f"mandatory requirement {req_id} has status 'failed' while overall_delivery is 'pass'",
            )
            continue
        if status not in TERMINAL_OK_STATUSES:
            _add(
                violations,
                record_path,
                "SEM-001",
                f"mandatory requirement {req_id} has non-terminal status '{status}' while "
                "overall_delivery is 'pass' (expected passed/blocked/not_applicable)",
            )
            continue
        if status in REASONED_STATUSES and not (req.get("gap") or "").strip():
            _add(
                violations,
                record_path,
                "SEM-001",
                f"mandatory requirement {req_id} has status '{status}' but no reason recorded "
                "in 'gap'",
            )
    return violations


# ---------------------------------------------------------------------------
# SEM-002: overall_delivery: pass must not coexist with an open (open or
# correcting) defect of severity recoverable or needs_check.
# Source: Section 10.2 ("no open recoverable or needs_check defects remain").
# ---------------------------------------------------------------------------
def check_sem_002(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    if record.get("overall_delivery") != "pass":
        return violations
    for defect in record.get("defects", []):
        if (
            defect.get("status") in OPEN_DEFECT_STATUSES
            and defect.get("severity") in BLOCKING_DEFECT_SEVERITIES
        ):
            _add(
                violations,
                record_path,
                "SEM-002",
                f"defect {defect.get('defect_id', '<unknown>')} is '{defect.get('status')}' with "
                f"severity '{defect.get('severity')}' while overall_delivery is 'pass'",
            )
    return violations


# ---------------------------------------------------------------------------
# SEM-003: no duplicate IDs within a record, checked independently per
# namespace (requirement_id, defect_id, iteration_id, artifact_id).
# Source: Section 12 table ("Duplicate IDs by property").
# ---------------------------------------------------------------------------
def check_sem_003(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    namespaces = [
        ("requirements", "requirement_id"),
        ("defects", "defect_id"),
        ("iterations", "iteration_id"),
        ("artifacts", "artifact_id"),
    ]
    for list_key, id_key in namespaces:
        seen: dict[str, int] = {}
        for item in record.get(list_key, []):
            item_id = item.get(id_key)
            if item_id is None:
                continue
            seen[item_id] = seen.get(item_id, 0) + 1
        for item_id, count in seen.items():
            if count > 1:
                _add(
                    violations,
                    record_path,
                    "SEM-003",
                    f"duplicate {id_key} '{item_id}' appears {count} times in '{list_key}'",
                )
    return violations


# ---------------------------------------------------------------------------
# SEM-004: a resolved defect must have non-empty resolution_evidence_refs.
# Source: Section 9.5 ("must not... close a defect without resolution
# evidence").
# ---------------------------------------------------------------------------
def check_sem_004(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    for defect in record.get("defects", []):
        if defect.get("status") == "resolved" and not defect.get("resolution_evidence_refs"):
            _add(
                violations,
                record_path,
                "SEM-004",
                f"defect {defect.get('defect_id', '<unknown>')} is 'resolved' but "
                "resolution_evidence_refs is empty",
            )
    return violations


# ---------------------------------------------------------------------------
# SEM-005: a mandatory artifact with freshness_status: stale must not
# coexist with overall_delivery: pass.
# Source: Section 11.3 ("overall_delivery: pass is forbidden while a
# mandatory artifact is stale").
# ---------------------------------------------------------------------------
def check_sem_005(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    if record.get("overall_delivery") != "pass":
        return violations
    for artifact in record.get("artifacts", []):
        if artifact.get("mandatory") and artifact.get("freshness_status") == "stale":
            _add(
                violations,
                record_path,
                "SEM-005",
                f"mandatory artifact {artifact.get('artifact_id', '<unknown>')} "
                f"({artifact.get('path', '<unknown path>')}) is 'stale' while overall_delivery "
                "is 'pass'",
            )
    return violations


# ---------------------------------------------------------------------------
# SEM-006: a validation run whose freshness_status is stale must not be the
# sole evidence backing a passed requirement when overall_delivery: pass.
# Source: Section 11.2 ("A check run before the last relevant change is
# stale") read together with Section 10.2.
#
# Backing runs for a requirement are resolved from requirement.validation_refs
# first; if that list is empty, we fall back to validation_runs whose
# covered_requirement_ids include the requirement. If every backing run found
# is stale, the requirement's 'passed' status has no current evidence.
# ---------------------------------------------------------------------------
def check_sem_006(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    if record.get("overall_delivery") != "pass":
        return violations
    validation_runs = {v.get("validation_id"): v for v in record.get("validation_runs", [])}
    for req in record.get("requirements", []):
        if req.get("status") != "passed":
            continue
        req_id = req.get("requirement_id", "<unknown>")
        backing_ids = list(req.get("validation_refs") or [])
        if not backing_ids:
            backing_ids = [
                v.get("validation_id")
                for v in record.get("validation_runs", [])
                if req_id in (v.get("covered_requirement_ids") or [])
            ]
        backing_runs = [validation_runs[bid] for bid in backing_ids if bid in validation_runs]
        if not backing_runs:
            continue
        if all(run.get("freshness_status") == "stale" for run in backing_runs):
            _add(
                violations,
                record_path,
                "SEM-006",
                f"requirement {req_id} is 'passed' but its only backing validation run(s) "
                f"({', '.join(sorted(backing_ids))}) are all 'stale'",
            )
    return violations


# ---------------------------------------------------------------------------
# SEM-007: parent_execution_id, if non-null, must be a structurally
# plausible exec- id (same shape as execution_id). This is a structural
# sanity check, not a live cross-record lookup.
# Source: Section 5.2, Section 5.3 (ID format).
# ---------------------------------------------------------------------------
def check_sem_007(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    parent_id = record.get("parent_execution_id")
    if parent_id is None:
        return violations
    if not isinstance(parent_id, str) or not EXEC_ID_PATTERN.match(parent_id):
        _add(
            violations,
            record_path,
            "SEM-007",
            f"parent_execution_id '{parent_id}' does not match the expected exec- id format",
        )
        return violations
    execution_id = record.get("execution_id")
    if isinstance(execution_id, str) and parent_id == execution_id:
        _add(
            violations,
            record_path,
            "SEM-007",
            f"parent_execution_id '{parent_id}' is identical to this record's own execution_id",
        )
    return violations


# ---------------------------------------------------------------------------
# SEM-008: iteration count sanity vs a stated max_full_iterations envelope,
# when present in the record (schema does not define a top-level
# max_full_iterations field, so this is looked up under project_extension
# and final_report, the two schema locations that allow free-form
# additional properties).
# Source: Section 9.6 (canonical envelope, max_full_iterations: 5, "a
# ceiling, not a standing permission").
# ---------------------------------------------------------------------------
def _find_max_full_iterations(record: dict) -> int | None:
    for container_key in ("project_extension", "final_report"):
        container = record.get(container_key)
        if isinstance(container, dict) and "max_full_iterations" in container:
            value = container["max_full_iterations"]
            if isinstance(value, int):
                return value
    return None


def check_sem_008(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    limit = _find_max_full_iterations(record)
    if limit is None:
        return violations
    full_iterations = [
        it for it in record.get("iterations", []) if it.get("iteration_type") == "full_iteration"
    ]
    count = len(full_iterations)
    if count > limit:
        _add(
            violations,
            record_path,
            "SEM-008",
            f"record has {count} full_iteration entries, exceeding the stated "
            f"max_full_iterations envelope of {limit}",
        )
    max_number = max((it.get("iteration_number", 0) for it in full_iterations), default=0)
    if max_number > limit:
        _add(
            violations,
            record_path,
            "SEM-008",
            f"highest full_iteration iteration_number is {max_number}, exceeding the stated "
            f"max_full_iterations envelope of {limit}",
        )
    return violations


ALL_CHECKS = [
    check_sem_001,
    check_sem_002,
    check_sem_003,
    check_sem_004,
    check_sem_005,
    check_sem_006,
    check_sem_007,
    check_sem_008,
]

RULE_DESCRIPTIONS = {
    "SEM-001": "overall_delivery: pass requires every mandatory requirement to be "
    "passed/blocked(reason)/not_applicable(reason); failed forbids pass",
    "SEM-002": "overall_delivery: pass forbids an open/correcting defect of severity "
    "recoverable or needs_check",
    "SEM-003": "requirement_id/defect_id/iteration_id/artifact_id must be unique within "
    "their own list",
    "SEM-004": "a resolved defect must carry non-empty resolution_evidence_refs",
    "SEM-005": "overall_delivery: pass forbids a mandatory artifact with freshness_status: stale",
    "SEM-006": "overall_delivery: pass forbids a passed requirement whose only backing "
    "validation run(s) are stale",
    "SEM-007": "parent_execution_id, if present, must be a structurally plausible exec- id "
    "and not equal to this record's own execution_id",
    "SEM-008": "full_iteration count/iteration_number must not exceed a stated "
    "max_full_iterations envelope, when present",
}


def validate_record(data: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    for check in ALL_CHECKS:
        violations.extend(check(data, record_path))
    return violations


def load_and_validate(path: Path, root: Path) -> RecordReport:
    try:
        display_path = str(path.relative_to(root))
    except ValueError:
        display_path = str(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return RecordReport(record_path=display_path, parse_error=f"could not read file: {exc}")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return RecordReport(record_path=display_path, parse_error=f"invalid JSON: {exc}")
    if not isinstance(data, dict):
        return RecordReport(
            record_path=display_path, parse_error="top-level JSON value must be an object"
        )
    return RecordReport(record_path=display_path, violations=validate_record(data, display_path))


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def collect_targets(explicit_paths: list[str], root: Path) -> list[Path]:
    if explicit_paths:
        return [Path(p) for p in explicit_paths]
    return sorted(root.glob(DEFAULT_GLOB))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Advisory semantic validator for Autonomous Execution Standard records "
        "(Phase 6, scoped). Read-only; never wired into CI."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="One or more execution-record JSON files. Defaults to "
        f"{DEFAULT_GLOB} relative to the repository root.",
    )
    args = parser.parse_args(argv)

    root = repo_root()
    targets = collect_targets(args.paths, root)

    if not targets:
        print(f"No execution records found (looked for {DEFAULT_GLOB}).")
        return 0

    reports = [load_and_validate(path, root) for path in targets]

    total_violations = 0
    total_parse_errors = 0
    for report in reports:
        if report.parse_error:
            total_parse_errors += 1
            print(f"ERROR {report.record_path}: {report.parse_error}")
            continue
        if not report.violations:
            print(f"PASS  {report.record_path}: 0 violations")
            continue
        print(f"FAIL  {report.record_path}: {len(report.violations)} violation(s)")
        for violation in report.violations:
            print(f"  - [{violation.rule_id}] {violation.message}")
        total_violations += len(report.violations)

    print()
    print("Summary:")
    print(f"- records scanned: {len(reports)}")
    print(f"- records clean: {sum(1 for r in reports if not r.parse_error and not r.violations)}")
    print(f"- records with violations: {sum(1 for r in reports if r.violations)}")
    print(f"- records with parse errors: {total_parse_errors}")
    print(f"- total violations: {total_violations}")

    return 1 if (total_violations or total_parse_errors) else 0


if __name__ == "__main__":
    sys.exit(main())
