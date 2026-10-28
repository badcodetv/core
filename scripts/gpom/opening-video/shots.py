#!/usr/bin/env python3
"""The GPOM opening-recut clip list: Kai's picks on the storyboard, turned into Flow jobs.

Picks read 17 Oct 2026 from https://claude.ai/artifact/7HjuaiKdhp2EYYMxaepsTi (db `picks`):
animation option `a` on every frame; stills #5 TO1T-a, #6 MK3P-c, #12 WL3-b, #15 EY4-c.
Frames 2 and 9 are kept clips and frame 10 is ffmpeg (build-terminal-ownership.py), so they
spend no credits. The drop (11-15) sorts first.

    python3 scripts/gpom/opening-video/shots.py        # JSON for the runner
"""
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
SCENES = REPO / 'docs/stories/gitpush-origin-master/scenes'
CLIPS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/opening-recut')
OUT = CLIPS / 'video'
STILL_PICKS = {5: 'TO1T-a', 6: 'MK3P-c', 12: 'WL3-b', 15: 'EY4-c'}
SKIP = {2, 9, 10}
# Kai's redo notes, 17 Oct night. Key = frame + '-r2'; each replaces the first take's motion.
REDO = {
    12: ('WL3-b', 4, "The camera does not move. The hooded metal figure sings one long slow note: its metal jaw "
                     "opens wide, closes, then opens wide again. Its two red eye lights glow steadily. The "
                     "red-robed figures behind stand still. Mist drifts slowly through the light."),
    1: ('ST4-c', 6, "Top-down view. The camera does not move. Heavy rain falls. Everyone in the crowd stands "
                    "completely still under their umbrellas, like a photograph. Only the rain moves: streaks of "
                    "rain and ripples spreading across the puddles on the wet paving."),
    # Kai: new mixed, un-uniform boardroom (TO1T2-b, picked 17 Oct night). Three movers at most.
    5: ('TO1T2-b', 6, "The camera does not move. At the front, the laughing woman and the seated man clink their "
                      "champagne glasses and laugh. On the right, the man in the dark suit pours champagne into a "
                      "glass. Everyone else stands chatting quietly, barely moving. The screen behind them stays "
                      "the same. The city lights glitter in the windows."),
    # Kai: the light should flash on and off like a flashlight so it can be cut to the beat.
    14: ('EY1-b', 6, "The camera does not move and nothing in the landscape changes. The white light at the centre "
                     "of the ring switches on and off like a giant flashlight, in sharp hard flashes. "
                     "[00:00-00:01] blinding on, beams blasting out. [00:01-00:02] off, the centre dark. "
                     "[00:02-00:03] on. [00:03-00:04] off. [00:04-00:05] on. [00:05-00:06] off. "
                     "Dust rolls slowly round the base. The sun stays low on the horizon."),
}

# Round 3, Kai's notes on the r2 takes. #12: every wording with singing in it vanished (five
# silent blocks); Omni makes sound, so "sings"/"note" likely trips a music or voice filter. No
# singing words, and both face stills. #14: a strobe, several flashes a second, the red rim lights
# travelling, clouds drifting gently.
SILENT_JAW = ("The camera does not move. The hooded metal figure's jaw slowly opens wide and closes, then "
              "opens and closes again, steady and mechanical. Its two red eye lights glow. Mist drifts slowly "
              "through the light behind it. Silent.")
R3 = {
    # #4 extension (Kai): the email seen from outside his office. Kai picked TO3-a (faces us).
    '04-r2': ('TO3-a', 6, "The camera does not move. Rain streams down the glass in front of us. Inside the one lit "
                          "office, the man in the dark suit types steadily on his laptop, pauses, then types again, "
                          "his face lit blue by the screen. The dark windows of the tower around him stay still."),
    # 19 Oct: it is a corner office, so look at the tower's corner with the two window walls meeting -> TO4-c.
    '04-r3': ('TO4-c', 6, "The camera does not move. Rain streams down the two panes of glass that meet at the "
                          "corner of the tower. Inside the one lit corner office, the man in the dark suit types "
                          "steadily on his laptop, pauses, then types again, his face lit blue by the screen. Every "
                          "other window of the tower stays dark and still."),
    # 19 Oct: the cut from the singing robot straight to WL2-b made the robot seem to vanish. Kai asked for
    # a much wider WL2-b -- a vast parade ground of robot blocks -- between them. Kai away, said proceed:
    # the two widest stills (WL4-b, WL4-c) are both animated so he can pick on return.
    **{f'13-r2{x}': (f'WL4-{x}', 8, "The camera does not move. The floodlight beams under the hovering ship pour "
                                     "down into the glowing well and sweep slowly. Haze drifts low across the "
                                     "wet parade ground and storm clouds roll slowly overhead. The floodlight "
                                     "towers glow. The vast blocks of red hooded figures stand perfectly still "
                                     "in formation. The camera does not move.") for x in 'bc'},
    # Bread re-made without the child (Flow refused BR1's upload): Kai picked BR2-b then asked for no
    # pushchair at all -> BR3-a.
    '07-r2': ('BR3-a', 6, "The camera does not move. The tired woman stares at the card reader, then slowly looks "
                          "up, defeated, still holding the loaf against her chest. Rain runs down the shop window "
                          "behind her. The fluorescent light hums. Nothing else moves."),
    # Kai loved 14-r3 (strobe + travelling red dot); same movement on the zoomed-out eye.
    '15-r2': ('EY4-c', 6, "The camera does not move and the mountains, the sun and the ring keep their exact shape. "
                          "The white light at the centre of the ring strobes: it flashes hard on and snaps off, on "
                          "and off, several times a second, like a strobe light, lighting up the empty mountain "
                          "ranges with each flash. The small red lights on the rim light up one after another, so a "
                          "red dot travels steadily round the ring. The clouds drift very gently. Dust rolls slowly "
                          "off the summit."),
    # Round 4 (Kai): the robot works but opens its mouth far too wide; WL3-b is blocked on every
    # wording, so the face is WL3-a. Street: Kai picked ST5-a (fewer people, drizzle).
    '12-r4': ('WL3-a', 4, "The camera does not move. The hooded metal figure's jaw opens just slightly, a small gap, "
                          "then closes, then opens slightly again, gentle and steady, as if quietly mouthing words. "
                          "Its two red eye lights glow. Mist drifts slowly through the light behind it. Silent."),
    '01-r3': ('ST5-a', 6, "Top-down view. The camera does not move. A light drizzle falls. The people stand still "
                          "under their umbrellas, one or two shift their weight. Fine rain glints, and small ripples "
                          "spread across the few puddles on the damp paving."),
    '12-r3a': ('WL3-b', 4, SILENT_JAW),
    '12-r3b': ('WL3-a', 4, SILENT_JAW),
    '14-r3': ('EY1-b', 6, "The camera does not move and the mountains, the sun and the ring keep their exact shape. "
                          "The white light at the centre of the ring strobes: it flashes hard on and snaps off, on "
                          "and off, several times a second, like a strobe light. The small red lights on the rim "
                          "light up one after another, so a red dot travels steadily round the ring. The clouds "
                          "drift very gently. Dust rolls slowly round the base."),
}


def shots():
    sb = json.loads((SCENES / 'opening-recut-storyboard.json').read_text())['frames']
    ao = {f['n']: f for f in json.loads((SCENES / 'opening-recut-animation-options.json').read_text())['frames']}
    out = []
    for f in sb:
        n = f['n']
        if n in SKIP:
            continue
        opt = next(o for o in ao[n]['options'] if o['id'] == 'a')
        sid = STILL_PICKS.get(n, f['stills'][0])
        src = CLIPS / 'moodboard' / f'{sid}.jpg'
        assert src.exists(), src
        out.append({'key': f'{n:02d}', 'n': n, 'title': f['title'], 'still': sid, 'option': 'a',
                    'label': opt['label'], 'motion': opt['veo_prompt'], 'character': None,
                    'src': str(src), 'plate': f'gpom-op-{n:02d}-{sid}.jpg',
                    'out': str(OUT / f'op-{n:02d}-{sid}.mp4')})
    for key, (sid, dur, motion) in list(((f'{n:02d}-r2'), v) for n, v in REDO.items()) + list(R3.items()):
        n = int(key[:2])
        out.append({'key': key, 'n': n, 'title': 'redo', 'still': sid, 'option': 'a',
                    'label': 'redo', 'motion': motion, 'character': None, 'duration': dur,
                    'src': str(CLIPS / 'moodboard' / f'{sid}.jpg'), 'plate': f'gpom-op-{n:02d}-{sid}.jpg',
                    'out': str(OUT / f'op-{key}-{sid}.mp4')})
    return sorted(out, key=lambda s: (s['n'] < 11, s['n']))


if __name__ == '__main__':
    json.dump(shots(), sys.stdout, indent=1)
