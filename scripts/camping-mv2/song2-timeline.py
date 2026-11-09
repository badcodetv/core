#!/usr/bin/env python3
"""Camping MV on song 2: rebuild a live Premiere sequence (e.g. `camping song 2 beat 6`) as a timeline page edl + preview.

    python3 scripts/camping-mv2/song2-timeline.py '<.bridge/state-<seq>.json>' <out-cut-dir> '<sequence name>'

Picture: the bridge's state dump, top enabled video track wins at every moment (effects, opacity, scaling not read), rebuilt in
ffmpeg; sound: A1 (the song) only, the clip sound tracks are muted in the sequence. No Premiere render (Jack 2026-10-19).
Beats = the song's sections (measured, docs/stories/camping/mv-song2/README.md); lines = the lyric, from faster-whisper
(mv-song2/analysis/words-new.json), with the bridge speakers from the lyric sheet (unverified on song 2).
Clip names: the shot id for round-10 clips (st = stadium, du = masked duo, re = real Bob/Tarquin, ly = lyric cutaway), NEW marks
the clips new in this cut.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
state = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = pathlib.Path(sys.argv[2])
SEQ = sys.argv[3]
seg_dir = out / 'segs'
seg_dir.mkdir(parents=True, exist_ok=True)
for old in seg_dir.glob('*.mp4'): old.unlink()
FPS = 25
TOTAL = state['sequence']['end']
SONG = next(c['mediaPath'] for t in state['audioTracks'] if t['label'] == 'A1' for c in t['items'])


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


vids = [(t['index'], c) for t in state['videoTracks'] for c in t.get('items', [])
        if c.get('start') is not None and not c.get('disabled') and c.get('mediaPath')]
cuts = sorted({0.0, TOTAL, *[c['start'] for _, c in vids], *[c['end'] for _, c in vids]})
segs = []
for a, b in zip(cuts, cuts[1:]):
    if b - a < 0.02:
        continue
    mid = (a + b) / 2
    top = max(((i, c) for i, c in vids if c['start'] <= mid < c['end']), key=lambda x: x[0], default=None)
    key = (top[0], top[1]['ref']) if top else None
    if segs and segs[-1]['key'] == key and abs(segs[-1]['end'] - a) < 1e-6:
        segs[-1]['end'] = b
        continue
    segs.append({'key': key, 'start': a, 'end': b, 'clip': top[1] if top else None, 'track': top[0] if top else None})

files = []
for n, s in enumerate(segs):
    f = seg_dir / f'{n:03d}.mp4'
    dur = s['end'] - s['start']
    nf = round(s['end'] * FPS) - round(s['start'] * FPS)  # frame-exact (2026-11-09: '-t' lost a frame here and there; 1.4 s by the end)
    vf = f'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1'
    if s['clip']:
        c = s['clip']
        src_t = c['inPoint'] + (s['start'] - c['start']) * c.get('speed', 1)
        ff('-ss', f'{src_t:.3f}', '-i', c['mediaPath'], '-an', '-vf', vf + ',tpad=stop_mode=clone:stop_duration=1', '-frames:v', nf,
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', f)
    else:
        ff('-f', 'lavfi', '-i', f'color=black:s=1280x720:r={FPS}', '-frames:v', nf, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f)
    files.append(f)
(seg_dir / 'list.txt').write_text(''.join(f"file '{f.name}'\n" for f in files))
picture = out / 'picture.mp4'
ff('-f', 'concat', '-safe', '0', '-i', seg_dir / 'list.txt', '-c', 'copy', picture)
ff('-i', picture, '-i', SONG, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{TOTAL:.3f}',
   out / 'preview.mp4')

SECTIONS = [('0', 'Opening: the stadium', 0.0, 'NEW: dark stadium, BADCODE on his screen on the first drum hit (2.76), lights slam on, the lit bowl on the bass (4.12), the crowd.'),
            ('1', 'Intro: the tunnel run', 10.96, 'Bob running through the tunnel, cut on the beat (beat 5).'),
            ('2', 'Verse 1 (Bob)', 19.87, ''), ('3', 'Hook 1', 55.32, ''), ('4', 'Verse 2 (Tarquin)', 77.13, ''),
            ('5', 'Hook 2', 120.76, ''),
            ('6', 'Bridge: the face-off', 142.56, 'NEW: the masked men rap at each other (du), cut with the real Bob and Tarquin arguing in the car park (re); cutaways on the words (ly, t21, b23, the Waitrose flashback); the clink on "same side"; both shout over the drum stop.'),
            ('7', 'Hook 3', 183.52, ''), ('8', 'Outro', 205.41, '')]
beats = []
for i, (bid, title, t0, see) in enumerate(SECTIONS):
    t1 = SECTIONS[i + 1][2] if i + 1 < len(SECTIONS) else TOTAL
    beats.append({'id': bid, 'title': title, 'start': t0, 'dur': round(t1 - t0, 3), 'see': see, 'lines': []})
WHO = [(143.6, 'Bob'), (148.7, 'Tarquin'), (152.8, 'both'), (159.6, 'Tarquin'), (165.3, 'Bob'), (171.0, 'Tarquin'),
       (175.0, 'Bob'), (181.7, 'both')]


def who(t):
    if 19 < t < 56: return 'Bob'
    if 77 < t < 121: return 'Tarquin'
    if 143 < t < 183.6: return next(w for s, w in reversed(WHO) if t >= s - 1e-6)
    return 'hook'


def beat_of(t):
    return next(b['id'] for b in reversed(beats) if t >= b['start'] - 1e-6)


for seg in json.loads((ROOT / 'docs/stories/camping/mv-song2/analysis/words-new.json').read_text()):
    if seg['text'].strip().startswith('Thank you for watching'): continue
    b = next(x for x in beats if x['id'] == beat_of(seg['start']))
    b['lines'].append({'i': len(b['lines']), 'who': who(seg['start']).lower(), 'name': who(seg['start']), 't': seg['start'],
                       'dur': round(seg['end'] - seg['start'], 3), 'text': seg['text'].strip(), 'by': 'kai'})


def label(p):
    m = re.search(r'/r10-(\w+?)-', p)
    if m: return f'NEW {m.group(1)}'
    m = re.search(r'/cb-(\w+?)-', p)
    if m: return f'rap {m.group(1)}'
    m = re.search(r'/ca-(\w+?)-', p)
    if m: return f'action {m.group(1)}'
    m = re.search(r'camping vid/(.+)$', p)
    return m.group(1) if m else pathlib.Path(p).name


video = [{'file': (label(s['clip']['mediaPath']) + f" (V{s['track'] + 1})") if s['clip'] else 'black',
          'source': (label(s['clip']['mediaPath']) + f" (V{s['track'] + 1})") if s['clip'] else 'black',
          'start': round(s['start'], 3), 'dur': round(s['end'] - s['start'], 3), 'beat': beat_of(s['start'] + 0.01)} for s in segs]
audio = [{'track': 'A1', 'name': 'mus-song 2'}]
events = [{'stem': 'mus-song 2', 't': 0.0, 'dur': round(TOTAL, 3), 'what': 'A1 song 2 maybe', 'src': SONG}]
flags = [
    "Picture rebuilt from the Premiere sequence in ffmpeg (top track wins); no Premiere render. Clip sound is muted in the sequence, so only the song plays.",
    "Bridge speakers come from the lyric sheet and are not checked by ear on song 2.",
    "du01 (143.92, 146.64): the posh man's triangle sits on his right eye in profile (not in your notes, so kept).",
    "Your one-beat blacks at 98.9, 120.7 and 133.7 stay.",
]
edl = {'sequence': SEQ, 'title': 'Camping MV Timeline', 'heading': f'Camping music video: {SEQ}',
       'intro': (f"The Premiere sequence `{SEQ}`, as it is now. NEW = round-10 clips (st stadium, du masked rappers, re real Bob and Tarquin, "
                 "ly lyric cutaways). Click any section, lyric line or clip to leave a note, or pin a note to the exact frame under the playhead."),
       'fps': FPS, 'total': round(TOTAL, 3), 'beats': beats, 'video': video, 'audio': audio, 'events': events, 'flags': flags}
(out / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'segments': len(segs), 'new': sum(1 for v in video if v['file'].startswith('NEW')), 'preview': str(out / 'preview.mp4')}))
