#!/usr/bin/env python3
"""Where a face's lips actually move in a clip, measured from the picture (2026-10-19, Bank Robbery short cut 7 notes;
moved from scripts/bank-robbery/ to scripts/lipsync/ 2026-10-29 — it is generic, used by every dubbed film).

Jack on cut 7: "at 20 secs she speaks but her lips dont move ... they speak when their mouths are closed". The dubs had
been placed on the faster-whisper word times of each Omni clip's OWN audio, and Omni's speech track does not follow its
picture: Denise's clip "says" its second phrase while her mouth is shut. So this measures the mouth instead.

MediaPipe Face Landmarker (Tasks API, model face_landmarker.task in ~/.cache/badcode-lips/) on every frame: the inner-lip
gap (landmarks 13 and 14) over the face height (10 to 152). Talking is a mouth that keeps changing shape, so the signal
is the frame-to-frame change of that gap, smoothed over a fifth of a second; runs above a threshold are "the lips move".

usage: lips.py <video> [--face left|right|big] [--crop x0,y0,x1,y1] [--json out.json]
prints [[start, end], ...] in seconds, and the per-frame gap if --json is given
run with ~/.cache/badcode-lips/venv/bin/python
"""
import json, os, sys
import cv2, numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions

CROP = None   # (x0, y0, x1, y1) as fractions: track a 2x upscaled crop round the face (our faces are small)
MODEL = os.path.expanduser('~/.cache/badcode-lips/face_landmarker.task')

def landmarker():
    return vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=MODEL), num_faces=4, min_face_detection_confidence=0.3, min_face_presence_confidence=0.3))
def detect(lm, fr, crop):
    """faces in a 2x upscaled crop of the frame, landmarks mapped back to whole-frame fractions"""
    h, w = fr.shape[:2]; x0, y0, x1, y1 = crop
    img = cv2.resize(fr[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)], None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
    return [[(x0 + p.x * (x1 - x0), y0 + p.y * (y1 - y0)) for p in f] for f in r.face_landmarks]
def find_crop(path, lm, face):
    """the faces are too small for the detector at 1280x720 (found by trial, 2026-10-19), so try a grid of half-frame
    windows on a few frames and centre a crop on the chosen face"""
    cap = cv2.VideoCapture(path); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); found = []
    for k in (n // 8, n // 3, n // 2):
        cap.set(cv2.CAP_PROP_POS_FRAMES, k); ok, fr = cap.read()
        if not ok: continue
        for x0 in (0.0, 0.25, 0.5):
            for y0 in (0.0, 0.2, 0.4):
                for f in detect(lm, fr, (x0, y0, x0 + 0.5, y0 + 0.6)):
                    found.append((f[1][0], f[1][1], abs(f[152][1] - f[10][1])))
    if not found: return None
    c = (min(found) if face == 'left' else max(found) if face == 'right' else max(found, key=lambda q: q[2]))
    hh = max(0.3, c[2] * 2.6); ww = hh * 1.2
    return (max(0, c[0] - ww / 2), max(0, c[1] - hh / 2), min(1, c[0] + ww / 2), min(1, c[1] + hh / 2))
def gaps(path, face='big'):
    lm = landmarker(); crop = CROP or find_crop(path, lm, face)
    if crop is None: return [None], 24
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS) or 24; out = []
    while True:
        ok, fr = cap.read()
        if not ok: break
        fs = detect(lm, fr, crop); g = None
        if fs:
            size = lambda f: abs(f[152][1] - f[10][1])
            f = max(fs, key=size)
            g = abs(f[14][1] - f[13][1]) / max(1e-6, size(f))
        out.append(g)
    return out, fps

def runs(g, fps, thr=None, gap=0.3, min_len=0.25):
    a = np.array([np.nan if x is None else x for x in g], float)
    if np.isnan(a).all(): return [], 0.0
    a = np.where(np.isnan(a), np.nanmedian(a), a)
    d = np.abs(np.diff(a, prepend=a[0]))
    w = max(1, int(round(fps / 5))); m = np.convolve(d, np.ones(w) / w, mode='same')
    open_ = a > (np.percentile(a, 20) + 0.25 * (np.percentile(a, 95) - np.percentile(a, 20)))   # visibly apart
    thr = thr if thr is not None else max(0.004, np.percentile(m, 40))
    on = (m > thr) & open_
    # join runs separated by less than `gap`, drop runs shorter than min_len
    res, s = [], None
    for i, v in enumerate(on):
        if v and s is None: s = i
        if not v and s is not None: res.append([s, i]); s = None
    if s is not None: res.append([s, len(on)])
    j = []
    for r in res:
        if j and (r[0] - j[-1][1]) / fps < gap: j[-1][1] = r[1]
        else: j.append(r)
    return [[round(a_ / fps, 3), round(b / fps, 3)] for a_, b in j if (b - a_) / fps >= min_len], float(thr)

if __name__ == '__main__':
    if '--crop' in sys.argv: CROP = [float(x) for x in sys.argv[sys.argv.index('--crop') + 1].split(',')]
    p = sys.argv[1]; face = sys.argv[sys.argv.index('--face') + 1] if '--face' in sys.argv else 'big'
    g, fps = gaps(p, face); r, thr = runs(g, fps)
    print(json.dumps(r))
    if '--json' in sys.argv: json.dump({'fps': fps, 'gap': g, 'runs': r, 'thr': thr}, open(sys.argv[sys.argv.index('--json') + 1], 'w'))
