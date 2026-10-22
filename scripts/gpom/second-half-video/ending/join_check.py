#!/usr/bin/env python3
"""continuous-shot step 5: join_check.py a.mp4 b.mp4 [strip.jpg]
Mean absolute grey difference between A's last frame and B's first, against the median/max frame-to-frame
step inside each clip (a good join sits below the in-clip step), plus a six-frame strip across the join."""
import subprocess, sys
import numpy as np
W, H = 160, 90
def frames(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(float)
a, b = frames(sys.argv[1]), frames(sys.argv[2])
step = lambda f: np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))
sa, sb = step(a), step(b)
j = np.abs(a[-1] - b[0]).mean(); j2 = np.abs(a[-1] - b[1]).mean()
print(f'join last->first {j:.2f}  last->second {j2:.2f}  | in-clip A median {np.median(sa):.2f} max {sa.max():.2f}  B median {np.median(sb):.2f} max {sb.max():.2f}  | {"OK" if j2 <= max(np.median(sa), np.median(sb)) * 1.5 else "CHECK"}')
if len(sys.argv) > 3:
    na = len(a)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', sys.argv[1], '-i', sys.argv[2], '-filter_complex',
        f"[0]select='gte(n,{na-3})',scale=426:240,setpts=N/24/TB[x];[1]select='lt(n,3)',scale=426:240,setpts=N/24/TB[y];[x][y]concat=n=2:v=1,tile=6x1",
        '-frames:v', '1', sys.argv[3]], check=True)
