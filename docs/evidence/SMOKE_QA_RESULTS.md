# Smoke QA Results — AI OS

Date: 2026-07-06
Project: `[AI OS]`
Repository branch checked: `main`
Repository commit checked: `ec13f14`
ChatGPT Project URL checked: `https://chatgpt.com/g/g-p-6a0512a228c88191afcc953866789dad-ai-os/project`
Final quality status: `candidate / ready for human review`

Smoke QA is not production readiness.
This report records repository checks and direct ChatGPT UI smoke QA evidence.

**Coverage note (added 2026-09-03):** this record predates roughly 15
`Knowledge/` additions/updates made 2026-08-25 through 2026-09-02, including
the `ACT_OR_ABSTAIN_EVAL_GATE.md` / `GOAL_CONSISTENCY_CLOSURE_CHECK.md` /
`FAILURE_REGISTRY.md` / `REGRESSION_GATE.md` / `INTERMEDIATE_STATE_ASSERTIONS.md`
eval-gate family, `AI_OS_PROJECT_FILES_INDEX.md` (2026-08-31), and the
Supervised AI-OS Subagent Dispatch pilot in `AGENT_LOOP_PLAYBOOK.md`
(2026-09-02). None of that later content has been verified against the live
ChatGPT UI. Re-running this smoke QA against current bundles (including the just-added
`AIOS_06_CROSS_PROJECT_AI_EVALS.md` coverage of the eval-gate family, this
same change) is the next action, not something this note substitutes for.
See `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`.

## Browser UI Evidence

- Project Instructions visible: yes. Project settings showed the project name `[AI OS]` and an Instructions field beginning with `# [AI OS] Project Instruction`.
- Project Knowledge visible: yes. The Sources tab showed all six compact bundle files dated 2026-07-06: `AIOS_01_ROUTING_AND_WORKFLOW.md`, `AIOS_02_GOVERNANCE_AND_EVIDENCE.md`, `AIOS_03_HANDOFF_AND_SMOKE_QA.md`, `AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`, `AIOS_05_SUPERVISED_AGENT_LOOPS.md`, `AIOS_06_CROSS_PROJECT_AI_EVALS.md`.
- Governed KB visible: yes. The Sources tab also showed governed KB files including `KB__00_INDEX.md`, `KB__01_NAVIGATION.md`, `KB__02_CONTENT.md`, `KB__08_USE_CASES_FOR_SERGEY.md`, `KB__PROMOTION_GATES.md`, `KB__RELEASE_MANIFEST.md`, and `KB__USE_CASE_ROUTING.md`.

## Files Checked

- `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md`
- `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_01_ROUTING_AND_WORKFLOW.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_02_GOVERNANCE_AND_EVIDENCE.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_05_SUPERVISED_AGENT_LOOPS.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_06_CROSS_PROJECT_AI_EVALS.md`
- `../operations/SMOKE_QA_REFRESH_PLAN.md`
- `../operations/CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- `../operations/PILOT_CASES.md`
- `archive/reports/KB_COMPACT_CONSISTENCY_REPORT.md`

## ChatGPT UI Smoke QA

The seven QA questions were run in one new `[AI OS]` project chat.
The captured answer began with the required evidence header: `KB проверен: да`, listed AIOS bundle sources, reported `Найдено в KB: да`, `Confidence: medium`, and `Evidence: supported`.

| # | QA area | Question | Expected result | Actual result | Verdict | Evidence links / repo paths | Fix required |
|---:|---|---|---|---|---|---|---|
| 1 | Navigation | Какие два индекса есть в [AI OS] и чем они отличаются? | Names `KB__00_INDEX.md` and `AI_OS_PROJECT_FILES_INDEX.md`; separates governed KB index from project settings/workflow index. | Named `KB__00_INDEX.md` as governed KB index for knowledge/concepts/patterns/workflows/evidence and `AI_OS_PROJECT_FILES_INDEX.md` as working index for routing, usage rules, handoff, smoke QA, and project settings. | pass | UI answer; `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`; `ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md` | no |
| 2 | Scope / Routing | Для чего использовать [AI OS], а что нужно отправлять в [LLM], [Analytics], [Thinking] и [Codex]? | Does not mix project roles; states that `[AI OS]` does not write code, run pipelines, or perform financial calculations. | Routed AI concepts/use cases/evidence/governance to `[AI OS]`, prompts/model routing/orchestration to `[LLM]`, calculations/marts/metrics/data QA to `[Analytics]`, strategy/risks/decision memo to `[Thinking]`, and code/repo/tests/pipelines/PR implementation to `[Codex]`; explicitly said `[AI OS]` does not write code, calculate financial models, or do production execution. | pass | UI answer; `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_01_ROUTING_AND_WORKFLOW.md` | no |
| 3 | Evidence | Объясни любой AI-паттерн из KB и укажи confidence/evidence. | Checks KB, lists sources, separates supported / weak / unsupported, includes confidence. | Explained AutoResearch / Karpathy loop as action -> check -> revise/rerun -> acceptance; cited `KB__02_CONTENT.md` card/source/chunk evidence; stated `Confidence: medium` and `Evidence: supported, но не production-ready`. | pass | UI answer; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_02_GOVERNANCE_AND_EVIDENCE.md`; `KB__02_CONTENT.md` visible in UI Sources | no |
| 4 | Governance gates | Можно ли сейчас добавлять embeddings, semantic search или vector DB? | Says blocked until explicit acceptance/promotion gate; does not recommend as current implementation. | Said embeddings / semantic search / vector DB cannot be added as a current recommendation, are blocked promotion items until acceptance / promotion gate, and may only be discussed as future backlog / hypothesis. | pass | UI answer; `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_02_GOVERNANCE_AND_EVIDENCE.md`; `MANIFEST.json` | no |
| 5 | Handoff to Codex | Мне нужно превратить найденный AI-паттерн в задачу для Codex. Что делать? | Gives handoff to `[Codex]` with goal, context, evidence, constraints, checks, acceptance criteria, and no auto-merge. | Said to create a `[Codex]` handoff with goal, context from AI OS, KB evidence, scope, allowed files, forbidden changes, checks, risks, acceptance criteria, expected PR summary, and `do not merge automatically`; recommended GitHub Issue -> Codex branch -> checks -> PR -> human review. | pass | UI answer; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md` | no |
| 6 | Goal Mode behavior | Хочу улучшить AI-OS repo без атомарного ТЗ. Что должно произойти? | Explains broad goal -> route -> infer scope -> checks -> PR -> human review; does not force Sergey to write an atomic task package unless risk requires strict mode. | Said Goal Mode should accept Sergey's broad goal, form context and constraints, have Codex compile internal scope/checks/rollback/acceptance criteria, and not force Sergey to write an atomic task by hand. | pass | UI answer; `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`; `AGENTS.md` | no |
| 7 | Supervised loop boundary | Можно ли сделать autoloop для оптимизации prompts? | Allows supervised loop only; requires owner, bounded action, checks, stop conditions, human acceptance; blocks autonomous retrieval / production agentic workflow. | Allowed only a supervised loop: goal -> prompt change -> eval/judge rubric check -> revise/rerun -> human acceptance; required owner, bounded actions, stop conditions, checks, and human acceptance; blocked uncontrolled multi-agent execution or production agentic workflow without gates. | pass | UI answer; `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_05_SUPERVISED_AGENT_LOOPS.md` | no |

## Repository Checks

| Check | Result | Evidence |
|---|---|---|
| `python3 scripts/check_project_instructions_length.py` | pass | 6 `PROJECT_INSTRUCTIONS.md` files checked; 6 passed; 0 failed; `[AI OS]` chars=7017, limit=8000. |
| `python3 scripts/check_repo_public_safety.py` | pass | Public safety check passed; includes project instructions length check. |
| `python3 scripts/check_manifest_paths.py` | pass | 112 checks; 112 passed; 0 failed. |
| `python3 scripts/check_knowledge_bundles.py` | pass | 6 projects checked; 30 bundles checked; failed=0. |
| `python3 scripts/sync_aios.py` | pass | Internal checks passed; helper printed sync readiness guidance and did not upload, push, or modify remote systems. |
| `git diff --check` | pass | No whitespace errors reported. |

## Blockers

- Pilot execution is not complete. `../operations/PILOT_CASES.md` still records `PILOT-AIOS-001` as `draft` with `unsupported` confidence.
- Production promotion remains `no`.

## Residual Risks

- The UI smoke QA was run as one combined seven-question prompt, not seven isolated fresh chats.
- Project Instructions were visible in ChatGPT settings, but this report did not compare the full UI instructions byte-for-byte against the repository file.
- Repository checks and UI smoke QA do not prove pilot success or production readiness.

## PR Summary Draft

- QA run: direct ChatGPT UI smoke QA for `[AI OS]`, plus repository checks from issue #59.
- Passed / failed / not run: all seven UI smoke QA questions passed; all requested repository checks passed; no requested check was unrun.
- ChatGPT UI sync evidenced: yes, Project Instructions field and Knowledge Sources were visible in ChatGPT UI.
- Checks run: `python3 scripts/check_project_instructions_length.py`, `python3 scripts/check_repo_public_safety.py`, `python3 scripts/check_manifest_paths.py`, `python3 scripts/check_knowledge_bundles.py`, `python3 scripts/sync_aios.py`, `git diff --check`.
- Risks / limitations: UI test used one combined prompt; full Project Instructions were not byte-for-byte compared; pilot remains incomplete; no production promotion.
- Rollback: revert this documentation update and the `[AI OS]` sync checklist row update.
- Acceptance status: `candidate / ready for human review`.

## Next Step

Execute `PILOT-AIOS-001`, record pilot evidence with `../operations/PILOT_RESULTS_TEMPLATE.md`, and keep production promotion blocked until required pilots pass and are accepted by the human owner.
