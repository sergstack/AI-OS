# Project Context

## Purpose

This file gives persistent engineering context for Codex / Claude Code tasks.

## Default principles

- Goal Mode is build-first for normal broad goals.
- Atomic task packages only for strict, high-risk, already-scoped, or ultra-long work.
- Minimal safe changes.
- Deterministic tests.
- Safely inferred acceptance criteria before implementation when the task is low risk.
- Long-run autonomy only for scoped, local, reversible, testable work.
- Diff review before final.
- Rollback notes for risky changes.

## Forbidden by default

- secrets handling;
- broad refactors;
- changing business logic without approval;
- deleting QA checks;
- changing output contracts without explicit acceptance;
- adding vector DB / embeddings / web UI / agentic automation before governance approval.

## Preferred final answer

```text
Summary
Files changed
Tests/checks
Assumptions
Risks
Acceptance status
Next step
```
