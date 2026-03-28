# VIDEO #02 — Production Plan
**Title:** "You're not broken. You're being farmed."
**Theme:** Why laziness isn't your fault — and the one-sentence fix
**Format:** 60s vertical (1080×1920) — TikTok / YouTube Shorts / Reels
**Source:** Jay Shetty — "If you're ambitious but lazy, please watch this…"
**URL:** https://www.youtube.com/watch?v=rNmOfqWGkjs

---

## Narrative Arc

```
HOOK (0–11s)     →  Personal confession. Viewer thinks "that's me."
DIAGNOSIS (11–27s)  →  Names the real cause: dopamine burnout, not character flaw
CLIMAX (27–50s)  →  Spoken-word poem. Full emotional release. THE shareable moment.
CLOSE (50–60s)   →  One sentence they'll replay 3 times.
```

---

## Segment Schedule

| Seg | Source File      | Cut Start | Cut End | Duration | Role          |
|-----|-----------------|-----------|---------|----------|---------------|
| 1   | source_jay.mp4  | 00:25     | 00:36   | 11s      | Hook / Pain   |
| 2   | source_jay.mp4  | 07:52     | 08:08   | 16s      | Diagnosis     |
| 3   | source_jay.mp4  | 17:46     | 18:09   | 23s      | Climax/Reframe|
| 4   | source_jay.mp4  | 19:17     | 19:27   | 10s      | Close / Fix   |

**Total: 60 seconds**

---

## Caption Overlays

| Time In | Time Out | Text                                     | Size |
|---------|----------|------------------------------------------|------|
| 0.5     | 5.0      | "I'd wake up tired,\nscroll for hours…"  | 72   |
| 5.5     | 10.5     | "I felt like I was wasting\nmy potential every single day." | 66 |
| 11.5    | 18.0     | "Laziness isn't lack of motivation.\nIt's dopamine burnout." | 68 |
| 18.5    | 26.5     | "Scrolling, snacking, streaming…\nreal work feels impossible." | 66 |
| 27.5    | 31.0     | "You're not lazy."                        | 88   |
| 31.5    | 35.0     | "You're not unmotivated."                 | 80   |
| 35.5    | 39.5     | "You're not broken."                      | 88   |
| 40.0    | 44.5     | "You're not failing to focus."            | 76   |
| 45.0    | 50.0     | "You're not the problem.\nYou're the product." | 76 |
| 51.0    | 57.0     | "The brain resists\nstarting — not continuing." | 76 |
| 57.5    | 60.0     | "Listen to that again."                   | 72   |

---

## Caption Style (matching Video #01)
- Font: Arial-Bold
- Color: white, stroke black width 3
- Position: 54% from top
- Method: caption (auto word-wrap)

---

## Music Direction
**Mood:** Starts melancholic / introspective → builds to quiet resolve by the end.
**Do NOT use uplifting/triumphant — the video ends on a revelation, not a celebration.**

**Recommended Bensound tracks to check:**
1. "Memories" — soft piano, emotional, perfect for the hook section
2. "Tenderness" — melancholic strings, builds gently
3. "Hope" — understated, contemplative

**How to find the MP3 URL:**
1. Go to bensound.com/free-music-for-videos
2. Click the track, hit Play
3. DevTools → Network → filter by cdn2.bensound → copy URL
4. Download with requests (same method as Video #01)

**Attribution for description:**
```
Music: "[Track Name]" by [Artist] — bensound.com
Original speech: Jay Shetty — https://youtu.be/rNmOfqWGkjs
Footage: Pexels.com (royalty-free)
```

---

## How to Download the Source Video

### Step 1 — Fix yt-dlp PATH issue (GitHubDesktop conflict)
The `[WinError 649]` is caused by a broken GitHubDesktop mount point in PATH.
Fix: strip PATH of GitHubDesktop before running yt-dlp:

```python
import subprocess, os

env = os.environ.copy()
env["PATH"] = ";".join(
    p for p in env["PATH"].split(";")
    if "GitHubDesktop" not in p
)

subprocess.run([
    "python", "-m", "yt_dlp",
    "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]",
    "--merge-output-format", "mp4",
    "-o", r"D:\desktop\Desktop\WithInYou\VideoProject_02\source_jay.mp4",
    "https://www.youtube.com/watch?v=rNmOfqWGkjs"
], env=env)
```

### Step 2 — Run assemble_video.py
```
python assemble_video.py
```

---

## Viral Potential Notes

**Why this cut works:**
- Seg 1 (hook): Opens with self-confession, not advice. Viewer feels understood before being taught.
- Seg 2 (diagnosis): Reframes laziness as neuroscience — removes shame. Highly saveable.
- Seg 3 (climax): The "You're not X, you're Y" poem has natural spoken-word rhythm. Viewers watch it 2-3 times.
- Seg 4 (close): "Listen to that again" is a built-in loop trigger. Ideal for Shorts replay metric.

**Expected strong moments for comments:**
- "You're the product" — always generates debate
- "Dopamine burnout" — people will tag friends
- "Listen to that again" — people will quote this in comments

---

## Pre-Post Checklist
- [ ] source_jay.mp4 downloaded (full video)
- [ ] assemble_video.py run successfully
- [ ] Music fades in/out smoothly (fade-in 2s, fade-out 3s)
- [ ] All captions readable, no overlap
- [ ] Logo watermark bottom-right
- [ ] Total duration exactly 60s (±1s)
- [ ] Attribution text ready for description
- [ ] Credit Jay Shetty in description + link to original

---

## Description Template
```
You don't have a discipline problem. You have a dopamine problem.

Jay Shetty breaks down exactly why ambition isn't enough — and the one insight that changes everything.

Full video: https://youtu.be/rNmOfqWGkjs

Music: "[Track Name]" by [Artist] — bensound.com

#motivation #mindset #productivity #jayshetty #shorts
```
