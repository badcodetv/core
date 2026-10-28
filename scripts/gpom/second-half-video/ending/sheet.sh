#!/usr/bin/env bash
# Contact sheet of up to 4 stills (2x2, labelled by filename) for picking: sheet.sh out.jpg a.jpg b.jpg [c.jpg d.jpg]
set -euo pipefail
out=$1; shift
args=(); f=""; i=0
for p in "$@"; do args+=(-i "$p"); n=$(basename "$p" .jpg); f+="[$i]scale=688:384,drawtext=text='$n':x=10:y=10:fontsize=24:fontcolor=white:box=1:boxcolor=black@0.6[v$i];"; i=$((i+1)); done
while [ $i -lt 4 ]; do args+=(-f lavfi -i color=black:s=688x384:d=1); f+="[$i]null[v$i];"; i=$((i+1)); done
ffmpeg -v error -y "${args[@]}" -filter_complex "${f}[v0][v1][v2][v3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0" -frames:v 1 "$out"
