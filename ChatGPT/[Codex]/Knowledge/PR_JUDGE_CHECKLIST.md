# PR Judge Checklist

## Purpose

Review a PR for goal fit, scope control, test evidence, and merge readiness.

## Inputs

- PR link or diff;
- original goal or issue;
- changed files;
- checks run;
- known risks and rollback.

## Checklist

- [ ] Goal matches the requested change.
- [ ] Changed files are inside expected scope.
- [ ] No unrelated refactor or formatting churn.
- [ ] No forbidden files, secrets, `.env`, credentials, raw dumps, or runtime artifacts.
- [ ] No unapproved formulas, schemas, metric definitions, column names, output contracts, APIs, or business logic changes.
- [ ] Tests/checks are appropriate for the risk.
- [ ] Docs-only changes use lightweight smoke/repo checks.
- [ ] Code/script/pipeline changes use test-first or explain why an existing focused test was enough.
- [ ] Risks and limitations are visible.
- [ ] Rollback is clear.
- [ ] Acceptance status is honest.

## Verdicts

```text
pass
revise
blocked
```

Use `pass` only when the PR is ready for owner review or merge decision.

Use `revise` when fixes are local, clear, and bounded.

Use `blocked` when missing data, unsafe scope, failing checks, secrets, production risk, or unclear acceptance prevents safe progress.

## Output

```text
Verdict:
Required fixes:
Risks:
Checks reviewed:
Merge readiness:
```

Do not merge automatically. An owner merge decision is required. For this
personal repository, explicit owner self-review counts as human-owned review.
