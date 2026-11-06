#!/usr/bin/env python3
"""Camping MV (balaclava swap): rebuild the live Premiere sequence `camping` as a timeline page edl + preview.

    python3 scripts/camping-mv2/balaclava-timeline.py <state-<seq>.json> <out-cut-dir> [sequence name]

Reads the bridge's state dump (premiere_get_sequence, params:false), works out which video clip is on top at every
moment (the highest enabled track wins; effects, opacity and scaling are NOT read, so a picture-in-picture shows as
the top clip full frame), and rebuilds that picture in ffmpeg with the song (A1) and the unmuted clip sound (A6).
Every rap-to-camera slot the balaclava men will replace is named "SWAP <shot> · <original>" on V1 of the page.
No Premiere render (Jack 2026-10-19: no renders).
"""
import json
import pathlib
import re
import subprocess
import sys

state = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = pathlib.Path(sys.argv[2])
seg_dir = out / 'segs'
seg_dir.mkdir(parents=True, exist_ok=True)
FPS = 25
TOTAL = state['sequence']['end']

SWAP = {'bob rapping/1.mp4': 's01', 'bob rapping/1.1.mp4': 's02', 'bob rapping/2.mp4': 's03', 'bob rapping/3.mov': 's04',
        'bob rapping/4.mp4': 's05', 'bob rapping/5.5.mp4': 's06', 'clips/12.mp4': 'm12', 'clips/13.mp4': 'm13',
        'Tarquin rapping/1.mp4': 't01', 'Tarquin rapping/2.mp4': 't02', 'Tarquin rapping/2.1.mp4': 't03',
        'Tarquin rapping/3.mp4': 't04', 'Tarquin rapping/4.3.mp4': 't05', 'Tarquin rapping/4.4.mp4': 't06',
        'Tarquin rapping/5.mp4': 't07', 'Tarquin rapping/6.mp4': 't08', 'clips/19.mp4': 'm19', 'clips/23.mp4': 'm23'}


def swap_id(path):
    m = re.search(r'/cb-(\w+)-[\w-]+\.mp4$', path)
    if m:
        return m.group(1)
    for k, v in SWAP.items():
        if path.endswith('/' + k):
            return v


def label(path):
    m = re.search(r'/clips/(.+)$', path)
    return m.group(1) if m else pathlib.Path(path).name


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


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


files = []
for n, s in enumerate(segs):
    f = seg_dir / f'{n:03d}.mp4'
    dur = s['end'] - s['start']
    vf = f'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1'
    if s['clip']:
        c = s['clip']
        src_t = c['inPoint'] + (s['start'] - c['start']) * c.get('speed', 1)
        ff('-ss', f'{src_t:.3f}', '-i', c['mediaPath'], '-t', f'{dur:.3f}', '-an', '-vf', vf,
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', f)
    else:
        ff('-f', 'lavfi', '-i', f'color=black:s=1280x720:r={FPS}', '-t', f'{dur:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f)
    files.append(f)

(seg_dir / 'list.txt').write_text(''.join(f"file '{f.name}'\n" for f in files))
picture = out / 'picture.mp4'
ff('-f', 'concat', '-safe', '0', '-i', seg_dir / 'list.txt', '-c', 'copy', picture)

# sound: A1 (song) + every unmuted clip sound on other tracks
auds = [(t, c) for t in state['audioTracks'] if not t['muted'] for c in t.get('items', [])
        if c.get('start') is not None and not c.get('disabled') and c.get('mediaPath')]
inputs, chains, mix = ['-i', picture], [], []
for k, (t, c) in enumerate(auds, start=1):
    inputs += ['-ss', f"{c['inPoint']:.3f}", '-t', f"{c['end'] - c['start']:.3f}", '-i', c['mediaPath']]
    ms = int(round(c['start'] * 1000))
    chains.append(f'[{k}:a]aresample=48000,adelay={ms}|{ms}[a{k}]')
    mix.append(f'[a{k}]')
fc = ';'.join(chains) + f";{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=longest[aout]"
ff(*inputs, '-filter_complex', fc, '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
   '-t', f'{TOTAL:.3f}', out / 'preview.mp4')

# edl in the timeline format (scripts/scene/timeline.py)
rap = [s for s in segs if s['clip'] and swap_id(s['clip']['mediaPath'])]
bob = [s for s in rap if swap_id(s['clip']['mediaPath'])[0] in 'sm' and s['start'] < 80]
tarq = [s for s in rap if s['start'] >= 80]
b0, b1 = bob[0]['start'], bob[-1]['end']
t0, t1 = tarq[0]['start'], tarq[-1]['end']
beats = [
    {'id': '0', 'title': 'Before the rap', 'start': 0, 'dur': b0, 'see': 'Unchanged.'},
    {'id': '1', 'title': "Bob's verse → duct-tape man", 'start': b0, 'dur': b1 - b0,
     'see': "Every clip named SWAP gets the duct-tape man (s01–s06, m12, m13). Action shots between them stay."},
    {'id': '2', 'title': 'Between the verses', 'start': b1, 'dur': t0 - b1, 'see': 'Unchanged.'},
    {'id': '3', 'title': "Tarquin's verse → tweed squire", 'start': t0, 'dur': t1 - t0,
     'see': 'Every clip named SWAP gets the tweed squire (t03–t08). Action shots between them stay.'},
    {'id': '4', 'title': 'After the rap', 'start': t1, 'dur': TOTAL - t1, 'see': 'Unchanged.'},
]


def beat_of(t):
    return next(b['id'] for b in reversed(beats) if t >= b['start'] - 1e-6)


video = []
for s in segs:
    if not s['clip']:
        name = 'black (gap)'
    else:
        p = s['clip']['mediaPath']
        sid = swap_id(p)
        tag = 'NEW' if '/cb-' in p else 'SWAP'
        name = f"{tag} {sid} · {label(p)} (V{s['track'] + 1})" if sid else f"{label(p)} (V{s['track'] + 1})"
    video.append({'file': name, 'source': name, 'start': round(s['start'], 3), 'dur': round(s['end'] - s['start'], 3),
                  'beat': beat_of(s['start'] + 0.01)})

audio = [{'track': 'A1', 'name': 'mus-song'}, {'track': 'A6', 'name': 'sfx-clip sound'}]
events = [{'stem': 'mus-song' if t['label'] == 'A1' else 'sfx-clip sound', 't': round(c['start'], 3),
           'dur': round(c['end'] - c['start'], 3), 'what': f"{t['label']} {label(c['mediaPath'])}", 'src': c['mediaPath']}
          for t, c in auds]

on_tl = {swap_id(c['mediaPath']) for _, c in vids if swap_id(c['mediaPath'])}
seen = {swap_id(s['clip']['mediaPath']) for s in rap}
hidden = sorted(on_tl - seen)
missing = sorted(set(SWAP.values()) - on_tl)
flags = [
    f"Not on the timeline at all: {', '.join(missing)} (stills made, but there is no slot for them).",
    f"On the timeline but always covered by a higher track, so never seen: {', '.join(hidden) or 'none'}.",
    "Picture rebuilt from the Premiere sequence in ffmpeg (top track wins); effects, opacity and scaling are not shown. No Premiere render.",
]
SEQ = sys.argv[3] if len(sys.argv) > 3 else 'camping'
edl = {'sequence': SEQ, 'title': 'Camping MV Timeline', 'heading': f'Camping music video: {SEQ}',
       'intro': (f"The Premiere sequence `{SEQ}`. Clips named NEW are the balaclava men in the rap-to-camera slots (SWAP = an "
                 "original rap shot still to replace); everything else is the original cut. Click any clip or beat to leave a note."),
       'fps': FPS, 'total': round(TOTAL, 3), 'beats': beats, 'video': video, 'audio': audio, 'events': events, 'flags': flags}
(out / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'segments': len(segs), 'swap_segments': len(rap), 'hidden': hidden, 'missing': missing,
                  'bob': [b0, b1], 'tarquin': [t0, t1]}))
