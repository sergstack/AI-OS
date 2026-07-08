# StreamDeck v2.8 MCP Setup Report

Status: candidate-only setup report
Profile targeted: `AI OS StreamDeck v2.8 Candidate`
Promotion status: candidate only
Human acceptance required: yes

## MCP available: yes

Elgato MCP Server is installed and configured for Codex.

Observed setup result:

- Official setup guide used: https://www.elgato.com/us/en/explorer/products/stream-deck/sd-mcp-setup/
- Stream Deck app version observed from user screenshot: 7.4.2.
- Stream Deck setting observed from user screenshot: `Enable MCP Deck` enabled.
- Installed npm package: `@elgato/mcp-server@0.1.1`.
- Installed binary on PATH: `elgato-mcp-server`.
- Codex MCP config added: `[mcp_servers.elgato_streamdeck]` in `~/.codex/config.toml`, not in the repository.
- Codex config validation result: passed; TOML parsed and the `elgato_streamdeck` server entry was present and enabled.
- Direct MCP handshake result: success.
- Stream Deck MCP tools found: `streamdeck__get_executable_actions`, `streamdeck__execute_action`.
- Current executable actions returned by MCP: 0.
- Reason current executable action list is empty: the Stream Deck `MCP Actions` profile has no configured action buttons/descriptions yet.
- Stream Deck profile control performed: none.

Because the Elgato MCP server exposes executable actions rather than profile-authoring operations, this report does not claim that a Stream Deck profile was created, duplicated, configured, or smoke-tested through MCP.

## MCP operations supported

Stream Deck operations supported in this environment:

| Operation | Supported through available MCP | Result |
|---|---:|---|
| Get executable MCP actions | yes | Available; returned an empty action list because no actions are configured on the MCP Actions profile yet |
| Execute an exposed MCP action | yes | Available; not used because no candidate action should be triggered automatically |
| Create profile | no | Not exposed by Elgato MCP server |
| Duplicate profile | no | Not exposed by Elgato MCP server |
| Set button title | no | Not exposed by Elgato MCP server |
| Set button icon | no | Not exposed by Elgato MCP server |
| Set button action | no | Not exposed by Elgato MCP server |
| Set text action body | no | Not exposed by Elgato MCP server |
| Create folders/pages | no | Not exposed by Elgato MCP server |
| Set icons from local PNG files | no | Not exposed by Elgato MCP server |
| Read full visible Stream Deck profile state | no | Not exposed by Elgato MCP server |

Capability boundary:

- MCP can execute existing actions that have already been placed on the Stream Deck `MCP Actions` profile.
- This does not currently prove that MCP can create or edit full Stream Deck profiles, folders, icons, text actions, or the complete v2.8 layout.

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

Profile creation status: not created through MCP because Elgato MCP does not expose profile creation or duplication operations.

Direct v2.8 profile setup via MCP: not completed.

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

MCP/device smoke QA result: partial connection smoke passed; candidate profile smoke not run.

Observed MCP smoke:

- `elgato-mcp-server --help` returned usage information.
- Codex config parsed successfully after adding the Elgato MCP server entry.
- Direct MCP client handshake succeeded.
- `listTools` returned `streamdeck__get_executable_actions` and `streamdeck__execute_action`.
- `streamdeck__get_executable_actions` returned an empty actions list because the Stream Deck `MCP Actions` profile has no configured action buttons/descriptions yet.

Reason candidate profile smoke was not run: Elgato MCP does not expose profile-authoring operations, no candidate profile was created through MCP, and no physical/manual candidate profile setup was performed in this run.

Source-map QA evidence available:

| Smoke item | Source-map status |
|---|---|
| HOME opens expected folders/screens | Map contains HOME folder targets for ROUTE, AI OS, THINKING, ANALYTICS, LLM, CODEX, MEMO, LOCAL AI, PILOTS, KB. |
| HOME JUDGE inserts text only | HOME K7 is `Text`, setting `System -> Text`. |
| HOME REVISOR inserts text only | HOME K8 is `Text`, setting `System -> Text`. |
| HOME AI TREND does not default to live web check | HOME AI TREND says volatile facts should be labeled `needs fresh check` and asks Sergey before live web check. |
| CODEX / Issue -> PR keeps merge policy boundary | CODEX K3 is a text action; safety text prohibits merging/publishing automatically. |
| REVISOR / Prompt QA is judge-only, not rewrite-first | Level 2 risk QA records the rename to `Prompt QA` and judge-only behavior. |
| Icons match icon map for HOME and at least one Level 2 screen | File existence verified for all icon-map PNG paths; visual/device application not performed. |
| v2.7 profile remains available | Not verified through MCP/device state; no Stream Deck profile operation was performed. |

## Deviations from map

- MCP server installation and Codex config were executed, but profile-authoring setup was not available through MCP.
- No candidate profile was created or duplicated through MCP.
- No buttons, folders, text actions, or icons were applied to a Stream Deck profile.
- MCP-visible executable actions were inspected and returned an empty list.
- Direct v2.8 profile setup via MCP was not completed.
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
    - CODEX / Issue -> PR keeps merge policy boundary.
    - REVISOR / Prompt QA is judge-only, not rewrite-first.
    - HOME icons and at least one Level 2 screen match the icon map.
    - v2.7 profile remains available.
13. Record human acceptance or requested fixes before any promotion.

MCP-specific manual step:

- Add only safe, candidate-approved actions to the Stream Deck `MCP Actions` profile if Sergey wants AI tools to execute them through MCP. Do not expose destructive, send, merge, publish, deploy, secret, or production actions.

Recommended next step:

- Create a small `MCP Actions` pilot with 5-7 safe, candidate-only action buttons and clear descriptions, then retest `streamdeck__get_executable_actions`.
- Keep the active v2.7 profile unchanged.
- Keep the full v2.8 layout candidate-only until a separate candidate profile is manually accepted.

## Residual risks

- Current Codex session may need restart or MCP reload before `elgato_streamdeck` appears as a first-class callable tool.
- Elgato MCP exposes executable actions, not profile construction; v2.8 profile setup still requires manual Stream Deck app work or another profile-authoring API.
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
