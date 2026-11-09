#!/usr/bin/env bash
# LatentSync 1.6 (ByteDance, open source): redraws a talking clip's mouth to match a voice we already have.
# Used by the lip-sync-dub skill. Needs Linux or WSL with an NVIDIA GPU (about 18 GB of video memory) and uv.
# Not for macOS (no CUDA).
#
#   scripts/lipsync/latentsync-setup.sh check     # prints INSTALLED or NOT INSTALLED (+ why); exit 0 / 1
#   scripts/lipsync/latentsync-setup.sh install   # clones, makes the venv, downloads the weights (~10 GB)
#
# Location: $LATENTSYNC_HOME (default ~/.cache/badcode-latentsync/LatentSync). Pinned to one commit so
# Kai's and Jack's installs are the same.
set -euo pipefail
HOME_DIR="${LATENTSYNC_HOME:-$HOME/.cache/badcode-latentsync/LatentSync}"
REPO=https://github.com/bytedance/LatentSync.git
COMMIT=a229c3948406bc2cf6eaf4873e662e70c6a04746   # 2025-06-20, LatentSync 1.6
WEIGHTS=ByteDance/LatentSync-1.6

check() {
  local why=()
  command -v nvidia-smi >/dev/null || why+=("no NVIDIA GPU visible (nvidia-smi missing)")
  [ -d "$HOME_DIR/.git" ] || why+=("code not cloned at $HOME_DIR")
  [ -x "$HOME_DIR/.venv/bin/python" ] || why+=("python environment not made")
  [ -f "$HOME_DIR/checkpoints/latentsync_unet.pt" ] || why+=("model weights not downloaded")
  [ -f "$HOME_DIR/checkpoints/whisper/tiny.pt" ] || why+=("whisper weights not downloaded")
  if [ -x "$HOME_DIR/.venv/bin/python" ]; then
    (cd "$HOME_DIR" && .venv/bin/python -c "import torch, latentsync; assert torch.cuda.is_available()" 2>/dev/null) \
      || why+=("python packages missing or CUDA not available in the venv")
  fi
  if [ ${#why[@]} -eq 0 ]; then echo "INSTALLED at $HOME_DIR"; return 0; fi
  echo "NOT INSTALLED:"; printf '  - %s\n' "${why[@]}"; return 1
}

install() {
  command -v uv >/dev/null || { echo "uv is needed first: curl -LsSf https://astral.sh/uv/install.sh | sh"; exit 1; }
  mkdir -p "$(dirname "$HOME_DIR")"
  [ -d "$HOME_DIR/.git" ] || git clone "$REPO" "$HOME_DIR"
  cd "$HOME_DIR"
  git fetch -q origin && git checkout -q "$COMMIT"
  [ -x .venv/bin/python ] || uv venv -p python3.10 .venv
  VIRTUAL_ENV=.venv uv pip install -r requirements.txt
  VIRTUAL_ENV=.venv uv pip install "huggingface_hub[cli]"
  .venv/bin/huggingface-cli download "$WEIGHTS" whisper/tiny.pt latentsync_unet.pt --local-dir checkpoints
  check
}

case "${1:-check}" in
  check) check ;;
  install) install ;;
  *) echo "usage: $0 check|install"; exit 2 ;;
esac
