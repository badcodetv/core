#!/usr/bin/env python3
"""Karen story film, cut r7: render every line in narration-r7.tsv in parallel (paid key, no pacing; docs/rules/voices.md).

    python3 scripts/karen/render-narration-r7.py [id ...]

narr = the story's locked Algenib setup (profile, default model); pres = the President's Charon profile;
plain = Google's plain TTS on gemini-3.8-flash-tts with an optional --style (never spoken). Skips takes already on disk.
"""
import pathlib, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path('/mnt/d/badcode-videos/karen-story/_outside/Karen/narration-r7')
OUT.mkdir(parents=True, exist_ok=True)
PROF = ROOT / 'docs/stories/karen/narration/profiles'
want = set(sys.argv[1:])
jobs = []
for ln in (ROOT / 'scripts/karen/narration-r7.tsv').read_text().splitlines():
    if not ln.strip() or ln.startswith('#'):
        continue
    i, who, voice, mode, style, text = ln.split('\t')
    if want and i not in want and not any(i.startswith(w) for w in want):
        continue
    if (OUT / f'{i}.wav').exists():
        continue
    jobs.append((i, voice, mode, style, text))


def run(j):
    i, voice, mode, style, text = j
    tf = pathlib.Path(tempfile.mkdtemp()) / f'{i}.txt'
    tf.write_text(text + '\n')
    cmd = ['uv', 'run', '-q', '--with', 'google-genai<2', 'python3', str(ROOT / 'scripts/aistudio-tts.py'), str(tf), str(OUT / f'{i}.wav'), '--voice', voice]
    if mode == 'narr':
        cmd += ['--profile', str(PROF / 'narrator-algenib.md')]
    elif mode == 'pres':
        cmd += ['--profile', str(PROF / 'president-charon.md')]
    else:
        cmd += ['--plain', '--model', 'gemini-3.8-flash-tts'] + (['--style', style] if style else [])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    return i, r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1:] if (r.stdout + r.stderr).strip() else ''


with ThreadPoolExecutor(6) as ex:
    for i, rc, msg in ex.map(run, jobs):
        print(i, 'ok' if rc == 0 else f'FAIL {msg}', flush=True)
