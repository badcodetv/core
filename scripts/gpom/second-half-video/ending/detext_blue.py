"""Wipe thin white lettering off a blue shop board in a clip (GPOM E round 9: Omni wrote a second 'DOWNLA...' on the
board next to the bank as the bus uncovered it).

    ~/.cache/badcode-lips/venv/bin/python -I detext_blue.py CLIP OUT --box x0,y0,x1,y1

Per frame, inside the box (padded): a grey morphological opening removes thin bright strokes; the result is used only
where the opened colour is the blue board (B well above R; a 41 px median along each row, which drops the letters and keeps the board's vertical light), so the passing red bus and the wall are left alone.
"""
import subprocess, sys
import cv2, numpy as np
a = sys.argv[1:]; clip, out = a[0], a[1]
x0, y0, x1, y1 = map(int, a[a.index('--box') + 1].split(','))
cap = cv2.VideoCapture(clip); fps = cap.get(cv2.CAP_PROP_FPS) or 24
W, H = int(cap.get(3)), int(cap.get(4))
ENC = ['-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)
k = np.ones((7, 7), np.uint8); n = 0
while True:
    ok, f = cap.read()
    if not ok: break
    roi = f[y0:y1, x0:x1].copy()
    r = roi.astype(np.int32)
    board = ((r[..., 0] - r[..., 2]) > 30).astype(np.uint8)              # the blue board
    near = cv2.dilate(board, np.ones((11, 11), np.uint8))                # the letters sit inside it
    pad = np.pad(roi, ((0, 0), (20, 20), (0, 0)), mode='edge')
    med = np.median(np.lib.stride_tricks.sliding_window_view(pad, 41, axis=1), axis=-1)  # along each row: letters out,
    w = cv2.GaussianBlur(cv2.erode(near, np.ones((3, 3), np.uint8)).astype(np.float32), (0, 0), 1.5)[..., None]  # the
    f[y0:y1, x0:x1] = np.clip(roi * (1 - w) + med * w, 0, 255).astype(np.uint8)  # board's top-to-bottom light kept
    enc.stdin.write(f.tobytes()); n += 1
enc.stdin.close(); enc.wait(); print(out, n, 'frames')
