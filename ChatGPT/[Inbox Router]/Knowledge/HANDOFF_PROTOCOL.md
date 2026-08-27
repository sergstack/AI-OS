# Inbox Router Handoff Protocol

Use the canonical field set in `HANDOFF_STYLE_STANDARD.md` when the destination
is an AI-OS project. Its mode literal is `goal / strict`.

## Destination notes

Select the destination only through `ROUTING_RULES.md`; this protocol governs
the handoff after that selection and does not define destination rows.

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
