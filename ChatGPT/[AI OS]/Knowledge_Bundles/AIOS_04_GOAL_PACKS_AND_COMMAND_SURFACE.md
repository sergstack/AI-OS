# [AI OS] — Goal Packs and Command Surface

## Purpose

Compact upload artifact for [AI OS] covering the first Goal Packs layer, one-touch command surface, context pack standard, and Prompt QA Factory.

## Source files

- `GOAL_PACKS.md`
- `COMMAND_SURFACE.md`
- `CONTEXT_PACK_STANDARD.md`
- `PROMPT_QA_FACTORY.md`
- `ChatGPT/[AI OS]/Knowledge/WEEKLY_AI_OS_REVIEW_TEMPLATE.md`
- `ChatGPT/[AI OS]/Knowledge/ARCHIVE_SUPERSEDED_RULE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- default_upload_mode: `Knowledge_Bundles`

---

# Content

## From: `GOAL_PACKS.md`

Goal Packs are reusable workflows for broad goals. Sergey starts from intent; AI-OS, LLM, Analytics, or Codex infer safe execution details.

In default Goal Mode, Goal Packs are not atomic task packages. Codex still compiles internal scope, checks, rollback, and acceptance criteria before editing.

### Active packs

| Pack | Trigger | Route | Output | Quality gate |
|---|---|---|---|---|
| `ai_trend_triage` | "What changed in AI and does it matter for me?" | `[AI OS]` -> `[Thinking]` or `[LLM]` if needed | short verdict, use cases, risks, next step | supported / weak / unsupported claims separated |
| `codex_goal_to_pr` | repo/workflow improvement or Goal Mode GitHub issue | `[Codex]` | branch, minimal diff, checks, PR for owner review | no atomic-task burden; checks pass or blockers are reported |
| `finance_memo_factory` | finance memo from data | `[Analytics]` -> `[LLM]` -> `[Codex]` only when repo artifact, automation, or executable package is needed -> judge/revise | memo narrative from Analytics facts; executable artifact or PR only when needed | calculations use Python or SQL |
| `analytics_factory_loop` | full analytics cycle for a question | `[Analytics]` -> `[LLM]` for narrative -> `[Codex]` only for artifacts/repo changes | compact analytical answer or memo with method, QA, limitations, and next run trigger | deterministic calculation before findings |
| `autoloop` | iterate analysis until QA passes or blockers are clear | `[Analytics]` | revised findings or blocker report | supervised loop only; stop on DQ fail, unclear grain, missing contract, or no validation path |
| `supervised_agent_loop_design` | design a safe loop for a workflow | `[AI OS]` -> `[Thinking]` / `[Codex]` when implementation packaging is needed | loop design with retry/rerun rule, stop conditions, owner acceptance point, and next trigger | supervised only; no autonomous retrieval or production agentic workflow |
| `cross_project_eval_review` | check this AI output / PR / memo / workflow | `[AI OS]` for evidence/governance routing, then owner project | eval verdict with required fixes, residual risks, final quality status, next step | deterministic checks override LLM judge |
| `context_pack_builder` | build a compact context package or prompt from a goal | `[LLM]` -> owner project by output type | Context Pack or CTC prompt with facts, constraints, forbidden inputs, expected output, and quality gate | curated context only; no raw dumps or unsupported retrieval |
| `local_ai_pilot` | test a local AI / Ollama / Open WebUI idea safely | `[LLM]` -> `[Thinking]` for hardware decisions -> `[Codex]` only for approved repo work | pilot plan or verdict with security boundary, eval matrix, limitations, and next step | experiment only; no production automation or autonomous retrieval |
| `audit_anomaly_review` | anomaly, variance, or suspicious record | `[Analytics]` -> `[Thinking]` if decision framing is needed | finding, likely cause, evidence, risk, recommended action | no LLM arithmetic |
| `streamdeck_prompt_upgrade` | improve a Stream Deck / quick prompt workflow | `[LLM]` -> `[Codex]` when repo edits are needed | tighter prompt or repo PR | prompt is short, routable, evidence-aware, and does not add unsupported automation |
| `prompt_qa_factory` | turn a reusable prompt into an accepted standard | `[AI OS]` -> owner project -> `[LLM]` / `[Thinking]` judge-revisor when needed -> `[Codex]` only for repo docs or PR work | Prompt QA Record with candidate -> test -> judge -> revise -> selected status, UX score, residual risks, and acceptance status | supervised only; human-owned acceptance required; no production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, or auto-merge |

### Candidate packs

| Pack | Route | Purpose | Promotion caution |
|---|---|---|---|
| `dashboard_critic` | `[Analytics]` / `[Thinking]` | review dashboard usefulness, clarity, or decision support | separate visual critique from metric correctness |
| `security_cleanup` | `[Codex]` | repo-only safety cleanup for risky public-repo artifacts or safety wording | not full access/security management |
| `weekly_ai_os_review` | `[AI OS]` -> `[Thinking]` / `[Codex]` | review drift and choose one next useful improvement | do not create status ledgers or operating journals |
| `reconciliation_builder` | `[Analytics]` -> `[Codex]` | build or improve reconciliation workflow | keep numeric logic deterministic and source layers explicit |

## From: `COMMAND_SURFACE.md`

One-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from the result Sergey wants, not from an atomic task form.

| Command | Target project | Input | Output | Related Goal Pack |
|---|---|---|---|---|
| `ChatGPT Route` | `[Inbox Router]` | goal, task, message, or unclear request | target project and next prompt | context-dependent |
| `Goal -> Codex APP` | Codex APP | broad repo/workflow goal, GitHub issue, or handoff | branch, checks, PR, report | `codex_goal_to_pr` |
| `AI Trend` | `[AI OS]` | AI topic, release, tool, link, or question | trend verdict, relevance, risks, next step | `ai_trend_triage` |
| `Finance Memo` | `[Analytics]` -> `[LLM]` | data, period, currency, audience | data contract / QA / memo narrative | `finance_memo_factory` |
| `Analytics Loop` | `[Analytics]` | question, data sources, period, grain, filters | full cycle from data contract to findings, memo, QA, and next run | `analytics_factory_loop` |
| `Autoloop Analysis` | `[Analytics]` | question, data, QA criteria, stop conditions | supervised revise/rerun loop or blocker report | `autoloop` |
| `Agent Loop Design` | `[AI OS]` | workflow goal, owner, checks, stop conditions | supervised loop design with acceptance gate | `supervised_agent_loop_design` |
| `Eval / Judge` | `[LLM]` / `[Thinking]` / `[Codex]` / `[Analytics]` / `[AI OS]` | output, workflow result, PR, memo, claim, or loop design | pass / revise / blocked review with required fixes | `cross_project_eval_review` |
| `Audit Anomaly` | `[Analytics]` | anomaly, account/entity, period, expected behavior | finding, evidence, risk, recommended action | `audit_anomaly_review` |
| `StreamDeck Improve` | `[LLM]` / `[Codex]` | current button/prompt and desired result | improved prompt or PR | `streamdeck_prompt_upgrade` |
| `Prompt QA` | `[AI OS]` -> owner project | reusable prompt candidate, use case, tests, judge criteria | Prompt QA Record with selected/candidate status, UX score, residual risks, and acceptance | `prompt_qa_factory` |
| `Local AI Pilot` | `[LLM]` / `[Thinking]` | local model, Ollama/Open WebUI idea, hardware question, or private draft use case | controlled experiment plan, security boundary, eval matrix, limitations | `local_ai_pilot` |
| `PR Judge` | `[Thinking]` / `[Codex]` | PR link, goal, checks, risks | pass / revise / blocked review | context-dependent |
| `Revisor` | `[LLM]` | draft plus judge notes | clearer final without new claims | context-dependent |
| `Context Pack` | `[LLM]` | goal, files, facts, constraints, expected output | compact reusable context pack or CTC prompt | `context_pack_builder` |
| `Sync Check` | `[Codex]` / Codex APP | repo branch or local checkout | repo checks plus sync guidance | `codex_goal_to_pr` |

Usage:

- Press or type the command.
- Add the goal and only the context needed to start.
- Let the target project infer route, scope, checks, and next action.
- Use strict task packages only when scope is already known or risk is high.

## From: `CONTEXT_PACK_STANDARD.md`

Context Packs are compact inputs for AI-OS, LLM, Analytics, and Codex workflows. They contain the context needed for the next decision or output, not every available file.

### Minimal schema

```markdown
# Context Pack

## Goal

## Decision needed

## Relevant files

## Facts

## Constraints

## Forbidden

## Open questions

## Expected output

## Quality gate
```

### Guidance

- Do not dump all files.
- Use curated context.
- Separate facts from assumptions.
- Mark missing evidence and open questions.
- Route deterministic calculations to `[Analytics]`.
- Route implementation, repo changes, checks, and PR work to `[Codex]`.
- Route AI evidence, governance, and trend interpretation to `[AI OS]`.
- Keep raw source files in the repo or source system; reference them instead of copying large bodies of text.

### Quality gate

A Context Pack is ready when the goal is clear, sources are named, facts and assumptions are separated, constraints and forbidden actions are visible, the expected output is specific, and the receiving project can act without asking Sergey to write an atomic task package.

## From: `PROMPT_QA_FACTORY.md`

Prompt QA Factory is the AI-OS standard for turning reusable prompts into accepted prompt assets.

Core loop:

```text
candidate -> test -> judge -> revise -> selected
```

Applies to StreamDeck prompts, ChatGPT Project prompts, Codex prompts, Judge/Revisor prompts, and Analytics memo prompts.

Selection requires recorded test cases, judge criteria, UX score, residual risks, and owner acceptance.

Forbidden: production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, auto-merge, and claims of production readiness.

### Prompt QA Record

```markdown
# Prompt QA Record

## Prompt name
## Owner project
## Use case
## Candidate prompt
## Test cases
## Judge criteria
## Iterations
## Final selected prompt
## UX score
## Residual risks
## Acceptance status
```

## From: `ChatGPT/[AI OS]/Knowledge/WEEKLY_AI_OS_REVIEW_TEMPLATE.md`

# Weekly AI-OS Review Template

Status: candidate / ready for human review.
Purpose: lightweight weekly review discipline, not a task manager, status ledger, operating journal, or autonomous workflow.

## Inputs

Week:
Reviewer:
New inputs:
Recent issues / PRs:
Recent repo changes:
Recent ChatGPT Project changes:
Recent Stream Deck / command changes:

## Open loops

| loop | owner project | current status | evidence status | risk | next decision |
|---|---|---|---|---|---|

Evidence status values:
- `supported`
- `weak`
- `unsupported`
- `mixed`

## Repo / Codex

Open PRs:
Stale issues:
Failing checks:
Blocked branches:
Repo safety concerns:

## Knowledge / Project sync

Bundles changed:
Upload needed:
Smoke QA needed:
Project Instructions changed:
Project Knowledge drift:

## Stream Deck / commands

Buttons to improve:
Buttons to retire:
Commands needing Prompt QA:
Prompt QA status:

## Archive / Superseded candidates

| candidate | reason | replacement | affected file | owner project | traceability note |
|---|---|---|---|---|---|

## Top improvement

Top 1 improvement this week:
Why it matters:
Evidence:
Risk if skipped:

## One next action

Action:
Owner:
Route:
Acceptance criteria:
Stop condition:

## Guardrails

- End with exactly one next action.
- Do not create a status ledger or operating journal.
- Do not create autonomous weekly review, production automation, retrieval, vector DB, embeddings, semantic search, or web UI.
- Keep candidate status until pilot evidence and owner acceptance exist.
- Stream Deck productivity commands require Prompt QA before promotion.

## From: `ChatGPT/[AI OS]/Knowledge/ARCHIVE_SUPERSEDED_RULE.md`

# Archive / Superseded Rule

Status: candidate / ready for human review.
Purpose: traceability rule for removing items from the active layer. This is not an auto-archive rule and not a deletion rule.

## Required record

Item:
Status:
Reason:
Replacement, if any:
Source / affected file:
Owner project:
Removal from active layer:
Traceability note:
Reviewer:
Date:

## Status values

- `active`
- `candidate`
- `superseded`
- `archived`
- `rejected`
- `blocked`

## Rules

- Do not delete without reason, replacement, and status.
- Do not auto-archive.
- Keep traceability from old item to replacement or decision record.
- Remove from active layer only after reviewer acceptance.
- Preserve enough context to understand why the item changed state.
- Do not archive private data, secrets, raw dumps, logs, runtime artifacts, embeddings, vector DB files, or zip archives into Project Knowledge.

## Superseded checklist

- [ ] Status is set.
- [ ] Reason is explicit.
- [ ] Replacement is listed or marked `none`.
- [ ] Source / affected file is listed.
- [ ] Owner project is listed.
- [ ] Active-layer removal is described.
- [ ] Traceability note links old item to replacement or decision.
- [ ] Reviewer accepted the change.

## Human acceptance

- [ ] Reviewer accepted archive / superseded status.
- [ ] Reviewer accepted replacement or `none`.
- [ ] Reviewer accepted traceability note.
- [ ] No production promotion is implied.
