# Goal Mode

Goal Mode is the default user-facing workflow for AI-OS and Codex. It is build-first: inspect, infer bounded scope, implement the smallest useful working version, check it, and report evidence.

## Flow

```text
GOAL -> inspect repo -> infer bounded safe scope -> branch -> implement smallest useful version -> check/fix in scope -> report/PR -> owner review
```

## User Interface

In default Goal Mode, the user gives a broad goal, not an atomic task package.

Router, AI OS, LLM, or Codex may turn that goal into a route, scope, execution plan, checks, rollback path, and acceptance criteria. Codex keeps that execution package internal unless strict mode is requested, the task spans independent releases, or risk requires explicit review.

Do not produce a roadmap, epic, child-issue tree, or approval package for a clear implementation goal unless Sergey explicitly asks for planning or a hard blocker prevents bounded execution.

## Autonomy

Codex may proceed with safe assumptions when the change is:

- docs or configuration only;
- local and reversible;
- inside allowed files;
- free of secrets, production/deploy/runtime changes, business logic, formulas, schemas, APIs, output contracts, metrics, or governed KB content changes;
- verifiable with a meaningful check.

Codex should ask a clarifying question or stop only for hard blockers, such as unsafe scope, missing secrets required for real execution, conflicting acceptance criteria, destructive actions, production/runtime mutation without approval, schema/metric/formula/provider-routing/output-contract changes without approval, or no possible validation.

## Advanced Mode

Atomic task packages remain available for strict, high-risk, or already-scoped work. They are an internal safety mechanism by default, not a required form Sergey must write for normal goals.

## Final Output

Keep the final user-facing report short:

- what changed;
- checks run;
- residual risks;
- next step.
