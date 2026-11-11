"""Cut 10 prep (Kai 2026-11-11: five different cuts to choose bits from).
Writes, beside this file:
  strips/<clip>.jpg   six frames of each clip (0.5 s … end), for the describers to look at
  pool.json           every clip on this machine: ref, file, seconds, what it was asked to show, where cut 9 used it
  music-map.json      lines, beats, bars, sections, the strong hits, loudness per bar, the events Kai named
  anchors.md          Kai's 28 cut-9 notes, each with the shot cut 9 had at that moment
    python3 prep.py [--strips]"""
import glob, json, pathlib, re, subprocess, sys
import numpy as np
HERE = pathlib.Path(__file__).parent
SC = HERE.parents[2]
MEDIA = pathlib.Path('/mnt/d/badcode-videos/bank-robbery-music/gang')
VID = MEDIA / 'video'; NOIR = MEDIA.parent / 'noir' / 'video'
SONG = MEDIA.parent / 'the version.wav'
END = 187.0  # Kai: end on "Don't just eat cake"

def ffdur(f):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)], capture_output=True, text=True).stdout)

# ---- pool
plan9 = json.load(open(SC / 'edit-plan-r9.json'))
vj = json.load(open(SC / 'video-jobs.json'))
asked = {j['key']: j.get('motion', '').replace('\n\nThanks.', '') for j in vj.get('extra', [])}
pool = []
for f in sorted(VID.glob('bg-*.mp4')):
    m = re.match(r'bg-(.+?-[a-z])-(.+)\.mp4$', f.name)
    pool.append({'ref': m.group(1), 'file': str(f), 'still': m.group(2)})
for f in sorted(NOIR.glob('*.mp4')):
    pool.append({'ref': 'cn:' + f.stem, 'file': str(f), 'still': None})
for p in pool:
    p['secs'] = round(ffdur(p['file']), 2)
    p['asked'] = asked.get(p['ref'], '')
    p['new_today'] = p['ref'].startswith('h')
    p['in_cut9'] = [round(r['start'], 2) for r in plan9 if r['clip'] == p['ref']]
(HERE / 'pool.json').write_text(json.dumps(pool, indent=1, ensure_ascii=False))
print(len(pool), 'clips in the pool,', sum(p['new_today'] for p in pool), 'new today')

if '--strips' in sys.argv:
    (HERE / 'strips').mkdir(exist_ok=True)
    for p in pool:
        out = HERE / 'strips' / (p['ref'].replace(':', '_') + '.jpg')
        if out.exists():
            continue
        n = 6; step = p['secs'] / n
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', p['file'], '-vf',
                        f"fps=1/{step:.3f},scale=480:-2,drawtext=text='%{{pts\\:hms}}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,tile=3x2",
                        '-frames:v', '1', '-q:v', '4', str(out)], check=True)

# ---- music map
tr = json.load(open(SC / 'song-transcript.json'))
lines = [{'start': s['start'], 'end': s['end'], 'text': s['text']} for s in tr['segments'] if s['start'] < END]
B = json.load(open(SC / 'beats-tracked.json'))
beats = [b for b in B['beats'] if b < END + 1]
ph = B['downbeat_phase']
bars = [b for i, b in enumerate(beats) if i % 4 == ph % 4]
SECTIONS = [("intro", 0, 20.14), ("verse1", 20.14, 41.2), ("verse2", 41.2, 61.86), ("chorus1", 61.86, 82.76), ("verse3", 82.76, 105.36),
            ("verse4", 105.36, 123.74), ("chorus2", 123.74, 144.18), ("break", 144.18, 154.74), ("verse5", 154.74, END)]
import librosa
y, sr = librosa.load(str(SONG), sr=22050, duration=END + 2)
o = librosa.onset.onset_strength(y=y, sr=sr, hop_length=256); t = librosa.times_like(o, sr=sr, hop_length=256)
pk = librosa.onset.onset_detect(onset_envelope=o, sr=sr, hop_length=256, units='frames')
strong = sorted(pk, key=lambda i: -o[i])[:int(len(pk) * 0.15)]
hits = sorted(round(float(t[i]), 3) for i in strong)
rms = librosa.feature.rms(y=y, hop_length=256)[0]
loud = []
for a, b in zip(bars, bars[1:] + [END]):
    m = (t >= a) & (t < b)
    loud.append({'bar_start': round(a, 3), 'loudness': round(float(rms[m].mean()), 4)})
mx = max(l['loudness'] for l in loud)
for l in loud:
    l['loudness'] = round(l['loudness'] / mx, 2)
halfbeats = sorted(beats + [round((a + b) / 2, 3) for a, b in zip(beats, beats[1:])])
def snap(x):  # Whisper's line starts run loose by ~0.3 s: the strong hit or half beat nearest each start
    near = [h for h in hits if abs(h - x) < 0.35]
    return min(near, key=lambda h: abs(h - x)) if near else min(halfbeats, key=lambda h: abs(h - x))
for l in lines:
    l['start_snapped'] = round(snap(l['start']), 3)
mm = {'end': END, 'fade_out': 'fade the picture and song out after "Don\'t just eat cake", ending at %.1f s' % END,
      'tempo_bpm': round(B['tempo'], 2), 'beat_s': round(60 / B['tempo'], 4),
      'sections': [{'id': k, 'start': s, 'end': e} for k, s, e in SECTIONS], 'lines': lines,
      'events': [{'t': 10.82, 'what': 'THE DROP (Kai: "the very moment that the music drops", cut 9 cut late at 11.15)'},
                 {'t': 20.14, 'what': 'the words start (Kai: first rapping shot here)'},
                 {'t': 61.86, 'what': 'chorus 1 starts: cut into the car chase (Kai: cut 9 was slightly early)'},
                 {'t': 123.74, 'what': 'chorus 2 starts: same visuals as chorus 1'},
                 {'t': 144.18, 'what': 'the break'},
                 {'t': 176.0, 'what': 'about here (Kai noted 2:56): the tone of the music changes dramatically, so should the picture'},
                 {'t': END, 'what': 'the end: "Don\'t just eat cake", fade out, no outro'}],
      'beats': [round(b, 3) for b in beats], 'bars': [round(b, 3) for b in bars], 'strong_hits': hits, 'loudness_per_bar': loud}
(HERE / 'music-map.json').write_text(json.dumps(mm, indent=1, ensure_ascii=False))
print(len(lines), 'lines,', len(beats), 'beats,', len(bars), 'bars,', len(hits), 'strong hits')

# ---- anchors: Kai's notes on cut 9, with the shot at that moment
notes = [json.loads(f.read_text()) for f in (SC / 'feedback/timeline-r9-kai/notes').glob('*.json')]
kai = sorted([n for n in notes if n.get('at', 0) > 1794400000000], key=lambda n: n['key'] and int(n['key'][2:]))
def shot_at(x):
    return next((r for r in plan9 if r['start'] <= x < r['end']), plan9[-1])
out = ['# Kai\'s notes on cut 9 (11 Nov), verbatim, with the shot cut 9 had at that moment\n']
for n in kai:
    x = int(n['key'][2:]) / 24  # the key is the frame number at 24 fps
    r = shot_at(x)
    out.append(f"- **{x:.1f} s** ({n['beat']}), cut 9 showed `{r['clip']}` ({r['start']:.2f}–{r['end']:.2f} s): \"{n['note'].strip()}\"")
(HERE / 'anchors.md').write_text('\n'.join(out) + '\n')
print(len(kai), 'notes from Kai')
