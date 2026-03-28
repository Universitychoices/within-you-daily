#!/usr/bin/env python3
"""
VIDEO #02 — Source Downloader
Downloads the Jay Shetty source video, bypassing the GitHubDesktop PATH conflict.
Run this FIRST before assemble_video.py.
"""

import subprocess, os, sys

DIR = r"D:\desktop\Desktop\WithInYou\VideoProject_02"
OUT = os.path.join(DIR, "source_jay.mp4")
URL = "https://www.youtube.com/watch?v=rNmOfqWGkjs"

if os.path.exists(OUT):
    print(f"  source_jay.mp4 already exists — skipping download.")
    sys.exit(0)

# Strip broken GitHubDesktop mount point from PATH
env = os.environ.copy()
clean_path = ";".join(
    p for p in env.get("PATH", "").split(";")
    if "GitHubDesktop" not in p
)
env["PATH"] = clean_path

print("Downloading Jay Shetty source video...")
print(f"  URL : {URL}")
print(f"  OUT : {OUT}\n")

result = subprocess.run([
    sys.executable, "-m", "yt_dlp",
    "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]",
    "--merge-output-format", "mp4",
    "-o", OUT,
    URL
], env=env)

if result.returncode == 0:
    size_mb = os.path.getsize(OUT) / 1_048_576
    print(f"\n  Downloaded: source_jay.mp4  ({size_mb:.1f} MB)")
else:
    print("\n  ERROR: download failed. Check yt-dlp is installed: pip install yt-dlp")
    sys.exit(1)
