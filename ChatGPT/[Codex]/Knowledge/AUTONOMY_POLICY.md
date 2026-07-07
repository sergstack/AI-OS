# Autonomy Policy

## Purpose

Define when Codex should continue autonomously and when it must stop.

For normal bounded repo work, use `Goal Mode Contract` in `GOAL_MODE.md` as the
named reusable standard for autonomy, execution order, forbidden actions,
reporting, PR review, no-auto-merge, and no-deletion-without-quarantine rules.

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

Canonical hard blockers. Stop and report a blocker when work requires or may cause:

- missing required approval for real provider/API execution;
- sensitive configuration value exposure risk;
- source workbook mutation or Safe Apply without approval;
- production/runtime/deploy/migration without explicit approval and rollback;
- destructive operations;
- schema, API, output contract, file format, or column order changes without approval;
- business logic, metrics, formulas, or financial controls without approval;
- governed KB change without required evidence/acceptance;
- conflicting acceptance criteria;
- no meaningful validation path;
- governance boundary violation.

## Provider/API safeguards

Sensitive configuration values are hard blockers for real provider/API execution, not for local implementation scaffolding.

Allowed without additional approval:

- implement provider/client code;
- implement dry-run and no-network execution paths;
- implement preflight checks;
- check whether required configuration variable names are present;
- check presence/non-empty status without printing values;
- add tests with mock or fake values;
- document required configuration variable names.

Requires explicit bounded approval:

- real provider/API calls;
- source mutation;
- Safe Apply;
- production/runtime/deploy actions;
- batch expansion beyond approved sample size;
- schema, metric, formula, provider-routing, or output-contract changes.

Never print, log, expose, summarize, or commit sensitive values. Never commit local configuration or machine-local credential files. Never expose raw provider responses in repo files, PR bodies, logs, or Knowledge bundles.

Local configuration presence is not approval. Approval must be explicit and bounded.

## Retry policy

If a check fails and the issue is local, reversible, and inside allowed files, attempt one minimal fix and rerun the smallest relevant check.

If the same check still fails, stop changing files and report:

- failing command;
- observed failure;
- attempted fix;
- residual risk;
- acceptance status.

## Final report requirement

Use the canonical final report schema in `EXECUTION_REPORTING_RULES.md`. Assumptions must be marked as assumptions, not facts.
