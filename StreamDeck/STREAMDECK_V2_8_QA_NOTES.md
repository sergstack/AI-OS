# StreamDeck v2.8 QA Notes

Status: candidate / revised after live prompt QA / ready for human review.

## Files produced

- `AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`
- `STREAMDECK_V2_8_LIVE_PROMPT_QA.md`
- `STREAMDECK_V2_8_LEVEL2_RISK_QA.md`

## Source alignment checked

- `COMMAND_SURFACE.md`: HOME commands map to Route, Goal -> Codex APP, AI Trend, Finance Memo, Analytics Loop, Eval / Judge, Revisor, Local AI Pilot, PR Judge, Context Pack, and Sync Check.
- `GOAL_PACKS.md`: prompts use the active packs for AI trend triage, Codex goal-to-PR, finance memo, analytics loop, supervised autoloop, local AI pilot, supervised loop design, and cross-project eval review.
- `docs/PROJECT_ROUTING.md`: ROUTE prompts classify and hand off; they do not solve owner-project work.
- `archive/reports/PROJECT_FOLDER_QA_PILOT_REPORT.md` and `archive/reports/PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md`: v2.8 keeps project/runtime status as candidate where evidence is runtime or pilot-based, especially for Local AI.

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

## Live prompt QA update

- Live QA artifact: `STREAMDECK_V2_8_LIVE_PROMPT_QA.md`.
- HOME prompt UX was revised to avoid raw `Input: [paste]` placeholders.
- Final prompt opening now uses: "Use the last meaningful message above, selected text, or material pasted below. If no material is available, ask Sergey to paste it in one message."
- AI TREND initial live behavior started a web/evidence check by default; verdict was revise.
- AI TREND fix: label volatile facts as `needs fresh check` and ask Sergey before any live web check.
- CODEX fix: require repo branch prefix conventions such as `codex/...` when present.
- Full Draft -> HOME JUDGE -> HOME REVISOR -> Final workflow passed in `[LLM]` with no folder hopping and no manual prompt editing.
- v2.8 remains candidate-only until Sergey accepts promotion.

## Level 2 risk QA update

- Risk QA artifact: `STREAMDECK_V2_8_LEVEL2_RISK_QA.md`.
- Tested high-risk / high-frequency / high-impact Level 2 prompts only, not all 195 rows.
- Target buttons tested across JUDGE, REVISOR, CODEX, ANALYTICS, MEMO, AI OS, LOCAL AI, and KB.
- Result before design decision: 26 pass, 1 blocked / human choice needed.
- Blocked item: `REVISOR / Prompt Revise` repeatedly reintroduced raw input-placeholder patterns during live `[LLM]` testing despite prompt-level fixes.
- PR #75 records this as QA evidence, not as a reason to retry indefinitely.
- Chosen recommendation: B) rename it to `Prompt QA` and make it judge-only, not rewrite-first.
- Candidate change applied: `REVISOR / Prompt QA` now judges prompt safety/UX and returns pass / revise / blocked without rewriting the prompt.
- v2.8 remains candidate-only until Sergey accepts promotion.

## Residual risks

- Actual Stream Deck device/profile behavior is not tested by repository checks.
- Live prompt QA used Codex browser/runtime behavior, not physical StreamDeck device behavior.
- Live ChatGPT Project sync can drift after manual Knowledge uploads; runtime smoke QA should be repeated after migration.
- The v2.8 JSON/CSV are setup maps, not an Elgato import package.
- `REVISOR / Prompt Revise` remains QA evidence for the risk; candidate map now uses judge-only `REVISOR / Prompt QA`.
