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
- Repo folder name: `[Inbox Router]`

The repo folder does not include `/` because slash creates nested folders in
repository paths.

Do not move the folder in this task. The repo folder may remain
`[Inbox Router]`, while the ChatGPT Project name may remain
`[Inbox / Router]`.

## Path exception

`[Inbox Router]` currently lives at repository root as a legacy / active project folder.

Do not move it in this PR.

Canonical active path for this project package:

```text
[Inbox Router]
```

Display name in ChatGPT may be:

```text
[Inbox / Router]
```

Future normalization to `ChatGPT/[Inbox Router]` requires a separate migration issue.

Russian is the default user-facing language. English is allowed for stable
product names, file names, and inter-project handoff fields.

## Folder structure

```text
[Inbox Router]/
├── README.md
├── PROJECT_INSTRUCTIONS.md
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
2. Paste `PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload Knowledge files from `Knowledge/`.
4. Do not upload governed KB dumps or unrelated project folders.

## What to upload

- `Knowledge/INBOX_ROUTER_FILES_INDEX.md`
- `Knowledge/INDEX.md`
- `Knowledge/ROUTING_RULES.md`
- `Knowledge/THINGS_OUTPUT_SCHEMA.md`
- `Knowledge/HANDOFF_PROTOCOL.md`
- `Knowledge/SMOKE_QA_FOR_INBOX_ROUTER.md`
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
