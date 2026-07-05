# Command Surface

This is the one-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from a result Sergey wants, not from an atomic task form.

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
| `PR Judge` | `[Thinking]` / `[Codex]` | PR link, goal, checks, risks | pass / revise / blocked review | context-dependent |
| `Revisor` | `[LLM]` | draft plus judge notes | clearer final without new claims | context-dependent |
| `Context Pack` | `[LLM]` | goal, files, facts, constraints, expected output | compact reusable context pack | context-dependent |
| `Sync Check` | `[Codex]` / Codex APP | repo branch or local checkout | repo checks plus sync guidance | `codex_goal_to_pr` |

## Usage

- Press or type the command.
- Add the goal and only the context needed to start.
- Let the target project infer route, scope, checks, and next action.
- Use strict task packages only when scope is already known or risk is high.
