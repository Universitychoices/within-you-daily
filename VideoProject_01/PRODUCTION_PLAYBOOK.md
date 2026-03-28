# WITHIN YOU DAILY — Video Production Playbook

## Folder Structure
```
WithInYou/
  VideoProject_01/          ← one folder per video
    clip_01_*.mp4           ← raw footage (Pexels, free)
    music_*.mp3             ← music (Bensound, free w/ attribution)
    assemble_video.py       ← assembly + render script
    within_you_video_01.mp4 ← FINAL OUTPUT
  IRIS_B_inferno.png        ← logo watermark (3000×3000)
  WATERMARK_within_you.png  ← YouTube watermark (150×150)
  BANNER_A_fixed.png        ← YouTube channel banner
```

---

## Video Specs (Platform-Optimised)
| Setting     | Value                        |
|-------------|------------------------------|
| Resolution  | 1080 × 1920 (9:16 vertical)  |
| FPS         | 30                           |
| Codec       | H.264 (libx264)              |
| Audio       | AAC                          |
| Bitrate     | 4000k                        |
| Duration    | 60–90 seconds                |

Works natively on: **TikTok · YouTube Shorts · Instagram Reels**

---

## Step-by-Step Process for Each Video

### 1. Choose Theme & Write Script
- Pick from the 7 content buckets (see research report)
- Write 8–12 caption lines, each 5–8 words max
- Target: 60–90 second narrative arc
- Structure: Hook (0–5s) → Empathy → Reframe → Truth → Uplift → Close

### 2. Find Footage (Pexels — Free, No Attribution)
Search at pexels.com/search/videos/[keyword]

**How to get direct download URLs without API:**
1. Open a Pexels video page in browser
2. Run in browser console:
```js
const str = JSON.stringify(JSON.parse(document.getElementById('__NEXT_DATA__').textContent).props?.pageProps?.medium);
console.log(str.match(/https?:\/\/[^"]*\.mp4[^"]*/g));
```
3. Pick the `hd_1920_1080` or `hd_2048_1080` quality URL
4. Download with Python:
```python
import requests
headers = {'Referer':'https://www.pexels.com/', 'User-Agent':'Mozilla/5.0'}
r = requests.get(url, headers=headers, stream=True)
with open('clip.mp4','wb') as f:
    for chunk in r.iter_content(1024*256): f.write(chunk)
```

**Best search terms by scene type:**
- Hook (sad/heavy): `person window rain sad`, `lying bed staring ceiling`
- Empathy: `person coffee morning thinking`, `tired exhausted quiet`
- Reframe: `person nature peaceful deep breath`, `eyes closed calm`
- Truth: `person meditating arms open mountain`, `standing peaceful`
- Uplift: `person walking sunrise golden hour`, `silhouette sunrise hope`
- Close: `person soft smile peaceful calm close up`

### 3. Find Music (Bensound — Free with Attribution)
Site: bensound.com/free-music-for-videos

**How to get direct MP3 URL:**
1. Open the track page, click Play
2. Check Network tab in DevTools → filter by `cdn2.bensound`
3. URL format: `https://cdn2.bensound.com/bensound-[trackname].mp3`
4. Download with Python (same method as video)

**Best mood filters for motivational content:**
- Touching, Reflective, Uplifting, Calm

**Required attribution in video description:**
```
Music: "[Track Name]" by [Artist] — bensound.com
```

### 4. Assemble Video (assemble_video.py)
Edit the SCHEDULE and CAPTIONS lists in the script:

```python
SCHEDULE = [
    # (filename, start_sec, duration_sec)
    ("clip_01_hook.mp4", 0, 7),
    ...
]

CAPTIONS = [
    # (time_in, time_out, text, font_size)
    (0.8, 5.5, "Your caption here", 72),
    ...
]
```

**Check actual clip durations first:**
```python
from moviepy import VideoFileClip
c = VideoFileClip("clip.mp4", audio=False)
print(c.duration, c.size)
```

**Run render:**
```
python assemble_video.py
```
Render time: ~25–35 min for 90s video at 1080×1920 on CPU.

### 5. Review Checklist Before Posting
- [ ] All captions readable (white text, black stroke)
- [ ] Logo watermark visible bottom-right
- [ ] Music fades in/out smoothly
- [ ] No clip ends abruptly mid-sentence
- [ ] Total duration 60–90 seconds
- [ ] Bensound attribution ready for description

### 6. Post Settings
- **YouTube Shorts**: Upload as vertical, add #shorts tag
- **TikTok**: Upload directly, add trending sounds if needed
- **Instagram Reels**: Upload, write hook in caption

---

## Content Themes (from Research Report)
Priority order for highest viral potential:
1. Discipline / Stoicism clips
2. Self-compassion / "healing while building"
3. Science-backed motivation (neuroscience angle)
4. Famous speech compilations
5. Transformation stories

**Best speaker content to clip:**
Goggins · Huberman · Willink · Hormozi · Bartlett · Dispenza

---

## Caption Style Guide
- Font: Arial-Bold, white, black stroke (width 3)
- Size: 64–92pt depending on line length
- Position: 54% down from top (centre-ish)
- Max 2 lines per caption, 6–8 words per line
- Timing: 5–9 seconds per card

---

## Music Attribution Template (copy into description)
```
Music: "Long Night" by Aventure — bensound.com
Footage: Pexels.com (royalty-free)
```
