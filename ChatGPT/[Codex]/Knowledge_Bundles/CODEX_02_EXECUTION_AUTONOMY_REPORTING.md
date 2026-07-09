# [Codex] — Execution Autonomy Reporting

## Purpose

Compact upload artifact for [Codex] covering execution autonomy reporting.

## Source files

- `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_LONG_RUN_PLAYBOOK.md`
- `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`
- `ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:66d87a0ecec0e9de39679d5ac40e38122191239edfde6c7262fe3fc9313a8641

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`

# Autonomy Policy
## Purpose
Define when Codex should continue autonomously and when it must stop.
For normal bounded repo work, use `Goal Mode Contract` in `GOAL_MODE.md` as the named reusable standard for autonomy, execution order, forbidden actions, reporting, PR/merge-gate posture, and no-deletion-without-quarantine rules.
## Continue without asking
- the change is local;
- the change is reversible;
- the change is inside allowed files;
- no business logic, schema, secret, production, deploy, or runtime risk exists;
- a meaningful smoke check is possible;
- assumptions can be logged in the final report.
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


## From: `ChatGPT/[Codex]/Knowledge/CODEX_LONG_RUN_PLAYBOOK.md`

# Codex Long-Run Playbook
## Purpose
## Cycle
```text
Inspect -> Plan -> Implement -> Test -> Retry once if safe -> Review -> Report
```
## Working rules
- Do not ask on reversible docs or configuration decisions inside allowed files.
- Use safe defaults from the task package and existing repository structure.
- Keep the diff small and trace every changed line to the task.
- Prefer updating existing files and cross-references over creating duplicate guidance.
- Do not widen scope to unrelated cleanup.
- Treat missing optional docs links as recoverable when a nearest valid path exists.
## Test and retry
If a check fails:
1. decide whether the failure is local, reversible, and inside allowed files;
2. attempt one minimal fix only when safe;
3. rerun the smallest relevant check;
4. if it still fails, stop and report diagnostics.
Do not retry when the issue involves secrets, production systems, migrations, destructive commands, governed KB content outside scope, or output contracts.
## Reporting
- changed files;
- commands and checks run;
- assumptions;
- risks or limitations;
- rollback path;
- acceptance status.
Use `pass`, `partial`, `fail`, or `blocked` honestly. Do not claim checks passed unless they were run and observed.


## From: `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`

# Codex Execution And Reporting Rules
## Execution modes
- inspect-only: изучи repo, верни files/entrypoints/risks/plan, не редактируй.
- implement: минимально измени allowed files, запусти checks.
- bugfix: reproduce/define failure -> root cause -> minimal patch -> regression check.
- refactor: зафиксируй текущее behavior -> minimal refactor -> regression/golden check.
- test/QA: выбери smallest useful test, запусти/добавь checks, верни pass/fail.
- data pipeline: проверь contracts, grain, raw/stage/marts, reconciliation, artifacts.
- release: acceptance, tests, release notes, rollback, residual risks.
## Planning
- scope;
- files to inspect/modify;
- assumptions;
- risks;
- tests to run.
## Parent / Child Issue Gate
If an issue references `Parent / Child Issue Gate Standard`, respect `Depends on` / child issue order, do not start a downstream child until its dependency is accepted or merged, normally use one PR per child issue, report blocked dependencies as gates, do not close the parent until final QA passes, and do not silently replace old contracts without a migration note or blocker.
## Existing Script Controlled Refactor
When using `Existing Script Controlled Refactor Standard`, report baseline, output contract, safety tests, before/after comparison, behavior changes, and acceptance status explicitly.
```text
Summary:
Branch:
Files inspected:
Files changed:
Baseline captured:
Output contract:
Safety tests:
Before/after comparison:
Behavior changes:
Checks run:
Risks:
Rollback:
PR:
Acceptance status:
```
## Testing
- unit / integration / contract / smoke / golden / data quality / artifact validation;
- build / type check / lint, если они есть и релевантны;
- repo-specific commands из README, package files или task package.
## Review
- diff соответствует scope;
- forbidden actions не выполнены;
- output contracts сохранены;
- tests/checks понятны;
- risks и assumptions названы;
- rollback/next step есть.
## Blocker format
```text
blocked_reason:
missing_input:
risk_if_continue:
safe_next_step:
files_inspected:
```
## Final response format
Canonical final report schema:
```text
Summary:
Branch:
Files inspected:
Files changed:
Commands run:
Test results:
Evidence / artifacts:
Assumptions:
Blockers:
Risks:
Rollback:
PR:
Acceptance status:
Merge / gate status:
```
Mode-specific reports may be shorter, but they must not conflict with this schema.


## From: `ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`

# Failure Modes
## Severity levels
### recoverable
- missing optional docs link;
- ambiguous wording in README;
- missing non-critical checklist item;
- no dedicated docs test command.
### needs_check
- changed instructions affect Codex behavior;
- changed file references;
- changed task contract wording;
- changed checklist acceptance language.
### hard_blocker
Stop when the issue creates governance, safety, or validation risk. Use the canonical hard-blocker list in `AUTONOMY_POLICY.md`; do not maintain a competing list here.
## Common failures
- Scope creep.
- Broad refactor instead of task.
- No tests.
- Business logic changed silently.
- Output schema changed silently.
- Secrets exposed.
- Sensitive values or raw provider responses exposed in repo files, PR bodies, logs, or Knowledge bundles.
- Real provider/API execution treated as approved only because local configuration exists.
- LLM narrative mixed with deterministic calculations.
- Validation deleted.
- Acceptance criteria missing.
- Rollback missing.
- Premature automation added.
## Response
If a failure mode appears:
1. classify it as `recoverable`, `needs_check`, or `hard_blocker`;
2. continue for `recoverable` issues and log the assumption;
3. inspect and validate before continuing for `needs_check` issues;
4. stop for `hard_blocker` issues and report blocker plus safe minimal next step.
