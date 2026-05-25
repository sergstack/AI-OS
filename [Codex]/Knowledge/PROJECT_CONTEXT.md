# Project Context

## Purpose

This file gives persistent engineering context for Codex / Claude Code tasks.

## Default principles

- Atomic task packages.
- Minimal safe changes.
- Deterministic tests.
- Acceptance criteria before implementation.
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
