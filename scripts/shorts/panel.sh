#!/usr/bin/env bash
# panel.sh — turn a finished comic panel (or two) into a 9:16 short.
#
# The companion to cut.sh: that one slices film, this one animates stills. Same card,
# same type, same colour discipline (see cut.sh for why the range conversion is a LUT
# at the tail and not a scale at the head).
#
# Usage:
#   scripts/shorts/panel.sh -i PANEL.png [-j SECOND.png] -o OUT.mp4 [options]
#
#   -i FILE   panel image (required)
#   -j FILE   second panel — the frame hard-cuts to it halfway (STYLE SWAP format)
#   -o FILE   output .mp4 (required)
#   -t SECS   duration (default 14)
#   -H TEXT   hook, top. \n breaks a line. The sarcasm.
#   -P TEXT   payoff, bottom. \n breaks a line. The straight line — who did it.
#   -a SECS   when the payoff appears (default: 55% through)
#   -m MODE   cover | slate | auto   (default auto: portrait covers, landscape gets the card)
#   -S N      hook font size (default 56)
#   -T TEXT   brand mark (default BADCODE)
#   -k TEXT   kicker at the foot (default badcode.tv)
#   -n        dry run
set -euo pipefail

P1=""; P2=""; OUT=""; DUR=14; HOOK=""; PAY=""; PAYAT=""; MODE=auto
HSIZE=56; MARK="BADCODE"; KICK="badcode.tv"; DRY=0
while getopts "i:j:o:t:H:P:a:m:S:T:k:n" o; do case "$o" in
  i) P1=$OPTARG;; j) P2=$OPTARG;; o) OUT=$OPTARG;; t) DUR=$OPTARG;;
  H) HOOK=$OPTARG;; P) PAY=$OPTARG;; a) PAYAT=$OPTARG;; m) MODE=$OPTARG;;
  S) HSIZE=$OPTARG;; T) MARK=$OPTARG;; k) KICK=$OPTARG;; n) DRY=1;;
  *) sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; exit 1;;
esac; done
[ -n "$P1" ] && [ -n "$OUT" ] || { sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
[ -f "$P1" ] || { echo "no such panel: $P1" >&2; exit 1; }

FONT=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
FONTR=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
INK=0xE8EDF2; DIM=0x8A949E; BG=0x07090B
FPS=30
[ -n "$PAYAT" ] || PAYAT=$(awk -v d="$DUR" 'BEGIN{printf "%.2f", d*0.55}')
esc() { printf '%s' "$1" | sed -e "s/'/\xe2\x80\x99/g" -e 's/\\/\\\\/g' -e 's/:/\\:/g' -e 's/%/\\%/g'; }

# auto mode: a portrait panel fills the frame, a landscape one would lose 60% of its width
pick_mode() {
  local a; a=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$1")
  awk -F, -v m="$MODE" '{r=$1/$2; if(m!="auto") print m; else print (r<0.85 ? "cover" : "slate")}' <<<"$a"
}
M=$(pick_mode "$P1")

# one panel -> a slow push; the crop/scale differs per mode but the output is always 1080x1920
build_one() {  # $1 idx, $2 file, $3 seconds
  local i=$1 f=$2 s=$3 frames
  frames=$(awk -v s="$s" -v f="$FPS" 'BEGIN{printf "%d", s*f}')
  if [ "$M" = cover ]; then
    echo "[${i}:v]scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,zoompan=z='min(zoom+0.00035,1.12)':d=${frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=${FPS},setsar=1[p${i}]"
  else
    echo "[${i}:v]scale=1400:-2:flags=lanczos,zoompan=z='min(zoom+0.00035,1.12)':d=${frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x608:fps=${FPS},setsar=1[s${i}];color=c=${BG}:s=1080x1920:r=${FPS}:d=${s}[c${i}];[c${i}][s${i}]overlay=x=0:y=(H-h)/2-96:shortest=1,drawbox=x=0:y=554:w=1080:h=2:color=0x3A4450@0.8:t=fill,drawbox=x=0:y=1166:w=1080:h=2:color=0x3A4450@0.8:t=fill[p${i}]"
  fi
}

INPUTS=(-loop 1 -t "$DUR" -i "$P1")
if [ -n "$P2" ]; then
  [ -f "$P2" ] || { echo "no such panel: $P2" >&2; exit 1; }
  H1=$(awk -v d="$DUR" 'BEGIN{printf "%.3f", d/2}')
  INPUTS=(-loop 1 -t "$H1" -i "$P1" -loop 1 -t "$H1" -i "$P2")
  G="$(build_one 0 "$P1" "$H1");$(build_one 1 "$P2" "$H1");[p0][p1]concat=n=2:v=1:a=0[v]"
else
  G="$(build_one 0 "$P1" "$DUR");[p0]null[v]"
fi

CHAIN=""; add() { CHAIN="${CHAIN:+$CHAIN,}$1"; }
add "drawtext=fontfile='${FONTR}':text='$(esc "$MARK")':fontcolor=${INK}:fontsize=32:x=(w-tw)/2:y=96:box=1:boxcolor=0x000000@0.55:boxborderw=14"

if [ -n "$HOOK" ]; then
  IDX=0; STEP=$(( HSIZE * 9 / 5 )); OLDIFS=$IFS; IFS=$'\n'
  for L in $(printf '%s' "$HOOK" | sed 's/\\n/\n/g'); do
    [ -n "$L" ] || { IDX=$((IDX+1)); continue; }
    add "drawtext=fontfile='${FONT}':text='$(esc "$L")':fontcolor=${INK}:fontsize=${HSIZE}:x=(w-tw)/2:y=$(( 190 + IDX*STEP )):box=1:boxcolor=0x000000@0.66:boxborderw=20"
    IDX=$((IDX+1))
  done; IFS=$OLDIFS
fi

# The payoff is the straight line and it arrives late, on its own, in the care register.
if [ -n "$PAY" ]; then
  PS=$(( HSIZE * 4 / 5 )); IDX=0; STEP=$(( PS * 9 / 5 )); N=$(printf '%s' "$PAY" | sed 's/\\n/\n/g' | grep -c .)
  BASE=$(( 1560 - (N-1)*STEP )); OLDIFS=$IFS; IFS=$'\n'
  for L in $(printf '%s' "$PAY" | sed 's/\\n/\n/g'); do
    [ -n "$L" ] || { IDX=$((IDX+1)); continue; }
    add "drawtext=fontfile='${FONT}':text='$(esc "$L")':fontcolor=${INK}:fontsize=${PS}:x=(w-tw)/2:y=$(( BASE + IDX*STEP )):box=1:boxcolor=0x000000@0.7:boxborderw=18:enable='gte(t,${PAYAT})'"
    IDX=$((IDX+1))
  done; IFS=$OLDIFS
fi

[ -n "$KICK" ] && add "drawtext=fontfile='${FONTR}':text='$(esc "$KICK")':fontcolor=${INK}:fontsize=34:x=(w-tw)/2:y=h-250:box=1:boxcolor=0x000000@0.55:boxborderw=14"

# same tail as cut.sh: arithmetic squeeze, then tag without re-converting
add "format=yuv420p"
add "lutyuv=y='16+val*219/255':u='128+(val-128)*224/255':v='128+(val-128)*224/255'"
add "setparams=range=tv:colorspace=bt709:color_primaries=bt709:color_trc=bt709"

VF="${G};[v]${CHAIN}[vout]"
mkdir -p "$(dirname "$OUT")"
CMD=(ffmpeg -y -hide_banner -v warning "${INPUTS[@]}"
  -f lavfi -t "$DUR" -i anullsrc=channel_layout=stereo:sample_rate=48000
  -filter_complex "$VF" -map "[vout]" -map "$([ -n "$P2" ] && echo 2 || echo 1):a"
  -c:v libx264 -preset medium -crf 19 -profile:v high -level 4.1 -r "$FPS"
  -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709
  -c:a aac -b:a 128k -ar 48000 -shortest -movflags +faststart "$OUT")
if [ "$DRY" = 1 ]; then printf '%q ' "${CMD[@]}"; echo; exit 0; fi
"${CMD[@]}"
echo "→ $OUT  [$M]"
