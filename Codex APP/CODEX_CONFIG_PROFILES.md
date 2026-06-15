# Codex Config Profiles

## Purpose

Document recommended non-secret Codex execution profiles. These are guidance profiles, not executable credentials or machine-specific configuration.

## safe-docs

- Intended use: documentation-only edits, repo hygiene, task templates, checklists.
- Recommended reasoning effort: low to medium.
- Approval behavior: continue on local reversible changes; ask for destructive actions or GitHub writes unless the task explicitly requests them.
- Permissions and sandbox expectation: read/write access limited to allowed repository files.
- Forbidden use: production code changes, secrets, migrations, deployments, generated data, raw KB edits outside scope.

## safe-code

- Intended use: scoped code fixes with clear files, tests, and rollback.
- Recommended reasoning effort: medium.
- Approval behavior: continue on local reversible implementation decisions; stop for public APIs, schemas, auth, migrations, or production behavior changes.
- Permissions and sandbox expectation: repository read/write with relevant test commands.
- Forbidden use: broad refactors, dependency additions, runtime infrastructure, production deploys, security-control changes without explicit approval.

## long-run-local

- Intended use: longer local tasks with complete task package, allowed files, smoke checks, and rollback.
- Recommended reasoning effort: medium to high.
- Approval behavior: do not ask unless a hard blocker appears; retry once on safe local failures.
- Permissions and sandbox expectation: local repository access, branch workflow, and non-destructive checks.
- Forbidden use: secrets handling, destructive filesystem operations, production mutations, governed KB changes outside scope, business logic or output contract changes without approval.

## ultra-long-local

- Intended use: multi-batch local implementation or documentation work with explicit task package, branch, allowed files, batch plan, checkpoints, smoke checks, and rollback.
- Recommended reasoning effort: high for planning and review; medium for repetitive batch execution.
- Approval behavior: continue through safe batches without asking; stop only on hard blockers; retry failed checks once when the fix is local, reversible, and inside allowed files.
- Permissions and sandbox expectation: local repository access, scoped branch workflow, non-destructive checks, optional checkpoint file only when support files are allowed.
- Required protocol: `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md`.
- Required template: `templates/ULTRA_LONG_TASK_PACKAGE.md` or equivalent complete task package.
- Forbidden use: secrets handling, destructive filesystem operations, production/runtime/deploy/migration actions, governed KB changes outside scope, business logic or output contract changes without approval, uncontrolled multi-agent work, autonomous retrieval, internet-enabled execution.

## review-only

- Intended use: diff review, task package review, risk assessment, acceptance checks.
- Recommended reasoning effort: low to medium.
- Approval behavior: do not edit files or run write operations.
- Permissions and sandbox expectation: read-only repository access.
- Forbidden use: implementation, staging, committing, pushing, merging, or changing files.
