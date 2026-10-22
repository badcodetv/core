#!/usr/bin/env python3
"""STAND-IN voice for one new AI line (GPOM ending scene D, review round 2), voiced in Gemini TTS because the Suno
takes of atom gpom-sh-end-ai-d3b could not be recorded (the WSLg PulseAudio server was lagging 3-15 s per pactl
call, so suno.mts record timed out on every take, new and old). The AI's voice is Kai's ruling: Suno "badcode
newsreader". This file only exists so the line can be heard in the rough cut; swap the Suno take in when it records.

    python3 scripts/gpom/second-half-video/ending/ai_standin.py

Writes <media D>/voices/ai-d3b-standin-<a|b>.wav, whisper-checks both, prints the pick.
"""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import voices as VO  # noqa: E402

OUT = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/D/voices')
TEXT = 'It only sends one back. ... Me.'
VOICE = 'Charon'  # calm, informative British-leaning male; not in the cut-3 cast (Derek is Algieba)
PROFILE = """# AUDIO PROFILE: a calm British newsreader, sixties, low and dry, unhurried, faintly wry

## THE SCENE
A dead, dry voiceover booth. No reverb, no music. He is speaking quietly to a hundred people who are about to give
their lives so that he can go back in time; he is not proud of it.

### DIRECTOR'S NOTES
Style: plain, honest, no apology and no drama; a fact. Pace: unhurried. A small held beat before "Me."
Accent: southern British, received pronunciation, a BBC newsreader.
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    work = VO.WORK / 'D'
    work.mkdir(parents=True, exist_ok=True)
    (work / 'ai-d3b.txt').write_text(TEXT)
    (work / 'ai-d3b.md').write_text(PROFILE)
    wavs = []
    for t in 'ab':
        w = OUT / f'ai-d3b-standin-{t}.wav'
        if not w.exists():
            subprocess.run(['uv', 'run', '-q', '--with', 'google-genai', 'python3', str(REPO / 'scripts/aistudio-tts.py'),
                            str(work / 'ai-d3b.txt'), str(w), '--profile', str(work / 'ai-d3b.md'), '--voice', VOICE],
                           check=True, env=os.environ)
        wavs.append(w)
    heard = VO.whisper(wavs)
    for w in wavs:
        print(w.name, VO.V.duration(w), json.dumps(heard.get(str(w), {}).get('text')))


if __name__ == '__main__':
    VO.V3.load_key()
    main()
