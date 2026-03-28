#!/usr/bin/env python3
"""
WITHIN YOU DAILY — Video #01
Theme : "You Are Doing Alright — It's OK To Feel Down"
Output: 1080 x 1920  (9:16 vertical — YouTube Shorts / TikTok / Reels)
Music : Long Night by Aventure (Bensound) — free with attribution
"""

import os, numpy as np
from moviepy import (
    VideoFileClip, AudioFileClip, CompositeVideoClip,
    ImageClip, concatenate_videoclips
)
from moviepy.video.VideoClip import TextClip
from moviepy.audio.fx import AudioFadeIn, AudioFadeOut

DIR  = r"D:\desktop\Desktop\WithInYou\VideoProject_01"
LOGO = r"D:\desktop\Desktop\WithInYou\IRIS_B_inferno.png"
OUT  = os.path.join(DIR, "within_you_video_01.mp4")

W, H, FPS = 1080, 1920, 30

# ── Actual clip durations (verified) ────────────────────────────────────────
# clip_01 8.8s | clip_02 16.8s | clip_03 16.9s | clip_04 9.2s
# clip_05 8.6s | clip_06 4.0s  | clip_07 2.8s  | clip_08 10.2s

SCHEDULE = [
    # (file, t_start, duration)  → total ~79s
    ("clip_01_hook.mp4",      0.0,  7.0),   #  0– 7  hook
    ("clip_02_empathy_a.mp4", 0.0, 10.0),   #  7–17  empathy: man in bed
    ("clip_03_empathy_b.mp4", 0.0,  9.0),   # 17–26  empathy: woman & coffee
    ("clip_04_reframe.mp4",   0.0,  9.2),   # 26–35  reframe: eyes closed
    ("clip_05_truth.mp4",     0.0,  8.6),   # 35–44  truth: arms open
    ("clip_02_empathy_a.mp4",10.0,  6.8),   # 44–51  (2nd pass) still empathy B-roll
    ("clip_06_uplift_a.mp4",  0.0,  4.0),   # 51–55  uplift: sunrise silhouette
    ("clip_07_uplift_b.mp4",  0.0,  2.8),   # 55–58  uplift: forest walk
    ("clip_06_uplift_a.mp4",  0.0,  4.0),   # 58–62  (loop sunrise)
    ("clip_03_empathy_b.mp4", 9.0,  7.0),   # 62–69  soft B-roll before close
    ("clip_08_close.mp4",     0.0, 10.2),   # 69–79  close: peaceful smile
]

# ── Captions (adjusted to ~79s total) ───────────────────────────────────────
CAPTIONS = [
    ( 0.8,  5.5, "Most people pretend\nthey're okay...\nwhen they're not.", 70),
    ( 7.5, 14.0, "Some days everything\nfeels heavy.",                       76),
    (15.0, 22.5, "You don't know why.\nYou just... do.",                     76),
    (27.0, 33.5, "Nothing is wrong\nwith you.",                              84),
    (35.5, 43.0, "Every person you admire\nhas days exactly like this.",     64),
    (45.0, 52.0, "You don't have to\nperform happiness.",                    76),
    (53.0, 58.0, "You're allowed to feel\nthe weight of things.",            66),
    (59.5, 66.5, "You've survived every\nhard day so far.",                  74),
    (67.5, 71.5, "Every. Single. One.",                                      92),
    (72.5, 78.0, "You are doing better\nthan you think.",                    80),
]


def fit_to_frame(clip):
    cw, ch = clip.size
    scale  = max(W / cw, H / ch)
    nw, nh = int(cw * scale), int(ch * scale)
    clip   = clip.resized((nw, nh))
    x1 = (nw - W) // 2
    y1 = (nh - H) // 2
    return clip.cropped(x1=x1, y1=y1, x2=x1+W, y2=y1+H)


def dark_grade(clip, f=0.70):
    """Multiply each pixel by f to darken (moody cinematic)."""
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
            text      = text,
            font_size = size,
            color     = "white",
            method    = "caption",
            size      = (W - 100, None),
            text_align = "center",
            duration   = duration,
        )


# ── Assemble clips ───────────────────────────────────────────────────────────
print("\nBuilding segments...")
segments = []
for fname, t0, dur in SCHEDULE:
    path = os.path.join(DIR, fname)
    c    = VideoFileClip(path, audio=False)
    t0   = min(t0, max(0.0, c.duration - 0.5))
    dur  = min(dur, c.duration - t0)
    c    = c.subclipped(t0, t0 + dur)
    c    = fit_to_frame(c)
    c    = dark_grade(c)
    segments.append(c)
    print(f"  {fname:35s}  {dur:.1f}s")

base   = concatenate_videoclips(segments, method="compose")
total  = base.duration
print(f"\n  Total duration: {total:.1f}s")

# ── Music ────────────────────────────────────────────────────────────────────
print("Adding music...")
music = (AudioFileClip(os.path.join(DIR, "music_long_night.mp3"))
         .subclipped(0, total)
         .with_effects([AudioFadeIn(2.5), AudioFadeOut(3.0)]))
base  = base.with_audio(music)

# ── Caption overlays ─────────────────────────────────────────────────────────
print("Adding captions...")
cap_clips = []
for (t_in, t_out, txt, fsz) in CAPTIONS:
    if t_in >= total:
        continue
    t_out = min(t_out, total)
    dur   = t_out - t_in
    tc    = make_text(txt, fsz, dur)
    # Vertical centre: slightly below mid-frame
    y_pos = int(H * 0.54) - tc.size[1] // 2
    tc    = tc.with_position(("center", y_pos)).with_start(t_in)
    cap_clips.append(tc)

# ── Logo watermark ───────────────────────────────────────────────────────────
overlays = cap_clips[:]
if os.path.exists(LOGO):
    logo = (ImageClip(LOGO)
            .resized(height=110)
            .with_opacity(0.50)
            .with_position((W - 130, H - 140))
            .with_duration(total))
    overlays.append(logo)

# ── Composite & export ───────────────────────────────────────────────────────
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

print(f"\n  DONE: within_you_video_01.mp4  ({total:.1f}s)")
print( "  Music credit: 'Long Night' by Aventure — bensound.com")
