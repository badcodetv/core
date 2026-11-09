#!/bin/bash
# 1080p silent copies of the round-10 clips into r10/video/premiere/, for Premiere.
V="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/r10/video"
cd "$V" || exit 1; mkdir -p premiere
for f in r10-*.mp4; do
  [ -f "premiere/$f" ] && continue
  ffmpeg -loglevel error -y -i "$f" -an -vf "scale=1920:1080:flags=lanczos" -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p "premiere/$f" && echo "$f"
done
