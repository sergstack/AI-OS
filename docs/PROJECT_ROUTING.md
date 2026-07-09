# Project Routing

Scope note: this file is a repo-level convenience overview. The canonical
front-door routing rules live in `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`.
If this overview and the Inbox Router rules diverge, use the Inbox Router file.

Routing first, reasoning second.

## Routing table

| Input type | Destination |
|---|---|
| Raw input / capture / unclear thought | `[Inbox Router]` |
| Things-ready action | Things |
| Hard time commitment | Calendar |
| Reference material / context | Notes / Obsidian |
| AI concept / AI pattern / supported evidence | `ChatGPT/[AI OS]` |
| Strategy / decision / risks / scenarios | `ChatGPT/[Thinking]` |
| Calculation / data / metrics / mart / reconciliation | `ChatGPT/[Analytics]` |
| Prompt / model routing / LLM workflow | `ChatGPT/[LLM]` |
| Implementation / code / tests / release | `ChatGPT/[Codex]` |
| Long-running Codex execution | `Codex APP` |

## Boundary rule

`[Inbox Router]` sorts and formulates. It does not deeply solve, calculate, implement, or create production workflows.

Codex issues should already be implementation-ready. If the input is raw or unclear, route it through `[Inbox Router]` before creating a Codex task.
