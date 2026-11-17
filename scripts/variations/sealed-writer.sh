#!/usr/bin/env bash
# Run ONE clean-room writer that cannot see the repo (Jack, 2026-11-17).
#
# Why: "sealed" writers spawned as general-purpose subagents load the whole CLAUDE.md and the 120+ line
# memory index (tested 2026-11-17), so other stories' looks and habits leak into every "fresh" prompt.
# Jack's original fix (2026-10-24) ran writers as `claude -p` in an empty /tmp folder; this restores it,
# and also switches off CLAUDE.md and auto memory explicitly.
#
#   scripts/variations/sealed-writer.sh <round-dir> <brief.md> [extra files...] -- <output.json>
#
# Copies the named brief files (and any reference images) from <round-dir> into an empty temp folder,
# runs the writer there with only Read/Write/WebSearch/WebFetch, and copies <output.json> back into
# <round-dir>. The writer sees nothing else.
set -euo pipefail
dir=$1; shift
files=()
while [[ $# -gt 0 && $1 != -- ]]; do files+=("$1"); shift; done
[[ ${1:-} == -- ]] || { echo "usage: $0 <round-dir> <files...> -- <output.json>" >&2; exit 2; }
out=$2
tmp=$(mktemp -d)
for f in "${files[@]}"; do
  src=$f; [[ -e $src ]] || src="$dir/$f"
  cp "$src" "$tmp/$(basename "$f")"
done
list=$(cd "$tmp" && ls | sed 's/^/- /')
prompt="You are a sealed prompt writer. Your whole world is this folder; read only these files:
$list
Do the web research the brief asks for. Then write the file \`$out\` in this folder exactly as the brief describes,
and reply with one line per prompt. Never name a real person. Describe only what should be in the picture."
cd "$tmp"
CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 \
  claude -p "$prompt" --allowedTools "Read,Write,WebSearch,WebFetch" --permission-mode acceptEdits
cd - >/dev/null
[[ -f "$tmp/$out" ]] || { echo "sealed-writer: no $out written (temp folder kept: $tmp)" >&2; exit 1; }
cp "$tmp/$out" "$dir/$out"
echo "sealed-writer: wrote $dir/$out"
