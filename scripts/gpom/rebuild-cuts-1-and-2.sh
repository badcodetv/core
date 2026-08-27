#!/usr/bin/env bash
# Rebuild GPOM cut 1 (Earth/satellite) and cut 2 (Hong Kong) as PER-BEAT clips, so the
# timing can be edited on the Premiere timeline instead of being baked into one file.
#
# Structure was MEASURED off the masters (frame-difference scan, 2026-08-27), not taken
# from the docs — both ledgers disagreed with the picture:
#   * cut 1 has exactly ONE hard cut, at 40.0s. The other six joins are frame-matched.
#     Seven beats of 8.000s. The shipped master had been re-encoded 24 -> 25fps
#     (1400 frames for 1344 frames of material), so it carries duplicated frames. Native is 24.
#   * cut 2 has hard cuts at 8.0s and 11.5s only, and is FOUR beats, not the five in the
#     ledger table. The 4.5s office push (B3) never made the v3 cut — the Veo push-in starts
#     on the same plate and does that job. The table sums to 32.3s against a 27.83s master.
# Joins verified: B1 = hk-modern-a REVERSED (last frame vs master f0 = 1.45/255; take b = 23.36),
# pushin_off/0000 = master @11.50 (1.27), frames/0000 = master @19.50 (1.30). All codec noise.
set -euo pipefail
R=/mnt/d/badcode-videos/gitpush-origin-master/clips
OUT=$R/beats
mkdir -p "$OUT"
V=(-c:v libx264 -crf 16 -pix_fmt yuv420p -an -y)
# Everything lands 1920x1080 / 24fps / square pixels, so Scale on the timeline stays at 100
# and is free for camera pushes later.
FIN="scale=1920:1080:flags=lanczos,setsar=1,fps=24"

echo "=== CUT 1 — Earth / satellite, 7 beats x 8s ==="
c1 () { ffmpeg -v error -i "$R/s00/$2" -vf "$FIN" "${V[@]}" "$OUT/EARTH-$1.mp4"; echo "  EARTH-$1"; }
c1r() { ffmpeg -v error -i "$R/s00/$2" -vf "reverse,$FIN" "${V[@]}" "$OUT/EARTH-$1.mp4"; echo "  EARTH-$1 (reversed)"; }
c1  b1-macro     s00v3-idle-macro-a.mp4
c1r b2-pullout1  s00v3-pushin2-b.mp4      # reversed: the deep push becomes the start of the pull-out
c1r b3-pullout2  s00v3-pushin-a.mp4       # reversed: chained stage two, lands frame-exact on the board
c1  b4-board     s00v3-idle-board-b.mp4
c1  b5-reveal    s00v2-reveal-flush-c.mp4
c1  b6-orbit1    s00v3-orbit1-b.mp4
c1  b7-orbit2    s00v3-orbit2-b.mp4

echo "=== CUT 2 — Hong Kong, 4 beats ==="
# B1 — the descent. Veo craned UP; reversed so we descend into the city.
ffmpeg -v error -i "$R/s01/s01-b1-hk-modern-a.mp4" -vf "reverse,$FIN" "${V[@]}" "$OUT/HK-b1-descent.mp4"
echo "  HK-b1-descent (reversed)"
# B2 — one lit floor in a black tower. Eased 1.07x push on the still, 3.5s = 84 frames.
# smoothstep easing so it starts and stops without a lurch.
ffmpeg -v error -loop 1 -i "$R/s01/stills/s01-tower-ext2-b.jpg" -t 3.5 -r 24 \
  -vf "scale=5760:3240:flags=lanczos,zoompan=z='1+0.07*pow(on/83,2)*(3-2*(on/83))':d=84:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=24,setsar=1" \
  "${V[@]}" "$OUT/HK-b2-tower.mp4"
echo "  HK-b2-tower"
# B3 — the Veo push-in to the CRT, screen already killed in post (build_screen.py). 192 frames.
ffmpeg -v error -framerate 24 -i "$R/s01/pushin_off/%04d.png" -vf "$FIN" "${V[@]}" "$OUT/HK-b3-pushin.mp4"
echo "  HK-b3-pushin"
# B4 — the terminal, composited natively at 1080 (build_terminal.py). 200 frames = 8.333s.
ffmpeg -v error -framerate 24 -i "$R/s01/frames/%04d.png" -vf "setsar=1,fps=24" "${V[@]}" "$OUT/HK-b4-terminal.mp4"
echo "  HK-b4-terminal"

echo "=== BUILT ==="
for f in "$OUT"/*.mp4; do
  printf "%-26s " "$(basename "$f")"
  ffprobe -v error -show_entries stream=width,height,r_frame_rate,nb_frames -show_entries format=duration -of csv=p=0 "$f" | tr '\n' ' '; echo
done
