#!/usr/bin/env python3
"""
WITHIN YOU DAILY -- Logo Collection Vol.2
Prismatic Depth design philosophy
5 high-impact, eye-catching concepts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
from matplotlib.collections import LineCollection
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

FONTS_DIR = (
    r"C:\Users\Acer\AppData\Roaming\Claude\local-agent-mode-sessions"
    r"\skills-plugin\93ddaecc-7407-4be1-ae40-ebe282b3d9f5"
    r"\dcb3680c-405d-4c27-9628-d8a399da84ef\skills\canvas-design\canvas-fonts"
)
OUTPUT_DIR = r"D:\desktop\Desktop"

def font(f):
    return FontProperties(fname=os.path.join(FONTS_DIR, f))

F_ITALIANA  = font('Italiana-Regular.ttf')
F_JURA_L    = font('Jura-Light.ttf')
F_JURA_M    = font('Jura-Medium.ttf')
F_ARSENAL   = font('ArsenalSC-Regular.ttf')
F_LORA_IT   = font('Lora-Italic.ttf')
F_LORA_BOLD = font('Lora-Bold.ttf')
F_WORK      = font('WorkSans-Regular.ttf')
F_INSTR     = font('InstrumentSans-Regular.ttf')
F_GLOOCK    = font('Gloock-Regular.ttf')
F_POIRET    = font('PoiretOne-Regular.ttf')
F_BIG_BOLD  = font('BigShoulders-Bold.ttf')

# Classic gold palette
G1 = '#3A1E00'; G2 = '#6E4206'; G3 = '#A07018'
G4 = '#C49828'; G5 = '#DEC050'; G6 = '#F4E8A8'

# Rose-gold / violet palette (lotus)
V0 = '#0A0614'; V1 = '#2E1228'; V2 = '#6A2A48'
RG3 = '#C07868'; RG4 = '#DFA888'; RG5 = '#F2D4BC'

# Teal/crystal palette (diamond)
T0 = '#05100E'; T1 = '#0C2A28'; T2 = '#1A5048'
TC3 = '#38907E'; TC4 = '#78C8B0'; TC5 = '#C8F0E4'


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

def circ(ax, cx, cy, r, **kw):
    ax.add_patch(mpatches.Circle((cx, cy), r, **kw))

def poly(ax, pts, **kw):
    ax.add_patch(mpatches.Polygon(pts, closed=True, **kw))

def petal_path(cx, cy, angle, length, width):
    """Smooth bezier petal pointing at `angle` from (cx,cy)"""
    p = angle + np.pi / 2
    tx = cx + length * np.cos(angle)
    ty = cy + length * np.sin(angle)
    verts = [
        (cx, cy),
        (cx + length*.30*np.cos(angle) + width*.46*np.cos(p),
         cy + length*.30*np.sin(angle) + width*.46*np.sin(p)),
        (cx + length*.72*np.cos(angle) + width*.30*np.cos(p),
         cy + length*.72*np.sin(angle) + width*.30*np.sin(p)),
        (tx, ty),
        (cx + length*.72*np.cos(angle) - width*.30*np.cos(p),
         cy + length*.72*np.sin(angle) - width*.30*np.sin(p)),
        (cx + length*.30*np.cos(angle) - width*.46*np.cos(p),
         cy + length*.30*np.sin(angle) - width*.46*np.sin(p)),
        (cx, cy),
        (cx, cy),
    ]
    codes = [Path.MOVETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.CLOSEPOLY]
    return Path(verts, codes)


# ═══════════════════════════════════════════════════════════════
#  LOGO 6 — THE IRIS
#  Geometric eye with structured crypt fibers and iris rings
#  Deep navy ground — amber iris — pale pupil glow
# ═══════════════════════════════════════════════════════════════

def logo_6_iris():
    BG = '#06080F'
    fig, ax = make_fig(BG)
    np.random.seed(42)

    cx, cy = 5.0, 5.60
    R_in   = 0.58   # pupil edge / iris start
    R_out  = 2.12   # iris outer / limbus
    R_deco = 2.48   # decorative outer ring

    # === Iris base — radial gradient fill via concentric rings ===
    for i in range(60):
        frac = i / 59.0
        r = R_in + (R_out - R_in) * frac
        # Warmth: bright amber near pupil, cooler bronze at limbus
        alpha = 0.045 + 0.055 * (1.0 - frac)
        col = G5 if frac < 0.4 else (G4 if frac < 0.7 else G3)
        circ(ax, cx, cy, r, facecolor=col, alpha=alpha, zorder=1)

    # === Iris fibers: structured crypts + fine fill ===
    n_crypts = 18
    fibers_per = 9

    for c in range(n_crypts):
        crypt_a = 2 * np.pi * c / n_crypts

        # Major crypt (slightly brighter, thicker)
        r_s = R_in + 0.04 * np.random.rand()
        r_e = R_out - 0.06 * np.random.rand()
        cos_c, sin_c = np.cos(crypt_a), np.sin(crypt_a)
        ax.plot([cx + r_s*cos_c, cx + r_e*cos_c],
                [cy + r_s*sin_c, cy + r_e*sin_c],
                color=G5, linewidth=0.55, alpha=0.28, zorder=2)

        # Fine fibers between this crypt and next
        for f in range(fibers_per):
            frac_f = (f + 1) / (fibers_per + 1)
            fa = crypt_a + 2 * np.pi / n_crypts * frac_f
            r_fs = R_in + 0.05 * np.random.rand()
            r_fe = R_out - 0.10 * np.random.rand()
            alpha_f = 0.10 + 0.14 * np.random.rand()
            lw_f = 0.20 + 0.15 * np.random.rand()
            ax.plot([cx + r_fs*np.cos(fa), cx + r_fe*np.cos(fa)],
                    [cy + r_fs*np.sin(fa), cy + r_fe*np.sin(fa)],
                    color=G4, linewidth=lw_f, alpha=alpha_f, zorder=2)

    # === Concentric iris bands ===
    for r_band in [0.85, 1.18, 1.55, 1.90]:
        th = np.linspace(0, 2*np.pi, 600)
        ax.plot(cx + r_band*np.cos(th), cy + r_band*np.sin(th),
                color=G3, linewidth=0.32, alpha=0.22, zorder=3)

    # === Limbus — heavy dark ring defining outer iris ===
    circ(ax, cx, cy, R_out + 0.10, fill=False,
         edgecolor='#1E0A00', linewidth=5.0, alpha=0.88, zorder=4)
    circ(ax, cx, cy, R_out, fill=False,
         edgecolor=G2, linewidth=0.55, alpha=0.35, zorder=4)

    # === Outer decorative ring with tick marks ===
    circ(ax, cx, cy, R_deco, fill=False,
         edgecolor=G2, linewidth=0.65, alpha=0.30, zorder=4)
    for deg in range(0, 360, 8):
        rad = np.radians(deg)
        tick_len = 0.12 if deg % 40 == 0 else 0.07
        r1, r2 = R_deco - tick_len, R_deco
        ax.plot([cx + r1*np.cos(rad), cx + r2*np.cos(rad)],
                [cy + r1*np.sin(rad), cy + r2*np.sin(rad)],
                color=G3, linewidth=0.40, alpha=0.28, zorder=4)

    # === Pupil ===
    circ(ax, cx, cy, R_in, facecolor='#040308', alpha=1.0, zorder=6)
    # Inner iris brightening ring around pupil
    for r_glow, a_glow in [(0.78, 0.16), (0.90, 0.10), (1.05, 0.05)]:
        circ(ax, cx, cy, r_glow, facecolor=G5, alpha=a_glow, zorder=5)

    # === Specular highlights ===
    ax.plot(cx + 0.22, cy + 0.22, 'o', color='white', markersize=5.5,
            alpha=0.70, zorder=9)
    ax.plot(cx - 0.14, cy + 0.32, 'o', color=G6, markersize=2.2,
            alpha=0.38, zorder=9)

    # === Typography ===
    ax.text(5.0, 2.90, 'W I T H I N   Y O U',
            fontproperties=F_GLOOCK, fontsize=20, color=G5,
            ha='center', va='center')
    ax.plot([3.70, 6.30], [2.56, 2.56], color=G2, linewidth=0.50, alpha=0.48)
    ax.text(5.0, 2.18, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=9, color=G3,
            ha='center', va='center', alpha=0.62)

    save_fig(fig, 'within_you_logo_6_iris.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 7 — THE NOVA
#  Explosive 360-degree starburst filling the canvas
#  Pure black ground — white core — amber to bronze rays
# ═══════════════════════════════════════════════════════════════

def logo_7_nova():
    BG = '#030303'
    fig, ax = make_fig(BG)
    np.random.seed(77)

    cx, cy = 5.0, 5.75   # shifted slightly up — text lives below
    max_R  = 3.85         # rays nearly reach canvas edges

    # === 360 individual rays in 4 tiers ===
    for i in range(360):
        angle = 2 * np.pi * i / 360
        cos_a, sin_a = np.cos(angle), np.sin(angle)

        rnd = np.random.rand()

        if i % 12 == 0:           # PRIMARY — 30 rays, long
            length = max_R * (0.82 + 0.16 * rnd)
            lw, alpha, col = 0.90, 0.75, G6
        elif i % 6 == 0:          # SECONDARY — 30 rays, medium-long
            length = max_R * (0.55 + 0.22 * rnd)
            lw, alpha, col = 0.60, 0.52, G5
        elif i % 3 == 0:          # TERTIARY — 60 rays, medium
            length = max_R * (0.28 + 0.28 * rnd)
            lw, alpha, col = 0.38, 0.32, G4
        else:                     # MICRO — 240 rays, short diffuse
            length = max_R * (0.08 + 0.18 * rnd)
            lw, alpha, col = 0.22, 0.14 + 0.12 * rnd, G3

        ax.plot([cx + 0.09*cos_a, cx + length*cos_a],
                [cy + 0.09*sin_a, cy + length*sin_a],
                color=col, linewidth=lw, alpha=alpha,
                zorder=2, solid_capstyle='round')

    # === Central blaze — layered glow ===
    glow = [(2.20, 0.018, G3), (1.40, 0.038, G3), (0.82, 0.08, G4),
            (0.45, 0.18, G5),  (0.22, 0.48, G6), (0.09, 1.00, 'white')]
    for r, a, c in glow:
        circ(ax, cx, cy, r, facecolor=c, alpha=a, zorder=5)

    # === Typography — tight below nova ===
    ax.text(5.0, 1.52, 'W I T H I N   Y O U',
            fontproperties=F_ITALIANA, fontsize=22, color=G5,
            ha='center', va='center', alpha=0.88)
    ax.plot([3.62, 6.38], [1.20, 1.20], color=G1, linewidth=0.55, alpha=0.52)
    ax.text(5.0, 0.84, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=9, color=G3,
            ha='center', va='center', alpha=0.60)

    save_fig(fig, 'within_you_logo_7_nova.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 8 — THE DIAMOND
#  Star-cut gemstone overhead view — interlocking facets
#  Deep teal-black ground — crystal-teal + gold facets
# ═══════════════════════════════════════════════════════════════

def logo_8_diamond():
    BG = '#050E0D'
    fig, ax = make_fig(BG)

    cx, cy  = 5.0, 5.52
    R_g     = 2.28   # girdle (outer edge)
    R_star  = 1.52   # star-facet tips
    R_table = 0.80   # inner table octagon

    # === 8 outer kite facets (girdle → R_star) ===
    for i in range(8):
        a1  = 2*np.pi * i / 8
        a3  = 2*np.pi * (i + 1) / 8
        a_mid = (a1 + a3) / 2
        p1  = [cx + R_g * np.cos(a1),    cy + R_g * np.sin(a1)]
        p2  = [cx + R_g * np.cos(a3),    cy + R_g * np.sin(a3)]
        tip = [cx + R_star * np.cos(a_mid), cy + R_star * np.sin(a_mid)]
        col = TC3 if i % 2 == 0 else T2
        alp = 0.52 if i % 2 == 0 else 0.35
        poly(ax, [p1, tip, p2], facecolor=col, edgecolor=TC4,
             linewidth=0.40, alpha=alp, zorder=2)

    # === 8 inner star facets (table → R_star) — interleaved ===
    for i in range(8):
        a_mid  = 2*np.pi * (i + 0.5) / 8
        a_left = 2*np.pi * i / 8
        a_rgt  = 2*np.pi * (i + 1) / 8
        tip   = [cx + R_star * np.cos(a_mid), cy + R_star * np.sin(a_mid)]
        p_l   = [cx + R_table * np.cos(a_left), cy + R_table * np.sin(a_left)]
        p_r   = [cx + R_table * np.cos(a_rgt),  cy + R_table * np.sin(a_rgt)]
        col = TC5 if i % 2 == 0 else TC4
        alp = 0.60 if i % 2 == 0 else 0.42
        poly(ax, [p_l, tip, p_r], facecolor=col, edgecolor=TC5,
             linewidth=0.40, alpha=alp, zorder=3)

    # === 8 table facets (inner octagon segments) ===
    for i in range(8):
        a1 = 2*np.pi * i / 8
        a2 = 2*np.pi * (i + 1) / 8
        p1 = [cx + R_table * np.cos(a1), cy + R_table * np.sin(a1)]
        p2 = [cx + R_table * np.cos(a2), cy + R_table * np.sin(a2)]
        col = TC5 if i % 2 == 0 else TC4
        alp = 0.68 if i % 2 == 0 else 0.50
        poly(ax, [[cx, cy], p1, p2], facecolor=col, edgecolor=TC5,
             linewidth=0.28, alpha=alp, zorder=4)

    # === Structural dividing lines ===
    for i in range(8):
        a = 2*np.pi * i / 8
        ax.plot([cx + R_table * np.cos(a), cx + R_g * np.cos(a)],
                [cy + R_table * np.sin(a), cy + R_g * np.sin(a)],
                color=TC4, linewidth=0.45, alpha=0.50, zorder=5)

    # === Girdle rings ===
    th = np.linspace(0, 2*np.pi, 600)
    ax.plot(cx + R_g * np.cos(th), cy + R_g * np.sin(th),
            color=TC4, linewidth=0.80, alpha=0.55, zorder=5)
    ax.plot(cx + (R_g + 0.10)*np.cos(th), cy + (R_g + 0.10)*np.sin(th),
            color=TC3, linewidth=0.35, alpha=0.22, zorder=5)

    # === Central table light ===
    for r, a, c in [(0.45, 0.15, TC4), (0.25, 0.30, TC5), (0.10, 0.80, 'white')]:
        circ(ax, cx, cy, r, facecolor=c, alpha=a, zorder=7)

    # === Typography ===
    ax.text(5.0, 2.60, 'W I T H I N   Y O U',
            fontproperties=F_LORA_BOLD, fontsize=20, color=TC5,
            ha='center', va='center', alpha=0.88)
    ax.plot([3.62, 6.38], [2.26, 2.26], color=T1, linewidth=0.52, alpha=0.52)
    ax.text(5.0, 1.90, 'D  A  I  L  Y',
            fontproperties=F_INSTR, fontsize=9, color=TC3,
            ha='center', va='center', alpha=0.62)

    save_fig(fig, 'within_you_logo_8_diamond.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 9 — THE VORTEX
#  Rotating-dash concentric rings — hypnotic inner pull
#  Near-black ground — amber gradient rings tightening inward
# ═══════════════════════════════════════════════════════════════

def logo_9_vortex():
    BG = '#070707'
    fig, ax = make_fig(BG)

    cx, cy  = 5.0, 5.52
    R_min   = 0.22
    R_max   = 2.38
    n_rings = 32
    n_dashes = 30      # segments per ring
    dash_arc  = 0.64   # fraction of segment that is filled (vs gap)

    for idx in range(n_rings):
        frac = idx / (n_rings - 1)
        R    = R_min + (R_max - R_min) * frac

        # Each ring rotates by half a segment relative to previous
        rotation = idx * (np.pi / n_dashes)

        # Brightness: innermost rings brightest
        alpha = 0.72 * (1.0 - frac * 0.78) + 0.06
        lw    = 1.05 - frac * 0.62

        # Color: gold to bronze
        col = G5 if frac < 0.25 else (G4 if frac < 0.55 else G3)

        seg_angle = 2 * np.pi / n_dashes
        for d in range(n_dashes):
            start = rotation + d * seg_angle
            end   = start + seg_angle * dash_arc
            th    = np.linspace(start, end, 28)
            ax.plot(cx + R*np.cos(th), cy + R*np.sin(th),
                    color=col, linewidth=lw, alpha=alpha,
                    solid_capstyle='round')

    # === Center light ===
    for r, a, c in [(0.55, 0.06, G4), (0.32, 0.15, G5),
                    (0.16, 0.42, G6), (0.06, 1.00, 'white')]:
        circ(ax, cx, cy, r, facecolor=c, alpha=a, zorder=6)

    # === Outer boundary ===
    th = np.linspace(0, 2*np.pi, 600)
    ax.plot(cx + (R_max + 0.10)*np.cos(th), cy + (R_max + 0.10)*np.sin(th),
            color=G2, linewidth=0.50, alpha=0.18, zorder=5)

    # === Typography ===
    ax.text(5.0, 2.55, 'W I T H I N   Y O U',
            fontproperties=F_ARSENAL, fontsize=19, color=G5,
            ha='center', va='center')
    ax.plot([3.55, 6.45], [2.22, 2.22], color=G1, linewidth=0.52, alpha=0.50)
    ax.text(5.0, 1.85, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=9, color=G3,
            ha='center', va='center', alpha=0.60)

    save_fig(fig, 'within_you_logo_9_vortex.png')


# ═══════════════════════════════════════════════════════════════
#  LOGO 10 — THE LOTUS
#  3-ring 24-petal awakening bloom in rose gold on violet-black
#  Most coloristically distinct logo in the collection
# ═══════════════════════════════════════════════════════════════

def logo_10_lotus():
    BG = V0
    fig, ax = make_fig(BG)

    cx, cy = 5.0, 5.58

    # ── OUTER ring: 8 petals ──────────────────────────────────
    for i in range(8):
        angle = 2*np.pi * i / 8
        p = petal_path(cx, cy, angle, 2.32, 0.72)
        fc = V2 if i % 2 == 0 else '#521A38'
        ax.add_patch(mpatches.PathPatch(p, facecolor=fc, edgecolor='none',
                                        alpha=0.55, zorder=2))
        ax.add_patch(mpatches.PathPatch(p, fill=False, edgecolor=RG3,
                                        linewidth=0.48, alpha=0.45, zorder=3))

    # ── MID ring: 8 petals offset 22.5 deg ──────────────────
    for i in range(8):
        angle = 2*np.pi * i / 8 + np.pi / 8
        p = petal_path(cx, cy, angle, 1.60, 0.54)
        fc = RG3 if i % 2 == 0 else V2
        ax.add_patch(mpatches.PathPatch(p, facecolor=fc, edgecolor='none',
                                        alpha=0.68, zorder=4))
        ax.add_patch(mpatches.PathPatch(p, fill=False, edgecolor=RG4,
                                        linewidth=0.50, alpha=0.55, zorder=5))

    # ── INNER ring: 8 petals ─────────────────────────────────
    for i in range(8):
        angle = 2*np.pi * i / 8
        p = petal_path(cx, cy, angle, 0.90, 0.30)
        ax.add_patch(mpatches.PathPatch(p, facecolor=RG4, edgecolor='none',
                                        alpha=0.80, zorder=6))
        ax.add_patch(mpatches.PathPatch(p, fill=False, edgecolor=RG5,
                                        linewidth=0.45, alpha=0.60, zorder=7))

    # ── Outer containment circle ─────────────────────────────
    th = np.linspace(0, 2*np.pi, 600)
    ax.plot(cx + 2.52*np.cos(th), cy + 2.52*np.sin(th),
            color=V2, linewidth=0.55, alpha=0.28, zorder=8)
    ax.plot(cx + 2.64*np.cos(th), cy + 2.64*np.sin(th),
            color=V1, linewidth=0.35, alpha=0.16, zorder=8)

    # ── Central jewel ────────────────────────────────────────
    for r, a, c in [(0.44, 0.22, RG3), (0.28, 0.42, RG4),
                    (0.14, 0.72, RG5), (0.06, 1.00, 'white')]:
        circ(ax, cx, cy, r, facecolor=c, alpha=a, zorder=9)

    # ── Typography ───────────────────────────────────────────
    ax.text(5.0, 2.58, 'W I T H I N   Y O U',
            fontproperties=F_LORA_IT, fontsize=22, color=RG5,
            ha='center', va='center', alpha=0.90)
    ax.plot([3.68, 6.32], [2.24, 2.24], color=V1, linewidth=0.52, alpha=0.52)
    ax.text(5.0, 1.88, 'D  A  I  L  Y',
            fontproperties=F_WORK, fontsize=9, color=RG3,
            ha='center', va='center', alpha=0.65)

    save_fig(fig, 'within_you_logo_10_lotus.png')


# ─────────────────────────────────────────────
# EXECUTE
# ─────────────────────────────────────────────

print()
print("  WITHIN YOU DAILY -- Logo Collection Vol.2")
print("  ===========================================")
print()

logo_6_iris();    print("   6/10  The Iris     -- structured eye of inner vision")
logo_7_nova();    print("   7/10  The Nova     -- explosive canvas-filling burst")
logo_8_diamond(); print("   8/10  The Diamond  -- teal star-cut faceted gem")
logo_9_vortex();  print("   9/10  The Vortex   -- hypnotic rotating dash rings")
logo_10_lotus();  print("  10/10  The Lotus    -- rose gold 24-petal bloom")

print()
print("  All 5 logos saved to Desktop.")
print()
