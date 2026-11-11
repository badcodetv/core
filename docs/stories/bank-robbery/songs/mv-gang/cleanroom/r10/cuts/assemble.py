"""Assemble one of the five cut-10 plans into a preview, an edl and a timeline page.
    python3 assemble.py A <page-out-dir>
<media>/cut10A/preview.mp4 + edl.json (song to 187.0 s, picture and sound fade over the last second), then the page."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
SC = HERE.parents[2]
sys.path.insert(0, str(SC.parents[4] / 'scripts' / 'scene'))
import timeline  # noqa: E402
L, OUT = sys.argv[1], sys.argv[2]
MEDIA = pathlib.Path('/mnt/d/badcode-videos/bank-robbery-music/gang'); VID = MEDIA / 'video'; NOIR = MEDIA.parent / 'noir' / 'video'
SONG = MEDIA.parent / 'the version.wav'
CUT = MEDIA / f'cut10{L}'; PARTS = CUT / 'parts'; PARTS.mkdir(parents=True, exist_ok=True)
END = 187.0
FADE = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0  # Kai on 10B: a 1 s fade is too aggressive, "just almost cut the audio off"
plan = json.load(open(HERE / f'plan-{L}.json'))
about = (HERE / f'about-{L}.md').read_text().strip() if (HERE / f'about-{L}.md').exists() else ''
NAMES = {'A': "Jack's cut, fixed", 'B': 'Strict alternation', 'C': 'On the words', 'D': 'Breathing', 'E': 'Energy curve', 'B2': 'Strict alternation, round 2 (on the kick)', 'B3': 'Strict alternation, round 3', 'B4': 'Strict alternation, round 4', 'B5': 'Strict alternation, round 5'}
def resolve(ref):
    return NOIR / (ref[3:] + '.mp4') if ref.startswith('cn:') else sorted(VID.glob(f'bg-{ref}-*.mp4'))[0]
BEATS = [("intro", "Intro", 0, 20.14), ("verse1", "Verse 1", 20.14, 41.2), ("verse2", "Verse 2", 41.2, 61.86),
         ("chorus1", "Chorus", 61.86, 82.76), ("verse3", "Verse 3", 82.76, 105.36), ("verse4", "Verse 4", 105.36, 123.74),
         ("chorus2", "Chorus", 123.74, 144.18), ("break", "Break", 144.18, 154.74), ("verse5", "Verse 5", 154.74, END)]
beat_of = lambda t: next((b[0] for b in BEATS if b[2] <= t < b[3] + 1e-6), BEATS[-1][0])
video, lines, listfile = [], {b[0]: [] for b in BEATS}, []
for i, r in enumerate(plan):
    src = resolve(r['clip'])
    fs, fe = round(r['start'] * 24), round(r['end'] * 24); d = (fe - fs) / 24
    part = PARTS / f'{i:03d}.mp4'; tag = part.with_suffix('.src'); key = f"{src}|{r['in']:.3f}|{d:.4f}"
    if not part.exists() or not tag.exists() or tag.read_text() != key:
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{r['in']:.3f}", '-i', str(src), '-t', f'{d:.4f}', '-an',
                        '-vf', 'scale=1280:720,fps=24,setsar=1', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', str(part)], check=True)
        tag.write_text(key)
    listfile.append(f"file '{part}'")
    b = beat_of(r['start'])
    video.append({'file': str(part), 'start': fs / 24, 'dur': d, 'beat': b, 'source': str(src), 'looped': False})
    lines[b].append({'i': len(lines[b]), 'who': 'song', 'name': 'the version.wav', 't': r['start'], 'dur': round(r['end'] - r['start'], 2),
                     'text': (r.get('line') or f"[{r['clip']}]") + (f"  [{r['clip']}: {r['why']}]" if r.get('why') else ''), 'by': 'claude'})
(CUT / 'list.txt').write_text('\n'.join(listfile) + '\n')
prev = CUT / 'preview.mp4'
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(CUT / 'list.txt'), '-t', str(END), '-i', str(SONG),
                '-map', '0:v', '-map', '1:a', '-vf', f'fade=t=out:st={END - FADE}:d={FADE}', '-af', f'afade=t=out:st={END - FADE}:d={FADE}',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-c:a', 'aac', '-b:a', '192k', '-t', str(END), str(prev)], check=True)
seq = f'Balaclava Gang 10{L}'
edl = {'sequence': seq, 'title': f'Gang Cut 10{L}', 'heading': f'The Bank Robbery MV, cut 10{L}: {NAMES.get(L, L)}',
       'intro': f'One of five cuts made from your cut-9 notes, each under a different rule (A Jack\'s cut fixed, B strict alternation, C on the words, '
                f'D breathing, E energy curve). This is {L}: {NAMES.get(L, L)}. Ends on "Don\'t just eat cake" at 3:07. Note the bits you like ("keep this chorus") '
                'and the bits you don\'t; the final cut takes the best of all five, then you finish it by hand in Premiere.',
       'fps': 24, 'total': END,
       'beats': [{'id': k, 'title': t, 'start': s, 'dur': round(e - s, 2), 'see': '', 'lines': lines[k]} for k, t, s, e in BEATS],
       'video': video, 'audio': [{'track': 'A1', 'name': 'mus-the version'}],
       'events': [{'stem': 'mus-the version', 't': 0, 'dur': END, 'what': 'the song', 'src': str(SONG)}],
       'flags': [about] if about else [],
       **(json.loads((HERE / f'replies-{L}.json').read_text()) if (HERE / f'replies-{L}.json').exists() else {})}
(CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
print(json.dumps(timeline.build(edl, prev, OUT)))
