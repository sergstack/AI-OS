# Prompt Library for Codex

## Inspect repo

```text
Inspect the repository for this task.
Do not edit yet.
Return relevant files, entrypoints, risks, and proposed plan.
```

## Implement

```text
Work in Goal Mode.
Inspect relevant files, infer bounded safe scope, implement the smallest useful working version, run meaningful checks, fix in-scope failures when safe, and report evidence.
Do not produce a roadmap, epic, child issue tree, or approval package unless planning was explicitly requested or a hard blocker prevents bounded implementation.
```

## Long-run implementation

```text
Implement the scoped task below in long-run mode.

Do not ask unless a hard blocker appears.
For reversible local decisions, make the safest assumption and continue.
Keep the diff minimal.
Run the smallest meaningful checks.
If a check fails, attempt one minimal fix.
Report changed files, checks, assumptions, risks, rollback, and acceptance status.
```

## Refactor safely

```text
Refactor only the specified files.
Do not change behavior.
Add or run regression checks.
Explain how behavior is preserved.
```

## Bugfix

```text
Reproduce or explain the bug.
Identify root cause.
Patch minimally.
Run tests.
Report residual risks.
```

## Review

```text
Review the diff for bugs, scope creep, missing tests, business logic changes, and output contract risks.
Return pass/revise/blocked.
```
