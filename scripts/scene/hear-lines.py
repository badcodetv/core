#!/usr/bin/env python3
"""Hear the words on a cut's voice track and write them as timeline lines (for a cut whose script is lost).

    python3 scripts/scene/hear-lines.py "<project dir>/.bridge/state-<sequence>.json" <scene-dir> [--track A3] [--model medium.en]
        [--render <the render the page plays>]

With --render (use it whenever the page plays a render): hears the render itself, so every word is timed to the
video Kai watches, and gives each word to the voice-track clip it falls in. Without it: plays each clip's own
file from inPoint to outPoint. 🔴 That goes wrong when a voice file was re-recorded after the cut (Camping,
2026-11-27: words up to ~5 s out, and clips that came back silent), so prefer --render. Each sentence is a
line at its time in the cut. Who speaks comes from the clip's file path (a folder or file named after
the character, e.g. narration/tarquin/3.wav, narration/bob 2.wav, narration/nell-kore-narrator/1.wav).

Writes <scene-dir>/lines.json: {"heard_from", "model", "lines": [{t, dur, who, name, text, src}]}. These are
what the machine heard, not a script: check names and odd words by ear. build-timeline.py puts them into
the beats that have no lines of their own. Re-execs itself under ~/.venvs/whisper (see scripts/transcribe.py).
"""
import argparse, json, os, pathlib, re, subprocess, sys

VENV = os.path.expanduser('~/.venvs/whisper/bin/python')
try:
    from faster_whisper import WhisperModel
except ImportError:
    if os.path.exists(VENV) and sys.executable != VENV:
        os.execv(VENV, [VENV, *sys.argv])
    sys.exit('faster_whisper not found (see scripts/transcribe.py)')
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'drive'))
from localmap import localize  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('state'); ap.add_argument('scene_dir')
ap.add_argument('--track', default='A3'); ap.add_argument('--model', default='medium.en')
ap.add_argument('--render', help='hear this render instead of the clip files (timing matches the page)')
ap.add_argument('--hint', default='', help='names and odd words to help spelling, e.g. "Tarquin, Waitrose"')
a = ap.parse_args()

st = localize(json.loads(pathlib.Path(a.state).read_text()))
track = next(t for t in st['audioTracks'] if t['label'].upper() == a.track.upper())
model = WhisperModel(a.model, device='cpu', compute_type='int8')
CAST = {'nell': 'Narrator', 'narrator': 'Narrator', 'kore': 'Narrator'}


def speaker(path):
    p = path.lower().replace('\\', '/')
    for part in reversed(p.split('/')[:-1] + [pathlib.Path(p).stem]):
        for k, v in CAST.items():
            if k in part:
                return v
        m = re.match(r'[a-z]+', part)
        if m and m.group() not in ('narration', 'audio', 'voices', 'vo', 'mnt', 'camping'):
            return m.group().capitalize()
    return 'Voice'


def hear(path, start=None, length=None):
    cmd = ['ffmpeg', '-v', 'error'] + (['-ss', str(start), '-t', str(length)] if start is not None else []) + \
          ['-i', path, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-']
    pcm = subprocess.run(cmd, capture_output=True, check=True).stdout
    segs, _ = model.transcribe(np.frombuffer(pcm, np.float32), word_timestamps=True, initial_prompt=a.hint or None)
    return [(w.start, w.end, w.word) for s in segs for w in s.words]


def sentences(words, who, src):
    out, sent = [], []
    for k, w in enumerate(words):
        sent.append(w)
        if re.search(r'[.?!…]["\')]?$', w[2].strip()) or k == len(words) - 1:
            out.append({'t': round(sent[0][0], 3), 'dur': round(sent[-1][1] - sent[0][0], 3), 'who': who.lower(), 'name': who,
                        'text': ''.join(x[2] for x in sent).strip(), 'src': src})
            sent = []
    return out


clips = sorted((i for i in track.get('items', []) if not i.get('disabled')), key=lambda i: i['start'])
lines, everything = [], hear(a.render) if a.render else None
for n, it in enumerate(clips):
    who, src = speaker(it['mediaPath']), pathlib.Path(it['mediaPath']).name
    if everything is not None:  # words whose middle falls in this clip (up to the next clip's start)
        end = min(it['end'], clips[n + 1]['start']) if n + 1 < len(clips) else it['end']
        words = [w for w in everything if it['start'] <= (w[0] + w[1]) / 2 < end]
    else:
        speed = it.get('speed', 1) or 1
        words = [(it['start'] + s / speed, it['start'] + e / speed, t)
                 for s, e, t in hear(it['mediaPath'], it['inPoint'], it['outPoint'] - it['inPoint'])]
    lines += sentences(words, who, src)
    print(f"{it['start']:7.2f}  {who:9} {it['name']}: {' '.join(w[2].strip() for w in words)}", file=sys.stderr)

out = pathlib.Path(a.scene_dir) / 'lines.json'
out.write_text(json.dumps({'heard_from': (f'{pathlib.Path(a.render).name}, speakers from ' if a.render else '') + f"{pathlib.Path(a.state).name} track {a.track}", 'model': a.model,
                           'lines': lines}, indent=1, ensure_ascii=False) + '\n')
print(f'{len(lines)} lines -> {out}')
