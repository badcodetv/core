#!/usr/bin/env bash
# Browser CHANNELS — never think about ports or profiles again.
#
# A channel is ONE CDP port plus ONE Chrome profile, claimed by one process at a time:
#   channel 1 -> port 9222, profile .flow-profile        (the original — unchanged)
#   channel 2 -> port 9223, profile .flow-profile-9223
#   channel N -> port 9221+N
#
#   ./scripts/browser-channel.sh claim      # THE ONE YOU WANT. Gives you a usable channel,
#                                           # launching a browser if none is free. Prints the port.
#   ./scripts/browser-channel.sh list       # what is running, what is claimed, what is logged in
#   ./scripts/browser-channel.sh up  <n>    # launch channel n specifically
#   ./scripts/browser-channel.sh port <n>   # print the port for channel n
#   ./scripts/browser-channel.sh release <n># drop a stale claim
#   ./scripts/browser-channel.sh down <n>   # kill channel n's browser
#
# `claim` prints `CHANNEL=<n> PORT=<p> LOGGED_IN=<yes|no|unknown>` on the last line so a caller
# can eval it. Ruled 2026-08-26 (Kai): the agent asks for a channel, it never chooses a port.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MAX_CHANNELS="${BADCODE_MAX_CHANNELS:-8}"
LOCKDIR="$ROOT/.flow-channels"
FIRST_PORT=9222

port_for()    { echo $(( FIRST_PORT + $1 - 1 )); }
profile_for() { if [ "$1" = "1" ]; then echo "$ROOT/.flow-profile"; else echo "$ROOT/.flow-profile-$(port_for "$1")"; fi; }

is_up()  { curl -sf --max-time 1 "http://localhost:$(port_for "$1")/json/version" >/dev/null 2>&1; }

# A lock is a file holding "<pid> <owner>", written by the LONG-LIVED process that owns the
# channel — the flow MCP server, one per Claude session. This script never writes one: it exits
# immediately, so a lock in its name would be stale the moment it was created. It only READS
# locks, to avoid handing you a channel another session is already using.
#
# A lock whose PID is gone is stale and removed, so a crashed session can never wedge a channel —
# the failure that would make this whole abstraction worse than typing a port by hand.
lock_pid() {
  local f="$LOCKDIR/$1.lock" pid
  [ -f "$f" ] || return 1
  pid="$(awk '{print $1}' "$f" 2>/dev/null || true)"
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then echo "$pid"; return 0; fi
  rm -f "$f" 2>/dev/null || true
  return 1
}
lock_owner() { awk '{print $2}' "$LOCKDIR/$1.lock" 2>/dev/null || true; }

# Is this channel's Chrome signed in? Ask CDP for its tab list and look for a sign-in URL.
# "unknown" when nothing is open yet — that is not the same as "no", and saying so matters.
logged_in() {
  local tabs
  tabs="$(curl -sf --max-time 2 "http://localhost:$(port_for "$1")/json/list" 2>/dev/null || true)"
  [ -z "$tabs" ] && { echo unknown; return; }
  if echo "$tabs" | grep -qE 'accounts\.google\.com|/signin'; then echo no
  elif echo "$tabs" | grep -qE 'labs\.google/fx/tools/flow|suno\.com'; then echo yes
  else echo unknown; fi
}

cmd_list() {
  printf '%-4s %-6s %-8s %-10s %-9s %s\n' CH PORT STATE CLAIMED LOGGEDIN PROFILE
  for c in $(seq 1 "$MAX_CHANNELS"); do
    local state claimed li
    if is_up "$c"; then state=up; li="$(logged_in "$c")"; else state=down; li=-; fi
    if pid="$(lock_pid "$c")"; then claimed="$pid:$(lock_owner "$c")"; else claimed=free; fi
    printf '%-4s %-6s %-8s %-10s %-9s %s\n' "$c" "$(port_for "$c")" "$state" "$claimed" "$li" "$(basename "$(profile_for "$c")")"
  done
}

cmd_up() {
  local c="$1"
  if is_up "$c"; then echo "channel $c already up on $(port_for "$c")"; return 0; fi
  FLOW_CDP_PORT="$(port_for "$c")" nohup "$ROOT/scripts/flow-chrome.sh" >/tmp/flow-chrome-$(port_for "$c").log 2>&1 &
  for _ in $(seq 1 40); do is_up "$c" && break; sleep 0.5; done
  is_up "$c" || { echo "channel $c failed to come up — see /tmp/flow-chrome-$(port_for "$c").log" >&2; return 1; }
  echo "channel $c up on $(port_for "$c")"
}

cmd_claim() {
  local owner="${1:-flow}" chosen=""
  # Prefer a browser that is already running, unclaimed, and signed in — no new login needed.
  for c in $(seq 1 "$MAX_CHANNELS"); do
    if is_up "$c" && ! lock_pid "$c" >/dev/null && [ "$(logged_in "$c")" = yes ]; then chosen="$c"; break; fi
  done
  # Then any running, unclaimed browser.
  if [ -z "$chosen" ]; then
    for c in $(seq 1 "$MAX_CHANNELS"); do
      if is_up "$c" && ! lock_pid "$c" >/dev/null; then chosen="$c"; break; fi
    done
  fi
  # Then launch the lowest channel that is down and unclaimed.
  if [ -z "$chosen" ]; then
    for c in $(seq 1 "$MAX_CHANNELS"); do
      if ! is_up "$c" && ! lock_pid "$c" >/dev/null; then cmd_up "$c" >&2 && chosen="$c"; break; fi
    done
  fi
  [ -z "$chosen" ] && { echo "ALL_CHANNELS_BUSY: all $MAX_CHANNELS channels are claimed by live processes. Release one: $0 release <n>" >&2; exit 1; }
  # No lock is written here — see the note above. The session's flow MCP server takes the claim
  # on its first call, and `$owner` is recorded there.
  echo "CHANNEL=$chosen PORT=$(port_for "$chosen") LOGGED_IN=$(logged_in "$chosen")"
}

case "${1:-}" in
  list|"")  cmd_list ;;
  claim)    cmd_claim "${2:-flow}" ;;
  up)       cmd_up "${2:?usage: up <channel>}" ;;
  down)     pkill -f "remote-debugging-port=$(port_for "${2:?usage: down <channel>}")" && echo "channel $2 stopped" || echo "channel $2 was not running" ;;
  port)     port_for "${2:?usage: port <channel>}" ;;
  release)  rm -f "$LOCKDIR/${2:?usage: release <channel>}.lock" && echo "channel $2 released" ;;
  *)        sed -n '2,20p' "$0"; exit 1 ;;
esac
