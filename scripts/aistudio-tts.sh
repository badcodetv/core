#!/usr/bin/env bash
# Run scripts/aistudio-tts.py on whatever Python this machine has (Jack, 2026-11-12: uv is not installed
# on his machine, so the documented `uv run` failed on the first try). Order: uv → ~/.venvs/genai →
# make ~/.venvs/genai once. Loads .env for the GEMINI key. Same arguments as aistudio-tts.py.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
set -a; [ -f "$ROOT/.env" ] && . "$ROOT/.env"; set +a
if command -v uv >/dev/null 2>&1; then
  exec uv run -q --with "google-genai<2" python3 "$ROOT/scripts/aistudio-tts.py" "$@"
fi
VENV="$HOME/.venvs/genai"
if ! "$VENV/bin/python" -c 'import google.genai' 2>/dev/null; then
  python3 -m venv "$VENV" && "$VENV/bin/pip" install -q "google-genai<2"
fi
exec "$VENV/bin/python" "$ROOT/scripts/aistudio-tts.py" "$@"
