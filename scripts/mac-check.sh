#!/usr/bin/env bash
# One-shot preflight for running BadCode's Suno automation on a Mac (2026-11-03).
# Checks the tools, installs packages, then opens the Suno browser and reads the create form back.
#   ./scripts/mac-check.sh
# Guide: docs/misc/2026-11-03-mac-setup.md
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
ok=1
say()  { printf '%s %s\n' "$1" "$2"; }
need() { if command -v "$1" >/dev/null 2>&1; then say "✅" "$1"; else say "❌" "$1 missing — $2"; ok=0; fi; }

[ "$(uname)" = "Darwin" ] || say "⚠️ " "this is not a Mac ($(uname)); the script still runs"
need git     "install Xcode command line tools: xcode-select --install"
need python3 "install Xcode command line tools: xcode-select --install (the prompt-check hook needs it)"
need curl    "should ship with macOS"
need node    "install Node 22+: brew install node@22  (or https://nodejs.org)"
if command -v node >/dev/null 2>&1; then
  major="$(node -p 'process.versions.node.split(".")[0]')"
  if [ "$major" -ge 22 ]; then say "✅" "node $(node -v)"; else say "❌" "node $(node -v) is too old — need 22+"; ok=0; fi
fi
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ -x "$CHROME" ] || [ -n "${CHROME_BIN:-}" ]; then say "✅" "Google Chrome"; else say "❌" "Google Chrome not in /Applications — install it from google.com/chrome"; ok=0; fi
[ "$ok" = 1 ] || { echo; echo "Fix the ❌ lines above, then run this again."; exit 1; }

echo; echo "Installing packages (npm install)…"
npm install --no-audit --no-fund >/dev/null || { echo "❌ npm install failed — run it by hand to see why"; exit 1; }
say "✅" "packages installed"

echo; echo "Opening the Suno browser (a separate Chrome window with its own profile)…"
npx tsx scripts/suno/suno.mts status
echo
echo "If it says LOGGED_IN=no or the form is empty: sign in to Suno in the Chrome window that opened,"
echo "leave that window running, and run this script once more."
