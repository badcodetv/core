#!/usr/bin/env bash
# VHS camcorder finish for a 9:16 cut (The Malevolent Force, Jack's library pick 2026-11-18).
# Dull, muddy consumer tape, not neon: soft horizontal smear (rebuilt from ~240 lines), chroma bleed, chroma noise,
# lifted muddy-green shadows, a noisy tracking band with a jitter at the bottom, a burned-in PLAY / time stamp.
# Usage: scripts/shorts/vhs_finish.sh <in.mp4> <out.mp4> ["STAMP TEXT"]
set -euo pipefail
IN="$1"; OUT="$2"; STAMP="${3:-03:07 AM  NOV.18}"; STAMP_ESC="${STAMP//:/\\:}"
FONT=$(fc-match -f '%{file}' 'DejaVu Sans Mono:bold' 2>/dev/null || echo /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf)
ffmpeg -loglevel error -y -i "$IN" -filter_complex "
[0:v]scale=1080:1920,setsar=1,
 scale=150:640:flags=bilinear,scale=1080:1920:flags=bicubic,
 split[s1][s2];[s2]lutyuv=y='val*0.45':u=128:v=128[ghost];[s1][ghost]blend=all_mode=screen:all_opacity=0.0,
 split[g1][g2];[g2]crop=iw-14:ih:0:0,pad=iw+14:ih:14:0[g2s];[g1][g2s]blend=all_mode=lighten:all_opacity=0.35,
 chromashift=cbh=9:crh=-7,
 eq=saturation=1.25:contrast=0.92:brightness=0.02:gamma_g=1.06,
 colorbalance=gs=0.05:bs=-0.03:rm=0.04,
 noise=c0s=8:c1s=22:c2s=22:allf=t,
 split[base][band];
[band]crop=1080:110:0:1790,noise=alls=70:allf=t+u,
 geq=lum='lum(X+12*sin(Y/3+N*1.7),Y)':cb='cb(X,Y)':cr='cr(X,Y)'[bandn];
[base][bandn]overlay=0:1790,
 drawtext=fontfile=$FONT:text='▶ PLAY':x=60:y=90:fontsize=58:fontcolor=white@0.85:shadowx=3:shadowy=3,
 drawtext=fontfile=$FONT:text='$STAMP_ESC':x=w-tw-60:y=h-210:fontsize=52:fontcolor=0xFFB040@0.9:shadowx=3:shadowy=3,
 format=yuv420p[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
