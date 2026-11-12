#!/usr/bin/env python3
"""Same Bench: the on-screen dates (Jack, 2026-11-12: "we need the date to be on screen for each time").
Two treatments, made by ffmpeg, never drawn by Flow:
  card   - a full-frame silent-film intertitle (black, double rule border, the year in Baskerville)
  burn   - the year set into the black void at the top of a picked still
Usage: same_bench_dates.py <media-dir>   (writes <media>/dates/*.png)"""
import subprocess, sys, pathlib
media = pathlib.Path(sys.argv[1]); out = media / 'dates'; out.mkdir(exist_ok=True)
FONT = '/mnt/c/Windows/Fonts/BASKVILL.TTF'
W, H = 768, 1376
GRAIN = "noise=alls=22:allf=t,eq=contrast=1.08"
def run(args): subprocess.run(['ffmpeg', '-v', 'error', '-y', *args], check=True)
for year in ('1919', '2026'):
    # intertitle card
    vf = (f"drawbox=x=48:y=300:w={W-96}:h={H-600}:color=white@0.85:t=3,"
          f"drawbox=x=62:y=314:w={W-124}:h={H-628}:color=white@0.6:t=1,"
          f"drawtext=fontfile={FONT}:text='{year}':fontcolor=white@0.92:fontsize=210:x=(w-tw)/2:y=(h-th)/2,"
          f"{GRAIN},vignette=PI/3.2")
    run(['-f', 'lavfi', '-i', f'color=c=0x0b0b0b:s={W}x{H}', '-frames:v', '1', '-vf', vf, str(out / f'card-{year}.png')])
still = {'1919': 'moodboard/A3-a.jpg', '2026': 'moodboard/B3-a.jpg'}
for year, rel in still.items():
    vf = (f"drawtext=fontfile={FONT}:text='{year}':fontcolor=white@0.9:fontsize=150:x=(w-tw)/2:y=120,"
          f"drawbox=x=(iw-300)/2:y=295:w=300:h=2:color=white@0.7:t=fill")
    run(['-i', str(media / rel), '-frames:v', '1', '-vf', vf, str(out / f'burn-{year}.png')])
# Dialogue cards (Jack, 2026-11-12, timeline r1: the ask before each "Forget it.", silent-film style).
# A quoted line, smaller, wrapped, inside the same double rule.
SAYS = {'say-1919': ['“They promised us', 'homes fit', 'for heroes.”'],
        'say-2026': ['“You clapped', 'for us every', 'Thursday.”']}
for name, rows in SAYS.items():
    vf = (f"drawbox=x=48:y=300:w={W-96}:h={H-600}:color=white@0.85:t=3,"
          f"drawbox=x=62:y=314:w={W-124}:h={H-628}:color=white@0.6:t=1,")
    for i, row in enumerate(rows):
        y = H // 2 - 110 + i * 95
        vf += f"drawtext=fontfile={FONT}:text='{row.replace(chr(39), '')}':fontcolor=white@0.92:fontsize=70:x=(w-tw)/2:y={y},"
    vf += f"{GRAIN},vignette=PI/3.2"
    run(['-f', 'lavfi', '-i', f'color=c=0x0b0b0b:s={W}x{H}', '-frames:v', '1', '-vf', vf, str(out / f'card-{name}.png')])
print('\n'.join(str(p) for p in sorted(out.glob('*.png'))))
