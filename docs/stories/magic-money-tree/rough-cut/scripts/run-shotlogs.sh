#!/usr/bin/env bash
# Index every picture-only film that has no shotlog yet, four at a time. Re-run to pick up new conforms.
# LIBRARY=1 also indexes clips/_library (reference films the edit plan does not use).
cd "$(dirname "$0")"
SKIP=(-not -path '*/_masters/*')
[ "${LIBRARY:-}" = 1 ] || SKIP+=(-not -path '*/_library/*')
find /mnt/d/badcode-videos/magic-money-tree/clips -name '*.picture-only.mov' "${SKIP[@]}" | sort |
while read -r f; do id=$(basename "$f" .picture-only.mov); [ -s "../shotlogs/$id.tsv" ] || echo "$f"; done |
xargs -P4 -I{} python3 shotlog.py {}
