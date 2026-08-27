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
CHROME="${CHROME_BIN:-}"
if [ -z "$CHROME" ]; then
  for c in \
    "google-chrome" "google-chrome-stable" "chromium" "chromium-browser" \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
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
