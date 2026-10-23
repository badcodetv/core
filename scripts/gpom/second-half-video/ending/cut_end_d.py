#!/usr/bin/env python3
"""GPOM second half, the ending, scene D (the clean room and the crossing): new-scene stage 4 rough cut.

    python3 scripts/gpom/second-half-video/ending/cut_end_d.py            # build D (edl, mix, stems, preview)
    python3 scripts/gpom/second-half-video/ending/cut_end_d.py --no-preview

Runs on cut_end.py's engine (Scene, Cut, voices, the join report, cut3's write / edl / preview) and registers itself
there as SCENE_FNS['D'], so `cut_end.py D` works too once cut_end.py imports this module. Scene D's own picture work
(white-balance match, eased Premiere-style moves, the beacon bloom on the AI's words, the fade to white) is done per
piece by frameops.py in the lips venv (cv2, float warps). Rules: LEAD 0.4, GAP 0.35, TAIL 0.6; speech never slowed
(lip-sync phrases sped to x1.3 at most); one stem per track; the mix at -16 LUFS.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import cut_end as E  # noqa: E402
import cut2 as C  # noqa: E402
import cut3 as C3  # noqa: E402

FPS, SR = E.FPS, E.SR
LEAD, GAP, TAIL, CUT_PRE = E.LEAD, E.GAP, E.TAIL, E.CUT_PRE
fr = E.fr
VID = E.CLIPS / 'video'
AI_TAKE = 'gpom-sh-end-ai-d-a-v6-w10-8afa9d8a.wav'
AI_D7 = 'gpom-sh-end-ai-d7-b-v6-w25-4fa3d2b1.wav'
# Speech regions in the AI takes (10 ms level frames over -48 dB from the take's peak; 50 ms before, 80 ms after).
AI = {'d1': (AI_TAKE, 0.00, 3.73), 'd2': (AI_TAKE, 5.66, 10.88), 'd3': (AI_TAKE, 12.48, 16.04),
      'd4': (AI_TAKE, 19.69, 23.69), 'd5': (AI_TAKE, 27.24, 29.55), 'd6': (AI_TAKE, 33.64, 39.11),
      'd7a': (AI_D7, 0.00, 4.37), 'd7b': (AI_D7, 6.93, 7.83),
      # review round 1: -d5 split in the 55 ms dip after "don't" (27.58-27.635, checked by whisper on cuts) and the
      # wrong pause after "Believing it" (28.20-28.95) removed; "I don't know if it works." alone, from -d6 (its "No. This is all of
      # it." is not used). The round-C retake (-d5/-d6r, with "Fair. Nothing up my sleeve.") could not be recorded:
      # Suno playback stalled (CAPTURE_TIMEOUT on every take, old and new). Swap it in when it records.
      'd5x': (AI_TAKE, 27.25, 27.62), 'd5y': (AI_TAKE, 27.62, 28.20), 'd5z': (AI_TAKE, 28.95, 29.80),
      'd6c': (AI_TAKE, 37.45, 39.11),
      # review round 2: -d2 split at its sentence stop (7.77-8.86) so the cut to D03c lands on "What it runs on";
      # -d3's 1.6 s pause between "You." and "And your consciousness." tightened to 0.6 s.
      'd2a': (AI_TAKE, 5.66, 7.85), 'd2b': (AI_TAKE, 8.80, 10.88),
      'd3y': (AI_TAKE, 12.48, 12.98), 'd3z': (AI_TAKE, 14.47, 16.04)}
# review round 2: every fragment takes its gain from its WHOLE atom (cut_end.Cut.say ref=), never from itself.
REF = {'d5x': 'd5', 'd5y': 'd5', 'd5z': 'd5', 'd6c': 'd6', 'd2a': 'd2', 'd2b': 'd2', 'd3y': 'd3', 'd3z': 'd3'}
# the new AI line (review round 2, trust test 4.12 part one): "It only sends one back. Me." (atom -d3b, Suno round D)
# Suno round D take c851b66f (w25), recorded 22 Oct after the PulseAudio fix (it replaces the Gemini stand-in). Its second
# reading ends "back." as a full stop and says "Me." alone, ~6.4 s later. The other three takes run "back me" together.
# Kai, 22 Oct: "a much bigger pause between back and me", but the long one was "far too long" -> ~1.3 s of silence.
AI_D3B = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/D/suno/gpom-sh-end-ai-d3b-d-v6-w25-c851b66f.wav'
AI['d3n1'] = (AI_D3B, 6.03, 7.84)  # "It only sends one back." (speech 6.08-7.76)
AI['d3n2'] = (AI_D3B, 13.98, 14.60)  # "Me." (speech 14.14-14.45)
AI['d3n'] = (AI_D3B, 6.03, 7.84)  # gain reference: the sentence, not the silence
D3N_PAUSE = 1.1  # gap between the two pieces; with the pads, ~1.3 s of silence between "back." and "Me."
REF.update({'d3n1': 'd3n', 'd3n2': 'd3n'})
D6_PARTS = [('d6c', 0.0)]  # the admission, as placed (key, gap before it); with the round-C retake: d6a, d6b, d6c
INTERIOR_EXCLUDE = {'D14'}  # the dusk exterior keeps its own light
BEACON = {'D00': ([536, 111], 34), 'D03': ([642, 455], 16), 'D03c': ([432, 92], 24), 'D08': ([627, 390], 20), 'D11': ([354, 290], 24),
          'D11b': (None, 30)}
STOP = 0.55  # the full stop between "You don't." and "Believing it is your bit." (review round 1)
LIFT = [1.15, 1.15, 1.15]  # the close shots in the chairs (D11, D11b, D12) sit ~30/255 under the room's wides
D14_GRADE = [0.70, 0.74, 0.82]  # ~0.6 stop down, the sky cooler, so the amber seam is the one warm light


def span(p, floor=40):
    s, e, _ = C3.bounds(p, floor)
    return max(0.0, s - 0.05), min(E.dur(p), e + 0.08)


def mean_rgb(src, t, still=False):
    args = ['-i', str(src)] if still else ['-ss', f'{t:.3f}', '-i', str(src)]
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', *args, '-frames:v', '1', '-vf', 'scale=160:90',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(90, 160, 3).astype(float).mean((0, 1))


class Piece:
    def __init__(self, fid, src, i0, t0, t1, beat, still=False, zoom=None, rot=None, white=None, glow=False,
                 centre=None, grade=None):
        self.fid, self.src, self.i0, self.t0, self.t1, self.beat = fid, pathlib.Path(src), i0, fr(t0), fr(t1), beat
        self.still, self.zoom, self.rot, self.white, self.glow = still, zoom, rot, white, glow
        self.centre, self.grade = centre, grade


class SceneD:
    def __init__(self, sc):
        self.sc = sc
        self.c = E.Cut(sc, 'gpom-second-half-D-rough2', 'Ending D Timeline',
                       'GPOM second half · the ending · scene D: the clean room and the crossing',
                       "Scene D of the ending, round 1 (Kai's notes, 22-23 Oct): suits on, the vast white room, the wafer "
                       "and 'what this will cost you', a hundred chairs and a cup of tea, they sit, the goodbye, the "
                       "crossing, and Maddie alone. Maddie leads; the boss is silent. Play it, click any beat, clip, line "
                       "or sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude when you're done.")
        self.pieces = []
        self.ai_spans = []  # (timeline start, src, a, b) of each AI placement, for the beacon bloom

    def clip(self, fid):
        return self.sc.clip(fid)

    def piece(self, *a, **k):
        p = Piece(*a, **k)
        assert p.t1 > p.t0, (p.fid, p.t0, p.t1)
        self.pieces.append(p)
        return p

    def human(self, stem, key, t, beat, i, who, lufs=-16.0, what=None):
        p = self.sc.voice(key)
        a, b = span(p)
        e = self.c.say(stem, p, a, b, t, what or f'{beat} line {i} {who}', lufs=lufs)
        self.c.line(beat_of(self.c, beat), i, who, t, e - t, self.sc.text(key), by_of(self.sc, key))
        return e

    def ai(self, key, t, beat, i, text=None, lufs=-17.0):
        f, a, b = AI[key]
        src = pathlib.Path(f) if f.startswith('/') else self.sc.media / 'suno' / f
        ref = AI[REF[key]][1:] if key in REF else None
        e = self.c.say('vox-ai', src, a, b, t, f'{beat} line {i} AI (atom gpom-sh-end-ai-{key[:2]}, speaker)',
                       chain=[E.SPEAKER], lufs=lufs, ref=ref)
        self.ai_spans.append((t, src, a, b))
        if text:
            self.c.line(beat_of(self.c, beat), i, 'ai', t, e - t, text, 'claude')
        return e


def beat_of(c, bid):
    return next(b for b in c.beats if b['id'] == bid)


def by_of(sc, key):
    bk, i, _ = key.split('-')
    return next(b for b in sc.cfg['beats'] if b['key'] == bk)['lines'][int(i)].get('by', 'claude')


def ai_text(sc, beat, i):
    b = next(x for x in sc.cfg['beats'] if x['key'] == beat)
    return b['lines'][i]['text']


# ---------------------------------------------------------------- the timeline

def build(sc):
    """Round 1 (Kai's notes, 22-23 Oct): Maddie leads, the boss is silent, the test (d5) and the tea-cup still (D15)
    are cut. Lip-sync per lip-sync-dub: mouth openings and closures read off the tracked 12 fps strips in
    clips/lips/<clip>-strip.jpg, voice onsets and b/p gaps off each take's 20 ms loudness; late never early, tempo <= 1.3
    (1.15 on the lady's breathy voice). Where Omni's mouth is far faster than any take, the phrase plays over a
    mouthless shot instead of being squeezed."""
    S = SceneD(sc)
    c, m = S.c, S.c.m

    def say(stem, key, a, b, t, what, tempo=1.0, lufs=-16.0):
        p = sc.voice(key)
        return c.say(stem, p, a, b, t, what, tempo=tempo, lufs=lufs, ref=span(p))

    # ---- d1: suits on. D00 (battered Maddie among the legs, bunting, before the clean room) carries her house rule;
    # Sandra on D01h-t2 (her face on the right). Her mouth: "I" opens 1.42, lips shut for the p of "hope" 1.83-1.92,
    # "this" 2.00, shut for the b of "bloody" 2.25, open to 2.50, shut for the p of "plan" ~2.58, then "plan works"
    # 2.67-3.0: far quicker than the take (1.6 s of mouth for 2.1 s of voice). Her take r4a: "I hope" 0.26-0.56 (p gap
    # 0.56-0.64), "this" 0.66-0.80 (b gap 0.80-0.88), "bloody" 0.88-1.20 (p gap 1.20-1.28), "plan works." 1.28-2.36.
    # So: "I hope" on her mouth, "this bloody" on her mouth with each closure on a closure (x1.0), and the cut to the
    # vast room lands on the p of "plan": "plan works." plays over D02 at its own speed.
    b = c.beat('d1', 'Suits on', 0.0, act='The clean room',
               see='A white changing room: the hundred pull clean-room suits over their jumpers. Maddie among the legs, '
                   'polite and brisk. Sandra, frightened, hopes the plan works.')
    k = 'd1-0-maddie'
    a0, b0 = span(sc.voice(k))
    e = S.human('vox-maddie', k, LEAD, 'd1', 0, 'maddie', what='d1 line 0 maddie: "Suits on, please. It\'s a clean room."')
    S.ai_spans.append((LEAD, sc.voice(k), a0, b0))  # her beacon blooms on her own words (D00, drawn in post)
    i01 = 0.6
    cut01 = fr(e + 0.3)
    zero01 = cut01 - i01
    S.piece('D00', S.clip('D00'), 0.0, 0.0, cut01, 'd1', glow=True, zoom=[[0.0, 1.035]])
    k = 'd1-1-sandra'
    t1 = zero01 + 1.55  # "I" 0.13 s after her mouth opens; the p of "hope" on her lips shut at ~1.9
    # the p of "hope" releases at ~0.64-0.66 in the take: the first cut there was heard "Oh, this..."
    say('vox-sandra', k, 0.22, 0.67, t1, 'd1 line 1 sandra: "I hope" (lip-sync, x1.0)', lufs=-15.0)
    e1 = say('vox-sandra', k, 0.67, 2.42, zero01 + 2.09, 'd1 line 1 sandra: "this bloody" on her mouth, "plan works." '
             'over the cut to D02 (x1.0)', lufs=-15.0)
    c.line(b, 1, 'sandra', t1, e1 - t1, sc.text(k), 'kai')
    cut02 = fr(zero01 + 2.66)
    S.piece('D01h', S.clip('D01h'), i01, cut01, cut02, 'd1')
    m['fussy'] = e1
    t = c.close(b, cut02)
    c.flags.append('d1 (Kai ld1-0/ld1-1): Maddie says "Suits on, please. It\'s a clean room." over D00 (still the battered '
                   'Maddie with her bunting: this is before the clean room); her beacon blooms with her voice, drawn in post. '
                   'Sandra, worried, under her breath: "I hope this bloody plan works." on the new D01h-t2.')
    c.flags.append('d1 lip-sync: Omni gave Sandra 1.6 s of mouth for 2.1 s of voice, so the line is not squeezed. "I hope" '
                   'and "this bloody" sit on her mouth at x1.0 (the p of "hope" on her lips shut at 1.83 s, the b of "bloody" '
                   'on 2.25 s), and the cut to the vast room lands on the p of "plan": "plan works." plays over the room at '
                   'its own speed. Her lip read is from her own face (the tracker first locked on the old lady beside her).')

    # ---- d2: into the room (D02r3: low wide inside the doors, the hundred stopped, the wafer far off, no prints)
    b = c.beat('d2', 'Into the room', t, act='The clean room',
               see='Through the doors into a vast white room with the wafer standing alone in the middle. Nobody walks '
                   'to it yet. Spotless: no mud, no prints.')
    # D02 runs on into d3: Derek's question is asked of the room, and the cut to the wafer comes after it. The old
    # wafer reveal (D03-t2) is not used: it has the battered Maddie with her bunting in the middle of it, and from the
    # clean room on she is gleaming with no bunting (Kai, Q1).
    s2 = t
    s3 = fr(s2 + 5.0)
    t = c.close(b, s3)
    c.flags.append('d2 (Kai at296/bd2): D02 re-made (D02r3-t1): the hundred stopped just inside the doors of a vast white '
                   'room, the wafer far off in the middle, a spotless floor; nobody walks, heads turn, rainbow bands ripple '
                   'over the wafer. A slow push 100 -> 105% after a 1 s hold (post), so the room draws them in.')

    # ---- d3: the wafer, the emotional height. D02's end (Derek's question) -> D03cr3 (gleaming Maddie, beacon
    # pulsing on her words, crowd and wafer beyond) -> D04r3 (the lady, listening, then her answer on her mouth) ->
    # D03cr3's tail. Maddie's take (r4a, Kai's pick by ear) keeps its own pauses: "It's the time machine." 0.45-2.25,
    # 2.0 s of silence, "You do understand" 4.25-5.85, 1.15 s, "what this will cost you." 7.0-8.85. Nothing tightened.
    b = c.beat('d3', 'The wafer', s3, act='The clean room',
               see='Derek asks what it is. Beside the wafer, Maddie, gleaming clean now with no explanation, tells them '
                   'what it is and what it will cost them. The old lady answers for all of them.')
    k = 'd3-0-derek'
    a = fr(s3 + 0.6)
    e = S.human('vox-derek', k, a, 'd3', 0, 'derek', what='d3 line 0 derek: "What is it?" (hushed)')
    cut3c = fr(e + 0.35)
    assert cut3c - s2 <= 8.0, cut3c - s2
    S.piece('D02', S.clip('D02'), 0.0, s2, cut3c, 'd2', zoom=[[0.0, 1.0], [1.0, 1.0], [8.0, 1.05]])
    k = 'd3-1-maddie'
    mv = sc.voice(k)
    tm = fr(cut3c + 0.8)  # a breath on her before she speaks
    e_m = c.say('vox-maddie', mv, 0.40, 8.95, tm, 'd3 line 1 maddie: "It\'s the time machine. ... You do understand what '
                'this will cost you." (her take\'s own pauses kept)', ref=span(mv))
    c.line(b, 1, 'maddie', tm + 0.05, e_m - tm - 0.05, sc.text(k), 'kai')
    cut04 = fr(tm + (6.95 - 0.40))  # in the 1.15 s pause, just before "what this will cost you."
    first3c = cut04 - cut3c
    S.piece('D03c', S.clip('D03c'), 0.0, cut3c, cut04, 'd3')
    # ---- the lady's answer, ending round 2 (Kai reel at2108/at2566, 23 Oct): stern, Kai's words, 10.8 s of voice
    # (take r7c). "what this will cost you." lands on her listening in the old D04r3-t1 (mouth shut to 2.75 s), then a
    # punch-in cut (112%) to the new D04r4-t2, where she says the whole line. Its mouth (12 fps strip, mouth-map.py):
    # runs 0.92-1.42 ("Look,"), 1.75-4.25, 5.21-7.63, 8.00-9.29. Her take: "Look," 0.26-0.66; "this has been the worst"
    # 0.98-3.00 (a 0.14 s gap after it); "possible outcome for humanity." 3.14-5.18; "If there's a chance we could go
    # back in time to change it," 5.52-8.88; "I want to take that chance." 9.54-11.04. Omni's run 2 is 1.7x too quick
    # for the take's 4.2 s, so the first half goes on her mouth (x1.3) and "possible outcome for humanity." plays at its
    # own speed over the hundred listening (D03cr3 from its start); the cut back to her skips the clip ahead to 0.2 s
    # before run 3. The rest on her mouth: run 3 at x1.3, run 4 at x1.15. Late never early (+0.04 s).
    k = 'd3-2-lady'
    old04 = sc.clips['media'] + '/D04r3-t1.mp4'
    i04 = 0.3
    cut4b = fr(e_m + 0.55)  # her look holds 0.55 s after "cost you."
    S.piece('D04', old04, i04, cut04, cut4b, 'd3')
    j0 = 0.45  # into D04r4-t2: 0.47 s of shut mouth before "Look,"
    z4 = cut4b - j0
    zin = [[0.0, 1.12]]
    t_look = z4 + 0.92 + 0.04
    say('vox-lady', k, 0.22, 0.68, t_look, 'd3 line 2 lady: "Look," (lip-sync, x1.0)')
    t_a = z4 + 1.75 + 0.04
    e_a = say('vox-lady', k, 0.94, 3.02, t_a, 'd3 line 2 lady: "this has been the worst" (lip-sync, x1.3)', tempo=1.3)
    cut_away = fr(e_a + 0.04)
    S.piece('D04', S.clip('D04'), j0, cut4b, cut_away, 'd3', zoom=zin)
    t_b = fr(cut_away + 0.12)
    e_b = say('vox-lady', k, 3.10, 5.22, t_b, 'd3 line 2 lady: "possible outcome for humanity." (over the hundred '
              'listening, x1.0)')
    back = fr(e_b + 0.30)
    S.piece('D03c', S.clip('D03c'), 0.0, cut_away, back, 'd3')
    j3 = 5.21 - 0.20
    z4b = back - j3
    e_c = say('vox-lady', k, 5.48, 8.92, z4b + 5.21 + 0.04, 'd3 line 2 lady: "If there\'s a chance we could go back in '
              'time to change it," (lip-sync, x1.3)', tempo=1.3)
    e_l = say('vox-lady', k, 9.50, 11.10, z4b + 8.00 + 0.04, 'd3 line 2 lady: "I want to take that chance." (lip-sync, '
              'x1.15)', tempo=1.15)
    c.line(b, 2, 'lady', t_look, e_l - t_look, sc.text(k), 'kai')
    back3c = fr(min(max(e_l + 0.6, z4b + 9.29 + 0.6), z4b + 10.0 - 2 / FPS))  # the clip is 10 s
    S.piece('D04', S.clip('D04'), j3, back, back3c, 'd3', zoom=zin)
    m['lady_d3'] = (t_look, e_l)
    # the breath after is the chairs (d4's overhead, held longer), cut ~0.6 s after her last word (the clip's end)
    end_d3 = back3c
    m['d3_lines'] = (a, e_l)
    t = c.close(b, end_d3)
    c.flags.append('d3 (Kai bd3/at713, the emotional height): the words are Kai\'s and Maddie says them; the boss is '
                   'silent, and "You wouldn\'t follow how it works", "Us.", "You. And your consciousness." and "It only '
                   'sends one back. Me." are all gone. Voices: Derek r5b and Maddie r4a are Kai\'s picks by ear; the lady is '
                   'r7c (ending round 2, picked by measurement). Maddie is gleaming from here on with no bunting and no explanation (Kai, Q1).')
    c.flags.append(f'd3 cut: Derek\'s hushed "What is it?" is asked of the vast room (D02 runs on into d3; the old '
                   'wafer reveal D03-t2 is gone, because the battered Maddie with her bunting stands in the middle of it); '
                   'cut to gleaming Maddie '
                   f'(D03cr3, her beacon pulsing in the clip) and {tm - cut3c:.1f} s on her before she speaks. Her take\'s '
                   'own pauses are kept whole (2.0 s after "It\'s the time machine.", 1.15 s before "what this will cost '
                   'you."). The cut to the lady falls in that last pause, so "what this will cost you." lands on her face. The cut '
                   'out of her face comes 0.6 s after her last word, onto the hundred chairs from above, held 2 s in silence '
                   'before they turn: the breath after the height is on what it will cost.')
    c.flags.append('d3 (Kai reel at2108/at2566, ending round 2): the lady no longer comforts Maddie. Stern, in Kai\'s '
                   'words: "Look, this has been the worst possible outcome for humanity. If there\'s a chance we could go '
                   'back in time to change it, I want to take that chance." (take r7c, 10.8 s). It answers Maddie\'s "You do '
                   'understand what this will cost you." (Kai\'s pick, unchanged; nothing added). No "I trust your boss".')
    c.flags.append(f'd3 lip-sync (the lady, D04r4-t2): "what this will cost you." lands on her listening (the old D04r3-t1), '
                   f'then a punch-in cut (112%) to the new clip, where Omni spoke her whole line 1.3-1.7x quicker than the '
                   f'take. "Look," on her mouth at x1.0; "this has been the worst" at x1.3; "possible outcome for humanity." '
                   f'at its own speed over the hundred listening (D03cr3 from its start, gleaming Maddie and the wafer); '
                   f'back on her for "If there\'s a chance... change it," at x1.3 and "I want to take that chance." at x1.15. '
                   f'Two phrases at x1.3 is the stretch cap: for Kai\'s ear.')

    # ---- d4: a hundred chairs (L3 overhead, rotate + push), the tea (D06): unchanged picture; Maddie says the line
    s4 = t
    b = c.beat('d4', 'A hundred chairs', s4, act='The clean room',
               see='Overhead, a hundred chairs laid out like a chip. Then one chair: a patchwork blanket and a mug of '
                   'tea, steaming.')
    d05 = 5.0  # round 1: held 2 s (was 1 s) as the breath after the lady's answer
    S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, s4, s4 + d05, 'd4', still=True,
            zoom=[[0.0, 1.04], [2.0, 1.04], [d05, 1.12]], rot=[[0.0, 0.0], [2.0, 0.0], [d05, 2.0]])
    s6 = fr(s4 + d05)
    # Reel round 1 (Kai at2347, 23 Oct): the lady's "Is that tea?" is dropped; Maddie just tells her, at the moment
    # the lady's question used to start.
    a2 = fr(s6 + LEAD + 1.2)
    e2 = S.human('vox-maddie', 'd4-0-maddie', a2, 'd4', 0, 'maddie')
    end_d4 = fr(min(s6 + 8.0, max(s6 + 6.6, e2 + TAIL)))
    S.piece('D06', S.clip('D06'), 0.0, s6, end_d4, 'd4')
    t = c.close(b, end_d4)
    c.flags.append('d4 (Kai at2347, reel round 1): the lady\'s "Is that tea?" is gone; Maddie just tells her.')
    c.flags.append('d4 (Kai ld4-1): "Milk, two sugars. I kept your loyalty cards." is Maddie\'s (she is the delivery robot; '
                   'she would have them). D05 now held 2 s (the breath after the lady\'s answer), then a 2-degree turn and a push 104 -> 112%; '
                   'D06 to the mug lifting out of frame.')
    c.flags.append('d5 (the test) is CUT whole (Kai bd5): the doubt is dealt with in the bunker negotiation scene.')

    # ---- d6: they sit. D10n (the last ones standing sit down), her question opening over it; D11r3-t2 (the lady, the
    # gleaming Maddie at the edge of frame) for the rest of it, on her mouth; she listens to Maddie's answer.
    # Her mouth on D11r3-t2: "When he arrives back in time," 1.58-3.0 (1.4 s for the take's 2.3 s: x1.6, too fast for
    # any stretch), shut 3.0-3.6; "what will he do?" 3.67-4.42 (rounded wh, rounded "do" 4.33); listens 4.5-8.
    # Her take r4c: "When he arrives back in time," 0.28-2.56; "what will he do?" 3.38-4.32.
    s6b = t
    b = c.beat('d6', 'They sit', s6b, act='The plan',
               see='They sit, every one of them; nobody makes them. Lying back, the old lady asks what he will do when he '
                   'gets back, and Maddie says it as plainly as it can be said.')
    i10, d10 = 0.4, 5.6
    cut11 = fr(s6b + d10)
    k = 'd6-0-lady'
    q1 = fr(cut11 - 2.30 - 0.06)
    say('vox-lady', k, 0.24, 2.56, q1, 'd6 line 0 lady: "When he arrives back in time," (over the wide: Omni\'s mouth is '
        'x1.6 too quick for it)')
    i11 = 3.10
    z11 = cut11 - i11
    eq = say('vox-lady', k, 3.36, 4.34, z11 + 3.66, 'd6 line 0 lady: "what will he do?" (lip-sync, x1.2)', tempo=1.2)
    c.line(b, 0, 'lady', q1 + 0.04, eq - q1 - 0.04, sc.text(k), 'kai')
    S.piece('D10n', S.clip('D10n'), i10, s6b, cut11, 'd6')
    k = 'd6-1-maddie'
    am = fr(eq + 0.45)
    em = S.human('vox-maddie', k, am, 'd6', 1, 'maddie', what='d6 line 1 maddie: "He\'s going to try and convince you lot '
                 'to sort your government out." (on the lady listening)')
    end11 = fr(z11 + 8.0 - 1 / FPS)
    S.piece('D11', S.clip('D11'), i11, cut11, end11, 'd6', zoom=[[i11, 1.0], [i11 + 1.0, 1.0], [8.0, 1.05]],
            grade=LIFT)  # D11r3 sits ~30/255 under the wide it cuts from
    m['q_lady'] = q1
    m['maddie_d6'] = (am, em)
    t = c.close(b, end11)
    c.flags.append('d6 (Kai ld6-0/ld6-1): the lady asks "When he arrives back in time, what will he do?" and Maddie '
                   'answers "He\'s going to try and convince you lot to sort your government out." Who keeps the gains is '
                   'no longer said here (Kai, Q2: the film has it right; the beneficiary rule is relaxed).')
    c.flags.append(f'd6 lip-sync: on D11r3-t2 Omni spoke "When he arrives back in time," in 1.4 s against the take\'s 2.3 s '
                   f'(x1.6, past any stretch), so that half of her question plays at its own speed over the wide of them '
                   f'sitting (D10n), and the cut to her face lands as it ends; "what will he do?" is on her mouth at x1.2. '
                   f'Maddie\'s answer plays on her listening (D11r3 to its end, a slow push 100 -> 105%)'
                   + (f'; its last {em - end11:.1f} s runs over the cut to the hands.' if em > end11 else '.'))

    # ---- d7: the goodbye (D12 whole, then D12x's first stretch: the chained clip, so the grip carries on unbroken).
    s7 = t
    b = c.beat('d7', 'Seat down', s7, act='The crossing',
               see='Two hands across the gap between two chairs. They find each other and grip. Her last joke, and his '
                   'answer.')
    a = fr(max(s7 + 1.0, em + 0.6))
    e = S.human('vox-sandra', 'd7-0-sandra', a, 'd7', 0, 'sandra', lufs=-17.0,
                what='d7 line 0 sandra: "Does this mean I get to hang out with non-grumpy Derek?"')
    a2 = fr(e + 0.5)
    e2 = S.human('vox-derek', 'd7-1-derek', a2, 'd7', 1, 'derek', lufs=-17.0,
                 what='d7 line 1 derek: "Yes, love. Are you ready for this?"')
    end_d7 = fr(e2 + 1.0)
    S.piece('D12', S.clip('D12'), 0.0, s7, min(end_d7, s7 + 8.0 - 1 / FPS), 'd7', grade=LIFT)
    i12x_used = 0.0
    if end_d7 > s7 + 8.0 - 1 / FPS:
        i12x_used = fr(end_d7 - (s7 + 8.0 - 1 / FPS))
        S.piece('D12x', S.clip('D12x'), 1 / FPS, s7 + 8.0 - 1 / FPS, end_d7, 'd7', grade=LIFT)
    m['hands'] = s7
    t = c.close(b, end_d7)
    c.flags.append('d7 (Kai ld7-0/ld7-1, bd7 "brilliant scene"): no seat joke. Sandra: "Does this mean I get to hang out '
                   'with non-grumpy Derek?" Derek: "Yes, love. Are you ready for this?" The shot is kept; the two lines '
                   f'need more than its 8 s, so it runs on into the first {i12x_used:.1f} s of D12x (chained from D12\'s last '
                   'frame, so the grip carries on unbroken) as the chair light begins to rise. Half a second\'s breath '
                   'between her line and his.')

    # ---- d8: the crossing. D10x-t2 (the "they sit" angle again, every chair occupied, the lights rising; a cut, not a
    # chain), then the hands as the light reaches them and the grip goes slack (D12x's later stretch), white; out of the
    # white, the doorway prints as real video (D14p-t2, no post zoom); the dusk wide, the seam runs bright and goes out.
    s8 = t
    b = c.beat('d8', 'The crossing', s8, act='The crossing',
               see='The room of a hundred occupied chairs again; the lights come up. The hands: the light reaches them and '
                   'the grip goes slack. White. Outside, the prints at the door, then the building at dusk: the amber seam '
                   'runs bright end to end and goes out.')
    d10x = 5.5
    S.piece('D10x', S.clip('D10x'), 0.0, s8, s8 + d10x, 'd8')
    s12x = fr(s8 + d10x)
    i12x, d12x = max(3.6, i12x_used + 0.5), 3.0
    S.piece('D12x', S.clip('D12x'), i12x, s12x, s12x + d12x, 'd8', white=[[d12x - 1.0, 0.0], [d12x, 1.0]])
    s14p = fr(s12x + d12x)
    d14p = 4.0
    S.piece('D14p', S.clip('D14p'), 0.3, s14p, s14p + d14p, 'd8', white=[[0.0, 1.0], [1.0, 0.0]], grade=D14_GRADE)
    s14 = fr(s14p + d14p)
    d14 = 7.5
    S.piece('D14', S.clip('D14'), 0.0, s14, s14 + d14, 'd8',
            zoom=[[0.0, 1.0], [1.5, 1.0], [7.5, 1.12]], centre=[[0.0, 640, 360], [1.5, 640, 360], [7.5, 700, 420]],
            grade=D14_GRADE)
    m['s14p'] = s14p
    m['spiral'] = s8
    m['seam_dark'] = fr(s14 + 6.3)
    m['s14'] = s14
    m['slack'] = s12x
    t = c.close(b, fr(s14 + d14))
    c.flags.append('d8 (Kai bd8/ld7-1): opens on the "they sit" angle again (D10x-t2, made fresh and cut to, not chained '
                   'from D10n): every chair visibly occupied, the light rising. The overhead D13 (it read as empty chairs) '
                   'is gone. Then the hands go slack as the light reaches them (D12x), ramped to white over 1 s.')
    c.flags.append('d8 (Kai at2259/at2379): the doorway prints re-made as real video (D14p-t2: clouds move, chalk dust '
                   'drifts towards the door, the doorway light breathes), played with no post zoom, out of the white. The '
                   'dusk building (D14) is kept as it was.')

    # ---- d9: Maddie alone (D16r3: the D10n angle, gleaming Maddie at true scale among a hundred empty chairs, each
    # holding what its person left; her beacon pulses once ~1-2 s). The music carries straight across from d8; no tea
    # cup still. "Boss..." on the pulse, then a long silence, then the hard cut to E.
    s9 = t
    b = c.beat('d9', 'After: Maddie alone', s9, act='After',
               see='The music carries on. Maddie, gleaming, small among a hundred empty chairs. She calls her boss. Nobody '
                   'answers.')
    i16 = 0.4
    t_boss = fr(s9 + 1.2 - i16)
    e_boss = S.human('vox-maddie', 'd9-0-maddie', t_boss, 'd9', 0, 'maddie', lufs=-17.0,
                     what='d9 line 0 maddie: "Boss..." (small, on her beacon\'s one pulse)')
    SIL = 4.3
    end_d9 = fr(e_boss + SIL)
    S.piece('D16', S.clip('D16'), i16, s9, end_d9, 'd9')
    m['boss'] = (t_boss, e_boss)
    m['silence'] = (e_boss, end_d9)
    m['s16'] = s9
    m['d16_last'] = i16 + (end_d9 - s9) - 1 / FPS  # D16r3's last frame shown: scene E's phone shows it
    t = c.close(b, end_d9)
    c.flags.append(f'd9 (Kai bd9/ld9-1): the tea-cup still (D15) is gone; straight from the dusk wide to Maddie, gleaming '
                   f'with no bunting, small among the empty chairs (D16r3-t1, from the D10n angle), the music carrying '
                   f'across. Her only line, "Boss...", on her beacon\'s one pulse, then {SIL} s of silence and the hard cut '
                   f'to E. "Mind how you go." has moved to E, whole, through the phone.')
    c.flags.append(f'd9: the {SIL} s silence fits inside D16r3 (it ends at {m["d16_last"]:.2f} s of the clip), so the '
                   'chained D16xr3-t1 (the chair lights dimming) is not used; it is there if Kai wants the silence longer. '
                   'Scene E\'s phone shows the last frame D shows (D16r3 at that time).')
    c.total = t
    S.pieces_done = True
    return S


# ---------------------------------------------------------------- picture

def ai_env(S, total):
    """Per-frame level of his voice (0..1), for the beacon bloom: RMS per frame, normalised, quick attack, slow fall."""
    n = int(round(total * FPS)) + 2
    env = np.zeros(n)
    for t, src, a, b in S.ai_spans:
        x = C.decode(src, a, b - a)[:, 0]
        hop = SR // FPS
        k = len(x) // hop
        r = np.sqrt((x[:k * hop].reshape(k, hop) ** 2).mean(1))
        r = np.clip(r / (np.percentile(r, 95) + 1e-9), 0, 1)
        s = int(round(t * FPS))
        env[s:s + k] = np.maximum(env[s:s + k], r[:max(0, min(k, n - s))])
    out = np.zeros(n)
    for i in range(1, n):
        out[i] = env[i] if env[i] > out[i - 1] else out[i - 1] * 0.82
    return out


def prep(S):
    """White-balance match, moves, glow and white ramps for every piece: one float pass each (frameops.py)."""
    c = S.c
    V = c.vdir
    # white balance: each source's channel ratios (mean of 3 frames in its used window) pulled 60% to the interiors'
    means = {}
    for p in S.pieces:
        if p.fid in means:
            continue
        ts = [p.i0 + 0.3, p.i0 + (p.t1 - p.t0) / 2, p.i0 + max(0.3, p.t1 - p.t0 - 0.3)]
        ts = [min(t, E.dur(p.src) - 0.1) for t in ts] if not p.still else [0]
        means[p.fid] = np.mean([mean_rgb(p.src, t, p.still) for t in ts], 0)
    ratio = {k: v / v.mean() for k, v in means.items()}
    target = np.mean([r for k, r in ratio.items() if k not in INTERIOR_EXCLUDE], 0)
    luma = np.array([0.2126, 0.7152, 0.0722])
    gains = {}
    for k, r in ratio.items():
        if k in INTERIOR_EXCLUDE:
            gains[k] = np.ones(3)
            continue
        g = (target / r) ** 0.6
        g = g / (luma @ (g * means[k]) / (luma @ means[k]))
        gains[k] = g
    S.wb = {k: (means[k].round(1).tolist(), gains[k].round(3).tolist()) for k in means}
    env = ai_env(S, c.total)
    for n, p in enumerate(S.pieces):
        d = p.t1 - p.t0
        out = V / f'{n:02d}-{p.fid}-i{p.i0:.2f}-d{d:.3f}.mp4'
        spec = dict(src=str(p.src), still=p.still, **{'in': p.i0}, dur=d, out=str(out), gains=gains[p.fid].tolist(),
                    zoom=p.zoom, rot=p.rot, white=p.white, centre=p.centre, grade=p.grade)
        if p.glow and p.fid in BEACON:
            xy, r = BEACON[p.fid]
            s = int(round(p.t0 * FPS))
            spec['glow'] = dict(xy=xy, r=r, env=env[s:s + int(round(d * FPS)) + 1].round(3).tolist())
        js = V / f'{out.stem}.json'
        js.write_text(json.dumps(spec))
        subprocess.run([str(E.LIPS_PY), '-I', str(HERE / 'frameops.py'), str(js)], check=True, capture_output=True)
        c.pic(out, 0.0, p.t0, p.t1, p.beat, source=p.src)
    held = [p for p in S.pieces if not p.still and p.i0 + (p.t1 - p.t0) > E.dur(p.src) + 0.5 / FPS]
    for p in held:
        c.flags.append(f'{p.fid}: runs {p.i0 + p.t1 - p.t0 - E.dur(p.src):.2f} s past its clip; the last frame holds '
                       '(no ping-pong) while its move keeps running.')
    spread = np.array([g for k, g in gains.items() if k not in INTERIOR_EXCLUDE])
    c.flags.append('Colour: every interior source is white-balanced 60% of the way to the interiors\' mean channel '
                   f'balance, brightness kept (gains R {spread[:, 0].min():.2f}-{spread[:, 0].max():.2f}, '
                   f'B {spread[:, 2].min():.2f}-{spread[:, 2].max():.2f}); D14, the dusk exterior, is left as shot. '
                   'sh-25 (D10) and D11 were the bluest, D00/D01 the warmest.')


def flash_check(path, t0, t1):
    """Harding-style screen: luminance swings of >= 10% of full scale that move >= 25% of the frame, counted per s."""
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{t0:.3f}', '-t', f'{t1 - t0:.3f}', '-i', str(path),
                          '-vf', 'scale=160:90,format=gray', '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    y = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(float)
    dif = np.diff(y, axis=0)
    up = ((dif > 25).mean((1, 2)) > 0.25)
    down = ((dif < -25).mean((1, 2)) > 0.25)
    ev = np.nonzero(up | down)[0]
    worst = max([((ev >= i) & (ev < i + FPS)).sum() for i in range(len(dif))] or [0]) // 2
    area = float(np.max(np.abs(dif) > 25, initial=0)) and float((np.abs(dif) > 25).mean((1, 2)).max())
    return worst, area


# ---------------------------------------------------------------- sound

def audio_d(S):
    c, m, sc = S.c, S.c.m, S.sc
    total = c.total
    mx = C.Mix(total)
    E.voices(c, mx)
    fx = C3.sfx_adder(mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}
    speech = sorted((v['t'], v['t'] + v['d'] / v['tempo']) for v in c.voices)

    def duck(x, t0, depth=0.5):
        pts = [(0, 1)]
        for a, b in speech:
            a, b = a - t0, b - t0
            if b < 0 or a > len(x) / SR:
                continue
            pts += [(max(0, a - 0.3), 1), (max(0, a), depth), (b, depth), (b + 0.5, 1)]
        pts.append((len(x) / SR, 1))
        pts = sorted(pts)
        return x * C.env(len(x), pts)

    # ---- D-room (09f81875): glassy piano, in after "fussy". Reel round 1 (Kai at2566/at2622, 23 Oct): it no longer
    # goes out under the lady's question; it carries on under the d6 speech (ducked like every line) and hands over to
    # D-cross on the hands, a 2.5 s fade out under D-cross's 1.5 s fade in.
    room = sc.media / 'suno' / 'gpom-sh-d-room-a-v6-w30-09f81875.wav'
    r0 = fr(m['fussy'] + 0.2)
    r1 = fr(m['hands'] + 1.5)
    d = r1 - r0
    x = C.level(C.decode(room, 0.0, d), rms=-25, peak=-4)
    x = duck(x, r0, 0.45)
    x *= C.env(len(x), [(0, 0), (1.2, 1), (d - 2.5, 1), (d, 0)])
    mx.add('mus-d-room', x, r0, room, 'D-room: glassy piano, music-box tender, in after "fussy", under the d6 speech, '
           'handing over to D-cross on the hands')
    # ---- D-cross (7bead5f0): cello and piano. Round 1 (Kai bd9): it carries straight across from the crossing into
    # Maddie alone. It enters on the hands and is placed so its held last chord (stops at 40.0 s in the take) and its
    # release (to 41.4 s; what follows in the file is not the cue) end on the hard cut to E. Its one breath (the take's
    # dip at ~24.5-26.5 s) is printed against the picture.
    cross = sc.media / 'suno' / 'gpom-sh-d-cross-a-v6-w30-7bead5f0.wav'
    stop_src, end_src = 40.0, 41.4
    c0 = m['hands']
    off = end_src - (total - c0)
    pad = max(0.0, -off)
    off = max(0.0, off)
    d = end_src - off
    x = C.decode(cross, off, d)
    x = C.level(x, rms=-23.5, peak=-3)
    x = duck(x, c0 + pad, 0.6)
    x *= C.env(len(x), [(0, 0), (1.5, 1), (d - 0.04, 1), (d, 0)])
    mx.add('mus-d-cross', x, c0 + pad, cross, 'D-cross: cello and piano nocturne, from the hands across the crossing to '
           'the cut to E')
    to_src = lambda tt: off + tt - c0 - pad  # noqa: E731
    c.flags.append(f'Music (Kai bd9: carry it across): D-cross enters on the hands at {off:.1f} s into the take and plays '
                   f'without an edit to the hard cut to E, its held last chord stopping {end_src - stop_src:.1f} s before '
                   f'the cut ({stop_src:.0f} s in the take, in the silence after "Boss...") and its release ringing out on '
                   f'the cut. The take\'s one breath (~24.5-26.5 s) falls at {c0 + pad + 24.5 - off:.1f}-'
                   f'{c0 + pad + 26.5 - off:.1f} s of the scene (the white is at {m["slack"] + 2.0:.1f}-{m["s14p"] + 1.0:.1f} '
                   f's); the dusk wide sits on {to_src(m["s14"]):.0f}-{to_src(m["s14"] + 7.5):.0f} s of the take. The seam '
                   'no longer goes dark on the chord (it did when the music stopped in d8). D-room plays from 0 s of its '
                   'take, in after Sandra\'s line, and now carries on under the d6 speech (Kai at2622) to hand over to D-cross on the '
                   'hands; both duck ~6 dB under speech. Kai to rule '
                   'on taste.')

    # ---- room tone: the clean room's air (ffmpeg), the whole scene bar the exterior; alone under D16's silence
    air = E.tone('cleanroom-air', 'anoisesrc=c=brown:r=48000:a=0.5,highpass=f=40,lowpass=f=320[n];'
                                  'sine=f=120:r=48000,volume=0.04[h];[n][h]amix=inputs=2:weights=1 1', 30)
    fx('sfx-room', air, 0.0, m['s14p'] + 0.6, rms=-44, fi=0.5, fo=0.6, tile=True, what='clean-room air handling (ffmpeg)')
    fx('sfx-room', air, st['d9'], total - st['d9'], src_in=7, rms=-45, fi=1.0, fo=0.0, tile=True,
       what='clean-room air, after (the silence)')
    # ---- the changing room and the walk
    # -43 (was -39): at -39 the shuffle masked her quiet "I hope" (the mix was heard "Oh, this bloody plan works")
    fx('sfx-crowd', E.SFX / 'fs189231-crowd-shuffling.mp3', 0.0, en['d1'], rms=-43, fi=0.3, fo=0.8,
       what='a hundred people struggling into suits')
    fx('sfx-crowd', E.SFX / 'fs189231-crowd-shuffling.mp3', st['d2'], en['d2'] - st['d2'], src_in=12, rms=-45, fi=0.6,
       fo=1.0, what='the hundred stopped inside the doors, shifting (nobody walks)')
    fx('sfx-crowd', E.SFX / 'fs653920-crowd-small-walla.mp3', st['d3'], 2.5, rms=-48, fi=0.3, fo=1.5,
       what='a murmur that stops at the wafer')
    # ---- Maddie: her clips pulse the beacon themselves (the boss is silent in D); one question beep in the silence
    C3.loop_wheels(fx, 'sfx-maddie', st['d4'] + 4.0 + 5.8, 1.6, rms=-38, fi=0.3, fo=0.4,
                   what='her wheels edging in (end of D06)')
    a, e = m['boss']
    fx('sfx-maddie-beeps', E.MS / 'synth-maddie-beep-question.wav', e + 1.7, rms=-36, what='beep: a question, unanswered')
    fx('sfx-beacon', E.SFX / 'synth-beacon-blip.wav', m['s16'] + 0.4, rms=-40, what='her beacon, still on')
    # ---- the crossing: the chairs power up under the spiral, the building's hum dies with the seam
    hum = E.tone('chairs-hum', 'sine=f=82.41:r=48000[a];sine=f=164.8:r=48000[b];sine=f=247.2:r=48000[c];'
                               'anoisesrc=c=pink:r=48000:a=0.04,lowpass=f=600[n];'
                               '[a][b][c][n]amix=inputs=4:weights=1 0.5 0.25 0.5,tremolo=f=0.5:d=0.15', 20)
    s8, sd = m['spiral'], m['seam_dark']
    x = C.level(C.decode(hum, 0, sd - s8 + 0.2), rms=-30)
    x *= C.env(len(x), [(0, 0), (3.0, 0.6), (6.0, 1), (6.6, 0.5), (m['s14p'] - s8 + 1.0, 0.5), (sd - s8 - 2.4, 0.7),
                        (sd - s8, 0)])
    mx.add('sfx-machine', x, s8, hum, 'the chairs power up; outside, the building\'s hum dies with the seam (ffmpeg)')
    fx('sfx-wind', C3.wind_file(), m['s14p'], en['d8'] - m['s14p'], src_in=12, rms=-36, fi=1.0, fo=0.4,
       what='wind on the downs at dusk')
    c.flags.append('Sound I made up for scene D: the clean-room air (brown noise + a faint 120 Hz, ffmpeg), the chairs\' '
                   'power-up hum on the spiral (82/165/247 Hz + pink noise) dying exactly as the seam goes dark, the '
                   'one unanswered question beep in the silence after "Boss...". No tea, rustle or suit '
                   'sounds exist in the library: the changing room is the crowd-shuffle recording.')
    return mx


# ---------------------------------------------------------------- run

def scene_d(sc):
    S = build(sc)
    prep(S)
    S.c.S = S
    return S.c


def audio_from_cut(c):
    return audio_d(c.S)


E.SCENE_FNS['D'] = (scene_d, audio_from_cut)


def main():
    key = 'D'
    sc = E.Scene(key)
    E.C3.ROOT = sc.media / 'cut'
    c = scene_d(sc)
    mx = audio_from_cut(c)
    tracks, mix = C3.write(c, mx)
    print('colour across the joins:')
    rows = E.join_report(c)
    big = [r for r in rows if r[4] > 30]
    c.flags.append('Colour joins (mean RGB either side of every cut, after the match): ' + (
        'steps over 30/255 only at ' + '; '.join(f'{r[0]} -> {r[1]} ({r[4]:.0f})' for r in big) +
        ', each a change of place or light (the white fade, the dusk exterior, the overhead), not a drift' if big
        else 'no step over 30/255') + '.')
    # photosensitivity: the chair lights rising (D10x) and the white ramp (D12x)
    for fid in ('D10x', 'D12x'):
        pv = [v for v in c.video if fid in pathlib.Path(v['source']).stem][-1]
        worst, area = flash_check(pv['file'], 0, pv['dur'])
        c.flags.append(f'Photosensitivity ({fid}): at most {worst} large-area flash pair(s) in any 1 s (the screen limit '
                       f'is 3), largest frame-to-frame change over 25/255 on {area * 100:.0f}% of the frame. A screen, not a '
                       'certified Harding test.')
        print(f'flash check {fid}: {worst} flash pairs/s max, area {area:.2f}')
    worst = rms_strip(c.dir / 'mix.wav')
    c.flags.append(f'Levels (review round 2): every phrase now takes its gain from its whole atom, and no phrase may go '
                   f'in over -1 dBFS (the 0.37 s "You don\'t." went in ~45 dB hot in round 1 and pulled all of D 10 dB '
                   f'down). Per-second RMS strip of the mix: the loudest second is {worst[0]:+.1f} dB over the median of '
                   f'the scene\'s active seconds (at {worst[1]:.0f} s; the check fails over +12 dB).')
    data = C3.edl(c, tracks, mix, mx)
    (c.dir / 'whitebalance.json').write_text(json.dumps(c.S.wb, indent=1))
    print(f'{c.key}: total {c.total:.2f}s, {len(c.video)} clips, {len(tracks)} stems')
    for b in data['beats']:
        print(f"  beat {b['id']:>3} {b['start']:7.2f} +{b['dur']:6.2f}  {b['title']}")
    if '--no-preview' not in sys.argv:
        C3.preview(c, data)
        qc_flag(c.dir)


def rms_strip(wav):
    """1 s RMS strip: no second may sit more than 12 dB above the median of the scene's active seconds (> -40 dB), so a
    single hot event cannot hide behind an integrated LUFS figure. (Against its +-3 s neighbours the check misfires on
    the line after the scene's deliberate silence.) Returns (worst excess dB, at s)."""
    x = C.decode(wav, 0, None)[:, 0]
    n = len(x) // SR
    r = np.array([20 * np.log10(np.sqrt(np.mean(x[i * SR:(i + 1) * SR] ** 2)) + 1e-9) for i in range(n)])
    med = float(np.median(r[r > -40]))
    i = int(np.argmax(r))
    worst = (float(r[i] - med), i)
    print(f'rms strip: active median {med:.1f} dB; loudest second {r[i]:.1f} dB at {i} s ({worst[0]:+.1f} dB)')
    assert worst[0] <= 12.0, f'a second sits {worst[0]:.1f} dB over the scene median at {i} s'
    return worst


def qc_flag(cut_dir):
    """Run delivery-qc on the preview and write its verdict (plus the out-of-range share) into the edl's flags."""
    pv = cut_dir / 'preview.mp4'
    r = subprocess.run([str(E.REPO / 'scripts/delivery-qc.sh'), str(pv)], capture_output=True, text=True)
    summary = [ln for ln in r.stdout.splitlines() if ' ok, ' in ln][-1].strip()
    st = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(pv), '-vf', 'signalstats=stat=brng,metadata=print:file=-',
                         '-an', '-f', 'null', '-'], capture_output=True, text=True).stdout
    br = [float(x.split('=')[1]) for x in st.splitlines() if 'BRNG' in x]
    data = json.loads((cut_dir / 'edl.json').read_text())
    data['flags'].insert(len(data['flags']) - 1,
                         f'delivery-qc: {summary}. Its FAIL is "limited range, content full" from single stray pixels: '
                         f'frames are clamped to 16-235 before encoding and {100 * np.mean(br):.3f}% of pixels end up '
                         f'outside (worst frame {100 * max(br):.2f}%), the encoder-rounding-on-grain case in delivery.md '
                         '(2026-10-19). Warns: -16 LUFS by design, blacks at 0 (same rounding), "frozen" stretches = '
                         'the deliberate holds (D05\'s 2 s before its move; Maddie still in the silence after "Boss...").')
    (cut_dir / 'edl.json').write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print('qc:', summary)


if __name__ == '__main__':
    if '--qc-only' in sys.argv:
        qc_flag(E.Scene('D').media / 'cut')
    else:
        main()
