#!/usr/bin/env python3
"""Draw entry.png for news-image-20261118: Wednesday 18 November 2026.

One 1024x1024 newspaper front page, drawn with Pillow + DejaVu only.
Deterministic: no random, no network, no timestamps in the PNG.
Run: python3 draw.py  -> writes entry.png beside this file.
Stories verified 19 Nov 2026 WIB in Reuters/AP/AFP digests for 18 Nov 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
NAVY = (18, 38, 74)
RED = (178, 34, 34)
BLUE = (30, 90, 160)
TEAL = (14, 110, 110)
ORANGE = (214, 92, 20)
GREEN = (30, 120, 60)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((24, 10), "THE WORLD IN ONE DAY", font=font(SANSB, 26), fill=(255, 214, 90))
d.text((24, 38), "WEDNESDAY 18 NOVEMBER 2026", font=font(SERIFB, 46), fill=WHITE)
d.text((24, 96), "The day's world news  —  in one image",
       font=font(SANS, 20), fill=(200, 210, 230))

# ---- Lead: Xi meets Putin in Shenzhen, full width ----
lx, ly, lw, lh = 16, 132, 992, 268
d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([lx, ly, lx + lw, ly + 34], radius=10, fill=RED)
d.rectangle([lx, ly + 20, lx + lw, ly + 34], fill=RED)
d.text((lx + 12, ly + 6), "LEAD  •  ASIA  •  APEC SHENZHEN", font=font(SANSB, 17), fill=WHITE)
d.text((lx + 14, ly + 44), "XI MEETS PUTIN",
       font=font(SANSB, 38), fill=INK)
d.text((lx + 14, ly + 88),
       "Trilateral summit with Trump",
       font=font(SANS, 21), fill=INK)
d.text((lx + 14, ly + 114),
       "set for Thursday in China.",
       font=font(SANS, 21), fill=INK)
d.text((lx + 14, ly + 142),
       "Xi hits protectionism; Putin hits sanctions.",
       font=font(SANSB, 19), fill=RED)
# Three flags on the right: China, Russia, USA
for i, lab in enumerate(["CHINA", "RUSSIA", "USA"]):
    fx = 560 + i * 145
    fy = ly + 70
    if i == 0:
        d.rectangle([fx, fy, fx + 120, fy + 70], fill=(200, 20, 20))
        d.text((fx + 42, fy + 16), "*", font=font(SANSB, 32), fill=(255, 220, 0))
    elif i == 1:
        d.rectangle([fx, fy, fx + 120, fy + 70], fill=WHITE)
        d.rectangle([fx, fy + 23, fx + 120, fy + 47], fill=(30, 90, 200))
        d.rectangle([fx, fy + 47, fx + 120, fy + 70], fill=RED)
    else:
        for s in range(7):
            d.rectangle([fx, fy + s * 10, fx + 120, fy + s * 10 + 10],
                        fill=RED if s % 2 == 0 else WHITE)
        d.rectangle([fx, fy, fx + 50, fy + 30], fill=NAVY)
    d.rectangle([fx, fy, fx + 120, fy + 70], outline=INK, width=2)
    d.text((fx + 18, fy + 78), lab, font=font(SANSB, 18), fill=INK)
d.text((560, ly + 200), "APEC opens; Quad meets in Manila too.",
       font=font(SANS, 18), fill=INK)

# ---- Row 2: Gulf strikes (left) and Crimea Bridge again (right) ----
y2, h2 = 416, 248
hx, hw = 16, 488
d.rounded_rectangle([hx, y2, hx + hw, y2 + h2], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([hx, y2, hx + hw, y2 + 34], radius=10, fill=ORANGE)
d.rectangle([hx, y2 + 20, hx + hw, y2 + 34], fill=ORANGE)
d.text((hx + 12, y2 + 6), "MIDDLE EAST", font=font(SANSB, 17), fill=WHITE)
d.text((hx + 12, y2 + 44), "IRAN STRIKES GULF BASES", font=font(SANSB, 28), fill=INK)
d.text((hx + 12, y2 + 82), "KUWAIT AND BAHRAIN HIT",
       font=font(SANSB, 22), fill=INK)
tx, ty = hx + 30, y2 + 150
d.rectangle([tx, ty, tx + 240, ty + 34], fill=INK)
d.rectangle([tx + 180, ty - 28, tx + 220, ty], fill=INK)
for fx, fh in [(tx + 20, 46), (tx + 70, 62), (tx + 130, 50), (tx + 185, 58)]:
    d.polygon([(fx, ty), (fx + 18, ty - fh), (fx + 36, ty)], fill=ORANGE)
d.rectangle([tx - 10, ty + 34, tx + 260, ty + 58], fill=(70, 140, 190))
d.text((hx + 12, y2 + 214),
       "After US jets hit Qeshm Island; tankers burn.",
       font=font(SANS, 18), fill=INK)

mx, mw = 520, 488
d.rounded_rectangle([mx, y2, mx + mw, y2 + h2], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([mx, y2, mx + mw, y2 + 34], radius=10, fill=BLUE)
d.rectangle([mx, y2 + 20, mx + mw, y2 + 34], fill=BLUE)
d.text((mx + 12, y2 + 6), "EUROPE  •  UKRAINE", font=font(SANSB, 17), fill=WHITE)
d.text((mx + 12, y2 + 44), "CRIMEA BRIDGE HIT AGAIN",
       font=font(SANSB, 28), fill=INK)
d.text((mx + 12, y2 + 82), "THIRD ATTACK IN FOUR DAYS",
       font=font(SANSB, 20), fill=INK)
# Bridge drawing, lower right of the card
bx, by = mx + 30, y2 + 120
d.rectangle([bx, by + 55, bx + 400, by + 100], fill=(70, 140, 190))
d.rectangle([bx, by + 10, bx + 150, by + 22], fill=NAVY)
d.rectangle([bx + 250, by + 10, bx + 400, by + 22], fill=NAVY)
d.rectangle([bx + 20, by - 20, bx + 32, by + 22], fill=NAVY)
d.rectangle([bx + 368, by - 20, bx + 380, by + 22], fill=NAVY)
d.polygon([(bx + 165, by + 22), (bx + 235, by + 22), (bx + 215, by + 80),
           (bx + 185, by + 80)], fill=(120, 120, 120))
d.text((mx + 12, y2 + 214),
       "Road arch fell Tuesday; Russia hits Izmail port.",
       font=font(SANS, 18), fill=INK)

# ---- Row 3: Senate (left) and Ebola (right) ----
y3, h3 = 680, 212
ax, aw = 16, 488
d.rounded_rectangle([ax, y3, ax + aw, y3 + h3], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([ax, y3, ax + aw, y3 + 34], radius=10, fill=NAVY)
d.rectangle([ax, y3 + 20, ax + aw, y3 + 34], fill=NAVY)
d.text((ax + 12, y3 + 6), "USA  •  SENATE", font=font(SANSB, 17), fill=WHITE)
d.text((ax + 12, y3 + 44), "PELTOLA WINS ALASKA",
       font=font(SANSB, 28), fill=INK)
d.text((ax + 12, y3 + 76), "DEMOCRATS TAKE 56-44",
       font=font(SANSB, 26), fill=INK)
d.text((ax + 12, y3 + 112), "Ninth Senate flip of the midterms;",
       font=font(SANS, 18), fill=INK)
d.text((ax + 12, y3 + 134), "largest majority since 2009.",
       font=font(SANS, 18), fill=INK)
d.text((ax + 12, y3 + 168), "Democrat beats Dan Sullivan in Alaska.",
       font=font(SANSB, 17), fill=NAVY)

nx, nw = 520, 488
d.rounded_rectangle([nx, y3, nx + nw, y3 + h3], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([nx, y3, nx + nw, y3 + 34], radius=10, fill=RED)
d.rectangle([nx, y3 + 20, nx + nw, y3 + 34], fill=RED)
d.text((nx + 12, y3 + 6), "HEALTH  •  CONGO", font=font(SANSB, 17), fill=WHITE)
d.text((nx + 12, y3 + 44), "EBOLA PASSES 11,000",
       font=font(SANSB, 30), fill=INK)
d.text((nx + 12, y3 + 82), "Second-largest outbreak on record;",
       font=font(SANS, 19), fill=INK)
d.text((nx + 12, y3 + 106), "children hit hardest.",
       font=font(SANS, 19), fill=INK)
for cx, cy, r in [(nx + 400, y3 + 150, 22), (nx + 435, y3 + 175, 13)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(120, 0, 0), width=2)
    for dx, dy in [(0, -r), (0, r), (-r, 0), (r, 0)]:
        d.line([cx, cy, cx + dx, cy + dy], fill=(120, 0, 0), width=3)
d.text((nx + 12, y3 + 168), "3 in 4 children under 5 do not survive.",
       font=font(SANSB, 17), fill=RED)

# ---- Bottom strip ----
sy, sh = 908, 100
d.rounded_rectangle([16, sy, 1008, sy + sh], radius=10,
                    fill=NAVY, outline=INK, width=2)
d.text((28, sy + 12), "ALSO TODAY:", font=font(SANSB, 18), fill=(255, 214, 90))
d.text((28, sy + 38), "Nvidia revenue doubles to $115.8B  •  Voyager 1 reaches one light-day from Earth",
       font=font(SANS, 18), fill=WHITE)
d.text((28, sy + 62), "Cyclone Akvan nears Andhra  •  India-Japan 2+2 talks in Tokyo",
       font=font(SANS, 18), fill=WHITE)

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
