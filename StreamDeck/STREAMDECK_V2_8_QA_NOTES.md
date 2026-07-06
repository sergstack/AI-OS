# StreamDeck v2.8 QA Notes

Status: candidate / ready for human review.

## Files produced

- `AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`

## Source alignment checked

- `COMMAND_SURFACE.md`: HOME commands map to Route, Goal -> Codex APP, AI Trend, Finance Memo, Analytics Loop, Eval / Judge, Revisor, Local AI Pilot, PR Judge, Context Pack, and Sync Check.
- `GOAL_PACKS.md`: prompts use the active packs for AI trend triage, Codex goal-to-PR, finance memo, analytics loop, supervised autoloop, local AI pilot, supervised loop design, and cross-project eval review.
- `docs/PROJECT_ROUTING.md`: ROUTE prompts classify and hand off; they do not solve owner-project work.
- `PROJECT_FOLDER_QA_PILOT_REPORT.md` and `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md`: v2.8 keeps project/runtime status as candidate where evidence is runtime or pilot-based, especially for Local AI.

## Acceptance mapping

- Level 1 HOME is simple and command-oriented: 15 daily buttons, no folder-heavy REPO/SYSTEM/STOP cluster.
- Level 2 screens cover ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, JUDGE, REVISOR, MEMO, LOCAL AI, PILOTS, and KB.
- JUDGE and REVISOR are one-touch HOME text prompts; deeper JUDGE/REVISOR screens are also present from LLM.
- SYNC is a HOME text prompt and is also available inside CODEX.
- LOCAL AI is one-touch from HOME as a focused candidate-only screen.
- QA is replaced by JUDGE.
- REPO is replaced by SYNC.
- SYSTEM is demoted because no clear daily command-surface use is supported by current evidence.
- STOP is removed from HOME because no safe text-only stop action is needed; built-in Stream Deck back/Esc remains manual outside the map.
- RESEARCH is reframed as AI TREND for trend triage and hype filtering.
- v2.7 files are preserved; v2.8 is a candidate side-by-side migration.
- Safety/manual-only rules are explicit in setup markdown and prompt text.

## Residual risks

- Actual Stream Deck device/profile behavior is not tested by repository checks.
- Live ChatGPT Project sync can drift after manual Knowledge uploads; runtime smoke QA should be repeated after migration.
- The v2.8 JSON/CSV are setup maps, not an Elgato import package.
