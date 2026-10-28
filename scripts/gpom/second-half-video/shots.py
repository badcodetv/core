#!/usr/bin/env python3
"""The GPOM second-half clip list: Kai's picks on the storyboard, turned into Flow jobs.

Picks read 17 Oct 2026 from https://claude.ai/artifact/EGgHQU6KzN9rgzGnyUHb6e (db `picks`):
animation option `a` for every frame except 2 and 3 (`c`), and still SB27a for frame 29. No
`notes`. Frames without a still pick take the storyboard's stills[0].

Only frames whose picked option has a Veo lane are here. The rest are post jobs (Premiere camera,
ffmpeg HUD, holds) and spend no credits: 4, 11, 13, 16, 18, 21, 23, 24, 27.

Two deviations from the options file, both forced by the plates:
  * 12a's veo_prompt is only the explosion ELEMENT on black, and its plate lane assumed machines
    idling at the doors. SB12a already shows the blasts mid-burst, so the plate prompt continues
    them. The element on black is a separate text-to-video job (`12-element`, no plate).
  * 7a is "two clips, one speaker each". Clip 2 animates SB07c (him, over her shoulder), the
    reverse of SB07a.

    python3 scripts/gpom/second-half-video/shots.py        # JSON for the runner
"""
import json
import os
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
SCENES = REPO / 'docs/stories/gitpush-origin-master/scenes'
CLIPS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half')
OUT = CLIPS / 'video'
BOT = 'West Country Bot'

ANIM_PICKS = {n: 'a' for n in range(1, 30)} | {2: 'c', 3: 'c'}
STILL_PICKS = {29: 'SB27a'}
# Frames whose clip moves the bot, so the Character is cast to hold its design (Kai, 17 Oct).
CAST = {9, 15, 19, 20}

# Prompts that replace or add to the options file (see the docstring).
OVERRIDE = {
    12: "The camera does not move. The three explosions keep bursting outward in white flashes in front of the "
        "bunker, sparks raining down and black smoke rolling up the grassy hillside; the green blast doors stay "
        "shut and untouched. The camera does not move.",
}
EXTRA = [
    {'key': '07-2', 'n': 7, 'still': 'SB07c',
     'motion': "The camera does not move. The man in the dark green jumper protests hard, throwing his hands wide, "
               "his face indignant; the woman in the cream jumper at the edge of frame stays still, her back to us. "
               "The camera does not move."},
    # Re-roll of 15 (2026-10-17): 15a's "rolls forward out of the smoke through the open blast doors"
    # made Omni put the bot back at the doors, because the plate already has it inside. Start the move
    # where the plate has the bot. Docs: automation-2026-09-rebuild.md item 77.
    {'key': '15-r2', 'n': 15, 'still': 'SBHELLOa', 'character': BOT,
     'motion': "The camera does not move. The small grey six-wheeled delivery robot, already inside the tunnel and "
               "close to camera, creeps forward a short way, about half a metre, and stops; its amber beacon "
               "blinks once. The torn bunting on its wheel flutters. Smoke drifts in the grey daylight behind it. "
               "The people in the foreground stay still. The camera does not move."},
    # Cast takes of 9 and 20: the first takes went in uncast (the Character had dropped off the "@" list).
    {'key': '09-c', 'n': 9, 'still': 'SB09a', 'character': BOT, 'label': 'cast take', 'motion': None},
    {'key': '20-c', 'n': 20, 'still': 'SB20a', 'character': BOT, 'label': 'cast take', 'motion': None},
]
# Flow refused SBEMERa at upload (UPLOAD_REFUSED, 2026-10-17); frame 19's other still stands in.
STILL_PICKS[19] = 'SBEMERb'
ELEMENT = {'key': '12-element', 'n': 12, 'still': None,
           'motion': None}  # filled from the options file below


# Cut 2 part 1 (beats 0-18): the four new shots N1-N4 from the `cut2.shots` block of
# second-half-audio-plan.json. Picks, prompts and why: scenes/second-half-cut2-shots.md. Selected with
# `--cut2` or GPOM_CUT2=1, so the old 29-frame list (and the old rough cut) is untouched. Stills live in
# storyboard/cut2/, clips land as video/cut2-N<k>.mp4, harvested through video/inbox-cut2/.
CUT2 = '--cut2' in sys.argv or os.environ.get('GPOM_CUT2') == '1'
CUT2_SHOTS = [
    {'key': 'N1', 'beat': '13', 'title': 'Bunker reaction', 'still': 'cut2/N1-b', 'character': None,
     'motion': "The camera does not move. Dust and grit keep sifting down from the cracked ceiling through the "
               "fluorescent light, and the tube flickers. The woman in the cream jumper and the man in the dark green "
               "jumper stay frozen mid-argument with their arms still raised, slowly tilting their heads further up; "
               "the two people at the right edge look up, then glance at each other. The camera does not move."},
    {'key': 'N2', 'beat': '14a', 'title': 'Maddie at the wrecked machines', 'still': 'cut2/N2-a', 'character': BOT,
     'motion': "The camera does not move. The small grey six-wheeled delivery robot races on up the scorched track "
               "towards the green blast doors, its wheels throwing up dust and grit, its amber beacon flashing and the "
               "torn bunting flapping, then skids to a stop in front of the doors. Smoke keeps rising from the three "
               "wrecked machines. The camera does not move."},
    {'key': 'N3', 'beat': '14b', 'title': 'The tannoy', 'still': 'cut2/N3-a', 'character': None,
     'motion': "The camera does not move. The bare bulb beside the cream tannoy horn flickers, dims and steadies, as "
               "if a voice is coming through. Dust drifts in its light. The people below keep looking up at the horn; "
               "a few shift their weight and glance at each other. The camera does not move."},
    {'key': 'N4', 'beat': '17', 'title': 'The old lady blocks the way', 'still': 'cut2/N4r2-b', 'character': None,
     'motion': "The camera does not move. The old woman stands her ground in the open blast doors, arms folded, "
               "staring down; she tightens her folded arms, lifts her chin and her mouth sets hard. Behind her smoke "
               "drifts across the hillside in the grey daylight. The amber beacon in the corner pulses slowly. The "
               "camera does not move."},
]


def cut2_shots():
    out = []
    for s in CUT2_SHOTS:
        out.append({**s, 'n': s['key'], 'option': 'cut2', 'label': f"cut2 beat {s['beat']}",
                    'src': str(CLIPS / 'storyboard' / f"{s['still']}.jpg"),
                    'plate': f"gpom-c2-{s['key']}-{s['still'].split('/')[-1]}.jpg",
                    'out': str(OUT / f"cut2-{s['key']}.mp4")})
    return out


def still_path(sid):
    for d in ('storyboard', 'moodboard'):
        p = CLIPS / d / f'{sid}.jpg'
        if p.exists():
            return str(p)
    raise SystemExit(f'no still {sid}')


def shots():
    if CUT2:
        return cut2_shots()
    sb = json.loads((SCENES / 'second-half-storyboard.json').read_text())['frames']
    ao = {str(f['n']): f for f in json.loads((SCENES / 'second-half-animation-options.json').read_text())['frames']}
    out = []
    for f in sb:
        n = f['n']
        opt = next(o for o in ao[str(f['anim'])]['options'] if o['id'] == ANIM_PICKS[n])
        motion = OVERRIDE.get(n, opt.get('veo_prompt') or '')
        if not motion or not f['stills']:
            continue
        sid = STILL_PICKS.get(n, f['stills'][0])
        key = f'{n:02d}-1' if n == 7 else f'{n:02d}'
        out.append({'key': key, 'n': n, 'title': f['title'], 'still': sid, 'option': opt['id'],
                    'label': opt['label'], 'motion': motion, 'character': BOT if n in CAST else None})
        if n == 12:
            ELEMENT['motion'] = opt['veo_prompt']
    for e in EXTRA:
        f = next(x for x in sb if x['n'] == e['n'])
        if e.get('motion') is None:
            e = {**e, 'motion': next(s['motion'] for s in out if s['n'] == e['n'])}
        out.append({'title': f['title'], 'option': 'a', 'character': None,
                    'label': 'second speaker' if e['key'] == '07-2' else 're-roll', **e})
    out.append({**ELEMENT, 'title': 'Explosion element on black', 'option': 'a', 'label': 'keyed blast',
                'character': None})
    for s in out:
        s['src'] = still_path(s['still']) if s['still'] else None
        s['plate'] = f"gpom-sh-{s['key']}-{s['still']}.jpg" if s['still'] else None
        s['out'] = str(OUT / f"sh-{s['key']}{'-' + s['still'] if s['still'] else ''}.mp4")
    return sorted(out, key=lambda s: s['key'])


if __name__ == '__main__':
    json.dump(shots(), sys.stdout, indent=1)
