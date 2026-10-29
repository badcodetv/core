# palette.sh — sourced by cut.sh, panel.sh and remix.sh. Loads ONE STORY's shorts palette.
#
# 🔴 There is no default palette (2026-10-29, design/2026-10-29-style-leak-audit.md §1). Until
# then every short was framed on GPOM's near-black card with its one thin rule, whatever story it
# came from. A palette is the story's look (docs/stories/<story>/look.md, docs/stories/STYLE.md):
# pass it with -C <file>, or set SHORTS_PALETTE. The brand mark text (-T) stays global.
#
# A palette file is plain shell that sets five colours (0xRRGGBB):
#   INK   main text          DIM   secondary text (brand mark, kicker, credits)
#   BG    the card behind the picture
#   RULE  the two thin rules above/below the 16:9 window (set it to BG to hide them)
#   BAR   remix.sh's receipt-card bars
# Existing: palettes/gpom.sh (GPOM's register — what every short used before 2026-10-29).
load_palette() {
  local f=${1:-${SHORTS_PALETTE:-}}
  if [ -z "$f" ]; then
    echo "no palette: pass -C <palette.sh> or set SHORTS_PALETTE — the story's colours, from its" >&2
    echo "docs/stories/<story>/look.md. There is no default palette. Format: scripts/shorts/palette.sh;" >&2
    echo "GPOM's is scripts/shorts/palettes/gpom.sh." >&2
    exit 1
  fi
  [ -f "$f" ] || { echo "no such palette file: $f" >&2; exit 1; }
  unset INK DIM BG RULE BAR
  # shellcheck disable=SC1090
  . "$f"
  local v
  for v in INK DIM BG RULE BAR; do
    [ -n "${!v:-}" ] || { echo "palette $f does not set $v (needs INK DIM BG RULE BAR)" >&2; exit 1; }
  done
  PALETTE_FILE=$f
}
