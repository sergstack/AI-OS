#!/usr/bin/env python3
"""Check Codex-facing files do not require atomic task packages by default."""

from pathlib import Path
import re
import sys


SEARCH_PATTERNS = [
    re.compile(r"atomic task package", re.IGNORECASE),
    re.compile(r"strict task package", re.IGNORECASE),
    re.compile(r"only by atomic", re.IGNORECASE),
    re.compile(r"только по atomic", re.IGNORECASE),
    re.compile(r"атомарн", re.IGNORECASE),
]

FORBIDDEN_PATTERNS = [
    re.compile(r"only by atomic", re.IGNORECASE),
    re.compile(r"только по atomic", re.IGNORECASE),
]

ACCEPTABLE_CONTEXT_PATTERNS = [
    re.compile(r"goal mode", re.IGNORECASE),
    re.compile(r"default", re.IGNORECASE),
    re.compile(r"not (?:the )?default", re.IGNORECASE),
    re.compile(r"not (?:a )?required", re.IGNORECASE),
    re.compile(r"not require", re.IGNORECASE),
    re.compile(r"without (?:requiring|asking)", re.IGNORECASE),
    re.compile(r"high-risk", re.IGNORECASE),
    re.compile(r"already-scoped", re.IGNORECASE),
    re.compile(r"explicit", re.IGNORECASE),
    re.compile(r"reserved", re.IGNORECASE),
    re.compile(r"strict", re.IGNORECASE),
    re.compile(r"advanced", re.IGNORECASE),
]

TASK_PACKAGE_CONTEXT = re.compile(
    r"(task|package|тз|задан|пакет|handoff|scope|scoped)", re.IGNORECASE
)

CODEX_FACING_PATHS = [
    "AGENTS.md",
    "README.md",
    "GOAL_MODE.md",
    "GOAL_PACKS.md",
    "COMMAND_SURFACE.md",
    "CONTEXT_PACK_STANDARD.md",
    "ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md",
    "ChatGPT/[AI OS]/Knowledge",
    "ChatGPT/[AI OS]/Knowledge_Bundles",
    "ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md",
    "ChatGPT/[Codex]/Knowledge",
    "ChatGPT/[Codex]/Knowledge_Bundles",
    "ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md",
    "ChatGPT/[LLM]/Knowledge",
    "ChatGPT/[LLM]/Knowledge_Bundles",
    "Codex APP",
    "StreamDeck/README.md",
    "StreamDeck/active/v3.0/config/action_profiles.json",
    "StreamDeck/active/v3.0/prompts/prompt_registry.json",
]

TEXT_SUFFIXES = {".md", ".json", ".csv", ".txt"}


def iter_codex_facing_files(root: Path):
    seen = set()
    for rel in CODEX_FACING_PATHS:
        path = root / rel
        if not path.exists():
            continue
        paths = path.rglob("*") if path.is_dir() else [path]
        for candidate in paths:
            if not candidate.is_file() or candidate.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if ".git" in candidate.parts:
                continue
            if candidate in seen:
                continue
            seen.add(candidate)
            yield candidate


def matching_terms(line: str) -> list[str]:
    terms = []
    for pattern in SEARCH_PATTERNS:
        if pattern.search(line):
            terms.append(pattern.pattern)
    return terms


def is_forbidden(line: str) -> bool:
    return any(pattern.search(line) for pattern in FORBIDDEN_PATTERNS)


def is_acceptable(line: str, context: str) -> tuple[bool, str]:
    if re.search(r"атомарн", line, re.IGNORECASE) and not TASK_PACKAGE_CONTEXT.search(line):
        return True, "atomic change wording, not task-package default"

    if is_forbidden(line):
        return False, "forbidden atomic-only wording"

    if any(pattern.search(context) for pattern in ACCEPTABLE_CONTEXT_PATTERNS):
        return True, "context scopes task packages away from default Goal Mode"

    return False, "missing Goal Mode/default/high-risk/strict/explicit context"


def main() -> int:
    root = Path.cwd()
    occurrences = 0
    failures = 0

    for path in iter_codex_facing_files(root):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        rel = path.relative_to(root)
        for index, line in enumerate(lines, start=1):
            terms = matching_terms(line)
            if not terms:
                continue

            context_lines = lines[max(0, index - 2) : min(len(lines), index + 1)]
            context = "\n".join(context_lines)
            ok, reason = is_acceptable(line, context)
            occurrences += 1
            status = "PASS" if ok else "FAIL"
            print(f"{status} {rel}:{index}: {reason}: {line.strip()}")
            if not ok:
                failures += 1

    print(f"Codex Goal Mode atomic-default occurrences checked: {occurrences}")
    print(f"Failed: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
