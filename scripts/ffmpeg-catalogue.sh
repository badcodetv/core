#!/usr/bin/env bash
# Re-harvest the live ffmpeg inventory that docs/video-fx/ffmpeg-catalogue.md is written against.
#
#   ./scripts/ffmpeg-catalogue.sh            # summary — run this after any ffmpeg upgrade
#   ./scripts/ffmpeg-catalogue.sh --all      # every video filter, one per line, with its blurb
#   ./scripts/ffmpeg-catalogue.sh --frei0r   # just the frei0r plugin names
#   ./scripts/ffmpeg-catalogue.sh --has NAME # is this filter present? exit 0/1
#
# The counts this prints are the check on the catalogue. If they have moved, the doc is stale.
set -euo pipefail

vfilters() { ffmpeg -hide_banner -filters 2>/dev/null | awk '$3 ~ /V->V|VV->V|N->V|\|->V/'; }

case "${1:-}" in
  --all)
    vfilters | sed 's/^ *//' ;;
  --frei0r)
    ls /usr/lib/frei0r-1/ 2>/dev/null | sed 's/\.so$//' | sort ;;
  --has)
    n="${2:?usage: --has FILTERNAME}"
    if vfilters | awk -v n="$n" '$2==n{f=1} END{exit !f}'; then echo "present: $n"; else echo "ABSENT: $n" >&2; exit 1; fi ;;
  *)
    echo "ffmpeg:        $(ffmpeg -hide_banner -version 2>/dev/null | head -1 | cut -d' ' -f3)"
    echo "all filters:   $(ffmpeg -hide_banner -filters 2>/dev/null | tail -n +9 | wc -l)"
    echo "video filters: $(vfilters | wc -l)"
    echo "frei0r plugins:$(ls /usr/lib/frei0r-1/ 2>/dev/null | wc -l)"
    echo "enabled libs:  $(ffmpeg -hide_banner -version 2>/dev/null | grep -o '\-\-enable-[a-z0-9]*' | tr '\n' ' ')"
    echo
    echo "Catalogue: docs/video-fx/ffmpeg-catalogue.md  (Premiere's twin: docs/premiere/effects-catalogue.md)"
    ;;
esac
