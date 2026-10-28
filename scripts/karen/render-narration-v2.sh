#!/usr/bin/env bash
# Karen narration v2: every line in narration-v2.tsv, Algenib, two takes (a, b), one WAV per line.
# Usage: scripts/karen/render-narration-v2.sh [id ...]   (needs a python with google-genai as $PY)
set -u
cd "$(dirname "$0")/../.."
set -a; . ./.env; set +a
PY=${PY:-python3}
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Karen/narration-v2"
PROFILE=docs/stories/karen/narration/profiles/narrator-algenib.md
mkdir -p "$OUT"; T=$(mktemp -d)
while IFS=$'\t' read -r id beat text; do
  [ $# -gt 0 ] && [[ ! " $* " == *" $id "* ]] && continue
  printf '%s\n' "$text" > "$T/$id.txt"
  for r in a b; do
    [ -s "$OUT/$id-$r.wav" ] && continue
    "$PY" scripts/aistudio-tts.py "$T/$id.txt" "$OUT/$id-$r.wav" --profile "$PROFILE" --voice Algenib 2>&1 | tail -1
  done
done < scripts/karen/narration-v2.tsv
