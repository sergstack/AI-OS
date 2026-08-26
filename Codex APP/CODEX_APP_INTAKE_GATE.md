# Codex App Intake Gate

## Purpose

Prevent vague or unsafe Codex tasks.

## Full intake fields

A full intake package includes:

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

## Normal Goal Mode default

For normal Goal Mode, Codex infers and logs the smallest conservative,
reversible scope when the answer is safely inferable. It records inferred
execution mode, risk mode, assumptions, allowed files, checks, and rollback;
it does not request a user round-trip merely to fill intake fields.

The full intake package remains required for `risk_mode: full`, an explicit
strict or advanced task package, and any existing hard-gated mode that already
requires a complete package. For other local, reversible tasks, proceed when:

- target files are obvious;
- change is reversible;
- no hard blocker is present;
- acceptance can be verified with a meaningful check.

Tasks produced by `ChatGPT/[Codex]` that are strict, advanced, or hard-gated
should also be validated against `CODEX_APP_TASK_PACKAGE_CONTRACT.md` before
implementation.

## Blocker response

Use this only for canonical hard blockers or genuinely unsafe/conflicting
scope, not for safely inferable normal Goal Mode intake fields.

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
