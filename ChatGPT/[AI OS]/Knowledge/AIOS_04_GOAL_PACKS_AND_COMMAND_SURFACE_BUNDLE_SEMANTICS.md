# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`.

## Legacy section: `GOAL_PACKS.md`

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

## Legacy section: `COMMAND_SURFACE.md`

One-touch command map for AI-OS, Stream Deck buttons, and quick prompts. Each command starts from the result Sergey wants, not from an atomic task form.
| `Autoloop Analysis` | `[Analytics]` | question, data, QA criteria, stop conditions | supervised revise/rerun loop or blocker report | `autoloop` |
Usage:

## Legacy section: `CONTEXT_PACK_STANDARD.md`

Context Packs are compact inputs for AI-OS, LLM, Analytics, and Codex workflows. They contain the context needed for the next decision or output, not every available file.
### Minimal schema
### Guidance
### Quality gate
A Context Pack is ready when the goal is clear, sources are named, facts and assumptions are separated, constraints and forbidden actions are visible, the expected output is specific, and the receiving project can act without asking Sergey to write an atomic task package.

## Legacy section: `PROMPT_QA_FACTORY.md`

Core loop:
Applies to StreamDeck prompts, ChatGPT Project prompts, Codex prompts, Judge/Revisor prompts, and Analytics memo prompts.
Selection requires recorded test cases, judge criteria, UX score, residual risks, and owner acceptance.
Forbidden: production automation, sensitive data, autonomous retrieval, vector DB, embeddings, semantic search, auto-merge, and claims of production readiness.
### Prompt QA Record
