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

For tiny docs-only tasks, Codex may proceed with safe assumptions if:

- target files are obvious;
- change is reversible;
- no governed KB or production code is touched;
- acceptance can be verified by grep or file check.

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
