# Codex App Intake Gate

## Purpose

Prevent vague or unsafe Codex tasks.

## Required fields before implementation

A Codex task should include:

- objective;
- context;
- repo;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- acceptance criteria;
- tests / smoke checks;
- rollback plan.

## Small-task exception

For small, local, reversible tasks, Codex may proceed with safe assumptions if:

- target files are obvious;
- change is reversible;
- no hard blocker is present;
- acceptance can be verified with a meaningful check.

Tasks produced by `ChatGPT/[Codex]` should also be validated against `CODEX_APP_TASK_PACKAGE_CONTRACT.md` before implementation.

## Blocker response

```text
blocked_reason:
missing_input:
risk_if_continue:
safe_next_step:
files_inspected:
```

## Bad task examples

- "Improve the project."
- "Make it production-ready."
- "Refactor everything."
- "Add automation."
- "Use AI to make it better."
- "Fix it somehow."
