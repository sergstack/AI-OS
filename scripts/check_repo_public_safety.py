#!/usr/bin/env python3
"""Run public repository safety checks for AI-OS docs."""

from pathlib import Path
import re
import sys

from check_project_instructions_length import main as check_project_instructions


SKIP_DIRS = {".git", "__pycache__"}
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".txt", ".toml", ".gitignore"}
FORBIDDEN_DIR_NAMES = {
    "embeddings",
    "embedding",
    "vector_db",
    "vectordb",
    "vector-db",
    "faiss",
    "chroma",
}
FORBIDDEN_FILE_SUFFIXES = {".env", ".log", ".tmp", ".sqlite", ".sqlite3", ".db"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[opsu]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]
LOCAL_PATH_PATTERN = re.compile(
    r"(?:(?<![A-Za-z0-9:])/(?:Users|home|Volumes)/[^\s)`'\"]+|[A-Za-z]:\\Users\\[^\s)`'\"]+)"
)


def iter_paths(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def is_text_file(path: Path) -> bool:
    return path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES


def main() -> int:
    root = Path.cwd()
    failures = []

    for path in iter_paths(root):
        rel = str(path.relative_to(root))
        lower_parts = {part.lower() for part in path.parts}

        if path.is_dir() and lower_parts & FORBIDDEN_DIR_NAMES:
            failures.append(f"Forbidden vector/embedding directory: {rel}")
            continue

        if path.is_file():
            if path.name == ".env" or path.suffix.lower() in FORBIDDEN_FILE_SUFFIXES:
                failures.append(f"Forbidden env/log/temp/runtime artifact: {rel}")

            if path.suffix.lower() == ".zip" and "Knowledge" in path.parts:
                failures.append(f"Forbidden zip archive as Knowledge source: {rel}")

            if not is_text_file(path):
                continue

            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue

            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    failures.append(f"Possible secret/token pattern: {rel}")
                    break

            for match in LOCAL_PATH_PATTERN.finditer(text):
                failures.append(f"Absolute local path reference: {rel}: {match.group(0)}")

    length_exit = check_project_instructions()
    if length_exit:
        failures.append("One or more PROJECT_INSTRUCTIONS.md files exceed 8000 characters")

    if failures:
        print("Public safety check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public safety check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
