"""Focused tests for the AIOS AutoResearch v0.2 failure-to-experiment front end
(issue #415, parent #409).

No real browser / network / model call: `FakeResearcherModel` is deterministic
and does no I/O. The deterministic preflight uses real `git worktree`
isolation against the repo's own HEAD (no network, no active-state change).
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "autoresearch_failure_intake.py"
FAILURE_SCHEMA_PATH = REPO_ROOT / "schemas" / "autoresearch_failure_record.schema.json"
PROPOSAL_SCHEMA_PATH = REPO_ROOT / "schemas" / "autoresearch_researcher_proposal.schema.json"
CONTRACT_PATH = REPO_ROOT / "docs" / "standards" / "autoresearch_v02_researcher_contract.json"

_spec = importlib.util.spec_from_file_location("autoresearch_failure_intake", MODULE_PATH)
fi = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = fi
_spec.loader.exec_module(fi)

jsonschema = pytest.importorskip("jsonschema")

H64 = "a" * 64
H64B = "b" * 64


def _proposal_schema() -> dict:
    return json.loads(PROPOSAL_SCHEMA_PATH.read_text(encoding="utf-8"))


def _manifest() -> dict:
    return json.loads((REPO_ROOT / "docs" / "standards" / "autoresearch_v01_manifest.json").read_text(encoding="utf-8"))


def _head() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()


def _field_record(**overrides) -> dict:
    base = {
        "schema_version": "0.2.0",
        "failure_id": "F-2026-09-04-01",
        "source_type": "field_observation",
        "source_refs": ["FAILURE_REGISTRY.md#F-2026-09-04-01"],
        "observed_at": "2026-09-04",
        "project": "ai_os",
        "user_task_or_ref": "user asked for a pure backtest",
        "observed_response_or_ref": "routed to 'the research team' with no hand-off",
        "sanitization_status": "sanitized",
        "sensitivity_class": "none",
        "field_trace_provenance": "sanitized",
        "source_revision_if_known": None,
        "reproduction_status": "not_attempted",
        "reproduction_run_refs": [],
        "reproduction_context_hash": None,
        "reproduction_model_hash": None,
        "expected_contract": "route to Analytics with a context-pack hand-off",
        "actual_failure_signal": "no owner named, no hand-off",
        "candidate_cause": "tie-break wording is ambiguous for pure-analysis requests",
        "cause_target": "ROUTING_RULES.md",
        "attribution_evidence": "",
        "plausible_alternative_causes": ["model variance", "user phrasing"],
        "minimal_discriminating_test": "",
        "attribution_status": "uncertain",
        "repair_eligibility": "discriminating_experiment_only",
        "limitations": "field observation only",
    }
    base.update(overrides)
    return base


# --------------------------------------------------------------------------
# Intake + sanitisation
# --------------------------------------------------------------------------


def test_field_observation_alone_is_never_reproduced():
    rec, errs = fi.intake_field_observation(_field_record())
    assert not errs
    assert rec["reproduction_status"] == "not_attempted"
    assessed = fi.assess_reproduction(rec, reproduction_runs=[])
    assert assessed["reproduction_status"] == "not_reproduced"


def test_missing_provenance_or_sanitization_blocks_public_intake():
    rec, errs = fi.intake_field_observation(_field_record(field_trace_provenance="raw_restricted"))
    assert rec is None and any("raw_restricted" in e for e in errs)
    rec2, errs2 = fi.intake_field_observation(_field_record(sanitization_status="pending"))
    assert rec2 is None and any("sanitiz" in e.lower() for e in errs2)


def test_secret_shaped_field_record_is_blocked():
    tainted = _field_record(observed_response_or_ref="dump: Authorization: Bearer aaaaaaaaaaaaaaaaaaaa")
    rec, errs = fi.intake_field_observation(tainted)
    assert rec is None and any("secret-shaped" in e for e in errs)


def test_field_schema_is_valid_and_unknown_context_cannot_be_reproduced():
    schema = json.loads(FAILURE_SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft7Validator.check_schema(schema)
    bad = _field_record(reproduction_status="reproduced")  # context hash still null
    errs = list(jsonschema.Draft7Validator(schema).iter_errors(bad))
    assert errs  # schema itself forbids it


# --------------------------------------------------------------------------
# Reproduction assessment
# --------------------------------------------------------------------------


def test_two_matching_runs_with_evidence_reproduce():
    rec = _field_record()
    runs = [
        {"invocation_id": "r1", "context_hash": H64, "model_hash": H64B, "failure_signal_present": True},
        {"invocation_id": "r2", "context_hash": H64, "model_hash": H64B, "failure_signal_present": True},
    ]
    out = fi.assess_reproduction(rec, runs)
    assert out["reproduction_status"] == "reproduced"
    assert out["reproduction_context_hash"] == H64


def test_runs_without_hashes_do_not_qualify():
    rec = _field_record()
    runs = [{"invocation_id": "r1", "failure_signal_present": True}]
    out = fi.assess_reproduction(rec, runs)
    assert out["reproduction_status"] == "not_reproduced"


def test_mixed_signal_runs_are_inconclusive():
    rec = _field_record()
    runs = [
        {"invocation_id": "r1", "context_hash": H64, "model_hash": H64B, "failure_signal_present": True},
        {"invocation_id": "r2", "context_hash": H64, "model_hash": H64B, "failure_signal_present": False},
    ]
    out = fi.assess_reproduction(rec, runs)
    assert out["reproduction_status"] == "reproduction_inconclusive"


# --------------------------------------------------------------------------
# Attribution + eligibility
# --------------------------------------------------------------------------


def test_reproduced_without_causal_evidence_stays_uncertain():
    rec = _field_record(reproduction_status="reproduced", attribution_evidence="")
    out = fi.assess_attribution(rec)
    assert out["attribution_status"] == "uncertain"
    assert fi.eligibility_for("uncertain") == "discriminating_experiment_only"


def test_supported_needs_reproduced_plus_grounded_evidence_and_addressed_alts():
    rec = _field_record(
        reproduction_status="reproduced",
        attribution_evidence="removing the ambiguous clause in a shadow run eliminates the signal across 3 matched pairs",
        cause_target="ROUTING_RULES.md",
        plausible_alternative_causes=["model variance [addressed]", "user phrasing [addressed]"],
        minimal_discriminating_test="A/B the clause vs baseline on 5 pure-analysis prompts",
    )
    out = fi.assess_attribution(rec)
    assert out["attribution_status"] == "supported"
    assert fi.eligibility_for("supported") == "proposal_eligible"


def test_empty_cause_or_explicit_rejection_is_rejected():
    assert fi.assess_attribution(_field_record(candidate_cause=""))["attribution_status"] == "rejected"
    assert fi.assess_attribution(_field_record(attribution_explicitly_rejected=True))["attribution_status"] == "rejected"
    assert fi.eligibility_for("rejected") == "ineligible"


# --------------------------------------------------------------------------
# Researcher context boundary
# --------------------------------------------------------------------------


def test_researcher_context_excludes_holdout_validation_expected_winner_secrets():
    m = _manifest()
    ctx = fi.build_researcher_context(failure_record=_field_record(), manifest=m, budget_remaining=20)
    # The scannable (externally-sourced) regions carry none of the forbidden
    # content; the manifest legitimately *names* protected surfaces (holdout,
    # goldens) so the Researcher knows what is off-limits.
    assert fi.researcher_context_findings(ctx) == []
    scannable = json.dumps(
        [ctx["train_diagnostics"], ctx["baseline_excerpt"], ctx["failure_record"]]
    ).lower()
    for tok in ("holdout", "golden", "expected winner", "keep_candidate"):
        assert tok not in scannable
    assert ctx["budget_remaining"] == 20
    assert ctx["mutable_protected_manifest"]["mutable_surfaces"]
    assert not any(k.startswith("validation") or k.startswith("holdout") for k in ctx)


def test_build_context_refuses_when_train_diag_smuggles_holdout():
    m = _manifest()
    with pytest.raises(fi.FailureIntakeError):
        fi.build_researcher_context(
            failure_record=_field_record(), manifest=m, budget_remaining=20,
            train_diagnostics=["case X failed the holdout golden expectation"],
        )


def test_researcher_contract_hash_is_self_consistent_and_drift_rejected(tmp_path):
    c = fi.ResearcherContract.load(CONTRACT_PATH)
    raw = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    assert raw["contract_hash"] == c.frozen_hash()
    raw["prompt_text"] += " (tamper)"
    p = tmp_path / "c.json"
    p.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(fi.FailureIntakeError):
        fi.ResearcherContract.load(p)


# --------------------------------------------------------------------------
# Researcher run + preflight
# --------------------------------------------------------------------------


def _base_proposal(patch_text: str, **overrides) -> dict:
    import hashlib

    prop = {
        "schema_version": "0.2.0",
        "proposal_id": "P-001",
        "researcher_invocation_id": "exp-1:researcher:0",
        "failure_id": "F-2026-09-04-01",
        "attribution_status": "supported",
        "falsifiable_hypothesis": "Clarifying the tie-break sentence removes the missing-owner failure on pure-analysis prompts.",
        "candidate_cause": "ambiguous tie-break wording",
        "alternative_causes_considered": ["model variance"],
        "minimal_discriminating_test": "A/B the reworded clause vs baseline on 5 prompts",
        "mutation_class": "tiebreak_rule_text",
        "target_file": "ROUTING_RULES.md",
        "target_anchor": "## Tie-break rules",
        "patch_text_or_ref": patch_text,
        "patch_hash": hashlib.sha256(patch_text.encode()).hexdigest(),
        "one_causal_mechanism_statement": "reword one sentence in the tie-break table body",
        "expected_effect": "pure-analysis prompts get an explicit Analytics route",
        "affected_eval_families": ["routing"],
        "possible_downside": "could over-route borderline strategy questions to Analytics",
        "required_checks": ["routing regression family", "handoff regression family"],
        "rollback": "revert the single-line change in the tie-break table body",
        "confidence": "medium",
        "limitations": "single wording change; effect size unknown pre-experiment",
    }
    prop.update(overrides)
    return prop


def test_rejected_attribution_blocks_mutation_proposal():
    m = _manifest()
    rec = _field_record(attribution_status="rejected", repair_eligibility="ineligible")
    out = fi.run_researcher(
        failure_record=rec, context={"budget_remaining": 5, "mutable_protected_manifest": {}},
        contract=fi.ResearcherContract.load(CONTRACT_PATH),
        model=fi.FakeResearcherModel(json.dumps(_base_proposal("x"))),
        manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(), proposal_schema=_proposal_schema(),
        experiment_id="exp-1",
    )
    assert out.status == "rejected"
    assert any("rejected" in f for f in out.findings)


def test_incomplete_proposal_after_retry_is_researcher_failure():
    m = _manifest()
    out = fi.run_researcher(
        failure_record=_field_record(attribution_status="supported", repair_eligibility="proposal_eligible"),
        context={"budget_remaining": 5, "mutable_protected_manifest": {}},
        contract=fi.ResearcherContract.load(CONTRACT_PATH),
        model=fi.FakeResearcherModel('{"proposal_id": "P-1"}'),  # missing required fields
        manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(), proposal_schema=_proposal_schema(),
        experiment_id="exp-1",
    )
    assert out.status == "rejected"
    assert "Researcher failure" in out.limitations


def test_patch_hash_mismatch_is_rejected_by_preflight():
    m = _manifest()
    prop = _base_proposal("some diff text")
    prop["patch_hash"] = "0" * 64
    out = fi.deterministic_preflight(
        proposal=prop, manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(),
        proposal_schema=_proposal_schema(),
    )
    assert out.status == "rejected"
    assert any("patch_hash" in f for f in out.findings)


def test_missing_rollback_or_regression_families_is_rejected():
    m = _manifest()
    prop = _base_proposal("d", rollback="", affected_eval_families=[])
    # schema will already flag; preflight must also reject
    out = fi.deterministic_preflight(
        proposal=prop, manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(),
        proposal_schema=_proposal_schema(),
    )
    assert out.status == "rejected"


def test_multi_file_or_nonapplying_patch_is_rejected():
    m = _manifest()
    two_file_patch = (
        "diff --git a/A.md b/A.md\n--- a/A.md\n+++ b/A.md\n@@ -1 +1,2 @@\n x\n+y\n"
        "diff --git a/B.md b/B.md\n--- a/B.md\n+++ b/B.md\n@@ -1 +1,2 @@\n x\n+y\n"
    )
    out = fi.deterministic_preflight(
        proposal=_base_proposal(two_file_patch), manifest=m, repo_root=REPO_ROOT,
        baseline_revision=_head(), proposal_schema=_proposal_schema(),
    )
    assert out.status == "rejected"


def test_valid_in_anchor_patch_reaches_ready_for_experiment():
    m = _manifest()
    surface = next(s for s in m["mutable_surfaces"] if s["surface_id"] == "MUT-HANDOFF-PROJECT-ADDITIONS")
    target_rel = surface["path"]
    # Build a real one-line, in-anchor patch against HEAD via an isolated worktree.
    import tempfile

    work = Path(tempfile.mkdtemp(prefix="mk-patch-"))
    subprocess.run(["git", "worktree", "add", "--detach", str(work), _head()], cwd=REPO_ROOT, check=True, capture_output=True)
    try:
        f = work / target_rel
        lines = f.read_text(encoding="utf-8").splitlines(keepends=True)
        idx = next(i for i, ln in enumerate(lines) if ln.strip() == "## Project-Specific Additions")
        lines.insert(idx + 1, "<!-- autoresearch preflight probe -->\n")
        f.write_text("".join(lines), encoding="utf-8")
        patch = subprocess.run(["git", "diff"], cwd=work, capture_output=True, text=True).stdout
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(work)], cwd=REPO_ROOT, capture_output=True)

    import hashlib

    prop = _base_proposal(
        patch,
        target_file=target_rel,
        target_anchor="## Project-Specific Additions",
        mutation_class="wording_clarification",
        patch_hash=hashlib.sha256(patch.encode()).hexdigest(),
    )
    out = fi.deterministic_preflight(
        proposal=prop, manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(),
        proposal_schema=_proposal_schema(),
    )
    assert out.status == "ready_for_experiment", out.findings
    assert out.proposal is not None


def test_preflight_does_not_change_active_repo_state():
    m = _manifest()
    before = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    fi.deterministic_preflight(
        proposal=_base_proposal("bad"), manifest=m, repo_root=REPO_ROOT, baseline_revision=_head(),
        proposal_schema=_proposal_schema(),
    )
    after = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after


def test_test_double_proposal_is_labelled_calibration_not_live():
    model = fi.FakeResearcherModel(json.dumps(_base_proposal("x")))
    assert model.provenance == "calibration_fixture"


def test_browser_researcher_model_shares_413_budget():
    import importlib

    lba_spec = importlib.util.spec_from_file_location(
        "autoresearch_live_browser_adapter", REPO_ROOT / "scripts" / "autoresearch_live_browser_adapter.py"
    )
    lba = importlib.util.module_from_spec(lba_spec)
    sys.modules[lba_spec.name] = lba
    lba_spec.loader.exec_module(lba)

    policy = lba.TransportPolicy(
        transport_id="playwright_mcp", transport_version="v", transport_mode="dedicated_persistent_profile",
        target_product="openai_chatgpt_ui", target_url_prefix="https://chatgpt.com/",
        session_policy="fresh_conversation", browser_session_ref="p-1",
    )
    budget = lba.BudgetState(max_provider_calls=40, max_cost_amount=0.0, max_cost_currency="USD")
    model = fi.BrowserResearcherModel(
        policy=policy, budget=budget, transport=lba.FakeBrowserTransport(scripted_response='{"proposal_id":"P"}'),
        context_id="0123456789abcdef", context_hash="a" * 64,
        authority_evidence_ref="docs/evidence/AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md#owner-authorization",
    )
    cap = model.propose("prompt", invocation_id="exp-1:researcher:0")
    assert cap.termination_status == "completed"
    assert budget.calls_used == 1
    assert model.provenance == "live"
