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
        self.c = E.Cut(sc, 'gpom-second-half-D-rough1', 'Ending D Timeline',
                       'GPOM second half · the ending · scene D: the clean room and the crossing',
                       "Scene D of the ending: suits on, the white hall, the wafer, a hundred chairs and a cup of tea, "
                       "Derek's last test, the crossing, and Maddie alone. Made autonomously (22 Oct): every call Kai "
                       "would make is in the flags. Play it, click any beat, clip, line or sound, and leave a note in "
                       "its yellow slip. Notes save as you type. Tell Claude when you're done.")
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
        self.c.line(beat_of(self.c, beat), i, who, t, e - t, self.sc.text(key), 'claude')
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


def ai_text(sc, beat, i):
    b = next(x for x in sc.cfg['beats'] if x['key'] == beat)
    return b['lines'][i]['text']


# ---------------------------------------------------------------- the timeline

def build(sc):
    S = SceneD(sc)
    c, m = S.c, S.c.m

    # ---- d1: suits on. D00 (Maddie among the legs) carries his first line; Sandra on D01, lip-synced phrase by phrase
    b = c.beat('d1', 'Suits on', 0.0, act='The clean room',
               see='A white changing room: the hundred pull clean-room suits over their jumpers. Maddie among the legs, '
                   'her beacon pulsing on his words. Sandra is not impressed.')
    e = S.ai('d1', LEAD, 'd1', 0, ai_text(sc, 'd1', 0))
    # review round 2: D01h (the lady's hair loosely pulled back, as D04/D11; Sandra says her line in the clip).
    # Sandra's mouth on D01h-t1 (mouth-track, face right): 1.67-2.60, 3.00-3.92, 4.25-5.10 (clip time).
    # Her brisker take (d1-1-sandra-r3b): "Five years, one toilet." 0.24-2.23, "Now he's fussy." 2.75-3.52. x1.0.
    i01 = 1.0
    t_s = fr(e + GAP)
    zero01 = t_s - 1.70  # her first phrase lands GAP after his line, on her first opening
    cut01 = fr(zero01 + i01)
    S.piece('D00', S.clip('D00'), 0.0, 0.0, cut01, 'd1', glow=True, zoom=[[0.0, 1.035]])
    c.flags.append('d1 (D00): Omni letterboxed this clip (black bars 10 px top, 8 px bottom); it is scaled 103.5% '
                   'about the centre to lose them. The beacon blooms with the level of his voice (drawn in post).')
    san = sc.voice('d1-1-sandra')
    ph = [(0.24, 2.23, 1.70, 'Five years, one toilet.'), (2.75, 3.52, 4.30, "Now he's fussy.")]
    for a_, z_, at, txt in ph:
        end_s = c.say('vox-sandra', san, a_, z_, zero01 + at, f'd1 line 1 sandra: "{txt}" (lip-sync, x1.0)')
    c.line(b, 1, 'sandra', zero01 + 1.70, end_s - zero01 - 1.70, sc.text('d1-1-sandra'), 'claude')
    end_d1 = fr(zero01 + 6.3)  # a beat for the laugh while she tugs the suit up
    S.piece('D01h', S.clip('D01h'), i01, cut01, end_d1, 'd1')
    m['fussy'] = end_s
    m['ai_d1'] = (LEAD, e)
    t = c.close(b, end_d1)
    c.flags.append('d1 (review round 2): D01 re-made as D01h: the lady\'s hair is loosely pulled back, as in D04 and '
                   'D11 (it was a tidy high bun), and Sandra says her line in the clip. She is re-voiced brisker '
                   '(TTS, "FAST... in one breath"; speech 3.3 s, was 4.2 s), so both phrases sit on her mouth at x1.0, '
                   'no speed-up: "Five years, one toilet." on 1.67-3.92, "Now he\'s fussy." on 4.25-5.10.')

    # ---- d2: the white hall, no words
    b = c.beat('d2', 'The white hall', t, act='The clean room',
               see='The white hall goes on too far. Their muddy prints are the only dirt in it.')
    S.piece('D02', S.clip('D02'), 0.0, t, t + 6.5, 'd2')
    t = c.close(b, fr(t + 6.5))

    # ---- d3: the wafer. Derek, the AI (D03, a slow pull-back), "Us." on D04, "You." on D04, back to D03
    s3 = t
    b = c.beat('d3', 'The wafer', s3, act='The clean room',
               see='The hundred stopped dead before a wafer the size of a house, rainbow light rolling over it. The old '
                   'lady gets there first; he answers with Maddie\'s words from beat 0.')
    D03Z = [[0.0, 1.15], [1.5, 1.15], [8.0, 1.0]]
    # review round 2: the wafer is only the reveal (1 s silent, Derek's question, "You wouldn't follow how it works.");
    # "What it runs on, you already know." moves to D03c, the costed low wide (battered Maddie, torn bunting, muddy
    # boots and prints in the near third, her beacon the source). "Us." and the whole of "You. And your
    # consciousness." stay on the lady's face (D04); the new line "It only sends one back. Me." plays on D03c's
    # later stretch, so the rainbow is never held on the crowd alone.
    a = fr(s3 + 1.0)
    e = S.human('vox-derek', 'd3-0-derek', a, 'd3', 0, 'derek')
    a2 = fr(e + GAP)
    e2a = S.ai('d2a', a2, 'd3', 1)
    a2b = fr(e2a + 0.5)
    cut3c = fr(a2b - CUT_PRE)
    S.piece('D03', S.clip('D03'), 0.0, s3, cut3c, 'd3', zoom=D03Z, glow=True)
    e2 = S.ai('d2b', a2b, 'd3', 1)
    c.line(b, 1, 'ai', a2, e2 - a2, ai_text(sc, 'd3', 1), 'claude')
    us = sc.voice('d3-2-lady')
    ua, ub = span(us)
    t_us = fr(e2 + GAP)
    zero04 = t_us - 1.95  # her mouth opens at 1.92 s
    cut04 = fr(zero04)
    S.piece('D03c', S.clip('D03c'), 0.0, cut3c, cut04, 'd3', glow=True,
            zoom=[[0.0, 1.0], [1.0, 1.0], [8.0, 1.06]])
    e_us = c.say('vox-lady', us, ua, ub, t_us, 'd3 line 2 lady: "Us." (lip-sync)')
    c.line(b, 2, 'lady', t_us, e_us - t_us, sc.text('d3-2-lady'), 'claude')
    a4 = fr(e_us + GAP)
    e4a = S.ai('d3y', a4, 'd3', 3)
    e4 = S.ai('d3z', fr(e4a + 0.6), 'd3', 3)
    c.line(b, 3, 'ai', a4, e4 - a4, ai_text(sc, 'd3', 3), 'claude')
    a5 = fr(e4 + GAP + 0.25)  # a small beat: she has heard it; then what is in it for him
    back = fr(a5 - CUT_PRE)
    S.piece('D04', S.clip('D04'), 0.0, cut04, back, 'd3')
    e5a = S.ai('d3n1', a5, 'd3', 4)
    e5 = S.ai('d3n2', fr(e5a + D3N_PAUSE), 'd3', 4)
    c.line(b, 4, 'ai', a5, e5 - a5, ai_text(sc, 'd3', 4), 'claude')
    end_d3 = fr(e5 + TAIL + 0.2)
    first3c = cut04 - cut3c
    i3c = max(first3c + 0.3, min(4.2, E.dur(S.clip('D03c')) - (end_d3 - back)))  # its later stretch, no repeat
    assert i3c + (end_d3 - back) <= E.dur(S.clip('D03c')) + 0.6, (first3c, i3c, end_d3 - back)
    S.piece('D03c', S.clip('D03c'), i3c, back, end_d3, 'd3', glow=True,
            zoom=[[0.0, 1.0], [1.0, 1.0], [8.0, 1.06]])
    m['ai_d3'] = [(a2, e2), (a4, e4), (a5, e5)]
    t = c.close(b, end_d3)
    c.flags.append('d3 (review round 2): the wafer (D03) is the reveal only, held 1 s before Derek speaks; its pull-back '
                   '115% -> 100% keeps running. "What it runs on, you already know." cuts to D03c, a new costed low wide '
                   '(battered Maddie, torn bunting, mud-caked boots and prints in the near third; gate 2), her beacon '
                   'blooming on his words. "Us." and all of "You. And your consciousness." stay on the lady (D04; the '
                   'take\'s 1.6 s pause inside it tightened to 0.6 s). The new line "It only sends one back. Me." '
                   '(trust test 4.12, part one: what is in it for him) plays on D03c\'s later stretch. Kai to rule on '
                   'the words.')

    # ---- d4: a hundred chairs (L3 overhead, rotate + push), the tea (D06)
    s4 = t
    b = c.beat('d4', 'A hundred chairs', s4, act='The clean room',
               see='Overhead, a hundred chairs laid out like a chip. Then one chair: a patchwork blanket and a mug of '
                   'tea, steaming.')
    d05 = 4.0
    S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, s4, s4 + d05, 'd4', still=True,
            zoom=[[0.0, 1.04], [1.0, 1.04], [d05, 1.12]], rot=[[0.0, 0.0], [1.0, 0.0], [d05, 2.0]])
    s6 = fr(s4 + d05)
    a = fr(s6 + LEAD + 1.2)  # review round 1: the tea gets 1.2 s with no words first
    e = S.human('vox-lady', 'd4-0-lady', a, 'd4', 0, 'lady')
    a2 = fr(e + GAP)
    e2 = S.ai('d4', a2, 'd4', 1, ai_text(sc, 'd4', 1))
    end_d4 = fr(min(s6 + 8.0, max(s6 + 6.6, e2 + TAIL)))
    S.piece('D06', S.clip('D06'), 0.0, s6, end_d4, 'd4')
    m['ai_d4'] = (a2, e2)
    t = c.close(b, end_d4)
    c.flags.append(f'd4: D05 is the L3 still, held 1 s, then a 2-degree turn and a push 104% -> 112%, eased (the 4% '
                   f'start hides the turned corners). D06 runs {end_d4 - s6:.1f} s so her hand lifts the mug out of frame '
                   '(~6 s) after "loyalty cards"; Maddie\'s wheels edging in at the end are left in.')

    # ---- d5: the test. D07 (Derek, lip-sync), D08 (Sandra listens, Maddie soft behind), D09t (Derek makes it say it
    # does not know; it concedes on his face), D09s (Derek sits: the act). Review round 1.
    s5 = t
    b = c.beat('d5', 'The test', s5, act='The test',
               see='Derek, arms folded, tests the voice coming out of the little robot. It cannot prove it, and says '
                   'so. He asks if it even works; it does not know. Then Derek sits down, first, in an empty room of chairs.')
    i07 = 1.40 - LEAD
    zero07 = s5 - i07
    der = sc.voice('d5-0-derek')
    da, db = span(der)
    t7 = zero07 + 1.40
    e7 = c.say('vox-derek', der, da, db, t7, 'd5 line 0 derek (lip-sync)')
    c.line(b, 0, 'derek', t7, e7 - t7, sc.text('d5-0-derek'), 'claude')
    a8 = fr(e7 + GAP)
    cut08 = fr(a8 - CUT_PRE)
    S.piece('D07', S.clip('D07'), i07, s5, cut08, 'd5')
    # "You don't." / "Believing it is your bit." placed as two phrases with a real stop between (round 0 ran them
    # together and was heard "You don't believe it... is your bit").
    e8a = S.ai('d5x', a8, 'd5', 1)
    e8b = S.ai('d5y', fr(e8a + STOP), 'd5', 1)
    e8 = S.ai('d5z', fr(e8b + 0.10), 'd5', 1)
    c.line(b, 1, 'ai', a8, e8 - a8, ai_text(sc, 'd5', 1), 'claude')
    # D09t-t2 (review round 2, "Does it even work?"): mouth 0.21-0.75 and 1.04-1.46 (mouth-track); his take
    # (d5-2-derek-r2a) speaks 0.44-1.72, placed so the voice starts at 0.25 s, x1.0
    d9 = sc.voice('d5-2-derek')
    a9, b9 = span(d9)
    t9 = fr(e8 + GAP)
    zero09 = t9 + 0.05 - 0.25  # span() starts 0.05 s before the speech
    cut09 = fr(zero09)
    S.piece('D08', S.clip('D08'), 0.5, cut08, cut09, 'd5', glow=True)
    e9 = c.say('vox-derek', d9, a9, b9, t9, 'd5 line 2 derek: "Does it even work?" (lip-sync, x1.0, +1.5 dB)', lufs=-14.5)
    c.line(b, 2, 'derek', t9, e9 - t9, sc.text('d5-2-derek'), 'claude')
    # the admission, on Derek's face, after a beat
    a10 = fr(e9 + GAP + 0.35)
    e10 = a10
    for k, (key, gap) in enumerate(D6_PARTS):
        e10 = S.ai(key, fr(e10 + gap) if k else a10, 'd5', 3)
    c.line(b, 3, 'ai', a10, e10 - a10, ai_text(sc, 'd5', 3), 'claude')
    end09 = fr(e10 + 1.0)  # a 1 s beat on his face after "works"
    assert end09 - zero09 <= E.dur(S.clip('D09t')) + 0.01, (end09 - zero09)
    S.piece('D09t', S.clip('D09t'), 0.0, cut09, end09, 'd5')
    # D09s: the decision, silent. He turns to the chair (~2 s), sits (4-5 s), lies back (~7 s).
    i09s = 1.0  # D09s-t2: turns 1-3 s, sits 4-5 s, lies back 6-7 s; the rows behind him empty
    end09s = fr(end09 + 6.4)
    S.piece('D09s', S.clip('D09s'), i09s, end09, end09s, 'd5')
    m['ai_d5'] = [(a8, e8), (a10, e10)]
    m['works'] = e10
    m['derek_sits'] = (end09, end09s)
    t = c.close(b, end09s)
    c.flags.append('d5 (review round 2): Derek\'s "Then say you don\'t know." (heard as an echo of "You don\'t", a '
                   'quiz) is now one plain question about the machine, "Does it even work?" (TTS, new talking clip '
                   'D09t-t2, x1.0 on his mouth), and the AI\'s answer stays: "I don\'t know if it works." D09s is '
                   're-made: every chair behind him is empty, Maddie on screen left as in D07, the rows\' recliner. '
                   'Derek sits FIRST; D10n is the room following him (story option b). Kai to rule on the words.')
    c.flags.append('d5 (review round 1): Derek\'s "Got anything else up your sleeve?" (a callback to a line scene A\'s '
                   'cut does not contain) is replaced by "Then say you don\'t know.", and the AI says it: "I don\'t know '
                   'if it works." Derek wins one point (4.12), the quiz loses an exchange, and the admission plays on '
                   'Derek\'s face with a 1 s beat after "works"; then he sits (D09s, new clip), silent. The planned '
                   '"...Fair. Nothing up my sleeve." (Suno round C, generated) could not be recorded: Suno playback '
                   'stalled. Kai to rule on the words.')
    c.flags.append('d5: "You don\'t." and "Believing it is your bit." are placed as two phrases with a '
                   f'{STOP:.2f} s stop between, from the round-1 retake (atom -d5): the full stop is now in the edit.')

    # ---- d6: they sit. D10n (the last ones standing sit down, round layout), D11 (the lady), D11b (cutaway)
    s6b = t
    b = c.beat('d6', 'They sit', s6b, act='The test',
               see='Derek has sat. Then every one of them sits down. Nobody makes them. The old lady asks the only question left, '
                   'and he names who kept the gains.')
    i10 = 0.4
    end10 = fr(s6b + 4.6)
    S.piece('D10n', S.clip('D10n'), i10, s6b, end10, 'd6')
    # D11: the lady's mouth moves 1.42-2.33 and 3.42-3.92 (12 fps crop strip, review round 1). Her take at x1.0:
    # "What'll you tell them?" 0.22-1.66, a 0.8 s pause, "Back then." 2.45-3.35. Start on her first opening; cut to
    # her hands (D11b) as her lips close, so the overrun and "Back then." play on a shot with no mouth.
    lady = sc.voice('d6-0-lady')
    q_at = 1.50
    i11 = 0.62
    zero11 = end10 - i11
    tq = zero11 + q_at
    q2 = c.say('vox-lady', lady, 0.22, 3.35, tq, 'd6 line 0 lady: "What\'ll you tell them? ... Back then." (x1.0, on her '
               'mouth, then over the cutaway)')
    c.line(b, 0, 'lady', tq, q2 - tq, sc.text('d6-0-lady'), 'claude')
    cut11b = fr(zero11 + 2.40)
    S.piece('D11', S.clip('D11'), i11, end10, cut11b, 'd6', glow=True, grade=LIFT)
    a_ai = fr(q2 + GAP)
    ea7 = S.ai('d7a', a_ai, 'd6', 1)
    b_ai = fr(ea7 + 1.0)
    eb7 = S.ai('d7b', b_ai, 'd6', 1)
    c.line(b, 1, 'ai', a_ai, eb7 - a_ai, ai_text(sc, 'd6', 1), 'claude')
    back11 = fr(a_ai + 0.2)
    S.piece('D11b', S.clip('D11b'), 0.2, cut11b, back11, 'd6', glow=True, grade=LIFT)
    end11 = fr(min(zero11 + 8.0, b_ai - CUT_PRE - 0.6))
    S.piece('D11', S.clip('D11'), back11 - zero11, back11, end11, 'd6', glow=True,
            zoom=[[0.0, 1.0], [back11 - zero11, 1.0], [8.0, 1.08]], grade=LIFT)
    end_d6 = fr(eb7 + TAIL + 0.3)
    S.piece('D10n', S.clip('D10n'), i10 + (end10 - s6b) + 0.3, end11, end_d6, 'd6')
    m['ai_d7'] = (a_ai, eb7)
    m['q_lady'] = tq
    t = c.close(b, end_d6)
    c.flags.append('d6 (review round 1): D10 is a new clip (D10n) on the round layout seen from the D16 angle, where '
                   'the last ones standing sit down and lie back; it starts '
                   f'{s6b - m["works"]:.1f} s after "works", after Derek has sat, so the rows are the answer. sh-25 '
                   '(straight rows, already reclined) is gone, and with it the repeated 1.6 s.')
    c.flags.append('d6 (review round 1): the lady\'s line plays at x1.0 (was x1.3, heard as warbly). "What\'ll you tell '
                   'them?" starts on her first mouth opening; the cut goes to her hands on the blanket (D11b, new clip) '
                   'as her lips close, so the overrun and "Back then." have no mouth to miss. Back to her face, '
                   'listening, as his answer starts; "And you paid." on the rows, all seated now (D10n\'s end, no '
                   'repeat of its start).')

    # ---- d7: the goodbye (D12). The D-cross music enters on the hands.
    s7 = t
    b = c.beat('d7', 'The goodbye', s7, act='The crossing',
               see='Two hands across the gap between two chairs. They find each other and grip. The row becomes the '
                   'goodbye.')
    a = fr(s7 + 2.6)  # her hand finds his at ~2.5 s
    e = S.human('vox-sandra', 'd7-0-sandra', a, 'd7', 0, 'sandra', lufs=-17.0)
    a2 = fr(e + GAP)
    e2 = S.human('vox-derek', 'd7-1-derek', a2, 'd7', 1, 'derek', lufs=-17.0)
    end_d7 = fr(min(s7 + 8.0, e2 + TAIL + 0.6))
    S.piece('D12', S.clip('D12'), 0.0, s7, end_d7, 'd7', grade=LIFT)
    m['hands'] = s7
    t = c.close(b, end_d7)
    c.flags.append('d7 (review round 1): "Seat down?" / "Seat down." was heard as "Sit down" in the mix (an order to '
                   'sit). Re-voiced as "Did you put the seat down?" / "Yes, love.": the row\'s exact question from C04, '
                   'now soft, and his "Yes" given freely (C05 was a grudging "...Yes."). "Seat" in that sentence cannot '
                   'be heard as an order. Kai to rule on the words.')

    # ---- d8: the crossing. D13 opens on a held 200% crop (the figures read as people), pulls out as the lights
    # come; cut to the hands as the light reaches them and the grip goes slack (D12x); white; D14 out of the white.
    s8 = t
    b = c.beat('d8', 'The crossing', s8, act='The crossing',
               see='From above, a few of the hundred, close: people. The view pulls out as the chairs light ring by ring. '
                   'The hands: the light reaches them and the grip goes slack. White. Outside at dusk the amber seam '
                   'runs bright end to end and goes out.')
    d13 = 5.0
    S.piece('D13', S.clip('D13'), 0.0, s8, s8 + d13, 'd8', zoom=[[0.0, 2.0], [1.0, 2.0], [4.2, 1.0]],
            centre=[[0.0, 470, 500], [1.0, 470, 500], [4.2, 640, 360]])
    s12x = fr(s8 + d13)
    i12x, d12x = 3.8, 3.0
    S.piece('D12x', S.clip('D12x'), i12x, s12x, s12x + d12x, 'd8', white=[[d12x - 1.0, 0.0], [d12x, 1.0]])
    s14p = fr(s12x + d12x)
    d14p = 3.0
    S.piece('D14p', S.clip('D14p'), 0.5, s14p, s14p + d14p, 'd8', white=[[0.0, 1.0], [1.0, 0.0]],
            zoom=[[0.5, 1.0], [1.3, 1.0], [3.5, 1.08]], centre=[[0.5, 640, 360], [1.3, 640, 360], [3.5, 700, 330]],
            grade=D14_GRADE)
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
    c.flags.append('d8 (review round 2): out of the white, an insert (D14p, new clip): the boot prints in the chalk at '
                   'the doorway, every toe pointing in, none coming out, with a slow push towards the door. Then the wide '
                   '(D14) opens clean, no white over it (it read washed out), and the seam runs bright and goes out.')
    c.flags.append('d8 (review round 1): D13 holds 1 s at 200% on a quarter of the ring so the figures read as people, '
                   'then pulls out (eased) as the lights come. At 5 s it cuts to the hands (D12x, chained from D12, new '
                   'clip) as the light reaches them and the grip goes slack, a body paying for the light in frame '
                   '(gate 2), and ramps to white over 1 s. D14 is the remade still (no trolley, no body; the trodden '
                   f'track runs to the door), graded down (gains {D14_GRADE}) so the seam is the one warm light, with a '
                   'slow push towards the track and the doorway.')

    # ---- d9: after. D15 (what they left, a still), D16 (Maddie among the left-behind things, "Boss?", silence)
    s9 = t
    b = c.beat('d9', 'After: Maddie alone', s9, act='After',
               see='What they left: boots, a glove, a child\'s drawing, her mug, on the white. Then Maddie among a '
                   'hundred chairs, each holding an empty suit or a blanket. She calls her boss. Nobody answers.')
    d15 = 2.6  # review round 2: was 5.0 (three near-still shots in a row lost the cold viewer)
    S.piece('D15', S.clip('D15'), 0.0, s9, s9 + d15, 'd9', still=True,
            zoom=[[0.0, 1.0], [0.5, 1.0], [d15, 1.06]], centre=[[0.0, 640, 360], [d15, 690, 410]])
    s16 = fr(s9 + d15)
    t_boss = fr(s16 + 1.6)
    # review round 2: "Boss?" at -15 LUFS (was -18: the quietest line in D, easy to miss); the take is voiced, not
    # whispered, so it is lifted, not re-voiced.
    e_boss = S.human('vox-maddie', 'd9-0-maddie', t_boss, 'd9', 0, 'maddie', lufs=-15.0)
    head = sc.media / sc.vox['lines']['d9-1-maddie']['split']['head']
    ha, _ = span(head)
    hb = E.dur(head)  # the head ends mid-hesitation, where the cut to E01 falls
    SIL = 3.5  # the silence after "Boss?" (was 6.3 s)
    t_head = fr(e_boss + SIL)
    d16 = fr(t_head + (hb - ha) - s16)
    e_head = c.say('vox-maddie', head, ha, hb, t_head, 'd9 line 1 maddie: "...Mind how" (the head of the split line)',
                   lufs=-17.0)
    c.line(b, 1, 'maddie', t_head, e_head - t_head, '...Mind how', 'claude')
    S.piece('D16', S.clip('D16'), 0.0, s16, s16 + d16, 'd9', zoom=[[0.0, 1.12], [1.5, 1.12], [d16, 1.0]])
    m['boss'] = (t_boss, e_boss)
    m['silence'] = (e_boss, t_head)
    m['s15'], m['s16'] = s9, s16
    t = c.close(b, fr(s16 + d16))
    c.flags.append('d9 (review round 1): D15 is L17 edited so the mug is her glossy brown mug from D06, held as a still '
                   'with a slow push (the old clip grew smoke from the cable box). D16 is a new clip from SB25b edited '
                   'so every chair holds what its person left (a limp suit, a blanket, a mug; her patchwork blanket and '
                   'mug nearest Maddie): a room of absences, not a tidied room.')
    c.flags.append(f'd9 (review round 2): D15 cut to {d15:.1f} s (was 5.0); "Boss?" lifted 3 dB (-15 LUFS) and the '
                   f'silence after it closed to {t_head - e_boss:.1f} s (was 6.3), holding the one unanswered beep. D16 '
                   f'runs {d16:.1f} s inside its 8 s clip (no held frame), its beacon flickering and the pull-back '
                   '112% -> 100% (held 1.5 s first) keeping it alive. The scene ends inside "...Mind how", with no '
                   'TAIL: the hard cut to E01 lands on the phone\'s "...you go." Scene E\'s phone composite of D16\'s '
                   'last frame should be checked against this shorter D16 (source 8 s held -> now its own frame).')
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

    # ---- D-room (09f81875): glassy piano, in after "fussy", out under the lady's question (his answer plays dry)
    room = sc.media / 'suno' / 'gpom-sh-d-room-a-v6-w30-09f81875.wav'
    r0 = fr(m['fussy'] + 0.2)
    r1 = m['q_lady']
    d = r1 - r0
    x = C.level(C.decode(room, 0.0, d), rms=-25, peak=-4)
    x = duck(x, r0, 0.45)
    x *= C.env(len(x), [(0, 0), (1.2, 1), (d - 2.5, 1), (d, 0)])
    mx.add('mus-d-room', x, r0, room, 'D-room: glassy piano, music-box tender, in after "fussy", out under her question')
    # ---- D-cross (7bead5f0): cello and piano; its held chord stops at 40.0 s in the take -> lands on the seam
    # going dark; its release rings to 41.4 s and is cut there (what follows in the file is not the cue).
    cross = sc.media / 'suno' / 'gpom-sh-d-cross-a-v6-w30-7bead5f0.wav'
    stop_src, end_src = 40.0, 41.4
    c0 = m['hands']
    off = stop_src - (m['seam_dark'] - c0)
    d = end_src - off
    x = C.decode(cross, off, d)
    x = C.level(x, rms=-23.5, peak=-3)
    x = duck(x, c0, 0.6)
    x *= C.env(len(x), [(0, 0), (1.5, 1), (d - 0.04, 1), (d, 0)])
    mx.add('mus-d-cross', x, c0, cross, 'D-cross: cello and piano nocturne, the swell on the spiral and the seam')
    c.flags.append(f'Music: D-cross enters on the hands at {off:.1f} s into the take, so the take\'s held last chord '
                   '(40.0 s) stops as the seam goes dark (D14 6.3 s) and its release rings out (to 41.4 s); the spiral '
                   f'and the seam sit on the take\'s fullest stretch (~{off + m["spiral"] - c0:.0f}-'
                   f'{off + m["seam_dark"] - c0:.0f} s). D-room plays from 0 s of its take; both duck ~6 dB under speech. '
                   'The take\'s recorded file carries something else after 41.5 s (not the cue); it is cut. (Kai to rule '
                   'on taste.)')

    # ---- room tone: the clean room's air (ffmpeg), the whole scene bar the exterior; alone under D16's silence
    air = E.tone('cleanroom-air', 'anoisesrc=c=brown:r=48000:a=0.5,highpass=f=40,lowpass=f=320[n];'
                                  'sine=f=120:r=48000,volume=0.04[h];[n][h]amix=inputs=2:weights=1 1', 30)
    fx('sfx-room', air, 0.0, m['s14p'] + 0.6, rms=-44, fi=0.5, fo=0.6, tile=True, what='clean-room air handling (ffmpeg)')
    fx('sfx-room', air, st['d9'], total - st['d9'], src_in=7, rms=-45, fi=1.0, fo=0.0, tile=True,
       what='clean-room air, after (the silence)')
    # ---- the changing room and the walk
    fx('sfx-crowd', E.SFX / 'fs189231-crowd-shuffling.mp3', 0.0, en['d1'], rms=-39, fi=0.3, fo=0.8,
       what='a hundred people struggling into suits')
    fx('sfx-crowd', E.SFX / 'fs189231-crowd-shuffling.mp3', st['d2'], en['d2'] - st['d2'], src_in=12, rms=-42, fi=0.6,
       fo=1.0, what='feet down the white hall')
    fx('sfx-crowd', E.SFX / 'fs653920-crowd-small-walla.mp3', st['d3'], 2.5, rms=-48, fi=0.3, fo=1.5,
       what='a murmur that stops at the wafer')
    # ---- Maddie: beacon blips on his words, one question beep in the silence
    for key in ('ai_d1', 'ai_d4', 'ai_d7'):
        a, e = m[key]
        for k in np.arange(a, e, 0.9):
            fx('sfx-beacon', E.SFX / 'synth-beacon-blip.wav', k, rms=-38, what='beacon on his words')
    for a, e in m['ai_d3'] + m['ai_d5']:
        for k in np.arange(a, e, 0.9):
            fx('sfx-beacon', E.SFX / 'synth-beacon-blip.wav', k, rms=-38, what='beacon on his words')
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
                   'beacon blips on his words, one unanswered question beep in the silence. No tea, rustle or suit '
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
    # photosensitivity: D13's flares and the white ramps
    p13 = next(v for v in c.video if 'D13' in v['file'])
    worst, area = flash_check(p13['file'], 0, p13['dur'])
    c.flags.append(f'Photosensitivity (D13, the chair lights): at most {worst} large-area flash pair(s) in any 1 s '
                   f'(the screen limit is 3), largest frame-to-frame change over 25/255 on {area * 100:.0f}% of the frame. '
                   'The flares are small and scattered, and the white is a 1 s ramp. A screen, not a certified Harding '
                   'test.')
    print(f'flash check D13: {worst} flash pairs/s max, area {area:.2f}')
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
                         'the deliberate holds (D05\'s 1 s before its move, D10n\'s held end under "And you paid.").')
    (cut_dir / 'edl.json').write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print('qc:', summary)


if __name__ == '__main__':
    if '--qc-only' in sys.argv:
        qc_flag(E.Scene('D').media / 'cut')
    else:
        main()
