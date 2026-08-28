# Contributing to AI-OS

AI-OS uses issue-driven, owner-reviewed changes. Public visibility does not
grant a license to reuse repository content; see `docs/rights_posture.md`.

## Before You Start

1. Open a Goal issue for broad, outcome-oriented work or a Codex Task issue for
   strict, already-scoped work.
2. Agree on the intended outcome, allowed scope, acceptance criteria, and
   checks.
3. Create a non-`main` branch. Keep the change minimal and reversible.

Do not include credentials, local configuration, raw dumps, logs, runtime
artifacts, embeddings, vector databases, or machine-specific absolute paths.

## Validate the Change

Run the repository checks before opening a pull request:

```bash
python3 scripts/sync_aios.py
python3 -m pytest tests/ -rA
```

If a check cannot run, document the blocker instead of reporting it as passed.

## Pull Requests

Use the pull request template and include:

- the linked issue and a concise summary;
- the exact files changed;
- checks run and their results;
- assumptions, residual risks, and rollback steps;
- acceptance and merge-gate status.

Protected files require owner review. Pull requests must follow the canonical
merge policy in `GOAL_MODE.md`; automation and contributors must not bypass the
human approval gates.
