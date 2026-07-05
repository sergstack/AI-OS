# Goal Packs

Goal Packs are reusable workflows for broad goals. They help Sergey start from intent while AI-OS, LLM, Analytics, or Codex infer the safe execution details.

Goal Packs are not atomic task packages. Codex still compiles internal scope, checks, rollback, and acceptance criteria before editing.

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
- output: branch, minimal diff, checks, PR for human review
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

### `local_ai_experiment`

- trigger: test a local AI idea without production promotion
- route: `[LLM]` / `[Codex]`
- input: hypothesis, sample input, success criteria, local constraints
- context needed: model routing, privacy needs, evaluation method
- output: experiment plan or local prototype PR
- quality gate: marked as experiment, not production-ready
- done when: pilot result or blocker is documented without adding heavy status layers

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
