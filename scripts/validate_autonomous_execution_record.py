#!/usr/bin/env python3
"""Advisory semantic validator for Autonomous Execution Standard (AES) records.

Scoped advisory semantic validation. This script checks the cross-field semantic
invariants documented in `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 12
("Validation responsibility matrix") that Phase 1's declarative JSON Schema
(`schemas/autonomous_execution_record.schema.json`) deliberately does not
enforce, because JSON Schema alone cannot express cross-field invariants.

Scope and non-goals (see `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 0.1 and
Section 17):

- This script is pure additive, advisory, and read-only. It never mutates an
  execution record.
- It is NOT wired into any CI workflow. It must be run manually or from
  local pytest. Wiring it into `.github/workflows/*` is a deliberately
  separate, not-yet-authorized step (see Section 17: "a blocking CI gate").
- It implements a fixed, documented subset of semantic rules (SEM-001
  through SEM-015 below). It is not a full implementation of every semantic
  case referenced in
  `docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md`.

Default-scan scope (deliberate, documented — not a rule weakening):

- With no `paths` argument, this script scans only the canonical top-level
  illustrative example records directly under
  `docs/autonomous_execution/examples/*.json` (the five Phase 1 examples).
  Every record in that default scope is expected to be fully clean.
- It does NOT recurse into `docs/autonomous_execution/examples/pilot_evidence/`
  by default. Pilot evidence records legitimately encode scenario-specific
  states as their actual subject matter — e.g. the Phase 3 artifact-freshness
  pilot's evidence intentionally records a *stale* mandatory artifact,
  because demonstrating staleness detection is the point of that pilot, not
  a defect in the record. Treating "every pilot_evidence record is clean"
  as a default-scan invariant would be a false assumption, not a stronger
  guarantee.
- The rules themselves (SEM-001 .. SEM-008) are unchanged and still apply in
  full to pilot evidence records — this only changes what gets swept in by
  default when no explicit paths are given. To validate pilot evidence
  explicitly (recommended when reviewing a specific pilot's evidence), pass
  its path(s) directly, e.g.:
      python3 scripts/validate_autonomous_execution_record.py \\
          docs/autonomous_execution/examples/pilot_evidence/*.json
  A caller may still get the historical "everything under examples/,
  recursively" behavior by passing that glob's expansion explicitly; this
  script does not remove that capability, it just no longer assumes it by
  default.

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

DEFAULT_GLOB = "docs/autonomous_execution/examples/*.json"

# Not scanned by default (see module docstring "Default-scan scope"):
# pilot evidence records may legitimately encode scenario-specific states
# (e.g. an intentionally stale artifact) that are the pilot's subject
# matter, not a defect. Validate this glob explicitly when reviewing pilot
# evidence.
PILOT_EVIDENCE_GLOB = "docs/autonomous_execution/examples/pilot_evidence/*.json"

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
# Source: docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md Section 8.2 rules 2, 3, 5;
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


def _closure_aware(record: dict) -> bool:
    """Return whether the record uses a contract that requires Closure Review.

    v1 is frozen historical evidence and continues to be read under the v1
    schema.  Every new v2 record is closure-required, so version selection
    cannot silently create a successful record without final review.
    """
    return record.get("standard_version") == "2.0.0" or record.get("closure_review") is not None


# SEM-009: a successful closure-aware record requires a passed Closure Review
# which rechecked goal and scope, inspected invariants, preserved authority,
# and found no remaining correctable gap.
def check_sem_009(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    if not _closure_aware(record) or record.get("overall_delivery") != "pass":
        return violations
    review = record.get("closure_review")
    if not isinstance(review, dict):
        _add(violations, record_path, "SEM-009", "closure-aware successful record has no closure_review")
        return violations
    if review.get("status") != "pass":
        _add(violations, record_path, "SEM-009", "overall_delivery: pass requires closure_review.status: pass")
    if not review.get("goal_rechecked") or not review.get("scope_rechecked"):
        _add(violations, record_path, "SEM-009", "passed Closure Review must recheck the original goal and agreed scope")
    if not review.get("invariants_checked"):
        _add(violations, record_path, "SEM-009", "passed Closure Review must record an invariant sweep")
    if review.get("remaining_correctable_gaps"):
        _add(violations, record_path, "SEM-009", "passed Closure Review cannot retain correctable gaps")
    if not review.get("authority_boundary_preserved"):
        _add(violations, record_path, "SEM-009", "Closure Review must preserve the external authority boundary")
    return violations


# SEM-010: the effective closure-correction ceiling is at most two and cannot
# be exceeded by recorded closure corrective iterations.
def check_sem_010(record: dict, record_path: str) -> list[Violation]:
    review = record.get("closure_review")
    if not isinstance(review, dict):
        return []
    violations: list[Violation] = []
    limit = review.get("effective_max_closure_corrective_iterations")
    count = review.get("closure_iteration_count")
    if isinstance(limit, int) and limit > 2:
        _add(violations, record_path, "SEM-010", "effective closure corrective limit exceeds canonical ceiling of 2")
    if isinstance(count, int) and isinstance(limit, int) and count > limit:
        _add(violations, record_path, "SEM-010", "closure corrective iteration count exceeds its effective limit")
    return violations


# SEM-011: closure-found defects must be registered and a successful closure
# after correction must cite fresh final validation evidence.
def check_sem_011(record: dict, record_path: str) -> list[Violation]:
    review = record.get("closure_review")
    if not isinstance(review, dict):
        return []
    violations: list[Violation] = []
    defects = {d.get("defect_id"): d for d in record.get("defects", [])}
    for defect_id in review.get("defects_found", []):
        if defect_id not in defects:
            _add(violations, record_path, "SEM-011", f"closure defect {defect_id} is absent from defects register")
    if review.get("status") == "pass" and review.get("closure_iteration_count", 0) > 0:
        final_revision = (record.get("source_revision") or {}).get("final_revision")
        fresh = [v for v in record.get("validation_runs", []) if v.get("result") == "pass" and v.get("freshness_status") == "current" and v.get("validated_revision") == final_revision]
        if not fresh:
            _add(violations, record_path, "SEM-011", "closure correction requires current validation at final source revision")
        for defect_id in review.get("defects_found", []):
            defect = defects.get(defect_id)
            if defect and defect.get("status") != "resolved":
                _add(violations, record_path, "SEM-011", f"closure defect {defect_id} is not resolved before Closure Review pass")
    return violations


# SEM-012: a repeat visit to an owner requires a named evidence delta.
# Source: AES Continuation Control Plane Contract, Section 5.
def check_sem_012(record: dict, record_path: str) -> list[Violation]:
    continuation = record.get("continuation")
    if not isinstance(continuation, dict):
        return []
    violations: list[Violation] = []
    visited_owners: set[str] = set()
    for route in continuation.get("route_trace") or []:
        owner = route.get("to_owner")
        if owner in visited_owners and not route.get("evidence_delta"):
            _add(
                violations,
                record_path,
                "SEM-012",
                f"repeat route to owner '{owner}' has no evidence_delta",
            )
        if isinstance(owner, str):
            visited_owners.add(owner)
    return violations


# SEM-013: progress partitions the original acceptance criteria, and a guard
# stop has the documented terminal reason and a report reference.
# Source: AES Continuation Control Plane Contract, Sections 4, 6, and 8.
def check_sem_013(record: dict, record_path: str) -> list[Violation]:
    continuation = record.get("continuation")
    if not isinstance(continuation, dict):
        return []
    violations: list[Violation] = []
    original = set(continuation.get("original_acceptance_criteria") or [])
    progress = continuation.get("progress")
    if isinstance(progress, dict):
        satisfied = set(progress.get("satisfied_criteria") or [])
        remaining = set(progress.get("remaining_criteria") or [])
        if satisfied & remaining or satisfied | remaining != original:
            _add(
                violations,
                record_path,
                "SEM-013",
                "progress must partition original_acceptance_criteria into satisfied and remaining criteria",
            )
        if record.get("overall_delivery") == "pass" and remaining:
            _add(
                violations,
                record_path,
                "SEM-013",
                "overall_delivery: pass requires no remaining original acceptance criteria",
            )

    guards = continuation.get("guards")
    if not isinstance(guards, dict) or not guards.get("tripped_guard"):
        return violations
    expected_reasons = {
        "hop_budget": "iteration_limit_reached",
        "per_owner_retry_limit": "hard_blocker",
        "no_progress_counter": "continuation_no_progress_limit_reached",
        "route_signature_cycle": "hard_blocker",
    }
    guard = guards["tripped_guard"]
    if record.get("execution_state") != "stopped":
        _add(violations, record_path, "SEM-013", "a tripped continuation guard requires execution_state: stopped")
    if record.get("terminal_reason") != expected_reasons.get(guard):
        _add(violations, record_path, "SEM-013", f"guard '{guard}' requires terminal_reason '{expected_reasons.get(guard)}'")
    if not guards.get("terminal_report_ref"):
        _add(violations, record_path, "SEM-013", "a tripped continuation guard requires terminal_report_ref")
    return violations


# SEM-014: candidate research and hypotheses must not become action-eligible
# after a context transformation, handoff, or resume.
# Source: Section 5.7 and Section 15 (authority provenance persistence).
def check_sem_014(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    containers = []
    continuation = record.get("continuation")
    if isinstance(continuation, dict):
        containers.append(("continuation", continuation.get("authority_provenance")))
    for handoff in record.get("handoffs", []):
        if isinstance(handoff, dict):
            containers.append((handoff.get("handoff_id", "handoff"), handoff.get("authority_provenance")))
    for location, provenance in containers:
        if not isinstance(provenance, dict):
            continue
        for claim in provenance.get("claims", []):
            if (
                isinstance(claim, dict)
                and claim.get("authority_class") in {"candidate_research", "hypothesis_recommendation"}
                and claim.get("action_eligibility") != "not_eligible"
            ):
                _add(
                    violations,
                    record_path,
                    "SEM-014",
                    f"{location} claim '{claim.get('claim_text', '<unknown>')}' is "
                    f"{claim.get('authority_class')} but not action-ineligible",
                )
    return violations


# SEM-015: declared side effects obey preview, authority, commit, and verify.
# Source: Section 13.2 (effect-boundary invariant).
def check_sem_015(record: dict, record_path: str) -> list[Violation]:
    violations: list[Violation] = []
    for action in record.get("external_actions", []):
        if not isinstance(action, dict):
            continue
        boundary = action.get("effect_boundary")
        if not isinstance(boundary, dict):
            continue  # historical records remain readable under their prior contract
        action_id = action.get("action_id", "<unknown>")
        committed = boundary.get("commit_performed")
        if not committed:
            continue
        if not action.get("authority_evidence_ref") or not boundary.get("authority_checked_at"):
            _add(violations, record_path, "SEM-015", f"action {action_id} committed without recorded authority check")
        preview = boundary.get("preview") or {}
        if boundary.get("commit_intent_fingerprint") != preview.get("intent_fingerprint") and not boundary.get("authority_rechecked_after_preview_change"):
            _add(violations, record_path, "SEM-015", f"action {action_id} materially differs from preview without authority recheck")
        if boundary.get("verification_result") != "pass" or not boundary.get("verification_evidence_ref"):
            _add(violations, record_path, "SEM-015", f"action {action_id} committed without passed verification evidence")
        if record.get("overall_delivery") == "pass" and boundary.get("verification_result") != "pass":
            _add(violations, record_path, "SEM-015", f"overall_delivery pass includes unverified committed action {action_id}")
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
    check_sem_009,
    check_sem_010,
    check_sem_011,
    check_sem_012,
    check_sem_013,
    check_sem_014,
    check_sem_015,
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
    "SEM-009": "v2 or closure-aware successful record requires a passed, goal/scope/invariant/authority-preserving Closure Review with no correctable gaps",
    "SEM-010": "closure corrective iterations must not exceed the effective ceiling of two",
    "SEM-011": "closure defects must be registered; successful closure corrections require current final validation",
    "SEM-012": "a repeat route to an owner requires a named evidence_delta",
    "SEM-013": "progress partitions original acceptance criteria; a guard stop has the documented terminal reason and report",
    "SEM-014": "candidate research and hypotheses remain not_eligible across continuation and handoff provenance",
    "SEM-015": "declared side effects require preview, authority check, intent consistency, and passed verification before successful completion",
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


def collect_targets(
    explicit_paths: list[str], root: Path, include_pilot_evidence: bool = False
) -> list[Path]:
    if explicit_paths:
        return [Path(p) for p in explicit_paths]
    targets = sorted(root.glob(DEFAULT_GLOB))
    if include_pilot_evidence:
        targets += sorted(root.glob(PILOT_EVIDENCE_GLOB))
    return targets


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Advisory semantic validator for Autonomous Execution Standard records "
        "(Phase 6, scoped). Read-only; never wired into CI."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="One or more execution-record JSON files. Defaults to the "
        f"canonical top-level examples ({DEFAULT_GLOB}); pilot evidence "
        f"under {PILOT_EVIDENCE_GLOB} is not included by default because it "
        "may legitimately contain scenario-specific states (see "
        "--include-pilot-evidence).",
    )
    parser.add_argument(
        "--include-pilot-evidence",
        action="store_true",
        help="Also scan docs/autonomous_execution/examples/pilot_evidence/*.json "
        "when no explicit paths are given. Off by default: pilot evidence may "
        "legitimately encode scenario-specific states (e.g. an intentionally "
        "stale artifact) that are a pilot's subject matter, not a defect, so "
        "it is not swept into the 'default scan must be clean' expectation. "
        "The SEM rules themselves are unchanged and still apply in full when "
        "this flag is used or when a pilot evidence path is passed explicitly.",
    )
    args = parser.parse_args(argv)

    root = repo_root()
    targets = collect_targets(args.paths, root, include_pilot_evidence=args.include_pilot_evidence)

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
