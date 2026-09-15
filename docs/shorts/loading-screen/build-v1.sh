#!/usr/bin/env bash
# Loading Screen V1: ink page (Omni) -> 3D page flip -> real 20.mp4. 1920x1080@24, 8s.
set -euo pipefail
SP="${SP:-$(pwd)}"
FF="${FF:-ffmpeg}"   # no ffmpeg in WSL: `npm i ffmpeg-static` in a scratch dir and pass FF=...
INK="${INK:?path to v1-ink-page.mp4}"; REAL="${REAL:?path to new clips/20.mp4}"
OUT="${1:-$SP/v1-loading-screen.mp4}"
T0=3.5; D=1.0; TOTAL=8
W=1920; H=1080; F=2.2   # F = focal length in page widths: smaller = stronger perspective

# Per-pixel page geometry (page hinged on the left edge, swinging toward camera, 0 -> 90 degrees).
P="clip((T-$T0)/$D\,0\,1)"
TH="(1-cos(PI*$P))/2*PI/2"
S="sin($TH)"; C="cos($TH)"
XN="(X/W)"
DEN="($C*$F+$XN*$S)"
U="($XN*$F/$DEN)"                       # source column, 0..1 across the page
G="($F/($F-$U*$S))"                     # perspective magnification at that column
SY="(((Y-H/2)/W)/$G*W+H/2)"             # source row
INSIDE="(gt($DEN\,0.0001)*lte($U\,1)*gte($SY\,0)*lte($SY\,H-1))"
SHADE="(1-0.38*$S-0.22*$S*$U+0.28*sin(2*$TH)*exp(-pow(($U-0.78)/0.16\,2)))"
EDGE="gte($U\,0.988)*$S"   # thin paper-thickness highlight on the free edge while it is lifted
PAGE_R="(r(clip($U*W\,0\,W-1)\,clip($SY\,0\,H-1))*$SHADE)*(1-$EDGE)+238*$EDGE"
PAGE_G="(g(clip($U*W\,0\,W-1)\,clip($SY\,0\,H-1))*$SHADE)*(1-$EDGE)+234*$EDGE"
PAGE_B="(b(clip($U*W\,0\,W-1)\,clip($SY\,0\,H-1))*$SHADE)*(1-$EDGE)+222*$EDGE"
PAGE_A="255*$INSIDE"

# Shadow the page casts on the real frame, just right of its moving edge; strongest mid-turn.
XE="($C*$F/($F-$S))"
SH="(1-0.65*sin(2*$TH)*gte($XN\,$XE)*exp(-($XN-$XE)/0.13))"

"$FF" -hide_banner -loglevel error -y \
  -i "$INK" -i "$REAL" \
  -f lavfi -t 0.7 -i "anoisesrc=color=pink:sample_rate=48000:amplitude=0.6" \
  -filter_complex "
    [0:v]trim=0:$(echo "$T0+$D" | bc),setpts=PTS-STARTPTS,fps=24,scale=$W:$H:flags=lanczos,format=gbrp,split[inkA][inkB];
    [1:v]trim=0:$(echo "$TOTAL-$T0" | bc),setpts=PTS-STARTPTS,fps=24,scale=$W:$H,format=gbrp,tpad=start_duration=$T0:start_mode=clone[realpad];
    [inkA]trim=0:$T0,setpts=PTS-STARTPTS[seg1];
    [inkB]trim=$T0:$(echo "$T0+$D" | bc),setpts=PTS-STARTPTS+$T0/TB,format=gbrap,geq=r='$PAGE_R':g='$PAGE_G':b='$PAGE_B':a='$PAGE_A'[page];
    [realpad]split[realU][realS];
    [realU]trim=$T0:$(echo "$T0+$D" | bc),setpts=PTS-STARTPTS+$T0/TB,geq=r='r(X\,Y)*$SH':g='g(X\,Y)*$SH':b='b(X\,Y)*$SH'[under];
    [under][page]overlay=format=gbrp,setpts=PTS-STARTPTS[seg2];
    [realS]trim=$(echo "$T0+$D" | bc):$TOTAL,setpts=PTS-STARTPTS[seg3];
    [seg1][seg2][seg3]concat=n=3:v=1:a=0,fps=24,format=yuv420p,
      scale=w='trunc($W*(1+0.05*t/$TOTAL)/2)*2':h='trunc($H*(1+0.05*t/$TOTAL)/2)*2':eval=frame:flags=lanczos,
      crop=$W:$H,setsar=1[v];
    [0:a]atrim=0:$(echo "$T0+$D" | bc),asetpts=PTS-STARTPTS[a1];
    [1:a]atrim=0:$(echo "$TOTAL-$T0" | bc),asetpts=PTS-STARTPTS[a2];
    [a1][a2]acrossfade=d=$D:c1=tri:c2=tri[bed];
    [2:a]highpass=f=1400,lowpass=f=7500,volume='if(lt(t\,0.10)\,t/0.10\,exp(-(t-0.10)*8))':eval=frame,volume=0.35,adelay=$(echo "($T0+0.05)*1000" | bc | cut -d. -f1)|$(echo "($T0+0.05)*1000" | bc | cut -d. -f1)[swish];
    [bed][swish]amix=inputs=2:duration=first:normalize=0,atrim=0:$TOTAL[a]
  " -map "[v]" -map "[a]" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p \
    -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
    -r 24 -c:a aac -b:a 192k -t $TOTAL "$OUT"
echo "$OUT"
