"""Structural completeness tests for the AIOS AutoResearch v0.1 parent final
QA document (issue #398, parent #388). Same discipline as #394/#395/#396's
contract-document tests: prove the document actually contains what it
claims to, not just that it exists.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "docs" / "evidence" / "AUTORESEARCH_PARENT_FINAL_QA_2026-09-03.md"

REQUIRED_SECTIONS = [
    "## 1. Child / dependency and evidence-completeness matrix",
    "## 2. Finalist selection basis",
    "## 3. Holdout isolation/access evidence",
    "## 4. Frozen contract and configuration hashes",
    "## 5. Deterministic hard-gate results",
    "## 6. Blind/reversed-order semantic Judge findings",
    "## 7. Analytics holdout and uncertainty results",
    "## 8. Validation-to-holdout generalization comparison",
    "## 9. Hidden regressions and benchmark-exploitation review",
    "## 10. Harness-level falsification assessment",
    "## 11. Complexity/cost versus manual bounded-review comparison",
    "## 12. Residual risks and rollback readiness",
    "## 13. Recommendation",
    "## 14. Parent gate",
]

VALID_RECOMMENDATIONS = {
    "promote_candidate_to_separate_implementation_issue",
    "revise_and_recalibrate",
    "simplify_to_manual_regression_suite",
    "stop_autoresearch",
    "open_new_parent_for_broader_search",
}

VALID_PARENT_GATES = {"pass", "revise", "blocked"}


def _text() -> str:
    return DOC.read_text(encoding="utf-8")


def test_document_exists():
    assert DOC.is_file()


def test_all_14_required_sections_present():
    text = _text()
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    assert missing == [], f"parent final QA doc is missing required sections: {missing}"


def test_recommendation_is_exactly_one_valid_literal():
    text = _text()
    found = [r for r in VALID_RECOMMENDATIONS if f"```text\n{r}\n```" in text]
    assert len(found) == 1, f"expected exactly one recommendation literal in a fenced block, found {found}"


def test_parent_gate_is_a_valid_literal():
    text = _text()
    found = [g for g in VALID_PARENT_GATES if f"```text\n{g}\n```" in text]
    assert len(found) == 1, f"expected exactly one parent gate literal in a fenced block, found {found}"


def test_all_ten_child_issues_are_referenced():
    text = _text()
    for n in range(389, 399):
        assert f"#{n}" in text, f"child issue #{n} not referenced in the completeness matrix"


def test_document_does_not_claim_holdout_was_accessed():
    text = _text()
    assert "not_applicable" in text.lower() or "Not applicable" in text
    # explicit, repeated honesty markers rather than a silent omission
    assert text.count("Not applicable") + text.count("**Not applicable") >= 3


def test_document_does_not_claim_a_live_judge_ran():
    text = _text()
    assert "NOT_RUN" in text


def test_document_states_zero_finalists_explicitly():
    text = _text()
    assert "zero finalists" in text.lower() or "No finalists were selected" in text


def test_document_reconciles_original_parent_acceptance_criteria():
    text = _text()
    assert "Parent #388 acceptance criteria — reconciled individually" in text
    # spot-check a handful of the literal criteria from issue #388's own text
    for phrase in (
        "distinguishes useful, harmful, and inconclusive candidates",
        "has no authority or promotion side effect",
        "Append-only history rejects mutation, deletion, or reordering",
        "runtime service, database, dashboard, or generic autonomous-agent layer",
    ):
        assert phrase in text, f"original parent acceptance criterion not reconciled verbatim: {phrase!r}"
