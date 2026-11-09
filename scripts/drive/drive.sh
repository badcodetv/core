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
# Reliability: a connection that goes quiet for 60 s is dropped and the file retried (the default waits
# 5 min); the whole run retries up to 5 times. A rerun is always safe: files already there are skipped.
# Every real run is logged to ~/.cache/badcode-drive/ so a slow or failed run can be read afterwards.
rc=(rclone --drive-root-folder-id "$id" --exclude-from "$HERE/exclude.txt" --update --transfers 4 --checkers 8
    --drive-chunk-size 64M --timeout 60s --contimeout 30s --retries 5 --low-level-retries 20
    --stats 10s --stats-one-line -v)
LOGDIR="$HOME/.cache/badcode-drive"; mkdir -p "$LOGDIR"
log="$LOGDIR/$cmd-$folder-$(date +%Y%m%d-%H%M%S).log"
# list what one direction WOULD copy: a count, the size, and the first 20 files (never a silent cap)
would() { local out n; out="$("${rc[@]}" copy "$1" "$2" --dry-run 2>&1)"
  n=$(grep -c "Skipped copy" <<<"$out" || true)
  echo "   $n file(s)"
  grep "Skipped copy" <<<"$out" | sed 's/.*NOTICE: //; s/: Skipped copy.*//; s/^/   /' | head -20
  (( n > 20 )) && echo "   ... and $((n - 20)) more"; true; }
dry=(--dry-run); [[ "$go" == --go ]] && dry=()
case "$cmd" in
  push|pull)
    if [[ "$cmd" == push ]]; then src="$local_dir"; dst="$REMOTE:"; else src="$REMOTE:"; dst="$local_dir"; fi
    if [[ ${#dry[@]} -gt 0 ]]; then echo "dry run: would $cmd"; would "$src" "$dst"; echo "(add --go to do it)"; exit; fi
    echo "$cmd $folder: progress every 10 s; full log $log"
    "${rc[@]}" copy "$src" "$dst" --log-file "$log" --stats-log-level NOTICE & pid=$!
    tail -n0 -F "$log" 2>/dev/null | grep --line-buffered -E "ETA|ERROR|Failed" & tp=$!
    rcode=0; wait $pid || rcode=$?; kill $tp 2>/dev/null || true
    if (( rcode == 0 )); then echo "done: $(grep -cE 'Copied \(' "$log" || true) file(s) copied, nothing failed"
    else echo "FAILED (rclone exit $rcode): $(grep -c ERROR "$log" || true) error(s); rerun the same command to pick up where it stopped, log: $log"; fi
    exit $rcode ;;
  status) echo "== would PUSH (local newer or missing on Drive):"; would "$local_dir" "$REMOTE:"
          echo "== would PULL (Drive newer or missing locally):"; would "$REMOTE:" "$local_dir" ;;
  *) echo "push | pull | status | list"; exit 1 ;;
esac
