#!/usr/bin/env bash
# Money For Something 2026: every clip in clips-2026.tsv through mfs-clip.mts (Frames, plate P1 or P2, The Host attached), one at a time.
# Skips clips already on disk. Jack's retry rule: on a failure wait 10 s and try again.
# usage: bash run-clips-2026.sh [name-prefix]
H="$(cd "$(dirname "$0")" && pwd)"
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026/videos"
W="$HOME/.cache/badcode-mfs-2026"; mkdir -p "$OUT"; LOG="$OUT/00-run-log.txt"
while IFS=$'\t' read -r NAME PLATE CH SEC N SCREEN LINE; do
  [ -z "$NAME" ] && continue; case "$NAME" in "${1:-}"*) ;; *) continue;; esac
  [ -f "$OUT/$NAME.mp4" ] && { echo "skip $NAME"; continue; }
  SKIP=1; [ "$PLATE" = P2 ] && [ ! -f "$W/.p2-uploaded" ] && SKIP=
  for TRY in 1 2 3; do
    (cd "$H/.." && MFS_DURATION="$SEC" MFS_SKIP_UPLOAD="$SKIP" npx tsx mfs-clip.mts "$W/mfs26-plate-$PLATE.jpg" "$H/prompts/$NAME.txt" "$OUT/$NAME.mp4" --char "$CH" --mode frames < /dev/null 2>&1 | tail -2 | tee -a "$LOG")
    [ -f "$OUT/$NAME.mp4" ] && { echo "OK $NAME" | tee -a "$LOG"; [ "$PLATE" = P2 ] && touch "$W/.p2-uploaded"; break; }
    echo "RETRY $NAME ($TRY)" | tee -a "$LOG"; sleep 10
  done
  rm -f "$OUT/$NAME.mp4.bar.png"
done < "$H/clips-2026.tsv"
echo ALL_DONE | tee -a "$LOG"
