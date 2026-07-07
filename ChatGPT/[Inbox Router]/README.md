# [Inbox / Router] Project Setup

## Purpose

`[Inbox / Router]` is the manual v0 front-door routing layer for Sergey's AI OS.
It receives raw thoughts, tasks, ideas, and problems, then turns them into a
clear route, clarification, next action, or handoff.

## What this project is

- lightweight ChatGPT Project setup;
- manual front-door intake / routing helper;
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
- Canonical repo folder path: `ChatGPT/[Inbox Router]`

The ChatGPT Project may be named:

```text
[Inbox / Router]
```

Russian is the default user-facing language. English is allowed for stable
product names, file names, and inter-project handoff fields.

## Folder structure

```text
ChatGPT/[Inbox Router]/
├── README.md
├── PROJECT_INSTRUCTIONS.md
├── CURRENT_STATUS.md
├── SMOKE_QA_RESULTS.md
└── Knowledge/
    ├── INBOX_ROUTER_FILES_INDEX.md
    ├── INDEX.md
    ├── ROUTING_RULES.md
    ├── THINGS_OUTPUT_SCHEMA.md
    ├── HANDOFF_PROTOCOL.md
    ├── SMOKE_QA_FOR_INBOX_ROUTER.md
    ├── ROUTER_WORKFLOW.md
    ├── ROUTER_HANDOFF_PROTOCOL.md
    ├── ROUTER_SMOKE_QA.md
    └── ROUTER_ANTI_PATTERNS.md
```

## How to configure ChatGPT Project

1. Create ChatGPT Project named `[Inbox / Router]`.
2. Paste `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload bundle files from `ChatGPT/[Inbox Router]/Knowledge_Bundles/UPLOAD_LIST.md`.
4. Do not upload governed KB dumps or unrelated project folders.

## What to upload

- `Knowledge_Bundles/INBOX_01_ROUTING_WORKFLOW.md`
- `Knowledge_Bundles/INBOX_02_HANDOFF_QA_ANTI_PATTERNS.md`

Granular `Knowledge/` files remain source material and may be uploaded only
when debugging a bundle sync issue.

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
