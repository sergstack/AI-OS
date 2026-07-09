#!/usr/bin/env python3
"""Check that Knowledge directories stay fully listed in their index files."""

from __future__ import annotations

from pathlib import Path


CHECKS = [
    (
        "ChatGPT/[AI OS]/Knowledge",
        ["ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md"],
    ),
    (
        "ChatGPT/[Analytics]/Knowledge",
        ["ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md"],
    ),
    (
        "ChatGPT/[Codex]/Knowledge",
        ["ChatGPT/[Codex]/Knowledge/INDEX.md"],
    ),
    (
        "ChatGPT/[Inbox Router]/Knowledge",
        [
            "ChatGPT/[Inbox Router]/Knowledge/INDEX.md",
            "ChatGPT/[Inbox Router]/Knowledge/INBOX_ROUTER_FILES_INDEX.md",
        ],
    ),
    (
        "ChatGPT/[LLM]/Knowledge",
        [
            "ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md",
            "ChatGPT/[LLM]/README.md",
        ],
    ),
    (
        "ChatGPT/[Thinking]/Knowledge",
        ["ChatGPT/[Thinking]/Knowledge/INDEX.md"],
    ),
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def missing_from_index(root: Path, knowledge_dir: str, index_path: str) -> list[str]:
    directory = root / knowledge_dir
    index_file = root / index_path
    if not directory.is_dir():
        return [f"missing knowledge directory: {knowledge_dir}"]
    if not index_file.is_file():
        return [f"missing index file: {index_path}"]

    index_text = index_file.read_text(encoding="utf-8")
    failures: list[str] = []
    for entry in sorted(directory.glob("*.md")):
        if entry.resolve() == index_file.resolve():
            continue
        if entry.name not in index_text:
            failures.append(f"{index_path} does not list {knowledge_dir}/{entry.name}")
    return failures


def main() -> int:
    root = repo_root()
    failures: list[str] = []
    checked = 0
    for knowledge_dir, indexes in CHECKS:
        for index_path in indexes:
            checked += 1
            failures.extend(missing_from_index(root, knowledge_dir, index_path))

    for failure in failures:
        print(f"FAIL {failure}")
    print(f"Index coverage pairs checked: {checked}")
    print(f"Failed: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
