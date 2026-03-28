#!/usr/bin/env python3
"""
WITHIN YOU DAILY - YouTube Video Watermark
150 x 150 px, transparent background PNG
YouTube spec: min 150x150, max 1MB, PNG recommended
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

OUT = r"D:\desktop\Desktop\WithInYou"

FIRE     = ['#FFD840','#F0A820','#E07010','#C84800','#A02E00','#7A1800']
F_OUTER  = '#4A0E00'
F_MID    = '#C04000'
F_INNER  = '#F08010'


def make_watermark():
    np.random.seed(99)

    # 150x150 at 150 DPI = 1 inch x 1 inch figure
    fig = plt.figure(figsize=(1.0, 1.0), dpi=150, facecolor='none')
    ax  = fig.add_axes([0, 0, 1, 1], facecolor='none')
    ax.set_xlim(0, 150); ax.set_ylim(0, 150)
    ax.axis('off')
    fig.patch.set_alpha(0.0)

    cx, cy  = 75, 75
    R_out   = 58
    R_in    = int(R_out * 0.257)
    R_pup   = int(R_out * 0.207)
    R_deco  = int(R_out * 1.128)
    th      = np.linspace(0, 2*np.pi, 400)

    # ── Dark circular backdrop (semi-transparent) ──────────────
    ax.add_patch(mpatches.Circle((cx, cy), R_out + 10,
                                  facecolor='#070300', alpha=0.55, zorder=0))

    # ── Background glow ────────────────────────────────────────
    for r_f, a_f, c_f in [
        (R_out*2.50, 0.06, '#1E0500'),
        (R_out*1.60, 0.10, '#2E0900'),
        (R_out*1.10, 0.18, '#5C1600'),
        (R_out*0.70, 0.28, '#782000'),
    ]:
        ax.add_patch(mpatches.Circle((cx, cy), r_f, facecolor=c_f, alpha=a_f, zorder=0))

    # ── Iris base fill ─────────────────────────────────────────
    for i in range(60):
        frac = i / 59.0
        r    = R_in + (R_out - R_in) * frac
        if   frac < 0.25: col, ba = F_INNER, 0.040
        elif frac < 0.55: col, ba = F_MID,   0.020
        else:             col, ba = F_OUTER,  0.014
        ax.add_patch(mpatches.Circle((cx, cy), r, facecolor=col, alpha=ba, zorder=1))

    # ── Iris fibers — 18 crypts x 14 fine ─────────────────────
    n_c = 18; n_f = 14; sec = 2*np.pi/n_c
    for c in range(n_c):
        base = 2*np.pi*c/n_c
        ca   = base + 0.008*(np.random.rand()-0.5)
        rs0  = R_in  + int(0.016*R_out*np.random.rand())
        rs1  = R_out - int(0.025*R_out*np.random.rand())
        ax.plot([cx+rs0*np.cos(ca), cx+rs1*np.cos(ca)],
                [cy+rs0*np.sin(ca), cy+rs1*np.sin(ca)],
                color='#FFD840', linewidth=0.9, alpha=0.50, zorder=3)
        for f in range(n_f):
            fa = base + sec*(f+1)/(n_f+1)
            r0 = R_in  + int(0.025*R_out*np.random.rand())
            r1 = R_out - int(0.034*R_out*np.random.rand())
            a  = 0.18 + 0.28*np.random.rand()
            lw = 0.5 + 0.5*np.random.rand()
            ci = min(int(np.random.rand()*3.2), 5)
            ax.plot([cx+r0*np.cos(fa), cx+r1*np.cos(fa)],
                    [cy+r0*np.sin(fa), cy+r1*np.sin(fa)],
                    color=FIRE[ci], linewidth=lw, alpha=a, zorder=2)

    # ── Band rings ─────────────────────────────────────────────
    for rb, cb, ab in [
        (R_in+int(R_out*.098), '#F08020', 0.25),
        (R_in+int(R_out*.480), '#904010', 0.16),
        (R_in+int(R_out*.706), '#603010', 0.12),
    ]:
        ax.plot(cx+rb*np.cos(th), cy+rb*np.sin(th),
                color=cb, linewidth=0.6, alpha=ab, zorder=3)

    # ── Limbus ─────────────────────────────────────────────────
    ax.add_patch(mpatches.Circle((cx, cy), R_out+4, fill=False,
                                  edgecolor='#0D0200', linewidth=3.5, alpha=0.97, zorder=5))
    ax.plot(cx+R_out*np.cos(th), cy+R_out*np.sin(th),
            color='#3A0800', linewidth=0.9, alpha=0.50, zorder=5)

    # ── Pupil + corona ─────────────────────────────────────────
    ax.add_patch(mpatches.Circle((cx, cy), R_pup, facecolor='#030100', alpha=1.0, zorder=7))
    for rg, ag, cg in [
        (R_in+int(R_out*.059), 0.30, F_INNER),
        (R_in+int(R_out*.116), 0.20, F_MID),
        (R_in+int(R_out*.179), 0.10, F_OUTER),
    ]:
        ax.add_patch(mpatches.Circle((cx, cy), rg, facecolor=cg, alpha=ag, zorder=6))

    # ── Outer precision ring ───────────────────────────────────
    ax.plot(cx+R_deco*np.cos(th), cy+R_deco*np.sin(th),
            color='#602000', linewidth=1.2, alpha=0.40, zorder=5)
    for deg in range(0, 360, 8):
        rad = np.radians(deg)
        tl  = int(R_out*.060) if deg%40==0 else int(R_out*.030)
        tw  = 1.0 if deg%40==0 else 0.6
        ta  = 0.28 if deg%40==0 else 0.14
        r0  = R_deco - tl
        ax.plot([cx+r0*np.cos(rad), cx+R_deco*np.cos(rad)],
                [cy+r0*np.sin(rad), cy+R_deco*np.sin(rad)],
                color='#C04800', linewidth=tw, alpha=ta, zorder=5)

    # ── Specular highlight ─────────────────────────────────────
    hl = int(R_out * 0.10)
    ax.plot(cx+hl, cy+hl, 'o', color='white',   markersize=3.5, alpha=0.80, zorder=10)
    ax.plot(cx-int(hl*.6), cy+int(hl*1.4), 'o', color='#FFF8C0',
            markersize=1.8, alpha=0.42, zorder=10)

    # ── Save with transparency ─────────────────────────────────
    path = os.path.join(OUT, 'WATERMARK_within_you.png')
    fig.savefig(path, dpi=150, transparent=True, bbox_inches='tight',
                facecolor='none', edgecolor='none')
    plt.close(fig)
    print("  Saved: WATERMARK_within_you.png  (150 x 150 px, transparent PNG)")


print()
print("  WITHIN YOU -- Video Watermark")
print("  ================================")
print()
make_watermark()
print()
print("  Upload at: YouTube Studio > Customisation > Branding > Video watermark")
print("  Recommended: show during entire video")
print()
