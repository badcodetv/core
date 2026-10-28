#!/usr/bin/env bash
# Money For Something, storyboard v3: run every clip in clips-v3.tsv through mfs-clip.mts, one at a time. Skips clips already on disk.
# Jack's retry rule: on a failure, the runner reloads the page itself; wait 10 s and try again, up to 4 times.
# usage: PLATES=<dir with mfs-plate-<id>.jpg> bash run-clips.sh [name-prefix]
H="$(cd "$(dirname "$0")" && pwd)"
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos/v3"
: "${PLATES:?set PLATES}"; mkdir -p "$PLATES/.uploaded"
while IFS=$'\t' read -r NAME PLATE CH; do
  [ -z "$NAME" ] && continue; case "$NAME" in "${1:-}"*) ;; *) continue;; esac
  [ -f "$OUT/$NAME.mp4" ] && { echo "skip $NAME"; continue; }
  for TRY in 1 2 3 4; do
    SKIP=""; [ -f "$PLATES/.uploaded/$PLATE" ] && SKIP=1
    ARGS=("$PLATES/mfs-plate-$PLATE.jpg" "$H/video-prompts/$NAME.txt" "$OUT/$NAME.mp4"); [ -n "$CH" ] && ARGS+=(--char "$CH")
    if (cd "$H" && MFS_SKIP_UPLOAD="$SKIP" npx tsx mfs-clip.mts "${ARGS[@]}" < /dev/null 2>&1 | tail -3); [ -f "$OUT/$NAME.mp4" ]; then touch "$PLATES/.uploaded/$PLATE"; echo "OK $NAME"; break; fi
    grep -q . <<<"$SKIP" || { ls "$OUT/$NAME.mp4.err.png" >/dev/null 2>&1 && touch "$PLATES/.uploaded/$PLATE.maybe"; }
    echo "RETRY $NAME ($TRY)"; read -t 10 <> <(:) || true
  done
done < "$H/clips-v3.tsv"
echo ALL_DONE
