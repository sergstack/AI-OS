# [Inbox Router] — Routing Workflow

## Purpose

Compact upload artifact for [Inbox Router] covering routing workflow.

## Source files

- `ChatGPT/[Inbox Router]/Knowledge/INBOX_ROUTER_FILES_INDEX.md`
- `ChatGPT/[Inbox Router]/Knowledge/ROUTER_WORKFLOW.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Inbox Router]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Inbox Router]/Knowledge/INBOX_ROUTER_FILES_INDEX.md`

# Inbox Router Files Index
## Purpose
## Project instruction
- `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` — paste into ChatGPT Project Instructions.
## Knowledge files
- `INDEX.md` — active Inbox Router knowledge index.
- `ROUTING_RULES.md` — front-door destination rules.
- `THINGS_OUTPUT_SCHEMA.md` — Things task output schema.
- `HANDOFF_PROTOCOL.md` — standard project handoff format.
- `SMOKE_QA_FOR_INBOX_ROUTER.md` — v05 smoke QA.
- `ROUTER_WORKFLOW.md` — legacy/support operating workflow and destination rules.
- `ROUTER_HANDOFF_PROTOCOL.md` — legacy/support handoff formats for target projects.
- `ROUTER_SMOKE_QA.md` — legacy/support smoke test examples.
- `ROUTER_ANTI_PATTERNS.md` — legacy/support failure modes and corrections.
## Upload order
1. `INDEX.md`
2. `ROUTING_RULES.md`
3. `THINGS_OUTPUT_SCHEMA.md`
4. `HANDOFF_PROTOCOL.md`
5. `SMOKE_QA_FOR_INBOX_ROUTER.md`
6. `ROUTER_WORKFLOW.md`
7. `ROUTER_HANDOFF_PROTOCOL.md`
8. `ROUTER_ANTI_PATTERNS.md`
9. `ROUTER_SMOKE_QA.md`
## Do not upload
- raw KB dumps;
- transcripts;
- logs;
- temporary files;
- secrets;
- unrelated project folders.
## Status


## From: `ChatGPT/[Inbox Router]/Knowledge/ROUTER_WORKFLOW.md`

# Router Workflow
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
