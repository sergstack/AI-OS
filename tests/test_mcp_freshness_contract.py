from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "ChatGPT/[AI OS]/Knowledge/SKILLS_HOOKS_MCP_DECISION_MATRIX.md"
GOLDEN_CASES = ROOT / "ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md"


def test_mcp_verification_has_bounded_freshness_and_reverify_gates():
    matrix = MATRIX.read_text(encoding="utf-8")
    golden_cases = GOLDEN_CASES.read_text(encoding="utf-8")

    assert "verified_revision_or_fingerprint:" in matrix
    assert "permissions_or_auth_scope:" in matrix
    assert "freshness_status: current | stale | unverifiable | not_applicable" in matrix
    assert "sets\nno arbitrary global time-to-live" in matrix
    assert "prior verification and approval\ndo not authorize it" in matrix
    assert "never installs,\nexecutes, promotes, or authorizes an MCP server automatically" in matrix

    for case_id in (
        "MCP-FRESHNESS-SAME-REVISION",
        "MCP-FRESHNESS-SCHEMA-DRIFT",
        "MCP-FRESHNESS-AUTH-EXPANSION",
        "MCP-FRESHNESS-UNKNOWN-IMPLEMENTATION",
    ):
        assert case_id in golden_cases
