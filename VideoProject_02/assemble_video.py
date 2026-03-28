#!/usr/bin/env python3
"""
WITHIN YOU DAILY — Video #02
Theme : "You're not broken. You're being farmed."
Source: Jay Shetty — "If you're ambitious but lazy, please watch this..."
Output: 1080 x 1920  (9:16 vertical — YouTube Shorts / TikTok / Reels)
Music : [Choose from Bensound — see VIDEO_02_PLAN.md]
"""

import os, numpy as np
from moviepy import (
    VideoFileClip, AudioFileClip, CompositeVideoClip,
    ImageClip, concatenate_videoclips
)
from moviepy.video.VideoClip import TextClip
from moviepy.audio.fx import AudioFadeIn, AudioFadeOut

DIR    = r"D:\desktop\Desktop\WithInYou\VideoProject_02"
SOURCE = os.path.join(DIR, "source_jay.mp4")
MUSIC  = os.path.join(DIR, "music_video02.mp3")   # rename your Bensound file to this
LOGO   = r"D:\desktop\Desktop\WithInYou\IRIS_B_inferno.png"
OUT    = os.path.join(DIR, "within_you_video_02.mp4")

W, H, FPS = 1080, 1920, 30

# ── Segment Schedule ─────────────────────────────────────────────────────────
# Cut from source_jay.mp4 (full Jay Shetty video)
#
# Seg 1 [00:25-00:36]  11s  HOOK   — personal confession
# Seg 2 [07:52-08:08]  16s  DIAG   — laziness = dopamine burnout
# Seg 3 [17:46-18:09]  23s  CLIMAX — "You're not the problem, you're the product"
# Seg 4 [19:17-19:27]  10s  CLOSE  — "The brain resists starting, not continuing"
#
SCHEDULE = [
    # (t_start_sec, duration_sec, label)
    (  25.0, 11.0, "hook"),
    ( 472.0, 16.0, "diagnosis"),   # 07:52 = 472s
    (1066.0, 23.0, "climax"),      # 17:46 = 1066s
    (1157.0, 10.0, "close"),       # 19:17 = 1157s
]

# ── Captions ──────────────────────────────────────────────────────────────────
CAPTIONS = [
    #  t_in   t_out  text                                                  size
    (  0.5,   5.0,  "\"I'd wake up tired,\nscroll for hours…\"",           72),
    (  5.5,  10.5,  "…still wonder why nothing\nin my life was changing.", 66),
    ( 11.5,  18.0,  "Laziness isn't lack\nof motivation.",                 76),
    ( 18.5,  26.5,  "It's dopamine burnout\nfrom cheap rewards.",          72),
    ( 27.5,  31.0,  "You're not lazy.",                                    92),
    ( 31.5,  35.0,  "You're not unmotivated.",                             80),
    ( 35.5,  39.5,  "You're not broken.",                                  92),
    ( 40.0,  44.5,  "You're not failing to focus.",                        76),
    ( 45.0,  50.0,  "You're not the problem.\nYou're the product.",        76),
    ( 51.0,  57.0,  "The brain resists\nstarting — not continuing.",       74),
    ( 57.5,  60.0,  "Listen to that again.",                               76),
]


def fit_to_frame(clip):
    cw, ch = clip.size
    scale  = max(W / cw, H / ch)
    nw, nh = int(cw * scale), int(ch * scale)
    clip   = clip.resized((nw, nh))
    x1 = (nw - W) // 2
    y1 = (nh - H) // 2
    return clip.cropped(x1=x1, y1=y1, x2=x1+W, y2=y1+H)


def dark_grade(clip, f=0.72):
    """Cinematic darkening — slightly less dark than Video #01 (talking head)."""
    def grader(frame):
        return (frame * f).clip(0, 255).astype(np.uint8)
    return clip.image_transform(grader)


def make_text(text, size, duration):
    """White bold text with black stroke, centre-aligned."""
    try:
        return TextClip(
            text         = text,
            font_size    = size,
            color        = "white",
            font         = "Arial-Bold",
            stroke_color = "black",
            stroke_width = 3,
            method       = "caption",
            size         = (W - 100, None),
            text_align   = "center",
            duration     = duration,
        )
    except Exception:
        return TextClip(
            text       = text,
            font_size  = size,
            color      = "white",
            method     = "caption",
            size       = (W - 100, None),
            text_align = "center",
            duration   = duration,
        )


# ── Load & cut source segments ────────────────────────────────────────────────
print("\nLoading source video...")
if not os.path.exists(SOURCE):
    print("  ERROR: source_jay.mp4 not found.")
    print("  Run download_source.py first.")
    raise SystemExit(1)

print("Building segments...")
segments = []
src = VideoFileClip(SOURCE, audio=True)

for t0, dur, label in SCHEDULE:
    t0  = min(t0, max(0.0, src.duration - 0.5))
    dur = min(dur, src.duration - t0)
    c   = src.subclipped(t0, t0 + dur)
    c   = fit_to_frame(c)
    c   = dark_grade(c)
    segments.append(c)
    print(f"  [{label:12s}]  {t0:.0f}s -> {t0+dur:.0f}s  ({dur:.1f}s)")

src.close()

base  = concatenate_videoclips(segments, method="compose")
total = base.duration
print(f"\n  Total duration: {total:.1f}s")

# ── Music ─────────────────────────────────────────────────────────────────────
print("Adding music...")
if not os.path.exists(MUSIC):
    print("  WARNING: music_video02.mp3 not found — rendering without music.")
    print("  Download a Bensound track and rename it to music_video02.mp3")
else:
    music = (AudioFileClip(MUSIC)
             .subclipped(0, total)
             .with_effects([AudioFadeIn(2.0), AudioFadeOut(3.0)])
             .with_volume_scaled(0.35))   # Lower than Video #01 — speech needs to be heard
    # Mix speech audio + background music
    from moviepy import CompositeAudioClip
    mixed = CompositeAudioClip([base.audio, music])
    base  = base.with_audio(mixed)

# ── Caption overlays ──────────────────────────────────────────────────────────
print("Adding captions...")
cap_clips = []
for (t_in, t_out, txt, fsz) in CAPTIONS:
    if t_in >= total:
        continue
    t_out = min(t_out, total)
    dur   = t_out - t_in
    tc    = make_text(txt, fsz, dur)
    y_pos = int(H * 0.54) - tc.size[1] // 2
    tc    = tc.with_position(("center", y_pos)).with_start(t_in)
    cap_clips.append(tc)

# ── Logo watermark ────────────────────────────────────────────────────────────
overlays = cap_clips[:]
if os.path.exists(LOGO):
    logo = (ImageClip(LOGO)
            .resized(height=110)
            .with_opacity(0.50)
            .with_position((W - 130, H - 140))
            .with_duration(total))
    overlays.append(logo)

# ── Composite & export ────────────────────────────────────────────────────────
print("Compositing final video...")
final = CompositeVideoClip([base] + overlays, size=(W, H)).with_duration(total)

print(f"\nExporting -> {OUT}")
final.write_videofile(
    OUT,
    fps         = FPS,
    codec       = "libx264",
    audio_codec = "aac",
    bitrate     = "4000k",
    threads     = 4,
    preset      = "fast",
    logger      = "bar",
)

print(f"\n  DONE: within_you_video_02.mp4  ({total:.1f}s)")
print( "  Credit Jay Shetty in description + link to original!")
