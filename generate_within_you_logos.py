#!/usr/bin/env python3
"""
WITHIN YOU DAILY — 5 Logo Concepts
Endogenous Light design philosophy
Cinematic identity for YouTube, Instagram, TikTok
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
from matplotlib.collections import LineCollection
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────

FONTS_DIR = (
    r"C:\Users\Acer\AppData\Roaming\Claude\local-agent-mode-sessions"
    r"\skills-plugin\93ddaecc-7407-4be1-ae40-ebe282b3d9f5"
    r"\dcb3680c-405d-4c27-9628-d8a399da84ef\skills\canvas-design\canvas-fonts"
)
OUTPUT_DIR = r"D:\desktop\Desktop"


# ─────────────────────────────────────────────
# FONTS
# ─────────────────────────────────────────────

def font(f):
    return FontProperties(fname=os.path.join(FONTS_DIR, f))

F_ITALIANA   = font('Italiana-Regular.ttf')
F_JURA_L     = font('Jura-Light.ttf')
F_JURA_M     = font('Jura-Medium.ttf')
F_BIG_BOLD   = font('BigShoulders-Bold.ttf')
F_ARSENAL    = font('ArsenalSC-Regular.ttf')
F_POIRET     = font('PoiretOne-Regular.ttf')
F_LORA_IT    = font('Lora-Italic.ttf')
F_LORA_BOLD  = font('Lora-Bold.ttf')
F_WORK       = font('WorkSans-Regular.ttf')
F_INSTR      = font('InstrumentSans-Regular.ttf')
F_GLOOCK     = font('Gloock-Regular.ttf')


# ─────────────────────────────────────────────
# GOLD PALETTE — endogenous warmth
# ─────────────────────────────────────────────

G0 = '#1C0A00'   # shadow / near-black
G1 = '#3A1E00'   # darkest bronze
G2 = '#6E4206'   # bronze
G3 = '#A07018'   # mid gold
G4 = '#C49828'   # primary gold
G5 = '#DEC050'   # bright gold
G6 = '#F4E8A8'   # pale cream


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def make_fig(bg='#080808'):
    fig = plt.figure(figsize=(10, 10), facecolor=bg)
    ax = fig.add_axes([0, 0, 1, 1], facecolor=bg)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def save_fig(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"  Saved: {name}")


def flame_path(cx, cy, w, h):
    """Smooth bezier flame / teardrop shape"""
    bx, by = cx, cy - h * 0.48
    tx, ty = cx, cy + h * 0.52
    verts = [
        (bx,            by),
        (bx - w*0.68,   by + h*0.18),
        (bx - w*0.50,   by + h*0.74),
        (tx,            ty),
        (bx + w*0.50,   by + h*0.74),
        (bx + w*0.68,   by + h*0.18),
        (bx,            by),
        (bx,            by),
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    return Path(verts, codes)


def add_circle(ax, cx, cy, r, **kwargs):
    ax.add_patch(mpatches.Circle((cx, cy), r, **kwargs))


def add_polygon(ax, pts, **kwargs):
    ax.add_patch(mpatches.Polygon(pts, closed=True, **kwargs))


# ═══════════════════════════════════════════════════════════════
#  LOGO 1 — THE EMBER
#  Five nested flame layers, deep bronze to pale cream
#  Italiana serif wordmark, Jura subtitle
# ═══════════════════════════════════════════════════════════════

def logo_1():
    BG = '#080808'
    fig, ax = make_fig(BG)

    cx, cy = 5.0, 5.55
    bw, bh = 1.85, 3.20

    # Soft ambient glow behind flame
    for r, a in [(3.2, 0.025), (2.4, 0.045), (1.6, 0.07), (0.9, 0.10)]:
        add_circle(ax, cx, cy, r, facecolor=G3, alpha=a, zorder=0)

    # Five nested flames — outer darkest → inner brightest
    layers = [
        (1.00, G1, 0.95),
        (0.78, G2, 0.95),
        (0.57, G3, 0.95),
        (0.38, G4, 0.95),
        (0.19, G6, 0.95),
    ]
    for scale, color, alpha in layers:
        p = flame_path(cx, cy + 0.06 * scale, bw * scale, bh * scale)
        ax.add_patch(mpatches.PathPatch(p, facecolor=color, edgecolor='none',
                                        alpha=alpha, zorder=2))

    # Thin golden separator
    ax.plot([3.60, 6.40], [3.15, 3.15], color=G2, linewidth=0.70, alpha=0.50)

    # "WITHIN YOU" — Italiana, wide tracking
    ax.text(5.0, 2.68, 'W I T H I N   Y O U',
            fontproperties=F_ITALIANA, fontsize=21,
            color=G5, ha='center', va='center')

    # "DAILY" — Jura Light, maximum spacing
    ax.text(5.0, 2.08, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=9,
            color=G3, ha='center', va='center')

    save_fig(fig, 'within_you_logo_1_ember.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 2 — THE ARC
#  Rising sun on deep navy — radial rays, semicircle, inner orb
#  BigShoulders bold wordmark
# ═══════════════════════════════════════════════════════════════

def logo_2():
    BG = '#06091A'
    fig, ax = make_fig(BG)

    cx, cy = 5.0, 4.85
    R = 2.52

    # 14 radial rays fanning upward
    for deg in np.linspace(8, 172, 14):
        rad = np.radians(deg)
        alpha = max(0.14, 1.0 - abs(deg - 90) / 84.0) * 0.52
        ax.plot([cx, cx + R * np.cos(rad)],
                [cy, cy + R * np.sin(rad)],
                color=G4, linewidth=0.72, alpha=alpha)

    # Outer arc
    th = np.linspace(0, np.pi, 400)
    ax.plot(cx + R * np.cos(th), cy + R * np.sin(th),
            color=G4, linewidth=1.0, alpha=0.60)

    # Mid arc
    R2 = R * 0.56
    ax.plot(cx + R2 * np.cos(th), cy + R2 * np.sin(th),
            color=G3, linewidth=0.45, alpha=0.32)

    # Baseline
    ax.plot([cx - R - 0.25, cx + R + 0.25], [cy, cy],
            color=G4, linewidth=0.85, alpha=0.42)

    # Small baseline tick marks
    for xt in np.linspace(cx - R - 0.1, cx + R + 0.1, 11):
        ax.plot([xt, xt], [cy - 0.07, cy + 0.07],
                color=G3, linewidth=0.45, alpha=0.28)

    # Inner sun — layered glow
    for r, a in [(0.58, 0.06), (0.38, 0.12), (0.22, 0.20)]:
        add_circle(ax, cx, cy, r, facecolor=G5, alpha=a, zorder=3)
    add_circle(ax, cx, cy, 0.13, facecolor=G6, alpha=0.90, zorder=4)

    # "WITHIN  YOU" — BigShoulders Bold, commanding
    ax.text(5.0, 3.55, 'WITHIN  YOU',
            fontproperties=F_BIG_BOLD, fontsize=32,
            color=G6, ha='center', va='center', alpha=0.90)

    ax.plot([3.20, 6.80], [3.18, 3.18], color=G1, linewidth=0.60, alpha=0.75)

    ax.text(5.0, 2.78, 'D  A  I  L  Y',
            fontproperties=F_INSTR, fontsize=10,
            color=G4, ha='center', va='center', alpha=0.62)

    save_fig(fig, 'within_you_logo_2_arc.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 3 — THE COMPASS
#  Precision geometric compass rose — inner navigation symbol
#  Arsenal SC wordmark
# ═══════════════════════════════════════════════════════════════

def logo_3():
    BG = '#0B0B0B'
    fig, ax = make_fig(BG)

    cx, cy = 5.0, 5.38
    R1 = 2.46   # outer ring
    R2 = 1.92   # inner ring
    R3 = 1.02   # band circle

    # Rings
    add_circle(ax, cx, cy, R1, fill=False, edgecolor=G3, linewidth=1.10, alpha=0.55)
    add_circle(ax, cx, cy, R2, fill=False, edgecolor=G3, linewidth=0.55, alpha=0.35)
    add_circle(ax, cx, cy, R3, fill=False, edgecolor=G3, linewidth=0.32, alpha=0.22)

    # Cardinal directions — spokes + diamond tips
    for deg in [0, 90, 180, 270]:
        rad = np.radians(deg)
        # Spoke
        ax.plot([cx + R3 * np.cos(rad), cx + R2 * np.cos(rad)],
                [cy + R3 * np.sin(rad), cy + R2 * np.sin(rad)],
                color=G4, linewidth=0.95, alpha=0.65)
        # Diamond tip
        tx = cx + (R2 + 0.16) * np.cos(rad)
        ty = cy + (R2 + 0.16) * np.sin(rad)
        perp = rad + np.pi / 2
        dl, dw = 0.19, 0.07
        pts = [
            [tx + dl * np.cos(rad),   ty + dl * np.sin(rad)],
            [tx + dw * np.cos(perp),  ty + dw * np.sin(perp)],
            [tx - dl * np.cos(rad),   ty - dl * np.sin(rad)],
            [tx - dw * np.cos(perp),  ty - dw * np.sin(perp)],
        ]
        add_polygon(ax, pts, facecolor=G5, edgecolor='none', alpha=0.82)

    # Diagonal spokes
    for deg in [45, 135, 225, 315]:
        rad = np.radians(deg)
        ax.plot([cx + R3 * np.cos(rad), cx + R2 * 0.86 * np.cos(rad)],
                [cy + R3 * np.sin(rad), cy + R2 * 0.86 * np.sin(rad)],
                color=G3, linewidth=0.42, alpha=0.38)
        ax.plot(cx + R2 * 0.86 * np.cos(rad),
                cy + R2 * 0.86 * np.sin(rad),
                'o', color=G4, markersize=2.4, alpha=0.48)

    # Minor ticks — 16-point
    for deg in np.arange(0, 360, 22.5):
        if deg % 45 != 0:
            rad = np.radians(deg)
            ax.plot([cx + (R2 - 0.13) * np.cos(rad), cx + R2 * np.cos(rad)],
                    [cy + (R2 - 0.13) * np.sin(rad), cy + R2 * np.sin(rad)],
                    color=G3, linewidth=0.32, alpha=0.26)

    # Outer micro-ticks — 32-point
    for deg in np.arange(0, 360, 11.25):
        if deg % 22.5 != 0:
            rad = np.radians(deg)
            ax.plot([cx + (R1 - 0.09) * np.cos(rad), cx + R1 * np.cos(rad)],
                    [cy + (R1 - 0.09) * np.sin(rad), cy + R1 * np.sin(rad)],
                    color=G2, linewidth=0.28, alpha=0.20)

    # Crosshairs
    ax.plot([cx - R3, cx + R3], [cy, cy], color=G3, linewidth=0.38, alpha=0.22)
    ax.plot([cx, cx], [cy - R3, cy + R3], color=G3, linewidth=0.38, alpha=0.22)

    # Center jewel
    add_circle(ax, cx, cy, 0.22, facecolor=G5, edgecolor=G3,
               linewidth=0.65, alpha=0.85, zorder=6)
    add_circle(ax, cx, cy, 0.07, facecolor=BG, alpha=1.0, zorder=7)

    # Text
    ax.text(5.0, 2.44, 'W I T H I N   Y O U',
            fontproperties=F_ARSENAL, fontsize=18,
            color=G5, ha='center', va='center')

    ax.plot([3.20, 6.80], [2.10, 2.10], color=G1, linewidth=0.52, alpha=0.60)

    ax.text(5.0, 1.73, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=9,
            color=G3, ha='center', va='center', alpha=0.62)

    save_fig(fig, 'within_you_logo_3_compass.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 4 — THE SUMMIT
#  Outlined mountain triangle, inner elevation lines, apex orb
#  PoiretOne airy wordmark
# ═══════════════════════════════════════════════════════════════

def logo_4():
    BG = '#080808'
    fig, ax = make_fig(BG)

    cx   = 5.0
    by   = 4.30    # base y
    ay   = 7.78    # apex y
    lx   = 2.45    # left base x
    rx   = 7.55    # right base x

    # Outer triangle — thin gold outline
    add_polygon(ax, [[lx, by], [cx, ay], [rx, by]],
                fill=False, edgecolor=G4, linewidth=1.25, alpha=0.70)

    # Inner triangle — ghost outline
    s = 0.50
    add_polygon(ax,
                [[cx - (cx-lx)*s, ay - (ay-by)*s],
                 [cx, ay - 0.06],
                 [cx + (rx-cx)*s, ay - (ay-by)*s]],
                fill=False, edgecolor=G3, linewidth=0.38, alpha=0.20)

    # Horizontal elevation bands inside triangle
    for frac in [0.22, 0.44, 0.64, 0.80]:
        y_line = by + (ay - by) * frac
        hw = (cx - lx) * (1.0 - frac)
        ax.plot([cx - hw + 0.10, cx + hw - 0.10], [y_line, y_line],
                color=G3, linewidth=0.26, alpha=0.16)

    # Baseline extension with end ticks
    ax.plot([lx - 0.45, rx + 0.45], [by, by], color=G3, linewidth=0.65, alpha=0.32)
    for xt in [lx - 0.45, lx, rx, rx + 0.45]:
        ax.plot([xt, xt], [by - 0.08, by + 0.08], color=G3, linewidth=0.45, alpha=0.25)

    # Apex light source — layered glow
    for r, a in [(0.65, 0.04), (0.42, 0.09), (0.25, 0.17)]:
        add_circle(ax, cx, ay, r, facecolor=G5, alpha=a, zorder=3)
    add_circle(ax, cx, ay, 0.20, facecolor=G6, alpha=0.88, zorder=4)

    # Text — PoiretOne, airy geometry
    ax.text(5.0, 3.44, 'W I T H I N   Y O U',
            fontproperties=F_POIRET, fontsize=26,
            color=G6, ha='center', va='center', alpha=0.88)

    ax.plot([3.45, 6.55], [3.08, 3.08], color=G1, linewidth=0.52, alpha=0.62)

    ax.text(5.0, 2.68, 'D  A  I  L  Y',
            fontproperties=F_POIRET, fontsize=10,
            color=G3, ha='center', va='center', alpha=0.68)

    save_fig(fig, 'within_you_logo_4_summit.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 5 — THE SPIRAL
#  Archimedean spiral — gold gradient line, inner growth philosophy
#  Lora Italic elegant serif wordmark
# ═══════════════════════════════════════════════════════════════

def logo_5():
    BG = '#070707'
    fig, ax = make_fig(BG)

    cx, cy = 5.0, 5.38
    R_max  = 2.52
    turns  = 2.9
    t_max  = turns * 2 * np.pi
    n      = 3200

    theta = np.linspace(0.04, t_max, n)
    r     = (R_max / t_max) * theta
    x     = cx + r * np.cos(theta)
    y     = cy + r * np.sin(theta)

    # Gradient line — near-black → bright gold
    pts  = np.array([x, y]).T.reshape(-1, 1, 2)
    segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
    prog = np.linspace(0, 1, len(segs))

    def gold_rgba(p):
        return (0.04 + 0.78 * p,   # R
                0.02 + 0.60 * p,   # G
                0.0,               # B
                0.08 + 0.84 * p)   # alpha

    lc = LineCollection(segs, colors=[gold_rgba(p) for p in prog],
                        linewidth=1.25, zorder=3)
    ax.add_collection(lc)

    # Thin outer boundary circle
    add_circle(ax, cx, cy, R_max + 0.07, fill=False,
               edgecolor=G2, linewidth=0.45, alpha=0.18, zorder=2)

    # Center anchor dot
    add_circle(ax, cx, cy, 0.065, facecolor=G6, alpha=0.82, zorder=5)

    # Main title — Lora Italic, classic serif elegance
    ax.text(5.0, 2.42, 'Within  You',
            fontproperties=F_LORA_IT, fontsize=28,
            color=G6, ha='center', va='center', alpha=0.88)

    ax.plot([3.55, 6.45], [2.07, 2.07], color=G1, linewidth=0.58, alpha=0.58)

    ax.text(5.0, 1.68, 'D  A  I  L  Y',
            fontproperties=F_WORK, fontsize=9.5,
            color=G3, ha='center', va='center', alpha=0.58)

    save_fig(fig, 'within_you_logo_5_spiral.png')


# ─────────────────────────────────────────────
# EXECUTE
# ─────────────────────────────────────────────

print()
print("  WITHIN YOU DAILY -- Logo Collection")
print("  ====================================")
print()

logo_1(); print("  1/5  The Ember      — nested flame in deep bronze")
logo_2(); print("  2/5  The Arc        — rising sun on midnight navy")
logo_3(); print("  3/5  The Compass    — precision inner navigation")
logo_4(); print("  4/5  The Summit     — mountain with apex light")
logo_5(); print("  5/5  The Spiral     — golden ratio inner growth")

print()
print("  All 5 logos saved to Desktop.")
print()
