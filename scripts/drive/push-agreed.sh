#!/usr/bin/env bash
# Push ONLY a story's agreed cut to Drive: the files listed in scripts/drive/agreed/<story>.list
# (paths relative to the story's folder on this machine), not the whole folder.
#   scripts/drive/push-agreed.sh <story>          dry run: how many listed files would go up
#   scripts/drive/push-agreed.sh <story> --go     upload them
# Same safety as drive.sh: copy only, never delete, a file is replaced only by a newer copy.
# A list is built from Premiere's snapshot of the agreed sequence (<folder>/.bridge/state-<sequence>.json):
#   jq -r '[.videoTracks[].items[],.audioTracks[].items[]] | map(.mediaPath) | unique[]' <state.json>
# with the folder prefix stripped, plus the .prproj and the timeline's edl.json + preview.mp4.
# rclone refuses --files-from together with --exclude-from, so exclude.txt is not used: keep caches off the list.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REMOTE="${BADCODE_DRIVE_REMOTE:-badcode}"
story="${1:?which story? (drive.sh list)}"; go="${2:-}"
list="$HERE/agreed/$story.list"; [[ -f "$list" ]] || { echo "no agreed list: $list"; exit 1; }
PY="$(command -v python3 || command -v python)"
id="$(cd "$HERE" && "$PY" -c "import json;print(json.load(open('folders.json'))['folders']['$story']['drive'])")"
local_dir="$("$PY" "$HERE/localmap.py" get "$story")" || exit $?
missing=$(cd "$local_dir" && while IFS= read -r f; do [[ -e "$f" ]] || echo "$f"; done < "$list")
[[ -z "$missing" ]] || { echo "listed but not on this machine:"; echo "$missing" | sed 's/^/   /'; }
rc=(rclone --drive-root-folder-id "$id" --update --transfers 4 --checkers 8 --drive-chunk-size 64M
    --timeout 60s --contimeout 30s --retries 5 --low-level-retries 20 --stats 10s --stats-one-line -v
    --files-from "$list" copy "$local_dir" "$REMOTE:")
left() { "${rc[@]}" --dry-run 2>&1 | grep -cE 'Skipped copy|ERROR|Failed' || true; }
if [[ "$go" != --go ]]; then echo "$story: $(wc -l < "$list") listed, $(left) to push or failing (add --go)"; exit; fi
LOGDIR="$HOME/.cache/badcode-drive"; mkdir -p "$LOGDIR"; log="$LOGDIR/push-agreed-$story-$(date +%Y%m%d-%H%M%S).log"
echo "push-agreed $story: log $log"
code=0; "${rc[@]}" --log-file "$log" --stats-log-level NOTICE || code=$?
echo "exit $code: $(grep -cE 'Copied \(' "$log" || true) copied, $(grep -c ERROR "$log" || true) errors; $(left) left"
exit $code
