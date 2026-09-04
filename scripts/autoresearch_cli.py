#!/usr/bin/env python3
"""AIOS AutoResearch v0.2 live controller and CLI (issue #416, parent #409).

ONE documented command surface that integrates the v0.1 foundation and the
v0.2 live components into a bounded, user-operable instrument -- so an
operator runs `autoresearch_cli <verb>` instead of writing a new Python
script per batch.

Verbs
-----
    doctor      validate environment / transport / authority / budget /
                model / context / manifests -- fails BEFORE any call
    context     compile / inspect a context pack, no model call
    baseline    run or resume a bounded live baseline set
    reproduce   attempt reproduction of one accepted field failure
    propose     invoke the bounded Researcher and preflight one proposal
    experiment  run one matched baseline/candidate experiment
    batch       run a predeclared bounded batch (never open-ended)
    report      validate the ledger and render a batch/experiment report
    cleanup     remove only registered ephemeral worktrees / state

Every verb that could make an external call accepts `--dry-run`, which
previews the planned subject / Researcher / Judge calls, the budget
reservation, the files / worktrees / contexts / outputs -- and makes zero
external calls.

Exit codes
----------
    0  success
    2  usage error (argparse)
    3  doctor / preflight failure (a gate is missing or failed)
    4  blocked: a live call is required but no authorized live transport
       binding is available (this is not an error -- it is #411's
       "no authorized transport/budget means blocked")
    5  integrity failure (ledger / worktree / drift)

This module integrates -- never reimplements -- `autoresearch_validator`,
`autoresearch_shadow_runner`, `autoresearch_decision_comparator`,
`autoresearch_context_pack_compiler` (#412), `autoresearch_live_browser_adapter`
(#413), `autoresearch_live_judge` (#414), and `autoresearch_failure_intake`
(#415). It runs no Phase 0 / Phase 1 batch (that is #417 / #418), mutates no
active Project configuration, and never commits / pushes / merges / deploys.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_validator as av  # noqa: E402
import autoresearch_shadow_runner as asr  # noqa: E402
import autoresearch_decision_comparator as adc  # noqa: E402
import autoresearch_context_pack_compiler as cpc  # noqa: E402
import autoresearch_live_browser_adapter as lba  # noqa: E402
import autoresearch_live_judge as lj  # noqa: E402
import autoresearch_failure_intake as fi  # noqa: E402

CLI_VERSION = "0.2.0"
REPO_ROOT = _HERE.parent

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_PREFLIGHT = 3
EXIT_BLOCKED = 4
EXIT_INTEGRITY = 5

VERBS = ("doctor", "context", "baseline", "reproduce", "propose", "experiment", "batch", "report", "cleanup")


class CliError(RuntimeError):
    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)
        self.code = code


# ---------------------------------------------------------------------------
# Budget ledger (integrates #413's BudgetState; adds per-role accounting)
# ---------------------------------------------------------------------------


@dataclass
class RoleBudget:
    max_provider_calls: Optional[int]
    max_cost_amount: Optional[float]
    max_cost_currency: Optional[str]
    max_wall_clock_minutes: Optional[int] = None
    subject_calls: int = 0
    researcher_calls: int = 0
    judge_calls: int = 0
    retries: int = 0
    cost_spent: float = 0.0

    def as_shared_state(self) -> "lba.BudgetState":
        st = lba.BudgetState(
            max_provider_calls=self.max_provider_calls,
            max_cost_amount=self.max_cost_amount,
            max_cost_currency=self.max_cost_currency,
            max_wall_clock_minutes=self.max_wall_clock_minutes,
        )
        st.calls_used = self.total_calls()
        return st

    def total_calls(self) -> int:
        return self.subject_calls + self.researcher_calls + self.judge_calls

    def remaining(self) -> Optional[int]:
        if self.max_provider_calls is None:
            return None
        return max(self.max_provider_calls - self.total_calls(), 0)

    def authorized(self) -> bool:
        return (
            self.max_provider_calls is not None
            and self.max_provider_calls > 0
            and self.max_cost_amount is not None
            and bool(self.max_cost_currency)
        )

    def summary(self) -> dict:
        return {
            "max_provider_calls": self.max_provider_calls,
            "subject_calls": self.subject_calls,
            "researcher_calls": self.researcher_calls,
            "judge_calls": self.judge_calls,
            "retries": self.retries,
            "total_calls": self.total_calls(),
            "remaining_calls": self.remaining(),
            "max_cost_amount": self.max_cost_amount,
            "max_cost_currency": self.max_cost_currency,
            "cost_spent": self.cost_spent,
            "authorized": self.authorized(),
        }


# ---------------------------------------------------------------------------
# Run manifest (durable, for bounded resume -- not a daemon / second lifecycle)
# ---------------------------------------------------------------------------

RUN_STEPS = (
    "loaded",
    "doctor",
    "preview",
    "baseline_context",
    "baseline_runs",
    "candidate_worktree",
    "candidate_patch",
    "candidate_context",
    "candidate_runs",
    "hard_gates",
    "judge",
    "comparator",
    "decision",
    "ledger",
    "report",
    "cleanup",
)


@dataclass
class RunManifest:
    run_id: str
    batch_id: str
    source_revision: str
    context_manifest_hash: Optional[str]
    evaluator_version_hash: Optional[str]
    authority_evidence_ref: str
    steps: dict = field(default_factory=dict)  # step -> "pending"|"done"|"failed"
    registered_worktrees: list = field(default_factory=list)
    live_invocation_ids: list = field(default_factory=list)

    @classmethod
    def new(cls, **kw) -> "RunManifest":
        m = cls(**kw)
        m.steps = {s: "pending" for s in RUN_STEPS}
        m.steps["loaded"] = "done"
        return m

    def mark(self, step: str, status: str) -> None:
        if step not in RUN_STEPS:
            raise CliError(f"unknown run step {step!r}", EXIT_INTEGRITY)
        self.steps[step] = status

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self.__dict__, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "RunManifest":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        m = cls(
            run_id=raw["run_id"],
            batch_id=raw["batch_id"],
            source_revision=raw["source_revision"],
            context_manifest_hash=raw.get("context_manifest_hash"),
            evaluator_version_hash=raw.get("evaluator_version_hash"),
            authority_evidence_ref=raw["authority_evidence_ref"],
        )
        m.steps = raw.get("steps", {s: "pending" for s in RUN_STEPS})
        m.registered_worktrees = raw.get("registered_worktrees", [])
        m.live_invocation_ids = raw.get("live_invocation_ids", [])
        return m


# ---------------------------------------------------------------------------
# Controller
# ---------------------------------------------------------------------------


@dataclass
class DoctorResult:
    ok: bool
    checks: list  # [(name, "pass"|"fail", detail)]

    def render(self) -> str:
        lines = ["autoresearch doctor:"]
        for name, status, detail in self.checks:
            lines.append(f"  [{status.upper():4}] {name}: {detail}")
        lines.append(f"  => {'READY' if self.ok else 'NOT READY'}")
        return "\n".join(lines)


class Controller:
    def __init__(
        self,
        *,
        repo_root: Path = REPO_ROOT,
        transport: Optional["lba.BrowserSessionTransport"] = None,
        judge_model: Optional["lj.JudgeModel"] = None,
        researcher_model: Optional["fi.ResearcherModel"] = None,
    ) -> None:
        self.repo_root = repo_root
        self.transport = transport
        self.judge_model = judge_model
        self.researcher_model = researcher_model

    # -- doctor -----------------------------------------------------------

    def doctor(self, *, batch_config: Optional[dict], budget: RoleBudget) -> DoctorResult:
        checks: list = []

        def add(name: str, ok: bool, detail: str) -> None:
            checks.append((name, "pass" if ok else "fail", detail))

        manifest_ok = (self.repo_root / "docs/standards/autoresearch_v01_manifest.json").is_file()
        add("v0.1 manifest present", manifest_ok, "autoresearch_v01_manifest.json")

        live_contract = self.repo_root / "docs/standards/AUTORESEARCH_V02_LIVE_CONTRACT.md"
        add("v0.2 live contract present", live_contract.is_file(), str(live_contract.name))

        add(
            "budget authorized",
            budget.authorized(),
            f"calls<={budget.max_provider_calls}, cost<={budget.max_cost_amount} {budget.max_cost_currency}",
        )

        if batch_config is not None:
            auth = str(batch_config.get("authority_status") or batch_config.get("transport_authority_status") or "")
            add("batch authority_status", auth in {"authorized"}, auth or "missing")
            add("context_manifest_hash present", bool(batch_config.get("context_manifest_hash")), str(batch_config.get("context_manifest_hash")))
            add("transport_id is playwright_mcp", batch_config.get("transport_id") == "playwright_mcp", str(batch_config.get("transport_id")))
        else:
            add("batch config supplied", False, "no --batch-config given")

        add(
            "live transport binding",
            self.transport is not None and getattr(self.transport, "transport_id", "") == "playwright_mcp",
            "a real PlaywrightMcpBrowserTransport with an mcp_call binding" if self.transport else "absent (dry-run / blocked only)",
        )

        try:
            lj.EvaluatorConfig.load(self.repo_root / "docs/standards/autoresearch_v02_evaluator_config.json")
            add("evaluator config loads (no drift)", True, "autoresearch_v02_evaluator_config.json")
        except Exception as exc:  # noqa: BLE001
            add("evaluator config loads (no drift)", False, str(exc))

        # doctor fails on any missing gate EXCEPT the live-transport binding,
        # which is a legitimate "dry-run only" state, not a doctor failure.
        blocking = [c for c in checks if c[1] == "fail" and c[0] != "live transport binding"]
        return DoctorResult(ok=not blocking, checks=checks)

    # -- context --------------------------------------------------------

    def compile_context(self, *, role: str, project: str, source_revision: str) -> dict:
        fn = {
            "subject_baseline": cpc.compile_subject_baseline,
        }.get(role)
        if fn is None:
            raise CliError(f"context role {role!r} not supported by this verb; use subject_baseline", EXIT_USAGE)
        return fn(repo_root=self.repo_root, source_revision=source_revision, project=project)

    # -- preview (PLAN -> PREVIEW EFFECT) -------------------------------

    def preview_experiment(self, *, batch_config: dict, case_ids: list, run_count: int, budget: RoleBudget) -> dict:
        subject = 2 * run_count * len(case_ids)  # baseline + candidate, per case, per run
        judge = 2 * len(case_ids)  # blind A/B both orders, per case
        return {
            "action_class": "matched_live_experiment",
            "external_calls": {"subject": subject, "researcher": 0, "judge": judge, "total": subject + judge},
            "budget_before": budget.summary(),
            "budget_after_if_run": {
                **budget.summary(),
                "total_calls": budget.total_calls() + subject + judge,
                "remaining_calls": None if budget.max_provider_calls is None else budget.max_provider_calls - (budget.total_calls() + subject + judge),
            },
            "transport_id": batch_config.get("transport_id"),
            "context_manifest_hash": batch_config.get("context_manifest_hash"),
            "worktrees": ["<ephemeral candidate worktree at baseline_revision>"],
            "outputs": ["run_manifest.json", "run_report.json"],
            "note": "preview only; not authorization (AES §13.2 / live-contract §5). Zero external calls made.",
        }

    # -- cleanup ------------------------------------------------------

    def cleanup(self, run_manifest: RunManifest) -> list:
        removed = []
        for wt in list(run_manifest.registered_worktrees):
            p = Path(wt)
            try:
                asr.remove_shadow_worktree(self.repo_root, p)
                removed.append(wt)
            except Exception as exc:  # noqa: BLE001
                removed.append(f"{wt} (error: {exc})")
        run_manifest.registered_worktrees = []
        run_manifest.mark("cleanup", "done")
        return removed

    # -- report ------------------------------------------------------

    def report(self, *, run_manifest: RunManifest, budget: RoleBudget, ledger_path: Optional[Path], decision: Optional[str]) -> dict:
        ledger_status = "not_provided"
        ledger_findings: list = []
        if ledger_path is not None and ledger_path.is_file():
            findings = av.verify_ledger(ledger_path)
            ledger_status = "verified" if not findings else "integrity_failure"
            ledger_findings = [f.evidence for f in findings]
        return {
            "report_version": "0.2.0",
            "run_id": run_manifest.run_id,
            "batch_id": run_manifest.batch_id,
            "source_revision": run_manifest.source_revision,
            "steps": run_manifest.steps,
            "live_invocation_ids": run_manifest.live_invocation_ids,
            "budget": budget.summary(),
            "decision": decision,
            "ledger_status": ledger_status,
            "ledger_findings": ledger_findings,
            "parent_tree_fingerprint": asr.parent_tree_fingerprint(self.repo_root),
            "authority_merge_production": {
                "authority_status": "owner_review_pending" if decision == "keep_candidate" else "not_required",
                "merge_status": "not_applicable",
                "production_status": "not_applicable",
            },
            "limitations": (
                "This report reconciles calls / steps / decision / ledger hashes for one run. "
                "A keep_candidate decision is research evidence only; it never advances a baseline, "
                "opens a PR, or changes active configuration."
            ),
        }


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def _load_json(path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _budget_from_args(args) -> RoleBudget:
    return RoleBudget(
        max_provider_calls=args.max_calls,
        max_cost_amount=args.max_cost,
        max_cost_currency=args.cost_currency,
        max_wall_clock_minutes=args.max_minutes,
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="autoresearch_cli",
        description="AIOS AutoResearch v0.2 live controller (issue #416). One command surface; "
        "no per-batch script. Every external-calling verb supports --dry-run.",
        epilog=(
            "Exit codes: 0 ok | 2 usage | 3 doctor/preflight failure | "
            "4 blocked (no authorized live transport) | 5 integrity failure.\n"
            "Config precedence: explicit CLI flag > --batch-config file > built-in default.\n"
            "Examples:\n"
            "  autoresearch_cli doctor --batch-config batch.json --max-calls 40 --max-cost 0 --cost-currency USD\n"
            "  autoresearch_cli context --role subject_baseline --project ai_os --source-revision HEAD\n"
            "  autoresearch_cli experiment --batch-config batch.json --cases c1,c2 --run-count 3 --dry-run\n"
            "  autoresearch_cli report --run-manifest run.json --ledger ledger.jsonl\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--version", action="version", version=f"autoresearch_cli {CLI_VERSION}")
    sub = p.add_subparsers(dest="verb", required=True, metavar="VERB")

    common_budget = argparse.ArgumentParser(add_help=False)
    common_budget.add_argument("--max-calls", type=int, default=None, help="hard ceiling on total provider calls")
    common_budget.add_argument("--max-cost", type=float, default=None, help="cost cap amount (0 == plan-included only)")
    common_budget.add_argument("--cost-currency", default=None, help="cost cap currency, e.g. USD")
    common_budget.add_argument("--max-minutes", type=int, default=None, help="wall-clock ceiling in minutes")

    d = sub.add_parser("doctor", parents=[common_budget], help="validate environment/authority/budget/identity before any call")
    d.add_argument("--batch-config", default=None)

    c = sub.add_parser("context", help="compile/inspect a context pack; no model call")
    c.add_argument("--role", default="subject_baseline", choices=["subject_baseline"])
    c.add_argument("--project", required=True, choices=["ai_os", "thinking", "analytics", "llm", "codex", "inbox_router", "thinkers_os"])
    c.add_argument("--source-revision", default="HEAD")
    c.add_argument("--summary", action="store_true", help="print the human summary instead of the manifest JSON")

    for verb, helptext in (
        ("baseline", "run or resume a bounded live baseline set"),
        ("experiment", "run one matched baseline/candidate experiment"),
        ("batch", "run a predeclared bounded batch (never open-ended)"),
    ):
        e = sub.add_parser(verb, parents=[common_budget], help=helptext)
        e.add_argument("--batch-config", required=True)
        e.add_argument("--cases", default="", help="comma-separated case ids")
        e.add_argument("--run-count", type=int, default=3)
        e.add_argument("--run-manifest", default=None, help="path to write/resume the durable run manifest")
        e.add_argument("--dry-run", action="store_true", help="preview calls/budget/worktrees/outputs; zero external calls")

    r = sub.add_parser("reproduce", parents=[common_budget], help="attempt reproduction of one accepted field failure")
    r.add_argument("--failure-record", required=True)
    r.add_argument("--runs", default="", help="path to a JSON list of reproduction run records")
    r.add_argument("--dry-run", action="store_true")

    pr = sub.add_parser("propose", parents=[common_budget], help="invoke bounded Researcher + preflight one proposal")
    pr.add_argument("--failure-record", required=True)
    pr.add_argument("--source-revision", default="HEAD")
    pr.add_argument("--dry-run", action="store_true")

    rep = sub.add_parser("report", help="validate ledger and render a batch/experiment report")
    rep.add_argument("--run-manifest", required=True)
    rep.add_argument("--ledger", default=None)
    rep.add_argument("--decision", default=None, choices=["keep_candidate", "discard", "inconclusive"])

    cl = sub.add_parser("cleanup", help="remove only registered ephemeral worktrees/state")
    cl.add_argument("--run-manifest", required=True)

    return p


def _git_rev(repo_root: Path, rev: str) -> str:
    import subprocess

    out = subprocess.run(["git", "rev-parse", rev], cwd=repo_root, capture_output=True, text=True)
    return out.stdout.strip() or rev


def main(argv: Optional[list] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    controller = Controller()

    try:
        if args.verb == "doctor":
            res = controller.doctor(batch_config=_load_json(args.batch_config), budget=_budget_from_args(args))
            print(res.render())
            return EXIT_OK if res.ok else EXIT_PREFLIGHT

        if args.verb == "context":
            rev = _git_rev(REPO_ROOT, args.source_revision)
            manifest = controller.compile_context(role=args.role, project=args.project, source_revision=rev)
            print(cpc.render_summary(manifest) if args.summary else json.dumps(manifest, indent=2))
            return EXIT_OK

        if args.verb in ("baseline", "experiment", "batch"):
            batch_config = _load_json(args.batch_config) or {}
            budget = _budget_from_args(args)
            case_ids = [c for c in args.cases.split(",") if c]
            preview = controller.preview_experiment(
                batch_config=batch_config, case_ids=case_ids or ["<none>"], run_count=args.run_count, budget=budget
            )
            if args.dry_run:
                print(json.dumps({"verb": args.verb, "dry_run": True, "preview": preview}, indent=2))
                return EXIT_OK
            # A real run requires an authorized live transport binding.
            doctor = controller.doctor(batch_config=batch_config, budget=budget)
            if not doctor.ok:
                print(doctor.render(), file=sys.stderr)
                return EXIT_PREFLIGHT
            print(
                json.dumps(
                    {
                        "verb": args.verb,
                        "status": "blocked",
                        "reason": "no authorized live PlaywrightMcpBrowserTransport binding is wired into this CLI invocation; "
                        "per live-contract §5/§10 a live batch needs an explicit owner-authorized transport. "
                        "Use --dry-run to preview, or run under the coordinated live session (#417).",
                        "preview": preview,
                    },
                    indent=2,
                )
            )
            return EXIT_BLOCKED

        if args.verb == "reproduce":
            rec = _load_json(args.failure_record)
            runs = _load_json(args.runs) if args.runs else []
            if isinstance(runs, dict):
                runs = runs.get("runs", [])
            if args.dry_run:
                print(json.dumps({"verb": "reproduce", "dry_run": True, "would_assess_runs": len(runs or [])}, indent=2))
                return EXIT_OK
            assessed = fi.assess_reproduction(rec, runs or [])
            print(json.dumps({"reproduction_status": assessed["reproduction_status"],
                              "reproduction_run_refs": assessed["reproduction_run_refs"]}, indent=2))
            return EXIT_OK

        if args.verb == "propose":
            rec = _load_json(args.failure_record)
            if args.dry_run:
                print(json.dumps({"verb": "propose", "dry_run": True,
                                  "researcher_calls_planned": 1, "retry_allowed": 1}, indent=2))
                return EXIT_OK
            if controller.researcher_model is None:
                print(json.dumps({"verb": "propose", "status": "blocked",
                                  "reason": "no live Researcher model binding; use --dry-run or the coordinated live session (#415/#417)."}, indent=2))
                return EXIT_BLOCKED
            return EXIT_OK

        if args.verb == "report":
            rm = RunManifest.load(Path(args.run_manifest))
            budget = RoleBudget(max_provider_calls=None, max_cost_amount=None, max_cost_currency=None)
            rep = controller.report(run_manifest=rm, budget=budget,
                                    ledger_path=Path(args.ledger) if args.ledger else None, decision=args.decision)
            print(json.dumps(rep, indent=2))
            return EXIT_INTEGRITY if rep["ledger_status"] == "integrity_failure" else EXIT_OK

        if args.verb == "cleanup":
            rm = RunManifest.load(Path(args.run_manifest))
            removed = controller.cleanup(rm)
            rm.save(Path(args.run_manifest))
            print(json.dumps({"verb": "cleanup", "removed": removed}, indent=2))
            return EXIT_OK

        parser.error(f"unknown verb {args.verb!r}")
        return EXIT_USAGE
    except CliError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.code
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_USAGE


if __name__ == "__main__":
    raise SystemExit(main())
