#!/usr/bin/env python3
"""Coordinated-session seam for AIOS AutoResearch v0.2 (issue #433, parent
#409, follow-up to #416).

This is the ONE place a real `mcp_call` enters the AutoResearch harness. A
plain `python3 scripts/autoresearch_cli.py experiment` cannot run live -- a
shell process has no MCP access -- so `main()` keeps `transport=None` and
stays structurally blocked. An operator/agent that *does* have the
`mcp__playwright__browser_*` tools calls `run_manual_candidate_evaluation`
here, passing an `mcp_call(tool_name, arguments) -> dict` proxy. That proxy
is the only new privilege; everything downstream is the already-frozen,
already-tested pipeline:

    lba.PlaywrightMcpBrowserTransport   (issue #413, reused unchanged)
    lba.live_browser_adapter_callable   (issue #413, reused unchanged)
    asr.run_shadow_experiment           (issue #393, reused unchanged)
    lj.BrowserJudgeModel / run_blind_ab (issue #414, reused unchanged)
    adc.evaluate_case / aggregate_decision (issue #395, reused unchanged)
    cli.Controller.run_experiment       (issue #433 sequencer -- NO new decision logic)

Hard boundaries (enforced by reuse, not restated):

- No admission-semantics change (#417/#418 untouched); no comparator/evaluator
  method change; no schema semantics change.
- No `keep_candidate`: a manual_candidate_evaluation resolves to
  reject | inconclusive | candidate_for_owner_review.
- No Phase 1 launch, no holdout access, no active Project / routing / main
  change, no auto PR / merge / deploy / promotion.
- This module performs NO I/O of its own: it never types a credential, never
  reads a cookie / storage-state / profile, never imports an MCP tool. It
  only forwards the injected `mcp_call`.

Method-sensitive glue (rerun orchestration MD-1, live-evidence -> comparator
input MD-2, decision label MD-4) lives in `autoresearch_cli` and is flagged
there for [AI OS] / [Analytics] sign-off per issue #433.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable, Optional

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_cli as cli  # noqa: E402
import autoresearch_live_browser_adapter as lba  # noqa: E402
import autoresearch_live_judge as lj  # noqa: E402

REPO_ROOT = cli.REPO_ROOT

McpCall = Callable[[str, dict], dict]


def build_transport(*, mcp_call: McpCall, batch_config: dict) -> "lba.PlaywrightMcpBrowserTransport":
    """The existing concrete transport, with the injected proxy. Not a new
    transport implementation."""
    return lba.PlaywrightMcpBrowserTransport(
        mcp_call=mcp_call,
        transport_version=str(batch_config.get("transport_version", "coordinated-session")),
    )


def build_judge(*, transport, batch_config: dict, budget: "lba.BudgetState",
                authority_evidence_ref: str) -> "lj.BrowserJudgeModel":
    evaluator_config = lj.EvaluatorConfig.load(
        REPO_ROOT / "docs/standards/autoresearch_v02_evaluator_config.json"
    )
    evh = evaluator_config.frozen_hash()
    return lj.BrowserJudgeModel(
        policy=cli._transport_policy(batch_config),
        budget=budget,
        transport=transport,
        judge_context_id=f"judge:{evh[:16]}",
        judge_context_hash=evh,
        authority_evidence_ref=authority_evidence_ref,
        independence_level="limited_same_model_class",
    )


def build_live_controller(*, mcp_call: McpCall, batch_config: dict, budget: "cli.RoleBudget",
                          authority_evidence_ref: str) -> "cli.Controller":
    shared = budget.as_shared_state()
    transport = build_transport(mcp_call=mcp_call, batch_config=batch_config)
    judge = build_judge(transport=transport, batch_config=batch_config, budget=shared,
                        authority_evidence_ref=authority_evidence_ref)
    return cli.Controller(transport=transport, judge_model=judge)


def run_manual_candidate_evaluation(
    *,
    mcp_call: McpCall,
    batch_config: dict,
    spec: "cli.ManualCandidateSpec",
    budget: "cli.RoleBudget",
    evidence_dir: Optional[Path] = None,
) -> dict:
    """Build a live-bound Controller and run exactly one bounded
    manual_candidate_evaluation. Fail-closed: missing authority / budget /
    session / context identity is still refused inside `run_experiment`
    (which reuses `doctor`'s predicates and `lba.invoke`'s gates)."""
    if str(batch_config.get("authority_status") or "") != "authorized":
        return {"status": "blocked", "reason": "batch authority_status is not 'authorized'"}
    if not budget.authorized():
        return {"status": "blocked", "reason": "budget not authorized"}
    authority_evidence_ref = str(batch_config.get("authority_evidence_ref", "")).strip()
    if not authority_evidence_ref:
        return {"status": "blocked", "reason": "batch_config.authority_evidence_ref is required for a live run"}

    controller = build_live_controller(
        mcp_call=mcp_call, batch_config=batch_config, budget=budget,
        authority_evidence_ref=authority_evidence_ref,
    )
    return controller.run_experiment(
        spec=spec, batch_config=batch_config, budget=budget, evidence_dir=evidence_dir,
    )


def load_spec(path: str | Path) -> "cli.ManualCandidateSpec":
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    patch_text = raw["patch_text"] if "patch_text" in raw else Path(raw["patch_file"]).read_text(encoding="utf-8")
    return cli.ManualCandidateSpec(
        experiment_id=raw["experiment_id"],
        baseline_revision=raw["baseline_revision"],
        project=raw["project"],
        research_surface=raw["research_surface"],
        target_file=raw["target_file"],
        patch_text=patch_text,
        candidate_patch_hash=raw["candidate_patch_hash"],
        cases=raw["cases"],
        run_count=int(raw.get("run_count", 3)),
        seed=int(raw.get("seed", 0)),
    )


__all__ = [
    "McpCall",
    "build_transport",
    "build_judge",
    "build_live_controller",
    "run_manual_candidate_evaluation",
    "load_spec",
]
