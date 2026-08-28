# [AI OS] — Goal Packs and Command Surface

## Purpose

Compact upload artifact for [AI OS] covering the first Goal Packs layer, one-touch command surface, context pack standard, and Prompt QA Factory.

## Source files

- `docs/standards/GOAL_PACKS.md`
- `docs/standards/COMMAND_SURFACE.md`
- `docs/standards/CONTEXT_PACK_STANDARD.md`
- `docs/standards/PROMPT_QA_FACTORY.md`
- `ChatGPT/[AI OS]/Knowledge/WEEKLY_AI_OS_REVIEW_TEMPLATE.md`
- `ChatGPT/[AI OS]/Knowledge/ARCHIVE_SUPERSEDED_RULE.md`
- `ChatGPT/[AI OS]/Knowledge/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- default_upload_mode: `Knowledge_Bundles`
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:f604982af9b80f3622213a1083e8bc26db04e31af7fe43ca753223aaa1ecf471
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `docs/standards/GOAL_PACKS.md`

# Goal Packs
Goal Packs are reusable workflows for broad goals. They help Sergey start from intent while AI-OS, LLM, Analytics, or Codex infer the safe execution details.
In default Goal Mode, Goal Packs are not atomic task packages. Codex still compiles internal scope, checks, rollback, and acceptance criteria before editing.
## Active Packs
### `ai_trend_triage`
- trigger: "What changed in AI and does it matter for me?"
- route: `[AI OS]` -> `[Thinking]` or `[LLM]` if needed
- input: topic, link, release note, model/tool name, or broad question
- context needed: AI OS KB evidence, fresh web check when facts may have changed, Sergey work relevance
- output: short verdict, use cases, risks, next step
- quality gate: supported vs weak vs unsupported claims separated
- done when: Sergey has a clear adopt / watch / ignore recommendation
### `codex_goal_to_pr`
- trigger: "Make this repo/workflow better" or a GitHub issue with Goal Mode
- route: `[Codex]`
- input: broad implementation goal, constraints, repo context, issue or handoff
- context needed: `AGENTS.md`, relevant repo files, allowed scope inferred from goal
- output: branch, minimal diff, checks, PR for owner review
- quality gate: no atomic-task burden on Sergey; checks pass or blockers are reported
- done when: PR exists with summary, risks, rollback, and merge/gate status
### `finance_memo_factory`
- trigger: "Prepare a finance memo from data"
- route: `[Analytics]` -> `[LLM]` -> `[Codex]` only when repo artifact, automation, or executable package is needed -> judge/revise
- input: data sources, period, currency, question, audience
- context needed: raw/stage/mart/report boundaries, formulas, assumptions, source files
- output: memo narrative from Analytics facts; executable artifact or PR only when needed
- quality gate: totals, deltas, ratios, and reconciliations are computed deterministically
- done when: memo is traceable to source data and residual risks are visible
### `analytics_factory_loop`
- trigger: "Run the full analytics cycle for this question"
- route: `[Analytics]` -> `[LLM]` for narrative -> `[Codex]` only for executable artifacts or repo changes
- input: question, data sources, period, grain, filters, audience, constraints
- context needed: data contract, RAW/STAGE/MART boundaries, formulas, QA checks, memo goal
- output: compact analytical answer or memo with traceable method, QA, limitations, and next run trigger
- quality gate: deterministic calculation before findings; memo claims trace to `mart_main_full` or compact mart
- done when: acceptance is candidate / ready for owner review and next run trigger is explicit
### `supervised_autoloop_analysis`
- trigger: "Iterate analysis until QA passes or blockers are clear"
- route: `[Analytics]`
- input: question, available data, QA criteria, stop conditions
- context needed: data contract, deterministic checks, judge/QA rubric, rerun criteria
- output: revised findings or blocker report; no autonomous retrieval or runtime artifacts
- quality gate: supervised analytical loop only; deterministic calculations first; stop on DQ fail, unclear grain, missing contract, or no validation path
- aliases: `autoloop_analysis`, `autoloop`
- done when: judge/QA passes, or rerun/blocker is explicit
### `audit_anomaly_review`
- trigger: "Check this anomaly, variance, or suspicious record"
- route: `[Analytics]` -> `[Thinking]` if decision framing is needed
- input: anomaly description, data slice, period, account/entity, expected behavior
- context needed: raw data, transformation logic, thresholds, exclusions, prior checks
- output: finding, likely cause, evidence, risk, recommended action
- quality gate: no LLM arithmetic; all numeric checks use Python or SQL
- done when: anomaly is classified as explained, unresolved, or blocked with next action
### `streamdeck_prompt_upgrade`
- trigger: "Improve this Stream Deck / quick prompt workflow"
- route: `[LLM]` -> `[Codex]` when repo edits are needed
- input: current prompt, target button/command, desired outcome, constraints
- context needed: command surface, prompt registry/library, related project instructions
- output: tighter prompt or repo PR with updated docs/instructions
- quality gate: prompt is short, routable, evidence-aware, and does not add unsupported automation
- done when: Sergey has a usable command/prompt and validation passes when files changed
### `prompt_qa_factory`
- trigger: "Turn this reusable prompt into an accepted standard"
- route: `[AI OS]` -> owner project -> `[LLM]` / `[Thinking]` judge-revisor when needed -> `[Codex]` only for repo docs or PR work
- input: candidate prompt, owner project, use case, test cases, judge criteria, acceptance constraints
- context needed: `docs/standards/PROMPT_QA_FACTORY.md`, supervised loop boundary, prompt registry/library, owner project rules
- output: Prompt QA Record with candidate -> test -> judge -> revise -> selected status, UX score, residual risks, and acceptance status
- quality gate: supervised only; human-owned acceptance required; no production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, or auto-merge
- done when: prompt is selected by owner acceptance or remains a candidate with visible risks and next revision need
### `context_pack_builder`
- trigger: "Build a compact context package or prompt from this goal"
- route: `[LLM]` -> owner project by output type
- input: goal, source files or facts, constraints, expected output, risk level
- context needed: `docs/standards/CONTEXT_PACK_STANDARD.md`, prompt registry, routing rules, raw-dump guardrails
- output: Context Pack or CTC prompt with goal, facts, constraints, forbidden inputs, expected output, and quality gate
- quality gate: curated context only; no raw dumps, source-card dumps, chunks, logs, runtime artifacts, secrets, vector DB, embeddings, semantic search, web UI, or autonomous retrieval
- done when: receiving project can act without asking Sergey to rewrite the context from scratch
### `local_ai_pilot`
- trigger: "Test this local AI / Ollama / Open WebUI idea safely"
- route: `[LLM]` -> `[Thinking]` for hardware decisions -> `[Codex]` only for approved repo work
- input: local AI use case, model/surface, context type, security boundary, success criteria
- context needed: local AI experiment playbook, Ollama/Open WebUI pilot rules, model eval matrix, security boundary
- output: pilot plan or verdict with context rules, judge/revise step, limitations, security notes, and next step
- quality gate: experiment only; no production automation, autonomous retrieval, vector DB, embeddings, semantic search, MCP tools, web UI production workflow, secrets, or runtime artifacts
- done when: pilot is pass / revise / blocked with candidate / ready for owner review status
### `supervised_agent_loop_design`
- trigger: "Design a safe loop for this workflow"
- route: `[AI OS]` -> `[Thinking]` / `[Codex]` when implementation packaging is needed
- input: goal, owner project, allowed actions, checks, stop conditions, acceptance gate
- context needed: supervised loop boundary, promotion gates, tool decision matrix
- output: loop design with retry/rerun rule, stop conditions, owner acceptance point, and next trigger
- quality gate: supervised only; no autonomous retrieval, vector DB, embeddings, semantic search, web UI, or production agentic workflow
- done when: loop is pass/revise/blocked with candidate / ready for owner review status
### `cross_project_eval_review`
- trigger: "Check this AI output / PR / memo / workflow"
- route: `[AI OS]` for evidence/governance routing, then owner project by output type
- input: output/workflow result, intended use, source context, risk level
- context needed: eval registry, judge calibration, golden cases, owner project rules
- output: eval verdict with required fixes, residual risks, final quality status, next step
- quality gate: deterministic checks override LLM judge; unsupported claims listed; high-risk outputs require owner review
- done when: result is `pass`, `revise`, or `blocked` with concrete next action
## Candidate Packs
### `dashboard_critic`
- trigger: review dashboard usefulness, clarity, or decision support
- route: `[Analytics]` / `[Thinking]`
- input: dashboard screenshot, metrics list, audience, decision needed
- context needed: metric definitions, period, source layer, user workflow
- output: findings, risks, suggested fixes
- quality gate: separates visual critique from metric correctness
- done when: fixes are prioritized by decision impact
### `security_cleanup`
- trigger: remove risky public-repo artifacts or tighten repo safety wording
- route: `[Codex]`
- input: repo path, suspected exposure, desired cleanup scope
- context needed: safety scans, git status, affected docs/config
- output: minimal cleanup PR
- quality gate: no secrets are exposed, moved, or printed
- done when: repo safety checks pass and rollback is clear
### `weekly_ai_os_review`
- trigger: review AI-OS drift, open ideas, and next useful improvement
- route: `[AI OS]` -> `[Thinking]` / `[Codex]`
- input: week scope, recent issues/PRs, current friction
- context needed: GitHub state, repo docs, recent accepted changes
- output: concise review and one recommended next goal
- quality gate: does not create status ledgers or operating journals
- done when: one next action is clear
### `reconciliation_builder`
- trigger: build or improve a reconciliation workflow
- route: `[Analytics]` -> `[Codex]`
- input: source systems, join keys, periods, currency, expected outputs
- context needed: raw/stage/mart/report layers, schema, controls, exceptions
- output: reconciliation design or implementation PR
- quality gate: numeric logic is deterministic and source layers stay explicit
- done when: reconciliation output is reproducible and exceptions are traceable

## From: `docs/standards/COMMAND_SURFACE.md`

# Command Surface
This is the one-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from a result Sergey wants, not from an atomic task form.
| Command | Target project | Input | Output | Related Goal Pack |
|---|---|---|---|---|
| `AI-OS Goal` | `ai-os-orchestrator` -> resolved owner | goal; route optional | bounded owner context, execution or explicit handoffs, checks, rollback, acceptance, status | context-dependent |
| `ChatGPT Route` | `[Inbox Router]` | goal, task, message, or unclear request | target project and next prompt | context-dependent |
| `Goal -> Codex APP` | Codex APP | broad repo/workflow goal, GitHub issue, or handoff | branch, checks, PR, report | `codex_goal_to_pr` |
| `AI Trend` | `[AI OS]` | AI topic, release, tool, link, or question | trend verdict, relevance, risks, next step | `ai_trend_triage` |
| `Finance Memo` | `[Analytics]` -> `[LLM]` | data, period, currency, audience | data contract / QA / memo narrative | `finance_memo_factory` |
| `Analytics Loop` | `[Analytics]` | question, data sources, period, grain, filters | full cycle from data contract to findings, memo, QA, and next run | `analytics_factory_loop` |
| `Autoloop Analysis` | `[Analytics]` | question, data, QA criteria, stop conditions | supervised revise/rerun loop or blocker report | `supervised_autoloop_analysis` |
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
## Usage
- Press or type the command.
- Add the goal and only the context needed to start.
- `AI-OS Goal` is the default when no route is supplied; the orchestrator resolves the owner before loading project context.
- Use `ChatGPT Route` when the desired output is routing only.
- Let the resolved owner infer scope, checks, and next action within its boundary.
- Use strict task packages only when scope is already known or risk is high.

## From: `docs/standards/CONTEXT_PACK_STANDARD.md`

# Context Pack Standard
Context Packs are compact inputs for AI-OS, LLM, Analytics, and Codex workflows. They should contain the context needed for the next decision or output, not every available file.
## Minimal Schema
```markdown
# Context Pack
## Goal
## Decision needed
## Relevant files
## Facts
## Authority provenance
## Constraints
## Forbidden
## Open questions
## Expected output
## Quality gate
```
## Guidance
- Do not dump all files.
- Use curated context.
- Separate facts from assumptions.
- For each decision-relevant claim, retain its authority class, source
  reference, and action eligibility. The same claim text can have different
  eligibility when its authority differs.
- Mark missing evidence and open questions.
- Route deterministic calculations to `[Analytics]`.
- Route implementation, repo changes, checks, and PR work to `[Codex]`.
- Route AI evidence, governance, and trend interpretation to `[AI OS]`.
- Keep raw source files in the repo or source system; reference them instead of copying large bodies of text.
## Quality Gate
A Context Pack is ready when:
- the goal is clear;
- relevant files or sources are named;
- facts and assumptions are separated;
- decision-relevant claims retain authority provenance and action eligibility;
- constraints and forbidden actions are visible;
- the expected output is specific;
- the receiving project can act without asking Sergey to write an atomic task package.

## From: `docs/standards/PROMPT_QA_FACTORY.md`

# Prompt QA Factory
Prompt QA Factory is the AI-OS standard for turning reusable prompts into accepted prompt assets.
It applies to StreamDeck prompts, ChatGPT Project prompts, Codex prompts, Judge/Revisor prompts, and Analytics memo prompts.
## Core Loop
```text
candidate -> test -> judge -> revise -> selected
```
The loop is supervised only. A prompt is not selected until a human accepts the final version.
## Statuses
| Status | Meaning |
|---|---|
| `candidate` | Draft prompt proposed for a repeated use case. It may be useful, but it is not accepted yet. |
| `test` | Candidate is run against small, representative cases. |
| `judge` | Output is reviewed against explicit criteria and risks. |
| `revise` | Prompt is changed only to address observed test or judge findings. |
| `selected` | Final prompt is accepted for reuse by the owner reviewer. |
## How To Test
Use the smallest representative set of cases that shows whether the prompt is useful in real work.
Each test should record:
- input context;
- expected output shape;
- actual output or observed behavior;
- friction points;
- unsupported claims or missing constraints;
- whether the prompt stayed inside the allowed scope.
For Analytics memo prompts, deterministic calculations must happen in Python or SQL before the prompt writes or reviews narrative.
## How To Judge
Judge against the intended workflow, not against whether the prompt sounds polished.
Minimum criteria:
- goal fit;
- output schema fit;
- source discipline;
- low-friction UX;
- no invented facts;
- no hidden automation;
- no sensitive data exposure;
- residual risks visible.
## Revision Rule
Revise only from observed evidence:
- failed or weak test case;
- judge finding;
- user friction;
- missing acceptance requirement;
- unsafe or unsupported behavior.
Do not broaden the prompt into a general agent, autonomous workflow, retrieval system, or production automation.
## Selection Rule
A prompt can be marked `selected` only when:
- test cases are recorded;
- judge criteria are recorded;
- UX score is recorded;
- residual risks are recorded;
- owner acceptance status is `accepted`;
- no blocked item is required.
## Supervision Boundary
Prompt QA Factory follows AI-OS supervised loop governance.
Allowed:
- local prompt drafting and revision;
- human-reviewed test cases;
- judge/revisor review;
- repository documentation or PR diffs;
- candidate / ready-for-human-review status before acceptance.
Forbidden:
- production automation;
- sensitive data;
- autonomous retrieval;
- vector DB, embeddings, or semantic search;
- auto-merge;
- claiming production readiness.
## UX Score
Record UX score as `1` to `5`.
| Score | Meaning |
|---|---|
| `1` | Confusing or high-friction. |
| `2` | Usable only with extra explanation. |
| `3` | Works for the narrow case but has visible friction. |
| `4` | Reusable with minor residual risks. |
| `5` | Low-friction, clear, and ready for accepted reuse. |
## Prompt QA Record
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
## Use By Prompt Type
| Prompt type | Owner | Typical test |
|---|---|---|
| StreamDeck prompts | `[LLM]` / `[Codex]` | Button command produces the intended low-friction result. |
| ChatGPT Project prompts | Owner project | Project follows source, routing, and output rules. |
| Codex prompts | `[Codex]` | Repo task stays bounded, reversible, and verifiable. |
| Judge/Revisor prompts | `[Thinking]` / `[LLM]` | Judge finds unsupported claims; Revisor improves without adding claims. |
| Analytics memo prompts | `[Analytics]` / `[LLM]` | Narrative uses deterministic results and shows assumptions, periods, currencies, and risks. |
## Done Criteria
The prompt record is complete, the final prompt is selected or explicitly left as a candidate, residual risks are visible, and owner acceptance is recorded.

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
## Removal from active layer
Active layer:
Change needed:
Replacement pointer:
Rollback note:
## Human acceptance
- [ ] Reviewer accepted archive / superseded status.
- [ ] Reviewer accepted replacement or `none`.
- [ ] Reviewer accepted traceability note.
- [ ] No production promotion is implied.

## From: `ChatGPT/[AI OS]/Knowledge/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`.
## Legacy section: `docs/standards/GOAL_PACKS.md`
Goal Packs are reusable workflows for broad goals. Sergey starts from intent; AI-OS, LLM, Analytics, or Codex infer safe execution details.
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
| `prompt_qa_factory` | turn a reusable prompt into an accepted standard | `[AI OS]` -> owner project -> `[LLM]` / `[Thinking]` judge-revisor when needed -> `[Codex]` only for repo docs or PR work | Prompt QA Record with candidate -> test -> judge -> revise -> selected status, UX score, residual risks, and acceptance status | supervised only; human-owned acceptance required; no production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, and follow merge policy in `GOAL_MODE.md` |
### Candidate packs
| Pack | Route | Purpose | Promotion caution |
|---|---|---|---|
| `dashboard_critic` | `[Analytics]` / `[Thinking]` | review dashboard usefulness, clarity, or decision support | separate visual critique from metric correctness |
| `security_cleanup` | `[Codex]` | repo-only safety cleanup for risky public-repo artifacts or safety wording | not full access/security management |
| `weekly_ai_os_review` | `[AI OS]` -> `[Thinking]` / `[Codex]` | review drift and choose one next useful improvement | do not create status ledgers or operating journals |
| `reconciliation_builder` | `[Analytics]` -> `[Codex]` | build or improve reconciliation workflow | keep numeric logic deterministic and source layers explicit |
## Legacy section: `docs/standards/COMMAND_SURFACE.md`
One-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from the result Sergey wants, not from an atomic task form.
| `Autoloop Analysis` | `[Analytics]` | question, data, QA criteria, stop conditions | supervised revise/rerun loop or blocker report | `autoloop` |
Usage:
## Legacy section: `docs/standards/CONTEXT_PACK_STANDARD.md`
Context Packs are compact inputs for AI-OS, LLM, Analytics, and Codex workflows. They contain the context needed for the next decision or output, not every available file.
### Minimal schema
### Guidance
### Quality gate
A Context Pack is ready when the goal is clear, sources are named, facts and assumptions are separated, constraints and forbidden actions are visible, the expected output is specific, and the receiving project can act without asking Sergey to write an atomic task package.
## Legacy section: `docs/standards/PROMPT_QA_FACTORY.md`
Core loop:
Applies to StreamDeck prompts, ChatGPT Project prompts, Codex prompts, Judge/Revisor prompts, and Analytics memo prompts.
Selection requires recorded test cases, judge criteria, UX score, residual risks, and owner acceptance.
Forbidden: production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, auto-merge, and claims of production readiness.
### Prompt QA Record
