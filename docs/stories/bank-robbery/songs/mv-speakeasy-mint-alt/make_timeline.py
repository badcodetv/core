"""Timeline (new-scene stage 4) for the whole ALT film. Round 1 (2026-10-28): 33 scenes, 8 s each. Round 2: scene 1 is
shown as its three options back to back (01A inside the getaway car, 01B the slide under the El, 01C three 2.67 s
shots), then scenes 2-33. One beat per segment (act = song section), Kai's lyric as the line, A1 = the clips' own
Omni sound. Normalises each piece to 24 fps / 48 kHz first (a raw concat broke timestamps). Keeps the round's plan and
replies from cut-notes.json. Writes <media>/cut/preview.mp4, sfx-omni.wav, edl.json."""
import json, pathlib, subprocess, importlib.util
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location('r3', HERE / 'make_rows_r3.py'); r3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r3)
cfg = json.loads((HERE / 'scene.json').read_text())
MEDIA = pathlib.Path(cfg['media']); VID = MEDIA / 'video'; CUT = MEDIA / 'cut'; CUT.mkdir(exist_ok=True)
TAKE = {6: 'sma-06-r2-B06-a', 17: 'sma-17-r2-B17-b', 25: 'sma-25-r2-A25-b'}
sb = {f['n']: f for f in json.loads((HERE / 'storyboard.json').read_text())['frames']}
D = 8.0
lyric = {n: (act, ly, layer, tx) for n, act, ly, layer, args, tx, body in r3.S}
# segments: (beat id, title, act, see, [(file, in, dur)])
segs = [
 ('1A', '01A · option A: inside the getaway car', 'v1', 'Option A. Light trails under the elevated railway; the police lamps in the rear window.', [(VID / 'sma-01A-O1A-a.mp4', 0, D)]),
 ('1B', '01B · option B: the slide under the El', 'v1', 'Option B. One sedan sliding sideways, sparks, time-smear.', [(VID / 'sma-01B-O1B-b.mp4', 0, D)]),
 ('1C', '01C · option C: three quick shots', 'v1', 'Option C. Wheel, gun, police lamp, 2.67 s each.', [(VID / f'sma-01C{i}-{s}.mp4', 0.5, D / 3) for i, s in ((1, 'O1C1-a'), (2, 'O1C2-b'), (3, 'O1C3-b'))]),
]
for n in range(2, 34):
    act, ly, layer, tx = lyric[n]
    f = VID / (TAKE.get(n, f"sma-{n:02d}-{sb[n]['stills'][0]}") + '.mp4')
    segs.append((str(n), f'{n:02d} · {layer}', act, f'Layer: {layer}. Transition out: {tx}.', [(f, 0, D)]))
NORM = CUT / 'norm2'; NORM.mkdir(exist_ok=True)
parts, beats, video, events, t = [], [], [], [], 0.0
for bid, title, act, see, pieces in segs:
    bstart = t
    for f, i0, d in pieces:
        assert f.exists(), f
        o = NORM / f'{len(parts):03d}.mp4'
        if not o.exists():
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(i0), '-i', f, '-f', 'lavfi', '-t', str(d), '-i', 'anullsrc=r=48000:cl=stereo',
                            '-filter_complex', f'[0:v]fps=24,scale=1280:720,setsar=1,trim=0:{d},setpts=PTS-STARTPTS[v];'
                            f'[0:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=0:{d},asetpts=PTS-STARTPTS[a]',
                            '-map', '[v]', '-map', '[a]', '-t', str(d), '-c:v', 'libx264', '-preset', 'fast', '-crf', '20',
                            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', o], check=True)
        parts.append(o)
        video.append({'file': str(f), 'start': round(t, 3), 'dur': d, 'beat': bid, 'source': str(f), 'looped': False})
        events.append({'stem': 'sfx-omni', 't': round(t, 3), 'dur': d, 'what': f'{title} sound (from the clip)', 'src': str(f)})
        t += d
    ly = lyric[1][1] if bid.startswith('1') else lyric[int(bid)][1]
    beats.append({'id': bid, 'title': title, 'start': round(bstart, 3), 'dur': round(t - bstart, 3), 'act': r3.ACTS[act], 'see': see,
                  'lines': [{'i': 0, 'who': 'song', 'name': 'Lyric (Kai)', 't': None, 'dur': 0, 'text': ly, 'by': 'kai'}]})
pv = CUT / 'preview.mp4'
lst = CUT / 'concat.txt'; lst.write_text(''.join(f"file '{o}'\n" for o in parts))
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', pv], check=True)
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', pv, '-vn', '-ac', '2', '-ar', '48000', CUT / 'sfx-omni.wav'], check=True)
notes = json.loads((HERE / 'cut-notes.json').read_text()) if (HERE / 'cut-notes.json').exists() else {}
edl = {'sequence': 'speakeasy-mint-alt-rough1', 'title': 'Speakeasy ALT Timeline', 'heading': 'The Speakeasy Mint ALT · rough 1',
       'intro': "The whole ALT film, scenes in film order, the clips' own sound effects on A1, the lyric shown as each scene's "
                "line. Round 2: scene 1 plays as its three options back to back (A, B, C), then scene 2 onwards. "
                "Leave a note in any yellow slip, or pin one to a frame. Tell Claude when you're done.",
       'fps': 24, 'total': round(t, 3), 'beats': beats, 'video': video, 'audio': [{'track': 'A1', 'name': 'sfx-omni'}], 'events': events,
       'flags': ['No song on this cut: the Bank Robbery take is not picked yet, so nothing is timed to the music.',
                 'Scene 1 appears three times (options A, B, C); keep one.',
                 'Every other clip runs its full 8 s; no trims, Premiere camera moves or match-cut transitions yet.',
                 'Scene 16 still has a cream baked-in border at the edges (crop ~106% in Premiere).'],
       **{k: notes[k] for k in ('round', 'plan', 'replies') if k in notes}}
(CUT / 'edl.json').write_text(json.dumps(edl, indent=1))
print('ok', round(t, 1), 's')
