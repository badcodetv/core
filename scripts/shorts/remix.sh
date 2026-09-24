#!/usr/bin/env bash
# remix.sh — build a two-part REMIX short: the record, then our frame.
#
# The third tool beside cut.sh (film) and panel.sh (stills). It makes the format in
# docs/marketing/shorts-karen-camping.md §12: part A is the REAL thing (archive footage,
# or a receipt card carrying a real figure); part B is a frame from Karen or Camping.
#
# Everything cut.sh learned applies unchanged and is reproduced here:
#   * the range conversion is an arithmetic LUT at the TAIL, never a scale at the head
#     (swscale fast-paths the squeeze away once the graph is running full-range);
#   * drawtext does not interpret the two-character sequence \n — only a real newline;
#   * every hook line is its own centred drawtext, because drawtext left-aligns blocks.
#
# Audio: 🔴 archive audio is ALWAYS stripped (visuals and soundtrack carry different
# licences). The short's audio is our film's, and it starts UNDER part A — so the viewer
# hears the scene before they see it, and the cut lands on sound already running.
#
# Usage:
#   scripts/shorts/remix.sh -b OURFILM -B START [-e DUR] -o OUT.mp4
#                           { -a ARCHIVE -A START [-d DUR] | -c 'LINE1|LINE2|...' }
#                           [-g '1997:3.5|2024:7.7'] [-H 'HOOK OVER A'] [-P 'PAYOFF OVER B']
#                           [-r 'credit string'] [-k kicker] [-R full|limited] [-n]
#
#   -b FILE   our master (Karen / Camping)              (required)
#   -B TS     in-point in our master, seconds           (required)
#   -e SECS   duration of part B                        (default 16)
#   -a FILE   archive source for part A
#   -A TS     in-point in the archive source
#   -d SECS   duration of part A                        (default 10)
#   -c TEXT   receipt card instead of archive: '|'-separated lines, first line is the label
#   -g SPEC   bars on the card: 'label:value|label:value'  (value is a number)
#   -H TEXT   hook burnt over part A.  \n breaks a line
#   -P TEXT   payoff burnt over part B. \n breaks a line
#   -r TEXT   credit / source line, small, under the picture. 🔴 required for any
#             attribution licence (CC-BY, OGL, OPL) — the clip does not ship without it
#   -k TEXT   kicker at the foot                        (default badcode.tv)
#   -T TEXT   brand mark, top                           (default BADCODE)
#   -S N      hook font size                            (default 56)
#   -R RANGE  luma range of OUR master: full | limited  (default full — the drive default)
#   -n        dry run
set -euo pipefail

OURS=""; BIN=""; BDUR=16; ARC=""; AIN=0; ADUR=10; CARD=""; BARS=""
HOOK=""; PAY=""; CREDIT=""; KICK="badcode.tv"; MARK="BADCODE"; HSIZE=56; SRCRANGE=full; DRY=0; OUT=""
while getopts "b:B:e:a:A:d:c:g:H:P:r:k:T:S:R:o:n" o; do case "$o" in
  b) OURS=$OPTARG;; B) BIN=$OPTARG;; e) BDUR=$OPTARG;;
  a) ARC=$OPTARG;; A) AIN=$OPTARG;; d) ADUR=$OPTARG;;
  c) CARD=$OPTARG;; g) BARS=$OPTARG;;
  H) HOOK=$OPTARG;; P) PAY=$OPTARG;; r) CREDIT=$OPTARG;; k) KICK=$OPTARG;;
  T) MARK=$OPTARG;; S) HSIZE=$OPTARG;; R) SRCRANGE=$OPTARG;; o) OUT=$OPTARG;; n) DRY=1;;
  *) sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'; exit 1;;
esac; done

[ -n "$OURS" ] && [ -n "$BIN" ] && [ -n "$OUT" ] || { sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
[ -n "$ARC" ] || [ -n "$CARD" ] || { echo "need either -a ARCHIVE or -c CARD" >&2; exit 1; }
[ -f "$OURS" ] || { echo "no such master: $OURS" >&2; exit 1; }

FONT=${BADCODE_FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf}
FONTR=${BADCODE_FONT_R:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf}
[ -f "$FONT" ]  || FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
[ -f "$FONTR" ] || FONTR=$FONT

INK=0xE8EDF2; DIM=0x8A949E; BG=0x07090B; LINE=0x3A4450; BAR=0x6E7A86
FPS=25
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

esc() { printf '%s' "$1" | sed -e "s/'/\xe2\x80\x99/g" -e 's/\\/\\\\/g' -e 's/:/\\:/g' -e 's/%/\\%/g'; }

# hook/payoff/credit/mark/kicker furniture, shared by both halves
furniture() { # $1 = hook text, $2 = y of picture bottom
  local TXT=$1 PICBOT=$2 C="" IDX=0 STEP=$(( HSIZE * 9 / 5 )) L
  add2() { C="${C:+$C,}$1"; }
  [ -n "$MARK" ]   && add2 "drawtext=fontfile='${FONTR}':text='$(esc "$MARK")':fontcolor=${DIM}:fontsize=34:x=(w-tw)/2:y=118"
  if [ -n "$TXT" ]; then
    local OLDIFS=$IFS; IFS=$'\n'
    for L in $(printf '%s' "$TXT" | sed 's/\\n/\n/g'); do
      [ -n "$L" ] && add2 "drawtext=fontfile='${FONT}':text='$(esc "$L")':fontcolor=${INK}:fontsize=${HSIZE}:x=(w-tw)/2:y=$(( 250 + IDX * STEP )):box=1:boxcolor=0x000000@0.62:boxborderw=20"
      IDX=$((IDX+1))
    done
    IFS=$OLDIFS
  fi
  [ -n "$CREDIT" ] && add2 "drawtext=fontfile='${FONTR}':text='$(esc "$CREDIT")':fontcolor=${DIM}:fontsize=25:x=(w-tw)/2:y=$(( PICBOT + 34 ))"
  [ -n "$KICK" ]   && add2 "drawtext=fontfile='${FONTR}':text='$(esc "$KICK")':fontcolor=${DIM}:fontsize=36:x=(w-tw)/2:y=h-250"
  printf '%s' "$C"
}

# ---------- part A ----------
if [ -n "$ARC" ]; then
  [ -f "$ARC" ] || { echo "no such archive source: $ARC" >&2; exit 1; }
  # archive is typically 4:3 and often interlaced; fit it to 1080 wide on the card.
  # 🔴 csv=p=0 can come back with a trailing comma on a multi-field stream record, and
  # "4:3," silently poisons the arithmetic below. Strip to digits and colons, first line only.
  AW=$(ffprobe -v error -select_streams v:0 -show_entries stream=width  -of csv=p=0 "$ARC" | head -1 | tr -cd '0-9')
  AH=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$ARC" | head -1 | tr -cd '0-9')
  ADAR=$(ffprobe -v error -select_streams v:0 -show_entries stream=display_aspect_ratio -of csv=p=0 "$ARC" 2>/dev/null | head -1 | tr -cd '0-9:')
  case "$ADAR" in ''|0:1|:*|*:) ADAR="${AW}:${AH}" ;; esac
  [ "${ADAR%:*}" -gt 0 ] 2>/dev/null || ADAR="${AW}:${AH}"
  PH=$(( 1080 * ${ADAR#*:} / ${ADAR%:*} )); PH=$(( PH / 2 * 2 ))
  [ "$PH" -gt 1180 ] && PH=1180
  PY=$(( (1920 - PH) / 2 - 96 )); PBOT=$(( PY + PH ))
  FIELD=$(ffprobe -v error -select_streams v:0 -show_entries stream=field_order -of csv=p=0 "$ARC" || true)
  DEINT=""; case "$FIELD" in tt|bb|tb|bt) DEINT="yadif=1," ;; esac
  AVF="[0:v]${DEINT}scale=1080:${PH}:flags=lanczos,setsar=1[p];color=c=${BG}:s=1080x1920:r=${FPS}[bg];[bg][p]overlay=x=0:y=${PY}:shortest=1[w]"
  AVF="${AVF};[w]drawbox=x=0:y=$((PY-6)):w=1080:h=2:color=${LINE}@0.8:t=fill,drawbox=x=0:y=$((PBOT+4)):w=1080:h=2:color=${LINE}@0.8:t=fill[q]"
  AF_CHAIN=$(furniture "$HOOK" "$PBOT")
  AVF="${AVF};[q]${AF_CHAIN}[vout]"
  ffmpeg -y -hide_banner -v warning -ss "$AIN" -t "$ADUR" -i "$ARC" -an \
    -filter_complex "$AVF" -map "[vout]" -r $FPS -c:v ffv1 -pix_fmt yuv420p "$TMP/a.mkv"
else
  # ---------- the receipt card ----------
  PY=470; PH=700; PBOT=$(( PY + PH ))
  CC=""; addc() { CC="${CC:+$CC,}$1"; }
  addc "drawbox=x=0:y=$((PY-6)):w=1080:h=2:color=${LINE}@0.8:t=fill"
  addc "drawbox=x=0:y=$((PBOT+4)):w=1080:h=2:color=${LINE}@0.8:t=fill"
  IDX=0; OLDIFS=$IFS; IFS='|'
  for L in $CARD; do
    if [ "$IDX" = 0 ]; then
      addc "drawtext=fontfile='${FONTR}':text='$(esc "$L")':fontcolor=${DIM}:fontsize=32:x=(w-tw)/2:y=$((PY+40))"
    else
      addc "drawtext=fontfile='${FONT}':text='$(esc "$L")':fontcolor=${INK}:fontsize=76:x=(w-tw)/2:y=$((PY + 40 + IDX*110))"
    fi
    IDX=$((IDX+1))
  done
  IFS=$OLDIFS
  if [ -n "$BARS" ]; then
    MAXV=0; OLDIFS=$IFS; IFS='|'; for S in $BARS; do V=${S#*:}; awk "BEGIN{exit !($V>$MAXV)}" && MAXV=$V; done; IFS=$OLDIFS
    N=0; OLDIFS=$IFS; IFS='|'
    for S in $BARS; do
      LB=${S%%:*}; V=${S#*:}
      BW=$(awk "BEGIN{printf \"%d\", 660*$V/$MAXV}")
      BYY=$(( PY + 170 + N*150 ))
      addc "drawbox=x=180:y=${BYY}:w=${BW}:h=62:color=${BAR}@0.95:t=fill"
      addc "drawtext=fontfile='${FONTR}':text='$(esc "$LB")':fontcolor=${DIM}:fontsize=36:x=180:y=$((BYY-48))"
      addc "drawtext=fontfile='${FONT}':text='$(esc "$V")x':fontcolor=${INK}:fontsize=52:x=$((180+BW+20)):y=$((BYY+4))"
      N=$((N+1))
    done
    IFS=$OLDIFS
  fi
  CF=$(furniture "$HOOK" "$PBOT")
  ffmpeg -y -hide_banner -v warning -f lavfi -t "$ADUR" -i "color=c=${BG}:s=1080x1920:r=${FPS}" -an \
    -vf "${CC},${CF}" -c:v ffv1 -pix_fmt yuv420p "$TMP/a.mkv"
fi

# ---------- part B — our frame, standard slate geometry ----------
case "$SRCRANGE" in
  full)    FIX="setsar=1" ;;
  limited) FIX="scale=in_range=limited:out_range=full,setsar=1" ;;
  *) echo "unknown range: $SRCRANGE" >&2; exit 1 ;;
esac
BVF="[0:v]${FIX},scale=1080:-2:flags=lanczos[s];color=c=${BG}:s=1080x1920:r=${FPS}[bg];[bg][s]overlay=x=0:y=(H-h)/2-96:shortest=1[w]"
BVF="${BVF};[w]drawbox=x=0:y=554:w=1080:h=2:color=${LINE}@0.8:t=fill,drawbox=x=0:y=1166:w=1080:h=2:color=${LINE}@0.8:t=fill[q]"
BF=$(CREDIT="" furniture "$PAY" 1166)
BVF="${BVF};[q]${BF}[vout]"
ffmpeg -y -hide_banner -v warning -ss "$BIN" -t "$BDUR" -i "$OURS" -an \
  -filter_complex "$BVF" -map "[vout]" -r $FPS -c:v ffv1 -pix_fmt yuv420p "$TMP/b.mkv"

# ---------- audio: our film's, running UNDER part A ----------
TOTAL=$(awk "BEGIN{print $ADUR + $BDUR}")
ASTART=$(awk "BEGIN{s=$BIN-$ADUR; if(s<0)s=0; print s}")
ffmpeg -y -hide_banner -v warning -ss "$ASTART" -t "$TOTAL" -i "$OURS" -vn \
  -af "aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11,apad" -t "$TOTAL" -c:a pcm_s16le "$TMP/aud.wav"

# ---------- join, convert range once, tag ----------
printf "file '%s'\nfile '%s'\n" "$TMP/a.mkv" "$TMP/b.mkv" > "$TMP/list"
LUT="format=yuv420p,lutyuv=y='16+val*219/255':u='128+(val-128)*224/255':v='128+(val-128)*224/255',setparams=range=tv:colorspace=bt709:color_primaries=bt709:color_trc=bt709"
mkdir -p "$(dirname "$OUT")"
CMD=(ffmpeg -y -hide_banner -v warning -stats -f concat -safe 0 -i "$TMP/list" -i "$TMP/aud.wav"
  -filter_complex "[0:v]${LUT}[vout]" -map "[vout]" -map 1:a -shortest
  -c:v libx264 -preset slow -crf 19 -profile:v high -level 4.1
  -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709
  -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart "$OUT")
if [ "$DRY" = 1 ]; then printf '%q ' "${CMD[@]}"; echo; exit 0; fi
"${CMD[@]}"
echo "→ $OUT"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,pix_fmt,color_range,color_space -show_entries format=duration -of default=nw=1 "$OUT"
