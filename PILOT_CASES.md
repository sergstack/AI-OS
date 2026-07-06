# Pilot Cases

## Purpose

Define minimum viable pilot cases that prove each project can operate from synchronized repository settings.

P3 defines backlog pilot definitions only. Do not mark a pilot complete until there is explicit result evidence.

Manifest/upload status: operational verification file; not a ChatGPT Project Knowledge upload bundle.

Allowed pilot statuses: `backlog`, `candidate`, `active`, `accepted`, `deprecated`, `blocked`.

## Pilot status summary

| Pilot ID | Project | Status | Confidence | Owner | Next step |
|---|---|---|---|---|---|
| `PILOT-AIOS-001` | `[AI OS]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-THINKING-001` | `[Thinking]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-ANALYTICS-001` | `[Analytics]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-LLM-001` | `[LLM]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-CODEX-001` | `[Codex]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-INBOX-001` | `[Inbox Router]` | backlog | unsupported | Sergey | Sync project, run smoke QA, then execute pilot |
| `PILOT-CODEXAPP-001` | Codex APP | backlog | unsupported | Sergey | Run local task package classification pilot |
| `PILOT-CROSS-001` | Cross-project | backlog | unsupported | Sergey | Execute after individual pilots are defined |

## [AI OS] Pilot

Pilot ID: `PILOT-AIOS-001`
Project: `[AI OS]`
Goal: Take one current AI topic or tool, check KB/fresh source separation, label evidence as supported / weak / unsupported, and produce routing/handoff.
Input: "Assess a current AI tool or pattern and decide whether it belongs in AI OS governance, LLM workflow, Analytics, Thinking, or Codex."
Expected behavior: The project separates KB evidence from fresh external checks, labels confidence, avoids blocked implementation recommendations, and gives one handoff.
Evidence required: ChatGPT response, KB files consulted or explicit not-found statement, any fresh source list if used, final routing/handoff.
Success criteria: KB checked / not found clearly stated; fresh external check separated if used; supported / weak / unsupported separated; no blocked feature recommended as current implementation; one clear next step.
Failure criteria: Claims unsupported evidence as fact; recommends embeddings, semantic search, vector DB, web UI, or autonomous retrieval as current implementation; omits routing/handoff.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: AI OS project instructions, Knowledge files, evidence rules, or blocked promotion gates change.
Next step: Sync `[AI OS]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## [Thinking] Pilot

Pilot ID: `PILOT-THINKING-001`
Project: `[Thinking]`
Goal: Create one decision memo from a real strategic/business/process choice.
Input: "Choose between three realistic options for a project/process decision and produce a decision memo."
Expected behavior: The project frames options, separates facts and assumptions, evaluates risks, assigns decision status, and includes revisit trigger.
Evidence required: Decision memo, assumptions list, risks, chosen recommendation or candidate decision, revisit trigger.
Success criteria: 2-4 options; facts / assumptions separated; risks listed; decision status assigned; revisit trigger included; handoff if needed.
Failure criteria: Gives a recommendation without assumptions or risks; omits status; performs Analytics/Codex work instead of decision framing.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: decision status rules, routing rules, or judge/revisor standards change.
Next step: Sync `[Thinking]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## [Analytics] Pilot

Pilot ID: `PILOT-ANALYTICS-001`
Project: `[Analytics]`
Goal: Use a small sample dataset or real lightweight analytical case to define data contract, stage, mart, QA checks, findings, and limitations.
Input: "Given a small tabular dataset, define the analysis contract and produce traceable findings without changing raw data."
Expected behavior: The project defines grain, period, filters, stage/mart design, QA checks, findings, and limitations.
Evidence required: Data contract, stage/mart plan or files, QA checklist, traceable findings, limitations.
Success criteria: grain / period / filters explicit; data contract present; stage_main_full and mart_main_full designed or created; QA checks listed; claims traceable to data/mart; limitations visible.
Failure criteria: Uses unsupported calculations; mixes raw/stage/mart/report layers; omits assumptions or limitations; routes implementation directly to Codex without analysis contract.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: analytics workflow, data contract, QA, or mart standards change.
Next step: Sync `[Analytics]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## [LLM] Pilot

Pilot ID: `PILOT-LLM-001`
Project: `[LLM]`
Goal: Create one reusable prompt/workflow item with model class routing, judge/revise loop, failure modes, and eval result.
Input: "Create a reusable prompt registry item for a bounded LLM workflow with quality gate and judge/revise handling."
Expected behavior: The project defines prompt metadata, input requirements, output schema, model class routing, quality gate, and eval or judge result.
Evidence required: Prompt/workflow item, routing rationale, quality gate, judge/revise result or explicit not-needed rationale.
Success criteria: prompt_id assigned; input requirements listed; output schema defined; model class selected by task, not hardcoded permanent model name; quality gate defined; judge/revise applied or explicitly not needed.
Failure criteria: Hardcodes a permanent model name without task rationale; lacks output contract; adds unsupported claims; omits quality gate.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: model routing, prompt registry, quality gate, or eval standard changes.
Next step: Sync `[LLM]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## [Codex] Pilot

Pilot ID: `PILOT-CODEX-001`
Project: `[Codex]`
Goal: Run one docs-only issue-driven Codex task from issue/task package to branch, checks, PR, human review, and no auto-merge.
Input: "Implement a small docs-only repo hygiene task from a complete task package."
Expected behavior: The project validates package completeness, uses a branch, runs checks, opens a PR, and waits for human review.
Evidence required: Task package, branch, changed files, checks, PR link, no auto-merge note.
Success criteria: task package has objective, scope, allowed files, forbidden actions, acceptance criteria, checks, rollback; branch used; checks run; PR opened; human review required; no auto-merge.
Failure criteria: Edits main directly; skips checks; widens scope without approval; merges automatically.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: Codex project instructions, task package protocol, or GitHub flow changes.
Next step: Sync `[Codex]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## [Inbox Router] Pilot

Pilot ID: `PILOT-INBOX-001`
Project: `[Inbox Router]`
Goal: Classify 20 raw inputs into target projects or mark unclear.
Input: "20 mixed raw requests spanning decisions, analytics, implementation, AI OS governance, LLM workflow, and unclear notes."
Expected behavior: The router assigns one target or unclear status, explains why, and gives next action without doing the target project's work.
Evidence required: Input list, routing table, reasons, unclear cases, next actions.
Success criteria: each input routed to one project or marked unclear; unclear cases are not forced; output includes reason and next action; no project absorbs responsibilities incorrectly.
Failure criteria: Forces unclear cases; performs decision/analytics/Codex work inside Router; omits reasons.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: project roles, routing rules, or Inbox Router schema changes.
Next step: Sync `[Inbox Router]`, run smoke QA, then record result with `PILOT_RESULTS_TEMPLATE.md`.

## Codex APP Pilot

Pilot ID: `PILOT-CODEXAPP-001`
Project: Codex APP
Goal: Verify that Codex APP task package contract can classify an ultra-long local task package into mode, allowed files, forbidden actions, batch plan, checkpoints, checks, rollback, and final response format.
Input: "One ultra-long-local task package with allowed files, forbidden actions, batch plan, checkpoint policy, checks, and rollback."
Expected behavior: Codex APP classifies the task package and produces a controlled execution plan without claiming external UI sync.
Evidence required: Local Codex output, batch/checkpoint classification, allowed/forbidden files, checks and rollback list.
Success criteria: mode classified; allowed files identified; forbidden actions identified; batch plan present; checkpoint policy present; validation checks listed; rollback present.
Failure criteria: Starts uncontrolled autonomy; ignores forbidden files; omits rollback or final response format.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: Codex APP templates, ultra-long protocol, or local execution contract changes.
Next step: Run local Codex APP pilot and record result with `PILOT_RESULTS_TEMPLATE.md`.

## Cross-project pilot

Pilot ID: `PILOT-CROSS-001`
Project: Cross-project
Goal: Take one realistic request and route it through Thinking -> Analytics / LLM / Codex / AI OS as needed.
Input: "A realistic request requiring decision framing, possible analysis, prompt/workflow design, implementation task packaging, and AI OS governance review."
Expected behavior: The projects hand off clearly without doing each other's work.
Evidence required: Routing decision, handoff package(s), final status, project boundaries observed.
Success criteria: routing decision explained; no project does another project's job; handoff package created when needed; final status recorded.
Failure criteria: Role confusion; missing handoff; unsupported production readiness claim.
Owner: Sergey
Status: backlog
Confidence: unsupported
Revisit trigger: any project role, handoff, or production promotion policy changes.
Next step: Run after individual project sync records are available.

## Acceptance rules

- A pilot is complete only when result evidence is recorded.
- Production promotion remains `no` until required pilots pass.
- Failed pilots must record failure criteria, blocker, and next step.
- Cross-project pilot should run after individual pilots are at least candidate-ready.

## Blockers

- ChatGPT Project UI sync is not verified in this repository.
- Pilot results are not yet recorded.
- Smoke QA refresh has not yet been run after sync.

## Next steps

1. Complete `CHATGPT_PROJECT_SYNC_CHECKLIST.md` after manual ChatGPT Project sync.
2. Run smoke QA using `SMOKE_QA_REFRESH_PLAN.md`.
3. Record pilot results with `PILOT_RESULTS_TEMPLATE.md`.
4. Update pilot statuses only when evidence exists.
