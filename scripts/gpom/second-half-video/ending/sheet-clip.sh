#!/usr/bin/env bash
# sheet-clip.sh <clip.mp4>: an 8-frame contact sheet (one per second-ish, timestamps burned) beside the clip as <clip>-sheet.jpg
set -euo pipefail
c=$1; d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$c")
n=8; fps=$(python3 -c "print($n/$d)")
ffmpeg -v error -y -i "$c" -vf "fps=$fps,scale=480:-2,drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=4x2" -frames:v 1 "${c%.mp4}-sheet.jpg"
echo "${c%.mp4}-sheet.jpg ($d s)"
