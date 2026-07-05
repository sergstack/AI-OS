# Goal Mode

Goal Mode is the default user-facing workflow for AI-OS and Codex.

## Flow

```text
GOAL -> route -> infer scope -> internal Codex execution package -> implement/check -> PR -> ChatGPT/Codex read GitHub for fresh state
```

## User Interface

The user gives a broad goal, not an atomic task package.

Router, AI OS, LLM, or Codex may turn that goal into a route, scope, execution plan, checks, rollback path, and acceptance criteria. Codex keeps the atomic execution package internal unless strict mode is requested or risk requires explicit review.

## Autonomy

Codex may proceed with safe assumptions when the change is:

- docs or configuration only;
- local and reversible;
- inside allowed files;
- free of secrets, production/deploy/runtime changes, business logic, formulas, schemas, APIs, output contracts, metrics, or governed KB content changes;
- verifiable with a meaningful check.

Codex should ask a clarifying question or stop only for hard blockers, such as unsafe scope, conflicting acceptance criteria, missing permission, destructive actions, or no possible validation.

## Advanced Mode

Atomic task packages remain available for strict, high-risk, or already-scoped work. They are an internal safety mechanism by default, not a required form Sergey must write for normal goals.

## Final Output

Keep the final user-facing report short:

- what changed;
- checks run;
- residual risks;
- next step.
