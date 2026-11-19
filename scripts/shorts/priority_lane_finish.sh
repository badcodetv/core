#!/usr/bin/env bash
# Priority Lane: a finish over the whole short (Jack, 2026-11-19: "is there any overlay we can put over it… like any
# filter"). Three options, each one look over the cut, applied last (after the picture is assembled, before the logo):
#   night35   the story's own look.md taken further: a night 35 mm print. Coarse moving grain, red-orange halation round
#             the sodium lamps and blue lights, cool shadows, a soft roll-off, a gentle vignette.
#   dashcam   as if caught on a camera bolted in the cab: wide-lens barrel bend, over-sharpened edges, crushed blacks,
#             a cold digital cast, a touch of blockiness. No burned-in text (badcode.md: no readable text).
#   bleach    bleach bypass: half the colour, hard contrast, silvery highlights, deep blacks, fine grain. Gritty, cold.
# Round 2 (Jack, 2026-11-19: "an array of differing filters"): noir (hard black and white), nightvision (green image
# intensifier), cctv (12 fps, blocky, cold, wide), sodium (orange-and-blue street-lamp duotone), crossproc (cross-processed
# film), super8 (warm faded home movie, gate weave, flicker), tealorange (blockbuster grade), thermal (heat-camera false colour).
# Usage: scripts/shorts/priority_lane_finish.sh <name> <in.mp4> <out.mp4>
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
  noir) VF="scale=1080:1920,setsar=1,hue=s=0,curves=all='0/0 0.3/0.18 0.7/0.85 1/1',eq=contrast=1.15,vignette=angle=PI/5,format=yuv420p,noise=c0s=10:c0f=t" ;;
  nightvision) VF="scale=1080:1920,setsar=1,hue=s=0,eq=gamma=1.6:contrast=1.2,colorchannelmixer=rr=0.12:rg=0.35:gr=0.3:gg=1.15:br=0.04:bg=0.12,
format=gbrp,split[b][h];[h]gblur=sigma=14[g];[b][g]blend=all_mode=screen:all_opacity=0.35,vignette=angle=PI/3.2,format=yuv420p,noise=alls=22:allf=t" ;;
  cctv) VF="scale=1080:1920,setsar=1,fps=12,fps=24,lenscorrection=k1=-0.1,eq=saturation=0.3:contrast=1.1:brightness=0.03,colorbalance=bs=0.06:gs=0.03,
scale=360:640,scale=1080:1920:flags=neighbor,format=yuv420p,noise=alls=8:allf=t" ;;
  sodium) VF="scale=1080:1920,setsar=1,hue=s=0,curves=r='0/0.02 0.5/0.62 1/1':g='0/0.01 0.5/0.38 1/0.85':b='0/0.06 0.5/0.2 1/0.45',eq=contrast=1.1,format=yuv420p,noise=c0s=8:c0f=t" ;;
  crossproc) VF="scale=1080:1920,setsar=1,curves=r='0/0 0.25/0.18 0.75/0.85 1/1':g='0/0.04 0.5/0.55 1/0.95':b='0/0.18 1/0.8',eq=saturation=1.25:contrast=1.08,format=yuv420p" ;;
  super8) VF="scale=1080:1920,setsar=1,scale=1100:1956,crop=1080:1920:x='10+4*sin(n/5)':y='18+5*sin(n/3.3)',
curves=master='0/0.08 0.5/0.52 1/0.9',colorbalance=rs=0.05:gs=0.02:bs=-0.06:rh=0.06:bh=-0.05,eq=saturation=0.85:brightness='0.025*sin(n*1.9)':eval=frame,
vignette=angle=PI/4,format=yuv420p,noise=c0s=20:c0f=t" ;;
  tealorange) VF="scale=1080:1920,setsar=1,colorbalance=rs=-0.12:gs=0.02:bs=0.14:rh=0.12:gh=0.03:bh=-0.12,eq=saturation=1.2:contrast=1.08,format=yuv420p" ;;
  thermal) VF="scale=1080:1920,setsar=1,format=gray,curves=all='0/0 0.4/0.35 1/1',pseudocolor=preset=heat,format=yuv420p,noise=alls=4:allf=t" ;;
  *) echo "unknown finish $K" >&2; exit 2 ;;
esac
ffmpeg -nostdin -loglevel error -y -i "$IN" -filter_complex "[0:v]${VF//$'\n'/}[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
