#!/usr/bin/env bash
# GPOM cut 3 — the "2032" card (C0). ffmpeg only; Premiere's API cannot write text.
# Duration is the only knob: everything is expression-driven, so a longer -t just holds
# the finished number with the cursor still blinking and the CRT mains flicker still running.
set -euo pipefail
OUT=${1:-/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/takes-recut/C0-POST-v2.mp4}
DUR=${2:-3}
F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
G=0x6EEB82           # matched to cut 2's tube: its terminal green peaks G=247, this card G=244
X=636; Y=434; CH=212; CW=140
D="fontfile=$F:fontsize=280:fontcolor=$G:x=$X:y=$Y-16"
ffmpeg -v error -f lavfi -i color=c=black:s=1920x1080:r=24 -t "$DUR" -filter_complex "\
[0:v]drawtext=$D:text='2':enable='gte(t,0.20)',\
drawtext=$D:text='20':enable='gte(t,0.42)',\
drawtext=$D:text='203':enable='gte(t,0.64)',\
drawtext=$D:text='2032':enable='gte(t,0.86)',\
drawbox=x=$((X+10)):y=$Y:w=$CW:h=$CH:color=$G@0.95:t=fill:enable='lt(t,0.20)',\
drawbox=x=$((X+179)):y=$Y:w=$CW:h=$CH:color=$G@0.95:t=fill:enable='between(t,0.20,0.42)',\
drawbox=x=$((X+347)):y=$Y:w=$CW:h=$CH:color=$G@0.95:t=fill:enable='between(t,0.42,0.64)',\
drawbox=x=$((X+516)):y=$Y:w=$CW:h=$CH:color=$G@0.95:t=fill:enable='between(t,0.64,0.86)',\
drawbox=x=$((X+684)):y=$Y:w=$CW:h=$CH:color=$G@0.95:t=fill:enable='gte(t,0.86)*lt(mod(t-0.86,0.72),0.44)',\
frei0r=glow:0.55,frei0r=scanline0r,\
eq=brightness='0.012*sin(6.2832*11.3*t)+0.008*sin(6.2832*27.1*t)':eval=frame,\
vignette=PI/5,noise=c0s=5:c0f=t+u,format=yuv420p,setsar=1[v]" \
 -map "[v]" -c:v libx264 -crf 15 -pix_fmt yuv420p -y "$OUT"
ffprobe -v error -show_entries stream=nb_frames,sample_aspect_ratio -show_entries format=duration -of default=nw=1 "$OUT"
