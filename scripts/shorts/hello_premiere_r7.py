#!/usr/bin/env python3
"""Hello, I'm BadCode (Short #17): Premiere media for rough cut 7 (Jack, 2026-11-19: "put it in Premiere").

    python3 scripts/shorts/hello_cut_r5.py --reel r7      # first: the cut, raw.mp4 and overlay-vf.json
    python3 scripts/shorts/hello_premiere_r7.py

Writes <media>/cut/r7/premiere-media/:
- one file per V1 shot, cut from cut/r7/_scratch/raw.mp4 (the 16mm film finish baked in, no captions, no handles),
- overlay.mov: the captions and the date stamps alone on a transparent canvas (ProRes 4444), for V2, so they can be
  moved, trimmed or switched off in Premiere (its scripting API cannot write text),
and cut/r7/edl-premiere.json (the cut's edl pointing V1 at those shots), ready for scripts/scene/premiere-plan.py.
"""
# style-lint: story=short-hello-im-badcode (this script belongs to one short)
import json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import hello_cut as r1  # noqa: E402

CUT = r1.MEDIA / 'cut/r7'
OUT = CUT / 'premiere-media'; OUT.mkdir(exist_ok=True)
RAW = CUT / '_scratch/raw.mp4'


def main():
    edl = json.loads((CUT / 'edl.json').read_text())
    rows = []
    for i, r in enumerate(edl['video']):
        name = pathlib.Path(r['file']).stem
        f = OUT / f'{i:02d}-{name}.mp4'
        r1.ff('-ss', f"{r['start']:.3f}", '-i', RAW, '-t', f"{r['dur']:.3f}", '-an', *r1.ENC, f)
        rows.append(dict(r, file=str(f), **{'in': 0}))
    ov = json.loads((CUT / 'overlay-vf.json').read_text())
    r1.ff('-f', 'lavfi', '-i', f"color=c=black@0.0:s={r1.W}x{r1.H}:r={r1.FPS}:d={ov['total']},format=yuva444p",
          '-vf', ','.join(ov['vf'] + ['format=yuva444p10le']), '-c:v', 'prores_ks', '-profile:v', '4444',
          '-pix_fmt', 'yuva444p10le', OUT / 'overlay.mov')
    edl.update({'video': rows, 'overlay': str(OUT / 'overlay.mov')})
    (CUT / 'edl-premiere.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'shots': len(rows), 'overlay': str(OUT / 'overlay.mov'), 'edl': str(CUT / 'edl-premiere.json')}))


if __name__ == '__main__':
    main()
