#!/bin/bash
# 1080p silent copies (clip's own fps) of the round-9 Ghostface clips (+ t06gf from round 8) into video/premiere/, for Premiere.
V="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/video"
cd "$V" || exit 1
for f in cb-*g-*gr9-[ab].mp4 cb-t06gf-t06gfr8-a.mp4; do
  [ -f "$f" ] || continue; [ -f "premiere/$f" ] && continue
  ffmpeg -loglevel error -y -i "$f" -an -vf "scale=1920:1080:flags=lanczos" -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p "premiere/$f" && echo "$f"
done
