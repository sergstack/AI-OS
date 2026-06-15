# Repository Map

## Purpose

Define the working architecture for AI-OS project folders and external destinations.

## Front door

`[Inbox Router]` is the AI-OS front-door routing layer.

If the input is raw, unclear, mixed, emotional, or not yet task-ready, route it to `[Inbox Router]` first.

## Project map

| Path / destination | Role |
|---|---|
| `[Inbox Router]` | Front-door router; turns raw input into Things task, Calendar item, Note, Someday / Maybe item, or project handoff. |
| `ChatGPT/[AI OS]` | AI concepts, patterns, evidence, confidence, governance. |
| `ChatGPT/[Thinking]` | Strategy, decisions, assumptions, risks, options, judge/revisor work. |
| `ChatGPT/[Analytics]` | Calculations, marts, metrics, reconciliations, deterministic data QA. |
| `ChatGPT/[LLM]` | Prompts, model routing, workflow orchestration, LLM quality. |
| `ChatGPT/[Codex]` | Implementation task framing, code review, tests/release handoff. |
| `Codex APP` | Execution/runtime layer for long-running Codex work. |
| Things | Action system for next actions; not a knowledge base. |
| Calendar | Time-bound commitments. |
| Notes / Obsidian | Context and reference material. |

## Actual path note

The Inbox Router repository folder is `[Inbox Router]`.
The ChatGPT Project may be named `[Inbox / Router]`.
