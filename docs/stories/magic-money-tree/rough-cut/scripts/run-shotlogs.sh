#!/usr/bin/env bash
# Index every conformed film that has no shotlog yet, eight at a time, from local copies of the
# downloaded masters (made here if missing). LIBRARY=1 also indexes the _library reference films.
# Usage: run-shotlogs.sh [id ...]   (no ids = every film in the conform status)
set -u
cd "$(dirname "$0")"
LOCAL=~/.cache/badcode/mmt-masters
CLIPS=/mnt/d/badcode-videos/magic-money-tree/clips
ST=../../research/footage-pass-2026-09-29/scripts/conform-status.tsv
mkdir -p "$LOCAL"
awk -F'\t' 'NR>1 && $13=="OK" {print $1"\t"$2"\t"$3}' "$ST" |
while IFS=$'\t' read -r id scene master; do
  [ $# -gt 0 ] && [[ " $* " != *" $id "* ]] && continue
  [ "$scene" = _library ] && [ "${LIBRARY:-}" != 1 ] && continue
  [ -s "../shotlogs/$id.tsv" ] && continue
  if [ ! -s "$LOCAL/$master" ]; then
    src=$(ls "$CLIPS/_masters/$master" "$CLIPS/$scene/$master" 2>/dev/null | head -1)
    cp "$src" "$LOCAL/$master.part" && mv "$LOCAL/$master.part" "$LOCAL/$master"
  fi
  echo "$id"
done | xargs -P8 -n1 python3 shotlog.py
