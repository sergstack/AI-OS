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
- done when: PR exists with summary, risks, rollback, and "Do not merge automatically"

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
- context needed: `PROMPT_QA_FACTORY.md`, supervised loop boundary, prompt registry/library, owner project rules
- output: Prompt QA Record with candidate -> test -> judge -> revise -> selected status, UX score, residual risks, and acceptance status
- quality gate: supervised only; human-owned acceptance required; no production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, or auto-merge
- done when: prompt is selected by owner acceptance or remains a candidate with visible risks and next revision need

### `context_pack_builder`

- trigger: "Build a compact context package or prompt from this goal"
- route: `[LLM]` -> owner project by output type
- input: goal, source files or facts, constraints, expected output, risk level
- context needed: `CONTEXT_PACK_STANDARD.md`, prompt registry, routing rules, raw-dump guardrails
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
