# Project Folder Consistency Report

## Summary

Status: `candidate / ready for human review`.

The six ChatGPT project folders have consistent required structure:

- `PROJECT_INSTRUCTIONS.md`
- `README.md`
- `Knowledge/`
- `Knowledge_Bundles/`
- `Knowledge_Bundles/UPLOAD_LIST.md`

Repository-level guidance remains aligned around Goal Mode, GitHub as live source of truth, Knowledge Bundles as the default upload mode, human review before merge, and compact cross-project handoffs.

## Files Inspected

Root files:

- `README.md`
- `PROJECT_REGISTRY.md`
- `SYNC_CONTRACT.md`
- `CONTEXT_PACK_STANDARD.md`
- `COMMAND_SURFACE.md`
- `GOAL_PACKS.md`
- `CHATGPT_CODEX_OPERATING_GUIDE.md`
- `GOAL_MODE_TEMPLATES.md`
- `AGENTS.md`

Project folders:

- `ChatGPT/[AI OS]/`
- `ChatGPT/[LLM]/`
- `ChatGPT/[Analytics]/`
- `ChatGPT/[Thinking]/`
- `ChatGPT/[Codex]/`
- `ChatGPT/[Inbox Router]/`

Focused consistency files:

- `ChatGPT/[AI OS]/Knowledge/ANTI_PATTERNS.md`
- `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`
- all `ChatGPT/*/Knowledge_Bundles/UPLOAD_LIST.md` files

## Inconsistencies Found

- `[AI OS]` handoff wording still implied Codex should work only from an `atomic task package`, while repo-level Goal Mode says broad goals are allowed and Codex infers scope, checks, rollback, and acceptance.
- `GOAL_PACKS.md` still listed candidate pack `local_ai_experiment` after active pack `local_ai_pilot` was added, creating duplicate Local AI routing language.
- There was no root-level shared handoff style reference covering all project folders in one compact place.

## Fixes Applied

- Updated `[AI OS]` handoff and anti-pattern wording to allow Goal Mode handoffs or strict scoped task packages, with scope, checks, rollback, and acceptance.
- Updated the matching `[AI OS]` handoff Knowledge Bundle so upload-ready content matches source Knowledge.
- Removed obsolete candidate pack `local_ai_experiment` from `GOAL_PACKS.md` and the compact Goal Packs bundle; `local_ai_pilot` remains the active Local AI route.
- Added `HANDOFF_STYLE_STANDARD.md` as a compact cross-project handoff reference.
- Added a README pointer to `HANDOFF_STYLE_STANDARD.md`.

## Known Residual Risks

- ChatGPT Project UI upload and smoke QA are not verified by repository checks alone.
- Knowledge Bundles remain cached upload artifacts; fresh state should still be read from GitHub or repo files.
- The report is a snapshot of the inspected repository state, not a runtime sync mechanism.

## Items Intentionally Not Changed

- `PROJECT_INSTRUCTIONS.md` files were not changed.
- Governed KB Gold content was not changed.
- Formulas, schemas, metric definitions, column names, output contracts, and business logic were not changed.
- No logs, journals, runtime artifacts, scripts, embeddings, vector DB, semantic search, web UI, autonomous retrieval, or production agent workflows were added.
- No separate consistency checklist was added; this report plus `HANDOFF_STYLE_STANDARD.md` is sufficient for the current follow-up.

## Acceptance Status

`candidate / ready for human review`

## Next Step

Open a small docs-only PR and keep merge human-reviewed.
