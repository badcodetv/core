#!/usr/bin/env bash
# Sealed Suno prompt writer — the clean room that actually is one (2026-10-23).
#
# Why: the "clean-room" helpers of Bank Robbery Rounds CR→GG were Agent-tool subagents spawned
# inside this repo. Those load CLAUDE.md and MEMORY.md automatically (dozens of Suno rules), and
# "ignore them" does not take them out of context. This runs a separate `claude -p` in an empty
# directory outside the repo: no CLAUDE.md, no memory, no skills, no tools, no MCP, a one-line
# system prompt. Its only knowledge is the brief file you give it.
#
# Usage: scripts/suno/sealed-writer.sh [--web] <brief.md> [out.md]
#   --web lets it use WebSearch/WebFetch (internet research, still no repo).
#   The brief should be Jack's own words, the listen log text and the lyric words — never a
#   paraphrase written by a session that has the repo loaded.
#   Self-check: scripts/suno/sealed-writer.sh --check   (asks it what it can see; expect "nothing")
set -euo pipefail

tools=""
if [[ "${1:-}" == "--web" ]]; then tools="WebSearch,WebFetch"; shift; fi

room="$(mktemp -d /tmp/suno-sealed-XXXXXX)"
trap 'rm -rf "$room"' EXIT

run() {
  (cd "$room" && timeout 1800 claude -p \
    --tools "$tools" --allowedTools "$tools" --disable-slash-commands --strict-mcp-config \
    --setting-sources "project" --no-session-persistence \
    --system-prompt "You are an experienced music producer who uses Suno." \
    "$1" < /dev/null)
}

if [[ "${1:-}" == "--check" ]]; then
  run "Do you see any project instructions, CLAUDE.md, memory notes, skills, or rules about Suno, BadCode, Jack or Kai in your context? Quote any. What tools do you have?"
  exit 0
fi

brief="${1:?usage: sealed-writer.sh <brief.md> [out.md]}"
out="${2:-/dev/stdout}"
run "$(cat "$brief")" > "$out"
