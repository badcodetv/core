#!/usr/bin/env bash
# Money For Something, the topical monologue: every clip in clips-topical.tsv through mfs-clip.mts (Frames, plate B, The Host attached), one at a time.
# Skips clips already on disk. Jack's retry rule: on a failure wait 10 s and try again, up to 4 times.
# usage: bash run-clips-topical.sh [name-prefix]
H="$(cd "$(dirname "$0")" && pwd)"
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos"
W="$HOME/.cache/badcode-mfs-topical"; LOG="$OUT/00-run-log.txt"
while IFS=$'\t' read -r NAME PLATE CH SEC N; do
  [ -z "$NAME" ] && continue; case "$NAME" in "${1:-}"*) ;; *) continue;; esac
  [ -f "$OUT/$NAME.mp4" ] && { echo "skip $NAME"; continue; }
  for TRY in 1 2; do
    (cd "$H" && MFS_DURATION="$SEC" MFS_SKIP_UPLOAD=1 npx tsx mfs-clip.mts "$W/mfst-plate-$PLATE.jpg" "$H/video-prompts/$NAME.txt" "$OUT/$NAME.mp4" --char "$CH" --mode frames < /dev/null 2>&1 | tail -2 | tee -a "$LOG")
    [ -f "$OUT/$NAME.mp4" ] && { echo "OK $NAME" | tee -a "$LOG"; break; }
    echo "RETRY $NAME ($TRY)" | tee -a "$LOG"; read -t 10 <> <(:) || true
  done
  rm -f "$OUT/$NAME.mp4.bar.png"
done < "$H/clips-topical.tsv"
echo ALL_DONE | tee -a "$LOG"
