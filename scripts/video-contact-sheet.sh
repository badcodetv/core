#!/usr/bin/env bash
# Build a contact sheet from a video so an agent can SEE the whole clip in one image.
#
# Sparse frame sampling (grab 3 stills and hope) misses exactly the errors that matter:
# a door that swings open for 1.5s, a hand that morphs, a sign that appears. A contact
# sheet costs one image of context and shows every beat of the clip at once.
#
# Usage:
#   scripts/video-contact-sheet.sh <video> [outfile] [fps] [cols]
#   scripts/video-contact-sheet.sh clip.mp4                       # 4fps, 6 cols, full frame
#   REGION=left  scripts/video-contact-sheet.sh clip.mp4          # left 30% only, brightened
#   REGION=right scripts/video-contact-sheet.sh clip.mp4
#   REGION=centre scripts/video-contact-sheet.sh clip.mp4
#
# REGION crops to one vertical band and lifts the exposure — use it when the suspect
# detail is dark or small (near-black BadCode frames hide motion at full-frame scale).
set -euo pipefail

VIDEO="${1:?usage: video-contact-sheet.sh <video> [outfile] [fps] [cols]}"
OUT="${2:-${VIDEO%.*}-sheet.jpg}"
FPS="${3:-4}"
COLS="${4:-6}"
REGION="${REGION:-full}"

case "$REGION" in
  left)   CROP="crop=iw*0.30:ih:0:0,";            EQ=",eq=brightness=0.18" ;;
  right)  CROP="crop=iw*0.30:ih:iw*0.70:0,";      EQ=",eq=brightness=0.18" ;;
  centre|center) CROP="crop=iw*0.40:ih:iw*0.30:0,"; EQ=",eq=brightness=0.18" ;;
  full)   CROP="";                                 EQ="" ;;
  *) echo "REGION must be one of: full left right centre" >&2; exit 1 ;;
esac

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")
N=$(awk -v d="$DUR" -v f="$FPS" 'BEGIN{printf "%d", d*f}')
ROWS=$(awk -v n="$N" -v c="$COLS" 'BEGIN{printf "%d", (n+c-1)/c}')

ffmpeg -loglevel error -i "$VIDEO" \
  -vf "${CROP}fps=${FPS},scale=320:-1,tile=${COLS}x${ROWS}:padding=3:color=0xff0000${EQ}" \
  -frames:v 1 "$OUT" -y

echo "$OUT  (${DUR}s, ${N} frames at ${FPS}fps, ${COLS}x${ROWS}, region=${REGION})"
