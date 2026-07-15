#!/usr/bin/env python3
"""Generate StreamDeck v2.8 icon assets, icon map, and previews.

The assets are self-generated with Pillow drawing primitives. No external
icons, screenshots, private profile exports, or font files are bundled.
"""

from __future__ import annotations

import csv
import math
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
STREAMDECK = ROOT / "StreamDeck"
SOURCE_MAP = STREAMDECK / "AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv"
ICON_ROOT = STREAMDECK / "icons" / "v2.8"
HOME_DIR = ICON_ROOT / "home"
LEVEL2_DIR = ICON_ROOT / "level2"
SIZE = 144

STYLE_GUIDE = STREAMDECK / "STREAMDECK_V2_8_ICON_STYLE_GUIDE.md"
ICON_MAP = STREAMDECK / "STREAMDECK_V2_8_ICON_MAP.csv"
HOME_PREVIEW = STREAMDECK / "STREAMDECK_V2_8_HOME_PREVIEW.png"
LEVEL2_PREVIEW = STREAMDECK / "STREAMDECK_V2_8_LEVEL2_PREVIEW.png"


@dataclass(frozen=True)
class ColorStyle:
    name: str
    top: tuple[int, int, int]
    bottom: tuple[int, int, int]
    accent: tuple[int, int, int]
    text: tuple[int, int, int] = (245, 249, 252)


LEVEL1 = ColorStyle("level1_dark_operator", (20, 24, 31), (3, 5, 10), (170, 213, 255))
LEVEL2_STYLES = {
    "blue_neutral": ColorStyle("blue_neutral", (30, 78, 125), (7, 25, 49), (104, 190, 255)),
    "blue_navigation": ColorStyle("blue_navigation", (20, 83, 138), (5, 35, 67), (114, 205, 255)),
    "green_ai": ColorStyle("green_ai", (17, 112, 91), (5, 55, 45), (83, 235, 187)),
    "teal_docs": ColorStyle("teal_docs", (23, 101, 112), (7, 50, 58), (116, 229, 230)),
    "amber_risk": ColorStyle("amber_risk", (143, 98, 16), (72, 42, 5), (255, 199, 74)),
    "red_review": ColorStyle("red_review", (138, 38, 43), (64, 14, 20), (255, 116, 120)),
    "green_operator": ColorStyle("green_operator", (33, 118, 63), (9, 54, 33), (115, 236, 141)),
    "neutral_empty": ColorStyle("neutral_empty", (44, 49, 57), (17, 20, 25), (116, 127, 140)),
}

HOME_ICONS = {
    "ROUTE": "compass",
    "AI OS": "network",
    "THINKING": "knight",
    "ANALYTICS": "bars",
    "LLM": "bubble",
    "CODEX": "brackets",
    "JUDGE": "shield",
    "REVISOR": "pencil_doc",
    "INBOX": "inbox",
    "MEMO": "memo",
    "AI TREND": "trend",
    "SYNC": "sync",
    "LOCAL AI": "chip",
    "PILOTS": "flag",
    "KB": "books",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def gradient(size: int, top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    img = Image.new("RGB", (size, size), top)
    pix = img.load()
    for y in range(size):
        t = y / (size - 1)
        for x in range(size):
            shade = 1.0 - 0.12 * math.hypot((x - size / 2) / size, (y - size / 2) / size)
            color = tuple(int((top[i] * (1 - t) + bottom[i] * t) * shade) for i in range(3))
            pix[x, y] = color
    return img


def rounded_button(style: ColorStyle, glossy: bool = True) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    base = gradient(SIZE, style.top, style.bottom).convert("RGBA")
    mask = Image.new("L", (SIZE, SIZE), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((7, 7, SIZE - 8, SIZE - 8), radius=20, fill=255)
    shadow = mask.filter(ImageFilter.GaussianBlur(5))
    img.alpha_composite(Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 150)), (0, 3))
    img.putalpha(shadow)
    out = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    out.alpha_composite(img)
    out.alpha_composite(Image.composite(base, Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0)), mask))
    d = ImageDraw.Draw(out)
    d.rounded_rectangle((7, 7, SIZE - 8, SIZE - 8), radius=20, outline=(255, 255, 255, 56), width=2)
    d.rounded_rectangle((10, 10, SIZE - 11, SIZE - 11), radius=17, outline=(0, 0, 0, 130), width=2)
    if glossy:
        gloss = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        gd = ImageDraw.Draw(gloss)
        gd.rounded_rectangle((14, 12, SIZE - 15, 61), radius=15, fill=(255, 255, 255, 34))
        out.alpha_composite(gloss)
    glow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((32, 21, 112, 102), fill=(*style.accent, 26))
    out.alpha_composite(glow.filter(ImageFilter.GaussianBlur(12)))
    return out, ImageDraw.Draw(out)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    spacing: int = 4,
) -> None:
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total = sum(heights) + spacing * (len(lines) - 1)
    y = xy[1] + (xy[3] - xy[1] - total) // 2
    for line, height in zip(lines, heights):
        width, _ = text_size(draw, line, fnt)
        x = xy[0] + (xy[2] - xy[0] - width) // 2
        draw.text((x, y), line, font=fnt, fill=fill)
        y += height + spacing


def fit_lines(draw: ImageDraw.ImageDraw, label: str, max_width: int, max_lines: int = 3) -> tuple[list[str], ImageFont.ImageFont]:
    clean = label.replace(" -> ", " ").replace("/", " / ")
    words = clean.split()
    for size in range(24, 11, -1):
        fnt = font(size, bold=True)
        wrapped: list[str] = []
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if text_size(draw, candidate, fnt)[0] <= max_width:
                current = candidate
            else:
                if current:
                    wrapped.append(current)
                current = word
        if current:
            wrapped.append(current)
        if len(wrapped) <= max_lines and all(text_size(draw, line, fnt)[0] <= max_width for line in wrapped):
            return wrapped, fnt
    return textwrap.wrap(clean, width=8)[:max_lines], font(11, bold=True)


def label_bottom(draw: ImageDraw.ImageDraw, label: str) -> None:
    label_font = font(14, bold=True)
    words = label.split()
    lines = [label] if len(label) <= 9 else [" ".join(words[:1]), " ".join(words[1:])]
    lines = [line for line in lines if line]
    center_text(draw, (12, 112, 132, 137), lines, label_font, (238, 243, 248), spacing=0)


def draw_icon(draw: ImageDraw.ImageDraw, name: str, accent: tuple[int, int, int]) -> None:
    white = (238, 245, 252)
    silver = (180, 193, 205)
    a = (*accent, 235)
    w = (*white, 245)
    s = (*silver, 230)
    if name == "compass":
        draw.ellipse((43, 26, 101, 84), outline=s, width=4)
        draw.polygon([(75, 34), (84, 72), (69, 63), (59, 72)], fill=w)
        draw.line((72, 29, 72, 84), fill=a, width=2)
    elif name == "network":
        pts = [(50, 38), (91, 38), (70, 69), (48, 80), (96, 80)]
        for p1, p2 in [(0, 2), (1, 2), (2, 3), (2, 4)]:
            draw.line((*pts[p1], *pts[p2]), fill=s, width=3)
        for x, y in pts:
            draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=w, outline=a, width=2)
    elif name == "knight":
        draw.polygon([(55, 85), (88, 85), (83, 70), (70, 62), (82, 47), (71, 35), (52, 47), (57, 62)], fill=w)
        draw.rectangle((50, 87, 92, 94), fill=s)
        draw.ellipse((70, 48, 75, 53), fill=(10, 14, 20))
    elif name == "bars":
        for x, h in [(45, 26), (64, 43), (83, 56)]:
            draw.rounded_rectangle((x, 88 - h, x + 12, 88), radius=3, fill=w)
        draw.line((38, 90, 104, 90), fill=s, width=3)
    elif name == "bubble":
        draw.rounded_rectangle((38, 34, 106, 80), radius=14, outline=w, width=4)
        draw.polygon([(61, 78), (52, 95), (78, 80)], fill=w)
        for x, h in [(54, 13), (67, 24), (80, 17), (93, 29)]:
            draw.line((x, 66 - h, x, 66), fill=a, width=4)
    elif name == "brackets":
        draw.line((58, 37, 43, 61, 58, 85), fill=w, width=6, joint="curve")
        draw.line((86, 37, 101, 61, 86, 85), fill=w, width=6, joint="curve")
        draw.line((67, 88, 78, 35), fill=a, width=4)
    elif name == "shield":
        draw.polygon([(72, 28), (101, 40), (96, 73), (72, 93), (48, 73), (43, 40)], outline=w, fill=None)
        draw.line((57, 61, 68, 74, 90, 50), fill=a, width=6)
    elif name == "pencil_doc":
        draw.rounded_rectangle((48, 30, 91, 88), radius=5, outline=s, width=3)
        draw.line((58, 49, 81, 49), fill=s, width=2)
        draw.line((58, 61, 78, 61), fill=s, width=2)
        draw.line((57, 88, 99, 46), fill=w, width=7)
        draw.line((92, 39, 102, 49), fill=a, width=7)
    elif name == "inbox":
        draw.line((42, 62, 54, 38, 90, 38, 102, 62), fill=s, width=4)
        draw.rounded_rectangle((39, 61, 105, 89), radius=6, outline=w, width=4)
        draw.line((58, 69, 65, 79, 80, 79, 87, 69), fill=a, width=4)
    elif name == "memo":
        draw.rounded_rectangle((49, 29, 94, 91), radius=5, fill=None, outline=w, width=3)
        draw.line((59, 48, 84, 48), fill=s, width=3)
        draw.line((59, 60, 82, 60), fill=s, width=3)
        draw.line((59, 73, 76, 73), fill=s, width=3)
        draw.line((85, 88, 101, 72), fill=a, width=5)
    elif name == "trend":
        draw.line((41, 86, 41, 39), fill=s, width=3)
        draw.line((39, 86, 104, 86), fill=s, width=3)
        draw.line((47, 78, 62, 63, 76, 69, 96, 43), fill=w, width=5)
        draw.polygon([(96, 43), (94, 58), (107, 38)], fill=a)
    elif name == "sync":
        draw.arc((39, 34, 98, 93), 25, 205, fill=w, width=5)
        draw.arc((46, 29, 105, 88), 205, 25, fill=a, width=5)
        draw.polygon([(43, 49), (49, 33), (59, 47)], fill=w)
        draw.polygon([(101, 73), (95, 91), (84, 77)], fill=a)
    elif name == "chip":
        draw.rounded_rectangle((49, 39, 95, 85), radius=8, outline=w, width=4)
        for x in [42, 102]:
            for y in [49, 61, 73]:
                draw.line((x, y, 49 if x < 50 else 95, y), fill=s, width=3)
        draw.text((59, 54), "AI", font=font(20, bold=True), fill=a)
    elif name == "flag":
        draw.line((51, 35, 51, 94), fill=s, width=5)
        draw.polygon([(55, 35), (98, 43), (76, 59), (98, 75), (55, 67)], fill=w)
        draw.line((55, 67, 55, 35), fill=a, width=3)
    elif name == "books":
        draw.rounded_rectangle((42, 37, 58, 89), radius=3, fill=w)
        draw.rounded_rectangle((62, 32, 79, 89), radius=3, fill=s)
        draw.rounded_rectangle((83, 42, 101, 89), radius=3, fill=w)
        draw.line((46, 49, 55, 49), fill=a, width=2)
        draw.line((86, 56, 98, 56), fill=a, width=2)


def home_icon(label: str, target: Path) -> None:
    img, draw = rounded_button(LEVEL1, glossy=True)
    draw_icon(draw, HOME_ICONS[label], LEVEL1.accent)
    label_bottom(draw, label)
    img.save(target)


def color_group(screen: str, label: str, note: str) -> str:
    text = f"{screen} {label} {note}".lower()
    if label == "BACK":
        return "blue_neutral"
    if label == "EMPTY":
        return "neutral_empty"
    if screen in {"ROUTE"} or "route" in text or "inbox" in text or "navigation" in text:
        return "blue_navigation"
    if screen in {"AI OS", "KB"} or "ideas" in text or "knowledge" in text:
        return "green_ai"
    if screen in {"LOCAL AI", "PILOTS"} or "operator" in text or "pilot" in text:
        return "green_operator"
    if screen in {"MEMO", "LLM"} or "memo" in text or "doc" in text or "prompt" in text:
        return "teal_docs"
    if screen == "JUDGE" or "judge" in text or "review" in text or "evidence" in text:
        return "red_review"
    if screen == "REVISOR" or "revise" in text or "blocked" in text or "bug" in text:
        return "amber_risk"
    if "risk" in text or "blocker" in text or "problem" in text:
        return "amber_risk"
    if screen in {"CODEX", "ANALYTICS"} or "task" in text or "check" in text:
        return "blue_navigation"
    return "teal_docs"


def level2_icon(screen: str, label: str, group: str, target: Path) -> None:
    style = LEVEL2_STYLES[group]
    img, draw = rounded_button(style, glossy=False)
    draw.rounded_rectangle((18, 18, 126, 126), radius=16, outline=(*style.accent, 120), width=2)
    if label == "BACK":
        draw.line((87, 43, 54, 72, 87, 101), fill=style.text, width=9, joint="curve")
    elif label == "EMPTY":
        draw.line((48, 72, 96, 72), fill=(150, 160, 170), width=4)
    else:
        lines, fnt = fit_lines(draw, label.upper(), 104, max_lines=3)
        center_text(draw, (18, 34, 126, 104), lines, fnt, style.text, spacing=5)
        small = font(11, bold=True)
        screen_short = screen.upper()[:10]
        w, _ = text_size(draw, screen_short, small)
        draw.text(((SIZE - w) // 2, 112), screen_short, font=small, fill=(*style.accent, 210))
    img.save(target)


def slug(value: str) -> str:
    clean = "".join(ch.lower() if ch.isalnum() else "_" for ch in value)
    return "_".join(part for part in clean.split("_") if part)


def read_rows() -> list[dict[str, str]]:
    with SOURCE_MAP.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def make_preview(rows: list[dict[str, str]], screen: str, target: Path) -> None:
    cols, rows_count = 5, 3
    gap = 18
    margin = 24
    width = margin * 2 + cols * SIZE + (cols - 1) * gap
    height = margin * 2 + rows_count * SIZE + (rows_count - 1) * gap
    preview = Image.new("RGBA", (width, height), (10, 12, 16, 255))
    for row in rows:
        if row["screen"] != screen:
            continue
        idx = int(row["button"][1:]) - 1
        x = margin + (idx % cols) * (SIZE + gap)
        y = margin + (idx // cols) * (SIZE + gap)
        if screen == "HOME":
            path = HOME_DIR / f"{row['button']}_{slug(row['label'])}.png"
        else:
            path = LEVEL2_DIR / slug(screen) / f"{row['button']}_{slug(row['label'])}.png"
        preview.alpha_composite(Image.open(path).convert("RGBA"), (x, y))
    target.parent.mkdir(parents=True, exist_ok=True)
    preview.save(target)


def write_icon_map(rows: list[dict[str, str]]) -> None:
    fields = ["screen", "button", "label", "icon_file", "style_group", "color_group", "notes"]
    with ICON_MAP.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            screen = row["screen"]
            label = row["label"]
            if screen == "HOME":
                icon_file = f"icons/v2.8/home/{row['button']}_{slug(label)}.png"
                style_group = "level1_gloss_pictogram"
                group = "level1_dark_operator"
                notes = f"{HOME_ICONS.get(label, 'pictogram')} pictogram. {row.get('note', '')}".strip()
            else:
                group = color_group(screen, label, row.get("note", ""))
                icon_file = f"icons/v2.8/level2/{slug(screen)}/{row['button']}_{slug(label)}.png"
                style_group = "level2_colored_text"
                notes = row.get("note", "")
            writer.writerow(
                {
                    "screen": screen,
                    "button": row["button"],
                    "label": label,
                    "icon_file": icon_file,
                    "style_group": style_group,
                    "color_group": group,
                    "notes": notes,
                }
            )


def write_style_guide() -> None:
    STYLE_GUIDE.write_text(
        """# StreamDeck v2.8 icon style guide

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
""",
        encoding="utf-8",
    )


def main() -> None:
    rows = read_rows()
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    LEVEL2_DIR.mkdir(parents=True, exist_ok=True)
    for row in rows:
        screen = row["screen"]
        label = row["label"]
        if screen == "HOME":
            home_icon(label, HOME_DIR / f"{row['button']}_{slug(label)}.png")
            continue
        group = color_group(screen, label, row.get("note", ""))
        out_dir = LEVEL2_DIR / slug(screen)
        out_dir.mkdir(parents=True, exist_ok=True)
        level2_icon(screen, label, group, out_dir / f"{row['button']}_{slug(label)}.png")
    write_icon_map(rows)
    write_style_guide()
    make_preview(rows, "HOME", HOME_PREVIEW)
    make_preview(rows, "ROUTE", LEVEL2_PREVIEW)
    print(f"Generated {len(rows)} icons")
    print(f"Wrote {ICON_MAP.relative_to(ROOT)}")
    print(f"Wrote {STYLE_GUIDE.relative_to(ROOT)}")
    print(f"Wrote {HOME_PREVIEW.relative_to(ROOT)}")
    print(f"Wrote {LEVEL2_PREVIEW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
