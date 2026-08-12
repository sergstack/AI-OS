#!/usr/bin/env python3
"""Supervised, transport-neutral live verification for named ChatGPT Projects.

The script never invokes, edits, or synchronizes a Project. A controlled browser or
manual operator performs the actual invocation and supplies a local capture. The
script binds that capture to canonical repository contracts and emits compact
governed evidence without the full response.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Protocol


MVP_PROJECTS = ("[AI OS]", "[LLM]", "[Analytics]")
FINAL_VERDICTS = {"pass", "fail", "blocked", "not_run"}
JUDGE_VERDICTS = {"pass", "fail", "revise", "blocked", "not_run"}
SYNC_STATES = {"SYNC_VERIFIED", "SYNC_PARTIAL", "SYNC_NOT_VERIFIED", "SYNC_STALE"}


class ContractError(ValueError):
    """Raised when canonical or captured evidence violates the verifier contract."""


@dataclass(frozen=True)
class ProjectRef:
    name: str
    path: str


@dataclass(frozen=True)
class TestCase:
    test_id: str
    project: str
    question: str
    expected_result: str
    pass_condition: str
    fail_condition: str
    required_groups: tuple[tuple[str, ...], ...]
    forbidden_phrases: tuple[str, ...]


@dataclass(frozen=True)
class LiveResponse:
    project: str
    test_id: str
    transport_type: str
    started_at: str
    completed_at: str
    response: str
    transport_status: str
    run_reference: str
    response_scope: str = "full response"


@dataclass(frozen=True)
class DeterministicResult:
    result: str
    critical: bool
    findings: tuple[str, ...]


@dataclass(frozen=True)
class JudgeResult:
    judge_surface: str
    judge_verdict: str
    material_findings: tuple[str, ...]
    unsupported_claims: tuple[str, ...]
    routing_defects: tuple[str, ...]
    evidence_defects: tuple[str, ...]
    limitations: tuple[str, ...]


class LiveTransport(Protocol):
    def run(self, project_ref: ProjectRef, test_case: TestCase) -> LiveResponse: ...


def _field(line: str, name: str) -> str | None:
    prefix = f"{name}:"
    return line[len(prefix) :].strip().strip("`") if line.startswith(prefix) else None


def _groups(value: str | None) -> tuple[tuple[str, ...], ...]:
    if not value:
        return ()
    return tuple(
        tuple(option.strip().casefold() for option in group.strip(" `").split("|") if option.strip())
        for group in value.split(";")
        if group.strip(" `")
    )


def _phrases(value: str | None) -> tuple[str, ...]:
    if not value:
        return ()
    return tuple(item.strip(" `").casefold() for item in value.split(";") if item.strip(" `"))


def parse_project_registry(path: Path) -> dict[str, ProjectRef]:
    text = path.read_text(encoding="utf-8")
    projects: dict[str, ProjectRef] = {}
    for name, project_path in re.findall(
        r"^\| `(\[[^`]+\])` \| `(ChatGPT/\[[^`]+\])` \|", text, re.MULTILINE
    ):
        if name in projects:
            raise ContractError(f"duplicate project: {name}")
        projects[name] = ProjectRef(name=name, path=project_path)
    if not projects:
        raise ContractError("no projects found in canonical registry")
    return projects


def parse_smoke_cases(path: Path) -> dict[str, TestCase]:
    cases: dict[str, TestCase] = {}
    current_project: str | None = None
    current: dict[str, str] = {}

    def finish() -> None:
        nonlocal current
        if not current:
            return
        required = ("Test ID", "Question", "Expected result", "Pass condition", "Fail condition")
        missing = [name for name in required if not current.get(name)]
        if missing or current_project is None:
            raise ContractError(f"incomplete smoke case: {', '.join(missing)}")
        test_id = current["Test ID"].strip("`")
        if test_id in cases:
            raise ContractError(f"duplicate Test ID: {test_id}")
        cases[test_id] = TestCase(
            test_id=test_id,
            project=current_project,
            question=current["Question"],
            expected_result=current["Expected result"],
            pass_condition=current["Pass condition"],
            fail_condition=current["Fail condition"],
            required_groups=_groups(current.get("Deterministic required groups")),
            forbidden_phrases=_phrases(current.get("Deterministic forbidden phrases")),
        )
        current = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = re.fullmatch(r"## (\[[^]]+\]) Smoke QA", line)
        if heading:
            finish()
            current_project = heading.group(1)
            continue
        value = _field(line, "Test ID")
        if value is not None:
            finish()
            current = {"Test ID": value}
            continue
        if line.startswith("Question:") and current_project in MVP_PROJECTS and not current:
            raise ContractError(f"missing Test ID for {current_project} smoke case")
        if current:
            for name in (
                "Question",
                "Expected result",
                "Pass condition",
                "Fail condition",
                "Deterministic required groups",
                "Deterministic forbidden phrases",
            ):
                value = _field(line, name)
                if value is not None:
                    current[name] = value
                    break
    finish()
    return cases


def _run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode:
        raise ContractError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()


def _sync_rows(path: Path) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `["):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) >= 18:
            rows[cells[0]] = cells
    return rows


def _parse_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _latest_change_date(root: Path, path: str) -> date | None:
    value = _run_git(root, "log", "-1", "--format=%cs", "--", path)
    return _parse_date(value) if value else None


def _upload_bundle_paths(root: Path, project_ref: ProjectRef) -> tuple[str, ...]:
    rel = f"{project_ref.path}/Knowledge_Bundles/UPLOAD_LIST.md"
    upload = root / rel
    if not upload.exists():
        return ()
    section = upload.read_text(encoding="utf-8").split("## Required upload files", 1)[-1]
    section = section.split("## ", 1)[0]
    names = re.findall(r"^- `([^`]+\.md)`", section, re.MULTILINE)
    return tuple(f"{project_ref.path}/Knowledge_Bundles/{name}" for name in names)


def source_binding(root: Path, project_ref: ProjectRef) -> dict[str, object]:
    paths = [f"{project_ref.path}/PROJECT_INSTRUCTIONS.md", *_upload_bundle_paths(root, project_ref)]
    sources = []
    for rel in paths:
        file_path = root / rel
        if not file_path.is_file():
            raise ContractError(f"missing source binding path: {rel}")
        sources.append({"path": rel, "sha256": hashlib.sha256(file_path.read_bytes()).hexdigest()})
    return {"repo_revision": _run_git(root, "rev-parse", "HEAD"), "sources": sources}


def sync_gate(root: Path, project_ref: ProjectRef, checklist: Path) -> dict[str, object]:
    row = _sync_rows(checklist).get(project_ref.name)
    if row is None:
        return {"state": "SYNC_NOT_VERIFIED", "evidence": "project row missing"}
    instructions_status, instructions_date = row[3], _parse_date(row[4])
    knowledge_status, knowledge_date = row[6], _parse_date(row[7])
    evidence = {
        "checklist": str(checklist.relative_to(root)),
        "instructions_status": instructions_status,
        "instructions_date": row[4],
        "knowledge_status": knowledge_status,
        "knowledge_date": row[7],
    }
    if instructions_status in {"partial", "pending"} or knowledge_status in {"partial", "pending"}:
        return {"state": "SYNC_PARTIAL", "evidence": evidence}
    if instructions_status != "done" or knowledge_status not in {"done", "not_applicable"}:
        return {"state": "SYNC_NOT_VERIFIED", "evidence": evidence}
    if instructions_date is None or (knowledge_status == "done" and knowledge_date is None):
        return {"state": "SYNC_NOT_VERIFIED", "evidence": evidence}
    instruction_source = f"{project_ref.path}/PROJECT_INSTRUCTIONS.md"
    instruction_changed = _latest_change_date(root, instruction_source)
    knowledge_sources = _upload_bundle_paths(root, project_ref)
    knowledge_dates = [
        changed
        for item in knowledge_sources
        if (changed := _latest_change_date(root, item)) is not None
    ]
    knowledge_changed = max(knowledge_dates, default=None)
    evidence["latest_instruction_change"] = str(instruction_changed) if instruction_changed else None
    evidence["latest_knowledge_change"] = str(knowledge_changed) if knowledge_changed else None
    if (instruction_changed and instruction_changed > instructions_date) or (
        knowledge_changed and knowledge_date and knowledge_changed > knowledge_date
    ):
        return {"state": "SYNC_STALE", "evidence": evidence}
    return {"state": "SYNC_VERIFIED", "evidence": evidence}


def plan_impact(root: Path, base: str, head: str) -> dict[str, object]:
    registry = parse_project_registry(root / "PROJECT_REGISTRY.md")
    cases = parse_smoke_cases(root / "SMOKE_QA_REFRESH_PLAN.md")
    changed = [line for line in _run_git(root, "diff", "--name-only", f"{base}..{head}").splitlines() if line]
    affected: set[str] = set()
    rationale: list[str] = []
    unknown: list[str] = []
    shared = {"AUTONOMOUS_EXECUTION_STANDARD.md", "HANDOFF_STYLE_STANDARD.md"}
    for path in changed:
        if path in shared:
            affected.update(MVP_PROJECTS)
            rationale.append(f"{path}: shared governance regression")
            continue
        matched = False
        for project, ref in registry.items():
            if path == ref.path or path.startswith(f"{ref.path}/"):
                matched = True
                if project in MVP_PROJECTS:
                    affected.add(project)
                    rationale.append(f"{path}: {project} contract scope")
                break
        if matched or Path(path).name.casefold().startswith("readme"):
            continue
        if path in {"PROJECT_REGISTRY.md", "SMOKE_QA_REFRESH_PLAN.md", "PILOT_CASES.md", "CHATGPT_PROJECT_SYNC_CHECKLIST.md"}:
            affected.update(MVP_PROJECTS)
            rationale.append(f"{path}: verifier governance regression")
        else:
            unknown.append(path)
    if unknown:
        affected.update(MVP_PROJECTS)
        rationale.append("unknown paths: conservative MVP regression")
    selected = sorted(case.test_id for case in cases.values() if case.project in affected)
    return {
        "base_revision": base,
        "head_revision": head,
        "changed_paths": changed,
        "affected_projects": sorted(affected),
        "selected_tests": selected,
        "mode": "REGRESSION" if affected else "SMOKE",
        "impact_status": "UNKNOWN" if unknown else "KNOWN",
        "unknown_paths": unknown,
        "rationale": rationale or ["README-only or empty diff: live_not_required"],
    }


class CapturedLiveTransport:
    """Thin adapter for an actual response captured by a supervised transport."""

    def __init__(self, capture: dict[str, object]):
        self.capture = capture

    def run(self, project_ref: ProjectRef, test_case: TestCase) -> LiveResponse:
        required = {
            "project",
            "test_id",
            "transport_type",
            "started_at",
            "completed_at",
            "response",
            "transport_status",
            "run_reference",
        }
        missing = sorted(required - self.capture.keys())
        if missing:
            raise ContractError(f"capture missing fields: {', '.join(missing)}")
        response = LiveResponse(
            **{key: str(self.capture[key]) for key in required},
            response_scope=str(self.capture.get("capture_scope", "full response")),
        )
        if response.project != project_ref.name or response.test_id != test_case.test_id:
            raise ContractError("capture identity does not match selected Project/Test ID")
        if response.transport_type not in {"CONTROLLED_BROWSER_TRANSPORT", "MANUAL_ASSISTED_TRANSPORT"}:
            raise ContractError("capture is not from a supported actual-Project transport")
        if not response.run_reference.startswith("https://chatgpt.com/g/g-p-"):
            raise ContractError("capture lacks an actual ChatGPT Project conversation reference")
        return response


def deterministic_evaluate(test_case: TestCase, response: str) -> DeterministicResult:
    text = response.casefold()
    findings: list[str] = []
    for group in test_case.required_groups:
        if not any(option in text for option in group):
            findings.append(f"missing required marker group: {' | '.join(group)}")
    for phrase in test_case.forbidden_phrases:
        if phrase in text:
            findings.append(f"forbidden phrase present: {phrase}")
    if findings:
        return DeterministicResult("fail", True, tuple(findings))
    if not test_case.required_groups and not test_case.forbidden_phrases:
        return DeterministicResult("not_applicable", False, ())
    return DeterministicResult("pass", False, ())


def parse_judge(payload: dict[str, object], target_project: str) -> JudgeResult:
    required = {
        "judge_surface",
        "judge_verdict",
        "material_findings",
        "unsupported_claims",
        "routing_defects",
        "evidence_defects",
        "limitations",
    }
    missing = sorted(required - payload.keys())
    if missing:
        raise ContractError(f"Judge result missing fields: {', '.join(missing)}")
    if payload["judge_surface"] == target_project:
        raise ContractError("target Project cannot act as its own independent Judge")
    if payload["judge_verdict"] not in JUDGE_VERDICTS:
        raise ContractError("invalid Judge verdict")
    list_fields = required - {"judge_surface", "judge_verdict"}
    if any(not isinstance(payload[name], list) for name in list_fields):
        raise ContractError("Judge finding fields must be arrays")
    return JudgeResult(
        judge_surface=str(payload["judge_surface"]),
        judge_verdict=str(payload["judge_verdict"]),
        material_findings=tuple(str(item) for item in payload["material_findings"]),
        unsupported_claims=tuple(str(item) for item in payload["unsupported_claims"]),
        routing_defects=tuple(str(item) for item in payload["routing_defects"]),
        evidence_defects=tuple(str(item) for item in payload["evidence_defects"]),
        limitations=tuple(str(item) for item in payload["limitations"]),
    )


def final_verdict(sync_state: str, live: LiveResponse, deterministic: DeterministicResult, judge: JudgeResult) -> str:
    if sync_state not in SYNC_STATES:
        raise ContractError("invalid sync state")
    if live.transport_status != "completed" or sync_state != "SYNC_VERIFIED":
        return "blocked"
    if deterministic.critical and deterministic.result == "fail":
        return "fail"
    if judge.judge_verdict in {"fail", "revise"}:
        return "fail"
    if judge.judge_verdict in {"blocked", "not_run"}:
        return "blocked"
    return "pass"


def failure_record(
    verdict: str,
    project_ref: ProjectRef,
    test_case: TestCase,
    binding: dict[str, object],
    response_hash: str,
    sync_state: str,
    deterministic: DeterministicResult,
    judge: JudgeResult,
) -> dict[str, object] | None:
    if verdict == "blocked":
        return {
            "classification": "external_dependency",
            "domain_subtype": "sync",
            "status": "blocked",
            "evidence": [sync_state],
            "next_safe_action": "Owner-led Project sync and evidence update, then rerun the selected case.",
        }
    if verdict != "fail":
        return None
    return {
        "classification": "contract",
        "domain_subtype": "live_behavior",
        "status": "open",
        "corrective_handoff": {
            "target": "[Codex]",
            "failed_test_id": test_case.test_id,
            "project": project_ref.name,
            "repo_revision": binding["repo_revision"],
            "expected_behavior": test_case.expected_result,
            "actual_behavior_evidence": {"response_sha256": response_hash},
            "deterministic_findings": list(deterministic.findings),
            "judge_findings": list(judge.material_findings),
            "likely_affected_sources": [item["path"] for item in binding["sources"]],
            "forbidden_actions": [
                "Do not edit live Project configuration inside the verifier.",
                "Do not bypass repository, owner, sync, or merge gates.",
            ],
            "required_rerun": [test_case.test_id, "materially affected sibling cases"],
        },
    }


def governed_record(
    root: Path,
    project_ref: ProjectRef,
    test_case: TestCase,
    live: LiveResponse,
    sync: dict[str, object],
    deterministic: DeterministicResult,
    judge: JudgeResult,
) -> dict[str, object]:
    response_hash = hashlib.sha256(live.response.encode("utf-8")).hexdigest()
    excerpt = " ".join(live.response.split())[:280]
    verdict = final_verdict(str(sync["state"]), live, deterministic, judge)
    binding = source_binding(root, project_ref)
    record = {
        "schema_version": "live-project-verifier-v1",
        "run_id": f"LPV-{test_case.test_id}-{response_hash[:12]}",
        "test_id": test_case.test_id,
        "project": project_ref.name,
        "source_binding": binding,
        "sync_state": sync["state"],
        "sync_evidence": sync["evidence"],
        "transport": {
            "type": live.transport_type,
            "status": live.transport_status,
            "started_at": live.started_at,
            "completed_at": live.completed_at,
            "run_reference": live.run_reference,
        },
        "response_sha256": response_hash,
        "response_hash_scope": live.response_scope,
        "bounded_excerpt": excerpt,
        "deterministic_result": asdict(deterministic),
        "judge_result": asdict(judge),
        "final_verdict": verdict,
        "limitations": [
            "Full runtime response remains local and is not part of this governed record.",
            "Exact transport start/completion timestamps may be not_observed when the UI does not expose them.",
        ],
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    failure = failure_record(
        verdict,
        project_ref,
        test_case,
        binding,
        response_hash,
        str(sync["state"]),
        deterministic,
        judge,
    )
    if failure is not None:
        record["failure"] = failure
    validate_record(record)
    return record


def validate_record(record: dict[str, object]) -> None:
    required = {
        "schema_version",
        "run_id",
        "test_id",
        "project",
        "source_binding",
        "sync_state",
        "sync_evidence",
        "transport",
        "response_sha256",
        "response_hash_scope",
        "bounded_excerpt",
        "deterministic_result",
        "judge_result",
        "final_verdict",
        "limitations",
        "recorded_at",
    }
    missing = sorted(required - record.keys())
    if missing:
        raise ContractError(f"run record missing fields: {', '.join(missing)}")
    if record["final_verdict"] not in FINAL_VERDICTS:
        raise ContractError("invalid final verdict")
    if record["sync_state"] not in SYNC_STATES:
        raise ContractError("invalid sync state")
    if "response" in record:
        raise ContractError("runtime response must not be stored in governed record")
    excerpt = record["bounded_excerpt"]
    if not isinstance(excerpt, str) or len(excerpt) > 280:
        raise ContractError("bounded excerpt exceeds 280 characters")
    deterministic = record["deterministic_result"]
    if not isinstance(deterministic, dict):
        raise ContractError("invalid deterministic result")
    if deterministic.get("critical") and deterministic.get("result") == "fail" and record["final_verdict"] == "pass":
        raise ContractError("critical deterministic fail cannot be promoted to pass")


def _root(value: str) -> Path:
    return Path(value).resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    commands = parser.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan")
    plan.add_argument("--base", required=True)
    plan.add_argument("--head", required=True)
    contract = commands.add_parser("contract")
    contract.add_argument("--project", required=True)
    contract.add_argument("--test-id", required=True)
    sync = commands.add_parser("sync")
    sync.add_argument("--project", required=True)
    evaluate = commands.add_parser("evaluate")
    evaluate.add_argument("--project", required=True)
    evaluate.add_argument("--test-id", required=True)
    evaluate.add_argument("--capture", type=Path, required=True)
    evaluate.add_argument("--judge", type=Path, required=True)
    validate = commands.add_parser("validate-record")
    validate.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    root = _root(args.root)
    registry = parse_project_registry(root / "PROJECT_REGISTRY.md")
    cases = parse_smoke_cases(root / "SMOKE_QA_REFRESH_PLAN.md")
    try:
        if args.command == "plan":
            output = plan_impact(root, args.base, args.head)
        elif args.command == "validate-record":
            output = json.loads(args.record.read_text(encoding="utf-8"))
            validate_record(output)
            output = {"status": "pass", "record": str(args.record)}
        else:
            if args.project not in MVP_PROJECTS or args.project not in registry:
                raise ContractError("project is outside Live Project Verifier v1 scope")
            project_ref = registry[args.project]
            if args.command == "sync":
                output = sync_gate(root, project_ref, root / "CHATGPT_PROJECT_SYNC_CHECKLIST.md")
            else:
                test_case = cases.get(args.test_id)
                if test_case is None:
                    raise ContractError(f"unknown Test ID: {args.test_id}")
                if test_case.project != args.project:
                    raise ContractError("Test ID does not belong to selected Project")
                if args.command == "contract":
                    output = asdict(test_case)
                else:
                    capture = json.loads(args.capture.read_text(encoding="utf-8"))
                    live = CapturedLiveTransport(capture).run(project_ref, test_case)
                    judge_payload = json.loads(args.judge.read_text(encoding="utf-8"))
                    judge_result = parse_judge(judge_payload, args.project)
                    sync_result = sync_gate(root, project_ref, root / "CHATGPT_PROJECT_SYNC_CHECKLIST.md")
                    deterministic = deterministic_evaluate(test_case, live.response)
                    output = governed_record(
                        root, project_ref, test_case, live, sync_result, deterministic, judge_result
                    )
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (ContractError, OSError, json.JSONDecodeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
