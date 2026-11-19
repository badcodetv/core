#!/usr/bin/env bash
# Priority Lane: a finish over the whole short (Jack, 2026-11-19: "is there any overlay we can put over it… like any
# filter"). Three options, each one look over the cut, applied last (after the picture is assembled, before the logo):
#   night35   the story's own look.md taken further: a night 35 mm print. Coarse moving grain, red-orange halation round
#             the sodium lamps and blue lights, cool shadows, a soft roll-off, a gentle vignette.
#   dashcam   as if caught on a camera bolted in the cab: wide-lens barrel bend, over-sharpened edges, crushed blacks,
#             a cold digital cast, a touch of blockiness. No burned-in text (badcode.md: no readable text).
#   bleach    bleach bypass: half the colour, hard contrast, silvery highlights, deep blacks, fine grain. Gritty, cold.
# Usage: scripts/shorts/priority_lane_finish.sh <night35|dashcam|bleach> <in.mp4> <out.mp4>
set -euo pipefail
K="$1"; IN="$2"; OUT="$3"
case "$K" in
  night35) VF="scale=1080:1920,setsar=1,curves=master='0/0.04 0.3/0.27 0.8/0.82 1/0.94',colorbalance=bs=0.04:gs=0.01:rh=0.025:bh=-0.03,
format=gbrp,split[b][h];[h]curves=all='0/0 0.78/0 1/1',gblur=sigma=18,colorchannelmixer=rr=1:gg=0.3:bb=0.08[g];[b][g]blend=all_mode=screen:all_opacity=0.28,
vignette=angle=PI/6,format=yuv420p,noise=c0s=16:c0f=t" ;;
  dashcam) VF="scale=1080:1920,setsar=1,lenscorrection=k1=-0.18:k2=-0.03,scale=1240:2204,crop=1080:1920,unsharp=5:5:1.4,
eq=contrast=1.18:saturation=0.85:gamma=0.92,colorbalance=bs=0.05:bm=0.03:rh=-0.02,
scale=540:960:flags=neighbor,scale=1080:1920:flags=bilinear,noise=alls=6:allf=t,format=yuv420p" ;;
  bleach) VF="scale=1080:1920,setsar=1,format=gbrp,split[c][l];[l]hue=s=0,curves=all='0/0 0.25/0.15 0.75/0.85 1/1'[m];
[c][m]blend=all_mode=overlay:all_opacity=0.65,eq=saturation=0.5:contrast=1.12,format=yuv420p,noise=c0s=9:c0f=t" ;;
  *) echo "unknown finish $K" >&2; exit 2 ;;
esac
ffmpeg -nostdin -loglevel error -y -i "$IN" -filter_complex "[0:v]${VF//$'\n'/}[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
