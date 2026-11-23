#!/usr/bin/env python3
"""check-cut.py <edl.json> [<audio root> ...]   (2026-11-23, The Den: two bugs put every voice early)

The two checks that would have caught them, run on a BUILT cut before anyone measures a mouth:

1. Every voice event lands where the edl says. Each event's take (its `src`, found under the audio roots or the
   cut's media folder) is cross-correlated against its built stem; |actual - planned| must be under 30 ms.
   Bug it catches: a mix of `adelay` + `amix` with no input starting at 0 begins at the first line and the WAV drops
   that gap, so every line plays early by the first line's start (The Den rough cuts 1-3: 0.35 s).
2. The preview and the timeline page's full-quality stream start picture and sound at 0 (ffprobe start_time).
   Bug it catches: libx264 B-frames in a fragmented MP4 start the picture 0.083 s late (every timeline page,
   2026-11-05 to 2026-11-23).

Exit 1 on any failure. Tempo per event = the take's length / the event's dur; searched (0.9-1.2) when that is missing.
"""
import json, pathlib, subprocess, sys
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'drive'))
from localmap import localize  # noqa: E402

SR = 8000


def load(f, tempo=1.0):
    return np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(f), '-af', f'atempo={tempo}', '-ac', '1',
                                         '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)


def starts(f):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,start_time', '-of', 'csv=p=0', str(f)],
                         capture_output=True, text=True).stdout
    return {l.split(',')[0]: float(l.split(',')[1]) for l in out.split() if ',' in l and l.split(',')[1] not in ('', 'N/A')}


def main():
    edl_path = pathlib.Path(sys.argv[1]); e = localize(json.loads(edl_path.read_text()))
    roots = [pathlib.Path(r) for r in sys.argv[2:]] + [edl_path.parent.parent.parent / 'audio', edl_path.parent]
    bad = 0
    stems = {a.get('name'): a['file'] for a in e.get('audio', []) if a.get('file')}
    cache = {}
    for ev in e.get('events', []):
        stem = ev.get('stem', '')
        if not stem.startswith('vox') or stem not in stems: continue
        src = pathlib.Path(ev['src'])
        f = next((c for r in roots for c in ([r / src] + list(r.rglob(src.name))) if c.exists()), None) if not src.is_absolute() else src
        if not f or not f.exists(): print(f"?    {ev['what'][:50]}: take not found ({ev['src']})"); continue
        if stem not in cache: cache[stem] = load(stems[stem])
        s = cache[stem]; t0 = int(ev['t'] * SR); lo = max(0, t0 - SR); best = None

        def trial(tempo):
            tk = load(f, tempo)
            if len(s[lo:t0 + len(tk) + SR]) < len(tk): return None
            c = np.correlate(s[lo:t0 + len(tk) + SR], tk, 'valid'); k = int(np.argmax(np.abs(c)))
            return (abs(c[k]) / (np.linalg.norm(tk) + 1e-9), (lo + k) / SR - ev['t'], float(tempo))
        # the event's dur is the take's length / its tempo (as the cut scripts write it): use that tempo when it reads sane;
        # otherwise search coarse, then 0.01 steps (near 1.0 a whole-take match at the wrong tempo lands mid-take: -0.03 s)
        n = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)],
                                 capture_output=True, text=True).stdout or 0)
        if ev.get('dur') and 0.85 < n / ev['dur'] < 1.3:
            best = trial(round(n / ev['dur'], 3))
        for tempo in (() if best else (0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2)):
            r = trial(tempo); best = r if r and (best is None or r[0] > best[0]) else best
        if best and not (ev.get('dur') and 0.85 < n / ev['dur'] < 1.3):
            for tempo in np.round(np.arange(best[2] - 0.04, best[2] + 0.041, 0.01), 2):
                r = trial(tempo); best = r if r and r[0] > best[0] else best
        ok = best and abs(best[1]) < 0.03
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'}  {ev['what'][:50]:52s} planned {ev['t']:7.3f}  off {best[1]:+.3f} s (x{best[2]})")
    for f in [edl_path.parent / 'preview.mp4', *edl_path.parent.glob('hq*.mp4')]:
        if f.exists():
            st = starts(f); ok = all(abs(v) < 0.001 for v in st.values()); bad += not ok
            print(f"{'ok ' if ok else 'BAD'}  {f.name}: stream starts {st}")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
