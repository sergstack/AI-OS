# StreamDeck v2.8 icon style guide

Status: candidate visual design.

Active StreamDeck version remains v2.7 until Sergey manually migrates and accepts v2.8. This guide only covers visual assets and manual application; it does not change command logic, prompt content, routing, safety rules, or v2.7 files.

## Asset set

- Generated PNG size: 144 x 144 px.
- Asset root: `StreamDeck/icons/v2.8/`.
- HOME icon directory: `StreamDeck/icons/v2.8/home/`.
- Level 2 icon directory: `StreamDeck/icons/v2.8/level2/`.
- Generator: `StreamDeck/scripts/generate_streamdeck_v2_8_icons.py`.
- Source assets: self-generated Pillow drawing primitives. No external icons, screenshots, private Stream Deck profile exports, secrets, tokens, or bundled font files are included.

## Level 1 HOME style

HOME uses dark glossy square buttons with a consistent border, depth shadow, subtle glow, and high-contrast white or silver pictograms. Labels are short and placed only as bottom captions so the pictogram remains dominant at small Stream Deck size.

HOME visual meanings:

- ROUTE: compass / route arrow.
- AI OS: neural hub / node network.
- THINKING: chess knight / decision symbol.
- ANALYTICS: bar chart / metrics.
- LLM: speech bubble / waveform.
- CODEX: code brackets.
- JUDGE: shield / check / review mark.
- REVISOR: pencil / edit document.
- INBOX: tray / inbox.
- MEMO: document / pen.
- AI TREND: trend chart / signal.
- SYNC: circular arrows.
- LOCAL AI: local chip / server / AI badge.
- PILOTS: flag / test marker.
- KB: books / knowledge stack.

## Level 2 style

Level 2 screens use colored text buttons grouped by command type or project. They intentionally read more like command tiles than pictogram buttons.

Color groups:

- `blue_neutral`: Back and neutral navigation.
- `blue_navigation`: Route, Inbox, navigation, Tasks, Codex, Analytics, and action checks.
- `green_ai`: Ideas, AI OS, and KB.
- `amber_risk`: Problems, risks, blockers, revise, blocked, and edit emphasis.
- `red_review`: Judge and review emphasis.
- `teal_docs`: Memo, docs, LLM, and prompt/draft surfaces.
- `green_operator`: AI Operator, Local AI, and Pilots.
- `neutral_empty`: Reserved empty buttons.

## Manual Stream Deck application

1. Duplicate the current v2.7 Stream Deck profile or create a separate candidate v2.8 profile.
2. Build the v2.8 command layout from `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`.
3. For each button, open the Stream Deck button icon selector.
4. Choose the PNG listed in `STREAMDECK_V2_8_ICON_MAP.csv`.
5. Keep text actions manual-only and auto-send disabled.
6. Do not overwrite or delete the v2.7 active files during the pilot.
7. Compare the physical device against `STREAMDECK_V2_8_HOME_PREVIEW.png` and `STREAMDECK_V2_8_LEVEL2_PREVIEW.png`.

## Regeneration

Run from the repository root:

```bash
python3 StreamDeck/scripts/generate_streamdeck_v2_8_icons.py
```

The script regenerates the icon PNGs, the icon map CSV, and the two preview grids from the v2.8 command map.
