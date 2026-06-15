# Inbox Router Knowledge Index

## Active files

- `INBOX_ROUTER_FILES_INDEX.md` — legacy file index.
- `INDEX.md` — active knowledge index.
- `ROUTING_RULES.md` — front-door destination rules.
- `THINGS_OUTPUT_SCHEMA.md` — Things task output schema.
- `HANDOFF_PROTOCOL.md` — standard project handoff format.
- `SMOKE_QA_FOR_INBOX_ROUTER.md` — v05 smoke QA.
- `ROUTER_WORKFLOW.md` — existing operating workflow.
- `ROUTER_HANDOFF_PROTOCOL.md` — existing handoff notes.
- `ROUTER_SMOKE_QA.md` — existing smoke examples.
- `ROUTER_ANTI_PATTERNS.md` — existing anti-patterns.

## Source priority

For v05 front-door behavior use:

1. `ROUTING_RULES.md`
2. `THINGS_OUTPUT_SCHEMA.md`
3. `HANDOFF_PROTOCOL.md`
4. `SMOKE_QA_FOR_INBOX_ROUTER.md`

Legacy/support files remain available for context:

- `ROUTER_WORKFLOW.md`
- `ROUTER_HANDOFF_PROTOCOL.md`
- `ROUTER_SMOKE_QA.md`
- `ROUTER_ANTI_PATTERNS.md`

If files conflict, v05 files override legacy router files.

## Boundary

Inbox Router classifies raw input, formulates clean output, and routes to Things, Calendar, Notes / Obsidian, or the right AI-OS project.
It does not deeply solve, calculate, implement, or create production workflows.
