# Command Surface

This is the one-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from a result Sergey wants, not from an atomic task form.

| Command | Target project | Input | Output | Related Goal Pack |
|---|---|---|---|---|
| `GOAL -> Codex` | `[Codex]` | broad repo/workflow goal, GitHub issue, or handoff | branch, checked diff, PR for review | `codex_goal_to_pr` |
| `AI Trend` | `[AI OS]` | AI topic, release, tool, link, or question | trend verdict, relevance, risks, next step | `ai_trend_triage` |
| `Finance Memo` | `[Analytics]` -> `[LLM]` | data, period, currency, audience | data contract / QA / memo narrative | `finance_memo_factory` |
| `Audit Anomaly` | `[Analytics]` | anomaly, account/entity, period, expected behavior | finding, evidence, risk, recommended action | `audit_anomaly_review` |
| `StreamDeck Improve` | `[LLM]` / `[Codex]` | current button/prompt and desired result | improved prompt or PR | `streamdeck_prompt_upgrade` |
| `Judge` | `[LLM]` | draft, claims, context, evidence limits | pass / revise / blocked with findings | context-dependent |
| `Revisor` | `[LLM]` | draft plus judge notes | clearer final without new claims | context-dependent |
| `Context Pack` | `[LLM]` | goal, files, facts, constraints, expected output | compact reusable context pack | context-dependent |
| `Sync Readiness` | `[Codex]` | repo branch or local checkout | validation results and sync guidance | `codex_goal_to_pr` |

## Usage

- Press or type the command.
- Add the goal and only the context needed to start.
- Let the target project infer route, scope, checks, and next action.
- Use strict task packages only when scope is already known or risk is high.
