# Inbox Router Handoff Protocol

Use the canonical field set in `HANDOFF_STYLE_STANDARD.md` when the destination
is an AI-OS project. Its mode literal is `goal / strict`.

## Destination notes

- `[AI OS]` — AI concepts, patterns, evidence, confidence, governance.
- `[Thinkers OS]` — thinker portfolio, required corpus, source requests/intake, provenance, author artifacts, Judge/Revisor, and synthesis maintenance.
- `[Thinking]` — strategy, decisions, assumptions, risks, options.
- `[Analytics]` — calculations, marts, metrics, reconciliations, data QA.
- `[LLM]` — prompts, model routing, workflow orchestration, LLM quality.
- `[Codex]` — implementation-ready tasks, code review, tests, release handoff.

## Codex handoff minimum

For `[Codex]`, broad repository or workflow goals may use `Mode: goal`.
Use `Mode: strict` only when the work is high-risk, already scoped, or
explicitly requested as a strict task package. Include known repo context,
constraints, checks, acceptance criteria, and rollback notes without inventing
missing facts.

## AES applicability

Inbox Router has thin AES applicability only when it packages or preserves a
governed execution handoff. Canonical execution semantics come from repo-root
`AUTONOMOUS_EXECUTION_STANDARD.md`; Router does not execute the target task,
run corrective loops, or gain merge/deploy/production authority. No Router
AES extension is currently required.
