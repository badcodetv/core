#!/usr/bin/env python3
"""Scene D, Derek's "Hundred. ... What will it feel like?" (Kai, 19 Nov: "it would be good to get a couple of options").
Derek is off screen for the whole line (the overhead of the hundred chairs, then the chairs from the floor), so nothing
needs to sync: this is a voice choice. New takes in the locked voice (Algieba, 3.1) with the line's own profile, the
pause written with Gemini pause tags, every take checked for its words, then each one heard in place in cut r23
(the other stems as they are, Derek's line swapped).

    python3 scripts/gpom/second-half-video/derek-hundred-1119.py voices | render
"""
import importlib.util, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

REPO = '/home/kai/projects/badcode/badcode'
spec = importlib.util.spec_from_file_location('ld', f'{REPO}/scripts/gpom/second-half-video/lipsync-d-1119.py')
d = importlib.util.module_from_spec(spec); sys.argv, _a = ['x'], sys.argv; spec.loader.exec_module(d); sys.argv = _a
m = d.m

LN = 'd3-13'
TEXT = "Hundred. ... What will it feel like?"
_v = json.load(open(f'{d.D}/voices.json'))['lines']['d3-13-derek']
m.LINES[LN] = ('derek', TEXT, 'curious', 0, '')
m.CASTD['derek'] = {'voice': 'Algieba', 'prompt': _v['prompt']}
TAGGED = {'v1': "Hundred. <long pause> What will it feel like?",
          'v2': "Hundred... <short pause> What will it feel like?",
          # v1/v2: whisper heard no "Hundred" in any of the six (19 Nov), so also the cut's own untagged text, and a short tag
          'v3': "Hundred. ... What will it feel like?",
          'v4': "Hundred. <short pause> What will it feel like?"}
NTAKES = 3
CUT = f'{d.SRC}/cut-r23'
AT, NOW = 20.625, f'{d.SRC}/voices/d3-13-derek-r20cd.wav'  # in the cut: speech from 0.16 s placed at 20.625 s
OUT = f'{m.MEDIA}/derek-hundred'
REP = f'{m.SCENE}/derek-hundred.json'


def cmd_voices():
    open(f'{m.SCENE}/{LN}.profile.md', 'w').write(m.CASTD['derek']['prompt'])
    vs = os.environ.get('VS', '').split() or list(TAGGED)
    jobs = [(v, t) for v in vs for t in range(1, NTAKES + 1)]
    with ThreadPoolExecutor(3) as ex:
        outs = list(ex.map(lambda j: (j, m.tts_tagged(LN, TAGGED[j[0]], '31', f'{LN}-{j[0]}t{j[1]}')), jobs))
    rep = json.load(open(REP)) if os.path.exists(REP) else {}
    for (v, t), out in outs:
        miss, heard = m.missing_words(LN, out)
        miss += [f'+{w}' for w in heard.split() if w in ('pause', 'long', 'short')]
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out],
                                   capture_output=True, text=True).stdout)
        a, b = m.speech_span(out)
        rep[os.path.basename(out)] = dict(text=TAGGED[v], miss=miss, heard=heard, dur=round(dur, 2),
                                          speech=[round(float(a), 2), round(float(b), 2)])
        print(os.path.basename(out), round(dur, 2), 'MISS' if miss else 'ok', miss, '|', heard)
    json.dump(rep, open(REP, 'w'), indent=1)


def render_one(take, frm, out, t0=17.5, t1=31.5):
    """The cut from t0 to t1: picture from the preview, every stem but Derek's, and the take with its speech at AT."""
    stems = sorted(f for f in os.listdir(f'{CUT}/stems') if f.endswith('.wav') and 'derek' not in f)
    ins = sum([['-i', f'{CUT}/stems/{s}'] for s in stems], [])
    n = len(stems)
    delay = int(round((AT - t0) * 1000))
    fc = ''.join(f'[{i + 1}:a]atrim={t0}:{t1},asetpts=PTS-STARTPTS[s{i}];' for i in range(n))
    fc += f'[{n + 1}:a]atrim=start={frm},asetpts=PTS-STARTPTS,loudnorm=I=-17:TP=-2,adelay={delay}:all=1[dk];'
    fc += ''.join(f'[s{i}]' for i in range(n)) + f'[dk]amix=inputs={n + 1}:normalize=0:duration=first[a]'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(t0), '-to', str(t1), '-i', f'{CUT}/preview.mp4', *ins,
                    '-i', take, '-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-crf', '23',
                    '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', out], check=True)


def cmd_render():
    os.makedirs(OUT, exist_ok=True)
    rep = json.load(open(REP))
    render_one(NOW, 0.16, f'{OUT}/now.mp4')
    for name, x in rep.items():
        if not x['miss']:
            render_one(f'{m.VOX}/{name}', x['speech'][0], f'{OUT}/{name[:-4]}.mp4')
            print('rendered', name, x['speech'])


if __name__ == '__main__':
    dict(voices=cmd_voices, render=cmd_render)[sys.argv[1]]()
