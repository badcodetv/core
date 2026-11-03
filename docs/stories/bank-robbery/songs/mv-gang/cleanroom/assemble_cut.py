"""Usage: python3 assemble_cut.py [r2]   (r2 → edit-plan-r2.json, <media>/cut2/, sequence Balaclava Gang 2)
Assemble the timeline-page cut of `Balaclava Gang 1` outside Premiere: <media>/cut/preview.mp4 + edl.json.
Same cuts as the Premiere sequence (edit-plan.json, c01-b → a02-b / a02-a because Flow refused it).
    python3 assemble_cut.py"""
import glob, json, pathlib, subprocess, sys
R = sys.argv[1] if len(sys.argv) > 1 else ''
HERE = pathlib.Path(__file__).parent
SC = HERE.parent
cfg = json.load(open(SC / 'scene.json'))
MEDIA = pathlib.Path(cfg['media']); VID = MEDIA / 'video'; CUT = MEDIA / ('cut2' if R == 'r2' else 'cut'); PARTS = CUT / 'parts'
PARTS.mkdir(parents=True, exist_ok=True)
SONG = pathlib.Path(cfg['song'])
plan = json.load(open(SC / ('edit-plan-r2.json' if R == 'r2' else 'edit-plan.json')))
NOIR = MEDIA.parent / 'noir' / 'video'
def resolve(ref):
    return NOIR / (ref[3:] + '.mp4') if ref.startswith('cn:') else sorted(VID.glob(f'bg-{ref}-*.mp4'))[0]
SUB = {('c01-b', 61.86): 'a02-b', ('c01-b', 123.74): 'a02-a'}
BEATS = [("intro", "Intro", 0, 20.14), ("verse1", "Verse 1", 20.14, 41.2), ("verse2", "Verse 2", 41.2, 61.86),
         ("chorus1", "Chorus", 61.86, 82.76), ("verse3", "Verse 3", 82.76, 105.36), ("verse4", "Verse 4", 105.36, 123.74),
         ("chorus2", "Chorus", 123.74, 144.18), ("break", "Break", 144.18, 154.74), ("verse5", "Verse 5", 154.74, 188.46),
         ("outro", "Outro", 188.46, 209.6)]
beat_of = lambda t: next(b[0] for b in BEATS if b[2] <= t < b[3] + 1e-6)
video, lines, listfile = [], {b[0]: [] for b in BEATS}, []
for i, r in enumerate(plan):
    clip = SUB.get((r['clip'], r['start']), r['clip'])
    src = resolve(clip)
    frames_s = round(r['start'] * 24); frames_e = round(r['end'] * 24); d = (frames_e - frames_s) / 24
    part = PARTS / f'{i:02d}.mp4'
    if not part.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-t', f'{d:.4f}', '-an',
                        '-vf', 'scale=1280:720,fps=24,setsar=1', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', str(part)], check=True)
    listfile.append(f"file '{part}'")
    b = beat_of(r.get('start_line', r['start']))
    video.append({'file': str(part), 'start': frames_s / 24, 'dur': d, 'beat': b, 'source': str(src), 'looped': False})
    lines[b].append({'i': len(lines[b]), 'who': 'song', 'name': 'the version.wav', 't': r['start'], 'dur': round(r['end'] - r['start'], 2),
                     'text': r['line'] + (f"  [{r['why']}]" if r.get('why') else ('' if clip == r['clip'] else f'  [{clip} stands in for {r["clip"]}, refused by Flow]')), 'by': 'kai'})
(CUT / 'list.txt').write_text('\n'.join(listfile) + '\n')
prev = CUT / 'preview.mp4'
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(CUT / 'list.txt'), '-i', str(SONG),
                '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(prev)], check=True)
total = 209.6
SEQ = 'Balaclava Gang 2' if R == 'r2' else 'Balaclava Gang 1'
edl = {'sequence': SEQ, 'title': 'Balaclava Gang Timeline', 'heading': f'The Bank Robbery MV: the balaclava gang, {SEQ}',
       'intro': f'The {SEQ} cut (same as the Premiere sequence in bank robbery.prproj): 65 shots on the lines of "the version.wav". '
                'Play it, click any section, shot or line and leave a note in its yellow slip, or pin one to a frame. Tell Claude when you are done.',
       'fps': 24, 'total': total,
       'beats': [{'id': k, 'title': t, 'start': s, 'dur': round(e - s, 2), 'see': '', 'lines': lines[k]} for k, t, s, e in BEATS],
       'video': video,
       'audio': [{'track': 'A1', 'name': 'mus-the version'}],
       'events': [{'stem': 'mus-the version', 't': 0, 'dur': total, 'what': 'the song', 'src': str(SONG)}],
       'flags': ['c01-b (the gang chanting in the bank lobby) was refused by Flow three times: the doors-bursting-in clips stand in at 1:02 and 2:04.',
                 'Lines whose still was not picked use the nearest picked clip (marked "not picked" in the line text).',
                 ('Cuts snapped to the strongest drum hit near each line (within 0.33 s).' if R == 'r2' else 'Cuts sit on Whisper\'s line starts (loose by ~0.3 s), not yet on the beat.'),
                 ('Shop sign readable in c02 ("BUTCHER\'S SHOP"). Colour Noir action clips are back (marked in the line text).' if R == 'r2' else 'Shop signs readable in x01 ("BAKERY") and c02 ("BUTCHER\'S SHOP").')]}
(CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
print(len(video), 'shots', prev)
