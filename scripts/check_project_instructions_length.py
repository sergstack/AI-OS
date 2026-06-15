#!/usr/bin/env python3
"""Validate ChatGPT Project Instructions length."""

from pathlib import Path
import sys

MAX_PROJECT_INSTRUCTIONS_CHARS = 8000


def iter_project_instruction_files(root: Path):
    for path in sorted(root.rglob("PROJECT_INSTRUCTIONS.md")):
        if ".git" in path.parts:
            continue
        yield path


def main() -> int:
    root = Path.cwd()
    passed = 0
    failed = 0

    for path in iter_project_instruction_files(root):
        text = path.read_text(encoding="utf-8")
        count = len(text)
        rel = path.relative_to(root)
        if count <= MAX_PROJECT_INSTRUCTIONS_CHARS:
            passed += 1
            print(f"PASS {rel} chars={count} limit={MAX_PROJECT_INSTRUCTIONS_CHARS}")
        else:
            failed += 1
            over_by = count - MAX_PROJECT_INSTRUCTIONS_CHARS
            print(
                f"FAIL {rel} chars={count} "
                f"limit={MAX_PROJECT_INSTRUCTIONS_CHARS} over_by={over_by}"
            )

    total = passed + failed
    print(f"Checked PROJECT_INSTRUCTIONS.md files: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Limit: {MAX_PROJECT_INSTRUCTIONS_CHARS} characters")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
