from __future__ import annotations

from pathlib import Path, PurePosixPath
import re


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/auto-merge.yml"
CODEOWNERS = ROOT / ".github/CODEOWNERS"


def auto_allowlist() -> re.Pattern[str]:
    text = WORKFLOW.read_text(encoding="utf-8")
    match = re.search(r"^\s+auto_allowed='([^']+)'$", text, flags=re.MULTILINE)
    assert match, "auto-merge workflow must declare an explicit auto allowlist"
    return re.compile(match.group(1))


def codeowner_patterns() -> list[str]:
    patterns = []
    for line in CODEOWNERS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            patterns.append(line.split()[0])
    return patterns


def is_codeowner_protected(path: str, patterns: list[str]) -> bool:
    relative = PurePosixPath(path)
    for pattern in patterns:
        normalized = pattern.lstrip("/")
        if pattern.endswith("/") and path.startswith(normalized):
            return True
        if "*" in normalized and relative.match(normalized):
            return True
        if path == normalized or path.endswith("/" + normalized):
            return True
    return False


def test_auto_allowlist_never_overlaps_codeowners_protection() -> None:
    allowlist = auto_allowlist()
    patterns = codeowner_patterns()
    tracked = (ROOT / ".git").exists()
    assert tracked
    paths = [line for line in __import__("subprocess").check_output(
        ["git", "ls-files"], cwd=ROOT, text=True
    ).splitlines() if line]
    protected = [path for path in paths if is_codeowner_protected(path, patterns)]
    assert protected
    overlaps = [path for path in protected if allowlist.fullmatch(path)]
    assert overlaps == []


def test_representative_governance_paths_require_owner_review() -> None:
    allowlist = auto_allowlist()
    protected_paths = [
        "schemas/autonomous_execution_record.schema.json",
        "SMOKE_QA_RESULTS.md",
        "CROSS_PROJECT_SMOKE_QA_RESULTS.md",
        "PILOT_CASES.md",
        "PILOT_RESULTS_TEMPLATE.md",
        "AUTONOMOUS_EXECUTION_STANDARD.md",
        "AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md",
        "ROUTING_RULES.md",
        "HANDOFF_STYLE_STANDARD.md",
        "PROMPT_QA_FACTORY.md",
        "PROJECT_CAPABILITIES.yaml",
        "knowledge_bundle_manifest.json",
        "CHATGPT_PROJECT_SYNC_CHECKLIST.md",
        "ChatGPT/[Inbox Router]/Knowledge/HANDOFF_PROTOCOL.md",
    ]
    assert all(not allowlist.fullmatch(path) for path in protected_paths)
    patterns = codeowner_patterns()
    assert is_codeowner_protected("ChatGPT/[Inbox Router]/Knowledge/HANDOFF_PROTOCOL.md", patterns)
