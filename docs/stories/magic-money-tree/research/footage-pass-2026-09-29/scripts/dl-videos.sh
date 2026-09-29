#!/usr/bin/env bash
# Sequential, polite download of archive.org originals for the Magic Money Tree film.
# Masters (with their original audio) go to clips/_masters; nothing here is import-ready.
set -u
S="$(cd "$(dirname "$0")" && pwd)"
CLIPS=/mnt/d/badcode-videos/magic-money-tree/clips
MASTERS="$CLIPS/_masters"
RECEIPTS=/home/kai/projects/badcode/badcode/docs/footage
STATUS="$S/dl-status.tsv"
mkdir -p "$MASTERS"
: > "$S/DONE.tmp"; rm -f "$S/DONE"
printf 'id\tscene\tresult\tfile\tbytes\tdeclared_bytes\tmd5_ok\tdeclared_len\n' > "$STATUS"
while read -r ID SCENE; do
  [ -z "${ID:-}" ] && continue
  META="$RECEIPTS/archive.org--$ID.json"
  curl -s --retry 3 "https://archive.org/metadata/$ID" > "$META.tmp"
  if [ "$(head -c 3 "$META.tmp")" = "{}" ] || [ ! -s "$META.tmp" ]; then
    rm -f "$META.tmp"; printf '%s\t%s\tDEAD\t\t\t\t\t\n' "$ID" "$SCENE" >> "$STATUS"; sleep 2; continue
  fi
  mv "$META.tmp" "$META"
  read -r NAME MD5 SIZE LEN < <(python3 - "$META" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); ext=('.mpeg','.mpg','.mp4','.mov','.avi','.ogv','.mkv','.m4v','.webm')
v=[f for f in d['files'] if f['name'].lower().endswith(ext)]
o=[f for f in v if f.get('source')=='original'] or v
f=sorted(o,key=lambda f:int(f.get('size',0)))[-1]
print(f['name'].replace(' ','%20'), f.get('md5','-'), f.get('size','0'), f.get('length','-'))
PY
)
  EXT="${NAME##*.}"; DEST="$MASTERS/$ID.$EXT"
  for TRY in 1 2 3 4; do
    curl -sL -C - --retry 5 --retry-delay 15 -o "$DEST" "https://archive.org/download/$ID/$NAME"
    GOT=$(stat -c %s "$DEST" 2>/dev/null || echo 0)
    [ "$GOT" = "$SIZE" ] && break
    sleep 30
  done
  SUM=$(md5sum "$DEST" | cut -d' ' -f1); OK=no; [ "$SUM" = "$MD5" ] && OK=yes
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ID" "$SCENE" "$([ "$OK" = yes ] && echo OK || echo CHECK)" "$ID.$EXT" "$GOT" "$SIZE" "$OK" "$LEN" >> "$STATUS"
  sleep 3
done < "$S/videos.list"
mv "$S/DONE.tmp" "$S/DONE"
