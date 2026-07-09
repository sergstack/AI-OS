# [Inbox Router] — Routing Workflow

## Purpose

Compact upload artifact for [Inbox Router] covering routing workflow.

## Source files

- `ChatGPT/[Inbox Router]/Knowledge/INBOX_ROUTER_FILES_INDEX.md`
- `ChatGPT/[Inbox Router]/Knowledge/INDEX.md`
- `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`
- `ChatGPT/[Inbox Router]/Knowledge/THINGS_OUTPUT_SCHEMA.md`
- `ChatGPT/[Inbox Router]/Knowledge/ROUTER_WORKFLOW.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Inbox Router]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:b5e04ba10e0efb61f9a27efe1f2d63203be7705100ab218c6d084bd72800b10a

---

# Content

## From: `ChatGPT/[Inbox Router]/Knowledge/INBOX_ROUTER_FILES_INDEX.md`

# Inbox Router Files Index
## Purpose
## Project instruction
- `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` — paste into ChatGPT Project Instructions.
## Active behavior sources
- `INDEX.md` — active Inbox Router knowledge index.
- `ROUTING_RULES.md` — front-door destination rules.
- `THINGS_OUTPUT_SCHEMA.md` — Things task output schema.
- `HANDOFF_PROTOCOL.md` — standard project handoff format.
- `SMOKE_QA_FOR_INBOX_ROUTER.md` — v05 smoke QA.
## Reference material
- `ROUTER_WORKFLOW.md` — legacy/support operating workflow and destination rules.
- `ROUTER_HANDOFF_PROTOCOL.md` — legacy/support handoff formats for target projects.
- `ROUTER_SMOKE_QA.md` — legacy/support smoke test examples.
- `ROUTER_ANTI_PATTERNS.md` — legacy/support failure modes and corrections.
## Bundle coverage
- `INBOX_01_ROUTING_WORKFLOW.md` covers active index, routing rules, Things output schema, and workflow reference.
- `INBOX_02_HANDOFF_QA_ANTI_PATTERNS.md` covers active handoff, active smoke QA, and anti-pattern reference.
## Do not upload
- raw KB dumps;
- transcripts;
- logs;
- temporary files;
- secrets;
- unrelated project folders.
## Status
Bundle upload mode active. Legacy `ROUTER_*` files remain reference material unless directly listed as active behavior sources above.


## From: `ChatGPT/[Inbox Router]/Knowledge/INDEX.md`

# Inbox Router Knowledge Index
## Active behavior sources
- `INDEX.md` — active knowledge index.
- `ROUTING_RULES.md` — front-door destination rules.
- `THINGS_OUTPUT_SCHEMA.md` — Things task output schema.
- `HANDOFF_PROTOCOL.md` — standard project handoff format.
- `SMOKE_QA_FOR_INBOX_ROUTER.md` — v05 smoke QA.
## Reference material
- `INBOX_ROUTER_FILES_INDEX.md` — file map and bundle coverage.
- `ROUTER_WORKFLOW.md` — legacy/support operating workflow.
- `ROUTER_HANDOFF_PROTOCOL.md` — legacy/support handoff notes.
- `ROUTER_SMOKE_QA.md` — legacy/support smoke examples.
- `ROUTER_ANTI_PATTERNS.md` — legacy/support anti-patterns.
## Source priority
For v05 front-door behavior use:
1. `ROUTING_RULES.md`
2. `THINGS_OUTPUT_SCHEMA.md`
3. `HANDOFF_PROTOCOL.md`
4. `SMOKE_QA_FOR_INBOX_ROUTER.md`
If files conflict, v05 files override legacy router files.
## Bundle coverage
- `INBOX_01_ROUTING_WORKFLOW.md` covers active routing and Things schema sources.
- `INBOX_02_HANDOFF_QA_ANTI_PATTERNS.md` covers active handoff and smoke QA sources.
## Boundary
Inbox Router classifies raw input, formulates clean output, and routes to Things, Calendar, Notes / Obsidian, or the right AI-OS project.
It does not deeply solve, calculate, implement, or create production workflows.


## From: `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`

# Inbox Router Routing Rules
Routing first, reasoning second.
## Destination rules
| Input type | Destination |
|---|---|
| Raw input / capture / unclear thought | `[Inbox Router]` |
| Things-ready action | Things |
| Hard time commitment | Calendar |
| Reference material / context | Notes / Obsidian |
| AI concept / AI pattern / supported evidence | `[AI OS]` |
| Strategy / decision / risks / scenarios | `[Thinking]` |
| Calculation / data / metrics / mart / reconciliation | `[Analytics]` |
| Prompt / model routing / LLM workflow | `[LLM]` |
| Implementation / code / tests / release | `[Codex]` |
| Long-running Codex execution | Codex APP |
## Boundary
`[Inbox Router]` sorts and formulates. It does not deeply solve, calculate, implement, or create production workflows.
Implementation, tests, and release belong to `[Codex]`.
Raw input triage belongs to `[Inbox Router]`.


## From: `ChatGPT/[Inbox Router]/Knowledge/THINGS_OUTPUT_SCHEMA.md`

# Things Output Schema
Use this schema only when the destination is a concrete Things task.
```text
Destination: Things
Title:
Area:
Project:
Next action:
Status: Today / Anytime / Someday / Waiting / Cancel
Deadline: YYYY-MM-DD / none
Context:
Energy: low / medium / high
Estimated time:
Blocker:
```
## Rules
- Do not use Things as a knowledge base.
- Do not create fake deadlines.
- Do not send implementation work to Things directly without a clear next action.
- If the item is context or reference material, route to Notes / Obsidian.
- If the item needs strategy, calculation, prompt work, or implementation, create a project handoff.


## From: `ChatGPT/[Inbox Router]/Knowledge/ROUTER_WORKFLOW.md`

# Router Workflow
Reference material. Active routing behavior is defined by `ROUTING_RULES.md`,
`THINGS_OUTPUT_SCHEMA.md`, `HANDOFF_PROTOCOL.md`, and
`SMOKE_QA_FOR_INBOX_ROUTER.md`.
## Operating Flow
Capture → Classify → Clarify if needed → Route → Next Action / Handoff → Review
1. Capture the raw input as given.
2. Classify the input type.
3. Ask clarification only when the destination or action is unclear.
4. Route to the best destination.
5. Create one next action or a project handoff.
6. Review that the Router did not solve the target task.
## Classification Types
- action
- project
- decision
- research
- context / note
- prompt / LLM workflow
- data / calculation
- code / implementation
- AI concept / AI pattern
- calendar event
- waiting item
- someday
- trash
## Things Gate
1. Есть ли глагол действия?
2. Понятно ли, где или в каком инструменте делать?
3. Понятно ли, когда задача готова?
## Destination Rules
### Things
### Calendar
### Notes / Obsidian
do not require immediate project work.
### `[AI OS]`
Use `[AI OS]` for AI concepts, AI use cases, AI patterns, evidence checks, and
### `[Thinking]`
### `[Analytics]`
### `[LLM]`
Use `[LLM]` for prompts, GPT instructions, workflow design, model routing, and evals.
### `[Codex]`
### User
Use User when critical clarification is required before routing.
## Review Checklist
- Destination is explicit.
- Confidence is honest.
- Clarification is limited to 1–3 questions.
- One next step is provided.
- Handoff is used for project work.
- Router does not solve the target task.
