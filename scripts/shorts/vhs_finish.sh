#!/usr/bin/env bash
# VHS camcorder finish for a 9:16 cut (The Malevolent Force, Jack's library pick 2026-11-18).
# Subtle since Jack's note 2026-11-18 ("less intense and more subtle"); the round-1 strength is in git history.
# Dull, muddy consumer tape, not neon: soft horizontal smear (rebuilt from ~240 lines), chroma bleed, chroma noise,
# lifted muddy-green shadows, a noisy tracking band with a jitter at the bottom, a burned-in PLAY / time stamp.
# Usage: scripts/shorts/vhs_finish.sh <in.mp4> <out.mp4> ["STAMP TEXT"]
set -euo pipefail
IN="$1"; OUT="$2"; STAMP="${3:-03:07 AM  NOV.18}"; STAMP_ESC="${STAMP//:/\\:}"
FONT=$(fc-match -f '%{file}' 'DejaVu Sans Mono:bold' 2>/dev/null || echo /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf)
ffmpeg -loglevel error -y -i "$IN" -filter_complex "
[0:v]scale=1080:1920,setsar=1,
 scale=300:960:flags=bilinear,scale=1080:1920:flags=bicubic,
 split[s1][s2];[s2]lutyuv=y='val*0.45':u=128:v=128[ghost];[s1][ghost]blend=all_mode=screen:all_opacity=0.0,
 split[g1][g2];[g2]crop=iw-8:ih:0:0,pad=iw+8:ih:8:0[g2s];[g1][g2s]blend=all_mode=lighten:all_opacity=0.15,
 chromashift=cbh=4:crh=-3,
 eq=saturation=1.1:contrast=0.96:brightness=0.01:gamma_g=1.03,
 colorbalance=gs=0.025:bs=-0.015:rm=0.02,
 noise=c0s=4:c1s=10:c2s=10:allf=t,
 split[base][band];
[band]crop=1080:60:0:1840,noise=alls=40:allf=t+u,
 geq=lum='lum(X+5*sin(Y/3+N*1.7),Y)':cb='cb(X,Y)':cr='cr(X,Y)'[bandn];
[base][bandn]overlay=0:1840,
 drawtext=fontfile=$FONT:text='▶ PLAY':x=60:y=90:fontsize=46:fontcolor=white@0.7:shadowx=3:shadowy=3,
 drawtext=fontfile=$FONT:text='$STAMP_ESC':x=w-tw-60:y=h-210:fontsize=42:fontcolor=0xFFB040@0.75:shadowx=3:shadowy=3,
 format=yuv420p[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
