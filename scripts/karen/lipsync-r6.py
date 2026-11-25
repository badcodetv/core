#!/usr/bin/env python3
"""Karen cut r6: lip-sync Karen's and Martha's lines (Kai, notes at2662/at2929 on cut r5: "let's spend effort on that").

The method of the lip-sync-dub skill (re-voice to the clip; fit every take whole on every clip, placed by its words):
Omni talking clips from a close start still with the exact words in the prompt (scenes/story-r6-shots, keys martha1..,
karen1..), several AI Studio takes in the cast voice, then every take x clip placed with one onset + one tempo
(0.97-1.15, never before the mouth) for the most words inside -45..+125 ms of the clip's own words (moved by the lag
between the clip's audio and its tracked mouth). The best pair is rendered: the muted clip -> post/<who>-lipsync.mp4,
the placed take -> post/<who>-lipsync-dub.wav (clip time), and fits-<who>.json lists every pair.

    python3 scripts/karen/lipsync-r6.py voices martha|karen     # extra takes in the cast voice
    python3 scripts/karen/lipsync-r6.py fit martha|karen        # check + fit + render the best
"""
import glob, json, os, re, subprocess, sys
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
K = '/mnt/d/badcode-videos/karen-story'
CLIPS = f'{K}/clips/r6/video'
POST = f'{K}/clips/r6/post'
VOX = f'{K}/_outside/Karen/narration-r6/lips'
WPY = os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python')
LPY = os.path.expanduser('~/.cache/badcode-lips/venv/bin/python')
FPS = 24
LINES = {
    'martha': dict(words="I can escalate you, Karen... but you're going to have to wait.", voice='en-us-csagent-5',
                   old=[f'{K}/_outside/Karen/narration-r4/lvl_m401a.wav'],
                   styles=['', 'tired, a short pause after Karen', 'brisk, bored', 'polite, flat, a beat after Karen']),
    'karen': dict(words="I don't want a form. I want a human. A senior human.", voice='Gacrux',
                  old=[f'{K}/_outside/Karen/narration-r4/lvl_k402a.wav'],
                  styles=['firm, clipped', 'imperious, each sentence its own beat', 'irritated, quick', 'cold, deliberate']),
}


def norm(w):
    return re.sub(r"[^a-z']", '', w.lower())


def words_of(path):
    code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
            "s,_=m.transcribe(sys.argv[1],word_timestamps=True,language='en');"
            "print(json.dumps([[w.word,w.start,w.end] for x in s for w in x.words]))")
    out = subprocess.run([WPY, '-c', code, path], capture_output=True, text=True, check=True).stdout
    return [(norm(w), s, e) for w, s, e in json.loads(out) if norm(w)]


def env(path, hop_s=1 / FPS, sr=24000):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    hop = int(sr * hop_s); n = len(x) // hop
    return 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)


def mouth(clip):
    strip = f'{POST}/lips/{os.path.basename(clip)}-strip.jpg'
    os.makedirs(os.path.dirname(strip), exist_ok=True)
    if not os.path.exists(strip + '.json'):
        subprocess.run([LPY, f'{REPO}/scripts/lipsync/mouth-track.py', clip, strip], capture_output=True)
    return np.array([np.nan if x is None else x for x in json.load(open(strip + '.json'))['scaled']], float)


def clip_anchors(clip):
    w = words_of(clip)
    e = env(clip); r = mouth(clip)
    n = min(len(e), len(r))
    ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
    lags = list(range(-12, 13))
    cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]
    lag = lags[int(np.nanargmax(cc))] / FPS
    return [(x, s + lag, e_ + lag) for x, s, e_ in w], lag, float(np.nanmean(~np.isnan(r)))


def place(cw, tw):
    """Best (n in window, mean err, onset, tempo) laying take words tw on clip words cw."""
    pairs, j = [], 0
    for w, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == w), None)
        if k is not None:
            pairs.append((s_, cw[k][1])); j = k + 1
    if len(pairs) < 2:
        return None
    ts = np.array([p[0] for p in pairs]); cs = np.array([p[1] for p in pairs])
    t0 = tw[0][1]
    best = None
    for tempo in np.arange(0.97, 1.151, 0.01):
        for i in range(len(pairs)):
            at = cs[i] + 0.04 - (ts[i] - t0) / tempo
            d = at + (ts - t0) / tempo - cs
            if d[0] < -0.045:
                continue
            n = int(np.sum((d >= -0.045) & (d <= 0.125)))
            err = float(np.mean(np.abs(d - 0.04)))
            if best is None or (n, -err) > (best[0], -best[1]):
                best = (n, err, float(at), float(tempo), len(pairs), [round(float(x) * 1000) for x in d])
    return best


def voices(who):
    L = LINES[who]
    os.makedirs(VOX, exist_ok=True)
    import tempfile
    for i, st in enumerate(L['styles']):
        out = f'{VOX}/{who}-v{i + 1}.wav'
        if os.path.exists(out):
            continue
        tf = tempfile.mktemp(suffix='.txt'); open(tf, 'w').write(L['words'] + '\n')
        cmd = ['uv', 'run', '-q', '--with', 'google-genai<2', 'python3', f'{REPO}/scripts/aistudio-tts.py', tf, out,
               '--voice', L['voice'], '--plain', '--model', 'gemini-3.8-flash-tts'] + (['--style', st] if st else [])
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
        print(out, 'ok' if r.returncode == 0 else r.stderr[-300:])
    subprocess.run(['python3', f'{REPO}/scripts/karen/finish-voice-r4.py', *sorted(glob.glob(f'{VOX}/{who}-v*.wav'))], check=True)


def fit(who):
    L = LINES[who]
    clips = sorted(glob.glob(f'{CLIPS}/r6-{who}[0-9]-*.mp4'))
    takes = L['old'] + sorted(glob.glob(f'{VOX}/lvl_{who}-v*.wav'))
    want = [norm(w) for w in L['words'].split()]
    tw_all = {t: words_of(t) for t in takes}
    rows = []
    for c in clips:
        cw, lag, seen = clip_anchors(c)
        heard = [w for w, _, _ in cw]
        hit = sum(1 for w in want if w in heard) / len(want)
        print(os.path.basename(c), f'lag {lag:+.2f}', f'face {seen:.0%}', 'heard:', ' '.join(heard))
        if hit < 0.7 or seen < 0.7:
            print('  set aside (says another line or the face is lost)')
            continue
        for t, tw in tw_all.items():
            if sum(1 for w in want if w in [x for x, _, _ in tw]) / len(want) < 0.9:
                continue
            b = place(cw, tw)
            if b:
                rows.append(dict(clip=c, take=t, n=b[0], of=b[4], err=round(b[1], 3), at=round(b[2], 3), tempo=round(b[3], 2),
                                 frm=tw[0][1], to=tw[-1][2], d=b[5]))
    rows.sort(key=lambda x: (-x['n'] / x['of'], x['err']))
    for x in rows[:8]:
        print(f"{x['n']}/{x['of']} err {x['err']:.3f} tempo {x['tempo']} at {x['at']:.2f}  {os.path.basename(x['clip'])}  {os.path.basename(x['take'])}  {x['d']}")
    json.dump(rows, open(f'{POST}/fits-{who}.json', 'w'), indent=1)
    if rows:
        render(who, rows[0])


def render(who, x):
    clip, take = x['clip'], x['take']
    frm, to = max(x['frm'] - 0.05, 0), x['to'] + 0.15
    end = x['at'] + (to - frm) / x['tempo'] + 0.6     # hold 0.6 s after the last word, then cut
    dur = min(end, float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip],
                                        capture_output=True, text=True).stdout))
    delay = max(0, int(round((x['at'] - 0.05 / x['tempo']) * 1000)))
    os.makedirs(POST, exist_ok=True)
    vid, dub = f'{POST}/{who}-lipsync.mp4', f'{POST}/{who}-lipsync-dub.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-t', f'{dur:.3f}', '-an', '-vf', f'scale=1920:1080,fps={FPS}',
                    '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', vid], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', take, '-af',
                    f"atrim={frm}:{to},asetpts=PTS-STARTPTS,atempo={x['tempo']},adelay={delay}:all=1,apad,atrim=0:{dur:.3f}",
                    '-ar', '48000', '-ac', '2', dub], check=True)
    for out, par in ((vid, clip), (dub, take)):
        subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', out, '--kind', 'video' if out.endswith('mp4') else 'voice',
                        '--engine', 'ffmpeg', '--tool', 'scripts/karen/lipsync-r6.py', '--parent', par, '--why',
                        f"lip-sync {who}: {x['n']}/{x['of']} words in -45..+125 ms, tempo {x['tempo']}, onset {x['at']:.2f}s"],
                       capture_output=True)
    print('rendered', vid, dub, f"{dur:.2f}s")


if __name__ == '__main__':
    dict(voices=voices, fit=fit)[sys.argv[1]](sys.argv[2])
