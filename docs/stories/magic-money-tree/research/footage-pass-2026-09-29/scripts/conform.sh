#!/usr/bin/env bash
# Conform every verified master to a picture-only ProRes file in its scene folder.
# Deinterlace only when measured (idet), never on the flag alone. Audio is always dropped.
set -u
S="$(cd "$(dirname "$0")" && pwd)"
CLIPS=/mnt/d/badcode-videos/magic-money-tree/clips
MASTERS="$CLIPS/_masters"
OUT="$S/conform-status.tsv"
[ -f "$OUT" ] || printf 'id\tscene\tmaster\tcoded\tsar\tfps\tflag\tinterlaced_share\tfilter\tmaster_s\tconform_s\tconform_bytes\tresult\tconform_file\n' > "$OUT"
conform_one() {  # id scene masterpath
  local ID="$1" SCENE="$2" SRC="$3"
  local DST="$CLIPS/$SCENE/$ID.picture-only.mov"
  grep -q "^$ID	" "$OUT" && return 0
  mkdir -p "$CLIPS/$SCENE"
  local W H SAR FPS AFPS FLAG DUR
  IFS='|' read -r W H SAR FPS AFPS FLAG < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,sample_aspect_ratio,r_frame_rate,avg_frame_rate,field_order -of csv=p=0:s='|' "$SRC" | head -1)
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SRC")
  local T=0 P=0 X=0
  for FR in 0.2 0.5 0.8; do
    local SS; SS=$(python3 -c "print(max(0,float('$DUR')*$FR))")
    local L; L=$(ffmpeg -nostdin -hide_banner -nostats -ss "$SS" -t 8 -i "$SRC" -an -vf idet -f null - 2>&1 | grep 'Multi frame detection' | tail -1)
    local a b c; a=$(echo "$L" | sed -n 's/.*TFF: *\([0-9]*\).*/\1/p'); b=$(echo "$L" | sed -n 's/.*BFF: *\([0-9]*\).*/\1/p'); c=$(echo "$L" | sed -n 's/.*Progressive: *\([0-9]*\).*/\1/p')
    T=$((T+${a:-0}+${b:-0})); P=$((P+${c:-0}))
  done
  local SHARE; SHARE=$(python3 -c "t=$T;p=$P;print(round(t/(t+p),2) if t+p else 0)")
  local VF="setfield=prog"; python3 -c "import sys;sys.exit(0 if $SHARE>0.25 else 1)" && VF="yadif=1"
  local RATE=(); [ "$FPS" != "$AFPS" ] && [ "$AFPS" != "0/0" ] && RATE=(-r "$AFPS")
  ffmpeg -nostdin -hide_banner -nostats -loglevel error -y "${RATE[@]}" -i "$SRC" -map 0:v:0 -an -vf "$VF" \
    -c:v prores_ks -profile:v 3 -vendor apl0 -pix_fmt yuv422p10le "$DST.part.mov" \
    && mv "$DST.part.mov" "$DST"
  local CD CB RES=FAILED
  CD=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$DST" 2>/dev/null || echo 0)
  CB=$(stat -c %s "$DST" 2>/dev/null || echo 0)
  python3 -c "import sys;sys.exit(0 if abs(float('$CD' or 0)-float('$DUR'))<1.5 else 1)" && RES=OK
  printf '%s\t%s\t%s\t%sx%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ID" "$SCENE" "$(basename "$SRC")" "$W" "$H" "$SAR" "$AFPS" "$FLAG" "$SHARE" "$VF" "$DUR" "$CD" "$CB" "$RES" "$SCENE/$ID.picture-only.mov" >> "$OUT"
}
# the two masters that were already on disk before this pass
conform_one gov.fdr.25.4 s01-dunkirk "$CLIPS/s01-dunkirk/gov.fdr.25.4.mpeg"
conform_one gov.ntis.ava06858vnb1 s05-britain-paid "$CLIPS/s05-britain-paid/ava06858vnb1.mpeg"
while :; do
  PENDING=0
  while IFS=$'\t' read -r ID SCENE RESULT FILE REST; do
    [ "$ID" = id ] && continue
    [ "$RESULT" = OK ] || continue
    grep -q "^$ID	" "$OUT" || { conform_one "$ID" "$SCENE" "$MASTERS/$FILE"; PENDING=1; }
  done < "$S/dl-status.tsv"
  if [ -f "$S/DONE" ] && [ "$PENDING" = 0 ]; then break; fi
  sleep 20
done
touch "$S/CONFORM_DONE"
