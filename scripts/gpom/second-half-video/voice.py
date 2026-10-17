#!/usr/bin/env python3
"""Voice every line of the second half's sound script in Gemini TTS, one take per line.

Reads scenes/second-half-audio-plan.json (the single source of the words) and writes
clips/second-half/audio/voice/<frame>-<i>-<who>.wav plus voice/takes.json (durations).
One voice per call: the multi-speaker mode drops and swaps lines (docs/ai-studio/README.md).
A take much shorter than its words should be is re-run (one take in five comes back truncated).

Rough-cut casting, Kai to re-cast: the casting tests in the plan are not run yet.

    python3 scripts/gpom/second-half-video/voice.py [frame ...]     # existing takes are kept
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

REPO = S.REPO
OUT = S.CLIPS / 'audio' / 'voice'
WORK = pathlib.Path(os.environ['HOME']) / '.cache/badcode-gpom-second-half/voice'
CAST = {'narrator': 'Algenib', 'ai': 'Algenib', 'bot': 'Aoede', 'woman': 'Kore', 'man': 'Fenrir', 'lady': 'Gacrux'}
# The hundred: one voice per take, stacked in the edit.
CROWD = [('Puck', 'Whoa.'), ('Leda', 'Hang on a minute.'), ('Orus', "What's that?"), ('Zephyr', 'Oh my God.')]
WPS = 2.6  # spoken words per second, for the truncation check

plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
profiles = {v['id']: v['prompt'] for v in plan['voices']}


def jobs(only):
    out = []
    for n, shot in plan['shots'].items():
        if only and n not in only:
            continue
        for i, (who, said) in enumerate(shot.get('lines', [])):
            if who == 'crowd':
                for j, (voice, text) in enumerate(CROWD):
                    out.append((f'{int(n):02d}-{i}-crowd{j}', 'crowd', voice, text))
            else:
                out.append((f'{int(n):02d}-{i}-{who}', who, CAST[who], said))
    return out


def duration(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def run(job):
    key, who, voice, text = job
    wav = OUT / f'{key}.wav'
    words = len(text.split())
    if wav.exists():
        return key, duration(wav), 'kept'
    (WORK / f'{key}.txt').write_text(text)
    prof = WORK / f'{who}.md'
    prof.write_text(profiles['crowd'] if who == 'crowd' else profiles[who])
    last = ''
    for attempt in range(1, 4):
        tmp = WORK / f'{key}.wav'
        r = subprocess.run(['uv', 'run', '-q', '--with', 'google-genai', 'python3', str(REPO / 'scripts/aistudio-tts.py'),
                            str(WORK / f'{key}.txt'), str(tmp), '--profile', str(prof), '--voice', voice],
                           capture_output=True, text=True, env=os.environ)
        if r.returncode or not tmp.exists():
            last = (r.stderr or r.stdout)[-200:]
            continue
        d = duration(tmp)
        # Short lines ("Hello.") run long relative to their words; only judge lines of 4+ words.
        if words >= 4 and d < 0.5 * words / WPS:
            last = f'short take {d:.1f}s for {words} words'
            continue
        shutil.move(str(tmp), wav)
        return key, d, f'ok (attempt {attempt})'
    return key, 0, 'FAILED ' + last


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    todo = jobs(set(sys.argv[1:]))
    with ThreadPoolExecutor(3) as ex:
        results = list(ex.map(run, todo))
    for key, d, how in results:
        print(f'{key:24s} {d:5.2f}s  {how}')
    takes = {k: d for k, d, h in results if d}
    index = OUT / 'takes.json'
    old = json.loads(index.read_text()) if index.exists() else {}
    index.write_text(json.dumps({**old, **takes}, indent=1, sort_keys=True))
