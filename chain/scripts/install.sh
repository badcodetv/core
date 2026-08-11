#!/usr/bin/env bash
# Bring a bare WSL/Linux machine up to the toolchain pinned in chain/versions.json.
# Safe to re-run: every step is skipped if it is already at the pinned version.
#
#   ./chain/scripts/install.sh          install anything missing or mismatched
#   ./chain/scripts/install.sh --force  reinstall even if versions already match
#
# Verify afterwards with:  npx tsx packages/cli/src/bin.ts chain doctor
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSIONS="$DIR/versions.json"
FORCE="${1:-}"

read_version() { node -e "process.stdout.write(require('$VERSIONS').$1)"; }

RUST_V="$(read_version rust)"
AGAVE_V="$(read_version agave)"
ANCHOR_V="$(read_version anchor)"

say()  { printf '\n\033[1m==> %s\033[0m\n' "$*"; }
skip() { printf '    already at %s, skipping\n' "$*"; }

# Anchor's build needs these; on a bare WSL image they are usually absent and the
# failure surfaces much later as a confusing linker error.
say "System build dependencies"
if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq build-essential pkg-config libssl-dev libudev-dev
else
  echo "    non-apt system; ensure a C toolchain, pkg-config and OpenSSL headers exist"
fi

say "Rust $RUST_V"
if ! command -v rustup >/dev/null 2>&1; then
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain "$RUST_V"
  # shellcheck disable=SC1091
  source "$HOME/.cargo/env"
elif [ "$(rustc --version | awk '{print $2}')" = "$RUST_V" ] && [ "$FORCE" != "--force" ]; then
  skip "$RUST_V"
else
  rustup toolchain install "$RUST_V"
  rustup default "$RUST_V"
fi

# Anchor MUST come before Solana: `avm install` pulls down its own Solana CLI and
# will silently overwrite whatever is already there. Install Solana first and you
# just watch your pinned version get clobbered.
say "Anchor $ANCHOR_V (via avm)"
if ! command -v avm >/dev/null 2>&1; then
  echo "    installing avm (builds from source, ~1 min)"
  cargo install --git https://github.com/solana-foundation/anchor avm --locked --force
fi
if command -v anchor >/dev/null 2>&1 \
   && anchor --version 2>/dev/null | grep -q "$ANCHOR_V" \
   && [ "$FORCE" != "--force" ]; then
  skip "$ANCHOR_V"
else
  # --from-source is not optional on older distros. Anchor's prebuilt binaries are
  # linked against GLIBC 2.39 (Ubuntu 24.04+); on 22.04 (GLIBC 2.35) the download
  # succeeds and then every invocation dies with a "version GLIBC_2.39 not found"
  # error that looks nothing like a packaging problem.
  echo "    building anchor $ANCHOR_V from source, this takes several minutes"
  avm install "$ANCHOR_V" --from-source --force
  avm use "$ANCHOR_V"
fi

say "Agave / Solana CLI $AGAVE_V"
if command -v solana >/dev/null 2>&1 \
   && solana --version 2>/dev/null | grep -q "$AGAVE_V" \
   && [ "$FORCE" != "--force" ]; then
  skip "$AGAVE_V"
else
  # Normally a no-op: avm has just installed exactly this version. Kept so the
  # pin is enforced rather than assumed, and so a drifted install self-heals.
  sh -c "$(curl -sSfL "https://release.anza.xyz/v$AGAVE_V/install")"
  export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"
fi

say "Done"
cat <<EOF
Add to your shell profile if it is not already there:

  export PATH="\$HOME/.local/share/solana/install/active_release/bin:\$PATH"
  export PATH="\$HOME/.cargo/bin:\$PATH"

Then verify:

  npx tsx packages/cli/src/bin.ts chain doctor
EOF
