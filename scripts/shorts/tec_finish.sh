#!/usr/bin/env bash
# Ten Economic Commandments: a finish over the whole short (Jack, 2026-11-19: "Come up with some sort of filter as well.
# And do a bunch of varied ones."). This short's own set, written for a late-90s New York rap video; no other story's
# finish is reused. Applied to each shot; the logo card is never filtered.
#   fisheye    a wide-angle rap-video lens: barrel bend, punchy colour, dark corners
#   hi8        a 90s camcorder tape: soft, smeared colour, slightly lifted blacks, fine noise
#   xerox      a photocopied mixtape flyer: hard black and white, toner grain, warm paper
#   trix       black-and-white street photo on fast film: deep blacks, heavy grain
#   kodachrome warm slide film: rich reds and yellows, deep shadows
#   cabletv    a 90s cable broadcast: low resolution, scanlines, colour fringing
#   riso       a two-ink print, teal and orange
#   goldleaf   gold and black duotone (the money)
# Usage: scripts/shorts/tec_finish.sh <name> <in.mp4> <out.mp4>
set -euo pipefail
K="$1"; IN="$2"; OUT="$3"
case "$K" in
  fisheye)    VF="scale=1080:1920,setsar=1,lenscorrection=k1=-0.32:k2=-0.06,scale=1300:2311,crop=1080:1920,eq=saturation=1.35:contrast=1.05,vignette=angle=PI/5,format=yuv420p" ;;
  hi8)        VF="scale=1080:1920,setsar=1,scale=480:854,scale=1080:1920:flags=bicubic,chromashift=cbh=6:crh=-5,eq=saturation=1.15:brightness=0.03:contrast=0.95,curves=master='0/0.06 1/0.96',format=yuv420p,noise=alls=10:allf=t" ;;
  xerox)      VF="scale=1080:1920,setsar=1,format=gray,curves=all='0/0 0.28/0 0.46/1 1/1',noise=alls=30:allf=t,format=yuv420p,colorchannelmixer=rr=1:gg=0.96:bb=0.86" ;;
  trix)       VF="scale=1080:1920,setsar=1,hue=s=0,curves=all='0/0 0.2/0.08 0.5/0.5 0.85/0.95 1/1',eq=contrast=1.1,format=yuv420p,noise=c0s=22:c0f=t" ;;
  kodachrome) VF="scale=1080:1920,setsar=1,colorbalance=rs=0.08:gs=0.02:bs=-0.06:rm=0.05:bm=-0.05:rh=0.03:bh=-0.06,eq=saturation=1.3:contrast=1.15:gamma=0.95,format=yuv420p,noise=c0s=6:c0f=t" ;;
  cabletv)    VF="scale=1080:1920,setsar=1,scale=360:640,scale=1080:1920:flags=neighbor,chromashift=cbh=4:crh=-4,eq=saturation=1.1:contrast=1.05,geq=lum='lum(X,Y)*(0.82+0.18*mod(Y,4)/3)':cb='cb(X,Y)':cr='cr(X,Y)',format=yuv420p" ;;
  riso)       VF="scale=1080:1920,setsar=1,format=gray,curves=all='0/0 0.5/0.45 1/1',format=rgb24,lutrgb=r='val*0.98':g='val*0.6+(255-val)*0.35':b='val*0.35+(255-val)*0.4',format=yuv420p,noise=alls=8:allf=t" ;;
  goldleaf)   VF="scale=1080:1920,setsar=1,format=gray,curves=all='0/0 0.3/0.15 0.8/0.9 1/1',format=rgb24,lutrgb=r='val*1.0':g='val*0.78':b='val*0.32',format=yuv420p,noise=c0s=6:c0f=t" ;;
  # Round 2, subtle (Jack, 2026-11-19: "less abrasive filters like more subtle ones and that fit the vibe"): each one a
  # light touch on colour and grain, never a new picture.
  warm35)     VF="scale=1080:1920,setsar=1,colorbalance=rh=0.025:gh=0.01:bh=-0.02:bs=0.01,curves=master='0/0.02 1/0.98',eq=saturation=0.95,format=yuv420p,noise=c0s=5:c0f=t" ;;
  matte)      VF="scale=1080:1920,setsar=1,curves=master='0/0.07 0.5/0.5 1/0.94',eq=saturation=0.88:contrast=0.97,format=yuv420p,noise=c0s=3:c0f=t" ;;
  dusk)       VF="scale=1080:1920,setsar=1,colorbalance=bs=0.035:gs=0.01:rh=0.03:bh=-0.02,eq=saturation=0.97,format=yuv420p,noise=c0s=4:c0f=t" ;;
  bloom)      VF="scale=1080:1920,setsar=1,format=gbrp,split[b][h];[h]curves=all='0/0 0.7/0 1/1',gblur=sigma=14[g];[b][g]blend=all_mode=screen:all_opacity=0.18,format=yuv420p,noise=c0s=4:c0f=t" ;;
  magazine)   VF="scale=1080:1920,setsar=1,curves=master='0/0.03 0.25/0.22 0.75/0.8 1/0.97',colorbalance=rm=0.02:gm=0.01:bm=-0.02,eq=saturation=0.9,vignette=angle=PI/7,format=yuv420p,noise=c0s=6:c0f=t" ;;
  tapelight)  VF="scale=1080:1920,setsar=1,chromashift=cbh=2:crh=-2,eq=saturation=1.05:brightness=0.01,curves=master='0/0.03 1/0.98',format=yuv420p,noise=alls=4:allf=t" ;;
  *) echo "unknown finish $K" >&2; exit 2 ;;
esac
ffmpeg -nostdin -loglevel error -y -i "$IN" -vf "$VF" -map 0:v -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy "$OUT"
