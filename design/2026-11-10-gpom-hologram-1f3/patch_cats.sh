#!/bin/bash
# 1F3: the cats only show in the cloud (from the bloom to just after "yet"); every frame is a pure function of t (record.mjs/frameAt),
# so after the full render, re-record frames A..B with the cat stills (bead-media-1f3.json c0/c1) and drop them over the same frame numbers.
set -e
cd /home/kai/projects/badcode/badcode
R=/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f3-24; A=${1:-1709}; B=${2:-2202}; T=$R/_patch
rm -rf $T; AT=$(python3 -c "print(','.join(f'{i/24:.6f}' for i in [$A]*3+list(range($A,$B+1))))")   # 3 warm-up frames: the first frames of a fresh page draw before the web font loads (tags missing); checked 64-70 dB PSNR vs the full render after warm-up
node design/2026-11-10-gpom-hologram-1f3/record.mjs http://127.0.0.1:8743/index.html $T --at $AT --media design/2026-11-10-gpom-hologram-1f3/bead-media-1f3.json --frames frames
python3 -c "
import shutil,pathlib
T=pathlib.Path('$T/frames'); R=pathlib.Path('$R/frames-beads'); n=0
for k,f in enumerate(sorted(T.glob('*.jpg'))[3:]): shutil.copyfile(f, R/f'{$A+k:05d}.jpg'); n+=1
print('patched',n,'frames from',$A)"
rm -rf $T
