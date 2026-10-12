#!/usr/bin/env bash
# The Bank Robbery, cut 10 (2026-10-12): the six one-second shouting shots under "Nobody films it".
# Picture: one stretch of each Omni clip in vids/v10 (clip, where it starts in the clip). Sound: the cut 8 stem from 238.33 s
# on (the crowd bed that was under the raised phones), sliced in step with the pictures so it runs unbroken across the six.
# Lengths must match SHOUT in build-cut10.py. Each piece carries 0.25 s spare at its end, like every other piece.
set -euo pipefail
P="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery"
V="$P/vids/v10"; OUT="$P/clips/cut10"; STEM="$P/clips/cut9/cut8-stem-no-narrator-no-music.mp4"
SHOTS=("s08m-low 0.4" "s08o-row-red 0.3" "s08p-row-blue 0.3" "s08l-red 0.3" "s08n-blue 0.3" "s08k-noses 0.3")
LENS=(1.0 1.0 1.0 1.0 1.0 1.125)
CROP="${CROP:-crop=iw*0.96:ih*0.96,}"   # the stills came back with a rounded film-frame border
a=238.33
for i in "${!SHOTS[@]}"; do
  set -- ${SHOTS[$i]}; d=${LENS[$i]}; n=$((i + 1))
  ffmpeg -v error -y -ss "$2" -i "$V/$1.mp4" -ss "$a" -i "$STEM" -t "$(echo "$d + 0.25" | bc)" \
    -filter_complex "[0:v]${CROP}scale=1280:720,fps=24,setsar=1,format=yuv420p[v];[1:a]volume=4.5dB,alimiter=limit=0.84:level=disabled[a]" \
    -map "[v]" -map "[a]" -c:v libx264 -crf 14 -preset medium -c:a pcm_s16le -ar 48000 "$OUT/c10-shout-$n.mov"
  a=$(echo "$a + $d" | bc)
done
ls -la "$OUT"/c10-shout-*.mov
