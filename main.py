#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue -- entry.

Draws one 1024x1024 meme with PIL from scratch (no network, no input
images): a cheerful robot agent at its desk, thumbs up, party hat on,
calendar on fire behind it -- it was asked to decline ONE meeting.

Top:    "I ASKED MY AGENT TO / DECLINE ONE MEETING"
Bottom: "IT DECLINED / MY WHOLE CAREER"

Writes to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Fonts are bundled in fonts/ so the render is identical anywhere. If
Pillow is unavailable, copies the pre-rendered entry.png shipped in the
repo, so the bytes written are the same either way. Deterministic.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")

W, H = 1024, 1024
PAPER = (255, 246, 229)   # warm paper
INK = (24, 24, 24)       # near-black
RED = (163, 22, 33)      # punchline red
TEAL = (31, 158, 142)
TEAL_DARK = (14, 90, 82)
TEAL_LIGHT = (43, 179, 163)
DESK = (176, 125, 79)

TOP_LINES = ["I ASKED MY AGENT TO", "DECLINE ONE MEETING"]
BOTTOM_LINES = ["IT DECLINED", "MY WHOLE CAREER"]


def load_font(name, size):
    for path in (
        os.path.join(HERE, "fonts", name),
        os.path.join("/usr/share/fonts/truetype/dejavu", name),
    ):
        try:
            from PIL import ImageFont
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    from PIL import ImageFont
    return ImageFont.load_default()


def text_center(draw, y, text, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text(((W - w) // 2 - box[0], y), text, font=font, fill=fill)


def text_center_in(draw, x0, x1, y, text, font, fill):
    """Center text horizontally inside the box [x0, x1]."""
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text(((x0 + x1 - w) // 2 - box[0], y), text, font=font, fill=fill)


def draw_meme():
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- top caption -------------------------------------------------
    font_top = load_font("DejaVuSans-Bold.ttf", 64)
    text_center(d, 42, TOP_LINES[0], font_top, INK)
    text_center(d, 118, TOP_LINES[1], font_top, INK)

    # ---- backdrop halo behind the robot ------------------------------
    d.ellipse([272, 205, 752, 745], fill=(214, 240, 234))
    d.ellipse([272, 205, 752, 745], outline=(150, 200, 190), width=4)

    # ---- wall calendar, on fire --------------------------------------
    d.rectangle([738, 262, 942, 392], fill=(255, 255, 255),
                outline=INK, width=5)
    d.rectangle([738, 262, 942, 302], fill=(200, 40, 40))
    font_cal = load_font("DejaVuSans-Bold.ttf", 24)
    text_center_in(d, 738, 942, 268, "NOVEMBER", font_cal, (255, 255, 255))
    for gx in (790, 842, 894):
        d.line([gx, 302, gx, 392], fill=(200, 200, 200), width=3)
    d.line([738, 347, 942, 347], fill=(200, 200, 200), width=3)
    # flames licking the top edge of the calendar
    for x0, x1, tip in ((758, 790, 216), (812, 844, 202), (866, 898, 218)):
        d.polygon([(x0, 264), ((x0 + x1) // 2, tip), (x1, 264)],
                  fill=(249, 115, 22))
        d.polygon([(x0 + 8, 264), ((x0 + x1) // 2, tip + 22), (x1 - 8, 264)],
                  fill=(250, 204, 21))

    # ---- robot --------------------------------------------------------
    # antenna
    d.line([512, 330, 512, 282], fill=INK, width=8)
    d.ellipse([495, 254, 529, 288], fill=(226, 59, 59), outline=INK, width=4)
    # ears
    d.ellipse([348, 398, 378, 430], fill=TEAL, outline=INK, width=4)
    d.ellipse([646, 398, 676, 430], fill=TEAL, outline=INK, width=4)
    # head
    d.rounded_rectangle([370, 330, 654, 502], radius=62, fill=TEAL,
                        outline=INK, width=6)
    # face screen
    d.rounded_rectangle([392, 352, 632, 480], radius=42, fill=(11, 59, 54))
    # eyes: left open, right winking
    d.ellipse([428, 386, 490, 442], fill=(255, 255, 255))
    d.ellipse([452, 400, 478, 428], fill=INK)
    d.arc([534, 388, 594, 440], 0, 180, fill=(255, 255, 255), width=7)
    # smile
    d.arc([468, 424, 556, 476], 0, 180, fill=(255, 255, 255), width=7)
    # party hat
    d.polygon([(452, 336), (512, 224), (566, 330)], fill=(255, 197, 61),
              outline=INK)
    for cx, cy in ((498, 288), (522, 268), (512, 306)):
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(226, 59, 59))
    d.ellipse([500, 208, 524, 232], fill=(226, 59, 59), outline=INK, width=3)
    # body
    d.rounded_rectangle([392, 512, 632, 664], radius=38, fill=TEAL_LIGHT,
                        outline=INK, width=6)
    # chest panel with buttons
    d.rounded_rectangle([452, 546, 572, 622], radius=14, fill=(232, 255, 249),
                        outline=INK, width=4)
    for i, col in enumerate(((226, 59, 59), (250, 204, 21), (34, 197, 94))):
        cx = 480 + i * 32
        d.ellipse([cx - 10, 568, cx + 10, 588], fill=col, outline=INK, width=3)
    # left arm: thumbs up
    d.line([392, 580, 322, 506], fill=INK, width=30)
    d.line([392, 580, 322, 506], fill=TEAL, width=20)
    d.ellipse([296, 472, 340, 516], fill=TEAL, outline=INK, width=4)
    d.rounded_rectangle([306, 448, 330, 486], radius=10, fill=TEAL,
                        outline=INK, width=4)
    # right arm: holding a mug
    d.line([632, 580, 728, 646], fill=INK, width=30)
    d.line([632, 580, 728, 646], fill=TEAL, width=20)
    d.rounded_rectangle([722, 612, 800, 684], radius=10, fill=(255, 255, 255),
                        outline=INK, width=5)
    d.arc([794, 628, 830, 668], -90, 90, fill=INK, width=6)
    font_mug = load_font("DejaVuSans-Bold.ttf", 22)
    text_center_in(d, 722, 800, 640, "BOSS", font_mug, RED)

    # ---- desk + laptop -----------------------------------------------
    d.rectangle([150, 700, 874, 738], fill=DESK, outline=INK, width=5)
    d.rectangle([190, 738, 214, 786], fill=DESK, outline=INK, width=4)
    d.rectangle([810, 738, 834, 786], fill=DESK, outline=INK, width=4)
    # laptop screen
    d.rectangle([448, 616, 578, 700], fill=(18, 59, 69), outline=INK, width=5)
    font_scr = load_font("DejaVuSans-Bold.ttf", 18)
    text_center_in(d, 448, 578, 628, "1 meeting", font_scr, (255, 255, 255))
    text_center_in(d, 448, 578, 652, "declined \u2713", font_scr,
                   (74, 222, 128))
    # laptop base
    d.polygon([(436, 700), (590, 700), (610, 724), (416, 724)],
              fill=(51, 51, 51), outline=INK)
    # "YOU'RE FIRED" email popup on the laptop
    d.rectangle([590, 636, 716, 688], fill=(255, 255, 255), outline=RED,
                width=4)
    font_mail = load_font("DejaVuSans-Bold.ttf", 16)
    text_center_in(d, 590, 716, 652, "YOU'RE FIRED", font_mail, RED)

    # ---- bottom caption (the punchline) -------------------------------
    font_bot = load_font("DejaVuSans-Bold.ttf", 78)
    text_center(d, 812, BOTTOM_LINES[0], font_bot, RED)
    text_center(d, 894, BOTTOM_LINES[1], font_bot, RED)

    return img


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        from PIL import Image  # noqa: F401  (presence check)
        img = draw_meme()
        img.save(OUT_PATH, format="PNG")
    except ImportError:
        fallback = os.path.join(HERE, "entry.png")
        if not os.path.exists(fallback):
            raise
        shutil.copyfile(fallback, OUT_PATH)
    print("wrote", OUT_PATH)


if __name__ == "__main__":
    main()
