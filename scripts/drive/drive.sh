#!/usr/bin/env bash
# Push or pull ONE Premiere folder between D:\badcode-videos and its Drive folder, on demand.
#   scripts/drive/drive.sh list                      folders it knows (folders.json)
#   scripts/drive/drive.sh status <folder>           what push and pull WOULD copy (changes nothing)
#   scripts/drive/drive.sh push   <folder> [--go]    local -> Drive
#   scripts/drive/drive.sh pull   <folder> [--go]    Drive -> local
# Without --go it is a dry run. It only ever COPIES: nothing is deleted on either side, and a file is
# only replaced when the copy being sent is newer (--update). Caches and auto-saves are skipped (exclude.txt).
# One-time setup: an rclone remote called "badcode" signed in as Kai (see README.md).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REMOTE="${BADCODE_DRIVE_REMOTE:-badcode}"
cmd="${1:-list}"; folder="${2:-}"; go="${3:-}"
cfg() { python3 -c "import json,sys;c=json.load(open('$HERE/folders.json'));$1" ; }
if [[ "$cmd" == list ]]; then cfg "[print(f'{k:24} -> Drive: {v[\"drive_name\"]!r} ({v[\"drive\"]})') for k,v in c['folders'].items()]"; exit; fi
[[ -n "$folder" ]] || { echo "which folder? (drive.sh list)"; exit 1; }
id="$(cfg "print(c['folders']['$folder']['drive'])" 2>/dev/null)" || { echo "unknown folder '$folder': add it to folders.json"; exit 1; }
local_dir="${BADCODE_MEDIA_ROOT:-$(cfg "print(c['local_root'])")}/$folder"
rc=(rclone --drive-root-folder-id "$id" --exclude-from "$HERE/exclude.txt" --update --transfers 4 --checkers 8
    --drive-chunk-size 64M --stats 10s --stats-one-line -v)
dry=(--dry-run); [[ "$go" == --go ]] && dry=()
case "$cmd" in
  push)   "${rc[@]}" copy "$local_dir" "$REMOTE:" "${dry[@]}" ;;
  pull)   "${rc[@]}" copy "$REMOTE:" "$local_dir" "${dry[@]}" ;;
  status) echo "== would PUSH (local newer or missing on Drive):"; "${rc[@]}" copy "$local_dir" "$REMOTE:" --dry-run 2>&1 | grep -E "Skipped copy|NOTICE" | sed 's/.*NOTICE: //' | head -200
          echo "== would PULL (Drive newer or missing locally):"; "${rc[@]}" copy "$REMOTE:" "$local_dir" --dry-run 2>&1 | grep -E "Skipped copy|NOTICE" | sed 's/.*NOTICE: //' | head -200 ;;
  *) echo "push | pull | status | list"; exit 1 ;;
esac
