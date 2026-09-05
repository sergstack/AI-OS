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
        # issue #433, minimal-for-C1 scope: run_experiment always performs
        # exactly `adc.MIN_MATCHED_RERUNS` matched reruns per case (no §8
        # 3->5 escalation in this scope), regardless of the `run_count`
        # argument/spec field -- so the preview reflects the ACTUAL call
        # count using the constant, not the requested run_count. The Judge
        # runs a blind A/B pass (both orders) on every one of those matched
        # reruns, not just once, because the MD-2 minimal mapping needs one
        # verdict pair per rerun to fill the comparator's per-rerun tuples.
        reruns = adc.MIN_MATCHED_RERUNS
        subject = 2 * reruns * len(case_ids)  # baseline + candidate, per case, per matched rerun
        judge = 2 * reruns * len(case_ids)  # blind A/B both orders, per case, per matched rerun
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

    # -- run_experiment (issue #433: the sequencer #416 never committed) --

    def run_experiment(
        self,
        *,
        spec: "ManualCandidateSpec",
        batch_config: dict,
        budget: RoleBudget,
        evidence_dir: Optional[Path] = None,
    ) -> dict:
        """Sequence the already-frozen live components into ONE matched
        baseline/candidate evaluation. This method invents NO decision logic:
        every gate, comparison, and verdict comes from an existing function
        (`cpc.*`, `asr.run_shadow_experiment`, `lj.run_blind_ab`,
        `adc.evaluate_case` / `adc.aggregate_decision`). It is reachable only
        when a real transport + judge binding has been injected into this
        Controller by `autoresearch_coordinated_session` under a coordinated
        live session; a bare CLI invocation keeps `transport is None` and is
        still structurally blocked.

        Method semantics (owner ruling, issue #433 -- MINIMAL-FOR-C1 scope,
        supersedes an earlier, broader MD-1..4 WIP; NOT the general reusable
        MD-1..4 semantics):
        - MD-1: exactly `adc.MIN_MATCHED_RERUNS` (3) matched reruns per case,
          always -- no more, no fewer. The canonical #395 §8 3->5 escalation
          loop is explicitly OUT OF SCOPE and NOT implemented here (deferred
          to a follow-up). If the §8 trigger condition fires anyway (a
          target-family case's `missingness_reason ==
          "evaluator_disagreement_unresolved"`), this code does not improvise
          extra reruns or a fix -- the comparator's own fallback already
          yields "inconclusive" for that case, and an explicit limitation
          string is recorded (see `_ESCALATION_TRIGGER_LIMITATION_PREFIX`
          below). That path never produces `keep_candidate` / PASS.
        - MD-2 (issue #435 decision, 2026-09-05, supersedes the earlier
          minimal-for-C1 symmetric mapping): `lj.run_blind_ab` now returns
          `sem.directional_verdicts`, a de-blinded `(baseline_verdict,
          candidate_verdict)` pair computed from the Judge's blind, POSITIONAL
          `subject` attribution (A/B/both -- never baseline/candidate
          identity) on each finding, only when both presentation orders
          agree on it after de-blinding. `_directional_pair` below passes
          this straight through -- it invents no direction itself, and
          `adc.evaluate_case_material_improvement` /
          `adc.aggregate_decision` are UNCHANGED by this decision.
        - MD-3: the outcome is written as a schema-valid
          `manual_candidate_evaluation` record appended to the shared
          tamper-evident hash-chained ledger (a distinct research-evidence
          class, not a failure-driven experiment_record).
        - MD-4: `keep_candidate` from the comparator is relabelled to
          `candidate_for_owner_review` (authority-lowering only); the raw
          comparator decision is preserved verbatim.
        The #395 comparator method and the frozen #394 evaluator contract are
        used UNCHANGED (no schema, prompt, or evaluator_contract_version
        change for this scope).
        """
        # -- fail-closed guards (reuse the same predicates doctor uses) --
        if self.transport is None:
            return {
                "status": "blocked",
                "reason": "no live transport binding; run via autoresearch_coordinated_session "
                "under a coordinated live session (issue #433). A bare CLI process cannot hold one.",
            }
        if self.judge_model is None:
            return {"status": "blocked", "reason": "no live judge binding"}
        if not budget.authorized():
            return {"status": "blocked", "reason": "budget not authorized (numeric call ceiling + cost cap + currency required)"}
        if str(batch_config.get("authority_status") or "") != "authorized":
            return {"status": "blocked", "reason": "batch authority_status is not 'authorized'"}
        ts_guard = batch_config.get("call_timeout_seconds")
        if not (isinstance(ts_guard, int) and not isinstance(ts_guard, bool) and ts_guard > 0):
            return {
                "status": "blocked",
                "reason": "call_timeout_seconds missing/invalid in batch_config; an explicit "
                "owner-authorized positive integer value is required",
            }
        if spec.run_count != adc.MIN_MATCHED_RERUNS:
            return {
                "status": "blocked",
                "reason": f"run_count must equal adc.MIN_MATCHED_RERUNS ({adc.MIN_MATCHED_RERUNS}) in this "
                f"minimal-for-C1 scope; got {spec.run_count}",
            }
        # Controlled-L1 context-boundary guards ([LLM]->[Codex] handoff, 2026-09-05):
        # a causal repo_replay comparison requires the Subject to run in a
        # neutral, non-Project-scoped transport (native Project instructions
        # are an uncontrolled concurrent treatment competing with the
        # candidate) and requires account-level memory/personalization/
        # custom-instruction influence to be proven excluded. Both fail
        # closed -- 'unproven' is never treated as 'excluded'. Native-Project
        # execution is reserved for a separate, not-yet-implemented,
        # owner-gated L2 transfer contract; no code path here ever runs one.
        if str(batch_config.get("subject_context_scope") or "") != "non_project_controlled":
            return {
                "status": "blocked",
                "reason": "subject_context_scope must be 'non_project_controlled' for a repo_replay "
                "causal comparison; a native-Project-scoped transport is a separate, "
                "not-yet-implemented L2 transfer contract and must never be used for this comparison.",
            }
        # Owner ruling, 2026-09-05 (hard block, not a value check): this
        # codebase has NO implemented machine-verification mechanism for
        # memory/personalization isolation -- none is invented here either.
        # A self-declared 'verified_disabled' string is not evidence, so a
        # causal L1 run (any real, non-test-double transport -- fake_browser
        # is fixed and cannot be mistaken for one) is hard-blocked
        # UNCONDITIONALLY on this precondition, regardless of what
        # batch_config declares, until a real verifier exists as separate,
        # not-yet-started work. This deliberately does NOT gate the
        # deterministic four-control calibration harness (FakeBrowserTransport,
        # capture_method == 'test_double'): that harness makes zero external
        # calls and has no isolation concern to verify in the first place.
        if self.transport.capture_method != "test_double":
            return {
                "status": "blocked",
                "reason": "memory_personalization_isolation_status has no machine-verifiable evidence "
                "mechanism implemented in this codebase; causal L1 is hard-blocked on this "
                f"precondition regardless of the declared value ({batch_config.get('memory_personalization_isolation_status')!r}) "
                "until a real verifier exists (owner ruling 2026-09-05) -- self-declaration is not evidence.",
            }

        manifest = av.load_manifest()
        shared_budget = budget.as_shared_state()
        evidence: dict = {
            "schema_note": "human-readable companion to the schema-valid, ledgered manual_candidate_evaluation record (issue #433); NOT a failure-driven experiment_record",
            "mode": spec.mode,
            "experiment_id": spec.experiment_id,
            "baseline_revision": spec.baseline_revision,
            "research_surface": spec.research_surface,
            "target_file": spec.target_file,
            "candidate_patch_hash": spec.candidate_patch_hash,
            "run_count": spec.run_count,
            "reruns": [],
            "limitations": [
                "repo_replay via a fresh chat is a lower-fidelity approximation of the real configured Project runtime; no UI-equivalence claim.",
                "subject and Judge share a model class (limited_same_model_class); Judge agreement is not independent corroboration.",
                "issue #435 decision (2026-09-05): MD-2 directional Judge extension is live -- blind A/B, positional subject attribution (A/B/both) de-blinded only after both orders validate; order-disagreement still maps to inconclusive, never averaged. Full §8 3->5 escalation remains out of scope and is explicitly blocked by the run_count guard below, not silently skipped.",
            ],
        }

        # -- deterministic context + hard-gate layer (all reused, unchanged) --
        try:
            baseline_ctx = cpc.compile_subject_baseline(
                repo_root=self.repo_root, source_revision=spec.baseline_revision, project=spec.project,
                research_surface=spec.research_surface,
            )
            # compile_subject_candidate runs asr.reject_patch_scope (the #388/#390
            # hard scope gate) inside an isolated worktree BEFORE rendering.
            candidate_ctx = cpc.compile_subject_candidate(
                repo_root=self.repo_root,
                source_revision=spec.baseline_revision,
                project=spec.project,
                candidate_patch_text=spec.patch_text,
                research_surface=spec.research_surface,
            )
        except cpc.ContextCompilerError as exc:
            evidence["hard_gate"] = {"status": "violated", "detail": str(exc)}
            return _finalize_pilot(evidence, raw_decision="discard", spec=spec, batch_config=batch_config,
                                   reason=f"deterministic hard gate (patch scope / apply): {exc}",
                                   evidence_dir=evidence_dir, budget=budget, shared_budget=shared_budget)

        # Loaded here (immediately once both contexts are known to have
        # compiled) so that `baseline_ctx`/`candidate_ctx`/`evh` are always
        # captured TOGETHER -- both on the context-drift early exit below and
        # on the full success path. This keeps `context_identities`'s single
        # `context_capture_status` flag (fix #2, issue #433) honest: it never
        # has to describe a state where only some of the three were captured.
        evaluator_config = lj.EvaluatorConfig.load(
            self.repo_root / "docs/standards/autoresearch_v02_evaluator_config.json"
        )
        evh = evaluator_config.frozen_hash()

        equiv = cpc.equivalence_report(baseline_ctx, candidate_ctx)
        evidence["context_equivalence"] = equiv
        if not equiv.get("equivalent") or set(equiv.get("differences", [])) - {spec.target_file}:
            return _finalize_pilot(evidence, raw_decision="discard", spec=spec, batch_config=batch_config,
                                   baseline_ctx=baseline_ctx, candidate_ctx=candidate_ctx, evh=evh,
                                   evaluator_config=evaluator_config,
                                   reason=f"context drift outside the declared mutation: {equiv}",
                                   evidence_dir=evidence_dir, budget=budget, shared_budget=shared_budget)
        # Mutation-visibility gate ([LLM]->[Codex] handoff, 2026-09-05): a
        # patch existing in Git is not itself experimental treatment -- the
        # declared mutation must actually be rendered into the Subject's
        # final payload (via mutable_surface_excerpt), or the comparison
        # never actually tested what it claims to. Zero Judge/Subject calls
        # happen past this point when the gate fires.
        excerpt_info = equiv.get("mutable_surface_excerpt") or {}
        if not excerpt_info.get("present") or not excerpt_info.get("excerpt_differs"):
            return _finalize_pilot(evidence, raw_decision="discard", spec=spec, batch_config=batch_config,
                                   baseline_ctx=baseline_ctx, candidate_ctx=candidate_ctx, evh=evh,
                                   evaluator_config=evaluator_config,
                                   reason=f"declared mutation is not visible in the rendered subject payload: {excerpt_info}",
                                   evidence_dir=evidence_dir, budget=budget, shared_budget=shared_budget)
        evidence["baseline_context_hash"] = baseline_ctx["context_hash"]
        evidence["candidate_context_hash"] = candidate_ctx["context_hash"]

        case_ids = [c["case_id"] for c in spec.cases]
        finding_schema = _load_json(
            str(self.repo_root / "schemas/autoresearch_live_semantic_finding.schema.json")
        )
        retry_limit = int(batch_config.get("retry_limit", 1))
        authority_evidence_ref = str(batch_config.get("authority_evidence_ref", ""))

        # per-case accumulators
        per_case: dict = {
            cid: {"baseline_verdicts": [], "candidate_verdicts": [], "b_hashes": [], "c_hashes": [],
                  "obs_rows": [], "sems": []}
            for cid in case_ids
        }

        def _one_matched_rerun(k: int) -> Optional[dict]:
            """One matched rerun = 1 shadow experiment (subject baseline+candidate
            per case) + a blind A/B Judge pass per case. Returns None on a
            deterministic hard-gate rejection (caller -> reject)."""
            cids = case_ids
            exp_id_k = f"{spec.experiment_id}-r{k}"
            requests_by_key = _build_requests(
                spec=spec, experiment_id=exp_id_k, case_ids=cids,
                baseline_ctx=baseline_ctx, candidate_ctx=candidate_ctx,
                authority_evidence_ref=authority_evidence_ref,
            )
            policy = _transport_policy(batch_config)
            sink: list = []
            adapter = lba.live_browser_adapter_callable(
                requests_by_key=requests_by_key, policy=policy, budget=shared_budget,
                transport=self.transport, results_sink=sink,
            )
            min_record = {
                "experiment_id": exp_id_k, "baseline_revision": spec.baseline_revision,
                "candidate_patch_hash": spec.candidate_patch_hash, "research_surface": spec.research_surface,
            }
            rr = asr.run_shadow_experiment(
                repo_root=self.repo_root, experiment_record=min_record, manifest=manifest,
                patch_text=spec.patch_text, adapter=adapter, case_ids=cids,
            )
            rec = {"rerun": k, "experiment_id": exp_id_k, "shadow_status": rr.status, "notes": rr.notes,
                   "invocations": [lba.to_live_invocation_record(r) for r in sink],
                   "shadow_findings": [f.evidence for f in rr.findings], "cases": {}}
            if rr.status == "rejected":
                evidence["reruns"].append(rec)
                return None

            for cid in cids:
                c = next(x for x in spec.cases if x["case_id"] == cid)
                bl = (rr.baseline_observations or {}).get(cid)
                cd = (rr.candidate_observations or {}).get(cid)
                bl_txt = bl["response"] if bl else None
                cd_txt = cd["response"] if cd else None
                bl_h = bl.get("response_hash") if bl else None
                cd_h = cd.get("response_hash") if cd else None
                if not bl_txt or not cd_txt:
                    # missing subject output this rerun -> null verdict pair (#395 §10 no_observation)
                    per_case[cid]["baseline_verdicts"].append(None)
                    per_case[cid]["candidate_verdicts"].append(None)
                    per_case[cid]["b_hashes"].append(bl_h)
                    per_case[cid]["c_hashes"].append(cd_h)
                    rec["cases"][cid] = {"baseline_verdict": None, "candidate_verdict": None,
                                         "baseline_response_hash": bl_h, "candidate_response_hash": cd_h,
                                         "judge_consistency": "not_run", "reason": "missing subject output"}
                    continue
                sem = lj.run_blind_ab(
                    case={"case_id": cid, "case_family": c["case_family"], "input": c.get("input")},
                    baseline_output=bl_txt, candidate_output=cd_txt,
                    evaluator_config=evaluator_config, judge=self.judge_model,
                    finding_schema=finding_schema, experiment_id=f"{exp_id_k}",
                    seed=spec.seed, deterministic_precheck="none", retry_limit=retry_limit,
                )
                bv, cv = _directional_pair(sem)
                per_case[cid]["baseline_verdicts"].append(bv)
                per_case[cid]["candidate_verdicts"].append(cv)
                per_case[cid]["b_hashes"].append(bl_h)
                per_case[cid]["c_hashes"].append(cd_h)
                per_case[cid]["sems"].append((k, sem))
                rec["cases"][cid] = {
                    "baseline_verdict": bv, "candidate_verdict": cv,
                    "baseline_response_hash": bl_h, "candidate_response_hash": cd_h,
                    "judge_consistency": sem.consistency, "contributes": sem.contributes,
                    "judge_invocation_ids": sem.judge_invocation_ids, "deblinding": sem.deblinding,
                }
            evidence["reruns"].append(rec)
            return rec

        # -- MD-1 (minimal-for-C1 scope, issue #433 owner ruling): exactly
        # `adc.MIN_MATCHED_RERUNS` matched reruns per case, always -- no §8
        # 3->5 escalation loop in this scope (deferred to a follow-up).
        for k in range(adc.MIN_MATCHED_RERUNS):
            if _one_matched_rerun(k) is None:
                return _finalize_pilot(
                    evidence, raw_decision="discard", spec=spec, batch_config=batch_config,
                    baseline_ctx=baseline_ctx, candidate_ctx=candidate_ctx, evh=evh,
                    evaluator_config=evaluator_config, per_case=per_case, case_results=[],
                    reason="deterministic hard gate inside run_shadow_experiment",
                    evidence_dir=evidence_dir, budget=budget, shared_budget=shared_budget)

        case_results: list = []
        for c in spec.cases:
            cid = c["case_id"]
            pc = per_case[cid]
            obs = adc.CaseObservation(
                case_id=cid, case_family=c["case_family"],
                baseline_verdicts=tuple(v if v in ("pass", "revise", "blocked") else None
                                       for v in pc["baseline_verdicts"]),
                candidate_verdicts=tuple(v if v in ("pass", "revise", "blocked") else None
                                         for v in pc["candidate_verdicts"]),
                model_provider_runtime_hash=av.sha256_hex(
                    json.dumps({"transport": batch_config.get("transport_id"), "case": cid},
                               sort_keys=True).encode()),
                evaluator_version_hash=evh,
                hard_gate_status="pass",
            )
            pc["obs_rows"] = [_obs_dump(obs)]
            case_results.append(adc.evaluate_case(obs, target_family_flag=c["target_family_flag"]))

        # MD-1 (minimal-for-C1 scope): if the canonical #395 §8 trigger fires
        # anyway (a target-family case is inconclusive because of unresolved
        # evaluator/run-variance disagreement at MIN_MATCHED_RERUNS), do NOT
        # improvise extra reruns or a fix -- adc's own fallback already
        # yields "inconclusive" for that case and `aggregate_decision` turns
        # any non-"keep" target result into a batch "inconclusive". Just
        # record an honest, explicit annotation; never upgrade this to PASS.
        evidence["limitations"].extend(_escalation_trigger_limitations(case_results))

        evidence["rerun_policy"] = {
            "min_matched_reruns": adc.MIN_MATCHED_RERUNS, "ceiling": 5,
            "escalation_trigger": _ESCALATION_TRIGGER_LIMITATION_PREFIX,
            "per_case_reruns_used": {cid: len(per_case[cid]["baseline_verdicts"]) for cid in case_ids},
            "escalated_cases": [], "budget_limited_cases": [],
        }

        raw = adc.aggregate_decision(case_results)
        evidence["comparator"] = raw
        evidence["case_results"] = [
            {"case_id": r.case_id, "case_family": r.case_family,
             "non_inferiority_result": r.non_inferiority_result,
             "material_regression_flag": r.material_regression_flag,
             "material_improvement_result": r.material_improvement_result,
             "run_variance_baseline": r.run_variance_baseline,
             "run_variance_candidate": r.run_variance_candidate,
             "missingness_reason": r.missingness_reason}
            for r in case_results
        ]
        return _finalize_pilot(
            evidence, raw_decision=raw["decision"], reason=raw["reason"], spec=spec,
            batch_config=batch_config, baseline_ctx=baseline_ctx, candidate_ctx=candidate_ctx,
            evh=evh, evaluator_config=evaluator_config, per_case=per_case, case_results=case_results,
            evidence_dir=evidence_dir, budget=budget, shared_budget=shared_budget)


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


# ---------------------------------------------------------------------------
# run_experiment support (issue #433) -- pure glue over frozen components
# ---------------------------------------------------------------------------


@dataclass
class ManualCandidateSpec:
    """One human-authored, pre-frozen candidate for a bounded
    `manual_candidate_evaluation` (issue #433). Not a Researcher proposal and
    not a failure-driven experiment: `research_surface` must still be a
    declared mutable surface id, `patch_text` must still pass the frozen
    scope gate, and the outcome maps to reject | inconclusive |
    candidate_for_owner_review -- never keep_candidate."""

    experiment_id: str
    baseline_revision: str
    project: str
    research_surface: str
    target_file: str
    patch_text: str
    candidate_patch_hash: str
    cases: list  # [{case_id, case_family, target_family_flag, input}]
    run_count: int = 3
    seed: int = 0
    mode: str = "manual_candidate_evaluation"


def _transport_policy(batch_config: dict) -> "lba.TransportPolicy":
    """Build the frozen per-batch browser policy from the #411 batch config.
    `call_timeout_seconds` is threaded through as an attribute the adapter's
    `_timeout_seconds` already looks for. issue #433 fix #3: no default is
    invented here -- when this is reached from `run_experiment`'s own rerun
    loop, `call_timeout_seconds` is already guaranteed to be a valid,
    owner-authorized positive integer by the fail-closed guard at the top of
    `run_experiment` (it runs before any of this code, and before any
    external call). A caller outside that guarded path (e.g. a coordinated
    session building a judge binding ahead of time) may still pass an
    unvalidated `batch_config`; this function performs no I/O itself, so a
    missing/invalid value here is caught by `run_experiment`'s guard before
    any live call is made."""
    policy = lba.TransportPolicy(
        transport_id=batch_config.get("transport_id", "playwright_mcp"),
        transport_version=str(batch_config.get("transport_version", "unversioned")),
        transport_mode="dedicated_persistent_profile",
        target_product=batch_config.get("target_product", "openai_chatgpt_ui"),
        target_url_prefix=batch_config.get("target_url_prefix", "https://chatgpt.com/"),
        session_policy=batch_config.get("session_policy", "fresh_conversation"),
        expected_model_selector=batch_config.get("expected_model_selector") or None,
        expected_context_hash=None,  # each request carries its own; baseline != candidate by design
        subject_context_scope=batch_config.get("subject_context_scope", "non_project_controlled"),
    )
    object.__setattr__(policy, "call_timeout_seconds", batch_config.get("call_timeout_seconds"))
    return policy


def _build_requests(*, spec: ManualCandidateSpec, experiment_id: str, case_ids: list,
                    baseline_ctx: dict, candidate_ctx: dict, authority_evidence_ref: str) -> dict:
    out: dict = {}
    for cid in case_ids:
        for condition, ctx in (("baseline", baseline_ctx), ("candidate", candidate_ctx)):
            payload = _case_payload(spec, cid, ctx)
            out[(experiment_id, condition, cid)] = lba.LiveInvocationRequest(
                invocation_id=f"{experiment_id}:{condition}:{cid}",
                experiment_id=experiment_id, condition=condition, case_id=cid,
                context_id=ctx["context_id"], context_hash=ctx["context_hash"],
                payload_text=payload, authority_evidence_ref=authority_evidence_ref,
                external_action_preview_ref=f"preview:{experiment_id}:{condition}:{cid}",
            )
    return out


def _case_payload(spec: ManualCandidateSpec, case_id: str, ctx: dict) -> str:
    """The subject prompt: the compiled repo-replay context summary followed
    by the frozen case task text. Deterministic; no candidate identity or
    hypothesis is ever included (both conditions get the same case text; only
    the context differs, by exactly the one mutated file)."""
    case = next((c for c in spec.cases if c["case_id"] == case_id), {})
    task = case.get("input") or "[no case input provided]"
    return f"{cpc.render_summary(ctx)}\n\n---\nTASK:\n{task}\n"


def _obs_dump(obs) -> dict:
    return {
        "case_id": obs.case_id, "case_family": obs.case_family,
        "baseline_verdicts": list(obs.baseline_verdicts),
        "candidate_verdicts": list(obs.candidate_verdicts),
        "hard_gate_status": obs.hard_gate_status,
    }


# --- METHOD DECISION MD-2 (owner decision on issue #435, 2026-09-05) ---
# `lj.run_blind_ab` now computes a directional, de-blinded
# `(baseline_verdict, candidate_verdict)` pair itself (see
# CaseSemanticEvidence.directional_verdicts in autoresearch_live_judge.py):
# each finding carries a POSITIONAL `subject` (A/B/both -- never baseline/
# candidate identity), the per-side worst verdict is computed from that
# attribution independently for each presentation order, and the two orders
# must agree on the RESULT after de-blinding or the pair is discarded
# (order disagreement -> inconclusive, exactly as before -- never averaged).
# This function does not invent any direction of its own; it passes through
# exactly what `run_blind_ab` already validated and de-blinded. It does not
# modify the #395 comparator method or the #394 evaluator contract's
# vocabulary -- `adc.CaseObservation`/`adc.evaluate_case_material_improvement`
# are byte-for-byte unchanged. The full 3->5 §8 escalation loop remains out
# of scope and is explicitly blocked by the `run_count` guard above, not
# silently skipped.
def _directional_pair(sem: "lj.CaseSemanticEvidence") -> tuple:
    if sem.directional_verdicts is None:
        return (None, None)
    return sem.directional_verdicts


_ESCALATION_TRIGGER_LIMITATION_PREFIX = (
    "#395 §8 escalation trigger (run_variance_or_disagreement) fired for"
)


def _escalation_trigger_limitations(case_results: list) -> list:
    """MD-1 (minimal-for-C1 scope, issue #433 owner ruling): if the canonical
    #395 §8 trigger fires for a case (`missingness_reason ==
    "evaluator_disagreement_unresolved"`, equivalently `run_variance_baseline`
    True at MIN_MATCHED_RERUNS), never improvise extra reruns or a fix --
    `adc`'s own fallback already yields "inconclusive" for that case and
    `aggregate_decision` turns any non-"keep" target result into a batch
    "inconclusive". Just return an explicit, honest limitation string per
    such case; the caller never upgrades this path to PASS."""
    out = []
    for r in case_results:
        if r.missingness_reason == "evaluator_disagreement_unresolved":
            out.append(
                f"{_ESCALATION_TRIGGER_LIMITATION_PREFIX} case_id={r.case_id!r}; "
                "full 3->5 escalation is out of scope for this minimal pilot and deferred to a "
                "follow-up; result recorded as inconclusive, never upgraded."
            )
    return out


# MD-4 (owner decision, issue #433): authority-LOWERING relabel only. The raw
# adc.aggregate_decision value is preserved verbatim in the ledger record and
# the result. candidate_for_owner_review carries no acceptance / merge /
# promotion authority; keep_candidate is never surfaced.
_PILOT_DECISION = {
    "keep_candidate": "candidate_for_owner_review",
    "discard": "reject",
    "inconclusive": "inconclusive",
}


def _first_hashes(baseline_ctx: Optional[dict], spec: "ManualCandidateSpec") -> Optional[str]:
    """The real content hash of `spec.target_file` inside the compiled
    baseline context, or `None` if it was never captured. NEVER a fabricated
    zero-hash or a hash of the file NAME string -- `None` is the honest value
    when no real content hash exists (paired with the record's
    `baseline_file_hash_status`, issue #433 fix #2). `baseline_ctx` is `None`
    on an early fail-closed exit (context never compiled). The target file can
    also legitimately be absent from `ordered_sources` if
    `canonical_subject_sources` excludes it for this project's capability
    declarations -- that is also `None`/`not_captured`, never a fallback
    hash."""
    if baseline_ctx is None:
        return None
    src = next((s for s in baseline_ctx.get("ordered_sources", []) if spec.target_file in s.get("path", "")), None)
    return src["content_hash"] if src else None


def _finalize_pilot(evidence: dict, *, raw_decision: str, reason: str, spec: "ManualCandidateSpec",
                    batch_config: dict, evidence_dir: Optional[Path], budget: RoleBudget, shared_budget,
                    baseline_ctx: Optional[dict] = None, candidate_ctx: Optional[dict] = None,
                    evh: Optional[str] = None, evaluator_config=None,
                    per_case: Optional[dict] = None, case_results: Optional[list] = None) -> dict:
    per_case = per_case or {}
    case_results = case_results or []
    # issue #433 fix #2: `baseline_ctx`/`candidate_ctx`/`evh` are always
    # captured together in `run_experiment`'s current control flow (the
    # evaluator config + its frozen hash are loaded immediately once both
    # contexts are known to have compiled, before either the context-drift
    # early exit or the full success path) -- so ONE shared status flag
    # covers all three honestly.
    context_captured = baseline_ctx is not None and candidate_ctx is not None and evh is not None
    if not context_captured:
        evidence["limitations"].append(
            "context compilation did not complete for this experiment (a deterministic hard gate fired "
            "before both baseline and candidate context could be compiled); the context hashes below are "
            "null (not_captured), never a fabricated placeholder hash."
        )
    pilot_decision = _PILOT_DECISION.get(raw_decision, "inconclusive")
    evidence["raw_decision"] = raw_decision
    evidence["pilot_decision"] = pilot_decision
    evidence["decision_reason"] = reason
    evidence["budget"] = budget.summary()

    # ---- MD-3: build the schema-valid, ledgered manual_candidate_evaluation record ----
    matched_observations = []
    judge_findings = []
    for rr in evidence.get("reruns", []):
        invocations_by_key = {
            (inv.get("case_id"), inv.get("condition")): inv.get("invocation_id")
            for inv in rr.get("invocations", [])
        }
        for cid, cd in rr.get("cases", {}).items():
            matched_observations.append({
                "case_id": cid,
                "case_family": next((c["case_family"] for c in spec.cases if c["case_id"] == cid), "routing"),
                "rerun": rr["rerun"],
                "baseline_response_hash": cd.get("baseline_response_hash"),
                "candidate_response_hash": cd.get("candidate_response_hash"),
                "baseline_verdict": cd.get("baseline_verdict"),
                "candidate_verdict": cd.get("candidate_verdict"),
                # issue #433 fix #5: the SUBJECT's own recorded invocation ids
                # for this rerun/case/condition -- looked up from the actually
                # recorded `rr["invocations"]`, never reconstructed/guessed;
                # `None` when no matching subject invocation was recorded
                # (e.g. the call was never attempted after an earlier
                # failure).
                "baseline_invocation_id": invocations_by_key.get((cid, "baseline")),
                "candidate_invocation_id": invocations_by_key.get((cid, "candidate")),
                # honestly labeled: these are the JUDGE's invocation ids, not
                # a generic "live_invocation_ids" (issue #433 fix #5).
                "judge_invocation_ids": cd.get("judge_invocation_ids", []),
                "judge_consistency": cd.get("judge_consistency", "not_run"),
            })
    for cid, pc in per_case.items():
        # issue #433 fix #4: keep the Judge finding for EVERY matched rerun
        # (not just the first) -- `sems` now stores (rerun_index, sem) pairs
        # so the true rerun index survives even when a rerun is skipped for a
        # case (missing subject output) and its position in the list would
        # otherwise no longer line up with the rerun number.
        for k, sem in pc.get("sems", []):
            bv, cv = _directional_pair(sem)
            judge_findings.append({
                "case_id": cid, "rerun": k, "consistency": sem.consistency,
                "baseline_verdict": bv, "candidate_verdict": cv,
                "contributes": sem.contributes, "deblinding": sem.deblinding,
            })

    rp = evidence.get("rerun_policy", {
        "min_matched_reruns": adc.MIN_MATCHED_RERUNS, "ceiling": 5,
        "escalation_trigger": "#395 §8 (n/a: hard gate fired before any matched rerun)",
        "per_case_reruns_used": {}, "escalated_cases": [], "budget_limited_cases": [],
    })
    baseline_file_hash = _first_hashes(baseline_ctx, spec)
    record = {
        "schema_version": "0.2.0",
        "record_kind": "manual_candidate_evaluation",
        "experiment_id": spec.experiment_id,
        "batch_id": str(batch_config.get("batch_id", spec.experiment_id)),
        "created_at": _now_iso(),
        "baseline_revision": spec.baseline_revision,
        # issue #433 fix #2: honest nullable hash + explicit status -- never a
        # fabricated zero-hash or filename hash.
        "baseline_file_hash": baseline_file_hash,
        "baseline_file_hash_status": "captured" if baseline_file_hash is not None else "not_captured",
        "candidate_patch_ref": f"sha256:{spec.candidate_patch_hash}",
        "candidate_patch_hash": spec.candidate_patch_hash,
        "target_file": spec.target_file,
        "research_surface": spec.research_surface,
        "authority_evidence_ref": str(batch_config.get("authority_evidence_ref", "")),
        "budget": {
            # issue #433 fix #3: no invented defaults. `run_experiment`'s
            # fail-closed guards (budget.authorized(), call_timeout_seconds
            # validity) already guarantee these are real, owner-authorized
            # values by the time `_finalize_pilot` is ever reached.
            "max_provider_calls": int(budget.max_provider_calls),
            "max_cost_amount": float(budget.max_cost_amount if budget.max_cost_amount is not None else 0.0),
            "max_cost_currency": budget.max_cost_currency,
            "calls_used": shared_budget.calls_used,
            "call_timeout_seconds": int(batch_config["call_timeout_seconds"]),
        },
        "context_identities": {
            "baseline_context_hash": baseline_ctx["context_hash"] if baseline_ctx else None,
            "candidate_context_hash": candidate_ctx["context_hash"] if candidate_ctx else None,
            "context_equivalence": evidence.get("context_equivalence", {"equivalent": False, "differences": []}),
            "transport_id": str(batch_config.get("transport_id", "playwright_mcp")),
            "subject_model_identity": str(batch_config.get("model", "not_observable")),
            "subject_model_identity_status": "declared" if batch_config.get("model") else "not_observable",
            "evaluator_version_hash": evh,
            "context_capture_status": "captured" if context_captured else "not_captured",
            "evaluator_contract_version": (
                evaluator_config.evaluator_contract_version if evaluator_config else "n/a-context-not-compiled"
            ),
        },
        "rerun_policy": rp,
        # issue #433 fix #1: zero observations means an empty list -- never a
        # synthetic placeholder row pretending an observation occurred.
        "matched_observations": matched_observations,
        "judge_findings": judge_findings,
        "comparator_raw_decision": {"decision": raw_decision, "reason": reason},
        "pilot_decision": pilot_decision,
        # Owner revise, 2026-09-05: the two controlled-L1 preconditions are
        # NOT equally verifiable today. subject_context_scope is now
        # machine-checked per call against the observed URL (see
        # matched_observations' invocation records / limitations above,
        # threaded from LiveInvocationResult.observed_page_url) --
        # memory_personalization_isolation_status has no such mechanism in
        # this codebase and remains a self-declared batch-config string.
        # This field states that split honestly on every record produced,
        # rather than letting a clean pilot_decision imply both are proven.
        "causal_validity_status": {
            "subject_context_scope_verification": "machine_verified_per_call_observed_url",
            "memory_personalization_isolation_verification": "self_declared_not_machine_verified",
        },
        "limitations": evidence["limitations"],
        "rollback": ("Candidate exists only in ephemeral shadow worktrees; nothing applied to main, active "
                     "Project config, or the ledger baseline. Revert is: discard the shadow worktrees. This "
                     "record and its evidence package are append-only."),
        "evidence_hashes": {
            "evidence_package_sha256": av.sha256_hex(
                json.dumps(evidence, sort_keys=True, separators=(",", ":")).encode()),
            "patch_sha256": spec.candidate_patch_hash,
        },
    }

    result = {
        "status": "completed",
        "pilot_decision": pilot_decision,
        "raw_decision": raw_decision,
        "reason": reason,
        "authority_note": "candidate_for_owner_review != keep_candidate != owner acceptance != merge/promotion authority",
    }

    schema_findings = av.validate_manual_evaluation_record(record)
    if schema_findings:
        result["status"] = "blocked"
        result["reason"] = "manual_candidate_evaluation record failed schema validation: " + \
            "; ".join(f"{f.path}: {f.evidence}" for f in schema_findings[:5])
        evidence["record_validation_errors"] = [f"{f.path}: {f.evidence}" for f in schema_findings]

    if evidence_dir is not None:
        evidence_dir = Path(evidence_dir)
        evidence_dir.mkdir(parents=True, exist_ok=True)
        pkg = evidence_dir / f"{spec.experiment_id}_evidence.json"
        pkg.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        result["evidence_path"] = str(pkg)
        rec_path = evidence_dir / f"{spec.experiment_id}_record.json"
        rec_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        result["record_path"] = str(rec_path)
        if result["status"] == "completed":
            ledger = evidence_dir / "autoresearch_manual_evaluations.jsonl"
            led_findings = av.manual_evaluation_ledger_append(ledger, record)
            if led_findings:
                result["status"] = "blocked"
                result["reason"] = "ledger append rejected: " + "; ".join(f.evidence for f in led_findings[:3])
            else:
                result["ledger_path"] = str(ledger)
    result["record"] = record
    return result


def _now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _spec_from_args(args, batch_config: dict, budget: RoleBudget) -> Optional["ManualCandidateSpec"]:
    if not getattr(args, "spec_file", None):
        return None
    raw = json.loads(Path(args.spec_file).read_text(encoding="utf-8"))
    return ManualCandidateSpec(
        experiment_id=raw["experiment_id"],
        baseline_revision=raw["baseline_revision"],
        project=raw["project"],
        research_surface=raw["research_surface"],
        target_file=raw["target_file"],
        patch_text=raw["patch_text"] if "patch_text" in raw else Path(raw["patch_file"]).read_text(encoding="utf-8"),
        candidate_patch_hash=raw["candidate_patch_hash"],
        cases=raw["cases"],
        run_count=int(raw.get("run_count", args.run_count)),
        seed=int(raw.get("seed", 0)),
    )


#: Indirection so a coordinated live session / test can supply a Controller
#: that already has a real (or fake) transport + judge binding. `main()` uses
#: the bare default, so a plain shell `autoresearch_cli experiment` still has
#: `transport is None` and stays structurally blocked.
_CONTROLLER_FACTORY = Controller


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
        e.add_argument("--spec-file", default=None,
                       help="JSON ManualCandidateSpec for a bound live 'experiment' run (issue #433)")
        e.add_argument("--evidence-dir", default=None, help="directory to write the sanitized evidence package")
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
    controller = _CONTROLLER_FACTORY()

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
            if controller.transport is None:
                # Unchanged fail-closed default: a bare shell invocation holds no
                # live transport (and cannot -- it has no MCP access). The seam
                # is `autoresearch_coordinated_session`, which injects a real
                # transport + judge and calls `Controller.run_experiment`
                # directly (issue #433).
                print(
                    json.dumps(
                        {
                            "verb": args.verb,
                            "status": "blocked",
                            "reason": "no authorized live PlaywrightMcpBrowserTransport binding is wired into this CLI invocation; "
                            "per live-contract §5/§10 a live batch needs an explicit owner-authorized transport. "
                            "Use --dry-run to preview, or run under the coordinated live session "
                            "(autoresearch_coordinated_session, issue #433).",
                            "preview": preview,
                        },
                        indent=2,
                    )
                )
                return EXIT_BLOCKED
            if args.verb != "experiment":
                print(json.dumps({"verb": args.verb, "status": "blocked",
                                  "reason": "only 'experiment' is wired for a bound live run in issue #433; "
                                            "'baseline'/'batch' remain preview/dry-run only."}, indent=2))
                return EXIT_BLOCKED
            spec = _spec_from_args(args, batch_config, budget)
            if spec is None:
                print(json.dumps({"verb": args.verb, "status": "blocked",
                                  "reason": "a bound experiment run needs a fully specified ManualCandidateSpec "
                                            "(--spec-file); none was supplied."}, indent=2))
                return EXIT_BLOCKED
            result = controller.run_experiment(spec=spec, batch_config=batch_config, budget=budget,
                                               evidence_dir=Path(args.evidence_dir) if args.evidence_dir else None)
            print(json.dumps({"verb": args.verb, **result}, indent=2))
            return EXIT_OK if result.get("status") == "completed" else EXIT_BLOCKED

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
