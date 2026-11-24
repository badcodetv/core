#!/usr/bin/env bash
# Sets up the demo's two folders inside a Bob container. Safe to run every time.
#   /project/work/.demo/main = a read-only worktree of origin/main (code, pool, cabinet, rules)
#   /project/work/.demo/live = the demo/live branch (the days and the government; workers commit and push here)
# The demo never uses /project/work/core (shared with other chats) or the simulation's folders.
#   git -C /project/work/core show origin/main:scripts/demo/bob-setup.sh | bash
set -euo pipefail
W=/project/work/.demo
REPO=https://github.com/badcodetv/core.git
mkdir -p "$W"
[ -d "$W/live/.git" ] || git clone --quiet "$REPO" "$W/live"
cd "$W/live"
git fetch --quiet origin --prune
git checkout --quiet -B demo/live origin/demo/live
git reset --quiet --hard origin/demo/live
git clean --quiet -fd
git worktree remove --force "$W/main" >/dev/null 2>&1 || rm -rf "$W/main"
git worktree prune
git worktree add --quiet --detach "$W/main" origin/main
echo "ready: main $(git -C "$W/main" log -1 --format=%h), live $(git log -1 --format=%h), today $(TZ=Europe/London date +%F)"
