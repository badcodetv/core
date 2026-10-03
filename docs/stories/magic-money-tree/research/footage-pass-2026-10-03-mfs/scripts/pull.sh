#!/usr/bin/env bash
# Money For Something: fetch the archive.org films already cleared in ../../../footage.md and
# conform each to a picture-only ProRes file beside Jack's Premiere project.
# Same method as footage-pass-2026-09-29 (md5 against archive.org, idet before any deinterlace,
# audio always dropped). One change: ProRes 422 LT, not HQ, because this folder is on OneDrive.
set -u
S="$(cd "$(dirname "$0")" && pwd)"
LIST="${1:-$S/videos.list}"
CLIPS="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/clips"
MASTERS="$CLIPS/_masters"
RECEIPTS="$(cd "$S/../../../../../footage" && pwd)"
STATUS="$S/pull-status.tsv"
mkdir -p "$MASTERS"
[ -f "$STATUS" ] || printf 'id\tscene\tmd5_ok\tmaster_bytes\tfilter\tmaster_s\tconform_s\tconform_bytes\tresult\tconform_file\n' > "$STATUS"
while read -r ID SCENE; do
  [ -z "${ID:-}" ] && continue
  grep -q "^$ID	.*	OK	" "$STATUS" && continue
  META="$RECEIPTS/archive.org--$ID.json"
  curl -s --retry 3 "https://archive.org/metadata/$ID" > "$META.tmp"
  if [ "$(head -c 3 "$META.tmp")" = "{}" ] || [ ! -s "$META.tmp" ]; then
    rm -f "$META.tmp"; printf '%s\t%s\t\t\t\t\t\t\tDEAD\t\n' "$ID" "$SCENE" >> "$STATUS"; continue
  fi
  [ -f "$META" ] && rm -f "$META.tmp" || mv "$META.tmp" "$META"
  read -r NAME MD5 SIZE < <(python3 - "$META" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); ext=('.mpeg','.mpg','.mp4','.mov','.avi','.ogv','.mkv','.m4v','.webm')
v=[f for f in d['files'] if f['name'].lower().endswith(ext)]
o=[f for f in v if f.get('source')=='original'] or v
f=sorted(o,key=lambda f:int(f.get('size',0)))[-1]
print(f['name'].replace(' ','%20'), f.get('md5','-'), f.get('size','0'))
PY
)
  SRC="$MASTERS/$ID.${NAME##*.}"
  for TRY in 1 2 3 4; do
    curl -sL -C - --retry 5 --retry-delay 15 -o "$SRC" "https://archive.org/download/$ID/$NAME"
    GOT=$(stat -c %s "$SRC" 2>/dev/null || echo 0); [ "$GOT" = "$SIZE" ] && break; sleep 30
  done
  OK=no; [ "$(md5sum "$SRC" | cut -d' ' -f1)" = "$MD5" ] && OK=yes
  if [ "$OK" != yes ]; then printf '%s\t%s\tno\t%s\t\t\t\t\tCHECK\t\n' "$ID" "$SCENE" "$GOT" >> "$STATUS"; continue; fi
  mkdir -p "$CLIPS/$SCENE"; DST="$CLIPS/$SCENE/$ID.picture-only.mov"
  IFS='|' read -r FPS AFPS < <(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,avg_frame_rate -of csv=p=0:s='|' "$SRC" | head -1)
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SRC")
  T=0; P=0
  for FR in 0.2 0.5 0.8; do
    SS=$(python3 -c "print(max(0,float('$DUR')*$FR))")
    L=$(ffmpeg -nostdin -hide_banner -nostats -ss "$SS" -t 8 -i "$SRC" -an -vf idet -f null - 2>&1 | grep 'Multi frame detection' | tail -1)
    a=$(echo "$L" | sed -n 's/.*TFF: *\([0-9]*\).*/\1/p'); b=$(echo "$L" | sed -n 's/.*BFF: *\([0-9]*\).*/\1/p'); c=$(echo "$L" | sed -n 's/.*Progressive: *\([0-9]*\).*/\1/p')
    T=$((T+${a:-0}+${b:-0})); P=$((P+${c:-0}))
  done
  VF="setfield=prog"; python3 -c "import sys;t=$T;p=$P;sys.exit(0 if t+p and t/(t+p)>0.25 else 1)" && VF="yadif=1"
  RATE=(); [ "$FPS" != "$AFPS" ] && [ "$AFPS" != "0/0" ] && RATE=(-r "$AFPS")
  ffmpeg -nostdin -hide_banner -nostats -loglevel error -y "${RATE[@]}" -i "$SRC" -map 0:v:0 -an -vf "$VF" \
    -c:v prores_ks -profile:v 1 -vendor apl0 -pix_fmt yuv422p10le "$DST.part.mov" && mv "$DST.part.mov" "$DST"
  CD=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$DST" 2>/dev/null || echo 0)
  CB=$(stat -c %s "$DST" 2>/dev/null || echo 0); RES=FAILED
  python3 -c "import sys;sys.exit(0 if abs(float('$CD' or 0)-float('$DUR'))<1.5 else 1)" && RES=OK
  printf '%s\t%s\tyes\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ID" "$SCENE" "$GOT" "$VF" "$DUR" "$CD" "$CB" "$RES" "$SCENE/$ID.picture-only.mov" >> "$STATUS"
done < "$LIST"
touch "$S/PULL_DONE"
