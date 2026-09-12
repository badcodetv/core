#!/usr/bin/env bash
# Launch a persistent Chrome/Chromium with a remote-debugging port for Flow automation.
# Log into Google/Flow ONCE in this window; the session persists in .flow-profile/.
#
# Resolution order for the browser binary:
#   1. $CHROME_BIN (explicit override)
#   2. A system Chrome/Chromium on PATH (Linux/macOS)
#   3. Playwright's bundled Linux Chromium (newest ~/.cache/ms-playwright/chromium-*).
#      This is the preferred path under WSL: it runs INSIDE WSL, so its debug port
#      is on WSL's own localhost — exactly where the Playwright MCP can attach —
#      and it renders via WSLg. (A Windows-side chrome.exe is intentionally NOT
#      used: under default WSL NAT networking its CDP port is not reachable here.)
#
# CONCURRENCY (2026-08-26). One browser per Claude session, not one globally.
#
#   ./scripts/flow-chrome.sh        -> port 9222, profile .flow-profile     (session 1)
#   ./scripts/flow-chrome.sh 2      -> port 9223, profile .flow-profile-9223 (session 2)
#   ./scripts/flow-chrome.sh 3      -> port 9224, ...
#
# Then start the Claude session that owns it with the matching port:
#   FLOW_CDP_PORT=9223 claude
#
# 🔴 Chrome REFUSES to share a user-data-dir between running instances, so a second
# browser needs a second profile — which means a separate one-time login to
# Google/Flow and Suno in that window. That cost is unavoidable, not a bug.
set -euo pipefail

# Optional first arg is a session index: 1 -> 9222, 2 -> 9223, ...
IDX="${1:-}"
if [ -n "$IDX" ]; then
  case "$IDX" in
    ''|*[!0-9]*) echo "Session index must be a number (1, 2, 3...). Got: $IDX" >&2; exit 1 ;;
  esac
  PORT=$(( 9221 + IDX ))
else
  PORT="${FLOW_CDP_PORT:-9222}"
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# One profile per port. 9222 keeps the original path, so the existing logged-in
# profile is untouched and session 1 behaves exactly as it always has.
if [ "$PORT" = "9222" ]; then
  PROFILE="${FLOW_PROFILE:-$ROOT/.flow-profile}"
else
  PROFILE="${FLOW_PROFILE:-$ROOT/.flow-profile-$PORT}"
fi

# Refuse to start a second Chrome on a port that already answers — that is the
# failure that looks like "the automation attached to the wrong browser".
if curl -sf --max-time 2 "http://localhost:$PORT/json/version" >/dev/null 2>&1; then
  echo "A browser is ALREADY listening on CDP :$PORT — not launching a second one." >&2
  echo "Use it as-is, or pick another session index (e.g. ./scripts/flow-chrome.sh 2)." >&2
  exit 1
fi

# Resolve a browser binary.
#
# 🔴 BRANDED CHROME IS FOR THE LISTENING CHANNEL ONLY (2026-09-12).
# AI Studio's GenerateContent refuses Chrome for Testing outright: pressed by hand it answers
# "Failed to create interaction: permission denied." (listen-mcp T3, confirmed by Kai 2026-09-11).
# So the listening channel must run real Google Chrome. Every OTHER channel must NOT: Flow's and
# Suno's logged-in profiles were written by the newer Chrome-for-Testing build, and Chrome refuses
# a user-data-dir written by a newer version — preferring branded Chrome globally would silently
# lock us out of accounts we are already signed into.
LISTEN_CHANNEL="${LISTEN_CHANNEL:-2}"
CHROME="${CHROME_BIN:-}"
if [ -z "$CHROME" ] && [ "$(( PORT - 9221 ))" = "$LISTEN_CHANNEL" ]; then
  for c in "google-chrome" "google-chrome-stable" \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME="$c"; break; fi
  done
  if [ -z "$CHROME" ]; then
    echo "Channel $LISTEN_CHANNEL is the LISTENING channel and needs branded Google Chrome," >&2
    echo "which is not installed. AI Studio refuses Chrome for Testing. Install it with:" >&2
    echo "  cd /tmp && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install -y ./google-chrome-stable_current_amd64.deb" >&2
    exit 1
  fi
fi
if [ -z "$CHROME" ]; then
  for c in "chromium" "chromium-browser"; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
# Fall back to Playwright's bundled Chromium (newest build by numeric suffix).
if [ -z "$CHROME" ]; then
  for d in $(ls -d "$HOME"/.cache/ms-playwright/chromium-*/ 2>/dev/null | sort -t- -k2 -n -r); do
    if [ -x "${d}chrome-linux64/chrome" ]; then CHROME="${d}chrome-linux64/chrome"; break; fi
  done
fi
if [ -z "$CHROME" ]; then
  echo "No Chrome/Chromium found. Set CHROME_BIN=/path/to/chrome, or run: npx playwright install chromium" >&2
  exit 1
fi

# AUDIO (2026-09-11). Each channel plays into its own virtual speaker, so the listening loop can
# record exactly what THIS Chrome plays (`parec`/ffmpeg on badcode_ch<N>.monitor) without spending
# a Suno download and without catching another channel's sound. A loopback copies that speaker to
# the default one, so live listening is unchanged.
#
# 🔴 Every PulseAudio step is best-effort: if pactl is missing or the WSLg audio server is not
# ready, Chrome launches exactly as it always has. PULSE_SINK is set ONLY once the sink is
# confirmed present — naming a sink that does not exist can leave Chrome with no audio at all.
# Runs after the port-refusal check above and skips if the sink already exists, so a repeat
# launch never stacks a second sink.
CH=$(( PORT - 9221 ))
SINK="badcode_ch$CH"
has_sink() {
  local sinks
  sinks="$(pactl list short sinks 2>/dev/null)" || return 1
  awk -v s="$SINK" '$2 == s { found = 1 } END { exit !found }' <<<"$sinks"
}
if ! command -v pactl >/dev/null 2>&1; then
  echo "warning: pactl not found — launching without a per-channel audio sink (recording unavailable)." >&2
elif ! pactl info >/dev/null 2>&1; then
  echo "warning: PulseAudio not reachable — launching without a per-channel audio sink (recording unavailable)." >&2
else
  if ! has_sink; then
    if pactl load-module module-null-sink sink_name="$SINK" \
         sink_properties=device.description="BadCode_channel_$CH" >/dev/null 2>&1; then
      pactl load-module module-loopback source="$SINK.monitor" sink=@DEFAULT_SINK@ latency_msec=60 >/dev/null 2>&1 \
        || echo "warning: loaded $SINK but its loopback failed — this channel will record but not be audible." >&2
    else
      echo "warning: could not create audio sink $SINK — launching without it (recording unavailable)." >&2
    fi
  fi
  if has_sink; then
    export PULSE_SINK="$SINK"
    echo "Audio sink: $SINK (record from $SINK.monitor)"
  fi
fi

echo "Launching: $CHROME"
echo "CDP port:  $PORT    profile: $PROFILE"
if [ "$PORT" != "9222" ]; then
  echo "→ This is a SECOND browser. Log into Google/Flow (and Suno if needed) in it once."
  echo "→ Start its Claude session with:  FLOW_CDP_PORT=$PORT claude"
else
  echo "→ Log into Google/Flow in the window that opens, then leave it running."
fi
exec "$CHROME" \
  --remote-debugging-port="$PORT" \
  --user-data-dir="$PROFILE" \
  --no-first-run --no-default-browser-check \
  --no-sandbox \
  "https://labs.google/fx/tools/flow"
