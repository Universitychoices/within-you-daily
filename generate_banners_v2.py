#!/usr/bin/env python3
"""
WITHIN YOU DAILY — YouTube Banners v2
Banner A: Fixed — eye centred properly, fully visible, no crop
Banner B: Creative "Duality" — two fire eyes framing the channel name
Both: 2560 x 1440 px @ 100 DPI, safe zone x:507–2053
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

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
F_ARSENAL = fp('ArsenalSC-Regular.ttf')
F_ITALIANA= fp('Italiana-Regular.ttf')
F_INSTR   = fp('InstrumentSans-Regular.ttf')
F_POIRET  = fp('PoiretOne-Regular.ttf')

BG       = '#070300'
FIRE     = ['#FFD840','#F0A820','#E07010','#C84800','#A02E00','#7A1800']
F_OUTER  = '#4A0E00'
F_MID    = '#C04000'
F_INNER  = '#F08010'


# ─────────────────────────────────────────────────────────────
# SHARED HELPERS
# ─────────────────────────────────────────────────────────────

def make_canvas():
    fig = plt.figure(figsize=(25.6, 14.4), dpi=100, facecolor=BG)
    ax  = fig.add_axes([0, 0, 1, 1], facecolor=BG)
    ax.set_xlim(0, 2560); ax.set_ylim(0, 1440)
    ax.axis('off')
    return fig, ax

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"  Saved: {name}")

def draw_iris(ax, cx, cy, R_out, seed=99, lw_scale=1.0):
    """Draw the full Iris B Inferno at given centre & radius."""
    np.random.seed(seed)

    R_pup  = int(R_out * 0.207)   # keep logo proportions
    R_in   = int(R_out * 0.257)
    R_deco = int(R_out * 1.128)
    th     = np.linspace(0, 2*np.pi, 800)

    # ── Background fire glow ──────────────────────────────────
    for r_f, a_f, c_f in [
        (R_out*2.50, 0.012, '#1E0500'),
        (R_out*1.88, 0.022, '#2E0900'),
        (R_out*1.39, 0.038, '#420E00'),
        (R_out*1.00, 0.060, '#5C1600'),
        (R_out*0.68, 0.092, '#782000'),
        (R_out*0.41, 0.135, '#952A00'),
        (R_out*0.21, 0.185, '#AE3400'),
        (R_out*0.10, 0.250, '#C03E00'),
    ]:
        ax.add_patch(mpatches.Circle((cx, cy), r_f, facecolor=c_f, alpha=a_f, zorder=0))

    # ── Sparse base fill ─────────────────────────────────────
    for i in range(80):
        frac = i / 79.0
        r    = R_in + (R_out - R_in) * frac
        if   frac < 0.25: col, ba = F_INNER, 0.030 + 0.038*(0.25-frac)
        elif frac < 0.55: col, ba = F_MID,   0.015
        else:             col, ba = F_OUTER,  0.011
        ax.add_patch(mpatches.Circle((cx, cy), r, facecolor=col, alpha=ba, zorder=1))

    # ── Iris fibers — 18 crypts × 20 fine ────────────────────
    n_c = 18; n_f = 20; sec = 2*np.pi/n_c
    for c in range(n_c):
        base = 2*np.pi*c/n_c
        ca   = base + 0.008*(np.random.rand()-0.5)
        rs0  = R_in  + int(0.016*R_out*np.random.rand())
        rs1  = R_out - int(0.025*R_out*np.random.rand())
        ax.plot([cx+rs0*np.cos(ca), cx+rs1*np.cos(ca)],
                [cy+rs0*np.sin(ca), cy+rs1*np.sin(ca)],
                color='#FFD840', linewidth=1.6*lw_scale, alpha=0.42, zorder=3)
        for f in range(n_f):
            fa = base + sec*(f+1)/(n_f+1)
            r0 = R_in  + int(0.025*R_out*np.random.rand())
            r1 = R_out - int(0.034*R_out*np.random.rand())
            a  = 0.14 + 0.28*np.random.rand()
            lw = (0.75 + 0.65*np.random.rand()) * lw_scale
            ci = min(int(np.random.rand()*3.2), 5)
            ax.plot([cx+r0*np.cos(fa), cx+r1*np.cos(fa)],
                    [cy+r0*np.sin(fa), cy+r1*np.sin(fa)],
                    color=FIRE[ci], linewidth=lw, alpha=a, zorder=2)

    # ── Band rings ────────────────────────────────────────────
    for rb, cb, ab in [
        (R_in+int(R_out*.098), '#F08020', 0.20),
        (R_in+int(R_out*.259), '#C05010', 0.16),
        (R_in+int(R_out*.480), '#904010', 0.13),
        (R_in+int(R_out*.706), '#603010', 0.10),
    ]:
        ax.plot(cx+rb*np.cos(th), cy+rb*np.sin(th),
                color=cb, linewidth=0.85*lw_scale, alpha=ab, zorder=3)

    # ── Limbus ────────────────────────────────────────────────
    ax.add_patch(mpatches.Circle((cx,cy), R_out+int(R_out*.068), fill=False,
                                  edgecolor='#0D0200',
                                  linewidth=max(4, int(R_out*.039))*lw_scale,
                                  alpha=0.97, zorder=5))
    ax.plot(cx+R_out*np.cos(th), cy+R_out*np.sin(th),
            color='#3A0800', linewidth=1.6*lw_scale, alpha=0.45, zorder=5)

    # ── Pupil + corona ────────────────────────────────────────
    ax.add_patch(mpatches.Circle((cx,cy), R_pup, facecolor='#030100', alpha=1.0, zorder=7))
    for rg, ag, cg in [
        (R_in+int(R_out*.059), 0.28, F_INNER),
        (R_in+int(R_out*.116), 0.18, F_MID),
        (R_in+int(R_out*.179), 0.10, F_OUTER),
        (R_in+int(R_out*.245), 0.05, '#601000'),
    ]:
        ax.add_patch(mpatches.Circle((cx,cy), rg, facecolor=cg, alpha=ag, zorder=6))

    # ── Outer precision ring + ticks ──────────────────────────
    ax.plot(cx+R_deco*np.cos(th), cy+R_deco*np.sin(th),
            color='#602000', linewidth=2.2*lw_scale, alpha=0.35, zorder=5)
    for deg in range(0, 360, 4):
        rad = np.radians(deg)
        if   deg%40==0: tl=int(R_out*.078); tw=1.6; ta=0.28
        elif deg%20==0: tl=int(R_out*.050); tw=1.1; ta=0.19
        else:           tl=int(R_out*.023); tw=0.8; ta=0.13
        r0 = R_deco - tl
        ax.plot([cx+r0*np.cos(rad), cx+R_deco*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R_deco*np.sin(rad)],
                color='#C04800', linewidth=tw*lw_scale, alpha=ta, zorder=5)

    # ── Specular highlights ───────────────────────────────────
    hl = int(R_out * 0.089)
    ax.plot(cx+hl, cy+hl, 'o', color='white',    markersize=max(6,int(R_out*.027)), alpha=0.75, zorder=10)
    ax.plot(cx-int(hl*.65), cy+int(hl*1.35), 'o', color='#FFF8C0',
            markersize=max(3,int(R_out*.012)), alpha=0.38, zorder=10)


# ═══════════════════════════════════════════════════════════════
#
#  BANNER A — FIXED
#  Eye fully visible, centred vertically, left-side composition.
#  Channel name right of eye. Clean classic layout.
#
# ═══════════════════════════════════════════════════════════════

def banner_A():
    fig, ax = make_canvas()

    # Eye — fully visible, left side of canvas
    cx, cy  = 760, 720
    R_out   = 440   # left edge: 760-440=320  right edge: 760+440=1200

    draw_iris(ax, cx, cy, R_out)

    # ── Full-width subtle centre line ─────────────────────────
    ax.plot([0, 2560], [720, 720], color='#1E0500', linewidth=0.9, alpha=0.20, zorder=4)

    # ── Vertical separator ────────────────────────────────────
    # Safe zone: x 507–2053. Separator sits just right of eye.
    ax.plot([1260, 1260], [300, 1140], color='#3A0E00', linewidth=1.0, alpha=0.30, zorder=4)

    # ── "WITHIN YOU" — right-aligned within safe zone (≤2030) ──
    ax.text(2030, 840,
            'WITHIN YOU',
            fontproperties=F_LORA_B, fontsize=108,
            color='#C85818', ha='right', va='center', alpha=0.96, zorder=8)

    # ── Horizontal rule ───────────────────────────────────────
    ax.plot([1280, 2030], [705, 705],
            color='#3A0E00', linewidth=1.8, alpha=0.48, zorder=4)

    # ── "DAILY" ───────────────────────────────────────────────
    ax.text(2030, 575,
            'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=52,
            color='#8A3010', ha='right', va='center', alpha=0.72, zorder=8)

    # ── Tagline ───────────────────────────────────────────────
    ax.text(2030, 438,
            'IGNITE  THE  FIRE  WITHIN',
            fontproperties=F_ARSENAL, fontsize=26,
            color='#5A1E08', ha='right', va='center', alpha=0.55, zorder=8)

    ax.plot([1280, 2030], [402, 402],
            color='#240800', linewidth=0.8, alpha=0.32, zorder=4)

    save(fig, 'BANNER_A_fixed.png')


# ═══════════════════════════════════════════════════════════════
#
#  BANNER B — DUALITY
#  Two fire eyes flank the channel name — one on each side.
#  Symmetrical. The name lives between two gazes.
#  The inner fire watches from both sides.
#
# ═══════════════════════════════════════════════════════════════

def banner_B():
    fig, ax = make_canvas()

    # ── Left eye — smaller, slightly bleeds off canvas ────────
    L_cx, L_cy, L_R = 248, 720, 310
    draw_iris(ax, L_cx, L_cy, L_R, seed=42, lw_scale=0.8)

    # ── Right eye — mirror, same scale ────────────────────────
    R_cx, R_cy, R_R = 2312, 720, 310
    draw_iris(ax, R_cx, R_cy, R_R, seed=7,  lw_scale=0.8)

    # ── Thin horizontal line connecting the two glows ─────────
    ax.plot([L_cx+L_R+60, R_cx-R_R-60], [720, 720],
            color='#2A0800', linewidth=0.9, alpha=0.28, zorder=4)

    # ── Vertical accent bars flanking text ───────────────────
    for xv in [660, 1900]:
        ax.plot([xv, xv], [430, 1010],
                color='#3A0E00', linewidth=0.8, alpha=0.30, zorder=4)

    # ── CHANNEL NAME — large, centred between the eyes ────────
    ax.text(1280, 840,
            'WITHIN  YOU',
            fontproperties=F_LORA_B, fontsize=118,
            color='#C85818', ha='center', va='center', alpha=0.96, zorder=8)

    # ── Horizontal rule ───────────────────────────────────────
    ax.plot([680, 1880], [700, 700],
            color='#3A0E00', linewidth=1.6, alpha=0.45, zorder=4)

    # ── "DAILY" centred ───────────────────────────────────────
    ax.text(1280, 575,
            'D  A  I  L  Y',
            fontproperties=F_JURA_L, fontsize=50,
            color='#8A3010', ha='center', va='center', alpha=0.72, zorder=8)

    # ── Tagline centred ───────────────────────────────────────
    ax.text(1280, 440,
            'I G N I T E   T H E   F I R E   W I T H I N',
            fontproperties=F_ARSENAL, fontsize=24,
            color='#521808', ha='center', va='center', alpha=0.52, zorder=8)

    ax.plot([680, 1880], [405, 405],
            color='#1E0600', linewidth=0.7, alpha=0.28, zorder=4)

    # ── Small decorative dots at cardinal points of each eye ──
    for (ecx, ecy, er) in [(L_cx, L_cy, L_R), (R_cx, R_cy, R_R)]:
        for deg in [0, 90, 180, 270]:
            rad = np.radians(deg)
            nx = ecx + (er + 38)*np.cos(rad)
            ny = ecy + (er + 38)*np.sin(rad)
            if 0 < nx < 2560 and 0 < ny < 1440:
                perp = rad + np.pi/2
                pts = [[nx+12*np.cos(rad),  ny+12*np.sin(rad)],
                       [nx+6 *np.cos(perp), ny+6 *np.sin(perp)],
                       [nx-12*np.cos(rad),  ny-12*np.sin(rad)],
                       [nx-6 *np.cos(perp), ny-6 *np.sin(perp)]]
                ax.add_patch(mpatches.Polygon(pts, closed=True,
                                              facecolor='#C04800', alpha=0.55, zorder=6))

    save(fig, 'BANNER_B_duality.png')


# ─────────────────────────────────────────────────────────────
print()
print("  WITHIN YOU -- YouTube Banners v2")
print("  ==================================")
print()
banner_A(); print("  A  Fixed    -- eye centred left, text right, clean layout")
banner_B(); print("  B  Duality  -- two fire eyes flank the name symmetrically")
print()
print("  Both saved to WithInYou folder.")
print()
