# Codex App Task Package Contract

## Purpose

Define the required interface between `ChatGPT/[Codex]` and the Codex App, Codex Web, Codex CLI, or IDE executor layer.

## Producer and executor

- Producer: `ChatGPT/[Codex]`
- Executor: `Codex APP / Codex App / Codex Web / Codex CLI / IDE`

## Goal Mode boundary

This contract applies to the executor-ready package, not to Sergey’s initial request.

For normal bounded repo work, a task may reference `Goal Mode Contract` from
`GOAL_MODE.md` instead of repeating the full autonomy, execution, forbidden,
reporting, PR, no-auto-merge, and no-deletion-without-quarantine rules.
Codex APP may define executor package shape and checks, but it must not replace
the canonical autonomy, hard-blocker, or reporting standards.

Sergey may start with a broad goal in ChatGPT. Goal Mode is build-first: the producer layer — `ChatGPT/[Codex]`, `[LLM]`, or a Goal Mode GitHub issue — should help Codex inspect relevant files, infer bounded safe scope, create or use a non-main branch, implement the smallest useful working version, run checks, fix in-scope failures when safe, and report evidence.

`Codex APP` must preserve execution safety. Before editing, it should identify the objective, repo, branch, allowed scope, forbidden actions, checks, rollback, and final response format.

For small, local, reversible tasks, `Codex APP` may safely infer missing fields and report what was inferred. Do not convert soft uncertainty into a roadmap, epic, child issue tree, or approval package. For unclear or high-risk work, stop on the canonical Codex hard blockers from `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`.

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

Refuse or block execution on the canonical Codex hard blockers from
`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`.

This contract adds executor-package blockers only when they prevent safe
execution:

- scope is unclear;
- allowed files are missing;
- acceptance criteria conflict;
- no meaningful validation path;
- the local path is missing and no safe local repository can be identified.

## Output format

The executor must use the canonical Codex final report schema from
`ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`. Use `none` for
unavailable PR fields when the task does not request GitHub sync.
Mode-specific reports may be shorter, but they must not conflict with this
schema.

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

Before execution, inspect the task package and confirm:

- objective is present or safely inferable;
- repository/local path is present or safely inferable;
- branch expectation is clear when GitHub sync is required;
- acceptance criteria are present or safely inferable;
- rollback or safe restore path is present;
- missing fields are logged when inferred.

For markdown task packages, inspect the text and confirm the required field headings are present. If a field is absent, continue only for small, local, reversible tasks where the missing field can be safely inferred and logged.

For ultra-long markdown task packages, also confirm the headings `Batch plan`, `Checkpoint policy`, `Safe retry policy`, and `Final response format` are present.

Take one task package produced by `ChatGPT/[Codex]` and verify that `Codex APP` can classify mode, allowed files, forbidden actions, acceptance criteria, checks, rollback, batch plan, and checkpoint policy before implementation.
