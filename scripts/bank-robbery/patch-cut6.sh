#!/usr/bin/env bash
# The Bank Robbery, cut 6 (2026-10-09): picture-only patches over the cut 5 render, audio untouched.
# Premiere was not connected, so this is NOT a Premiere sequence yet: edl-cut6-changes.txt lists the same
# changes as timeline edits. Review and reasons: docs/stories/bank-robbery/review-cut5.md.
set -euo pipefail
P="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery"
C="$P/clips"; V="$P/vids"; O="$C/cut6"; mkdir -p "$O"; cd "$O"
IN="$P/renders/bank robbery - cut 5-20261008-1845.mp4"
OUT="$P/renders/bank robbery - cut 6-20261009-patch.mp4"
E="-an -c:v libx264 -crf 14 -preset medium -pix_fmt yuv420p -r 24"
seg(){ ffmpeg -v error -y -ss "$3" -i "$2" -t "$4" -vf "scale=1280:720,setsar=1,fps=24${5:+,$5}" $E "$1"; }
seg fry.mp4    "$C/cut5/c5-s00d-fry.mp4"   6.4  1.125      # egg already down: no flip, no bacon stuck to it
seg pint.mp4   "$C/cut5/c5-s00e-pint.mp4"  0.2  1.125      # the pull, before the head turns to a blob
seg bf.mp4     "$V/s01-breakfast.mp4"      6.25 1.7083     # after the mug has changed hands
seg den.mp4    "$C/cut1/hold-s01-denise.mp4" 0  5.375      # Denise's hold starts 2.2 s early to fill
seg remote.mp4 "$V/v3/s01b-remote.mp4"     3.2  4.7917     # after the remote and the plates stop changing
TW="crop=iw*0.71:ih*0.71:iw*0.145:0,scale=1280:720:flags=lanczos,unsharp=5:5:0.5,noise=alls=5:allf=t"   # model out by crop, no black band
seg tw1.mp4 "$C/cut2/c2-t-s05d-twist-1.mp4"   0      4.3333 "$TW"
seg tw2.mp4 "$V/v3/s05d-twist-1.mp4"          6.0833 1.7917 "$TW"
seg tw3.mp4 "$C/cut1/hold-s05-accountant.mp4" 0      2.6667 "$TW"
seg tw4.mp4 "$C/cut2/c2-t-s05d-twist-2.mp4"   0      1.9583 "$TW"
seg w1.mp4 "$V/s09-walk.mp4"            0.4167 7.5417      # the eating walk, half a second longer
seg w2.mp4 "$C/cut4/c4-s09-walk.mp4"    0.2917 2.75        # out before one man passes through the other
seg w3.mp4 "$C/cut5/c5-s08f-argue.mp4"  0      7.0
# keys: only the stretch after the keyring and the shop lights stop changing, slowed to fill the slot
ffmpeg -v error -y -ss 3.9 -i "$C/cut4/c4-s11e-cafe-for-sale.mp4" -t 6.2 -vf "scale=1280:720,setsar=1,setpts=PTS*9.7083/6.2,minterpolate=fps=24:mi_mode=blend" -t 9.7083 $E keys.mp4
printf "file 'bf.mp4'\nfile 'den.mp4'\nfile 'remote.mp4'\n" > l1.txt
printf "file 'tw1.mp4'\nfile 'tw2.mp4'\nfile 'tw3.mp4'\nfile 'tw4.mp4'\n" > l2.txt
printf "file 'w1.mp4'\nfile 'w2.mp4'\nfile 'w3.mp4'\n" > l3.txt
for i in 1 2 3; do ffmpeg -v error -y -f concat -safe 0 -i l$i.txt -c copy g$i.mp4; done
FC=""; cur="0:v"; i=0
for p in "fry 6.625 7.75" "pint 8.875 10.0" "g1 32.0833333 43.9583333" "g2 133.7916667 144.5416667" "g3 240.9583333 258.25" "keys 340.2916667 350.0"; do
  set -- $p; i=$((i+1)); a=$2; b=$(python3 -c "print($3-0.021)"); a0=$(python3 -c "print($2-0.001)")
  FC="$FC[$i:v]setpts=PTS-STARTPTS+$a/TB[p$i];[$cur][p$i]overlay=eof_action=repeat:enable='between(t,$a0,$b)'[o$i];"; cur="o$i"
done
ffmpeg -v error -y -i "$IN" -i fry.mp4 -i pint.mp4 -i g1.mp4 -i g2.mp4 -i g3.mp4 -i keys.mp4 -filter_complex "${FC%;}" -map "[o6]" -map 0:a -c:a copy -c:v libx264 -crf 15 -preset medium -pix_fmt yuv420p -r 24 -movflags +faststart "$OUT"
echo "wrote $OUT"
