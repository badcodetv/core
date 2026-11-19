#!/usr/bin/env bash
# Priority Lane, voice casting round 7 (Jack, 2026-11-19: "we need to fix the voices").
# Every speaking role recast the docs/rules/voices.md way: 4 voices per role (2 Google library voices chosen by region,
# age and gender, 2 designed with one plain sentence each, ids in voices/r7/designed-voices.tsv), each reading the role's
# real lines PLAIN (no style, no profile, no note) on gemini-3.8-flash-tts. One call every ~22 s.
# A take under 70% of the role's expected length is re-run once (about one in five comes back cut short).
# The constable's takes also get a police-radio version (band-passed, light crunch), which is how the cut plays him.
#   scripts/shorts/priority_lane_cast_r7.sh            render every take not yet on disk
set -uo pipefail
cd "$(dirname "$0")/../.."
V=docs/stories/shorts/priority-lane/voices/r7
OUT="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/priority-lane/audio/casting-r7"
mkdir -p "$OUT"
declare -A MIN=([paramedic1]=3.0 [paramedic2]=2.5 [driver]=2.2 [minister]=3.5 [constable]=2.5)
dur() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1" 2>/dev/null || echo 0; }
while IFS=$'\t' read -r opt voice _rest; do
  [ -z "$opt" ] && continue
  role=${opt%-*}
  f="$OUT/pl-r7-$opt.wav"
  if [ -s "$f" ]; then echo "have $opt"; continue; fi
  for try in 1 2; do
    scripts/aistudio-tts.sh "$V/lines/$role.txt" "$f" --plain --model gemini-3.8-flash-tts --voice "$voice" >/dev/null 2>"$OUT/.err-$opt" || true
    d=$(dur "$f"); echo "$opt $voice try$try ${d}s"
    sleep 22
    python3 -c "import sys; sys.exit(0 if float('$d' or 0) >= ${MIN[$role]} else 1)" && break
  done
  if [ "$role" = constable ] && [ -s "$f" ]; then
    ffmpeg -nostdin -loglevel error -y -i "$f" -af "highpass=f=450,lowpass=f=3200,acompressor=threshold=-20dB:ratio=6,volume=1.6,aformat=sample_rates=48000" "$OUT/pl-r7-$opt-radio.wav"
  fi
done < "$V/casting.tsv"
