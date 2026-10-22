#!/usr/bin/env bash
# sheet-stills.sh <frame-id> [scene=D]: a 2-column labelled contact sheet of every still option for one frame,
# written beside them as <frame>-sheet.jpg. Prints the file list and md5 duplicates.
set -euo pipefail
F=$1; SC=${2:-D}
D=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/$SC/stills
cd "$D"
files=( $(ls ${F}-r*.jpg 2>/dev/null | grep -v sheet | grep -v STRAY) )
md5sum "${files[@]}" | sort | uniq -w32 -D || true
args=(); fl=""; n=${#files[@]}
for i in "${!files[@]}"; do args+=(-i "${files[$i]}"); fl+="[$i]scale=640:358,drawtext=text='${files[$i]%.jpg}':x=8:y=8:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6[v$i];"; done
cols=2; rows=$(( (n+1)/2 ))
lay=""; for i in $(seq 0 $((n-1))); do x=$(( (i%cols)*640 )); y=$(( (i/cols)*358 )); lay+="${x}_${y}|"; done
if [ $n -eq 1 ]; then ffmpeg -v error -y "${args[@]}" -filter_complex "${fl}[v0]copy" "$F-sheet.jpg"
else ins=""; for i in $(seq 0 $((n-1))); do ins+="[v$i]"; done
ffmpeg -v error -y "${args[@]}" -filter_complex "${fl}${ins}xstack=inputs=$n:layout=${lay%|}:fill=black" "$F-sheet.jpg"; fi
echo "$D/$F-sheet.jpg  (${files[*]})"
