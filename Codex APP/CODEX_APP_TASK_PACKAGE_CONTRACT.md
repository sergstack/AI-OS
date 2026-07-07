# Codex App Task Package Contract

## Purpose

Define the required interface between `ChatGPT/[Codex]` and the Codex App, Codex Web, Codex CLI, or IDE executor layer.

## Producer and executor

- Producer: `ChatGPT/[Codex]`
- Executor: `Codex APP / Codex App / Codex Web / Codex CLI / IDE`

## Goal Mode boundary

This contract applies to the executor-ready package, not to Sergey’s initial request.

Sergey may start with a broad goal in ChatGPT. Goal Mode is build-first: the producer layer — `ChatGPT/[Codex]`, `[LLM]`, or a Goal Mode GitHub issue — should help Codex inspect relevant files, infer bounded safe scope, create or use a non-main branch, implement the smallest useful working version, run checks, fix in-scope failures when safe, and report evidence.

`Codex APP` must preserve execution safety. Before editing, it should confirm the objective, repo, branch, allowed scope, forbidden actions, checks, rollback, and final response format.

For small, local, reversible tasks, `Codex APP` may safely infer missing fields and report what was inferred. Do not convert soft uncertainty into a roadmap, epic, child issue tree, or approval package. For unclear, high-risk, production, destructive, secret-related, schema/metric/formula/provider-routing/output-contract, or governed-KB tasks, stop and report a blocker.

Provider/API safeguards block real external execution, not local scaffolding. The executor may implement provider/client code, dry-run or no-network paths, preflight checks, configuration variable name checks, and tests with mock values without additional approval. It must not print, log, expose, summarize, or commit sensitive values; commit local credential files; expose raw provider responses; run real provider/API calls without explicit bounded approval; or treat local configuration presence as approval.

For approved real provider/API execution, report redacted evidence only: command name, route/client, sample size, status code or success/failure class, sanitized response shape, redacted error summary, and safe artifact paths only.

## Required input fields

Every executor-ready task package should include or safely infer:

- `objective`
- `context`
- `repo`
- `local path`
- `branch`
- `files to inspect`
- `files allowed to modify`
- `forbidden actions`
- `expected outputs`
- `acceptance criteria`
- `tests / smoke checks`
- `rollback plan`
- `final response format`

## Local + GitHub task fields

For local + GitHub tasks, also include:

- local repository path;
- target branch;
- expected PR behavior;
- branch cleanup expectation.

## Ultra-long task fields

For ultra-long tasks, also include:

- autonomy profile, usually `ultra-long-local`;
- operating mode;
- batch plan;
- checkpoint policy;
- support files allowed: yes / no;
- safe retry rule;
- context reload rule;
- next safe action format.

Use `templates/ULTRA_LONG_TASK_PACKAGE.md` when preparing these tasks.

## Refuse or block conditions

Refuse or block execution when:

- scope is unclear;
- allowed files are missing;
- secrets, tokens, credentials, or `.env` values are required;
- production deploy, runtime mutation, migration, or destructive filesystem action is required without explicit approval;
- business logic, formulas, schemas, APIs, output contracts, or column names may change without explicit approval;
- governed KB content outside the allowed scope must change;
- acceptance criteria conflict;
- no meaningful validation is possible;
- the local path is missing and no safe local repository can be identified.

## Output format

The executor must report:

```text
Summary:
Files changed:
Local path:
Branch:
Commit:
PR URL:
Tests/checks run:
Assumptions:
Risks/limitations:
Rollback:
Acceptance status:
Next step:
```

Use `none` for unavailable commit or PR fields when the task does not request GitHub sync.

## Ultra-long output format

For ultra-long tasks, the executor must also report:

```text
Mode:
Autonomy profile:
Batches completed:
Current checkpoint:
Remaining batches:
Next safe action:
```

Do not claim `pass` unless checks were actually run and observed.

## Smoke test

Before execution, verify:

```bash
test -n "$objective"
test -n "$repo"
test -n "$local_path"
test -n "$branch"
test -n "$acceptance_criteria"
test -n "$rollback_plan"
```

For markdown task packages, inspect the text and confirm the required field headings are present. If a field is absent, continue only for small, local, reversible tasks where the missing field can be safely inferred and logged.

For ultra-long markdown task packages, also confirm the headings `Batch plan`, `Checkpoint policy`, `Safe retry policy`, and `Final response format` are present.

Take one task package produced by `ChatGPT/[Codex]` and verify that `Codex APP` can classify mode, allowed files, forbidden actions, acceptance criteria, checks, rollback, batch plan, and checkpoint policy before implementation.
