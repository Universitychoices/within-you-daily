#!/usr/bin/env python3
"""
WITHIN YOU DAILY -- Premium Logo Refinements
4 improved versions of Ember (1) and Iris (6)
Optimised for social media account / profile icons
YouTube: 800x800 | Instagram: 1080x1080 | TikTok: 200x200 display
Key rule: bold, high-contrast core — icon must READ at 40px
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ─────────────────────────────────────────────────────────────
# PATHS & FONTS
# ─────────────────────────────────────────────────────────────

FONTS = (
    r"C:\Users\Acer\AppData\Roaming\Claude\local-agent-mode-sessions"
    r"\skills-plugin\93ddaecc-7407-4be1-ae40-ebe282b3d9f5"
    r"\dcb3680c-405d-4c27-9628-d8a399da84ef\skills\canvas-design\canvas-fonts"
)
OUT = r"D:\desktop\Desktop\WithInYou"

fp = lambda f: FontProperties(fname=os.path.join(FONTS, f))

F_ITALIANA  = fp('Italiana-Regular.ttf')
F_GLOOCK    = fp('Gloock-Regular.ttf')
F_JURA_L    = fp('Jura-Light.ttf')
F_JURA_M    = fp('Jura-Medium.ttf')
F_ARSENAL   = fp('ArsenalSC-Regular.ttf')
F_LORA_B    = fp('Lora-Bold.ttf')
F_LORA_IT   = fp('Lora-Italic.ttf')
F_POIRET    = fp('PoiretOne-Regular.ttf')
F_INSTR     = fp('InstrumentSans-Regular.ttf')
F_WORK      = fp('WorkSans-Regular.ttf')

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def canvas(bg):
    fig = plt.figure(figsize=(10, 10), facecolor=bg)
    ax  = fig.add_axes([0, 0, 1, 1], facecolor=bg)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_aspect('equal'); ax.axis('off')
    return fig, ax

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"  -> {name}")

def ring(ax, cx, cy, r, **kw):
    th = np.linspace(0, 2*np.pi, 800)
    ax.plot(cx + r*np.cos(th), cy + r*np.sin(th), **kw)

def disc(ax, cx, cy, r, **kw):
    ax.add_patch(mpatches.Circle((cx, cy), r, **kw))

def flame(cx, cy, w, h):
    """Smooth bezier flame/teardrop"""
    bx, by = cx, cy - h*.48
    tx, ty = cx, cy + h*.52
    v = [(bx,by),
         (bx-w*.68, by+h*.18), (bx-w*.50, by+h*.74), (tx,ty),
         (bx+w*.50, by+h*.74), (bx+w*.68, by+h*.18), (bx,by), (bx,by)]
    c = [Path.MOVETO,
         Path.CURVE4,Path.CURVE4,Path.CURVE4,
         Path.CURVE4,Path.CURVE4,Path.CURVE4,
         Path.CLOSEPOLY]
    return Path(v, c)


# ═══════════════════════════════════════════════════════════════
#
#  EMBER  v A  ──  SOVEREIGN
#  Refined classic. 8 flame layers. Massive cinematic glow.
#  Precision medallion frame with degree tick marks.
#  Dominates the canvas — designed to read at 40px.
#
# ═══════════════════════════════════════════════════════════════

def ember_sovereign():
    BG = '#050505'
    fig, ax = canvas(BG)

    cx, cy = 5.0, 5.30
    W, H   = 2.30, 4.05     # flame dimensions — much larger than original

    # ── Dramatic multi-layer ambient glow ──────────────────────
    # Each layer wider and cooler; gives genuine fire-lighting effect
    for r, a, col in [
        (4.55, 0.010, '#2E1000'),
        (3.90, 0.020, '#461800'),
        (3.20, 0.038, '#5C2400'),
        (2.55, 0.062, '#763000'),
        (1.90, 0.096, '#8E4008'),
        (1.38, 0.138, '#A45412'),
        (0.92, 0.185, '#B8681C'),
        (0.54, 0.235, '#C87A22'),
        (0.28, 0.300, '#D48A28'),
    ]:
        disc(ax, cx, cy, r, facecolor=col, alpha=a, zorder=0)

    # ── 8 nested flame layers — near-black to cream-white ──────
    for scale, col in [
        (1.000, '#160600'),
        (0.860, '#30140200'),   # will fix hex below
        (0.720, '#5E3004'),
        (0.580, '#906016'),
        (0.440, '#B88022'),
        (0.305, '#D49C30'),
        (0.175, '#ECC040'),
        (0.068, '#F8EEB0'),
    ]:
        # Ensure valid hex
        col = col[:7]
        p = flame(cx, cy + 0.06*scale, W*scale, H*scale)
        ax.add_patch(mpatches.PathPatch(p, facecolor=col, edgecolor='none',
                                        alpha=0.97, zorder=2))

    # ── Medallion outer frame ───────────────────────────────────
    R_med = 4.28
    ring(ax, cx, cy, R_med,       color='#7A5010', linewidth=1.10, alpha=0.45, zorder=4)
    ring(ax, cx, cy, R_med-0.12,  color='#503208', linewidth=0.38, alpha=0.24, zorder=4)
    ring(ax, cx, cy, R_med+0.12,  color='#3A2004', linewidth=0.28, alpha=0.14, zorder=4)

    # Degree tick marks — 3 sizes for visual rhythm
    for deg in range(0, 360, 5):
        rad = np.radians(deg)
        if   deg % 90 == 0: tl, tw, ta = 0.28, 0.80, 0.48   # cardinal
        elif deg % 30 == 0: tl, tw, ta = 0.18, 0.60, 0.34   # major
        elif deg % 15 == 0: tl, tw, ta = 0.11, 0.44, 0.24   # mid
        else:               tl, tw, ta = 0.06, 0.32, 0.16   # minor
        r0 = R_med - tl
        ax.plot([cx+r0*np.cos(rad), cx+R_med*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R_med*np.sin(rad)],
                color='#A07020', linewidth=tw, alpha=ta, zorder=4)

    # ── Inner glow ring just outside flame tip ─────────────────
    ring(ax, cx, cy+H*.52, 0.28, color='#F0D878', linewidth=0.5, alpha=0.30, zorder=3)

    # ── Typography ─────────────────────────────────────────────
    ax.text(5.0, 2.15, 'W I T H I N   Y O U',
            fontproperties=F_GLOOCK, fontsize=19,
            color='#D4A828', ha='center', va='center', alpha=0.92)
    ax.plot([3.82, 6.18], [1.82, 1.82],
            color='#3C2004', linewidth=0.60, alpha=0.60, zorder=4)
    ax.text(5.0, 1.42, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=8.5,
            color='#8A6010', ha='center', va='center', alpha=0.65)

    save(fig, 'EMBER_A_sovereign.png')


# ═══════════════════════════════════════════════════════════════
#
#  EMBER  v B  ──  CELESTIAL
#  Flame enclosed within three concentric orbital rings.
#  Each ring carries different weight + tick rhythm.
#  Cosmic / stoic feeling — the inner fire as the fixed star.
#
# ═══════════════════════════════════════════════════════════════

def ember_celestial():
    BG = '#050508'   # very slightly blue-black for cosmic feel
    fig, ax = canvas(BG)

    cx, cy = 5.0, 5.45
    W, H   = 1.90, 3.40     # flame slightly contained within rings

    # ── Ambient glow ───────────────────────────────────────────
    for r, a, col in [
        (2.80, 0.040, '#5C3008'),
        (2.10, 0.075, '#7A4410'),
        (1.50, 0.118, '#9A5818'),
        (1.00, 0.165, '#B06C20'),
        (0.58, 0.220, '#C07C26'),
        (0.28, 0.290, '#CC882A'),
    ]:
        disc(ax, cx, cy, r, facecolor=col, alpha=a, zorder=0)

    # ── 8 flame layers ─────────────────────────────────────────
    for scale, col in [
        (1.000, '#160500'),
        (0.850, '#3C1C02'),
        (0.700, '#6C3C08'),
        (0.555, '#9A5C16'),
        (0.415, '#BC7E22'),
        (0.280, '#D49C30'),
        (0.155, '#EAC03C'),
        (0.065, '#F6ECA8'),
    ]:
        p = flame(cx, cy + 0.06*scale, W*scale, H*scale)
        ax.add_patch(mpatches.PathPatch(p, facecolor=col, edgecolor='none',
                                        alpha=0.97, zorder=2))

    # ── THREE orbital rings ─────────────────────────────────────
    # Inner orbit — close, warm, brightest
    R1 = 2.25
    ring(ax, cx, cy, R1, color='#A07020', linewidth=0.90, alpha=0.52, zorder=5)
    for deg in range(0, 360, 30):
        rad = np.radians(deg)
        tl = 0.16 if deg % 90 == 0 else 0.09
        r0 = R1 - tl
        ax.plot([cx+r0*np.cos(rad), cx+R1*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R1*np.sin(rad)],
                color='#C09030', linewidth=0.55, alpha=0.38, zorder=5)
    # 4 small diamond nodes at cardinal points on inner orbit
    for deg in [0, 90, 180, 270]:
        rad = np.radians(deg)
        nx, ny = cx + R1*np.cos(rad), cy + R1*np.sin(rad)
        perp = rad + np.pi/2
        size = 0.10
        pts = [[nx + size*np.cos(rad),   ny + size*np.sin(rad)],
               [nx + size*np.cos(perp),  ny + size*np.sin(perp)],
               [nx - size*np.cos(rad),   ny - size*np.sin(rad)],
               [nx - size*np.cos(perp),  ny - size*np.sin(perp)]]
        ax.add_patch(mpatches.Polygon(pts, closed=True,
                                      facecolor='#D4B040', alpha=0.72, zorder=6))

    # Middle orbit — medium, standard weight
    R2 = 3.10
    ring(ax, cx, cy, R2, color='#7A5010', linewidth=0.65, alpha=0.38, zorder=5)
    for deg in range(0, 360, 15):
        rad = np.radians(deg)
        tl = 0.10 if deg % 45 == 0 else 0.05
        r0 = R2 - tl
        ax.plot([cx+r0*np.cos(rad), cx+R2*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R2*np.sin(rad)],
                color='#906020', linewidth=0.42, alpha=0.28, zorder=5)

    # Outer orbit — widest, most subtle, creates the seal boundary
    R3 = 3.82
    ring(ax, cx, cy, R3,      color='#4A2C08', linewidth=0.55, alpha=0.30, zorder=5)
    ring(ax, cx, cy, R3+0.10, color='#301800', linewidth=0.28, alpha=0.14, zorder=5)
    # Minute degree marks on outer ring
    for deg in range(0, 360, 6):
        rad = np.radians(deg)
        tl = 0.12 if deg % 30 == 0 else 0.05
        r0 = R3 - tl
        ax.plot([cx+r0*np.cos(rad), cx+R3*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R3*np.sin(rad)],
                color='#6A3C10', linewidth=0.35, alpha=0.22, zorder=5)

    # ── Typography ─────────────────────────────────────────────
    ax.text(5.0, 2.05, 'W I T H I N   Y O U',
            fontproperties=F_ITALIANA, fontsize=21,
            color='#D0A430', ha='center', va='center', alpha=0.90)
    ax.plot([3.78, 6.22], [1.72, 1.72],
            color='#3A2004', linewidth=0.55, alpha=0.55, zorder=5)
    ax.text(5.0, 1.32, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=8.5,
            color='#7A5510', ha='center', va='center', alpha=0.62)

    save(fig, 'EMBER_B_celestial.png')


# ═══════════════════════════════════════════════════════════════
#
#  IRIS  v A  ──  DEEP
#  Maximally detailed iris. 360 structured fibers + 18 crypts.
#  High-contrast: very dark base lets fibers GLOW individually.
#  Stronger limbus, brighter pupil corona, precise outer ring.
#
# ═══════════════════════════════════════════════════════════════

def iris_deep():
    BG = '#05070E'
    fig, ax = canvas(BG)
    np.random.seed(42)

    cx, cy  = 5.0, 5.28
    R_pup   = 0.52    # pupil radius
    R_in    = 0.65    # inner iris edge
    R_out   = 2.42    # outer iris (limbus)
    R_deco  = 2.72    # decorative ring

    # ── Ambient background glow (warm, subtle) ─────────────────
    for r, a, col in [(3.6,0.025,'#2A1600'),(2.7,0.045,'#3A2000'),
                      (1.9,0.072,'#4E2C06')]:
        disc(ax, cx, cy, r, facecolor=col, alpha=a, zorder=0)

    # ── Iris base fill — deliberately DARK so fibers stand out ─
    # Only light near the pupil (inner 30%)
    for i in range(80):
        frac = i / 79.0
        r    = R_in + (R_out - R_in) * frac
        # Very sparse fill — fibers will provide the color
        base_alpha = 0.018 + 0.025 * max(0, 0.35 - frac)
        col = '#C08018' if frac < 0.30 else ('#804010' if frac < 0.65 else '#3C1A04')
        disc(ax, cx, cy, r, facecolor=col, alpha=base_alpha, zorder=1)

    # ── 360 structured iris fibers (18 crypts × 20 fibers) ─────
    n_crypts = 18
    fibers_per = 20

    for c_idx in range(n_crypts):
        base_angle = 2*np.pi * c_idx / n_crypts

        # ── Crypt (major fiber — brighter, thicker) ─────────────
        ca = base_angle + 0.008 * (np.random.rand() - 0.5)
        r0 = R_in  + 0.04 * np.random.rand()
        r1 = R_out - 0.06 * np.random.rand()
        ax.plot([cx + r0*np.cos(ca), cx + r1*np.cos(ca)],
                [cy + r0*np.sin(ca), cy + r1*np.sin(ca)],
                color='#E8C848', linewidth=0.58, alpha=0.40, zorder=3)

        # ── Fine fibers within this sector ──────────────────────
        sector = 2*np.pi / n_crypts
        for f in range(fibers_per):
            frac_f = (f + 1) / (fibers_per + 1)
            fa  = base_angle + sector * frac_f

            # Vary start/end radii for organic feel
            rs  = R_in  + 0.06 * np.random.rand()
            re  = R_out - 0.08 * np.random.rand()

            # Fiber alpha: brighter near center, fading outward
            brightness = 0.14 + 0.22 * np.random.rand()
            lw  = 0.22 + 0.18 * np.random.rand()

            # Colour variety: mix of gold, amber, pale cream
            choice = np.random.rand()
            col = '#F0D060' if choice > 0.72 else ('#C49030' if choice > 0.38 else '#A06818')

            ax.plot([cx + rs*np.cos(fa), cx + re*np.cos(fa)],
                    [cy + rs*np.sin(fa), cy + re*np.sin(fa)],
                    color=col, linewidth=lw, alpha=brightness, zorder=2)

    # ── Iris collarets / band rings ─────────────────────────────
    for r_b, alpha_b in [(0.95,0.18),(1.28,0.14),(1.65,0.12),(2.05,0.10)]:
        ring(ax, cx, cy, r_b, color='#B07820', linewidth=0.30, alpha=alpha_b, zorder=3)

    # ── Limbus — thick dark boundary (defines the iris) ─────────
    disc(ax, cx, cy, R_out + 0.16, fill=False,
         edgecolor='#100400', linewidth=7.0, alpha=0.95, zorder=5)
    ring(ax, cx, cy, R_out,        color='#3A1800', linewidth=0.55, alpha=0.45, zorder=5)

    # ── Pupil ───────────────────────────────────────────────────
    # Strong dark pupil — the void at the center
    disc(ax, cx, cy, R_pup, facecolor='#020104', alpha=1.0, zorder=7)
    # Pupil corona — bright inner iris glow ring
    for r_g, a_g, c_g in [(0.80,0.25,'#E0C040'),(0.92,0.16,'#C89030'),
                           (1.06,0.09,'#A07020'),(1.22,0.05,'#7A5010')]:
        disc(ax, cx, cy, r_g, facecolor=c_g, alpha=a_g, zorder=6)

    # ── Decorative outer precision ring ─────────────────────────
    ring(ax, cx, cy, R_deco,        color='#6A4810', linewidth=0.75, alpha=0.35, zorder=5)
    ring(ax, cx, cy, R_deco + 0.14, color='#3E2806', linewidth=0.35, alpha=0.18, zorder=5)
    # Fine tick marks (every 4 degrees)
    for deg in range(0, 360, 4):
        rad = np.radians(deg)
        tl  = 0.16 if deg % 40 == 0 else (0.10 if deg % 20 == 0 else 0.05)
        tw  = 0.55 if deg % 40 == 0 else 0.35
        ta  = 0.30 if deg % 40 == 0 else 0.18
        r0  = R_deco - tl
        ax.plot([cx+r0*np.cos(rad), cx+R_deco*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R_deco*np.sin(rad)],
                color='#A07020', linewidth=tw, alpha=ta, zorder=5)

    # ── Specular highlights ─────────────────────────────────────
    # Primary catch light
    ax.plot(cx+0.22, cy+0.22, 'o', color='white',  markersize=6.0, alpha=0.75, zorder=10)
    # Secondary ghost light
    ax.plot(cx-0.16, cy+0.30, 'o', color='#F8F0C0', markersize=2.5, alpha=0.38, zorder=10)

    # ── Typography ─────────────────────────────────────────────
    ax.text(5.0, 2.02, 'W I T H I N   Y O U',
            fontproperties=F_ARSENAL, fontsize=18,
            color='#CCA030', ha='center', va='center', alpha=0.90)
    ax.plot([3.85, 6.15], [1.70, 1.70],
            color='#2E1604', linewidth=0.52, alpha=0.55, zorder=5)
    ax.text(5.0, 1.32, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=8.5,
            color='#7A5C12', ha='center', va='center', alpha=0.62)

    save(fig, 'IRIS_A_deep.png')


# ═══════════════════════════════════════════════════════════════
#
#  IRIS  v B  ──  INFERNO
#  Fire-spectrum iris. Amber → orange → red-black ground.
#  Completely different colour temperature from v A.
#  Intense, passionate — fire looking back at you.
#
# ═══════════════════════════════════════════════════════════════

def iris_inferno():
    BG = '#070300'    # near-black with warm brown undertone
    fig, ax = canvas(BG)
    np.random.seed(99)

    cx, cy  = 5.0, 5.28
    R_pup   = 0.50
    R_in    = 0.62
    R_out   = 2.42
    R_deco  = 2.72

    # Fire colour palette
    F_OUTER  = '#4A0E00'   # deep red-black outer iris
    F_MID    = '#C04000'   # mid amber-red
    F_INNER  = '#F08010'   # bright amber near pupil
    F_BRIGHT = '#FFD030'   # hot yellow-amber
    F_CORE   = '#FFF8B0'   # near-white core

    # ── Warm ambient background fire glow ──────────────────────
    for r, a, col in [
        (4.00, 0.020, '#300A00'),
        (3.20, 0.038, '#4A1000'),
        (2.40, 0.065, '#681600'),
        (1.70, 0.100, '#842000'),
        (1.10, 0.145, '#9A2C00'),
        (0.60, 0.200, '#B03600'),
        (0.30, 0.270, '#C04000'),
    ]:
        disc(ax, cx, cy, r, facecolor=col, alpha=a, zorder=0)

    # ── Iris base fill — fire gradient ─────────────────────────
    for i in range(80):
        frac = i / 79.0
        r    = R_in + (R_out - R_in) * frac
        if frac < 0.25:
            col = F_INNER;   base_a = 0.03 + 0.04*(0.25-frac)
        elif frac < 0.55:
            col = F_MID;     base_a = 0.016
        else:
            col = F_OUTER;   base_a = 0.012
        disc(ax, cx, cy, r, facecolor=col, alpha=base_a, zorder=1)

    # ── Fire iris fibers ────────────────────────────────────────
    FIRE_COLS = [
        '#FFD840', '#F0A820', '#E07010',
        '#C84800', '#A02E00', '#7A1800',
    ]
    n_crypts = 18
    fibers_per = 20

    for c_idx in range(n_crypts):
        base_angle = 2*np.pi * c_idx / n_crypts

        # Crypt
        ca = base_angle + 0.008*(np.random.rand()-0.5)
        r0 = R_in  + 0.04*np.random.rand()
        r1 = R_out - 0.06*np.random.rand()
        ax.plot([cx+r0*np.cos(ca), cx+r1*np.cos(ca)],
                [cy+r0*np.sin(ca), cy+r1*np.sin(ca)],
                color='#FFD840', linewidth=0.60, alpha=0.42, zorder=3)

        sector = 2*np.pi / n_crypts
        for f in range(fibers_per):
            frac_f = (f+1)/(fibers_per+1)
            fa  = base_angle + sector*frac_f
            rs  = R_in  + 0.06*np.random.rand()
            re  = R_out - 0.08*np.random.rand()

            # Fibers brighter near center (lower frac_f start radius)
            radial_pos = (rs - R_in) / (R_out - R_in)
            brightness = 0.16 + 0.26*np.random.rand()
            lw   = 0.22 + 0.18*np.random.rand()
            col  = FIRE_COLS[int(radial_pos * (len(FIRE_COLS)-1) + np.random.rand()*.5)]
            ax.plot([cx+rs*np.cos(fa), cx+re*np.cos(fa)],
                    [cy+rs*np.sin(fa), cy+re*np.sin(fa)],
                    color=col, linewidth=lw, alpha=brightness, zorder=2)

    # ── Band rings ──────────────────────────────────────────────
    for r_b, col_b, a_b in [
        (0.92, '#F08020', 0.20), (1.26, '#C05010', 0.16),
        (1.62, '#904010', 0.13), (2.02, '#603010', 0.10),
    ]:
        ring(ax, cx, cy, r_b, color=col_b, linewidth=0.28, alpha=a_b, zorder=3)

    # ── Limbus ──────────────────────────────────────────────────
    disc(ax, cx, cy, R_out+0.16, fill=False,
         edgecolor='#0D0200', linewidth=7.5, alpha=0.96, zorder=5)
    ring(ax, cx, cy, R_out, color='#3A0800', linewidth=0.52, alpha=0.45, zorder=5)

    # ── Pupil ───────────────────────────────────────────────────
    disc(ax, cx, cy, R_pup, facecolor='#030100', alpha=1.0, zorder=7)
    for r_g, a_g, c_g in [
        (0.78, 0.28, F_INNER), (0.90, 0.18, F_MID),
        (1.04, 0.10, F_OUTER), (1.20, 0.05, '#601000'),
    ]:
        disc(ax, cx, cy, r_g, facecolor=c_g, alpha=a_g, zorder=6)

    # ── Outer precision ring ────────────────────────────────────
    ring(ax, cx, cy, R_deco,       color='#602000', linewidth=0.75, alpha=0.35, zorder=5)
    ring(ax, cx, cy, R_deco+0.14,  color='#3A1000', linewidth=0.32, alpha=0.18, zorder=5)
    for deg in range(0, 360, 4):
        rad = np.radians(deg)
        tl  = 0.16 if deg % 40 == 0 else (0.10 if deg % 20 == 0 else 0.05)
        tw  = 0.55 if deg % 40 == 0 else 0.35
        ta  = 0.28 if deg % 40 == 0 else 0.16
        r0  = R_deco - tl
        ax.plot([cx+r0*np.cos(rad), cx+R_deco*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R_deco*np.sin(rad)],
                color='#C04800', linewidth=tw, alpha=ta, zorder=5)

    # ── Specular ────────────────────────────────────────────────
    ax.plot(cx+0.22, cy+0.22, 'o', color='white',   markersize=6.5, alpha=0.78, zorder=10)
    ax.plot(cx-0.15, cy+0.30, 'o', color='#FFF8C0', markersize=2.8, alpha=0.40, zorder=10)

    # ── Typography ─────────────────────────────────────────────
    ax.text(5.0, 2.02, 'W I T H I N   Y O U',
            fontproperties=F_LORA_B, fontsize=19,
            color='#D06020', ha='center', va='center', alpha=0.92)
    ax.plot([3.85, 6.15], [1.70, 1.70],
            color='#3A0E00', linewidth=0.52, alpha=0.55, zorder=5)
    ax.text(5.0, 1.32, 'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=8.5,
            color='#8A3010', ha='center', va='center', alpha=0.62)

    save(fig, 'IRIS_B_inferno.png')


# ─────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────

print()
print("  WITHIN YOU -- Premium Profile Icon Refinements")
print("  ================================================")
print()
ember_sovereign(); print("  1A  Ember Sovereign  -- medallion frame, 8 layers, cinematic glow")
ember_celestial(); print("  1B  Ember Celestial  -- flame inside 3 orbital rings")
iris_deep();       print("  6A  Iris Deep        -- 360 fibers, max contrast, bright corona")
iris_inferno();    print("  6B  Iris Inferno     -- fire spectrum, amber-red, intense")
print()
print("  All saved to WithInYou folder.")
print()
