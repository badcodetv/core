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
# --tag r5 (Kai, 4 Nov, D round 5): Maddie's new key line (at469), the lady's answer cut (at567/at715), the d6 question
# and answer cut (at1091/at1178/at1285), the all-seated D10x shot for d6 (at1054/at1615). Writes <media>/cut-r5/.
R14 = E.TAG == 'r14'  # Kai, 9 Nov (timeline r13): Hundred+question one take, Sandra's jeopardy, the vow without 'take a seat', no Thank you, hands quick to white
R13 = E.TAG in ('r13', 'r14')  # Kai, 9 Nov: dialogue 1I (the hundred choose: 'take a seat'), the lady asks 'And afterwards?', 'my love'
R11 = E.TAG in ('r11', 'r13', 'r14')  # Kai at1242 (6 Nov): no Sandra / 'me too', only 'Are you ready for this?'; the music must not change
R9 = E.TAG in ('r9', 'r10', 'r11', 'r13', 'r14')  # r10: Kai at978, the key line re-worded; Kai, 6 Nov, timeline r8 notes: Maddie empathetic (at331/at557), no 'Will it hurt?' (at849), no waffle (at1147/at1275)
R8 = E.TAG in ('r8', 'r9', 'r10', 'r11', 'r13', 'r14')  # Kai, 6 Nov, timeline r7 notes: cut to the chase (at1400), no tea (at1750), cello from 'they sit' (at1849), hands straight to white (at2360)
R7 = E.TAG in ('r7', 'r8', 'r9', 'r10', 'r11', 'r13', 'r14')  # Kai, 6 Nov: dialogue page draft 1F (the wafer: what it costs) + 2D (the goodbye)
R5 = E.TAG in ('r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r13', 'r14')  # r6: the same edit, with the re-made suits (D00r7) and tea (D06r7) shots
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
    if R7:
        # D round 7 (Kai, 6 Nov; dialogue page W1GrGb1W8meMiHaxLkYffj, draft 1F): Maddie tells them what it costs.
        # Picture, all existing clips (mouth reads off 2 fps face strips, 6 Nov): D03c Maddie (her first line) ->
        # D05 the empty chairs from above (Derek counts, off; "It runs on you..."; Sandra's question, off) -> D08 Sandra's
        # face, mouth shut throughout (Maddie's answer lands on her) -> D07-t1 Derek (mouth open ~1.5-3.5 s: "And then?";
        # shut after 4 s: he hears "You don't wake up.") -> D11c6 the lady (silent; her nod on the promise) -> D09t-t2
        # Derek (mouth open ~0.5-1.0 s: "He?"; then listening) -> D09s-t2 Derek walks to his chair and lies back ("Right.").
        e1 = S.human('vox-maddie', k, fr(cut3c + 0.25), 'd3', 1, 'maddie')
        cut05 = fr(e1 + 0.35)
        assert cut05 - cut3c <= 8.0 - 1 / FPS, cut05 - cut3c
        S.piece('D03c', S.clip('D03c'), 0.0, cut3c, cut05, 'd3')
        if R14:  # Kai at542: "Hundred. ... What will it feel like?" as one take, so his voice holds and the pause is his
            e2 = S.human('vox-derek', 'd3-13-derek', fr(cut05 + 0.7), 'd3', 13, 'derek', lufs=-17.0)
        else:
            e2 = S.human('vox-derek', 'd3-2-derek', fr(cut05 + 0.7), 'd3', 2, 'derek', lufs=-18.0)
        if R13:
            # D round 13 (Kai, 9 Nov; timeline r12 at701/at803/at940/at1025, dialogue page round 3 pick 1I). Over the chairs
            # from above (D05): "Hundred." / "What will it feel like?" (Derek, off: his D07 face read as angry, at803) /
            # "It's a bit like dying..." Then the lady's close-up (D11c, her mouth to be redrawn by LatentSync): "And
            # afterwards?"; Maddie's answer and her vow follow (picture below).
            e8 = e2 if R14 else S.human('vox-derek', 'd3-8-derek', fr(e2 + 0.5), 'd3', 8, 'derek', lufs=-17.0)
            e9 = S.human('vox-maddie', 'd3-9-maddie', fr(e8 + 0.5), 'd3', 9, 'maddie')
            cut11c = fr(e9 + 0.5)
            d05 = cut11c - cut05
            S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, cut05, cut11c, 'd3', still=True,
                    zoom=[[0.0, 1.04], [1.0, 1.04], [d05, 1.18]], rot=[[0.0, 0.0], [1.0, 0.0], [d05, 3.0]])
            i11c = 0.5
            e10 = S.human('vox-lady', 'd3-10-lady', fr(cut11c + 0.6), 'd3', 10, 'lady', lufs=-17.0)
            m['lady_q'] = (fr(cut11c + 0.6), e10, cut11c, i11c)
            e11 = S.human('vox-maddie', 'd3-11-maddie', fr(e10 + 0.5), 'd3', 11, 'maddie')
            # Picture for the answer and the vow: the lady (D11c) for the start of the answer, her hands on the patchwork
            # (D11b, mouthless) for the rest; Sandra (D08, mouth shut) hears "I won't switch it on unless you want it."; the
            # end of the vow on Maddie's beacon (D03c's unused tail); the cut to them sitting lands on "take a seat".
            MAX6 = 6.0 - 1 / FPS
            cut11b = fr(min(cut11c + MAX6 - i11c, max(e10 + 2.5, e11 + 0.4 - MAX6)))
            S.piece('D11c', S.clip('D11c'), i11c, cut11c, cut11b, 'd3', grade=LIFT)
            cut08 = fr(min(cut11b + MAX6, e11 + 0.4))  # if the answer runs past her hands, Sandra hears its end
            if not R14:
                S.piece('D11b', S.clip('D11b'), 0.0, cut11b, cut08, 'd3', grade=LIFT)
            if R14:
                # Kai at1068: Sandra, frightened: "I don't like the idea of... it feels like dying." / Maddie, with long pauses:
                # "I won't switch it on unless you want it. ... All of you. ... And only if you're sure." No "take a seat": a
                # breath, then they sit. STAND-INS until the new two-shot (Sandra speaking, clean Maddie beside her) is made:
                # Sandra on D08 (mouth shut; the battered Maddie behind her), the vow on D03c from its start (a repeat).
                S.piece('D11b', S.clip('D11b'), 0.0, cut11b, cut08, 'd3', grade=LIFT)
                e14 = S.human('vox-sandra', 'd3-14-sandra', fr(max(cut08 + 0.3, e11 + 0.6)), 'd3', 14, 'sandra', lufs=-17.0)
                cutm = fr(min(cut08 + MAX6, e14 + 0.4))
                S.piece('D08', S.clip('D08'), 0.0, cut08, cutm, 'd3')
                e15 = S.human('vox-maddie', 'd3-15-maddie', fr(cutm + 0.4), 'd3', 15, 'maddie')
                end_d3 = fr(e15 + 1.0)
                assert end_d3 - cutm <= 8.0 + 3.0, ('the vow overruns Maddie even with a held last frame', e15, cutm)
                if end_d3 - cutm > 8.0 - 1 / FPS:
                    c.flags.append(f'D round 14 STAND-IN: the vow runs {end_d3 - cutm - 8.0:.1f} s past D03c; its last frame holds '
                                   '(the robot is still; the beacon keeps pulsing on her words).')
                S.piece('D03c', S.clip('D03c'), 0.0, cutm, end_d3, 'd3')
                m['take_seat'] = e15
                m['lady_d3'] = (e15, e15)
                m['d3_lines'] = (a, e15)
                t = c.close(b, end_d3)
                b['see'] = ('Derek asks what it is. Maddie: it runs on them, all hundred. "Hundred." A pause. What will it feel '
                            'like? A bit like dying, mostly like nodding off. The lady: and afterwards? They will be themselves, '
                            'just before it all went wrong, and he will be with them. Sandra: she doesn\'t like it, it feels like '
                            'dying. Maddie: she won\'t switch it on unless they want it, all of them, and only if they\'re sure.')
                c.flags.append('D round 14 (Kai, 9 Nov, timeline r13): "Hundred. ... What will it feel like?" one take (at542); Sandra '
                               '"I don\'t like the idea of... it feels like dying." and Maddie "I won\'t switch it on unless you want it. ... '
                               'All of you. ... And only if you\'re sure." with long pauses, no "take a seat" (at1068); no "Thank you" '
                               '(at1284); the hands quick: in on the grip, the whisper at once, white (at1342/at1575).')
                c.flags.append('D round 14 STAND-INS: Sandra speaks on D08 (mouth shut, battered Maddie behind) and the vow plays on '
                               'D03c from its start (seen earlier). Both go when the new two-shot is made. The chair layouts (D05, D10x) '
                               'and the hands (D12, Sandra reaching) are the old shots until the new ones are approved.')
        if R13 and not R14:
            e12 = S.human('vox-maddie', 'd3-12-maddie', fr(e11 + 0.35), 'd3', 12, 'maddie')
            i3t = 4.2
            end_d3 = fr(e12 - 0.9)  # out on "take a seat": they sit
            cut3t = fr(max(cut08 + 1.0, end_d3 - (8.0 - i3t - 1 / FPS)))
            assert cut3t - cut08 <= MAX6, ('the vow overruns Sandra and Maddie', e12, cut3t)
            S.piece('D08', S.clip('D08'), 0.0, cut08, cut3t, 'd3')
            S.piece('D03c', S.clip('D03c'), i3t, cut3t, end_d3, 'd3')
            m['take_seat'] = e12
            m['lady_d3'] = (e12, e12)
            m['d3_lines'] = (a, e12)
            t = c.close(b, end_d3)
            b['see'] = ('Derek asks what it is. Maddie: it runs on them, all hundred. Derek asks what it will feel like: a bit '
                        'like dying, mostly like nodding off. The lady asks what comes after: they will be themselves, just '
                        'before it all went wrong, and he will be with them. Maddie will not switch it on unless they all '
                        'want it: if they are sure, take a seat.')
            c.flags.append('D round 13 (Kai, 9 Nov, dialogue 1I + timeline r12 notes): Derek "What will it feel like?" (off, over the '
                           'chairs) / Maddie "It\'s a bit like dying. Mostly like nodding off in front of the telly." / the lady, on '
                           'her close-up, "And afterwards?" / Maddie "Two things..." on the lady and her hands (D11b) / "I won\'t switch it on '
                           'unless you want it. All of you. If you\'re sure... take a seat." on Sandra listening (D08), then Maddie\'s beacon; the cut to them sitting '
                           'lands on "take a seat". "And then?" (Derek\'s angry-looking D07) and D07 are gone. Seven new Gemini '
                           'takes (voices_fix.py D r13), pauses held to 0.45-0.6 s (tighten.py), words untouched.')
            c.flags.append('D round 13 lip-sync: the lady\'s "And afterwards?" is on D11c, a silent close-up: her mouth does not '
                           'move until LatentSync redraws it (one command for Kai).')
    if R7 and not R13:
        e3 = S.human('vox-maddie', 'd3-3-maddie', fr(e2 + 0.6), 'd3', 3, 'maddie')
        if R9:
            # Kai at849: "Will it hurt?" / "Not much..." cut, with Sandra's shot (D08): the chairs go straight to Derek.
            cut07 = fr(e3 + 0.7)
            d05 = cut07 - cut05
            S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, cut05, cut07, 'd3', still=True,
                    zoom=[[0.0, 1.04], [1.0, 1.04], [d05, 1.14]], rot=[[0.0, 0.0], [1.0, 0.0], [d05, 2.5]])
        else:
            e4 = S.human('vox-sandra', 'd3-4-sandra', fr(e3 + 0.7), 'd3', 4, 'sandra', lufs=-17.0)
            cut08 = fr(e4 + 0.3)
            d05 = cut08 - cut05
            S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, cut05, cut08, 'd3', still=True,
                    zoom=[[0.0, 1.04], [1.0, 1.04], [d05, 1.16]], rot=[[0.0, 0.0], [1.0, 0.0], [d05, 3.0]])
            e5 = S.human('vox-maddie', 'd3-5-maddie', fr(cut08 + 0.45), 'd3', 5, 'maddie')
            cut07 = fr(min(cut08 + 8.0 - 1 / FPS, e5 + 0.7))
            S.piece('D08', S.clip('D08'), 0.0, cut08, cut07, 'd3')
        i07 = 0.9
        e6 = S.human('vox-derek', 'd3-6-derek', fr(cut07 + 1.5 - i07), 'd3', 6, 'derek')  # on his mouth at ~1.5 s
        a7 = fr(e6 + 0.6) if R8 else fr(max(e6 + 0.6, cut07 + 4.0 - i07))  # r7: once his mouth has shut (~4 s); r8: his mouth is redrawn (LatentSync), shut after the line
        e7 = S.human('vox-maddie', 'd3-7-maddie', a7, 'd3', 7, 'maddie')
        # The key line (~14 s) needs more picture than any one shot: Derek hears "You don't wake up. Not this you." (D07
        # to its end), the promise lands on the lady's nod (D11c6), and "...he'll be there with you" comes back to Maddie's
        # beacon (D03cr3's unused tail, 4.2 s on). "He?" waits for her last word; it is on Derek's mouth only if it lands
        # within 0.5 s of the cut to D09t-t2.
        if R9:
            # Kai at1147/at1275: the waffle is gone, the line is short: Derek hears it (D07, his redrawn mouth shut), and the
            # promise lands on the lady's nod (D11c6) if it runs past his shot.
            out07 = fr(min(cut07 + 8.0 - i07 - 1 / FPS, e7 + 0.6))
            S.piece('D07', S.clip('D07'), i07, cut07, out07, 'd3')
            cut09t = out07
            if e7 + 0.6 > out07:
                cut09t = fr(min(out07 + 6.0 - 0.5 - 1 / FPS, e7 + 0.6))
                S.piece('D11c', S.clip('D11c'), 0.5, out07, cut09t, 'd3', grade=LIFT)
            if e7 + 0.6 > cut09t:  # r10: the longer line ends on Maddie's beacon (D03cr3's unused tail)
                out11c = cut09t
                cut09t = fr(min(out11c + 8.0 - 4.2 - 1 / FPS, e7 + 0.6))
                S.piece('D03c', S.clip('D03c'), 4.2, out11c, cut09t, 'd3')
        else:
            out07 = fr(cut07 + 8.0 - i07 - 1 / FPS)
            S.piece('D07', S.clip('D07'), i07, cut07, out07, 'd3')
            i11c = 0.5
            out11c = fr(out07 + 6.0 - i11c - 1 / FPS)
            S.piece('D11c', S.clip('D11c'), i11c, out07, out11c, 'd3', grade=LIFT)  # the promise on the lady
            i3t = 4.2
            cut09t = fr(min(out11c + 8.0 - i3t - 1 / FPS, max(e7 + 0.3, out11c + 1.5)))
            S.piece('D03c', S.clip('D03c'), i3t, out11c, cut09t, 'd3')
        if R8:
            # Kai at1400 (6 Nov): cut to the chase. "He?" / "He's only data, love. Data travels." / "Right." and Derek walking to
            # his chair are gone: the scene goes from the promise straight to them sitting.
            assert e7 + 0.2 <= cut09t, ('the key line overruns its picture', e7, cut09t)
            end_d3 = cut09t  # out on Maddie's beacon, the promise just said
            e10 = e7
            if R9:
                c.flags.append('D round 9 (Kai at331/at557/at849/at1147/at1275): Maddie empathetic, in Kai\'s words: "It\'s the time '
                               'machine. And it runs on you. Can you see how many chairs there are?" / Derek "Hundred." / "Yeah. It runs on '
                               'all of you, all at once. It\'s a bit like dying. Mostly like nodding off in front of the telly." / "And then?" / '
                               '"You don\'t wake up. Not this you. But look, it\'s going to be fine. He\'ll be there with you this time." '
                               '"Will it hurt? / Not much..." and Sandra\'s shot (D08) are cut.')
            c.flags.append('D round 8 (Kai at1400): cut to the chase. Maddie\'s line in Kai\'s words: "You don\'t wake up. Not this '
                           'you. But look, you\'ll go back. It\'ll still be you, before it all went wrong. And he\'ll be there with you '
                           'this time." "He?", "He\'s only data, love. Data travels." and "Right." are cut, with D09t and D09s.')
        else:
            he = fr(max(cut09t + 0.45, e7 + 0.45))
            i09t = max(0.0, fr(0.5 - (he - cut09t)))
            e8 = S.human('vox-derek', 'd3-8-derek', he, 'd3', 8, 'derek')
            if he - cut09t > 0.5:
                c.flags.append(f'D round 7: "He?" lands {he - cut09t:.2f} s into D09t, after his mouth has moved (~0.5 s): '
                               'it reads as off his lips. Kai to judge.')
            e9 = S.human('vox-maddie', 'd3-9-maddie', fr(e8 + 0.5), 'd3', 9, 'maddie')
            cut09s = fr(min(cut09t + 8.0 - i09t - 1 / FPS, e9 + 0.6))
            S.piece('D09t', S.clip('D09t'), i09t, cut09t, cut09s, 'd3')
            e10 = S.human('vox-derek', 'd3-10-derek', fr(cut09s + 0.5), 'd3', 10, 'derek')
            end_d3 = fr(cut09s + 7.0)  # he walks to his chair, sits and lies back (~7 s)
            S.piece('D09s', S.clip('D09s'), 0.0, cut09s, end_d3, 'd3')
        m['lady_d3'] = (e10, e10)
        m['d3_lines'] = (a, e10)
        t = c.close(b, end_d3)
        b['see'] = ('Derek asks what it is. Maddie tells them straight: count the chairs; it runs on them; a bit like dying, '
                    'they won\'t wake up, not this them; but they\'ll go back, still themselves, before it all went wrong, and '
                    'this time he\'ll be there with them.') if R8 else ('Derek asks what it is. Maddie, gleaming, tells them straight: count the chairs; it runs on them; a bit '
                    'like dying, they won\'t wake up, not this them; but they will be themselves again, just before it all went '
                    'wrong, and this time he will be there with them. Derek: "Right." He is the first to lie down.')
        c.flags.append('D round 7 (Kai, 6 Nov, dialogue draft 1F): the wafer now says what it costs. Twelve new Gemini takes '
                       '(voices_fix.py D r7). All picture is existing clips, no credits: D03c, the chairs from above (D05), '
                       'Sandra listening (D08, mouth shut), Derek (D07: "And then?" on his mouth), the lady\'s nod on the '
                       'promise (D11c6), Derek again (D09t-t2: "He?" on his mouth), then Derek walking to his chair and lying '
                       'back (D09s-t2) on "Right.": he goes first.')
        c.flags.append('D round 7 lip-sync is approximate (2 fps mouth reads): "And then?" and "He?" are placed on Derek\'s '
                       'open mouth; Hundred and Will it hurt? are off-screen over the chairs. For Kai\'s eye.')
    if R5 and not R7:
        # Take r5e, five phrases (silence map at -38 dB): "It's the time machine." 0.0-1.79; "It'll send all of you
        # back," 2.70-4.84; "to before it all went wrong." 5.70-7.35; "And it'll send him too," 9.05-10.72; "so he can
        # help you avoid it." 11.63-13.18. Its pauses held to 0.6 / 0.6 s so the first three fit her 8 s shot, 1.0 s before "And", 0.85 s before "so".
        # The first three on her (D03c, 8 s); the cut to the hundred chairs from above lands in that breath, and the
        # last two play over them.
        tm = fr(cut3c + 0.25)
        P = [(0.0, 1.85, 0.0), (2.64, 4.90, 0.6), (5.64, 7.41, 0.6), (8.99, 10.78, 1.0), (11.57, 13.24, 0.85)]
        ends, t_ = [], tm
        for i, (v0, v1, gap) in enumerate(P):
            if i:
                t_ = fr(ends[-1] + gap)
            ends.append(c.say('vox-maddie', mv, v0, v1, t_, f'd3 line 1 maddie: phrase {i + 1} (r5e)', ref=span(mv)))
        c.line(b, 1, 'maddie', tm, ends[-1] - tm, sc.text(k), 'kai')
        cut05 = fr(ends[2] + 0.4)
        assert cut05 - cut3c <= 8.0 - 1 / FPS, cut05 - cut3c
        S.piece('D03c', S.clip('D03c'), 0.0, cut3c, cut05, 'd3')
        end_d3 = fr(max(ends[-1] + 1.2, cut05 + 5.0))
        d05 = end_d3 - cut05
        S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, cut05, end_d3, 'd3', still=True,
                zoom=[[0.0, 1.04], [1.5, 1.04], [d05, 1.12]], rot=[[0.0, 0.0], [1.5, 0.0], [d05, 2.0]])
        m['lady_d3'] = (ends[-1], ends[-1])
        m['d3_lines'] = (a, ends[-1])
        t = c.close(b, end_d3)
        c.flags.append('D round 5 (Kai at469): Maddie\'s line is now the film\'s key line, in Kai\'s words: "It\'s the time '
                       'machine. It\'ll send all of you back, to before it all went wrong. And it\'ll send him too, so he can help '
                       'you avoid it." (Gemini Aoede, take r5e, heard exactly). Three phrases on her, then the cut to the hundred '
                       'chairs from above in the breath before "And", the last two over the chairs.')
        c.flags.append('D round 5 (Kai at567/at715): the old lady\'s answer ("Look, this has been the worst possible outcome...") '
                       'is cut with both its shots: the deal was made in the bunker. Her voice is no longer heard in D.')
    if not R5:
        # D round 3 (Kai reel at2055, 23 Oct): the old listening shot of the lady (D04r3-t1) is cut; from Maddie it goes
        # straight to the rainbow on the lady's face (D04r4-t2). So all of Maddie's line has to play on D03cr3 (8 s): her
        # take r4a in three phrases (silence map, 20 ms: "It's the time machine." 0.46-2.28, "You do understand" 4.20-5.80,
        # "what this will cost you." 6.98-8.66), its pauses held to 1.35 s and 0.8 s (were 1.9 and 1.2), 0.3 s on her first.
        tm = fr(cut3c + 0.3)
        e1 = c.say('vox-maddie', mv, 0.40, 2.32, tm, 'd3 line 1 maddie: "It\'s the time machine."', ref=span(mv))
        e2 = c.say('vox-maddie', mv, 4.14, 5.86, fr(e1 + 1.35), 'd3 line 1 maddie: "You do understand"', ref=span(mv))
        e_m = c.say('vox-maddie', mv, 6.94, 8.74, fr(e2 + 0.8), 'd3 line 1 maddie: "what this will cost you."', ref=span(mv))
        c.line(b, 1, 'maddie', tm + 0.05, e_m - tm - 0.05, sc.text(k), 'kai')
        cut04 = fr(e_m + 0.05)
        assert cut04 - cut3c <= 8.0 - 1 / FPS, cut04 - cut3c
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
        cut4b = cut04  # D round 3: straight from Maddie to the rainbow on her face (D04r3-t1 is out)
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
                       f'(D03cr3, her beacon pulsing in the clip) and {tm - cut3c:.1f} s on her before she speaks. D round 3 (Kai '
                       'at2055): her whole line plays on her, its pauses held to 1.35 s and 0.8 s so it fits her 8 s clip, '
                       'and the cut goes straight to the rainbow on the lady\'s face (the old listening shot is out). The cut '
                       'out of her face comes 0.6 s after her last word, onto the hundred chairs from above, held 2 s in silence '
                       'before they turn: the breath after the height is on what it will cost.')
        c.flags.append('d3 (Kai reel at2108/at2566, ending round 2): the lady no longer comforts Maddie. Stern, in Kai\'s '
                       'words: "Look, this has been the worst possible outcome for humanity. If there\'s a chance we could go '
                       'back in time to change it, I want to take that chance." (take r7c, 10.8 s). It answers Maddie\'s "You do '
                       'understand what this will cost you." (Kai\'s pick, unchanged; nothing added). No "I trust your boss".')
        c.flags.append(f'd3 lip-sync (the lady, D04r4-t2, at 112%): the cut comes straight from Maddie\'s "cost you.", 0.5 s '
                       f'before her first word. Omni spoke her whole line 1.3-1.7x quicker than the '
                       f'take. "Look," on her mouth at x1.0; "this has been the worst" at x1.3; "possible outcome for humanity." '
                       f'at its own speed over the hundred listening (D03cr3 from its start, gleaming Maddie and the wafer); '
                       f'back on her for "If there\'s a chance... change it," at x1.3 and "I want to take that chance." at x1.15. '
                       f'Two phrases at x1.3 is the stretch cap: for Kai\'s ear.')

    if R8:
        c.flags.append('D round 8 (Kai at1750): the tea (d4: D06, "Milk, two sugars.") is cut whole: "We need to be brutal."')
    else:
        # ---- d4: a hundred chairs (L3 overhead, rotate + push), the tea (D06): unchanged picture; Maddie says the line
        s4 = t
        b = c.beat('d4', 'A hundred chairs', s4, act='The clean room',
                   see='Overhead, a hundred chairs laid out like a chip. Then one chair: the old lady under her patchwork '
                       'blanket reaches down for her steaming mug of tea.')
        d05 = 0.0 if R5 else 5.0  # round 1: held 2 s (was 1 s) as the breath after the lady's answer; R5: in d3
        if not R5:
            S.piece('D05', sc.picks['picks']['D05']['file'], 0.0, s4, s4 + d05, 'd4', still=True,
                    zoom=[[0.0, 1.04], [2.0, 1.04], [d05, 1.12]], rot=[[0.0, 0.0], [2.0, 0.0], [d05, 2.0]])
        s6 = fr(s4 + d05)
        # Reel round 1 (Kai at2347, 23 Oct): the lady's "Is that tea?" is dropped; Maddie just tells her, at the moment
        # the lady's question used to start.
        a2 = fr(s6 + (LEAD + 0.6 if R5 else LEAD + 1.2))
        e2 = S.human('vox-maddie', 'd4-0-maddie', a2, 'd4', 0, 'maddie')
        end_d4 = fr(min(s6 + 8.0, max(s6 + 6.6, e2 + TAIL)))
        S.piece('D06', S.clip('D06'), 0.0, s6, end_d4, 'd4')
        t = c.close(b, end_d4)
        c.flags.append('d4 (Kai at2347, reel round 1): the lady\'s "Is that tea?" is gone; Maddie just tells her.')
        c.flags.append('d4 (D round 4, Kai at2525, pick D06r6-a): D06 re-made (D06r6-t1, 12 credits): the old lady, lying '
                       'back in her chair under the patchwork blanket, reaches down and lifts her own mug of tea out of frame.')
        c.flags.append('d4 (D round 3, Kai reel at2525): "I kept your loyalty cards." is cut: Maddie says only "Milk, two '
                       'sugars." (the same take, cut before the second sentence).')
        c.flags.append('d4 (Kai ld4-1): "Milk, two sugars." is Maddie\'s (she is the delivery robot; '
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
    if R5:
        b['see'] = 'They sit, every one of them; nobody makes them. No words.'
        d10r5 = 3.5
        if R13 and not R14:  # Kai, 9 Nov (dialogue 1I): they sit because they chose to; Maddie's quiet "Thank you." over them
            b['see'] = 'They sit, every one of them: that is the yes. Maddie, very quietly: "Thank you."'
            et = S.human('vox-maddie', 'd6-0-maddie', fr(max(m['take_seat'] + 1.8, s6b + 2.4)), 'd6', 0, 'maddie', lufs=-19.0,
                         what='d6 line 0 maddie: "Thank you." (very quiet, as they sit)')
            d10r5 = min(8.0 - 1 / FPS, fr(et + 1.2 - s6b))
        S.piece('D10x', S.clip('D10x'), 0.0, s6b, fr(s6b + d10r5), 'd6')
        em = s6b
        m['q_lady'] = s6b
        m['maddie_d6'] = (s6b, s6b)
        t = c.close(b, fr(s6b + d10r5))
        c.flags.append('D round 5 (Kai at1054/at1615): "they sit" is now the D10x angle (the canonical room, everyone in '
                       'their chair, as the crossing opens on), held 3.5 s with no words. The lady\'s "When he arrives back '
                       'in time, what will he do?", Maddie\'s answer, and both their shots (D11, D11c) are cut (Kai '
                       'at1091/at1178/at1285: Maddie has already said it). Straight on to Sandra and Derek\'s hands.')
    if not R5:
        i10, d10 = 0.4, 3.5  # D round 3 (Kai at2714): out before ~4 s, where the near man sits up and a figure sits in behind him
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
        # D round 4 (Kai at2787, pick D11c6-d): a silent close-up of the lady as the plan sinks in, before the hands
        # (it cut too quickly to Sandra and Derek). D11c6-t1: she looks to the robot, her eyes fix, a breath, one small nod.
        i11c, d11c = 1.2, 3.6
        S.piece('D11c', S.clip('D11c'), i11c, end11, fr(end11 + d11c), 'd6', grade=LIFT)
        end11c = fr(end11 + d11c)
        m['q_lady'] = q1
        m['maddie_d6'] = (am, em)
        t = c.close(b, end11c)
        c.flags.append(f'd6 (D round 4, Kai at2787): a silent close-up of the old lady (D11c6-t1, 6 s, 10 credits) holds '
                       f'{d11c:.1f} s after Maddie\'s answer: her eyes fix on the robot, a breath, one small nod. Then the hands.')
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
    b = c.beat('d7', 'Before the world ended' if R7 else 'Seat down', s7, act='The crossing',
               see='Two hands across the gap between two chairs. They find each other and grip. Her last joke, and his '
                   'answer.')
    if R8:
        # Kai at1951/at2104/at2152 (6 Nov): Sandra's new line opens over the last of "they sit", so the hands (D12, then
        # D12x chained) only have to carry Derek and the white. D12x grips firm to ~4.0 s and loosens from ~4.5 s; the
        # white has to be full by 3.7 s, so nothing of the loosening is ever seen.
        if R14:
            # Kai at1342/at1575: quicker. In on the grip (D12 from 2.0 s: her hand has nearly found his), the whisper at once,
            # then white over 1.5 s on this shot; no D12x.
            i12 = 2.0
            a = fr(s7 + 0.6)
            e3 = S.human('vox-derek', 'd7-2-derek', a, 'd7', 2, 'derek', lufs=-19.0,
                         what=f'd7 line 2 derek, whispered: "{sc.text("d7-2-derek")}"')
            end_d7 = fr(e3 + 1.6)
            dd = end_d7 - s7
            S.piece('D12', S.clip('D12'), i12, s7, end_d7, 'd7', grade=LIFT, white=[[max(0.0, dd - 1.5), 0.0], [dd, 1.0]])
            m['x12_from'] = None
            i12x_used = 0.0
            em = e3
        elif R11:  # Kai at1242: only his whisper, on the hands, once they have found each other and gripped (~4.5 s in D12)
            a = e2 = fr(s7 + 5.0)
        else:
            a = fr(s7 - 1.6)
            e = S.human('vox-sandra', 'd7-0-sandra', a, 'd7', 0, 'sandra', lufs=-17.0,
                        what=f'd7 line 0 sandra: "{sc.text("d7-0-sandra")}" (opens over the last of they sit)')
            e2 = S.human('vox-derek', 'd7-1-derek', fr(e + 0.5), 'd7', 1, 'derek', lufs=-17.0,
                         what=f'd7 line 1 derek: "{sc.text("d7-1-derek")}"')
        if not R14:
            e3 = S.human('vox-derek', 'd7-2-derek', a if R11 else fr(e2 + 1.3), 'd7', 2, 'derek', lufs=-19.0,
                         what=f'd7 line 2 derek, whispered: "{sc.text("d7-2-derek")}" (Kai at2104: a pause before it)')
            X12_GRIP = 3.7  # D12x clip time by which the white is full
            end_d7 = fr(max(e3 + 0.5, s7 + 8.0 - 1 / FPS)) if R11 else fr(e3 + 0.5)  # r11: D12 whole, so D12x chains on unbroken
            S.piece('D12', S.clip('D12'), 0.0, s7, min(end_d7, s7 + 8.0 - 1 / FPS), 'd7', grade=LIFT)
            i12x_used = max(0.0, fr(end_d7 - (s7 + 8.0 - 1 / FPS)))
            assert i12x_used <= X12_GRIP - 1.5, ('the goodbye runs into the loosening grip', i12x_used)
            if i12x_used > 0:
                S.piece('D12x', S.clip('D12x'), 1 / FPS, s7 + 8.0 - 1 / FPS, end_d7, 'd7', grade=LIFT)
            m['x12_from'] = i12x_used
            em = e3
    else:
        a = fr(max(s7 + 1.0, em + 0.6))
        e = S.human('vox-sandra', 'd7-0-sandra', a, 'd7', 0, 'sandra', lufs=-17.0,
                    what=f'd7 line 0 sandra: "{sc.text("d7-0-sandra")}"')
        a2 = fr(e + 0.5)
        e2 = S.human('vox-derek', 'd7-1-derek', a2, 'd7', 1, 'derek', lufs=-17.0,
                     what=f'd7 line 1 derek: "{sc.text("d7-1-derek")}"')
        end_d7 = fr(e2 + 1.0)
        S.piece('D12', S.clip('D12'), 0.0, s7, min(end_d7, s7 + 8.0 - 1 / FPS), 'd7', grade=LIFT)
        i12x_used = 0.0
        if end_d7 > s7 + 8.0 - 1 / FPS:
            i12x_used = fr(end_d7 - (s7 + 8.0 - 1 / FPS))
            S.piece('D12x', S.clip('D12x'), 1 / FPS, s7 + 8.0 - 1 / FPS, end_d7, 'd7', grade=LIFT)
    m['hands'] = s7
    t = c.close(b, end_d7)
    c.flags.append(('d7 (D round 7, Kai 6 Nov, dialogue draft 2D): no afterwards. ' if R7 else 'd7 (Kai ld7-0/ld7-1, bd7 "brilliant scene"): no seat joke. ')
                   + f'Sandra: "{sc.text("d7-0-sandra")}" Derek: "{sc.text("d7-1-derek")}" The shot is kept; the two lines '
                   f'need more than its 8 s, so it runs on into the first {i12x_used:.1f} s of D12x (chained from D12\'s last '
                   'frame, so the grip carries on unbroken) as the chair light begins to rise. Half a second\'s breath '
                   'between her line and his.')

    # ---- d8: the crossing. D10x-t2 (the "they sit" angle again, every chair occupied, the lights rising; a cut, not a
    # chain), then the hands as the light reaches them and the grip goes slack (D12x's later stretch), white; out of the
    # white, the doorway prints as real video (D14p-t2, no post zoom); the dusk wide, the seam runs bright and goes out.
    s8 = t
    b = c.beat('d8', 'The crossing', s8, act='The crossing',
               see='The room of a hundred occupied chairs again; the lights come up. The hands: the light reaches them and '
                   'still holding on, they go to white. Outside, the prints at the door, then the building at dusk: the amber seam '
                   'runs bright end to end and goes out.')
    d10x = 0.0 if R8 else 5.5  # Kai at2360 (6 Nov): no cut back to the chairs; the hands go straight to white
    if not R8:
        S.piece('D10x', S.clip('D10x'), 0.0, s8, s8 + d10x, 'd8')
    s12x = fr(s8 + d10x)
    # D round 3 (Kai at3282): fade to white while they are STILL holding hands. D12x's grip holds to ~4.6 s and goes
    # slack from ~4.8 s, so its window now ends at 4.7 s, ramping to white over its last 1.5 s (was: the slack hands,
    # white over 1 s after the release). The grip is the same few seconds already seen in d7: still hands, no jump.
    if R14:  # the hands went to white in d7 (Kai at1575)
        d12x = 0.0
    else:
        i12x, d12x = (m['x12_from'], fr(3.7 - m['x12_from'])) if R8 else (2.2, 2.5)
        S.piece('D12x', S.clip('D12x'), i12x if (not R8 or i12x > 0) else 1 / FPS, s12x, s12x + d12x, 'd8',
                white=[[max(0.0, d12x - 1.5), 0.0], [d12x, 1.0]], grade=LIFT if R8 else None)
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
                   'is gone. Then the hands (D12x), ramped to white over 1.5 s while they are still holding on (D round 3, Kai '
                   'at3282: they never let go on screen).')
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
    if R13 and 'D12' in gains and 'D12x' in gains:
        # Kai at1428 (9 Nov): a grade jump at the join of the hands. D12x is D12 chained on (one continuous shot), but each
        # got its own white balance from its own mean (D12x's is skewed by the light swelling later in it): one balance.
        gains['D12x'] = gains['D12']
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
    # Kai at1849 (6 Nov, r8): the mournful cello takes over on 'they sit', not on the hands; the cute piano goes there.
    cin = st['d6'] if R8 else m['hands']
    r1 = fr(cin + (3.0 if R11 else 1.5))
    d = r1 - r0
    x = C.level(C.decode(room, 0.0, d), rms=-25, peak=-4)
    x = duck(x, r0, 0.45)
    x *= C.env(len(x), [(0, 0), (1.2, 1), (d - (4.5 if R11 else 2.5), 1), (d, 0)])
    mx.add('mus-d-room', x, r0, room, 'D-room: glassy piano, music-box tender, in after "fussy", under the d6 speech, '
           'handing over to D-cross on the hands')
    # ---- D-cross (7bead5f0): cello and piano. Round 1 (Kai bd9): it carries straight across from the crossing into
    # Maddie alone. It enters on the hands and is placed so its held last chord (stops at 40.0 s in the take) and its
    # release (to 41.4 s; what follows in the file is not the cue) end on the hard cut to E. Its one breath (the take's
    # dip at ~24.5-26.5 s) is printed against the picture.
    cross = sc.media / 'suno' / 'gpom-sh-d-cross-a-v6-w30-7bead5f0.wav'
    stop_src, end_src = 40.0, 41.4
    c0 = cin
    off = end_src - (total - c0)
    pad = max(0.0, -off)
    off = max(0.0, off)
    d = end_src - off
    x = C.decode(cross, off, d)
    x = C.level(x, rms=-23.5, peak=-3)
    x = duck(x, c0 + pad, 0.6)
    x *= C.env(len(x), [(0, 0), (4.0 if R11 else 1.5, 1), (d - 0.04, 1), (d, 0)])
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
    # (D round 4: D06 re-made with the lady lifting her own mug; no robot edges into it, so no wheels there)
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
    E.C3.ROOT = sc.media / (f'cut-{E.TAG}' if E.TAG else 'cut')
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
    for fid in ('D10x', 'D12' if R14 else 'D12x'):  # r14: the white ramp is on D12 itself
        pv = [v for v in c.video if pathlib.Path(v['source']).stem.startswith(fid + '-') or pathlib.Path(v['source']).stem == fid][-1]
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
