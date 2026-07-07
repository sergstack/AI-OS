# Testing Workflow

## Test types

- unit tests;
- integration tests;
- contract tests;
- smoke tests;
- golden output regression;
- data quality checks;
- artifact validation.

## Steps

1. Identify risk.
2. Choose smallest useful test.
3. Run existing tests first if possible.
4. Add tests only where useful.
5. Report pass/fail/blocked.

## Docs-only fallback checks

If no unit tests exist for docs-only changes, run file-existence, grep, markdown consistency, and git diff checks.

Minimum generic fallback commands:

```bash
git status --short
git diff --stat
git diff --check
find <affected_dir> -name "*.md" -type f | sort
```

For the AI-OS repository, use the standard validation scripts in `scripts/`.

If `markdownlint` is available, run it against the affected markdown files. Do not install it just for a docs-only task unless the task explicitly asks.

## Smoke test command format

```bash
# example
pytest tests/
python scripts/validate_artifact_outputs.py
```

Use actual repo commands from the task package.
