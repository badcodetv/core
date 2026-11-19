#!/usr/bin/env python3
"""Lip-sync pass on GPOM scene D, the clean room (Kai, 19 Nov: "let's go with the next stages"), with the method that
worked on scenes A and C: clips first, a per-word table, re-voice with pause tags where the clips pause, rank by words
in time (.claude/skills/lip-sync-dub/SKILL.md, top). Reuses every step of lipsync-a-1118.py; only the scene's facts differ.

Three talking shots in cut r23: Sandra on D01h (the changing room, the old lady beside her), the old lady on D11c (close-up),
Sandra on D08c (two-shot, Derek's shoulder on the left). The takes in the cut now on D11c and D08c are the old method
(cut phrase by phrase onto the mouth, the "-dub" files); take a here is the whole take they were cut from.

    python3 scripts/gpom/second-half-video/lipsync-d-1119.py jobs | voices | check | fit | words | revoice | render [line...]
"""
import importlib.util, json, os, shutil, sys

REPO = '/home/kai/projects/badcode/badcode'
spec = importlib.util.spec_from_file_location('la', f'{REPO}/scripts/gpom/second-half-video/lipsync-a-1118.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

m.PREFIX = 'ld'
m.MEDIA = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/D'
m.VOX, m.CLIPS, m.OUT = f'{m.MEDIA}/voices', f'{m.MEDIA}/video', f'{m.MEDIA}/pairs'
D = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-d-crossing'
m.SCENE = f'{D}/lipsync-1119'
SRC = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/D'
m.CUT = f'{SRC}/cut-r23'
m.STILL = {'sandra-d1': 'sandra-D01h', 'lady': 'lady-D11c6', 'sandra-d3': 'sandra-D08c'}
m.FACE = {'sandra-D01h': 'right', 'sandra-D08c': 'right'}  # the old lady is on Sandra's left in D01h, Derek in D08c
m.BED = f'{SRC}/cut-r23/stems/11-sfx-room.wav'
# each line's own profile from the scene's voices.json (same locked voices: Autonoe, Vindemiatrix)
_v = json.load(open(f'{D}/voices.json'))['lines']
m.CASTD = {'sandra-d1': {'voice': 'Autonoe', 'prompt': _v['d1-1-sandra']['prompt']},
           'lady': {'voice': 'Vindemiatrix', 'prompt': _v['d3-10-lady']['prompt']},
           'sandra-d3': {'voice': 'Autonoe', 'prompt': _v['d3-14-sandra']['prompt']}}

D3_14 = ("One continuous shot, the camera holds still on the two of them. The woman in the cream polo neck looks at the man "
         "and, quietly and uneasily, she says: I don't like the idea of... She stops, lips pressed shut, and glances down "
         "for a moment, then looks back up at him and says: it feels like dying. Then her mouth stays closed and she just "
         "looks at him, frightened, to the end. The man on the left listens, still. The small robot behind them waits. "
         "No cuts, no music.")
m.LINES = {
    'd1-1': ('sandra-d1', "I hope this bloody plan works.", "worried, under her breath", 6,
             "The camera does not move. In the white changing room the old woman on the left fastens her white suit and says "
             "nothing. The woman on the right, in the cream polo neck and an open white suit, stands with her mouth closed "
             "for a moment, then, worried, under her breath, she says: I hope this bloody plan works. Then she closes her "
             "mouth and looks ahead. The people behind keep pulling on their suits. The camera does not move."),
    'd3-10': ('lady', "And afterwards?", "quiet and plain", 6,
              "One continuous close-up, the camera holds completely still on the old woman in glasses resting her head "
              "against the dark chair. For a moment she listens, eyes on someone off to the right. Then she lifts her chin "
              "slightly and asks, quietly and plainly: And afterwards? Then her lips close and stay closed; she waits for "
              "the answer, still looking right, and gives one small slow breath. No cuts, no music."),
    'd3-14': ('sandra-d3', "I don't like the idea of... it feels like dying.", "frightened, a real pause after 'of'", 8, D3_14),
}
m.ARM_KEYS = {}
JOBS = {'d1-1': 'abcdef', 'd3-10': 'abcdef', 'd3-14': 'abcdef'}
# Flow clips already made for these shots, free extra candidates (key y/z: never a pool key)
OLD = {'d1-1': {'y': 'D01h-t2.mp4'}, 'd3-10': {'y': 'D11c-t2a.mp4', 'z': 'D11c-t2b.mp4'},
       'd3-14': {'y': 'D08c-t2a.mp4', 'z': 'D08c-t2b.mp4'}}
# where each line sits in cut r23 (shot file, in, length shown on the page, shot start in the preview). D01h is only
# 2.04 s in the cut: "plan works." plays over the cut to D02 (the old phrase-by-phrase fit), so the page shows 2.9 s.
m.NOW = {'d1-1': ('D01h-t2.mp4', 0.0, 2.9, 3.4583), 'd3-10': ('D11c-t2a.mp4', 0.0, 5.4583, 31.5417),
         'd3-14': ('D08c-t2a.mp4', 0.0, 5.625, 42.9583)}
# the whole takes the cut's voices came from are take a; the other passing takes of that round follow
TAKES = {'d1-1': ['d1-1-sandra-r4a.wav', 'd1-1-sandra-r4c.wav'],
         'd3-10': ['d3-10-lady-r23ya.wav', 'd3-10-lady-r23yb.wav', 'd3-10-lady-r23yc.wav', 'd3-10-lady-r23yd.wav'],
         'd3-14': ['d3-14-sandra-r17qd.wav', 'd3-14-sandra-r17qa.wav', 'd3-14-sandra-r17qb.wav', 'd3-14-sandra-r17qc.wav']}
m.REVOICE = {}
m.MODELS = {'31': 'gemini-3.1-flash-tts-preview'}


def setup():
    for d in (f'{m.MEDIA}/moodboard', f'{m.CLIPS}/inbox', m.VOX, m.SCENE):
        os.makedirs(d, exist_ok=True)
    for still, src in (('sandra-D01h', f'{SRC}/stills/fix2/D01h-r2-b.jpg'), ('lady-D11c6', f'{SRC}/stills/fix6/D11c6-d.jpg'),
                       ('sandra-D08c', f'{SRC}/stills/fix14/D08c-r14-b.jpg')):
        if not os.path.exists(f'{m.MEDIA}/moodboard/{still}.jpg'):
            shutil.copy(src, f'{m.MEDIA}/moodboard/{still}.jpg')
    for ln, fs in TAKES.items():
        for k, f in zip('abcd', fs):
            if not os.path.exists(f'{m.VOX}/{ln}-{k}.wav'):
                shutil.copy(f'{SRC}/voices/{f}', f'{m.VOX}/{ln}-{k}.wav')
    for ln, olds in OLD.items():
        who = m.LINES[ln][0]
        for k, f in olds.items():
            dst = f'{m.CLIPS}/ld-L{ln.replace("-", "")}{k}-{m.STILL[who]}.mp4'
            if not os.path.exists(dst):
                shutil.copy(f'{SRC}/clips/{f}', dst)
    for ln, (who, *_r) in m.LINES.items():
        open(f'{m.SCENE}/{ln}.profile.md', 'w').write(m.CASTD[who]['prompt'])
    pool = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/A/video/inbox/pool.json'
    if not os.path.exists(f'{m.CLIPS}/inbox/pool.json'):
        shutil.copy(pool, f'{m.CLIPS}/inbox/pool.json')
    json.dump(dict(story='gitpush-origin-master', scene='gpom-lipsync-d-1119', prefix='ld', title='GPOM scene D clean room: lip-sync pass 19 Nov',
                   media=m.MEDIA, flow_project='462e2124-a6c6-4630-a121-7ee651daf338',
                   video={'model': 'Omni 1.2 Flash', 'aspect': '16:9', 'mode': 'Frames', 'duration': 6},
                   about='Kai 19 Nov: scene D talking lines with the pause-tag method. Script: scripts/gpom/second-half-video/lipsync-d-1119.py'),
              open(f'{m.SCENE}/scene.json', 'w'), indent=1)


def cmd_jobs():
    setup()
    extra = []
    for ln, keys in JOBS.items():
        who, _, _, dur, motion = m.LINES[ln]
        for k in keys:
            extra.append(dict(key=f'L{ln.replace("-", "")}{k}', n=0, still=m.STILL[who], duration=dur, motion=motion,
                              character=None, why=f'lip-sync 19 Nov scene D: line {ln} clip {k}'))
    json.dump(dict(extra=extra), open(f'{m.SCENE}/video-jobs.json', 'w'), indent=1)
    print(len(extra), 'jobs')


if __name__ == '__main__':
    c = sys.argv[1]; ls = sys.argv[2:] or list(m.LINES)
    if c == 'jobs':
        cmd_jobs()
    elif c == 'voices':
        setup(); m.KEYS = os.environ.get('TAKES', 'abcd'); m.cmd_voices(ls)
    else:
        dict(check=lambda: m.cmd_check(ls), fit=lambda: m.cmd_fit(ls), words=lambda: m.cmd_words(ls),
             revoice=lambda: m.cmd_revoice(ls), render=lambda: m.cmd_render(ls))[c]()
