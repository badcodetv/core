#!/usr/bin/env bash
# Karen story film, round 3 (2026-11-18): the new lines in narration-r3.tsv, one take per line.
# Narrator = the story's locked Algenib setup (profile + default model); Karen (Gacrux) and Susan (Kore) plain on 3.8.
# Usage: scripts/karen/render-narration-r3.sh [id ...]
set -u
cd "$(dirname "$0")/../.."
set -a; . ./.env; set +a
OUT=/mnt/d/badcode-videos/karen-story/_outside/Karen/narration-r3
PROFILE=docs/stories/karen/narration/profiles/narrator-algenib.md
mkdir -p "$OUT"; T=$(mktemp -d)
TTS=(uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py)
while IFS=$'\t' read -r id who text; do
  [ $# -gt 0 ] && [[ ! " $* " == *" $id "* ]] && continue
  [ -s "$OUT/$id-a.wav" ] && continue
  printf '%s\n' "$text" > "$T/$id.txt"
  case $who in
    narrator) "${TTS[@]}" "$T/$id.txt" "$OUT/$id-a.wav" --profile "$PROFILE" --voice Algenib 2>&1 | tail -1 ;;
    karen)    "${TTS[@]}" "$T/$id.txt" "$OUT/$id-a.wav" --plain --model gemini-3.8-flash-tts --voice Gacrux 2>&1 | tail -1 ;;
    susan)    "${TTS[@]}" "$T/$id.txt" "$OUT/$id-a.wav" --plain --model gemini-3.8-flash-tts --voice Kore 2>&1 | tail -1 ;;
  esac
  sleep 22
done < scripts/karen/narration-r3.tsv
