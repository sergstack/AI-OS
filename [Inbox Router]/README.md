# [Inbox / Router] Project Setup

## Purpose

`[Inbox / Router]` is a manual v0 input routing layer for Sergey's AI OS.
It receives raw thoughts, tasks, ideas, and problems, then turns them into a
clear route, clarification, next action, or handoff.

## What this project is

- lightweight ChatGPT Project setup;
- manual intake / routing helper;
- entry layer before Things, Calendar, Notes, `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`.

## What this project is not

- not governed KB;
- not automation;
- not agentic workflow;
- not vector search;
- not production routing system;
- not a general-purpose chat.

## Folder naming

- ChatGPT Project name: `[Inbox / Router]`
- Repo folder name: `[Inbox Router]`

The repo folder does not include `/` because slash creates nested folders in
repository paths.

## Folder structure

```text
[Inbox Router]/
├── README.md
├── PROJECT_INSTRUCTIONS.md
└── Knowledge/
    ├── INBOX_ROUTER_FILES_INDEX.md
    ├── ROUTER_WORKFLOW.md
    ├── ROUTER_HANDOFF_PROTOCOL.md
    ├── ROUTER_SMOKE_QA.md
    └── ROUTER_ANTI_PATTERNS.md
```

## How to configure ChatGPT Project

1. Create ChatGPT Project named `[Inbox / Router]`.
2. Paste `PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload Knowledge files from `Knowledge/`.
4. Do not upload governed KB dumps or unrelated project folders.

## What to upload

- `Knowledge/INBOX_ROUTER_FILES_INDEX.md`
- `Knowledge/ROUTER_WORKFLOW.md`
- `Knowledge/ROUTER_HANDOFF_PROTOCOL.md`
- `Knowledge/ROUTER_SMOKE_QA.md`
- `Knowledge/ROUTER_ANTI_PATTERNS.md`

## What not to upload

- raw KB dumps;
- transcripts;
- temp files;
- logs;
- unrelated project files;
- secrets.

## Operating model

Capture -> Classify -> Clarify if needed -> Route -> Next Action / Handoff -> Review.

## Status

Manual v0 experiment.
Not production.
Not automation.
