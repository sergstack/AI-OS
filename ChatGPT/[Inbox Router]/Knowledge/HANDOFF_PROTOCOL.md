# Inbox Router Handoff Protocol

Use this format when the destination is an AI-OS project.

```text
From:
To:
Task type:
Mode: goal / strict task
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:
```

## Destination notes

- `[AI OS]` — AI concepts, patterns, evidence, confidence, governance.
- `[Thinking]` — strategy, decisions, assumptions, risks, options.
- `[Analytics]` — calculations, marts, metrics, reconciliations, data QA.
- `[LLM]` — prompts, model routing, workflow orchestration, LLM quality.
- `[Codex]` — implementation-ready tasks, code review, tests, release handoff.

## Codex handoff minimum

For `[Codex]`, broad repository or workflow goals may use `Mode: goal`.
Use `Mode: strict task` only when the work is high-risk, already scoped, or
explicitly requested as a strict task package. Include known repo context,
constraints, checks, acceptance criteria, and rollback notes without inventing
missing facts.
