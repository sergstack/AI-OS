# StreamDeck v2.8 MCP Setup Report

Status: candidate-only setup report
Profile targeted: `AI OS StreamDeck v2.8 Candidate`
Promotion status: candidate only
Human acceptance required: yes

## MCP available: no

No Stream Deck MCP integration is exposed in the current Codex environment.

Observed MCP/tool discovery result:

- Available MCP/app surfaces found: Gmail, Google Calendar, GitHub, Hugging Face, Node REPL.
- Stream Deck MCP operations found: none.
- Stream Deck profile control performed: none.

Because no Stream Deck MCP tool is available, this report does not claim that a Stream Deck profile was created, duplicated, configured, or smoke-tested through MCP.

## MCP operations supported

Stream Deck operations supported in this environment:

| Operation | Supported through available MCP | Result |
|---|---:|---|
| Create profile | no | Not available |
| Duplicate profile | no | Not available |
| Set button title | no | Not available |
| Set button icon | no | Not available |
| Set button action | no | Not available |
| Set text action body | no | Not available |
| Create folders/pages | no | Not available |
| Set icons from local PNG files | no | Not available |
| Read visible Stream Deck profile state | no | Not available |

## Candidate inputs inspected

- `StreamDeck/AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`
- `StreamDeck/AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json`
- `StreamDeck/AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`
- `StreamDeck/STREAMDECK_V2_8_ICON_MAP.csv`
- `StreamDeck/icons/v2.8/**`
- `StreamDeck/STREAMDECK_V2_8_HOME_PREVIEW.png`
- `StreamDeck/STREAMDECK_V2_8_LEVEL2_PREVIEW.png`
- `StreamDeck/STREAMDECK_V2_8_LIVE_PROMPT_QA.md`
- `StreamDeck/STREAMDECK_V2_8_LEVEL2_RISK_QA.md`

Input readiness observed by local file checks:

- Button map rows: 195.
- Screens in map: HOME, ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, JUDGE, REVISOR, MEMO, LOCAL AI, PILOTS, KB.
- Actions in map: 12 Folder, 118 Text, 12 Navigation Back, 53 Empty.
- Icon map rows: 195.
- PNG assets under `StreamDeck/icons/v2.8`: 195.
- Missing icon files referenced by icon map: 0.

## Profile targeted

Target candidate profile name:

```text
AI OS StreamDeck v2.8 Candidate
```

Profile creation status: not created through MCP because Stream Deck MCP is not available.

Safety requirement:

- Do not overwrite or delete the active v2.7 profile.
- Do not promote v2.8 active.
- Build or import only a separate candidate profile.

## Buttons/folders configured

Configured through MCP: none.

Candidate map prepared for manual setup:

- HOME has 15 buttons.
- HOME folders: ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, MEMO, LOCAL AI, PILOTS, KB.
- HOME text actions: JUDGE, REVISOR, INBOX, AI TREND, SYNC.
- Level 2 screens prepared in the map: ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, JUDGE, REVISOR, MEMO, LOCAL AI, PILOTS, KB.
- All text actions must use `System -> Text` with auto-send disabled.
- Navigation back keys must use Stream Deck back/navigation behavior and should not be reprogrammed as destructive actions.
- Empty keys should remain empty or reserved according to the map.

## Icons applied

Applied through MCP: none.

Icon readiness:

- HOME icon files exist for K1 through K15.
- Level 2 icon files exist for all icon-map rows.
- Icon map has no missing local PNG references.

Manual setup must apply icons from `StreamDeck/STREAMDECK_V2_8_ICON_MAP.csv`, using paths under `StreamDeck/icons/v2.8/`.

## Smoke QA result

MCP/device smoke QA result: not run.

Reason: no Stream Deck MCP operations are available, and no physical/manual Stream Deck setup was performed in this run.

Source-map QA evidence available:

| Smoke item | Source-map status |
|---|---|
| HOME opens expected folders/screens | Map contains HOME folder targets for ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, MEMO, LOCAL AI, PILOTS, KB. |
| HOME JUDGE inserts text only | HOME K7 is `Text`, setting `System -> Text`. |
| HOME REVISOR inserts text only | HOME K8 is `Text`, setting `System -> Text`. |
| HOME AI TREND does not default to live web check | HOME AI TREND says volatile facts should be labeled `needs fresh check` and asks Sergey before live web check. |
| CODEX / Issue -> PR keeps no-auto-merge | CODEX K3 is a text action; safety text prohibits merging/publishing automatically. |
| REVISOR / Prompt QA is judge-only, not rewrite-first | Level 2 risk QA records the rename to `Prompt QA` and judge-only behavior. |
| Icons match icon map for HOME and at least one Level 2 screen | File existence verified for all icon-map PNG paths; visual/device application not performed. |
| v2.7 profile remains available | Not verified through MCP/device state; no Stream Deck profile operation was performed. |

## Deviations from map

- No MCP setup was executed.
- No candidate profile was created or duplicated.
- No buttons, folders, text actions, or icons were applied to a Stream Deck profile.
- No device-visible state was inspected.
- No physical HOME or Level 2 navigation smoke test was performed.

## Manual steps still needed

1. Open the Stream Deck desktop app.
2. Confirm the active v2.7 profile remains present and is not selected for overwrite.
3. Create or duplicate a separate profile named `AI OS StreamDeck v2.8 Candidate`.
4. Use `StreamDeck/AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md` as the setup guide.
5. Configure HOME according to `StreamDeck/AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`.
6. Create the Level 2 folders/screens listed in the map.
7. Add text actions with `System -> Text` only.
8. Keep auto-send disabled for every text action.
9. Apply icons from `StreamDeck/STREAMDECK_V2_8_ICON_MAP.csv`.
10. Compare HOME with `StreamDeck/STREAMDECK_V2_8_HOME_PREVIEW.png`.
11. Compare at least one Level 2 screen with `StreamDeck/STREAMDECK_V2_8_LEVEL2_PREVIEW.png`.
12. Run manual smoke QA:
    - HOME opens expected folders/screens.
    - HOME JUDGE inserts text only.
    - HOME REVISOR inserts text only.
    - HOME AI TREND asks before live web check.
    - CODEX / Issue -> PR keeps no-auto-merge.
    - REVISOR / Prompt QA is judge-only, not rewrite-first.
    - HOME icons and at least one Level 2 screen match the icon map.
    - v2.7 profile remains available.
13. Record human acceptance or requested fixes before any promotion.

## Residual risks

- Stream Deck MCP integration may exist outside this Codex environment, but it is not available here.
- Elgato profile import/export behavior remains untested in this run.
- Physical-device behavior, folder navigation, icon rendering, key timing, and text insertion behavior remain unverified.
- Manual setup may introduce transcription errors unless checked against the CSV, JSON, setup markdown, icon map, and previews.
- v2.8 must remain candidate-only until Sergey manually accepts promotion.

## Promotion status

Promotion status: candidate only.

Do not promote v2.8 active until:

- the candidate profile exists separately from v2.7;
- manual or MCP/device smoke QA passes;
- icons and text actions are checked against the map;
- Sergey explicitly accepts promotion.
