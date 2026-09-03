# Inbox Router Knowledge Index

Canonical repository path: `ChatGPT/[Inbox Router]`

ChatGPT Project display name may remain `[Inbox / Router]`.

## Active behavior sources

- `INDEX.md` — active knowledge index.
- `ROUTING_RULES.md` — front-door destination rules.
- `THINGS_OUTPUT_SCHEMA.md` — Things task output schema.
- `HANDOFF_PROTOCOL.md` — standard project handoff format.
- `SMOKE_QA_FOR_INBOX_ROUTER.md` — v06 smoke QA.

## Reference material

- `INBOX_ROUTER_FILES_INDEX.md` — file map and bundle coverage.
- `ROUTER_WORKFLOW.md` — legacy/support operating workflow.
- `ROUTER_HANDOFF_PROTOCOL.md` — legacy/support handoff notes.
- `ROUTER_SMOKE_QA.md` — legacy/support smoke examples.
- `ROUTER_ANTI_PATTERNS.md` — legacy/support anti-patterns.

## Source priority

For v06 front-door behavior use:

1. `ROUTING_RULES.md`
2. `THINGS_OUTPUT_SCHEMA.md`
3. `HANDOFF_PROTOCOL.md`
4. `SMOKE_QA_FOR_INBOX_ROUTER.md`

Legacy/support files remain available for context:

- `ROUTER_WORKFLOW.md`
- `ROUTER_HANDOFF_PROTOCOL.md`
- `ROUTER_SMOKE_QA.md`
- `ROUTER_ANTI_PATTERNS.md`

If files conflict, v06 files override legacy router files.

## Bundle coverage

- `INBOX_01_ROUTING_WORKFLOW.md` covers active routing and Things schema sources.
- `INBOX_02_HANDOFF_QA_ANTI_PATTERNS.md` covers active handoff and smoke QA sources.

## Boundary

Inbox Router classifies raw input, formulates clean output, and routes to Things, Calendar, Notes / Obsidian, or the right AI-OS project.
It does not deeply solve, calculate, implement, or create production workflows.
