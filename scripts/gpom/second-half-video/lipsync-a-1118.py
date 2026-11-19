#!/usr/bin/env python3
"""Lip-sync pass on scene A's row (Kai, 18 Nov 2026: "massively improve the lip syncing"; plan in
docs/stories/gitpush-origin-master/lipsync-plan-2026-11-18.md, steps 3-6, steps 1-2 skipped on Kai's word).

Per line: five new AI Studio takes (cast voice, same words), five new Omni talking clips from the approved start still
(Frames, the line in the prompt), then every take fitted WHOLE on every clip's tracked mouth (voice-row-fit.fit: one
onset + one tempo, never before the mouth opens), best three pairs rendered for the picks page.

    python3 scripts/gpom/second-half-video/lipsync-a-1118.py voices [line...]   # 5 takes each, transcribed
    python3 scripts/gpom/second-half-video/lipsync-a-1118.py jobs               # writes the pool scene's video-jobs.json
    python3 scripts/gpom/second-half-video/lipsync-a-1118.py check [line...]    # transcribe + mouth-track the new clips
    python3 scripts/gpom/second-half-video/lipsync-a-1118.py fit [line...]      # every take x every clip, top 3
    python3 scripts/gpom/second-half-video/lipsync-a-1118.py render [line...]   # the top 3 + "now in the film" as mp4s
"""
import importlib.util, json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np

REPO = '/home/kai/projects/badcode/badcode'
spec = importlib.util.spec_from_file_location('vrf', f'{REPO}/scripts/gpom/second-half-video/voice-row-fit.py')
vrf = importlib.util.module_from_spec(spec); spec.loader.exec_module(vrf)

MEDIA = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/A'
VOX = f'{MEDIA}/voices'
CLIPS = f'{MEDIA}/video'          # pool output (<prefix>-<key>-<still>.mp4)
OUT = f'{MEDIA}/pairs'
SCENE = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/lipsync-1118'
CAST = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-cut3-cast.json'
CUT = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/A-d27'
STILL = {'woman': 'sandra-SB07b', 'man': 'derek-SB07c'}
FACE = {}
FPS = 24
PREFIX = 'la'
CASTD = json.load(open(CAST))['cast']
BED = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/audio/sfx/fs767306-room-tiled-public-bathroom.mp3'

# line: (who, words, direction for the voice, clip seconds, Flow motion prompt, fit window (clip s), fit only to (take phrase idx))
LINES = {
    '6-0': ('woman', "Derek. You've left the seat up. Again.",
            "sharp, sarcastic; 'Derek.' clipped on its own, then a short beat, then 'You've left the seat up.' quick "
            "and pointed; a long pause, glaring; then one flat word, 'Again.'", 6,
            "Locked-off camera, no camera movement. The woman in the cream jumper, facing us, points at the man and "
            "scolds him, sharp and sarcastic, her lips shaping every word clearly. She says: Derek. You've left the seat up. "
            "She glares for a moment, then adds one flat word. She says: Again. Then her lips stay pressed shut. "
            "The man seen from behind stays still and silent. Sound: tiled room echo, a dripping tap."),
    '7d-0': ('man', "I'm really sorry, love.",
             "sheepish and quick, a placating mumble, the words run together; a long, drawn-out 'I'm' at the start", 5,
             "The shot stays fixed; only the people move. Derek, the husband in the dark green jumper, stands silent for "
             "a second taking the telling-off, then mumbles a sheepish apology, his lips shaping every word. He says: "
             "I'm really sorry, love. Then his mouth closes and he looks at the floor. His wife, her back to us, stays "
             "quiet and still. Sound: tiled room echo, a dripping tap."),
    '7-0': ('woman', "Five years underground, and you still can't put a seat down.",
            "brisk and cutting, the words tumbling out, building; 'Five years underground,' fast, straight into the rest", 6,
            "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, jabs a finger at the man "
            "and tears into him, cutting and sarcastic, her lips shaping every word clearly. She says: Five years "
            "underground, and you still can't put a seat down. Then she shuts her mouth and glares. The man seen from "
            "behind does not move or speak. Sound: tiled room echo, a dripping tap."),
    '7d-1': ('man', 'But the world ended, Sandra!',
             "indignant, arms up, a burst; 'But the world ended,' then 'Sandra!' louder", 5,
             "Static frame, nothing but the people moves. The husband in the dark green jumper flings his hands wide and "
             "shouts at his wife, exasperated, his lips shaping every word. He says: But the world ended, Sandra! Then "
             "his mouth shuts and he holds still, staring at her, hands still spread. His wife, seen from behind, holds "
             "still and says nothing. Sound: tiled room echo, a dripping tap."),
    '7-2': ('woman', "Yeah, the world ended. Doesn't mean you get to stop having manners.",
            "snaps straight back, quick and cutting, the words tumbling out fast, no pause after 'ended.'", 6,
            "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, fires straight back at "
            "the man, quick, sharp and sarcastic, her lips shaping every word clearly. She says: Yeah, the world ended. "
            "Doesn't mean you get to stop having manners. Then she shuts her mouth and folds her arms. The man seen from "
            "behind does not move or speak. Sound: tiled room echo, a dripping tap."),
}
# where the line sits in the film now (A-d27): shot file, its in point, shot length; the voice wav and its start
NOW = {
    '6-0': ('cut3-lip-6-0-v3-muted.mp4', 0.0, 2.5, 129.208),
    '7d-0': ('cut3-lip-7d-0-r19-muted.mp4', 1.7083, 1.9583, 131.708),
    '7-0': ('cut3-lip-7-0-r24-muted.mp4', 0.0, 4.375, 133.667),
    '7d-1': ('cut3-lip-7d-1-muted.mp4', 0.625, 1.9583, 138.042),
    '7-2': ('cut3-lip-7-2-v3-muted.mp4', 0.0, 3.625, 140.0),
}
KEYS = 'abcde'
CLIP_KEYS = 'abcdefghij'
WPY = vrf.WPY


def norm(w):
    return re.sub(r"[^a-z']", '', w.lower())


def take_path(line, k):
    return f'{VOX}/{line}-{k}.wav'


FAST = {  # round 2 of voices: Omni's mouths run faster than the first takes; direct the take to the clip's pace
    '6-0': "quick and sharp; 'Derek.' clipped, a short beat, 'You've left the seat up.' fast, a beat, then a flat 'Again.'",
    '7d-0': "a fast, sheepish mumble, all four words run together in barely more than a second, no drawn-out 'I'm'",
    '7-0': "fast and cutting, the whole line in one quick breath, no pause after 'underground'",
    '7d-1': "a fast indignant burst, the whole line in about a second, 'Sandra!' louder",
    '7-2': "rapid-fire, snapping straight back, the whole line fast in one breath, no pause after 'ended.'",
}


def tts(line, k):
    who, text, direction = LINES[line][:3]
    if k in 'fghij':
        direction = FAST[line]
    cast = CASTD[who]
    prof = re.sub(r'^Pace: .*$', 'Pace: ' + direction + '.', cast['prompt'], count=1, flags=re.M)
    os.makedirs(SCENE, exist_ok=True); os.makedirs(VOX, exist_ok=True)
    pf, tf = f'{SCENE}/{line}{"-fast" if k in "fghij" else ""}.profile.md', f'{SCENE}/{line}.txt'
    open(pf, 'w').write(prof); open(tf, 'w').write(text + '\n')
    out = take_path(line, k)
    if not os.path.exists(out):
        subprocess.run(f'set -a; . ./.env; set +a; uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py {tf} {out} '
                       f'--profile {pf} --voice {cast["voice"]}', shell=True, cwd=REPO, capture_output=True, check=True)
        subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', out, '--kind', 'voice', '--engine',
                        'Gemini TTS', '--model', f'gemini-3.1-flash-tts-preview / {cast["voice"]}', '--tool',
                        'scripts/aistudio-tts.py (billed key) via lipsync-a-1118.py', '--prompt-file', pf,
                        '--setting', f'text={text}', '--why', 'lip-sync pass 18 Nov (Kai): five new takes per line'],
                       check=True, capture_output=True)
    return out


_W = {}


def words_of(path):
    if path not in _W:
        _W[path] = vrf.words_of(path)
    return _W[path]


def missing_words(line, path):
    want = [norm(x) for x in LINES[line][1].split()]
    got = [w for w, _, _ in words_of(path)]
    return [x for x in want if x not in got], ' '.join(got)


def cmd_voices(lines):
    rep = {}
    for ln in lines:
        with ThreadPoolExecutor(3) as ex:
            takes = list(ex.map(lambda k: tts(ln, k), os.environ.get('TAKES', KEYS)))
        rep[ln] = {}
        for t in takes:
            miss, heard = missing_words(ln, t)
            d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', t],
                                     capture_output=True, text=True).stdout)
            rep[ln][os.path.basename(t)] = dict(miss=miss, heard=heard, dur=round(d, 2))
            print(ln, os.path.basename(t), round(d, 2), 'MISS' if miss else 'ok', miss, '|', heard)
    p = f'{SCENE}/voices.json'
    prev = json.load(open(p)) if os.path.exists(p) else {}
    for k, v in rep.items():
        prev.setdefault(k, {}).update(v)
    json.dump(prev, open(p, 'w'), indent=1)


def cmd_jobs():
    extra = []
    for ln, (who, text, _, dur, motion, *_r) in LINES.items():
        for k in CLIP_KEYS:  # a-e: first five (18 Nov am); f-j: five more (Kai, 18 Nov pm), new keys so nothing is overwritten
            extra.append(dict(key=f'L{ln.replace("-", "")}{k}', n=0, still=STILL[who], duration=dur, motion=motion,
                              character=None, why=f'lip-sync 18 Nov: line {ln} clip {k}'))
    json.dump(dict(extra=extra), open(f'{SCENE}/video-jobs.json', 'w'), indent=1)
    print(len(extra), 'jobs')


# Pause test (Kai, 18 Nov evening: "all in on the Flow plan"; docs/google-flow/2026-11-18-lip-sync-sweep.md, try #2).
# Lines 7-0 and 7-2 have a pause inside. Control arm = the plain clips a-j already made. Arm "action" (keys k-r):
# the pause written as an action between two "She says:". Arm "beat" (keys s-z): a [beat] token in the words.
EXP = {
    '7-0': {
        'action': "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, tears into the man, "
                  "cutting and sarcastic, her lips shaping every word clearly. She says: Five years underground. "
                  "She stops and jabs her finger hard at the toilet seat, lips pressed shut, then says: and you still can't "
                  "put a seat down. Then she shuts her mouth and glares. The man seen from behind does not move or speak. "
                  "Sound: tiled room echo, a dripping tap.",
        'beat': "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, jabs a finger at the man "
                "and tears into him, cutting and sarcastic, her lips shaping every word clearly. She says: Five years "
                "underground, [beat] and you still can't put a seat down. Then she shuts her mouth and glares. The man seen "
                "from behind does not move or speak. Sound: tiled room echo, a dripping tap.",
    },
    '7-2': {
        'action': "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, fires straight back at "
                  "the man, sharp and sarcastic, her lips shaping every word clearly. She says: Yeah, the world ended. "
                  "She rolls her eyes and tilts her head, lips pressed shut, then says: Doesn't mean you get to stop having "
                  "manners. Then she shuts her mouth and folds her arms. The man seen from behind does not move or speak. "
                  "Sound: tiled room echo, a dripping tap.",
        'beat': "Locked-off camera, the frame holds still. The woman in the cream jumper, facing us, fires straight back at "
                "the man, quick, sharp and sarcastic, her lips shaping every word clearly. She says: Yeah, the world ended. "
                "[beat] Doesn't mean you get to stop having manners. Then she shuts her mouth and folds her arms. The man "
                "seen from behind does not move or speak. Sound: tiled room echo, a dripping tap.",
    },
}
ARM_KEYS = {'action': 'klmnopqr', 'beat': 'stuvwxyz'}


def arm_of(clip):
    k = re.search(rf'{PREFIX}-L[0-9a-z]+?([a-z])-', os.path.basename(clip)).group(1)
    return next((a for a, ks in ARM_KEYS.items() if k in ks), 'plain')


def cmd_exp_jobs():
    p = f'{SCENE}/video-jobs.json'
    jobs = json.load(open(p))
    have = {e['key'] for e in jobs['extra']}
    for ln, arms in EXP.items():
        who, _, _, dur = LINES[ln][:4]
        for arm, motion in arms.items():
            for k in ARM_KEYS[arm]:
                key = f'L{ln.replace("-", "")}{k}'
                if key not in have:
                    jobs['extra'].append(dict(key=key, n=0, still=STILL[who], duration=dur, motion=motion, character=None,
                                              why=f'pause test 18 Nov: line {ln}, arm {arm}, clip {k}'))
    json.dump(jobs, open(p, 'w'), indent=1)
    print(len(jobs['extra']), 'jobs')


def clips_of(line):
    tag = f'L{line.replace("-", "")}'
    return sorted(f'{CLIPS}/{f}' for f in os.listdir(CLIPS)
                  if re.match(rf'{PREFIX}-{tag}[a-z]-', f) and f.endswith('.mp4') and '-muted' not in f)


def mouth(clip):
    os.makedirs(f'{MEDIA}/strips', exist_ok=True)  # media, not the repo (Kai 18 Nov: no images committed)
    strip = f'{MEDIA}/strips/{os.path.basename(clip)}-strip.jpg'
    # two faces in frame (scene D, 19 Nov): FACE maps a still's name to which face is talking ('left'/'right', default 'big')
    face = next((f for s, f in FACE.items() if s in os.path.basename(clip)), 'big')
    if not os.path.exists(strip + '.json'):
        subprocess.run([vrf.LPY, f'{REPO}/scripts/lipsync/mouth-track.py', clip, strip, '--face', face], capture_output=True)
    js = json.load(open(strip + '.json'))
    return np.array([np.nan if x is None else x for x in js['scaled']], float)


def cmd_check(lines):
    p = f'{SCENE}/clips.json'
    rep = json.load(open(p)) if os.path.exists(p) else {}
    only = os.environ.get('ONLY')  # e.g. ONLY=fghij: check just the newer clips
    for ln in lines:
        for c in clips_of(ln):
            if only and re.search(rf'{PREFIX}-L[0-9a-z]+?([a-z])-', os.path.basename(c)).group(1) not in only:
                continue
            miss, heard = missing_words(ln, c)
            r = mouth(c)
            md5 = subprocess.run(['md5sum', c], capture_output=True, text=True).stdout.split()[0]
            d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', c],
                                     capture_output=True, text=True).stdout)
            rep[os.path.basename(c)] = dict(line=ln, miss=miss, heard=heard, md5=md5, dur=round(d, 2),
                                            tracked=round(float(np.mean(~np.isnan(r))), 2))
            print(ln, os.path.basename(c), round(d, 2), md5[:8], 'tracked', rep[os.path.basename(c)]['tracked'],
                  'MISS' if miss else 'ok', miss, '|', heard)
    json.dump(rep, open(p, 'w'), indent=1)
    dup = {}
    for k, v in rep.items():
        dup.setdefault(v['md5'], []).append(k)
    for m, ks in dup.items():
        if len(ks) > 1:
            print('DUPLICATE md5', ks)


def speech_span(path):
    e = vrf.fine_env(path)
    act = np.where(e > e.max() - 40)[0]
    return max(0.0, act[0] * 0.01 - 0.03), (act[-1] + 1) * 0.01 + 0.05


_ANCH = {}


def clip_anchors(clip):
    """The clip's own words, moved by the lag between its own audio and its tracked mouth (Omni's audio drifts)."""
    if clip in _ANCH:
        return _ANCH[clip]
    w = words_of(clip)
    e = vrf.env(clip); r = mouth(clip)
    n = min(len(e), len(r))
    ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
    lags = list(range(-12, 13))
    cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]
    lag = lags[int(np.nanargmax(cc))] / FPS
    _ANCH[clip] = ([(x, s_ + lag) for x, s_, _ in w], lag)
    return _ANCH[clip]


def match_err(cw, tw, at, tempo, frm):
    """Mean |clip word start - placed take word start| over the line's words, matched in order."""
    errs, j = [], 0
    for x, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == x), None)
        if k is None:
            continue
        errs.append(abs(cw[k][1] - (at + (s_ - frm) / tempo))); j = k + 1
    return (float(np.mean(errs)), float(np.max(errs)), len(errs)) if errs else (9, 9, 0)


def fit_pair(line, clip, take):
    r = mouth(clip)
    if np.mean(~np.isnan(r)) < 0.7:
        return None
    cw, lag = clip_anchors(clip)
    tw = words_of(take)
    a, b = speech_span(take)
    e = vrf.fine_env(take, a, b)
    # anchor on the first word both share: whisper hears a phantom "it" before Derek's "Doesn't" on many clips (18 Nov)
    # 19 Nov (scene D "And afterwards?"): whisper put the clip's first word at 0.0, before the mouth opens, which
    # left an empty window; take the first shared word whose window can hold a take that never starts early
    pairs = [(i, k) for k, (x, _, _) in enumerate(tw[:3]) for i, (y, _) in enumerate(cw[:3]) if x == y] or [(0, 0)]
    # a word whisper starts at 0.0 in the file is a guess (it pins the first word to the start), not a time
    pairs = [p for p in pairs if cw[p[0]][1] - lag > 0.05 and tw[p[1]][1] > 0.05] or pairs
    for j in pairs:
        first = cw[j[0]][1] if cw else 0.0
        t0 = (tw[j[1]][1] - a) if tw else 0.0  # that word in the take, from its speech start
        win = (max(-0.04, first - t0 - 0.35), first - t0 + 0.35)
        if win[1] > win[0] + 0.1:
            break
    sc, on, tempo, det = vrf.fit(r, e, tempos=np.arange(0.97, 1.151, 0.01), window=win)
    if on is None:
        return None
    me, mx, nw = match_err(cw, tw, on, tempo, a)
    return dict(line=line, clip=os.path.basename(clip), take=os.path.basename(take), score=round(float(sc - 1.5 * me), 3),
                mouth=round(float(sc), 3), word_err=round(me, 3), word_max=round(mx, 3), words=nw, lag=round(lag, 3),
                at=on, tempo=tempo, frm=round(float(a), 3), to=round(float(b), 3), **det)


def cmd_fit(lines):
    vrep = json.load(open(f'{SCENE}/voices.json'))
    crep = json.load(open(f'{SCENE}/clips.json'))
    p = f'{SCENE}/fits.json'
    allf = json.load(open(p)) if os.path.exists(p) else {}
    for ln in lines:
        takes = [f'{VOX}/{n}' for n, v in vrep[ln].items() if not v['miss']]
        clips = [c for c in clips_of(ln) if not crep.get(os.path.basename(c), {}).get('miss', ['?'])]
        jobs = [(c, t) for c in clips for t in takes]
        for c in clips:
            clip_anchors(c)
        for t in takes:
            words_of(t)
        with ThreadPoolExecutor(6) as ex:
            res = [x for x in ex.map(lambda ct: fit_pair(ln, *ct), jobs) if x]
        res = [word_place(x) for x in res]  # 18 Nov: also try placing the take by its words, keep the better
        for x in res:  # rank by words inside the tolerance window first (sweep try #2d), then the old score
            rows = word_table(x)
            x['in_window'] = sum(1 for _, d in rows if d is not None and -0.045 <= d <= 0.125)
            x['near'] = sum(1 for _, d in rows if d is not None and -0.1 <= d <= 0.2)
            x['n_words'] = len(rows)
        res.sort(key=lambda x: (-x['in_window'], -x['near'], -x['score']))
        # top 3, at most one per clip, so Kai sees three different pictures
        top, seen = [], set()
        for x in res:
            if x['clip'] in seen:
                continue
            top.append(x); seen.add(x['clip'])
            if len(top) == 3:
                break
        allf[ln] = dict(all=res, top=top, clips=len(clips), takes=len(takes))
        print(ln, f'{len(clips)} clips x {len(takes)} takes')
        for x in top:
            print('  TOP', x)
    json.dump(allf, open(p, 'w'), indent=1)


def render_pair(x, out):
    clip = f'{CLIPS}/{x["clip"]}'; take = take_path(x['line'], x['take'].split('-')[-1][0]) if False else f'{VOX}/{x["take"]}'
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip],
                               capture_output=True, text=True).stdout)
    delay = max(0, int(round(x['at'] * 1000)))
    bed = BED
    af = (f"[1:a]atrim={x['frm']}:{x['to']},asetpts=PTS-STARTPTS,atempo={x['tempo']},adelay={delay}|{delay},apad[v];"
          f"[2:a]volume=0.25,apad[b];[v][b]amix=inputs=2:normalize=0,atrim=0:{dur}[a]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-i', take, '-i', bed, '-filter_complex', af,
                    '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                    '-c:a', 'aac', '-b:a', '160k', '-t', str(dur), '-movflags', '+faststart', out], check=True)
    subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', out, '--kind', 'video', '--engine', 'ffmpeg',
                    '--tool', 'lipsync-a-1118.py render', '--parent', clip, '--parent', take,
                    '--why', f'lip-sync pair for line {x["line"]}: voice at {x["at"]} s x{x["tempo"]}, score {x["score"]}'],
                   check=True, capture_output=True)


def render_now(line, out):
    f, i, d, t = NOW[line]
    src = f'{CUT}/preview.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', src, '-t', str(d + 0.9), '-c:v', 'libx264', '-crf', '20',
                    '-preset', 'fast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out],
                   check=True)


def cmd_render(lines):
    os.makedirs(OUT, exist_ok=True)
    fits = json.load(open(f'{SCENE}/fits.json'))
    tag = os.environ.get('TAG', '')  # TAG=r2-: the 50-clip round (Kai, 18 Nov pm) renders beside round 1, never over it
    for ln in lines:
        if not os.path.exists(f'{OUT}/{ln}-now.mp4'):
            render_now(ln, f'{OUT}/{ln}-now.mp4')
        for i, x in enumerate(fits[ln]['top']):
            render_pair(x, f'{OUT}/{ln}-{tag}pick{i + 1}.mp4')
            print(ln, i + 1, x['clip'], x['take'], x['score'], x['tempo'])


# Re-voice to the clip (sweep 2026-11-18 try #2b): same words, the pauses moved with Gemini's pause tags to where the
# word table says the picked clips pause. Both the locked 3.1 sound and 3.8 (the voice rule's model), three takes each.
REVOICE = {
    '6-0': ["Derek, you've left the seat up. <long pause> Again.",
            "Derek. <short pause> You've left the seat up. <long pause> Again."],
    '7-0': ["Five years underground, <short pause> and you still can't put a seat down.",
            "Five <short pause> years underground, and you still can't put a seat down."],
    '7-2': ["Yeah, the world ended. <long pause> Doesn't mean you get to stop having manners.",
            "Yeah, the world ended... <long pause> Doesn't mean you get to stop having manners."],
}
MODELS = {'31': 'gemini-3.1-flash-tts-preview', '38': 'gemini-3.8-flash-tts'}


def tts_tagged(line, text, model, name):
    who = LINES[line][0]
    cast = CASTD[who]
    tf = f'{SCENE}/{name}.txt'
    open(tf, 'w').write(text + '\n')
    pf = f'{SCENE}/{line}.profile.md'
    out = f'{VOX}/{name}.wav'
    if not os.path.exists(out):
        subprocess.run(f'set -a; . ./.env; set +a; uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py {tf} {out} '
                       f'--profile {pf} --voice {cast["voice"]} --model {MODELS[model]}', shell=True, cwd=REPO,
                       capture_output=True, check=True)
        subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', out, '--kind', 'voice', '--engine',
                        'Gemini TTS', '--model', f'{MODELS[model]} / {cast["voice"]}', '--tool',
                        'scripts/aistudio-tts.py via lipsync-a-1118.py revoice', '--prompt-file', pf,
                        '--setting', f'text={text}', '--why', 'lip-sync 18 Nov: re-voice with pause tags to the clips'],
                       check=True, capture_output=True)
    return out


def cmd_revoice(lines):
    p = f'{SCENE}/voices.json'
    rep = json.load(open(p))
    jobs = [(ln, vi, text, m, t) for ln in lines if ln in REVOICE for vi, text in enumerate(REVOICE[ln])
            for m in MODELS for t in range(int(os.environ.get('NTAKES', 3)))]
    def one(j):
        ln, vi, text, m, t = j
        return j, tts_tagged(ln, text, m, f'{ln}-v{vi + 1}m{m}t{t + 1}')
    with ThreadPoolExecutor(4) as ex:
        done = list(ex.map(one, jobs))
    for (ln, vi, text, m, t), out in done:
        miss, heard = missing_words(ln, out)
        extra = [w for w in heard.split() if w in ('pause', 'long', 'short')]
        miss = miss + [f'+{w}' for w in extra]  # a spoken tag counts as a fail
        if len(heard.split()) > len(LINES[ln][1].split()) + 2:
            miss.append('read-the-brief')  # 3.8 sometimes reads the whole profile aloud (18 Nov)
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out],
                                 capture_output=True, text=True).stdout)
        rep[ln][os.path.basename(out)] = dict(miss=miss, heard=heard, dur=round(d, 2), text=text, model=MODELS[m])
        print(ln, os.path.basename(out), round(d, 2), 'MISS' if miss else 'ok', miss, '|', heard)
    json.dump(rep, open(p, 'w'), indent=1)


def word_table(x):
    """Per word: placed voice start minus the clip's own word start (s). + = voice late. Window -0.045..+0.125 (ITU-R BT.1359)."""
    cw, _ = clip_anchors(f'{CLIPS}/{x["clip"]}')
    tw = words_of(f'{VOX}/{x["take"]}')
    rows, j = [], 0
    for w, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == w), None)
        if k is None:
            rows.append((w, None)); continue
        rows.append((w, round(x['at'] + (s_ - x['frm']) / x['tempo'] - cw[k][1], 3))); j = k + 1
    return rows


def word_place(x):
    """Search onset + tempo (0.97-1.15) for the most words inside -45..+125 ms of the clip's own words (shifted by its lag
    to the tracked mouth). Keeps the mouth-score placement if that already does as well. The voice never starts more than
    45 ms before the clip's first shared word."""
    cw, _ = clip_anchors(f'{CLIPS}/{x["clip"]}')
    tw = words_of(f'{VOX}/{x["take"]}')
    pairs, j = [], 0
    for w, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == w), None)
        if k is not None:
            pairs.append((s_, cw[k][1])); j = k + 1
    if len(pairs) < 2:
        return x
    ts = np.array([p[0] for p in pairs]); cs = np.array([p[1] for p in pairs])
    best = None
    for tempo in np.arange(0.97, 1.151, 0.01):
        for i in range(len(pairs)):  # candidate: word i lands 40 ms late
            at = cs[i] + 0.04 - (ts[i] - x['frm']) / tempo
            d = at + (ts - x['frm']) / tempo - cs
            if d[0] < -0.045:
                continue
            n = int(np.sum((d >= -0.045) & (d <= 0.125)))
            err = float(np.mean(np.abs(d - 0.04)))
            if best is None or (n, -err) > (best[0], -best[1]):
                best = (n, err, round(float(at), 4), round(float(tempo), 2))
    rows = word_table(x)
    have = sum(1 for _, d in rows if d is not None and -0.045 <= d <= 0.125)
    if best and best[0] > have:
        x = dict(x, at=best[2], tempo=best[3], placed='by-words')
    return x


def cmd_words(lines):
    fits = json.load(open(f'{SCENE}/fits.json'))
    out = {}
    for ln in lines:
        out[ln] = []
        for i, x in enumerate(fits[ln]['top']):
            rows = word_table(x)
            ok = sum(1 for _, d in rows if d is not None and -0.045 <= d <= 0.125)
            out[ln].append(dict(pick=f'p{i + 1}', clip=x['clip'], take=x['take'], tempo=x['tempo'], words=rows,
                                in_window=f'{ok}/{len(rows)}'))
            print(ln, f'p{i + 1}', x['clip'][5:9], x['take'], f'{ok}/{len(rows)} in window', '  '.join(
                f'{w}:{"?" if d is None else f"{int(d * 1000):+d}"}' for w, d in rows))
    json.dump(out, open(f'{SCENE}/word-table.json', 'w'), indent=1)


if __name__ == '__main__':
    c = sys.argv[1]; ls = sys.argv[2:] or list(LINES)
    dict(voices=lambda: cmd_voices(ls), jobs=cmd_jobs, exp_jobs=cmd_exp_jobs, revoice=lambda: cmd_revoice(ls), words=lambda: cmd_words(ls), check=lambda: cmd_check(ls), fit=lambda: cmd_fit(ls),
         render=lambda: cmd_render(ls))[c]()
