#!/usr/bin/env bash
# Open a URL in the Windows default browser from WSL (Kai, 2026-11-27: "always open browsers on Windows rather
# than ... inside WSL"). Pages for Kai or Jack open here; the WSL Chrome (scripts/flow-chrome.sh) is only for
# automation (Flow, Suno, Playwright checks), because its debug port must be reachable from WSL.
#   scripts/open-in-windows.sh http://localhost:8765/t/karen/story/
set -euo pipefail
url="${1:?usage: open-in-windows.sh <url>}"
case "$url" in http://*|https://*) ;; *) echo "only http(s) URLs: $url" >&2; exit 1 ;; esac
if command -v wslview >/dev/null 2>&1; then exec wslview "$url"; fi
# rundll32 hands the URL to the default browser without cmd.exe re-parsing & or ^ in it
exec /mnt/c/Windows/System32/rundll32.exe url.dll,FileProtocolHandler "$url"
