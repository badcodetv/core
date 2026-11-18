#!/usr/bin/env python3
"""Lip-sync pass on GPOM scene C, the walk out (Kai, 18 Nov 2026: "move forward onto the next chunks"), with the method
that worked on scene A: clips first, a per-word table, re-voice with pause tags, rank by words in time
(.claude/skills/lip-sync-dub/SKILL.md, top). Reuses every step of lipsync-a-1118.py; only the scene's facts differ.

    python3 scripts/gpom/second-half-video/lipsync-c-1118.py jobs | voices | check | fit | words | revoice | render [line...]
"""
import importlib.util, json, os, shutil, sys

REPO = '/home/kai/projects/badcode/badcode'
spec = importlib.util.spec_from_file_location('la', f'{REPO}/scripts/gpom/second-half-video/lipsync-a-1118.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

m.PREFIX = 'lc'
m.MEDIA = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/C'
m.VOX, m.CLIPS, m.OUT = f'{m.MEDIA}/voices', f'{m.MEDIA}/video', f'{m.MEDIA}/pairs'
m.SCENE = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-c-walk-out/lipsync-1118'
SRC = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/C'
m.CUT = f'{SRC}/cut-noaliens'
m.STILL = {'woman': 'sandra-C04r2a', 'man': 'derek-C05r6b'}
m.BED = f'{SRC}/cut-noaliens/stems/10-sfx-wind.wav'
# the scene's own profiles (outdoors on the downs), same locked voices
_v = {x['file'].split('/')[-1]: x for x in json.load(open(f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-c-walk-out/voices.json'))['lines'].values()}
m.CASTD = {'woman': {'voice': 'Autonoe', 'prompt': _v['c4-0-sandra-r1c.wav']['prompt']},
           'man': {'voice': 'Algieba', 'prompt': _v['c4-1-derek-r1c.wav']['prompt']}}

DEREK = ("The camera does not move. The man and the woman walk steadily towards the camera side by side, shoulder to "
         "shoulder, and stay level with each other the whole time. The man, looking straight ahead, speaks straight away, "
         "weary and gentle, slowly, each word separate, with a small pause after the first sentence. He says: Doesn't "
         "bloody matter now, love. We're not coming back, are we? Then he closes his mouth and walks on in silence, his jaw "
         "set. Then he turns his head and gives the woman beside him a long, flat look, his mouth closed, saying nothing. "
         "The woman keeps her mouth closed throughout. The camera does not move.")
m.LINES = {
    'c4-0': ('woman', "I hope you put that bloody seat down.", "quick and clipped", 6,
             "The camera does not move. The woman walks steadily towards the camera with her mouth closed, her coat moving "
             "in the wind. After a moment she turns her head to the man beside her and speaks, slowly and pointedly, each "
             "word separate, as if to a child. She says: I hope you put that bloody seat down. Then she closes her mouth, "
             "looks ahead and keeps walking. The people behind keep walking. The camera does not move."),
    'c4-1': ('man', "Doesn't bloody matter now, love. We're not coming back, are we?", "weary and gentle, a real pause "
             "between the two sentences", 8, DEREK),
}
# the pause between Derek's sentences, written as an action (scene A: an action lengthened the clip's pause, [beat] less)
ACTION = DEREK.replace("He says: Doesn't bloody matter now, love. We're not coming back, are we?",
                       "He says: Doesn't bloody matter now, love. He looks down at the track for a moment, lips pressed "
                       "shut, then says: We're not coming back, are we?")
assert ACTION != DEREK
m.ARM_KEYS = {'action': 'klmn'}
JOBS = {'c4-0': [(k, None) for k in 'abcdefgh'], 'c4-1': [(k, None) for k in 'abcd'] + [(k, ACTION) for k in 'klmn']}
# where each line sits in the cut now (shot file, in, shot length, shot start in the preview)
m.NOW = {'c4-0': ('c04r1-seat-t1.mp4', 1.2083, 3.4167, 10.5), 'c4-1': ('c05r6-t1.mp4', 0.0, 6.7917, 13.9167)}
# From the per-word table (18 Nov): Derek's first sentence lands, everything after "love." is 0.8-0.9 s early, so the
# clips pause ~0.9 s longer between the sentences than take a/c. Locked model only (Kai picked 3.1 takes on scene A).
m.REVOICE = {'c4-1': ["Doesn't bloody matter now, love. <long pause> We're not coming back, are we?",
                      "Doesn't bloody matter now, love... <long pause> We're not coming back, are we?",
                      "Doesn't bloody matter now, love. <long pause> <long pause> We're not coming back, are we?"]}
m.MODELS = {'31': 'gemini-3.1-flash-tts-preview'}


def setup():
    os.makedirs(f'{m.MEDIA}/moodboard', exist_ok=True); os.makedirs(f'{m.CLIPS}/inbox', exist_ok=True)
    os.makedirs(m.VOX, exist_ok=True); os.makedirs(m.SCENE, exist_ok=True)
    for still, src in (('sandra-C04r2a', f'{SRC}/stills/C04-r2-a.jpg'), ('derek-C05r6b', f'{SRC}/stills/fix6/C05r6-b.jpg')):
        if not os.path.exists(f'{m.MEDIA}/moodboard/{still}.jpg'):
            shutil.copy(src, f'{m.MEDIA}/moodboard/{still}.jpg')
    # the takes in the cut now are take a
    for ln, f in (('c4-0', 'c4-0-sandra-r1c.wav'), ('c4-1', 'c4-1-derek-r1c.wav')):
        if not os.path.exists(f'{m.VOX}/{ln}-a.wav'):
            shutil.copy(f'{SRC}/voices/{f}', f'{m.VOX}/{ln}-a.wav')
    for ln, (who, *_r) in m.LINES.items():
        open(f'{m.SCENE}/{ln}.profile.md', 'w').write(m.CASTD[who]['prompt'])
    # reuse the 10 pool projects scene A's run made (same story)
    pool = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/A/video/inbox/pool.json'
    if not os.path.exists(f'{m.CLIPS}/inbox/pool.json'):
        shutil.copy(pool, f'{m.CLIPS}/inbox/pool.json')
    json.dump(dict(story='gitpush-origin-master', scene='gpom-lipsync-c-1118', prefix='lc', title='GPOM scene C walk out: lip-sync pass 18 Nov',
                   media=m.MEDIA, flow_project='462e2124-a6c6-4630-a121-7ee651daf338',
                   video={'model': 'Omni 1.2 Flash', 'aspect': '16:9', 'mode': 'Frames', 'duration': 6},
                   about='Kai 18 Nov: scene C talking lines with the pause-tag method. Script: scripts/gpom/second-half-video/lipsync-c-1118.py'),
              open(f'{m.SCENE}/scene.json', 'w'), indent=1)


def cmd_jobs():
    setup()
    extra = []
    for ln, keys in JOBS.items():
        who, _, _, dur, motion = m.LINES[ln]
        for k, alt in keys:
            extra.append(dict(key=f'L{ln.replace("-", "")}{k}', n=0, still=m.STILL[who], duration=dur, motion=alt or motion,
                              character=None, why=f'lip-sync 18 Nov scene C: line {ln} clip {k}{" (pause as action)" if alt else ""}'))
    json.dump(dict(extra=extra), open(f'{m.SCENE}/video-jobs.json', 'w'), indent=1)
    print(len(extra), 'jobs')


if __name__ == '__main__':
    c = sys.argv[1]; ls = sys.argv[2:] or list(m.LINES)
    if c == 'jobs':
        cmd_jobs()
    elif c == 'voices':
        m.KEYS = os.environ.get('TAKES', 'bcde'); m.cmd_voices(ls)
    else:
        dict(check=lambda: m.cmd_check(ls), fit=lambda: m.cmd_fit(ls), words=lambda: m.cmd_words(ls),
             revoice=lambda: m.cmd_revoice(ls), render=lambda: m.cmd_render(ls))[c]()
