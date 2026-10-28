#!/usr/bin/env bash
# Money For Something 2026 round 2: the podcast and the HS2 reporter (clips-r2.tsv) through mfs-clip.mts in INGREDIENTS mode:
# the still as the scene, the speaker's Flow Character attached for its saved voice (custom voices attach only to Ingredients).
# Each still is uploaded once (marker file). Jack's retry rule: on a failure wait 10 s and try again.
H="$(cd "$(dirname "$0")" && pwd)"
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026/videos"
W="$HOME/.cache/badcode-mfs-2026"; LOG="$OUT/00-run-log.txt"
while IFS=$'\t' read -r NAME PLATE CH SEC N SCREEN LINE; do
  [ -z "$NAME" ] && continue; case "$NAME" in "${1:-}"*) ;; *) continue;; esac
  [ -f "$OUT/$NAME.mp4" ] && { echo "skip $NAME"; continue; }
  SKIP=; [ -f "$W/.up-$PLATE" ] && SKIP=1
  for TRY in 1 2 3; do
    (cd "$H/.." && MFS_DURATION="$SEC" MFS_SKIP_UPLOAD="$SKIP" npx tsx mfs-clip.mts "$W/mfs26-$PLATE.jpg" "$H/prompts/$NAME.txt" "$OUT/$NAME.mp4" --char "$CH" --mode ingredients < /dev/null 2>&1 | tail -2 | tee -a "$LOG")
    [ -f "$OUT/$NAME.mp4" ] && { echo "OK $NAME" | tee -a "$LOG"; touch "$W/.up-$PLATE"; break; }
    SKIP=; [ -f "$W/.up-$PLATE" ] && SKIP=1
    echo "RETRY $NAME ($TRY)" | tee -a "$LOG"; sleep 10
  done
  rm -f "$OUT/$NAME.mp4.bar.png"
done < "$H/clips-r2.tsv"
echo ALL_DONE | tee -a "$LOG"
