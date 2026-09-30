#!/usr/bin/env bash
# cut.sh — cut one 9:16 short out of a BadCode master.
#
# The masters on the drive are FULL-RANGE with NO COLOUR TAG (measured 2026-09-18:
# Karen YMIN=0 YMAX=255, Camping YMIN=10 YMAX=248, both color_range=unknown) — the
# exact bug docs/video-fx/delivery.md records against camping.mp4. Every cut here
# converts full->limited for real and tags it, or the shadows crush on upload.
#
# Usage:
#   scripts/shorts/cut.sh -i MASTER -s START -t DUR -o OUT.mp4 [options]
#
#   -i FILE     source master (required)
#   -s TS       start timestamp, e.g. 92.4 or 00:01:32.4   (default 0)
#   -t SECS     duration in seconds                         (default 30)
#   -o FILE     output .mp4                                 (required)
#   -m MODE     slate | crop | full                         (default slate)
#                 slate — 16:9 window on a near-black 9:16 card, hook above,
#                         captions below. Keeps the composition. House default.
#                 crop  — full-bleed centre crop to 9:16. For centred single
#                         figures only; it throws away 68% of the width.
#                 full  — 16:9 letterboxed centre, no text furniture.
#   -p PAN      crop recentre, -1 (left) .. 1 (right)       (default 0)
#   -H TEXT     hook line above the window. Use \n for a line break.
#   -k TEXT     kicker line at the very bottom (e.g. the funnel line)
#   -c FILE     burn captions from an .srt
#   -S N        hook font size                              (default 58)
#   -R RANGE    source luma range: full | limited            (default full)
#   -T TEXT     top brand mark                              (default BADCODE)
#   -L          skip loudness normalisation (faster; for previews)
#   -n          dry run — print the ffmpeg command and exit
set -euo pipefail

SRC=""; START="0"; DUR="30"; OUT=""; MODE="slate"; PAN="0"
HOOK=""; KICKER=""; SRT=""; MARK="BADCODE"; LOUD=1; DRY=0; HSIZE=58
CAPFONT=${BADCODE_CAPFONT:-DejaVu Sans Mono}; CAPSIZE=${BADCODE_CAPSIZE:-46}
SRCRANGE=full

while getopts "i:s:t:o:m:p:H:k:c:T:S:R:Ln" o; do case "$o" in
  i) SRC=$OPTARG;; s) START=$OPTARG;; t) DUR=$OPTARG;; o) OUT=$OPTARG;;
  m) MODE=$OPTARG;; p) PAN=$OPTARG;; H) HOOK=$OPTARG;; k) KICKER=$OPTARG;;
  c) SRT=$OPTARG;; T) MARK=$OPTARG;; S) HSIZE=$OPTARG;; R) SRCRANGE=$OPTARG;;
  L) LOUD=0;; n) DRY=1;;
  *) sed -n '2,30p' "$0" | sed 's/^# \{0,1\}//'; exit 1;;
esac; done

[ -n "$SRC" ] && [ -n "$OUT" ] || { sed -n '2,30p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
[ -f "$SRC" ] || { echo "no such source: $SRC" >&2; exit 1; }

FONT=${BADCODE_FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf}
FONTR=${BADCODE_FONT_R:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf}
[ -f "$FONT" ] || FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
[ -f "$FONTR" ] || FONTR=$FONT

INK=0xE8EDF2          # brand off-white
DIM=0x8A949E          # dim label grey
BG=0x07090B           # near-black card
LINE=0x3A4450         # the one thin light

FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$SRC")
FPS=${FPS:-25/1}

# drawtext escaping. Apostrophes become typographic ' (filtergraph quoting cannot
# carry a raw one, and it reads better anyway). A literal \n becomes a real newline —
# ffmpeg 6.1 drawtext does NOT interpret the two-character sequence (verified 2026-09-18).
esc() {
  printf '%s' "$1" \
    | sed -e "s/'/\xe2\x80\x99/g" -e 's/\\/\\\\/g' -e 's/:/\\:/g' -e 's/%/\\%/g'
}

# ---- colour ----
# 🔴 The conversion goes LAST, not first. Every graphic we draw (the card, the hook
# bars, the text, the captions) is specified in RGB and rasterised full-range, so a
# conversion at the head leaves the furniture outside 16-235 and delivery-qc.sh fails
# the file for exactly the bug it is meant to catch. Verified 2026-09-18.
# So: bring the source into full range, build everything there, convert once at the tail.
case "$SRCRANGE" in
  full)    FIX="setsar=1" ;;                                      # drive default
  limited) FIX="scale=in_range=limited:out_range=full,setsar=1" ;;
  *) echo "unknown source range: $SRCRANGE (use full|limited)" >&2; exit 1 ;;
esac

case "$MODE" in
  crop)
    VF="[0:v]${FIX},crop=w='floor(min(iw\,ih*9/16)/2)*2':h=ih:x='(iw-ow)/2+${PAN}*(iw-ow)/2':y=0,scale=1080:1920:flags=lanczos[v]"
    CAPMARGIN=430 ;;
  full)
    VF="[0:v]${FIX},scale=1080:-2:flags=lanczos[s];color=c=${BG}:s=1080x1920:r=${FPS}[bg];[bg][s]overlay=x=0:y=(H-h)/2:shortest=1[v]"
    CAPMARGIN=430 ;;
  slate)
    # window sits 96px above centre: y 560..1168 on a 1920 canvas.
    VF="[0:v]${FIX},scale=1080:-2:flags=lanczos[s];color=c=${BG}:s=1080x1920:r=${FPS}[bg];[bg][s]overlay=x=0:y=(H-h)/2-96:shortest=1[w]"
    VF="${VF};[w]drawbox=x=0:y=554:w=1080:h=2:color=${LINE}@0.8:t=fill,drawbox=x=0:y=1166:w=1080:h=2:color=${LINE}@0.8:t=fill[v]"
    CAPMARGIN=500 ;;
  *) echo "unknown mode: $MODE" >&2; exit 1;;
esac

CHAIN=""
add() { CHAIN="${CHAIN:+$CHAIN,}$1"; }

# brand mark, top
if [ -n "$MARK" ]; then
  MY=$([ "$MODE" = slate ] && echo 118 || echo 96)
  add "drawtext=fontfile='${FONTR}':text='$(esc "$MARK")':fontcolor=${DIM}:fontsize=34:x=(w-tw)/2:y=${MY}"
fi

# Hook, above the window (slate) or upper third (crop/full). Each \n-separated line
# is its own drawtext so every line is centred on its own bar — drawtext left-aligns
# inside a multi-line block, which looks broken at this size.
if [ -n "$HOOK" ]; then
  HY=$([ "$MODE" = slate ] && echo 250 || echo 190)
  STEP=$(( HSIZE * 9 / 5 ))
  IDX=0
  OLDIFS=$IFS; IFS=$'\n'
  for LINE in $(printf '%s' "$HOOK" | sed 's/\\n/\n/g'); do
    [ -n "$LINE" ] || { IDX=$((IDX+1)); continue; }
    add "drawtext=fontfile='${FONT}':text='$(esc "$LINE")':fontcolor=${INK}:fontsize=${HSIZE}:x=(w-tw)/2:y=$(( HY + IDX * STEP )):box=1:boxcolor=0x000000@0.62:boxborderw=20"
    IDX=$((IDX+1))
  done
  IFS=$OLDIFS
fi

# kicker, bottom
if [ -n "$KICKER" ]; then
  add "drawtext=fontfile='${FONTR}':text='$(esc "$KICKER")':fontcolor=${DIM}:fontsize=36:x=(w-tw)/2:y=h-250"
fi

# Burnt captions. 🔴 ffmpeg converts an .srt into ASS with PlayRes 384x288, so
# force_style margins and sizes are in THAT space, not pixels — MarginV=420 simply
# vanishes off a 1920-tall frame (verified 2026-09-18). So: convert, rewrite the
# play-res to the real frame, and write the house style in real pixels.
if [ -n "$SRT" ]; then
  [ -f "$SRT" ] || { echo "no such subtitle file: $SRT" >&2; exit 1; }
  ASS=$(mktemp --suffix=.ass)
  trap 'rm -f "$ASS"' EXIT
  case "$SRT" in
    *.ass|*.ssa) cp "$SRT" "$ASS" ;;
    *) ffmpeg -y -v error -i "$SRT" "$ASS" ;;
  esac
  sed -i -e 's/^PlayResX:.*/PlayResX: 1080/' -e 's/^PlayResY:.*/PlayResY: 1920/' \
    -e "s|^Style: Default,.*|Style: Default,${CAPFONT},${CAPSIZE},\&H00F2EDE8,\&H00F2EDE8,\&H00000000,\&H80000000,-1,0,0,0,100,100,0,0,1,5,0,2,90,90,${CAPMARGIN},1|" "$ASS"
  add "ass=filename='$(esc "$ASS")'"
fi

# The one real conversion, after all the furniture is drawn.
# 🔴 NOT `scale=in_range=full:out_range=limited` here: with no resize and no format
# change swscale takes a fast path and the squeeze silently does nothing once the
# graph is running full-range-flagged (measured 2026-09-18: YMAX stayed 255). An
# arithmetic LUT cannot be optimised away, and `setparams` then tags without
# re-converting. Verified lossless out of this graph: exactly YMIN=16 / YMAX=235.
add "format=yuv420p"
add "lutyuv=y='16+val*219/255':u='128+(val-128)*224/255':v='128+(val-128)*224/255'"
add "setparams=range=tv:colorspace=bt709:color_primaries=bt709:color_trc=bt709"

VF="${VF};[v]${CHAIN}[vout]"

AF="aresample=48000"
[ "$LOUD" = 1 ] && AF="${AF},loudnorm=I=-14:TP=-1.5:LRA=11"

mkdir -p "$(dirname "$OUT")"

CMD=(ffmpeg -y -hide_banner -v warning -stats
  -ss "$START" -t "$DUR" -i "$SRC"
  -filter_complex "$VF" -map "[vout]" -map 0:a:0? -af "$AF"
  -c:v libx264 -preset slow -crf 19 -profile:v high -level 4.1
  -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709
  -c:a aac -b:a 192k -ar 48000 -ac 2
  -movflags +faststart "$OUT")

if [ "$DRY" = 1 ]; then printf '%q ' "${CMD[@]}"; echo; exit 0; fi
"${CMD[@]}"
echo "→ $OUT"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,pix_fmt,color_range,color_space -of default=nw=1 "$OUT"
