# AI OS Stream Deck Documentation

## Active version

Current active version: v2.7

Candidate version: v2.9 review-confirmed operator panel (supersedes the v2.8 candidate).

Status checked: 2026-07-09.

## Files

- `ROUTING_FIXED_AIOS_StreamDeck_Setup_Instruction_v2.7_PROJECT_ALIGNED_EN_LABELS.md`
- `ROUTING_FIXED_AIOS_StreamDeck_Button_Map_v2.7_PROJECT_ALIGNED_EN_LABELS.json`
- `ROUTING_FIXED_AIOS_StreamDeck_Button_Map_v2.7_PROJECT_ALIGNED_EN_LABELS.csv`
- `STREAMDECK_LEARNING_CYCLE_PROMPTS_CANDIDATE.md`
- `AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`
- `STREAMDECK_V2_8_QA_NOTES.md`
- `STREAMDECK_V2_8_LIVE_PROMPT_QA.md`
- `STREAMDECK_V2_8_LEVEL2_RISK_QA.md`

## v2.7 scope

- Project-aligned English labels.
- Routing-fixed 15-screen layout.
- Old Stream Deck version files were removed after v2.7 promotion.

## Learning Cycle candidate

- `STREAMDECK_LEARNING_CYCLE_PROMPTS_CANDIDATE.md` contains the candidate prompt set for the Learning Cycle screen: `Daily / Master / Hardcore / Judge / Revisor / QA / Save Mini / Save Full`.
- Status: candidate / ready for Stream Deck pilot.
- Promotion status: not permanent standard.
- Evidence status: practical recommendation / needs 3–5 real runs.
- The active v2.7 setup, JSON, and CSV files are not replaced by this candidate document.

## v2.8 candidate

- `AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md` defines the candidate two-level operator panel.
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json` and `.csv` contain the matching setup map.
- `STREAMDECK_V2_8_QA_NOTES.md` records source alignment, acceptance mapping, and residual risks.
- `STREAMDECK_V2_8_LIVE_PROMPT_QA.md` and `STREAMDECK_V2_8_LEVEL2_RISK_QA.md` record live prompt and risk QA context.
- Status: candidate / ready for human review.
- Active status: v2.7 remains active until Sergey manually migrates and accepts v2.8.
- Promotion status: not promoted by repo files; manual migration and acceptance remain required.
- MCP Actions status: registry/run-package artifacts exist, but manual Stream Deck
  `MCP Actions` profile setup and live MCP execution evidence remain required.
- Migration path: duplicate or create a separate Stream Deck profile, build v2.8 side by side, then manually promote after pilot review.

## v2.9 candidate (review-confirmed)

- `AIOS_StreamDeck_Setup_Instruction_v2.9.md` — full setup instruction with per-button project, risk, MCP action, and next-button hints.
- `AIOS_StreamDeck_Button_Map_v2.9.json` — enriched button map (195 cells, 13 screens).
- `AIOS_StreamDeck_Button_Map_v2.9.xlsx` — spreadsheet button map (README, Button Map, MCP Registry, HOME Grid sheets).
- Scope: consolidates the StreamDeck MCP command-surface issue tree (#184–#191) after its review pass. HOME layout is identical to v2.8; the prompt-first HOME proposal was rejected because it made the CODEX and LLM Level-2 screens unreachable.
- Corrected metadata: 16 canonical commands, 12 active + 4 candidate goal packs, 195 button cells, 7 MCP registry actions (2 execution-verified: `AIOS_HOME_JUDGE`, `AIOS_HOME_REVISOR`).
- Prompt texts are reused verbatim from v2.8; no Prompt QA run has been executed, so prompts remain candidate.
- Status: candidate / ready for owner review. v2.7 remains active; v2.8 artifacts are preserved.

### v2.8 HOME

```text
ROUTE      AI OS      THINKING   ANALYTICS  LLM
CODEX      JUDGE      REVISOR    INBOX      MEMO
AI TREND   SYNC       LOCAL AI   PILOTS     KB
```

### v2.8 migration notes

- `QA` is replaced by `JUDGE` with pass / revise / blocked verdict prompts.
- `REVISOR` is added to HOME.
- `REPO` is replaced by `SYNC`; deeper repo work remains under `CODEX`.
- `RESEARCH` is reframed as `AI TREND`.
- `SYSTEM` is demoted from HOME because it has no clear daily command-surface role in current evidence.
- `STOP` is removed from HOME because no safe text-only stop action is needed; use manual Stream Deck back/Esc behavior outside this map.
- v2.7 files are preserved.

## Safety

- Text buttons only insert text.
- Auto-send must remain disabled.
- No destructive actions.
- Terminal commands must be inserted as text and run manually.
- v2.8 remains manual-only: no deletion, sending, merging, publishing, production automation, secrets, runtime artifacts, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents.
