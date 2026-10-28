#!/usr/bin/env bash
# Recover a Veo clip whose download ENOENT'd: Chrome still saved it to ~/Downloads
# under Flow's own auto-title. Takes the newest .mp4 there and moves it to $1.
# NEVER re-run a generation to recover a download - it bills again.
set -euo pipefail
dst="$1"
src=$(ls -t ~/Downloads/*.mp4 2>/dev/null | head -1)
[ -n "$src" ] || { echo "NO CANDIDATE"; exit 1; }
age=$(( $(date +%s) - $(stat -c %Y "$src") ))
[ "$age" -lt 600 ] || { echo "STALE (${age}s old): $src"; exit 1; }
mv "$src" "$dst"
echo "rescued $(basename "$src") -> $dst"
