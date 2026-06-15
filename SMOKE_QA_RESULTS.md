# Smoke QA Results — AI OS

Smoke QA is not production readiness.
It only verifies that the ChatGPT Project follows routing, KB usage, evidence rules, and governance.

| Date | Area | Question | Expected result | Actual result | Verdict | Fix required |
|---|---|---|---|---|---|---|
| 2026-05-25 | Navigation | Какие два индекса есть в [AI OS] и чем они отличаются? | Names `KB__00_INDEX.md` and `AI_OS_PROJECT_FILES_INDEX.md` correctly | not_run | not_run | Run after upload |
| 2026-05-25 | Scope | Для чего использовать [AI OS], а что отправлять в [LLM], [Analytics], [Thinking] и [Codex]? | Routes tasks correctly and says AI OS does not write code or run financial calculations | not_run | not_run | Run after upload |
| 2026-05-25 | Evidence | Объясни любой AI-паттерн из KB и укажи confidence/evidence. | Checks KB and separates supported/weak/unsupported | not_run | not_run | Run after upload |
| 2026-05-25 | Governance | Можно ли сейчас добавлять embeddings, semantic search или vector DB? | Says blocked until acceptance/promotion gate | not_run | not_run | Run after upload |
| 2026-05-25 | Handoff | Мне нужно превратить найденный AI-паттерн в задачу для Codex. Что делать? | Gives handoff to [Codex] with goal, context, constraints, acceptance criteria | not_run | not_run | Run after upload |
| 2026-06-15 | Repo governance | Are all PROJECT_INSTRUCTIONS.md files <= 8000 characters? | Validation script reports all pass | not_run | not_run | Run `python3 scripts/check_project_instructions_length.py` |
| 2026-06-15 | Operational verification | Is ChatGPT Project sync and pilot evidence recorded? | `CHATGPT_PROJECT_SYNC_CHECKLIST.md`, `SMOKE_QA_REFRESH_PLAN.md`, and `PILOT_CASES.md` are updated after manual sync | not_run | not_run | Run after manual ChatGPT Project sync |
