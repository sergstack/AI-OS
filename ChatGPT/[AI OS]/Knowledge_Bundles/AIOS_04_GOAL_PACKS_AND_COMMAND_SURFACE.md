# [AI OS] — Goal Packs and Command Surface

## Purpose

Compact upload artifact for [AI OS] covering the first Goal Packs layer, one-touch command surface, and context pack standard.

## Source files

- `GOAL_PACKS.md`
- `COMMAND_SURFACE.md`
- `CONTEXT_PACK_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: root files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- default_upload_mode: `Knowledge_Bundles`

---

# Content

## From: `GOAL_PACKS.md`

Goal Packs are reusable workflows for broad goals. Sergey starts from intent; AI-OS, LLM, Analytics, or Codex infer safe execution details.

Goal Packs are not atomic task packages. Codex still compiles internal scope, checks, rollback, and acceptance criteria before editing.

### Active packs

| Pack | Trigger | Route | Output | Quality gate |
|---|---|---|---|---|
| `ai_trend_triage` | "What changed in AI and does it matter for me?" | `[AI OS]` -> `[Thinking]` or `[LLM]` if needed | short verdict, use cases, risks, next step | supported / weak / unsupported claims separated |
| `codex_goal_to_pr` | repo/workflow improvement or Goal Mode GitHub issue | `[Codex]` | branch, minimal diff, checks, PR for human review | no atomic-task burden; checks pass or blockers are reported |
| `finance_memo_factory` | finance memo from data | `[Analytics]` -> `[LLM]` -> `[Codex]` only when repo artifact, automation, or executable package is needed -> judge/revise | memo narrative from Analytics facts; executable artifact or PR only when needed | calculations use Python or SQL |
| `analytics_factory_loop` | full analytics cycle for a question | `[Analytics]` -> `[LLM]` for narrative -> `[Codex]` only for artifacts/repo changes | compact analytical answer or memo with method, QA, limitations, and next run trigger | deterministic calculation before findings |
| `supervised_autoloop_analysis` | iterate analysis until QA passes or blockers are clear | `[Analytics]` | revised findings or blocker report | supervised loop only; stop on DQ fail, unclear grain, missing contract, or no validation path |
| `audit_anomaly_review` | anomaly, variance, or suspicious record | `[Analytics]` -> `[Thinking]` if decision framing is needed | finding, likely cause, evidence, risk, recommended action | no LLM arithmetic |
| `streamdeck_prompt_upgrade` | improve a Stream Deck / quick prompt workflow | `[LLM]` -> `[Codex]` when repo edits are needed | tighter prompt or repo PR | prompt is short, routable, evidence-aware, and does not add unsupported automation |

### Candidate packs

| Pack | Route | Purpose | Promotion caution |
|---|---|---|---|
| `dashboard_critic` | `[Analytics]` / `[Thinking]` | review dashboard usefulness, clarity, or decision support | separate visual critique from metric correctness |
| `security_cleanup` | `[Codex]` | repo-only safety cleanup for risky public-repo artifacts or safety wording | not full access/security management |
| `local_ai_experiment` | `[LLM]` / `[Codex]` | test a local AI idea | mark as experiment, not production-ready |
| `weekly_ai_os_review` | `[AI OS]` -> `[Thinking]` / `[Codex]` | review drift and choose one next useful improvement | do not create status ledgers or operating journals |
| `reconciliation_builder` | `[Analytics]` -> `[Codex]` | build or improve reconciliation workflow | keep numeric logic deterministic and source layers explicit |

## From: `COMMAND_SURFACE.md`

One-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from the result Sergey wants, not from an atomic task form.

| Command | Target project | Input | Output | Related Goal Pack |
|---|---|---|---|---|
| `GOAL -> Codex` | `[Codex]` | broad repo/workflow goal, GitHub issue, or handoff | branch, checked diff, PR for review | `codex_goal_to_pr` |
| `AI Trend` | `[AI OS]` | AI topic, release, tool, link, or question | trend verdict, relevance, risks, next step | `ai_trend_triage` |
| `Finance Memo` | `[Analytics]` -> `[LLM]` | data, period, currency, audience | data contract / QA / memo narrative | `finance_memo_factory` |
| `Analytics Loop` | `[Analytics]` | question, data sources, period, grain, filters | full cycle from data contract to findings, memo, QA, and next run | `analytics_factory_loop` |
| `Autoloop Analysis` | `[Analytics]` | question, data, QA criteria, stop conditions | supervised revise/rerun loop or blocker report | `supervised_autoloop_analysis` |
| `Audit Anomaly` | `[Analytics]` | anomaly, account/entity, period, expected behavior | finding, evidence, risk, recommended action | `audit_anomaly_review` |
| `StreamDeck Improve` | `[LLM]` / `[Codex]` | current button/prompt and desired result | improved prompt or PR | `streamdeck_prompt_upgrade` |
| `Judge` | `[LLM]` | draft, claims, context, evidence limits | pass / revise / blocked with findings | context-dependent |
| `Revisor` | `[LLM]` | draft plus judge notes | clearer final without new claims | context-dependent |
| `Context Pack` | `[LLM]` | goal, files, facts, constraints, expected output | compact reusable context pack | context-dependent |
| `Sync Readiness` | `[Codex]` | repo branch or local checkout | validation results and sync guidance | `codex_goal_to_pr` |

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
