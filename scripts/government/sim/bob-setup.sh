#!/usr/bin/env bash
# Sets up the simulation's two folders inside a Bob container. Safe to run every time.
#   /project/work/.gov-sim/main = a read-only worktree of origin/main (code, pool, rules)
#   /project/work/.gov-sim/live = the simulation/live branch (issue files; workers commit and push here)
# The simulation never uses /project/work/core, which other chats share.
# Run it straight from main without checking anything out:
#   git -C /project/work/core show origin/main:scripts/government/sim/bob-setup.sh | bash
set -euo pipefail
W=/project/work/.gov-sim
REPO=https://github.com/badcodetv/core.git
mkdir -p "$W"
[ -d "$W/live/.git" ] || git clone --quiet "$REPO" "$W/live"
cd "$W/live"
git fetch --quiet origin --prune
git checkout --quiet -B simulation/live origin/simulation/live
git reset --quiet --hard origin/simulation/live
git clean --quiet -fd
git worktree remove --force "$W/main" >/dev/null 2>&1 || rm -rf "$W/main"
git worktree prune
git worktree add --quiet --detach "$W/main" origin/main
echo "ready: main $(git -C "$W/main" log -1 --format=%h), live $(git log -1 --format=%h), today $(TZ=Europe/London date +%F)"
