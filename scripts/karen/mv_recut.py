#!/usr/bin/env python3
"""Karen music video re-cut: plan -> beat-snapped picture cut -> preview + timeline edl.

    python3 scripts/karen/mv_recut.py r1

Reads docs/stories/karen/scenes/music-video/{song-map,catalogue,cut-<r>-plan,lyric-times}.json.
Each plan shot is [clip id, beats, in-point s, why]; a shot's start and end land on beats from
song-map.json, and a section's last shot (beats null) fills to the section's end.
Writes <media>/cut-<r>/{edl.json, preview.mp4, segs/} where media = karen-music/clips/recut.
Picture only from the clips; the sound is song.wav. Rendered 1920x1080 at 25 fps (the sequence rate).
"""
import json
import pathlib
import subprocess
import sys

R = sys.argv[1] if len(sys.argv) > 1 else 'r1'
SCENE = pathlib.Path(__file__).resolve().parents[2] / 'docs/stories/karen/scenes/music-video'
MEDIA = pathlib.Path('/mnt/d/badcode-videos/karen-music/clips/recut')
NEW = pathlib.Path('/mnt/d/badcode-videos/karen-music/clips/recut-cartoon')
SONG = '/mnt/d/badcode-videos/karen-music/song.wav'
FPS = 25

song = json.loads((SCENE / 'song-map.json').read_text())
cat = {i['id']: i for i in json.loads((SCENE / 'catalogue.json').read_text())['items']}
_plan = json.loads((SCENE / f'cut-{R}-plan.json').read_text())
if 'at' in _plan:  # r2+: absolute strong-beat starts, choruses inherited from an earlier round
    base = json.loads((SCENE / f"cut-{_plan['inherit']['from']}-plan.json").read_text())['sections']
    plan = {k: base[k] for k in _plan['inherit']['sections']}
    at_plan = _plan['at']
else:
    plan, at_plan = _plan['sections'], {}
lyrics = json.loads((SCENE / 'lyric-times.json').read_text())['lines']
beats = song['beats']
out = MEDIA / f'cut-{R}'
segs = out / 'segs'
segs.mkdir(parents=True, exist_ok=True)


def probe(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def source(cid):
    if cid in cat:
        return pathlib.Path(cat[cid]['path']), cat[cid]['style']
    p = NEW / f'{cid}.mp4'
    if p.exists():
        return p, 'cartoon'
    raise SystemExit(f'unknown clip {cid}')


snap = lambda t: round(round(t * FPS) / FPS, 4)
video, flags, shots = [], [], []
strong = song.get('strong')
starts = []  # (time, cid, inp, why, section)
for sec in song['sections']:
    sid = sec['id']
    if sid in at_plan:
        for cid, at, inp, why in at_plan[sid]:
            if strong and not strong[at]:
                flags.append(f"{sid}: '{cid}' starts on beat {at}, which is not a strong beat")
            starts.append((0.0 if at == 0 else beats[at], cid, inp, why, sid))
        continue
    k = min(range(len(beats)), key=lambda i: abs(beats[i] - sec['start']))
    k += _plan.get('inherit', {}).get('shift', {}).get(sid, 0)  # r4: move a whole inherited section onto the kick
    t = 0.0 if sid == 'intro' else beats[k]
    for cid, nb, inp, why in plan[sid]:
        starts.append((t, cid, inp, why, sid))
        if nb:
            k += nb
            t = beats[k]
starts.sort(key=lambda x: x[0])
for n, (t, cid, inp, why, sid) in enumerate(starts):
    end = starts[n + 1][0] if n + 1 < len(starts) else song['duration']
    a, b = snap(t), snap(end)
    src, style = source(cid)
    dur = probe(src)
    inp = inp or 0.0
    want = b - a
    looped, slow = False, None
    if inp + want > dur - 0.05:
        inp2 = max(0.0, dur - 0.05 - want)
        if inp2 < inp:
            flags.append(f"{sid} {a:.2f}s: '{cid}' in-point moved {inp:.1f}->{inp2:.1f}s to fit {want:.2f}s")
        inp = inp2
        if want > dur - 0.05:
            if want <= (dur - inp) * 1.4:
                slow = round(want / (dur - 0.05 - inp), 3)
                flags.append(f"{sid} {a:.2f}s: '{cid}' is {dur:.1f}s, needs {want:.2f}s: slowed to {1/slow:.0%} speed")
            else:
                looped = True
                flags.append(f"{sid} {a:.2f}s: '{cid}' is {dur:.1f}s, needs {want:.2f}s: played forward then back")
    pool = 'cartoon' if sid in ('chorus-1', 'chorus-2', 'final-chorus', 'break') else 'photo'
    if style != pool:
        flags.append(f"{sid} {a:.2f}s: '{cid}' is {style} in a {pool} section")
    chars = [c.lower() for c in (cat.get(cid, {}).get('characters') or [])]
    if style == 'photo' and any('karen' in c for c in chars):
        flags.append(f"{sid} {a:.2f}s: '{cid}' shows Karen (photographic)")
    shots.append(dict(cid=cid, src=str(src), start=a, dur=round(b - a, 4), inp=round(inp, 3), looped=looped, slow=slow,
                      beat=sid, why=why))

# render each shot to a uniform segment, then concat and lay the song under it
listfile = out / 'segs.txt'
with listfile.open('w') as lf:
    for i, s in enumerate(shots):
        seg = segs / f'{i:03d}.mp4'
        frames = round(s['dur'] * FPS)
        vf = 'scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=25'
        if s.get('slow'):
            vf = f"setpts={s['slow']}*PTS," + vf
        if s['looped']:
            vf = 'split[f][r];[r]reverse[rv];[f][rv]concat=n=2:v=1,' + vf
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', str(s['inp']), '-i', s['src'], '-an',
               '-filter_complex' if s['looped'] else '-vf', vf, '-frames:v', str(frames),
               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', str(seg)]
        subprocess.run(cmd, check=True)
        lf.write(f"file '{seg}'\n")
        video.append({'file': str(seg), 'start': s['start'], 'dur': s['dur'], 'beat': s['beat'], 'source': s['src'],
                      'looped': s['looped'], 'in': s['inp'], 'why': s['why'], 'id': s['cid']})
pic = out / 'picture.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(listfile), '-c', 'copy', str(pic)], check=True)
prev = out / 'preview.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(pic), '-i', SONG, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                '-c:a', 'aac', '-b:a', '192k', '-shortest', str(prev)], check=True)

INTRO = {'r4': ('Round 4: the choruses onto the kick. Both choruses, the spy-riff break and the final chorus started on a snare beat, so every chorus cut was half a bar off, as you heard. Each now starts one beat later, on the kick, with the same cuts; the verses are round 3, unchanged.'), 'r3': ('Round 3: the timing fix. Every cut outside the choruses now lands on the kick (beats 1 and 3) instead of the snare; verse 1 opens exactly on the drop at 27.33 s. Choruses unchanged. Play it and note anything that still feels off.'), 'r2': ('Round 2. Your notes: no photographic Karen, more abstract, more of Aarron and the band, and the verses on the '
                 'beat. Every verse shot now starts on the strong beat where its sung line starts (round 1 ran a line ahead in '
                 'verse 1), the band fills the gaps between lines, and the choruses and break are exactly as before. '
                 'Click any section or shot and leave a note in its yellow slip.')}
titles = {'intro': 'Intro: the phone menu', 'verse-1': 'Verse 1: Monday, nine-oh-five', 'pre-chorus-1': 'Pre-chorus 1',
          'chorus-1': 'Chorus 1 (cartoon)', 'verse-2': 'Verse 2: Regional office', 'pre-chorus-2': 'Pre-chorus 2',
          'chorus-2': 'Chorus 2 (cartoon)', 'break': 'Break: the spy riff (cartoon)', 'bridge': 'Bridge: six weeks in a phone box',
          'verse-3': 'Verse 3: Deputy Secretary', 'final-chorus': 'Final chorus (cartoon)', 'outro': 'Outro: the President'}
beats_out = []
for sec in song['sections']:
    ls = [l for l in lyrics if sec['start'] - 0.3 <= l['t'] < sec['end'] - 0.3]
    nxt = lambda i: ls[i + 1]['t'] if i + 1 < len(ls) else sec['end']
    n_shots = sum(1 for v in video if v['beat'] == sec['id'])
    beats_out.append({'id': sec['id'], 'title': titles[sec['id']], 'start': sec['start'], 'dur': round(sec['end'] - sec['start'], 3),
                      'see': f"{n_shots} shots over {sec['beats']} beats ({sec['confidence']} boundary). {sec['note']}",
                      'act': sec['pool'],
                      'lines': [{'i': i, 'who': l['who'], 'name': l['who'].title(), 't': l['t'], 'dur': round(nxt(i) - l['t'], 2),
                                 'text': l['text'], 'by': 'kai'} for i, l in enumerate(ls)]})
edl = {'sequence': f'karen-music-{R}', 'title': 'Karen Music Re-cut', 'round': int(R[1:]), 'heading': 'All Day to Complain: the re-cut',
       'intro': INTRO.get(R) or ('Round 1 of the Karen music video re-cut. Every picture change lands on a beat of the song (89 BPM); '
                 'choruses and the spy-riff break are cartoon, everything else is filmed-look footage from the music '
                 'and story projects. The 14 new cartoon clips are marked c01–c14. Play it, click any section or shot, '
                 'and leave a note in its yellow slip.'),
       'fps': FPS, 'total': song['duration'], 'beats': beats_out, 'video': video,
       'audio': [{'track': 'A1', 'name': 'mus-song'}],
       'events': [{'stem': 'mus-song', 't': 0.0, 'dur': song['duration'], 'what': 'All Day to Complain (song.wav)', 'src': SONG}],
       'flags': flags}
(out / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'shots': len(shots), 'flags': flags, 'preview': str(prev), 'length': probe(prev)}, indent=1))
