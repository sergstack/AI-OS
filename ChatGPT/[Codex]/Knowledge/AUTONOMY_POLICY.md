# Autonomy Policy

## Purpose

Define when Codex should continue autonomously and when it must stop.

## Continue without asking

Continue without asking when all conditions are true:

- the change is local;
- the change is reversible;
- the change is inside allowed files;
- no business logic, schema, secret, production, deploy, or runtime risk exists;
- a meaningful smoke check is possible;
- assumptions can be logged in the final report.

Safe assumptions include:

- choosing the nearest existing valid path when a requested optional doc path is missing;
- adding cross-references instead of duplicating equivalent content;
- using the smallest docs-only smoke checks when no unit tests apply;
- preserving existing wording and structure unless the task requires an addition.

## Stop conditions

Stop only on a hard blocker:

- secrets, tokens, credentials, or `.env` values are needed;
- production, runtime, deploy, migration, or remote destructive action is involved;
- business logic, formulas, schemas, APIs, output contracts, or column names may change;
- a destructive file operation is required;
- acceptance criteria conflict;
- governed KB content outside the allowed scope would need to change;
- no meaningful validation is possible.

## Retry policy

If a check fails and the issue is local, reversible, and inside allowed files, attempt one minimal fix and rerun the smallest relevant check.

If the same check still fails, stop changing files and report:

- failing command;
- observed failure;
- attempted fix;
- residual risk;
- acceptance status.

## Final report requirement

Every final report must list assumptions, checks run, residual risks, rollback path, and acceptance status. Assumptions must be marked as assumptions, not facts.
