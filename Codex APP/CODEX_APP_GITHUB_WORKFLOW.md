# Codex App GitHub Workflow

## Purpose

Define safe branch / PR workflow for Codex.

## Branch naming

| Branch prefix | Use |
|---|---|
| `docs/...` | documentation and setup files |
| `fix/...` | bugfix |
| `feat/...` | feature |
| `qa/...` | tests / smoke checks |
| `chore/...` | repo hygiene |
| `refactor/...` | scoped refactor only |

## Rules

- Never work directly on `main` unless explicitly instructed.
- Prefer small branches.
- One branch = one bounded issue, task, or Goal Mode change.
- PR must explain tests, risks and rollback.
- Do not mix docs, code, data schema and business logic changes in one PR.

## PR template

```md
## Summary

## Changed files

## Checks run

## Acceptance criteria

## Risks / limitations

## Rollback

## Acceptance status
pass / fail / blocked
```

## Merge rule

Codex APP must not decide mergeability or merge PRs by itself.

Repository merge is allowed only through:

- explicit owner action; or
- the active GitHub merge gate for Tier 0/1 docs PRs after required checks pass.

Before a PR is considered ready for either path:

- expected files changed;
- no forbidden files touched;
- checks are reported;
- acceptance status is clear.

Tier 2 protected paths listed in `.github/CODEOWNERS` require owner review.
