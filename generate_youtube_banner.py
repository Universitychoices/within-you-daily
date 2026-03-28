#!/usr/bin/env python3
"""
WITHIN YOU DAILY — YouTube Banner
2560 x 1440 px @ 100 DPI
Matches IRIS_B_inferno logo exactly:
  - Same #070300 warm-black background
  - Same fire-spectrum iris (amber → orange → red-black)
  - Same Lora Bold amber typography
Safe zone: centre 1546 x 423 px (x: 507–2053, y: 508–931)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ─────────────────────────────────────────────────────────────
FONTS = (
    r"C:\Users\Acer\AppData\Roaming\Claude\local-agent-mode-sessions"
    r"\skills-plugin\93ddaecc-7407-4be1-ae40-ebe282b3d9f5"
    r"\dcb3680c-405d-4c27-9628-d8a399da84ef\skills\canvas-design\canvas-fonts"
)
OUT = r"D:\desktop\Desktop\WithInYou"

fp = lambda f: FontProperties(fname=os.path.join(FONTS, f))
F_LORA_B  = fp('Lora-Bold.ttf')
F_LORA_IT = fp('Lora-Italic.ttf')
F_JURA_L  = fp('Jura-Light.ttf')
F_INSTR   = fp('InstrumentSans-Regular.ttf')
F_ARSENAL = fp('ArsenalSC-Regular.ttf')

# ─────────────────────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────────────────────

def banner():
    BG = '#070300'
    np.random.seed(99)

    # ── Canvas: 2560×1440 px ─────────────────────────────────
    fig = plt.figure(figsize=(25.6, 14.4), dpi=100, facecolor=BG)
    ax  = fig.add_axes([0, 0, 1, 1], facecolor=BG)
    ax.set_xlim(0, 2560)
    ax.set_ylim(0, 1440)
    ax.axis('off')

    # ── Iris dimensions (scaled from logo proportions) ────────
    # Logo was in 10-unit space; scale ≈ 232 to reach ~560px radius
    cx, cy  = 545, 720      # iris centre — left portion of canvas
    R_pup   = 116           # pupil
    R_in    = 144           # inner iris edge
    R_out   = 560           # outer iris / limbus
    R_deco  = 632           # decorative precision ring

    # ── Fire colour palette (matches logo exactly) ────────────
    FIRE = ['#FFD840','#F0A820','#E07010','#C84800','#A02E00','#7A1800']
    F_OUTER  = '#4A0E00'
    F_MID    = '#C04000'
    F_INNER  = '#F08010'

    # ══════════════════════════════════════════════════════════
    #  BACKGROUND GLOW — warm fire light radiating from iris
    # ══════════════════════════════════════════════════════════
    for r, a, col in [
        (1400, 0.012, '#1E0500'),
        (1050, 0.022, '#2E0900'),
        ( 780, 0.038, '#420E00'),
        ( 560, 0.060, '#5C1600'),
        ( 380, 0.092, '#782000'),
        ( 230, 0.135, '#952A00'),
        ( 120, 0.185, '#AE3400'),
        (  55, 0.250, '#C03E00'),
    ]:
        ax.add_patch(mpatches.Circle((cx, cy), r, facecolor=col, alpha=a, zorder=0))

    # Subtle warm glow that bleeds rightward behind the text
    ax.add_patch(mpatches.Circle((cx, cy), 1600, facecolor='#1A0400', alpha=0.018, zorder=0))

    # ══════════════════════════════════════════════════════════
    #  IRIS BASE FILL — sparse so individual fibers pop
    # ══════════════════════════════════════════════════════════
    for i in range(80):
        frac = i / 79.0
        r    = R_in + (R_out - R_in) * frac
        if   frac < 0.25: col, ba = F_INNER, 0.030 + 0.038*(0.25-frac)
        elif frac < 0.55: col, ba = F_MID,   0.015
        else:             col, ba = F_OUTER,  0.011
        ax.add_patch(mpatches.Circle((cx, cy), r, facecolor=col, alpha=ba, zorder=1))

    # ══════════════════════════════════════════════════════════
    #  IRIS FIBERS — 18 crypts × 20 fine fibers = 360 total
    # ══════════════════════════════════════════════════════════
    n_crypts = 18
    fibers_per = 20
    sector = 2 * np.pi / n_crypts

    for c in range(n_crypts):
        base = 2 * np.pi * c / n_crypts

        # Major crypt
        ca  = base + 0.008 * (np.random.rand() - 0.5)
        rs0 = R_in  + int(9  * np.random.rand())
        rs1 = R_out - int(14 * np.random.rand())
        ax.plot([cx + rs0*np.cos(ca), cx + rs1*np.cos(ca)],
                [cy + rs0*np.sin(ca), cy + rs1*np.sin(ca)],
                color='#FFD840', linewidth=1.6, alpha=0.42, zorder=3)

        # Fine fibers
        for f in range(fibers_per):
            fa = base + sector * (f + 1) / (fibers_per + 1)
            r0 = R_in  + int(14 * np.random.rand())
            r1 = R_out - int(19 * np.random.rand())
            a  = 0.15 + 0.28 * np.random.rand()
            lw = 0.75 + 0.65 * np.random.rand()
            ci = min(int(np.random.rand() * 3.2), 5)
            ax.plot([cx + r0*np.cos(fa), cx + r1*np.cos(fa)],
                    [cy + r0*np.sin(fa), cy + r1*np.sin(fa)],
                    color=FIRE[ci], linewidth=lw, alpha=a, zorder=2)

    # ══════════════════════════════════════════════════════════
    #  IRIS BAND RINGS
    # ══════════════════════════════════════════════════════════
    th = np.linspace(0, 2*np.pi, 800)
    for r_b, col_b, a_b in [
        (R_in  + 55,  '#F08020', 0.20),
        (R_in  + 145, '#C05010', 0.16),
        (R_in  + 268, '#904010', 0.13),
        (R_in  + 395, '#603010', 0.10),
    ]:
        ax.plot(cx + r_b*np.cos(th), cy + r_b*np.sin(th),
                color=col_b, linewidth=0.85, alpha=a_b, zorder=3)

    # ══════════════════════════════════════════════════════════
    #  LIMBUS — heavy dark ring defining iris boundary
    # ══════════════════════════════════════════════════════════
    ax.add_patch(mpatches.Circle((cx, cy), R_out + 38, fill=False,
                                  edgecolor='#0D0200', linewidth=22.0, alpha=0.97, zorder=5))
    ax.plot(cx + R_out*np.cos(th), cy + R_out*np.sin(th),
            color='#3A0800', linewidth=1.6, alpha=0.45, zorder=5)

    # ══════════════════════════════════════════════════════════
    #  PUPIL
    # ══════════════════════════════════════════════════════════
    ax.add_patch(mpatches.Circle((cx, cy), R_pup, facecolor='#030100', alpha=1.0, zorder=7))
    # Corona glow rings around pupil
    for rg, ag, cg in [
        (182, 0.28, F_INNER), (210, 0.18, F_MID),
        (242, 0.10, F_OUTER), (278, 0.05, '#601000'),
    ]:
        ax.add_patch(mpatches.Circle((cx, cy), rg, facecolor=cg, alpha=ag, zorder=6))

    # ══════════════════════════════════════════════════════════
    #  OUTER PRECISION RING WITH TICK MARKS
    # ══════════════════════════════════════════════════════════
    ax.plot(cx + R_deco*np.cos(th), cy + R_deco*np.sin(th),
            color='#602000', linewidth=2.2, alpha=0.35, zorder=5)
    ax.plot(cx + (R_deco+18)*np.cos(th), cy + (R_deco+18)*np.sin(th),
            color='#3A1000', linewidth=0.9, alpha=0.16, zorder=5)

    for deg in range(0, 360, 4):
        rad = np.radians(deg)
        if   deg % 40 == 0: tl, tw, ta = 44, 1.6, 0.28
        elif deg % 20 == 0: tl, tw, ta = 28, 1.1, 0.19
        else:               tl, tw, ta = 13, 0.8, 0.13
        r0 = R_deco - tl
        ax.plot([cx + r0*np.cos(rad), cx + R_deco*np.cos(rad)],
                [cy + r0*np.sin(rad), cy + R_deco*np.sin(rad)],
                color='#C04800', linewidth=tw, alpha=ta, zorder=5)

    # ══════════════════════════════════════════════════════════
    #  SPECULAR HIGHLIGHTS
    # ══════════════════════════════════════════════════════════
    ax.plot(cx + 50, cy + 50, 'o', color='white',    markersize=16, alpha=0.75, zorder=10)
    ax.plot(cx - 34, cy + 74, 'o', color='#FFF8C0', markersize=7,  alpha=0.38, zorder=10)

    # ══════════════════════════════════════════════════════════
    #  SAFE-ZONE SAFE ZONE MARKER (debug — remove for final)
    #  Uncomment to see safe zone:
    #  rect = mpatches.Rectangle((507,508),1546,423,fill=False,edgecolor='cyan',linewidth=1)
    #  ax.add_patch(rect)
    # ══════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════
    #  FULL-WIDTH CENTRE LINE (very subtle — visual anchor)
    # ══════════════════════════════════════════════════════════
    ax.plot([0, 2560], [720, 720], color='#220600', linewidth=1.0, alpha=0.22, zorder=4)

    # ══════════════════════════════════════════════════════════
    #  VERTICAL SEPARATOR between iris zone and text zone
    # ══════════════════════════════════════════════════════════
    ax.plot([1200, 1200], [240, 1200], color='#3A0E00', linewidth=1.0, alpha=0.28, zorder=4)

    # ══════════════════════════════════════════════════════════
    #  TYPOGRAPHY  (everything within safe zone x:1240–2050)
    # ══════════════════════════════════════════════════════════

    # ── Channel name ──────────────────────────────────────────
    # "WITHIN YOU" — large, dominant, fire amber
    ax.text(1268, 830,
            'WITHIN YOU',
            fontproperties=F_LORA_B,
            fontsize=108,
            color='#C85818',
            ha='left', va='center',
            alpha=0.96,
            zorder=8)

    # ── Thin rule between title and sub ───────────────────────
    ax.plot([1268, 2060], [700, 700],
            color='#3A0E00', linewidth=1.8, alpha=0.50, zorder=4)

    # ── "DAILY" ───────────────────────────────────────────────
    ax.text(1268, 572,
            'D  A  I  L  Y',
            fontproperties=F_JURA_L,
            fontsize=52,
            color='#8A3010',
            ha='left', va='center',
            alpha=0.72,
            zorder=8)

    # ── Fine tagline ──────────────────────────────────────────
    ax.text(1272, 430,
            'IGNITE  THE  FIRE  WITHIN',
            fontproperties=F_ARSENAL,
            fontsize=26,
            color='#5A1E08',
            ha='left', va='center',
            alpha=0.55,
            zorder=8)

    # ── Bottom rule ───────────────────────────────────────────
    ax.plot([1268, 2060], [395, 395],
            color='#2A0800', linewidth=0.8, alpha=0.35, zorder=4)

    # ══════════════════════════════════════════════════════════
    #  SAVE
    # ══════════════════════════════════════════════════════════
    path = os.path.join(OUT, 'WITHIN_YOU_youtube_banner.png')
    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor(), edgecolor='none',
                bbox_inches=None)
    plt.close(fig)
    print(f"  Saved: WITHIN_YOU_youtube_banner.png  (2560 x 1440 px)")


banner()
print()
print("  YouTube banner complete.")
print("  Upload at: YouTube Studio > Customisation > Branding > Banner image")
print()
