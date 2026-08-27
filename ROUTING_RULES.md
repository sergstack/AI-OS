# Canonical Routing Rules

Routing first, reasoning second. This is the single owner of destination
selection; `HANDOFF_STYLE_STANDARD.md` owns handoff fields. No other file
redefines these rows.

## Registered capability destinations

| Input type | Destination |
| --- | --- |
| Raw input, capture, unclear thought | `[Inbox Router]` |
| AI concept, AI pattern, supported evidence, AI governance question, governance promotion decision | `[AI OS]` |
| Thinker author, required corpus, source request or intake, provenance, author artifact, cross-author synthesis maintenance, Lens Router, Conflict Map | `[Thinkers OS]` |
| Strategy, decision, risks, scenarios, options, assumptions | `[Thinking]` |
| Applying thinker patterns to a real decision | `[Thinking]` |
| Calculation, data, metrics, mart, reconciliation, quantitative validation, data QA | `[Analytics]` |
| Prompt, model routing, model selection, LLM workflow, orchestration, eval design | `[LLM]` |
| Implementation, code, tests, refactor, release, schemas, automation, validators | `[Codex]` |

## External destinations

These are not registry capabilities. A non-match is expected; do not create a capability, invoke `project-context`, or widen authority.

| Input type | Destination | Class |
| --- | --- | --- |
| Things-ready action | Things | `external` |
| Hard time commitment | Calendar | `external` |
| Reference material, context, idea | Notes / Obsidian | `external` |
| Long-running Codex execution | `Codex APP` directory | `internal_non_capability` |
| Critical clarification required before routing | User | `owner_escalation` |

## Tie-break rules

| Case | Rule |
| --- | --- |
| Coding task preparation | `[Codex]`; `[LLM]` only for a prompt or workflow deliverable |
| Production readiness | `[Codex]` repository/release; `[LLM]` prompt/workflow; `[AI OS]` governance promotion; earliest unfinished stage wins |
| Production workflow rollout | `[Codex]` implementation; `[LLM]` prior workflow design |
| Thinker patterns in a decision | `[Thinking]` decision; `[Thinkers OS]` corpus/artifacts |
| Numbers inside a strategy memo | `[Analytics]` calculation; `[Thinking]` decision |
| AI governance question | `[AI OS]`, including reusable rule promotion candidates arriving from `[Thinking]` |
| Still ambiguous | `blocked`; state candidates and missing deciding fact |

## Boundary

`[Inbox Router]` sorts and formulates. It does not deeply solve, calculate,
implement, or create production workflows. Codex issues must already be
implementation-ready. Raw or unclear input goes through `[Inbox Router]` first.
