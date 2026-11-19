#!/usr/bin/env bash
# 16mm film finish for a 9:16 cut (Hello, I'm BadCode, Jack 2026-11-19: "put an overlay over it… just look better…
# something like [Malevolent Force's] but don't use that one"). Deliberately not the VHS finish (vhs_finish.sh):
# no smear, no tracking band, no chroma bleed. Instead a projected-print feel:
#   - a print grade: blacks lifted a touch, highlights rolled off, warm highlights over slightly cool shadows
#   - halation: the bright parts glow red-orange at their edges, the way light spills in film emulsion
#   - fine luma-only grain that moves every frame
#   - gate weave: the frame drifts a pixel or two, slowly, as film does in a gate
#   - a soft vignette and a very small exposure flicker
# Strength is one number (STRENGTH, 0..1, default 1). Audio is copied through.
# Usage: scripts/shorts/film_finish.sh <in.mp4> <out.mp4> [STRENGTH]
set -euo pipefail
IN="$1"; OUT="$2"; S="${3:-1}"
HALO=$(python3 -c "print(round(0.32*$S,3))")
GRAIN=$(python3 -c "print(round(11*$S))")
FLICK=$(python3 -c "print(round(0.012*$S,4))")
ffmpeg -loglevel error -y -i "$IN" -filter_complex "
[0:v]scale=1104:1962,crop=1080:1920:x='12+3*sin(n/9)+1.5*sin(n/3.7)':y='21+3*sin(n/13)+1*sin(n/5.3)',setsar=1,
 curves=master='0/0.05 0.25/0.255 0.75/0.76 1/0.95',
 colorbalance=rs=-0.02:bs=0.025:rh=0.03:gh=0.01:bh=-0.035,
 eq=saturation=0.92:brightness='$FLICK*sin(n*2.1)*sin(n*0.7)':eval=frame,
 format=gbrp,split[base][hi];
[hi]curves=all='0/0 0.72/0 1/1',gblur=sigma=22,colorchannelmixer=rr=1:gg=0.38:bb=0.12[halo];
[base][halo]blend=all_mode=screen:all_opacity=$HALO,
 vignette=angle=PI/5.5,
 format=yuv420p,noise=c0s=$GRAIN:c0f=t,
 format=yuv420p[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
