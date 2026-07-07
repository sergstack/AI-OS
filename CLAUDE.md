# CLAUDE.md

Status: legacy/reference compatibility pointer.
Source of truth: `AGENTS.md`.
Upload: not uploaded to ChatGPT Project Knowledge bundles.

Use `AGENTS.md` as the source of truth for this repository.

This file is a lightweight compatibility pointer for Claude Code and other coding-agent surfaces. Do not duplicate the full policy here.

Key defaults:

- Goal Mode by default: build first, plan only when asked.
- Make minimal, reversible, verifiable changes.
- Do not commit to `main`.
- Do not merge automatically.
- Do not touch secrets, `.env`, runtime artifacts, production deploys, formulas, schemas, output contracts, metric definitions, or business logic without explicit approval.
- Run the smallest meaningful checks and report real results.

## Ask-less default

Safety lives in mechanics — non-main branch, small diffs, checks, PR review — not in pre-approval questions.

- Work on a non-main branch and show the result in a PR instead of asking permission first. A PR the user can close is safer and cheaper than a question the user must answer.
- Do not ask about reversible in-scope decisions. Make the safest assumption, continue, and list assumptions in the PR or final report.
- Ask only on hard blockers: secrets or credentials, production/deploy or destructive irreversible actions, spending money, publishing outside the repository, or an explicit approval gate from `AGENTS.md`.
- Prefer self-verification over questions: run the repository checks from `AGENTS.md` (`python3 scripts/check_*.py`) or task-specific tests before reporting, and treat a failing check as something to fix once, not something to ask about.
- Report honestly and compactly: what changed, what was checked with real results, what remains.
