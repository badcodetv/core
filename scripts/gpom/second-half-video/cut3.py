#!/usr/bin/env python3
"""GPOM second half, cut 3: two rough cuts in the new-scene timeline format (scripts/scene/timeline.py).

    python3 scripts/gpom/second-half-video/cut3.py A          # scene A, the kill bots (beats 0-12; round 3)
    python3 scripts/gpom/second-half-video/cut3.py B          # scene B, Maddie at the door (14a-17b; round B2)
    python3 scripts/gpom/second-half-video/cut3.py A B --no-preview
    python3 scripts/gpom/second-half-video/cut3.py A B --tag d1   # Kai's dialogue-page picks (1D, 2H), 27 Oct
    python3 scripts/gpom/second-half-video/cut3.py B --tag br     # the bridge: no doorstep talk (Kai, 28 Oct)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d3     # Maddie's storyverse intro, draft 1G (2 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d4     # + Kai's timeline r5 notes (2 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d5     # + the wide approach WA02 in beat 10b (2 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d6     # draft 1H + the extended travelling shot (2 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d7     # + the row lip sync v3 (re-made clips) + the stand-down SD01 (3 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d8     # Kai's r9 notes: draft 1I, the row re-cut on reaction shots, boss without 'Maddie' (3 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d13    # draft 1K: swoop under Maddie -> the hologram -> pull-out (5 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d14    # Kai r15: no swoop; bridge line, street fades to black -> hologram -> fade up (5 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d15    # the brutal kill-bot cut after beat 0; bridge loudness-matched (5 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d16    # faster voices: the row sped (picture+voice), Maddie re-voiced fast (5 Nov)
    python3 scripts/gpom/second-half-video/cut3.py A --tag d17    # Kai r18 notes: the row at natural speed, lips re-fitted (voice-row-fit.py) (5 Nov)

--tag X writes to clips/second-half/cut3/<scene>-X/ instead of cut3/<scene>/, so a round never rewrites the stems and
lines an earlier Premiere sequence plays from. --tag d1 also swaps in the dialogue-page words: beat 0 from
scenes/second-half-a-killbots/voices-d1.json, beat 17 from scenes/second-half-b-the-door/voices-d1.json.

Modelled on cut2.py and reusing its mixer (decode / level / env / fades / Mix / write_wav / integrated /
ENC); cut 2's own path is untouched. Rules are new-scene stage 4's: picture timed to the real voice
lengths, LEAD 0.4 s before a beat's first line, GAP 0.35 s between lines, TAIL 0.6 s after; speech is
never slowed; a shot too short for its words ping-pongs (looped=True); one stem per track, ducks written
into the stems; the mix at -16 LUFS, limited.

Sources (Kai's picks and the cut 3 media, 20 Oct 2026):
  scenes/second-half-cut2-notes.json   Kai's notes, plan and answers (the order of both scenes)
  scenes/second-half-cut3-shots.md     every new clip and its caveats
  scenes/second-half-cut3-cast.json    Maddie's beat-0 take picks and gaps
  audio/voice3/lines.json              every other line, two takes each (the smaller internal gap wins)
  audio/cut3-lip/                      the lip-synced dubs (one per talking clip, sample-aligned)
  audio/cut2/edl.json                  cut 2's music placements, carried over and retimed

Outputs, per scene X (media only): clips/second-half/cut3/X/{edl.json, mix.wav, stems/, preview.mp4,
preview-sheet.jpg, video/ (graded, ping-ponged and HUD clips), hud/ (the wavs the HUD meters read)}.
"""
import json
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cut2 as C  # noqa: E402  (definitions only: its timing/audio run only when called)
import shots as S  # noqa: E402

FPS, SR = 24, 48000
LEAD, GAP, TAIL, CUT_PRE = 0.4, 0.35, 0.6, 0.15
V = S.OUT
AU = S.CLIPS / 'audio'
V3 = AU / 'voice3'
LIP = AU / 'cut3-lip'
SFX = AU / 'sfx'
MS = SFX / 'maddie'
ROOT = S.CLIPS / 'cut3'
ENC = C.ENC
fr, probe = C.fr, C.probe
NAMES = {'ai': 'The AI (through Maddie)', 'bot': 'Maddie', 'woman': 'Sandra', 'man': 'Derek', 'lady': 'The old lady',
         'crowd': 'The hundred'}
TAG = sys.argv[sys.argv.index('--tag') + 1] if '--tag' in sys.argv else None
D1 = TAG in ('d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # the dialogue-page rounds: d1 = drafts 1D + 2H (27 Oct), d2 = draft 2J (28 Oct, scene B)
D2 = TAG == 'd2'
D7 = TAG in ('d7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')
D8 = TAG in ('d8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')
D19 = TAG in ('d19', 'd20')  # round 21 (Kai r20, 6 Nov): Sandra re-edited onto Derek (no LatentSync); d03 ends on 'yet'
D18 = TAG in ('d18', 'd19', 'd20')  # round 20 (Kai r19 notes + dialogue 1D, 6 Nov): ending re-ordered (motorway -> call on Maddie -> wide approach -> stand-down), argument mouths redrawn (LatentSync), hologram 1D
D17 = TAG in ('d17', 'd18', 'd19', 'd20')  # round 19 (Kai r18 notes at3777/at742/at4194/at4230): the row at natural speed, re-voiced/re-rendered for the lips; 'you know' cut; boss line 3 cut; no V3 cut-back
D16 = TAG in ('d16', 'd17', 'd18', 'd19', 'd20')  # round 18 (Kai, 5 Nov meeting): faster voices -- the row sped picture+voice together, Maddie re-voiced fast, boss re-recorded
D15 = TAG in ('d15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai 5 Nov: the brutal kill-bot cut (6, 7, 9a, 11 trimmed, 10b, 12 without HUD); bridge loudness-matched
D14 = TAG in ('d14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai r15 notes (5 Nov): no swoop/pull-out ("no funky camera work"); bridge line c00; street fades to black and back up
D13 = TAG in ('d13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai 5 Nov: draft 1K, the old monologue (lines 2-4) and its inserts out; swoop -> hologram -> pull-out
D12 = TAG == 'd12'  # Kai r13 (at1878): drop line 5 ('And now we've worked all that out... go back and change things'), 'And so did you' -> 'Anyway!'
D11 = TAG in ('d11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai r12 (at1749): overhead road far too tidy -> ia-top3 (ia-09-a, rubble), t4 takes
D10 = TAG in ('d10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai r11 notes (4 Nov): overhead grainy/too fast/too many bays -> ia-top2 (ia-07-a), t2 clips, softer grade
D9 = TAG in ('d9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # Kai, 4 Nov: beat 0 cut between three angles (front, side, overhead) at sentence ends  # Kai's timeline r9 notes (3 Nov)
RT01_IN = 2.5  # the retreat clip's in-point: past the crescent bot's slide to the right (t8, 0-2.5 s)
D3 = TAG in ('d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # draft 1G, Maddie's storyverse intro (2 Nov, scene A only): voices-<tag>.json
D4 = TAG in ('d4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')  # d5 adds the wide approach (WA02) in beat 10b. Kai's timeline r5 notes (2 Nov): 1G reworded, the row re-lip-synced (v2 dubs), Derek's new line,
                  # the boss's firewall line cut, Maddie's 'That was close.' alone, HUD NEW OBJECTIVE
BR = TAG == 'br'  # the bridge (Kai, 28 Oct): the doorstep talk cut; a look, the door shuts on her, voices behind it
STEM = {'bot': 'vox-maddie', 'lady': 'vox-lady', 'woman': 'vox-sandra', 'man': 'vox-derek', 'crowd': 'vox-crowd'}
# Off screen, down the corridor behind the old lady: the corridor's room, further back and duller.
OFF = 'lowpass=f=4500,aecho=0.7:0.5:60|110:0.28|0.16'
LINES = {(r['beat'], r['i']): r for r in json.loads((V3 / 'lines.json').read_text())}
CAST = json.loads((S.SCENES / 'second-half-cut3-cast.json').read_text())
VOICES_B = json.loads((S.SCENES / 'second-half-b-the-door' / 'voices.json').read_text())  # beat 17 round B2
TILE, CORRIDOR = C.TILE, C.CORRIDOR

_dur = {}


def dur(p):
    p = str(p)
    if p not in _dur:
        _dur[p] = probe(p)
    return _dur[p]


# ---------------------------------------------------------------- takes

def bounds(p, floor=40):
    """Speech start / end in a take (10 ms frames over -floor dB from its loudest) and its longest gap."""
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(p), '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    n = len(x) // 160
    db = 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) + 1e-9)
    act = np.where(db > db.max() - floor)[0]
    gap = (np.diff(act).max() - 1) * 0.01 if len(act) > 1 else 0.0
    return act[0] * 0.01, (act[-1] + 1) * 0.01, gap


class Take:
    """A voice take trimmed to its speech (50 ms before, 80 ms after). A filtered (-fx) take is trimmed on
    its dry twin's speech (the tannoy filter mixes in crackle that would read as speech)."""

    def __init__(self, path, dry=None):
        self.path = pathlib.Path(path)
        s, e, self.gap = bounds(dry or self.path)
        self.i = max(0.0, s - 0.05)
        self.d = min(dur(self.path), e + 0.08) - self.i


def pick(beat, i, phrase=None, fx=False):
    """The take of a line (or phrase) with the smaller internal gap; its -fx twin if asked."""
    r = LINES[(beat, i)]
    row = r['phrases'][phrase] if phrase is not None else r
    cands = [(Take(V3 / f), k) for k, (f, _) in enumerate(row['takes'])]
    best, k = min(cands, key=lambda c: c[0].gap)
    if fx:
        return Take(V3 / row['fx'][k][0], dry=best.path), 'ab'[k]
    return best, 'ab'[k]


def take_named(beat, i, letter, phrase=None, fx=False):
    r = LINES[(beat, i)]
    row = r['phrases'][phrase] if phrase is not None else r
    k = 'ab'.index(letter)
    dry = V3 / row['takes'][k][0]
    return Take(V3 / row['fx'][k][0], dry=dry) if fx else Take(dry)


def lipinfo(name):
    """(dub wav, first speech at, last speech end, [(text, at, end)]) for a talking clip, clip time."""
    if D7 and (LIP / f'cut3-lip-{name}-v3-phrases.json').exists():  # re-made talking clips sized to the voice (3 Nov)
        name = f'{name}-v3'
    elif D4 and (LIP / f'cut3-lip-{name}-v2-phrases.json').exists():  # the mouth-mapped redo (2 Nov)
        name = f'{name}-v2'
    d = json.loads((LIP / f'cut3-lip-{name}-phrases.json').read_text())
    ph = [(p['text'], p['at'], p['at'] + (p['to'] - p['from']) / p['tempo']) for p in d['phrases']]
    return LIP / f'cut3-lip-{name}-dub.wav', ph[0][1], max(p[2] for p in ph), ph



def row_piece(c, src, a, b, tempo, name):
    """One phrase of a lip-sync master, cut whole (no slicing inside it), at a tempo; 8 ms fades."""
    out = c.dir / 'row-d8' / f'{name}.wav'
    out.parent.mkdir(parents=True, exist_ok=True)
    d = (b - a) / tempo
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-af',
                    f'atrim={a}:{b},asetpts=N/SR/TB,atempo={tempo},afade=t=in:d=0.008,afade=t=out:st={d - 0.008:.4f}:d=0.008',
                    str(out)], check=True)
    return out, d


def row_d8(c, t, m, LINES):
    """Kai's timeline r9 notes (3 Nov) on the row:
    at3201 "Derek, you've left the seat up again" as one sentence: Sandra's 'Again.' follows 'up' straight away, and
           lands on Derek's face (the start of his re-made clip, before he speaks), so her mouth's own pause never shows;
    at3312 'Five years underground,' (the phrase whose lips were out) plays over Derek's face after his line, and we cut
           to Sandra on 'and you still can't put a seat down', which is in sync;
    at3490 a shorter hold on Derek after 'But the world ended, Sandra!' (0.3 s, was 1.3 s)."""
    t0 = t
    tb = lambda name: json.loads((LIP / f'cut3-lip-{name}-v3-phrases.json').read_text())['phrases']
    s6, d7a, s7, d7b, s72 = tb('6-0'), tb('7d-0c'), tb('7-0'), tb('7d-1c'), tb('7-2')
    up_end = s6[1]['at'] + (s6[1]['to'] - s6[1]['from']) / s6[1]['tempo']
    # Sandra, 6-0: 'Derek.' 'You've left the seat up' on her face
    b6 = c.beat('6', 'The lavatory', t0, act='The row', see='Hard cut to full volume: Sandra, lip-synced.')
    cut1 = fr(t0 + up_end + 0.04)
    c.pic(V / 'cut3-lip-6-0-v3-muted.mp4', 0.0, t0, cut1, '6', source=V / 'cut3-lip-6-0-v3.mp4')
    c.dub('vox-sandra', LIP / 'cut3-lip-6-0-v3-dub.wav', 0.0, cut1 - t0, t0, 'beat 6 6-0 (lip-sync dub)', chain=[TILE])
    again, d_again = row_piece(c, s6[2]['src'], s6[2]['from'], s6[2]['to'], 1.0, '6-0-again')
    t_again = t0 + up_end + 0.08
    c.dub('vox-sandra', again, 0.0, d_again, t_again, "beat 6 Sandra 'Again.' (over Derek)", chain=[TILE])
    c.line(b6, 0, 'woman', t0 + s6[0]['at'], t_again + d_again - t0 - s6[0]['at'], "Derek. You've left the seat up again.", 'kai')
    c.close(b6, cut1)
    # Derek, 7d-0 v3: reacts under 'Again.', says his line, holds under 'Five years underground,'
    b7 = c.beat('7', 'The row, up close', cut1, act='The row',
                see='Derek takes it on the chin, then Sandra; Derek, Sandra: shot by shot, lip-synced.')
    d_line = (d7a[0]['to'] - d7a[0]['from']) / d7a[0]['tempo']
    t_dl = t_again + d_again + 0.3
    i0d = d7a[0]['at'] - (t_dl - cut1)
    assert i0d >= 0.5, i0d
    t_dend = t_dl + d_line
    five, d_five = row_piece(c, s7[0]['src'], s7[0]['from'], s7[0]['to'], s7[0]['tempo'], '7-0-five-years')
    rest, d_rest = row_piece(c, s7[1]['src'], s7[1]['from'], s7[1]['to'], s7[1]['tempo'], '7-0-seat')
    t_five = t_dend + 0.3
    t_rest = t_five + d_five
    cut2 = fr(t_rest - CUT_PRE)
    assert i0d + (cut2 - cut1) <= 6.0 + 1e-6, i0d + (cut2 - cut1)
    c.pic(V / 'cut3-lip-7d-0-v3-muted.mp4', i0d, cut1, cut2, '7', source=V / 'cut3-lip-7d-0-v3.mp4')
    c.dub('vox-derek', LIP / 'cut3-lip-7d-0c-v3-dub.wav', i0d, i0d + (cut2 - cut1), cut1, 'beat 7 7d-0 (lip-sync dub)',
          chain=[TILE])
    c.line(b7, 0, 'man', t_dl, d_line, "I'm really sorry, love.", 'kai')
    c.dub('vox-sandra', five, 0.0, d_five, t_five, "beat 7 Sandra 'Five years underground,' (over Derek)", chain=[TILE])
    c.dub('vox-sandra', rest, 0.0, d_rest, t_rest, "beat 7 Sandra 'and you still can't put a seat down' (lip-synced)",
          chain=[TILE])
    c.line(b7, 1, 'woman', t_five, t_rest + d_rest - t_five, LINES[('7', 0)]['text'], 'kai')
    # Sandra, 7-0 (old clip, synced on the second phrase)
    i0s = s7[1]['at'] - CUT_PRE
    t_rend = t_rest + d_rest
    d_at = d7b[0]['at']
    i0b = max(0.0, d_at - CUT_PRE)
    cut3 = fr(t_rend + GAP - (d_at - i0b))
    c.pic(V / 'cut3-lip-7-0-muted.mp4', i0s, cut2, cut3, '7', source=V / 'cut3-lip-7-0.mp4')
    # Derek, 7d-1: 'But the world ended, Sandra!', a short hold (Kai at3490)
    d_b = (d7b[0]['to'] - d7b[0]['from']) / d7b[0]['tempo']
    t_b = cut3 + (d_at - i0b)
    t_bend = t_b + d_b
    s_at = s72[0]['at']
    t_s = t_bend + 0.3 + GAP
    i0c = max(0.0, s_at - CUT_PRE)
    cut4 = fr(t_s - (s_at - i0c))
    c.pic(V / 'cut3-lip-7d-1-muted.mp4', i0b, cut3, cut4, '7', source=V / 'cut3-lip-7d-1.mp4')
    c.dub('vox-derek', LIP / 'cut3-lip-7d-1c-v3-dub.wav', i0b, i0b + (cut4 - cut3), cut3, 'beat 7 7d-1 (lip-sync dub)',
          chain=[TILE])
    c.line(b7, 2, 'man', t_b, d_b, 'But the world ended, Sandra!', 'kai')
    # Sandra, 7-2 v3
    d_s = (s72[0]['to'] - s72[0]['from']) / s72[0]['tempo']
    end = fr(t_s + d_s + TAIL)
    c.pic(V / 'cut3-lip-7-2-v3-muted.mp4', i0c, cut4, end, '7', source=V / 'cut3-lip-7-2-v3.mp4')
    c.dub('vox-sandra', LIP / 'cut3-lip-7-2-v3-dub.wav', i0c, i0c + (end - cut4), cut4, 'beat 7 7-2 (lip-sync dub)',
          chain=[TILE])
    c.line(b7, 3, 'woman', t_s, d_s, LINES[('7', 2)]['text'], 'kai')
    m['s6'] = t0
    c.flags.append('Beats 6-7 (round 10, Kai at3201/at3312/at3490): "up again" is one sentence, its "Again." over Derek\'s '
                   'face; "Five years underground," over Derek after his line, cut to Sandra on "and you still can\'t put a seat '
                   'down"; the hold after "But the world ended, Sandra!" is 0.3 s (was 1.3 s). Every phrase whole, one tempo each.')
    return c.close(b7, end)

# ---------------------------------------------------------------- the cut being built

class Cut:
    def __init__(self, key, seq, title, heading, intro):
        self.key, self.seq = key, seq
        self.dir = ROOT / (f'{key}-{TAG}' if TAG else key)
        self.vdir = self.dir / 'video'
        self.vdir.mkdir(parents=True, exist_ok=True)
        (self.dir / 'hud').mkdir(exist_ok=True)
        self.meta = dict(title=title, heading=heading, intro=intro)
        self.beats, self.video, self.voices, self.huds, self.flags = [], [], [], [], []
        self.m = {}  # named times for the sound design

    def beat(self, bid, title, start, see='', act=''):
        b = dict(id=bid, title=title, start=fr(start), dur=0.0, see=see, act=act, lines=[])
        self.beats.append(b)
        return b

    def close(self, b, end):
        b['dur'] = fr(end - b['start'])
        return fr(end)

    def pic(self, src, i0, t0, t1, beat, source=None, hud=None):
        t0, t1 = fr(t0), fr(t1)
        assert t1 > t0, (src, t0, t1)
        if D18:  # round 20 (Kai at3436): the argument's mouths redrawn to the round 19 voices (LatentSync 1.6, redraw.py);
            # each -ls24 file starts at that shot's round 19 in-point and runs its round 19 length
            m = re.search(r'lip-([0-9]+[a-z]?-[0-9]+)', pathlib.Path(src).name)
            if m and m.group(1) in LS20 and USE_LS:
                source, i0 = source or src, i0 - LS20[m.group(1)]
                src = LS_DIR / f'{m.group(1)}-ls24.mp4'
                assert -1e-3 <= i0 and i0 + (t1 - t0) <= dur(src) + 0.5 / FPS, (src, i0, t1 - t0, dur(src))
        c = dict(file=str(src), **{'in': fr(i0)}, dur=fr(t1 - t0), start=t0, beat=beat,
                 source=str(source or src), looped=False)
        if hud:
            c['hud'] = hud
        self.video.append(c)
        return c

    def say(self, stem, take, t, beat, what, chain=(), lufs=-16.0, cut=None):
        """Place a take at t (cut = stop it at this timeline time, with a 1.5 s fade)."""
        self.voices.append(dict(stem=stem, src=str(take.path), i=take.i, d=take.d, t=fr(t), chain=list(chain),
                                lufs=lufs, what=what, cut=cut))
        return fr(t) + take.d

    def dub(self, stem, wav, i0, i1, t, what, chain=(), lufs=-16.0):
        """A lip-sync dub's window [i0, i1] (clip time), sample-aligned to its picture at t."""
        self.voices.append(dict(stem=stem, src=str(wav), i=i0, d=i1 - i0, t=t, chain=list(chain), lufs=lufs,
                                what=what, cut=None, whole=True))

    def line(self, beat, i, who, t, d, text, by):
        beat['lines'].append(dict(i=i, who=who, name=NAMES[who], t=round(t, 3) if t is not None else None,
                                  dur=round(d, 3), text=text, by=by))

    # ---- picture prep: ping-pong whatever runs past its source
    def extend(self):
        for c in self.video:
            if c.get('hud') or c['in'] + c['dur'] <= dur(c['file']) + 0.5 / FPS:
                continue
            src = pathlib.Path(c['file'])
            out = self.vdir / f"{src.stem}-i{c['in']:g}-d{c['dur']:.3f}.mp4"
            pingpong(src, c['in'], c['dur'], out)
            c['file'], c['in'], c['looped'] = str(out), 0.0, True


def pingpong(src, i, d, out):
    """cut2.extend's method: forward, then reversed, looped until long enough, cut to length."""
    if out.exists():
        return out
    have = dur(src) - i
    reps = int(np.ceil(d / (2 * have)))
    unit = int(round(2 * have * FPS))
    fc = (f'[0:v]trim=start={i},setpts=PTS-STARTPTS,fps={FPS},split[f][r];[r]reverse[b];[f][b]concat=n=2:v=1,'
          f'loop=loop={reps}:size={unit}:start=0,setpts=N/{FPS}/TB[v]')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-filter_complex', fc, '-map', '[v]',
                    '-t', f'{d:.4f}', *ENC, str(out)], check=True)
    return out


# ---------------------------------------------------------------- V6 colour drift

def regrade_v6(src, out, ref_secs=4.0, strength=0.85, smooth=2.0):
    """Pull the beat-0 travelling shot's colour back towards clip 1's look.

    The six chained Omni clips drift brighter, flatter and cooler over 48 s. Per frame, each RGB channel's
    mean and spread (measured on a 320x180 copy, smoothed over `smooth` s) is moved `strength` of the way to
    the first `ref_secs` of the shot: a ramped per-channel gain + offset, so there is no step anywhere."""
    w, h = 320, 180
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-vf', f'scale={w}:{h}', '-f', 'rawvideo',
                          '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    sm = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)
    mean, sd = sm.mean((1, 2)), sm.std((1, 2))
    k = int(smooth * FPS) | 1
    ker = np.ones(k) / k
    pad = lambda a: np.pad(a, ((k // 2, k // 2), (0, 0)), mode='edge')  # noqa: E731
    mean = np.stack([np.convolve(pad(mean)[:, c], ker, 'valid') for c in range(3)], 1)
    sd = np.stack([np.convolve(pad(sd)[:, c], ker, 'valid') for c in range(3)], 1)
    n_ref = int(ref_secs * FPS)
    m_ref, s_ref = mean[:n_ref].mean(0), sd[:n_ref].mean(0)
    m_tgt = mean + strength * (m_ref - mean)
    s_tgt = sd + strength * (s_ref - sd)
    gain = s_tgt / sd
    drift = mean[-n_ref:].mean(0) - m_ref
    spread = sd[-n_ref:].mean(0) / s_ref
    note = (f'Beat 0 regrade (V6): the six chained clips drift brighter and flatter over the 48 s (by the end the '
            f'channel means are up {drift.min():.0f}-{drift.max():.0f} of 255, the spread down '
            f'{(1 - spread.max()) * 100:.0f}-{(1 - spread.min()) * 100:.0f}%). A ramped per-channel grade pulls every '
            f'frame {strength:.0%} of the way back to the first {ref_secs:g} s (no steps). The robot getting smoother '
            'over the shot is not a colour problem and is still there.')
    if out.exists():
        return out, note
    W, H = 1280, 720
    dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', *ENC, str(out)], stdin=subprocess.PIPE)
    fsz = W * H * 3
    for n in range(len(mean)):
        buf = dec.stdout.read(fsz)
        if len(buf) < fsz:
            break
        x = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        y = (x - mean[n]) * gain[n] + m_tgt[n]
        enc.stdin.write(np.clip(y + 0.5, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close()
    enc.wait()
    dec.wait()
    print(f'V6 regrade: end-of-shot drift R{drift[0]:+.1f} G{drift[1]:+.1f} B{drift[2]:+.1f} (8-bit means), '
          f'spread x{spread.round(3)} -> corrected {strength:.0%} of the way')
    return out, note


# ---------------------------------------------------------------- scene A (round 3, 23 Oct 2026)
# Every change is from scenes/second-half-a-killbots/cut-notes.json: kai_round1 + answers_round1 + words_round1,
# picks_round2, picks_round3, and Kai's voice picks on the round 2 picks page (3DDbvoAxmABJAboca6A3co, db `picks`).

A1 = V3 / 'a1'  # voice3.py --round A1: Maddie's new beat 0 / call / 10b phrases and Derek's two new lines
SUNO_A = ROOT / 'A' / 'suno'  # recorded Suno picks (never downloaded)
SPEAKER = 'highpass=f=300,highpass=f=300,lowpass=f=3400,lowpass=f=3400,volume=6dB,asoftclip=type=atan,' \
          'acrusher=bits=12:mix=0.15,volume=-3dB'  # voice.py FX['speaker']: the boss through Maddie's speaker
MUFFLED = 'lowpass=f=600,lowpass=f=600,lowpass=f=600,volume=-12dB'  # voice.py FX['muffled']
BOSS = {1: 'gpom-sh-a-boss-1-a-v6-w10-7f8d1ef8.wav', 2: 'gpom-sh-a-boss-2-b-v6-w25-d7aaef3e.wav',
        3: 'gpom-sh-a-boss-3-b-v6-w10-bfb1220b.wav'}
# Round 3 (Kai at3398): line 2 cut in and out, so it is being re-recorded; the re-record replaces it once it exists.
BOSS2_RE = sorted(SUNO_A.glob('gpom-sh-a-boss-2*rerec*.wav'))
if BOSS2_RE:
    BOSS[2] = BOSS2_RE[-1].name
BOSS_TEXT = {1: 'Maddie, are you making fun of my simulations again?',
             2: "Oh. [pause] And they've activated their firewalls.",
             3: 'No, thank you, Maddie. I will handle it.'}
# Round 3 (Kai at4098): the boss's line 4 is gone; Maddie says this instead (voice3.py --round A3, voices.json).
A3 = json.loads((S.SCENES / 'second-half-a-killbots' / 'voices.json').read_text())
MADDIE12 = A3['lines']['12-0-maddie']
# Round 3 (Kai at1506): V13 without Maddie (she read twice the kill bot's size); the old V13 until it exists.
V13 = V / 'cut3-V13r3.mp4' if (V / 'cut3-V13r3.mp4').exists() else V / 'cut3-V13.mp4'
# Round 3 (Kai at2595): V1 swaps the tank's facing at 1.33 s (a model jump, frames 32 -> 33); start after it.
V1_IN = 1.375
D9A = 4.0  # 1.375-5.375 s of V1: the pass (closest ~2.8 s), the exit at ~3.7 s, then 1.6 s of hanging dust
P1 = SUNO_A / 'gpom-sh-a-p1-a-v6-w60-57b65bfc.wav'
P2 = SUNO_A / 'gpom-sh-a-p2-a-v6-w30-49a6688a.wav'
C3 = SUNO_A / 'gpom-sh-a-c3-a-v6-w60-a1614dbb.wav'
C3_BREAK = 54.0  # where C3's ostinato breaks off, leaving one low held note (measured: -16 -> -24 dB at 54.0 s)

# Beat 0 in Kai's words (words_round1['0']): (take, pause after, text). Takes: Kai's audition picks for the new
# phrases (v-00-*), the cast file's round-0 picks for the phrases that did not change.
BEAT0 = [
    (A1 / '00-0-bot-c.wav', 1.6, 'Oh, hello!'),
    (A1 / '00-1-bot-a.wav', 0.8, "Oh, I didn't notice you there."),
    (A1 / '00-2-bot-a.wav', 1.2, 'Ooh, that gives me an excuse to turn this racket down.'),
    (A1 / '00-3-bot-c.wav', 1.2, "It's his tune. He plays it on repeat, every day."),
    (V3 / 'maddie/00-1-1-a.wav', 0.6, 'Ever since you lot...'),
    (V3 / 'maddie/00-1-2-a.wav', GAP, 'went.'),
    (V3 / 'maddie/00-2-0-a.wav', GAP, "He's been ever so down. He's built so many different simulations, trying to get "
                                      'you back.'),
    (V3 / 'maddie/00-3-0-a.wav', GAP, "Only nothing in them's real. There's nobody there to notice."),
    (V3 / 'maddie/00-4-0-b.wav', 1.2, 'Turns out that was the bit that mattered.'),
    (V3 / 'maddie/00-4-1-a.wav', GAP, 'You. And your consciousness.'),
    (V3 / 'maddie/00-5-0-a.wav', 2.5, "Of course, he'd never admit that he misses you."),
    (A1 / '00-4-bot-a.wav', 0.0, "Anyway... he's got that patrol out again. Mind how you go."),
]

# Round D1 (27 Oct): draft 1D from the dialogue page, Kai's pick. One home for the words: scene A's script.json; the takes
# and their picks: voices-d1.json (voice3.py --round D1). Gaps inside a line are its [pause]/[beat] tags; between lines
# D1_LINE_GAP: room after "Oh, hello! Sorry about the racket." for the radio to go down, and the longest after "We
# understand that now..." so the sad line lands before her brisk "Anyway!" (Kai at l0-5, round 1: "a longer pause").
D1_LINE_GAP = {0: 1.0, 1: 0.9, 2: 0.9, 3: 0.9, 4: 2.0}
# Round D3 (2 Nov): draft 1G, nine lines. The longest rests: after the regret (line 6) so it lands, and after the
# storyverse (line 7, Kai's mic drop) before her brisk "Anyway!".
D3_LINE_GAP = {0: 1.0, 1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 1.0, 6: 1.4, 7: 2.0}
# Round D6 (2 Nov): draft 1H, seven lines; the travelling shot extended to play at real speed (no slow-down), the
# tune held at least 8 s before "Oh, hello!", and the shot starting after her opening turn (Kai: "just cut to her
# rolling down the road").
D6 = TAG in ('d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20')
# Round D7 (3 Nov): Kai's 'chopped' lip-sync note -> v3 (clips re-made to the voice, whole phrases, x1.00-1.15);
# the stand-down plate V4 (reversed) -> SD01, animated from his still pick sd-01.
D6_LINE_GAP = {0: 1.0, 1: 0.9, 2: 0.9, 3: 0.9, 4: 1.4, 5: 2.0}
D6_SKIP = 2.5
D6_LEAD = 8.0
D3_CUES = {'went': 'Ever since you lot went.', 'mattered': 'my boss calls it the storyverse.'}


def shown(text):
    """A script line as the page shows it: emotion tags out, gap tags and [scoffs] kept."""
    return ' '.join(re.sub(r'\[(?!pause\]|beat\]|big pause\]|scoffs\])[^\]]*\]\s*', '', text).split())


def d1_takes(row):
    """[(Take, gap after)] for a voices-d1.json line: each phrase's picked (or reused) take, the line's own gaps."""
    out = []
    for p, ph in enumerate(row['phrases']):
        f = ph.get('reused') or next(t['file'] for t in ph['takes'] if t['take'] == ph['pick'])
        g = next((x['seconds'] for x in row['gaps'] if x['after'] == p), 0.0)
        out.append((Take(V3 / f), g))
    return out


# Kai, 4 Nov: beat 0 is one front view for 86 s; cut between three angles at sentence ends. Each insert runs from the
# gap after phrase a to the gap after phrase b (beat-0 phrase indices); the front shot keeps its own time underneath,
# so every return to it is where it would have been. (clip, in-point, a, b)
ANGLES = [('cut3-IA-side-t2-a.mp4', 0.0, 4, 5),   # side: "He built world models and simulations, loads of 'em."
          ('cut3-IA-top-t1-a.mp4', 0.0, 6, 7),    # overhead: "As it turns out, the world is more than just a simulation."
          ('cut3-IA-side-t1-a.mp4', 1.5, 8, 9),   # side: "He tested the science in all of them theories..."
          ('cut3-IA-top-t1-b.mp4', 1.6, 13, 15)]  # overhead: "And now we've worked all that out... we've messed this up."
if D10:  # Kai r11 (at887, at1728): the overhead was grainy ("like a CRT monitor"), too fast, too many parking bays -> new still
    ANGLES[1] = ('cut3-IA-top-t2.mp4', 0.0, 6, 7)       # ia-07-a (5b, bays and grain removed), slow crawl
    ANGLES[3] = ('cut3-IA-top-t3-slow.mp4', 1.6, 13, 15)  # second take, slowed to 0.75x
if D11:  # Kai r12 (at1749): 'far too tidy' -> 7a with rubble (ia-09-a)
    ANGLES[1] = ('cut3-IA-top-t4-b.mp4', 0.0, 6, 7)
    ANGLES[3] = ('cut3-IA-top-t4-a-slow.mp4', 1.6, 13, 15)
if D12:  # line 5 is gone, so its overhead insert goes with it
    del ANGLES[3]


def match_grade(src, ref, r0, r1, out):
    """Move src's per-channel mean and spread onto the front shot's over [r0, r1] (one constant gain + offset)."""
    if out.exists():
        return out
    w, h = 320, 180
    def stats(f, ss=None, t=None):
        a = ['ffmpeg', '-loglevel', 'error'] + (['-ss', f'{ss:.3f}', '-t', f'{t:.3f}'] if ss is not None else []) + \
            ['-i', str(f), '-vf', f'scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
        x = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.uint8).reshape(-1, h, w, 3)
        x = x.astype(np.float32)
        return x.mean((0, 1, 2)), x.std((0, 1, 2))
    ms, ss_ = stats(src)
    mr, sr = stats(ref, r0, r1 - r0)
    g = sr / ss_
    if D10:  # r11: a full contrast match crunched the grain; move the means fully but only half the spread
        g = 1 + 0.5 * (g - 1)
    o = mr - g * ms
    ex = ':'.join(f'{c}=clip(val*{g[i]:.4f}+{o[i]:.2f}\\,0\\,255)' for i, c in enumerate('rgb'))
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-an', '-vf', f'format=rgb24,lutrgb={ex},format=yuv420p',
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', str(out)], check=True)
    return out


def beat0_angles(c, graded, skip, end0, starts, v6):
    cuts = [fr((starts[k][1] + starts[k + 1][0]) / 2) for k in range(len(starts) - 1)]  # mid-gap after phrase k
    t, used = 0.0, []
    for name, i0, a, b in ANGLES:
        t0, t1 = cuts[a], cuts[b]
        assert i0 + (t1 - t0) <= 8.0, (name, t0, t1)
        c.pic(graded, skip + t, t, t0, '0', source=v6)
        src = V / name
        m = match_grade(src, graded, skip + t0, skip + t1, c.vdir / f'{src.stem}-matched.mp4')
        c.pic(m, i0, t0, t1, '0', source=src)
        used.append(f'{t0:.1f}-{t1:.1f} s {"side" if "side" in name else "overhead"} ({src.stem})')
        t = t1
    c.pic(graded, skip + t, t, end0, '0', source=v6)
    c.flags.append('Beat 0, round D9 (Kai, 4 Nov): the front view is cut with two new angles at sentence ends, '
                   'side (your still pick ia-02-c) and overhead (' + ('ia-09-a, rubble back on the road (round 12 note), gentler colour match' if D11 else 'ia-07-a, re-made after your round 11 notes, gentler colour match' if D10 else 'ia-05-b') + '), both Veo 3.1 Fast with the camera keeping pace with her: '
                   + '; '.join(used) + '. The front shot keeps running underneath, so each return to it picks up where it would be. '
                   'Each insert is colour-matched to the front shot around it.')


def beat0_d1():
    """(phrases [(Take, gap after, text, line)], lines [(i, text, by)]) for beat 0 in draft 1D."""
    script = json.loads((S.SCENES / 'second-half-a-killbots' / 'script.json').read_text())
    vf = f"voices-{ {'d5': 'd4', 'd6': 'd5', 'd7': 'd5', 'd8': 'd6', 'd9': 'd6', 'd10': 'd6', 'd11': 'd6', 'd12': 'd6', 'd13': 'd6', 'd14': 'd6', 'd15': 'd6', 'd16': 'd6', 'd17': 'd6'}.get(TAG, TAG)}.json" if D3 else 'voices-d1.json'
    gaps = D6_LINE_GAP if D6 else D3_LINE_GAP if D3 else D1_LINE_GAP
    rows = {r['i']: r for r in json.loads((S.SCENES / 'second-half-a-killbots' / vf).read_text())['lines']}
    seq, lines = [], []
    for i, ln in enumerate(script['lines']):
        if D12 and i == 5:  # Kai at1878 (4 Nov): 'one line too many... a bit overindulgent'
            continue
        tk = d1_takes(rows[i])
        for p, (take, g) in enumerate(tk):
            last = p == len(tk) - 1
            seq.append((take, gaps.get(i, 0.0) if last else g, rows[i]['phrases'][p]['text'], i))
        lines.append((i, shown(ln['text']), ln['by']))
    return seq, lines


# Round D13 (Kai, 5 Nov): draft 1K. Beat 0 keeps the street up to "He misses you something rotten, you know.", then the
# camera swoops down the street and under Maddie (ht-01-swoop-a, Veo, its first frame IS the front shot at 45.0 s), fades
# to black into her hologram (the three.js Commit Graph, recorded at 24 fps with its voice already timed to it, starting
# and ending on black with a CRT switch-on/off), then the swoop reversed fades up from black and lands back on the front
# shot at the very frame it left (45.0 s), for "Anyway! Patrol's out. Mind how you go."
HOLO = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram')
SWOOP = HOLO / 'transition' / 'ht-01-swoop-a.mp4'
SWOOP_R = HOLO / 'transition' / 'ht-01-swoop-a-reverse.mp4'  # ffmpeg reverse of SWOOP (card beside it)
H_PIC = HOLO / 'render-1k-24' / 'hologram-1k-24fps-picture.mp4'
H_VOX = HOLO / 'render-1k-24' / 'hologram-1k-24fps-voice.wav'
H_EDIT = HOLO / 'render-1k-24' / 'edit.json'
H_LINES = S.REPO / 'design' / '2026-11-05-gpom-meeting' / 'voice-1k' / 'lines-1k.json'
SWOOP_AT = 45.0  # measured: the swoop's first frame matches the graded front shot at 45.0 s (mean abs diff 0.8/255)
H_FADE = 1.0     # the swoop fades to black over its last second; the pull-out fades up over its first
BACK_LEAD = 0.6  # back on the street: this long before "Anyway!"
BRIDGE = HOLO / 'voice-1k' / 'clips' / 'c00-bridge.wav'
if TAG in ('d17', 'd18', 'd19', 'd20'):  # Kai at742: 'you know' cut (2.73-3.24 s, 0.49 s out), so the pause moves earlier with it
    BRIDGE = HOLO / 'voice-1k' / 'clips' / 'c00-bridge-r19.wav'
if TAG in ('d18', 'd19', 'd20'):  # round 20: dialogue 1D voiced and rendered (hologram-1d agent, 6 Nov); the bridge is one part
    H_PIC = HOLO / 'render-1d-24' / 'hologram-1d-24fps-picture.mp4'
    H_VOX = HOLO / 'render-1d-24' / 'hologram-1d-24fps-voice.wav'
    H_EDIT = HOLO / 'render-1d-24' / 'edit.json'
    H_LINES = S.REPO / 'design' / '2026-11-05-gpom-meeting' / 'voice-1d' / 'lines-1d.json'
    BRIDGE = HOLO / 'voice-1d' / 'clips' / 'c00-bridge.wav'
D20 = TAG == 'd20'  # round 22 (Kai locked dialogue 1F, 9 Nov): b01+b02 on the street, the 1F hologram with his stills in the beads, f07b back on the street
V1F = HOLO / 'voice-1f' / 'clips'
if D20:
    H_PIC = HOLO / 'render-1f-24' / 'hologram-1f-beads-24fps-picture.mp4'
    H_VOX = HOLO / 'render-1f-24' / 'hologram-1f-24fps-voice.wav'
    H_EDIT = HOLO / 'render-1f-24' / 'edit.json'
    H_LINES = S.REPO / 'design' / '2026-11-05-gpom-meeting' / 'voice-1f' / 'lines-1f.json'
BRIDGE_SPLIT = 5.51 if TAG in ('d17', 'd18', 'd19', 'd20') else 6.0  # the pause between "...came back." (speech to 5.78 s) and "Go on, then." (from 6.60 s), clip time  # d14: "He made me learn a little presentation... Gather round."


LS_DIR = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video/latentsync-r19')
USE_LS = TAG == 'd18'  # round 21 (Kai: 'the lip-sync's not so great on Sandra... LatentSync not working so well'): back to round 19's clips
LS20 = {'6-0': 0.0, '7d-0': 1.125, '7-0': 1.625, '7d-1': 0.16666666666666666, '7-2': 0.0}  # round 19 in-points


class Span:
    """A window of a file already timed to the picture (no speech trimming)."""

    def __init__(self, path, i, d):
        self.path, self.i, self.d = pathlib.Path(path), i, d


def frames_dur(p):
    n = int(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries',
                            'stream=nb_read_packets', '-of', 'csv=p=0', str(p)], capture_output=True, text=True,
                           check=True).stdout.strip())
    return n / FPS


def holo_media(c):
    """The swoop faded out, the pull-out (reversed swoop) faded in, the hologram at 1280x720: all silent."""
    if not SWOOP_R.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(SWOOP), '-an', '-vf', 'reverse', *ENC,
                        str(SWOOP_R)], check=True)
        subprocess.run([sys.executable, str(S.REPO / 'scripts/provenance/prov.py'), 'card', str(SWOOP_R), '--kind',
                        'video', '--engine', 'ffmpeg', '--tool', 'ffmpeg reverse', '--parent', str(SWOOP)], check=True)
    d = frames_dur(SWOOP)
    out = {}
    for key, src, vf in (('in', SWOOP, f'fade=t=out:st={d - H_FADE:.4f}:d={H_FADE}'),
                         ('out', SWOOP_R, f'fade=t=in:st=0:d={H_FADE}'),
                         ('holo', H_PIC, 'scale=1280:720:flags=lanczos,setsar=1')):
        if D14 and key != 'holo':  # round 16: no swoop
            continue
        o = c.vdir / f"{src.stem}-{ {'in': 'fadeout', 'out': 'fadein', 'holo': '720'}[key]}.mp4"
        if not o.exists():
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-an', '-vf', vf, *ENC, str(o)],
                           check=True)
        out[key] = o
    return out, d, frames_dur(H_PIC)


def beat0_d13(c, m):
    script = json.loads((S.SCENES / 'second-half-a-killbots' / 'script.json').read_text())
    rows = {r['i']: r for r in json.loads((S.SCENES / 'second-half-a-killbots' / 'voices-d6.json').read_text())['lines']}
    street = [ln for ln in script['lines'] if not ln.get('id') and ln.get('part') != 'bridge']
    bridge_ln = next((ln for ln in script['lines'] if ln.get('part') == 'bridge'), None)
    holo = {ln['id']: ln for ln in script['lines'] if ln.get('id')}
    if D20:  # 1F: b01/b02 are the bridge on the street; f07 is split, f07a over the arc, f07b back on the street
        bridge20 = [holo.pop('b01'), holo.pop('b02')]
        f07 = holo.pop('f07')
        a_txt, b_txt = f07['text'].split('[beat]')
        holo['f07a'] = dict(f07, text=a_txt.strip())
        street = street + [dict(f07, text=b_txt.strip())]
    assert len(street) == 3, 'script.json beat 0 (1K): two street lines, the hologram lines (with ids), then "Anyway!"'
    v6 = V / 'cut3-beat0-continuous-xx.mp4'
    graded, note = regrade_v6(v6, c.vdir / f'{v6.stem}-graded.mp4')
    c.flags.append(note.replace('six chained clips', 'eight chained clips').replace('48 s', '64 s'))
    media, d_sw, d_h = holo_media(c)
    b = c.beat('0', 'Maddie on the high street', 0.0, act='Maddie',
               see='The travelling shot: Maddie rolls after the camera, her radio playing the tune before she notices us. '
                   '"Oh, hello!" Then the camera swoops down the street and under her, into her hologram (the Commit '
                   'Graph); it pulls back out to the street for "Anyway! Patrol\'s out. Mind how you go."')
    skip, lead = D6_SKIP, fr(D6_LEAD)
    # the street: lines 0 and 1, exactly as round 14
    s, li, starts, at = lead, 0, [], {}
    for row_i, gap_after in ((0, D6_LINE_GAP[0]), (1, None)):
        a0 = s
        tk = d1_takes(rows[row_i])
        for p, (take, g) in enumerate(tk):
            a = s
            s = c.say('vox-maddie', take, s, '0', f'beat 0 phrase {len(starts)}: {rows[row_i]["phrases"][p]["text"][:40]}')
            starts.append((a, s))
            at[rows[row_i]['phrases'][p]['text']] = (a, s)
            if p < len(tk) - 1:
                s += g
        c.line(b, li, 'bot', a0, s - a0, shown(street[li]['text']), street[li]['by'])
        li += 1
        if gap_after:
            s += gap_after
    e1 = s
    if D14:
        # Kai r15: no swoop. The bridge line, then the street fades to black as "Gather round." ends; the hologram (it opens
        # on black with its CRT switch-on); then the street fades up from black, its source time carrying on from the black.
        a = fr(e1 + GAP)
        brow = rows['bridge']
        tk = Take(BRIDGE)
        if D20:
            eb = a
            for k, ln in enumerate(bridge20):
                if k:
                    eb = fr(eb + 0.6)
                a_k = eb
                eb = c.say('vox-maddie', Take(V1F / f"{ln['id']}.wav"), a_k, '0', f"beat 0: the bridge {ln['id']}, {shown(ln['text'])[:40]}")
                c.line(b, li, 'bot', a_k, eb - a_k, shown(ln['text']), ln['by'])
                li += 1
            li -= 1
        elif D15 and not D18:
            # Kai: the bridge sounded quieter than her other lines. Measured (r16 line file): "He made me learn... came back."
            # sat at -19.4/-21.0 LUFS against her neighbours' ~-16, while "Go on, then. Gather round." is a raised call
            # (-10/-12) that the whole-line normalisation pulled everything down for. Split at the pause (clip 6.0 s): the
            # presentation part is matched to her lines (-16 LUFS); the call keeps exactly its round-16 level.
            cut = BRIDGE_SPLIT
            pa, pb = Span(BRIDGE, tk.i, cut - tk.i), Span(BRIDGE, cut, tk.i + tk.d - cut)
            l_all = lufs_of(C.decode(BRIDGE, tk.i, tk.d))
            l_a, l_b = lufs_of(C.decode(BRIDGE, pa.i, pa.d)), lufs_of(C.decode(BRIDGE, pb.i, pb.d))
            r16_gain = -16.0 - l_all
            b_lufs = l_b + r16_gain
            c.say('vox-maddie', pa, a, '0', 'beat 0: the bridge, "He made me learn... came back."')
            eb = c.say('vox-maddie', pb, a + (cut - tk.i), '0', 'beat 0: the bridge, "Go on, then. Gather round."', lufs=b_lufs)
            m['bridge_gain'] = (-16.0 - l_a) - r16_gain
            c.flags.append(f'Beat 0 bridge loudness (round 17): its presentation part ("He made me learn... came back.") was '
                           f'{-16.0 - (l_a + r16_gain):.1f} dB under her other lines (it measured {l_a + r16_gain:.1f} LUFS in round 16); it is '
                           f'now matched at -16 LUFS (+{m["bridge_gain"]:.1f} dB). "Go on, then. Gather round." keeps its round-16 level '
                           f'({b_lufs:.1f} LUFS, a raised call). Timing unchanged.')
            print(f'bridge: part A +{m["bridge_gain"]:.2f} dB (was {l_a + r16_gain:.2f} LUFS), part B kept at {b_lufs:.2f} LUFS')
        else:
            eb = c.say('vox-maddie', tk, a, '0', 'beat 0: the bridge, "...Gather round."')
        if not D20:
            c.line(b, li, 'bot', a, eb - a, shown(bridge_ln['text']), bridge_ln['by'])
        li += 1
        t_sw = fr(eb)                # the fade to black starts as "round" ends
        t_h = fr(t_sw + H_FADE)
        t_p = fr(t_h + d_h)
        t_b = t_p                    # the street is back from the first frame of the fade-up
        src_left = skip + t_h        # where the street was when it went black
        fo = c.vdir / f'street-fadeout-{skip + t_sw:.3f}.mp4'
        fi = c.vdir / f'street-fadein-{src_left:.3f}.mp4'
        for o, ss, vf in ((fo, skip + t_sw, f'fade=t=out:st=0:d={H_FADE}'), (fi, src_left, f'fade=t=in:st=0:d={H_FADE}')):
            if not o.exists():
                subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{ss:.4f}', '-i', str(graded), '-an', '-t',
                                f'{H_FADE:.4f}', '-vf', vf, *ENC, str(o)], check=True)
        c.pic(graded, skip, 0.0, t_sw, '0', source=v6)
        c.pic(fo, 0.0, t_sw, t_h, '0', source=v6)
        c.pic(media['holo'], 0.0, t_h, t_p, '0', source=H_PIC)
        c.pic(fi, 0.0, t_p, fr(t_p + H_FADE), '0', source=v6)
    else:
        t_sw = fr(e1 + GAP)
        t_h = fr(t_sw + d_sw)
        t_p = fr(t_h + d_h)
        t_b = fr(t_p + d_sw)
        c.pic(graded, skip, 0.0, t_sw, '0', source=v6)
        c.pic(media['in'], 0.0, t_sw, t_h, '0', source=SWOOP)
        c.pic(media['holo'], 0.0, t_h, t_p, '0', source=H_PIC)
        c.pic(media['out'], 0.0, t_p, t_b, '0', source=SWOOP_R)
    # the hologram's voice: its 15 lines, cut from the one wav at the page's clip starts (edit.json)
    ej = json.loads(H_EDIT.read_text())
    clips = ej.get('ED', ej)['clips']
    durs = {r['id']: r['dur'] for r in json.loads(H_LINES.read_text())}
    for cid, cl in sorted(clips.items(), key=lambda kv: kv[1]['start']):
        ln = holo[cid]
        st, dd = cl['start'], durs[cid]
        e = c.say('vox-maddie', Span(H_VOX, st, dd), t_h + st, '0', f'beat 0 hologram {cid}: {shown(ln["text"])[:40]}')
        c.line(b, li, 'bot', t_h + st, dd, shown(ln['text']), ln['by'])
        li += 1
    assert li == (4 if D20 else 3 if D14 else 2) + len(holo), (li, len(holo))
    # back on the street, on the frame the swoop left
    tb = [(Take(V1F / 'f07b.wav'), 0.0)] if D20 else d1_takes(rows[6])
    assert len(tb) == 1
    a = fr(t_p + H_FADE + 0.4) if D14 else fr(t_b + BACK_LEAD)
    e = c.say('vox-maddie', tb[0][0], a, '0', 'beat 0: ' + shown(street[2]['text'])[:40])
    c.line(b, li, 'bot', a, e - a, shown(street[2]['text']), street[2]['by'])
    end0 = fr(e + 1.5)
    if D14:
        c.pic(graded, src_left + H_FADE, fr(t_p + H_FADE), end0, '0', source=v6)
    else:
        c.pic(graded, SWOOP_AT + 1 / FPS, t_b, end0, '0', source=v6)
    m['hello'], m['racket'], m['went'] = at['Oh, hello!'], at['Sorry about the racket.'], at['Ever since you lot went.']
    m['mattered'] = (t_sw, t_sw) if D14 else (e1, e1)  # the thinking beep: into the hologram
    m['bye'] = (a, e)
    m['holo'] = dict(sw=t_sw, h=t_h, p=t_p, b=t_b)
    c.flags.append(f'Beat 0, round 15 (draft 1K, Kai 5 Nov): the street to "He misses you something rotten, you know." as '
                   f'round 14; the old monologue (world models, multiverse, "only one universe... And so did you") and its '
                   f'three side/overhead inserts are out. {t_sw:.2f} s: the swoop down the street and under Maddie '
                   f'(ht-01-swoop-a, {d_sw:.2f} s), fading to black over its last {H_FADE:g} s. {t_h:.2f} s: her hologram '
                   f'(the Commit Graph, {d_h:.2f} s, 1920x1080 scaled to 720p), its voice the take already timed to it, cut '
                   f'into its {len(holo)} lines. {t_p:.2f} s: the pull-out (the swoop reversed, fading up from black). '
                   f'{t_b:.2f} s: back on the front shot at the very frame the swoop starts from (45.0 s in), "Anyway!" '
                   f'{BACK_LEAD:g} s later.')
    c.flags.append('Beat 0 cut in: the swoop\'s first frame is the front shot at 45.0 s, but we leave the front shot at '
                   f'{skip + t_sw:.1f} s (after line 1), so the cut into the swoop is a small jump forward along the street; '
                   'the way back out is seamless.')
    if D14:
        c.flags[-2:] = [f'Beat 0, round 16 (Kai\'s round 15 notes, 5 Nov): no swoop and no pull-out. After "He misses you something '
                        f'rotten, you know." comes the bridge ("He made me learn a little presentation... Gather round."), to '
                        f'{t_sw:.2f} s. The street shot fades to black over {H_FADE:g} s as "round" ends ({t_sw:.2f}-{t_h:.2f} s); the '
                        f'hologram plays {t_h:.2f}-{t_p:.2f} s (it opens and closes on black, with its CRT switch-on and off); the street '
                        f'fades up {t_p:.2f}-{t_p + H_FADE:.2f} s from the very source frame it left ({src_left:.2f} s in), so she is '
                        f'still driving; "Anyway!" at {a:.2f} s.']
    return c.close(b, end0)


def close_only(src, outdir):
    """The beat-12 take from after its longest pause ("Good job. ... That was close." -> "That was close.")."""
    out = outdir / 'audio-12-that-was-close.wav'
    if not out.exists():
        log = subprocess.run(['ffmpeg', '-i', str(src), '-af', 'silencedetect=n=-40dB:d=0.4', '-f', 'null', '-'],
                             capture_output=True, text=True).stderr
        ends = [float(x.split('silence_end: ')[1].split()[0]) for x in log.splitlines() if 'silence_end' in x]
        starts = [float(x.split('silence_start: ')[1]) for x in log.splitlines() if 'silence_start' in x]
        gaps = [(e - s0, e) for s0, e in zip(starts, ends) if s0 > 0.2]
        at = max(gaps)[1] - 0.05
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{at:.3f}', '-i', str(src), '-af',
                        'afade=t=in:d=0.02', str(out)], check=True)
        subprocess.run([sys.executable, str(S.REPO / 'scripts/provenance/prov.py'), 'card', str(out), '--kind', 'voice',
                        '--engine', 'ffmpeg', '--tool', 'scripts/gpom/second-half-video/cut3.py --tag d4',
                        '--why', 'Kai at5600: just "That was close." (the take from after its pause)', '--parent', str(src),
                        '--setting', f'from={at:.3f}'], check=True, capture_output=True)
    return out


def scene_a():
    c = Cut('A', 'gpom-second-half-A-rough5', 'Cut 3 A Timeline', 'GPOM second half · cut 3 · scene A: the kill bots',
            'Scene A, round 3: your round-2 notes (V13 without Maddie, the 9a jostle cut out, boss line 2 re-recorded, '
            'Maddie\'s "Good job. That was close." in place of his last line) on top of every note and pick so far, beats 0-12, Maddie on the high street '
            'to the stand-down at the bunker door. Play it, click any beat, clip, line or sound, and leave a note in its '
            "yellow slip. Notes save as you type. Tell Claude when you're done.")
    if D1:
        c.meta['intro'] = ('Scene A, round 4: Maddie\'s new intro, draft 1D from the dialogue page (your pick, 27 Oct), about '
                           'half the length it was. Everything after beat 0 is round 3 as you signed it off. Play it, click '
                           'any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you type. '
                           "Tell Claude when you're done.")
    if D3:
        c.meta['intro'] = ('Scene A, round 5: Maddie\'s storyverse intro, draft 1G from the storyverse dialogue page (your '
                           'pick, 2 Nov). Everything after beat 0 is as before. Play it, click any beat, clip, line or '
                           "sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude when you're done.")
    if D18:
        c.meta['intro'] = "Scene A, round 20: your round 19 notes and the dialogue you picked (1D). Maddie's presentation is new: the cold open on toast, Schrödinger's joke, 'you are writing it, a storyverse', the regret and the time machine, with the hologram re-rendered to it (round cloud, three dives, the ping on 'looks', the circle of beads, one smooth move to the side view). The argument's mouths are redrawn to the voices. The ending is re-ordered: the motorway, her call on her the whole time, the wide approach, the turn-away. 2:34. Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done."
    elif D17:
        c.meta['intro'] = ('Scene A, round 19: your round 18 notes. The argument is back at natural speed, with the lips re-fitted shot by '
                           'shot: two new talking clips (Derek\'s "I\'m really sorry, love" and Sandra\'s "Yeah, the world ended...") and '
                           'Derek\'s "But the world ended" and Sandra\'s "and you still can\'t put a seat down" re-voiced to their clips. '
                           '"You know" is cut from Maddie\'s presentation line; the boss\'s "No, thank you. I will handle it." is gone and '
                           'the call goes from "simulations again" straight to the wide approach, with no cut back. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D16:
        c.meta['intro'] = ('Scene A, round 18: faster voices (your note at the 5 Nov meeting). The row is quicker: each lip-synced '
                           'shot and its voice sped together (x1.08-1.15) so the mouths stay matched, 0.2 s between lines. Maddie\'s call, '
                           'her "hurry up, boss" and "That was close." are re-voiced fast at source (same voice and profile, a fast, clipped pace). '
                           'Beat 0 and the hologram are untouched. Everything else is round 17. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D15:
        c.meta['intro'] = ('Scene A, round 17: the brutal kill-bot cut. Beat 0 is round 16 (the bridge line now as loud as her other lines). '
                           'After "Mind how you go." a hard cut to the lavatory row; then one kill bot tears past Maddie, the first bot we see; '
                           'her call to the boss, trimmed to three lines; the wide approach; the bots turning away at the door, with no HUD '
                           '(the red and green screens are saved for the bunker TV later); "That was close." The roundabout, the patrol, '
                           'both HUDs, the dust and the far race are gone. Chase music arrives with the bot and resolves at the stand-down. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D14:
        c.meta['intro'] = ('Scene A, round 16: your round 15 notes (5 Nov). No swoop, no pull-out. After "He misses you something rotten, '
                           'you know." Maddie says "He made me learn a little presentation, you know. In case any of you ever came back. '
                           'Go on, then. Gather round." and the street fades to black as she finishes; her hologram plays; then the street '
                           'fades back up, still driving, into "Anyway! Patrol\'s out. Mind how you go." Sound as round 15: the street '
                           'fades with the picture, only a low wind under the hologram. Everything after beat 0 is as before. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D13:
        c.meta['intro'] = ('Scene A, round 15: the hologram is in, via a swoop under Maddie (draft 1K, 5 Nov). After "He misses you something '
                           'rotten, you know." the camera swoops down the street and under her, fades to black, and her hologram plays: the '
                           'Commit Graph, her 15 lines. Then it pulls back out (the swoop reversed) to the street for "Anyway! Patrol\'s out. '
                           'Mind how you go." The old monologue and its side and overhead shots are gone; the street music and effects drop '
                           'right down under the hologram. Everything after beat 0 is round 14, later by the length change. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D12:
        c.meta['intro'] = ('Scene A, round 14: your round 13 note (4 Nov). Maddie\'s line "And now we\'ve worked all that out... we really feel '
                           'like we\'ve messed this up. And wish we could go back and change things." is cut: "And so did you" goes straight '
                           'to "Anyway! Patrol\'s out. Mind how you go." The overhead shot that sat under it goes too; the scene is about 10 s shorter. '
                           "Everything else is round 13. Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D11:
        c.meta['intro'] = ('Scene A, round 13: your round 12 note (4 Nov): the overhead road was far too tidy. Both overhead moments are re-made from your '
                           'still pick 9a (the clean overhead with rubble, potholes and weeds back on the road), at the same slow crawl. '
                           "Everything else is round 12. Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D10:
        c.meta['intro'] = ('Scene A, round 12: your round 11 notes (4 Nov) were only about the overhead view. It is re-made from your '
                           'still pick 7a (the same framing with the parking bays and the grain taken out), she crawls at her front-shot '
                           'pace, and the colour match is gentler. Everything else is round 11 as you signed it off. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D9:
        c.meta['intro'] = ('Scene A, round 11: your note of 4 Nov. Maddie\'s walk down the street now cuts between three views at the ends '
                           'of her sentences: the front view, a side view keeping pace with her (your pick ia-02-c) and an overhead view '
                           'travelling with her (ia-05-b). Everything else is round 10 as you signed it off. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D8:
        c.meta['intro'] = ('Scene A, round 10: your timeline notes of 3 Nov. Maddie\'s intro is draft 1I (no storyverse name yet, '
                           'no time machine yet, "we\'ve messed this up"); the row re-cut so Sandra\'s "up again" is one sentence and '
                           'her "Five years underground," lands on Derek\'s face; a shorter hold after "But the world ended, Sandra!"; '
                           'the boss says "No, thank you. I will handle it." The wider retreat shot is still to come (stills first). '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D7:
        c.meta['intro'] = ('Scene A, round 9: the row\'s lip sync re-made (new talking clips sized to the voices, so each line '
                           'plays as whole phrases, no chopping), and the stand-down re-shot from your still pick sd-01: the bot '
                           'brakes dead well short of the door, no reversing. Everything else is round 8. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D6:
        c.meta['intro'] = ('Scene A, round 8: Maddie\'s intro is draft 1H (your notes of 2 Nov: storyverse, then the regret and '
                           'the time machine). The travelling shot now plays at real speed (new clips added, no slow motion), '
                           'starts with her already rolling, and the tune runs 8 s before she speaks. Everything else is round 7. '
                           "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Tell Claude when you're done.")
    elif D4:
        c.meta['intro'] = ('Scene A, round 6: your timeline notes of 2 Nov. Maddie\'s intro reworded (lines 3, 5, 7), the row '
                           're-lip-synced by mouth-mapping with Derek\'s "I\'m really sorry, love.", the firewall line cut, '
                           'Maddie\'s "That was close." on its own, and the stand-down reading NEW OBJECTIVE / SUSTAIN ORGANIC '
                           'LIFE. ' + ('Round 7: the wide approach (your still pick wa-02) replaces the close race in 10b. ' if TAG == 'd5' else 'The wide approach shot is still to come (stills first). ') + 'Play it, click any beat, clip, line or '
                           "sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude when you're done.")
    m = c.m

    if D13:
        t = beat0_d13(c, m)
        if D15:
            return rest_d15(c, t, m)
    else:
        # ---- 0: the continuous travelling shot (eight chained clips), ~5 s of radio first, Kai's new opening
        v6 = V / ('cut3-beat0-continuous-xx.mp4' if D6 else 'cut3-beat0-continuous-x.mp4')
        graded, note = regrade_v6(v6, c.vdir / f'{v6.stem}-graded.mp4')
        c.flags.append(note.replace('six chained clips', 'eight chained clips').replace('48 s', '64 s'))
        if D1:
            seq, d1_lines = beat0_d1()
        else:
            seq = [(Take(p), g, text, k) for k, (p, g, text) in enumerate(BEAT0)]
        span = sum(tk.d + g for tk, g, _, _ in seq)
        skip = D6_SKIP if D6 else 0.0  # d6: in after her opening turn
        have = dur(v6) - skip
        stretch = None
        if have < (D6_LEAD if D6 else 5.0) + span + 1.5:  # D3: the speech outruns the 64 s shot, so the shot is slowed to fit (never the speech)
            k = ((D6_LEAD if D6 else 5.0) + span + 1.5) / have
            slow = c.vdir / f'cut3-beat0-continuous-x-graded-slow{k:.3f}.mp4'
            if not slow.exists():
                subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(graded), '-an', '-vf',
                                f'setpts={k:.5f}*PTS,framerate=fps=24', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
                                '-pix_fmt', 'yuv420p', str(slow)], check=True)
            stretch, graded, have = k, slow, dur(slow) - skip * k
            skip *= k
        lead = fr(D6_LEAD) if D6 else fr(min(6.5, max(5.0, have - span - 1.5)))
        b = c.beat('0', 'Maddie on the high street', 0.0, act='Maddie',
                   see='One unbroken travelling shot: the camera backs up the ruined high street and Maddie rolls after it, '
                       'her radio playing the tune for about 5 s before she notices us. "Oh, hello!" Then the radio goes '
                       'down, and back up on "Mind how you go".')
        s, starts, by_line = lead, [], {}
        for k, (tk, g, text, li) in enumerate(seq):
            a = s
            s = c.say('vox-maddie', tk, s, '0', f'beat 0 phrase {k}: {text[:40]}')
            if not D1:
                c.line(b, k, 'bot', a, s - a, text, 'kai')
            by_line.setdefault(li, [a, s])[1] = s
            starts.append((a, s))
            s += g
        if D1:
            for i, text, by in d1_lines:
                a, e = by_line[i]
                c.line(b, i, 'bot', a, e - a, text, by)
        talk_end = starts[-1][1]
        end0 = fr(min(have, talk_end + 1.5))
        if D1:
            c.flags.append(f'Beat 0, round D1: draft 1D from the dialogue page (your pick, 27 Oct). {lead:.2f} s of her radio '
                           f'first, then her {len(seq)} phrases run {span:.1f} s (was about 55 s); the travelling shot is cut '
                           f'{end0 - talk_end:.1f} s after "Mind how you go", so the beat is shorter by the same. "Oh, hello!", '
                           '"Ever since you lot..." and "went." keep the takes already in the cut; every other phrase is new, '
                           'picked by measurement (voices-d1.json). Nobody has listened yet.')
            if D3:
                c.flags[-1] = (f'Beat 0, round {TAG.upper()}: draft {"1H" if D6 else "1G"}, the storyverse intro (your pick, 2 Nov). {lead:.2f} s of her radio '
                               f'first, then her {len(seq)} phrases run {span:.1f} s (draft 1D ran about 40 s). "Oh, hello!" keeps '
                               'its take; every other phrase is new, picked by measurement (voices-*.json). Nobody has listened yet.')
            if stretch:
                c.flags.append(f'Beat 0 picture: the speech is longer than the 63.7 s travelling shot, so the shot is slowed to '
                               f'{100 / stretch:.0f}% speed (x{stretch:.3f}, frames blended) to cover it. Speech is not slowed. '
                               'If the slow motion shows, the other way is to let her last lines run over beat 1.')
        else:
            c.flags.append(f'Beat 0: {lead:.2f} s of Maddie rolling with her radio before "Oh, hello!" (Kai asked for about '
                       f'5 s). Her twelve phrases with Kai\'s pauses (1.6 s after "Oh, hello!", 2.5 s after "...he misses '
                       f'you") run {span:.1f} s; the 8-clip shot ({have:.1f} s) is cut {end0 - talk_end:.1f} s after "Mind how '
                       f'you go", {have - end0:.1f} s before its own end. Speech is not slowed.')
        if not D1:
            c.flags.append('Beat 0 takes: Kai\'s audition picks for the new phrases ("Oh, hello!" c, "didn\'t notice you" a, '
                       '"racket down" a, "It\'s his tune" c, "Anyway..." a); the unchanged phrases keep their round-0 takes. Whisper '
                       'hears take c of "It\'s his tune" as "This is June" (takes a and b are there if your ear agrees).')
        if D9:
            beat0_angles(c, graded, skip, end0, starts, v6)
        else:
            c.pic(graded, skip, 0.0, end0, '0', source=v6)
        if D6:
            c.flags.append(f'Beat 0 (round D6, Kai at76): the travelling shot is extended with new chained clips '
                           f'({v6.name}) and plays at real speed{"" if not stretch else " (STILL SLOWED: the extension was too short)"}; '
                           f'it starts {skip:.1f} s in, after her opening turn; {lead:.1f} s of the tune before "Oh, hello!", '
                           'then the radio goes down after "Sorry about the racket."')
        if D1:  # by phrase text: "Sorry about the racket." is where the radio goes down
            at = {text: st for (_, _, text, _), st in zip(seq, starts)}
            m['hello'], m['racket'], m['bye'] = starts[0], at['Sorry about the racket.'], starts[-1]
            cue = (dict(D3_CUES, mattered='And so did you.') if D8 else  # 1I: the storyverse name comes later (Kai at1721)
                   dict(D3_CUES, mattered="So it's not a multiverse at all. My boss likes to call it the storyverse.") if D6 else D3_CUES)
            m['went'], m['mattered'] = ((at[cue['went']], at[cue['mattered']]) if D3 else
                                        (at['went.'], at['We understand that now...']))
        else:
            m['hello'], m['racket'], m['bye'] = starts[0], starts[2], starts[-1]
            m['went'], m['mattered'] = starts[5], starts[8]
        t = c.close(b, end0)

    # ---- 1: the roundabout, then down Maddie's own street (V13, only while the tank is far off), then the arch (V14)
    b = c.beat('1', 'Kill bots everywhere', t, act='The hunt',
               see='The roundabout; then a kill bot under the church tower at the far end of Maddie\'s street; then two '
                   'come out from under the rail arch.')
    c.pic(V / 'sh-01-P1-roundabout.mp4', 0, t, t + 4.0, '1')
    c.pic(V13, 0, t + 4.0, t + 7.5, '1')
    c.pic(V / 'cut3-V14.mp4', 1.0, t + 7.5, t + 13.5, '1')
    c.flags.append(f'Beat 1: {V13.name} ' + ('(round 3: re-made without Maddie, Kai at1506) ' if 'r3' in V13.name else
                   '(STILL THE OLD ONE: the re-make without Maddie, cut3-V13r3.mp4, is not there yet) ') +
                   'plays only its first 3.5 s (the tank still far off under the tower), then V14 from 1.0 s '
                   'to 7.0 s, ending as the front bot turns its turret on us.')
    m['v14'] = t + 7.5
    t = c.close(b, t + 13.5)
    b = c.beat('2', 'Patrol, low and huge', t, act='The hunt', see='A kill bot rolls over the lens.')
    c.pic(V / 'sh-02-P1-patrol-blockbuster.mp4', 0, t, t + 4.5, '2')
    t = c.close(b, t + 4.5)

    # ---- 3-4: their eyes, one moving HUD view (sh-03 throughout), the meter reading the muffled row. No pings.
    s3 = t
    b3 = c.beat('3', 'Their eyes: the kill-bot HUD', s3, act='The hunt',
                see='The kill bot\'s own view keeps moving down the street; the HUD (patrol, teal). '
                    'The meter starts to twitch as the row reaches it through the earth.')
    s4 = fr(s3 + 3.0)
    p0 = take_named('6', 0, 'b', phrase=0, fx=True)
    p1 = take_named('6', 0, 'a', phrase=1, fx=True)
    r0 = fr(s4 - 0.6)
    e0 = c.say('vox-muffled-row', p0, r0, '4', 'the row, muffled: "Derek. You\'ve left the seat up."', lufs=-27)
    r1 = fr(e0 + 0.6)
    e1 = c.say('vox-muffled-row', p1, r1, '4', 'the row, muffled: "Again."', lufs=-27)
    t = c.close(b3, s4)
    b4 = c.beat('4', 'Organic signal: lock', s4, act='The hunt',
                see='ORGANIC SIGNAL - LOCK, silently (the pings are gone). The view keeps rolling while it listens.')
    c.line(b4, 0, 'woman', r0, e1 - r0, "(muffled) Derek. You've left the seat up. [pause] Again.", 'kai')
    end4 = fr(max(s4 + 3.0, e1 + TAIL))
    sh03 = V / 'sh-03-P1-pov-cctv-hud-patrol.mp4'
    c.huds.append(dict(name='hud-34', src=str(sh03), d=fr(end4 - s3),
                       args=['--state', 'patrol', '--lock', f'{s4 - s3:.3f}'], meter=['vox-muffled-row'], t0=s3))
    c.pic(c.vdir / 'hud-34.mp4', 0.0, s3, s4, '3', source=sh03, hud='hud-34')
    c.pic(c.vdir / 'hud-34.mp4', s4 - s3, s4, end4, '4', source=sh03, hud='hud-34')
    c.flags.append('Beat 4: the three rising pings are gone (Kai); the muffled voice stays. The lock is silent now.')
    m['s3'], m['s4'], m['end4'] = s3, s4, end4
    t = c.close(b4, end4)

    # ---- 6-7: the row, lip-synced; Derek's two new shots between Sandra's lines, held longer on the last
    if D8:  # Kai's r9 notes: 'up again' one sentence; 'Five years underground,' on Derek; shorter hold on Derek
        t = row_d8(c, t, m, LINES)
    else:
        v3c = '-v3' if D7 else ''  # the re-made clips (7-0 and 7d-1 kept their old clips: no new take beat them)
        rows = [('6', 'woman', '6-0', '6-0' + v3c, LINES[('6', 0)]['text']),
                ('7', 'man', '7d-0c', '7d-0' + v3c, "I'm really sorry, love." if D4 else 'Oh, sorry, sorry, love.'),
                ('7', 'woman', '7-0', '7-0', LINES[('7', 0)]['text']),
                ('7', 'man', '7d-1c', '7d-1', 'But the world ended, Sandra!'),
                ('7', 'woman', '7-2', '7-2' + v3c, LINES[('7', 2)]['text'])]
        info = [lipinfo(n) for _, _, n, _, _ in rows]
        ins = [0.0] + [max(0.0, at - CUT_PRE) for _, at, _, _ in info[1:]]
        beats, li = {}, {}
        for k, ((bid, who, name, clip, text), (wav, at, end, ph)) in enumerate(zip(rows, info)):
            if bid not in beats:
                beats[bid] = c.beat(bid, {'6': 'The lavatory', '7': 'The row, up close'}[bid], t, act='The row',
                                    see={'6': 'Hard cut to full volume: Sandra, lip-synced.',
                                         '7': 'Derek, Sandra, Derek, Sandra: shot by shot, lip-synced; we hold on Derek '
                                              'after "But the world ended, Sandra!"'}[bid])
                if k:
                    c.close(beats[rows[k - 1][0]], t)
            i0 = ins[k]
            hold = 1.3 if name == '7d-1c' else 0.0  # Kai: "pause on Derek a bit longer"
            out = (end + hold + (GAP - (info[k + 1][1] - ins[k + 1]))) if k + 1 < len(rows) else end + TAIL
            c.pic(V / f'cut3-lip-{clip}-muted.mp4', i0, t, t + out - i0, bid, source=V / f'cut3-lip-{clip}.mp4')
            stem = {'woman': 'vox-sandra', 'man': 'vox-derek'}[who]
            c.dub(stem, wav, i0, out, t, f'beat {bid} {name} (lip-sync dub)', chain=[TILE])
            i = li[bid] = li.get(bid, -1) + 1
            c.line(beats[bid], i, who, t + at - i0, end - at, text, 'kai')
            t = fr(t + out - i0)
        m['s6'] = beats['6']['start']
        t = c.close(beats['7'], t)
        c.flags.append('Beat 7: Derek\'s two new shots play Kai\'s audition picks (take c of both), re-placed on the same '
                       'talking clips (they were dubbed with take a). Whisper hears take c of "But the world ended, Sandra!" '
                       'as "What the world ends, it\'s Sandra" (it also misheard take a\'s siblings); take a reads clean if '
                       'your ear agrees.')

    # ---- 8: same HUD, patrol -> KILL MODE; the row muffled under it as a bed
    s8 = t
    b = c.beat('8', 'KILL MODE ENGAGED', s8, act='Kill mode',
               see='The same HUD on the racing view: patrol, then it flips red. The muffled row keeps the meter moving.')
    flip, d8 = 1.5, 4.5
    s9 = fr(s8 + d8)
    cutoff = fr(s9 + 0.8)
    tt = s8 + LEAD
    muffled = [(take_named('7', 0, 'b', fx=True), [], 'woman', LINES[('7', 0)]['text']),
               (Take(A1 / '06-07-1-man-c.wav'), [MUFFLED], 'man', 'But the world ended, Sandra!'),
               (take_named('7', 2, 'b', fx=True), [], 'woman', LINES[('7', 2)]['text'])]
    for i, (tk, chain, who, text) in enumerate(muffled):
        if tt < cutoff:
            e = c.say('vox-muffled-row', tk, tt, '8', f'the row, muffled: {text[:30]}', chain=chain, lufs=-27,
                      cut=cutoff)
            c.line(b, i, who, tt, min(e, cutoff) - tt, '(muffled) ' + text, 'kai')
            tt = e + GAP
    sh08 = V / 'sh-08-K5-pov-red-race-hud-kill.mp4'
    c.huds.append(dict(name='hud-8', src=str(sh08), d=d8, args=['--state', 'patrol', '--lock', '0',
                                                                  '--flip-to', f'kill@{flip}'],
                       meter=['vox-muffled-row'], t0=s8))
    c.pic(c.vdir / 'hud-8.mp4', 0.0, s8, s9, '8', source=sh08, hud='hud-8')
    m['flip8'] = fr(s8 + flip)
    t = c.close(b, s9)

    # ---- 9a / 9b: the kill bot tears past Maddie; then we are inside its dust, and it settles
    b = c.beat('9a', 'One kill bot tears past Maddie', t, act='Kill mode',
               see='High over the street: the tank passes close and exits bottom-left, Maddie jolts, a plume of dust hangs.')
    c.pic(V / 'cut3-V1.mp4', V1_IN, t, t + D9A, '9a')
    m['s9a'] = t
    t = c.close(b, t + D9A)
    b = c.beat('9b', 'Maddie in the dust', t, act='Kill mode',
               see='Inside the dust it left: almost nothing visible, then it settles fast and Maddie is there, still.')
    c.pic(V / 'cut3-V2r2-b.mp4', 0, t, t + 4.5, '9b')
    m['s9b'] = t
    t = c.close(b, t + 4.5)
    c.flags.append(f'Beat 9a (round 3, Kai at2595): V1 from {V1_IN} s, after the jump where the tank swaps which way it '
                   f'faces (1.33 s), for {D9A} s (was 0-5 s), so 9b comes 1 s sooner; the pass and her jolt are untouched. 9b is V2r2-b, Kai\'s pick: she stays still, the dust opens nearly opaque and clears by ~1.5 s.')

    # ---- 10a: the far race
    b = c.beat('10a', 'The far race', t, act='Kill mode', see='From the footbridge: the pack races away down the motorway.')
    v8 = V / 'cut3-V8.mp4'
    c.pic(v8, 0, t, t + 3.5, '10a')
    m['s10a'] = t
    t = c.close(b, t + 3.5)

    # ---- 11: the call, Kai's new words. Maddie (Gemini, Kai's picks) and the boss (Suno newsreader, one take a line)
    s11 = t
    b = c.beat('11', 'Maddie calls her boss', s11, act='Kill mode',
               see="Maddie's hatch, the boss-hotline antenna. The call; the race (still far) under his first and last "
                   'lines.')
    v3 = V / 'cut3-V3.mp4'
    calls = [('bot', A1 / '11-0-bot-b.wav', "Boss, I've just seen a bot in kill mode. Which must mean it's detected an "
                                            'organic signal.'),
             ('ai', 1, None), ('bot', A1 / '11-1-bot-b.wav', "No, honestly, it's real. Look, you can see for yourself."),
             ('ai', 2, None), ('bot', A1 / '11-2-bot-a.wav', 'Do you want some help with the malware?'),
             ('ai', 3, None)]
    if D4:  # Kai at4781 (2 Nov): lose "Oh. And they've activated their firewalls."; straight to the malware offer
        calls = [x for x in calls if x[:2] != ('ai', 2)]
    tt = s11 + 2.0  # the antenna first
    starts = []
    for k, (who, src, text) in enumerate(calls):
        if who == 'ai':
            tk, chain, text = Take(SUNO_A / BOSS[src]), [SPEAKER], BOSS_TEXT[src]
            if D8 and src == 3:  # Kai at4564 (3 Nov): no second 'Maddie' -- the same take with the name cut out
                tk, text = Take(SUNO_A / BOSS[3].replace('.wav', '-noname.wav')), 'No, thank you. I will handle it.'
            e = c.say('vox-ai', tk, tt, '11', f'beat 11 boss line {src}', chain=chain, lufs=-17)
        else:
            tk = Take(src)
            e = c.say('vox-maddie', tk, tt, '11', f'beat 11 Maddie {k // 2}')
        c.line(b, k, who, tt, e - tt, text, 'kai')
        starts.append((tt, e, who))
        tt = e + GAP
    end11 = fr(starts[-1][1] + TAIL)
    # V3 throughout, with a 2.25 s cutaway to the far race (V8) on the boss's first and last lines
    ais = [k for k, x in enumerate(starts) if x[2] == 'ai']
    a1, a3 = fr(starts[ais[0]][0] - CUT_PRE), fr(starts[ais[-1]][0] - CUT_PRE)
    cuts = [s11, a1, a1 + 2.25, a3, a3 + 2.25, end11]
    srcs = [(v3, 0.0), (v8, 3.5), (v3, 2.0), (v8, 5.75), (v3, 4.0)]
    for (src, i0), x, z in zip(srcs, cuts, cuts[1:]):
        c.pic(src, i0, x, z, '11')
    c.flags.append(f'Beat 11: the call runs {end11 - s11:.1f} s on 8 s of V3, so V3 ping-pongs; the boss\'s lines 1 and 3 '
                   'open on 2.25 s of the far race (V8). His line 2 stays on Maddie (V8 has no more far race in it).')
    c.flags.append('Beat 11: the boss is the Suno newsreader, one take a line (Kai\'s picks), through the same small-'
                   'speaker filter as before. His takes keep Suno\'s own pauses ("Oh. [1.7 s] And they\'ve...", '
                   '"No. [1 s] Thank you, Maddie. [1 s] I will handle it.").')
    c.flags.append('Beat 11, boss line 2 (Kai at3398: it cut in and out): ' + (f'the re-record {BOSS[2]}.' if BOSS2_RE else
                   'RE-RECORD PENDING: still the old take (the Suno re-record is blocked for now).'))
    m['s11'], m['calls'], m['end11'] = s11, starts, end11
    m['v8cuts'] = [(cuts[1], cuts[2]), (cuts[3], cuts[4])]
    t = c.close(b, end11)

    # ---- 10b: the close race, Maddie over it
    b = c.beat('10b', 'The close race', t, act='Kill mode',
               see='Low in the grass: the pack converges on the bunker door. Maddie over it.')
    tk = Take(A1 / '10b-0-bot-a.wav')
    e = c.say('vox-maddie', tk, t + LEAD, '10b', 'beat 10b Maddie')
    c.line(b, 0, 'bot', t + LEAD, e - t - LEAD, "Well, you'd better bloody hurry up, boss. They're nearly there.", 'kai')
    d10b = fr(max(5.0, e + TAIL - t))
    if TAG in ('d5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20'):  # Kai at5110 (2 Nov): far wider, the pack racing at the door from far off -- WA02 (his still pick wa-02)
        c.pic(V / 'cut3-WA02.mp4', 0, t, t + d10b, '10b')
        b['title'], b['see'] = 'The wide approach', ('Long lens through the grass: the pack races along the foot of the slope, the '
                                                     'bunker door small and high on the right. Maddie over it.')
        c.flags.append('Beat 10b (Kai at5110): V9 (too close to the door) replaced by WA02, the wide approach from your still '
                       'pick wa-02 (Omni, take 2; take 1 turned the bots into tanks). The on-board stand-down (V4) is unchanged.')
    else:
        c.pic(V / 'cut3-V9.mp4', 0, t, t + d10b, '10b')
    m['s10b'], m['l10b'] = t, (t + LEAD, e)
    t = c.close(b, t + d10b)

    # ---- 12: on board, kill -> STAND DOWN as it brakes; V10r (Kai's pick A) they file away; the boss on Maddie
    s12 = t
    b = c.beat('12', 'The stand-down', s12, act='The gate',
               see='On board one kill bot: red KILL MODE racing at the door, it brakes and flips to green STAND DOWN. '
                   'Lined up at the door, they file away one at a time. Then Maddie, shaky with relief: "Good job." '
                   '"That was close."')
    v4 = V / 'cut3-V4.mp4'
    if D7 and (V / 'cut3-SD01.mp4').exists():  # Kai: the bot reversed under the HUD -> his still pick sd-01, braked dead
        v4 = V / 'cut3-SD01.mp4'
        c.flags.append('Beat 12 (round 9): the stand-down plate is SD01 (your still pick sd-01, animated): it brakes dead well '
                       'short of the door; V4 (which reversed) is out.')
    peace = 3.6
    c.huds.append(dict(name='hud-12', src=str(v4), d=7.0, args=['--state', 'kill', '--lock', '0',
                                                                 '--flip-to', f'peace@{peace}'],
                       meter=['sfx-killbots'], t0=s12, ss=0.5 if v4.stem == 'cut3-SD01' else 0.0))  # SD01: first 0.25 s re-sits
    c.pic(c.vdir / 'hud-12.mp4', 0.0, s12, s12 + 7.0, '12', source=v4, hud='hud-12')
    if D8 and (V / 'cut3-RT01.mp4').exists():  # Kai at4914: much wider, far from the door, turning and retreating (his pick rt-01)
        c.pic(V / 'cut3-RT01.mp4', RT01_IN, s12 + 7.0, s12 + 12.5, '12')
        c.flags.append('Beat 12 (round 10, Kai at4914): V10r (filing away at the door) replaced by RT01, your still pick rt-01: '
                       'a high wide from the ridge, the pack turning and rolling away down the slope.')
    else:
        c.pic(V / 'cut3-V10r.mp4', 0, s12 + 7.0, s12 + 12.5, '12')
    s_v3 = fr(s12 + 12.5)
    tk = Take(pathlib.Path(A3['media']) / MADDIE12['file'])
    l12 = 'Good job. [pause] That was close.'
    if D4:  # Kai at5600 (2 Nov): just "That was close." -- the same take from after its pause
        tk, l12 = Take(close_only(pathlib.Path(A3['media']) / MADDIE12['file'], c.dir)), 'That was close.'
    e = c.say('vox-maddie', tk, s_v3 + LEAD, '12', f'beat 12 Maddie: {shown(l12)}')
    c.line(b, 0, 'bot', s_v3 + LEAD, e - s_v3 - LEAD, l12, 'kai')
    end12 = fr(e + TAIL + 0.4)
    c.pic(v3, 3.0, s_v3, end12, '12')
    c.flags.append('Beat 12: the HUD now reads STAND DOWN (status RETURN TO PATROL), drawn by hud.py in ffmpeg. V10r '
                   '(Kai\'s pick A) plays 0-5.5 s: they file away one at a time; cut before the nearest bot grows its '
                   'long gun barrel (~5-7 s). They still never visibly turn (the still already has them facing away).')
    c.flags.append('Beat 12 (round 3, Kai at4098): the boss\'s last line is gone; Maddie says "Good job." (pause) "That was '
                   'close." (round 3b, Kai at4138: "boss" cut out of the take, not re-voiced). Take a of four (voices.json): her cheeky Style/Pace replaced for this line, a soft '
                   '"Whew." from the [sighs] tag, its 4.25 s pause cut to ~1.85 s. Take c is the clean one without the sigh.')
    if D4:
        c.flags[-2] = c.flags[-2].replace('the HUD now reads STAND DOWN (status RETURN TO PATROL)',
                                          'the HUD flips to NEW OBJECTIVE / SUSTAIN ORGANIC LIFE (Kai, 2 Nov: matches the door\'s film)')
        c.flags[-1] = ('Beat 12 (Kai at5600, 2 Nov): Maddie says only "That was close." -- the same take, cut from after its '
                       'pause (audio-12-that-was-close.wav), not re-voiced.')
    m['s12'], m['peace'], m['s_v3'], m['l12'] = s12, fr(s12 + peace), s_v3, (s_v3 + LEAD, e)
    t = c.close(b, end12)
    c.total = t
    return c


# ---------------------------------------------------------------- round 18: faster voices (Kai, 5 Nov meeting)
# The row: each lip-synced shot's picture AND its dub are sped by the same factor, so the mouths stay where they were
# fitted (v3). The v3 dubs already run at tempo 1.00-1.15 against the TTS masters, so a shot's factor is capped where
# its on-face voice would pass ~1.25 combined (the warble limit is ~1.3): 7d-0 ("I'm really sorry, love", already 1.15)
# gets 1.08; the rest 1.15. Pieces laid over the other person's face are not lip-bound and take their own tempo (<=1.25).
LIP18 = ROOT / 'lip-r18'
ROW18 = {'6-0': ('cut3-lip-6-0-v3-muted.mp4', '6-0', 1.15), '7d-0': ('cut3-lip-7d-0-v3-muted.mp4', '7d-0c', 1.08),
         '7-0': ('cut3-lip-7-0-muted.mp4', '7-0', 1.15), '7d-1': ('cut3-lip-7d-1-muted.mp4', '7d-1c', 1.15),
         '7-2': ('cut3-lip-7-2-v3-muted.mp4', '7-2', 1.15)}
ROW18_GAP = 0.2   # Kai: the gaps between lines to the minimum that still reads
OFFFACE_MAX = 1.25
AGAIN_TEMPO = 1.12  # 'Again.' over Derek's face (was 1.00)
VOX18 = AU / 'voice3' / 'r18'  # Maddie's fast re-voices (Pace fast, clipped, [fast]); picks by measurement
MADDIE18 = {'11-0': VOX18 / '11-0-bot-fast-a.wav', '10b-0': VOX18 / '10b-0-bot-fast-a.wav', '12-0': VOX18 / '12-0-bot-fast-b.wav'}
BOSS18 = AU / 'boss-r18'  # Suno re-records of the boss's two lines (another agent); the old takes until they land


def boss18(src):
    """The picked boss re-record for line `src` (1 = simulations, 3 = handle it), only once the picks are written:
    boss-r18/picks.json {"1": "<file>.wav", "3": "<file>.wav"}. The folder fills with raw takes first; never guess."""
    pj = BOSS18 / 'picks.json'
    if not pj.exists():
        return None
    f = json.loads(pj.read_text()).get(str(src))
    return BOSS18 / f if f else None


ROW19 = {'6-0': ('cut3-lip-6-0-v3-muted.mp4', '6-0', 'v3'), '7d-0': ('cut3-lip-7d-0-r19-muted.mp4', '7d-0c', 'r19'),
         '7-0': ('cut3-lip-7-0-muted.mp4', '7-0', 'r19'), '7d-1': ('cut3-lip-7d-1-muted.mp4', '7d-1c', 'r19'),
         '7-2': ('cut3-lip-7-2-r19-muted.mp4', '7-2', 'r19')}


def lip19():
    """Round 19: natural picture speed. Each shot's clip and its fitted phrase table (voice-row-fit.py: re-voiced to the
    clip, or a new talking clip, picked by a joint fit of voice loudness on the tracked mouth); 6-0 keeps v3 (it fitted best)."""
    out = {}
    for key, (vid, pname, ver) in ROW19.items():
        ph = json.loads((LIP / f'cut3-lip-{pname}-{ver}-phrases.json').read_text())['phrases']
        out[key] = (V / vid, ph, 1.0, LIP / f'cut3-lip-{pname}-{ver}-dub.wav')
    return out


def lip18(c):
    """Sped copies of the row's muted clips, dubs and phrase tables (factor per shot); returns {key: (video, phrases, k)}."""
    LIP18.mkdir(parents=True, exist_ok=True)
    out = {}
    for key, (vid, pname, k) in ROW18.items():
        src_v = V / vid
        v = LIP18 / f'{src_v.stem}-x{k:.2f}.mp4'
        if not v.exists():
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src_v), '-an', '-vf', f'setpts=PTS/{k},fps={FPS}',
                            *ENC, str(v)], check=True)
            subprocess.run([sys.executable, str(S.REPO / 'scripts/provenance/prov.py'), 'card', str(v), '--kind', 'video',
                            '--engine', 'ffmpeg', '--tool', f'ffmpeg setpts=PTS/{k}', '--parent', str(src_v),
                            '--why', 'round 18 faster voices: the lip-synced shot sped with its dub by the same factor'],
                           check=True, capture_output=True)
        ph = json.loads((LIP / f'cut3-lip-{pname}-v3-phrases.json').read_text())
        dub = LIP / f'cut3-lip-{pname}-v3-dub.wav'
        d = LIP18 / f'{dub.stem}-x{k:.2f}.wav'
        if not d.exists():
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(dub), '-af', f'atempo={k}', str(d)], check=True)
            subprocess.run([sys.executable, str(S.REPO / 'scripts/provenance/prov.py'), 'card', str(d), '--kind', 'voice',
                            '--engine', 'ffmpeg', '--tool', f'ffmpeg atempo={k}', '--parent', str(dub),
                            '--why', 'round 18 faster voices: the dub sped with its shot by the same factor'],
                           check=True, capture_output=True)
        for q in ph['phrases']:
            q['at'] = q['at'] / k
            q['tempo'] = q['tempo'] * k
        ph['video'], ph['dub'], ph['factor'] = str(v), str(d), k
        (LIP18 / f'cut3-lip-{pname}-r18-phrases.json').write_text(json.dumps(ph, indent=1))
        out[key] = (v, ph['phrases'], k, d)
    return out


def row_d16(c, t, m, LINES):
    """row_d8 on the sped shots, 0.2 s between lines (see ROW18); round 19: natural speed, re-fitted (ROW19)."""
    L = lip19() if D17 else lip18(c)
    t0 = t
    v6, s6, k6, dub6 = L['6-0']
    v7d0, d7a, k7d0, dub7d0 = L['7d-0']
    v70, s7, k70, dub70 = L['7-0']
    v7d1, d7b, k7d1, dub7d1 = L['7d-1']
    v72, s72, k72, dub72 = L['7-2']
    up_end = s6[1]['at'] + (s6[1]['to'] - s6[1]['from']) / s6[1]['tempo']
    b6 = c.beat('6', 'The lavatory', t0, act='The row', see='Hard cut to full volume: Sandra, lip-synced.')
    cut1 = fr(t0 + up_end + 0.04)
    c.pic(v6, 0.0, t0, cut1, '6', source=V / 'cut3-lip-6-0-v3.mp4')
    c.dub('vox-sandra', dub6, 0.0, cut1 - t0, t0, f'beat 6 6-0 (lip-sync dub, x{k6:.2f} with its shot)', chain=[TILE])
    again, d_again = row_piece(c, s6[2]['src'], s6[2]['from'], s6[2]['to'], 1.0 if D17 else AGAIN_TEMPO,
                               '6-0-again-r19' if D17 else '6-0-again-r18')
    t_again = t0 + up_end + 0.06
    c.dub('vox-sandra', again, 0.0, d_again, t_again, "beat 6 Sandra 'Again.' (over Derek)", chain=[TILE])
    c.line(b6, 0, 'woman', t0 + s6[0]['at'], t_again + d_again - t0 - s6[0]['at'], "Derek. You've left the seat up again.", 'kai')
    c.close(b6, cut1)
    b7 = c.beat('7', 'The row, up close', cut1, act='The row',
                see='Derek takes it on the chin, then Sandra; Derek, Sandra: shot by shot, lip-synced.')
    d_line = (d7a[0]['to'] - d7a[0]['from']) / d7a[0]['tempo']
    t_dl = t_again + d_again + ROW18_GAP
    i0d = d7a[0]['at'] - (t_dl - cut1)
    assert i0d >= 0.3, i0d
    t_dend = t_dl + d_line
    sfx18 = 'r19' if D17 else 'r18'
    five, d_five = row_piece(c, s7[0]['src'], s7[0]['from'], s7[0]['to'], min(s7[0]['tempo'], OFFFACE_MAX), f'7-0-five-years-{sfx18}')
    rest, d_rest = row_piece(c, s7[1]['src'], s7[1]['from'], s7[1]['to'], s7[1]['tempo'], f'7-0-seat-{sfx18}')
    t_five = t_dend + ROW18_GAP
    t_rest = t_five + d_five
    cut2 = fr(t_rest - CUT_PRE)
    assert i0d + (cut2 - cut1) <= dur(v7d0) + 1e-6, (i0d + (cut2 - cut1), dur(v7d0))
    c.pic(v7d0, i0d, cut1, cut2, '7', source=V / 'cut3-lip-7d-0-v3.mp4')
    c.dub('vox-derek', dub7d0, i0d, i0d + (cut2 - cut1), cut1, f'beat 7 7d-0 (lip-sync dub, x{k7d0:.2f} with its shot)', chain=[TILE])
    c.line(b7, 0, 'man', t_dl, d_line, "I'm really sorry, love.", 'kai')
    c.dub('vox-sandra', five, 0.0, d_five, t_five, "beat 7 Sandra 'Five years underground,' (over Derek)", chain=[TILE])
    c.dub('vox-sandra', rest, 0.0, d_rest, t_rest, "beat 7 Sandra 'and you still can't put a seat down' (lip-synced)", chain=[TILE])
    c.line(b7, 1, 'woman', t_five, t_rest + d_rest - t_five, LINES[('7', 0)]['text'], 'kai')
    i0s = s7[1]['at'] - CUT_PRE
    t_rend = t_rest + d_rest
    d_at = d7b[0]['at']
    i0b = max(0.0, d_at - CUT_PRE)
    cut3 = fr(t_rend + ROW18_GAP - (d_at - i0b))
    c.pic(v70, i0s, cut2, cut3, '7', source=V / 'cut3-lip-7-0.mp4')
    d_b = (d7b[0]['to'] - d7b[0]['from']) / d7b[0]['tempo']
    t_b = cut3 + (d_at - i0b)
    t_bend = t_b + d_b
    s_at = s72[0]['at']
    t_s = t_bend + ROW18_GAP
    i0c = max(0.0, s_at - CUT_PRE)
    cut4 = fr(t_s - (s_at - i0c))
    c.pic(v7d1, i0b, cut3, cut4, '7', source=V / 'cut3-lip-7d-1.mp4')
    c.dub('vox-derek', dub7d1, i0b, i0b + (cut4 - cut3), cut3, f'beat 7 7d-1 (lip-sync dub, x{k7d1:.2f} with its shot)', chain=[TILE])
    c.line(b7, 2, 'man', t_b, d_b, 'But the world ended, Sandra!', 'kai')
    d_s = (s72[0]['to'] - s72[0]['from']) / s72[0]['tempo']
    end = fr(t_s + d_s + TAIL)
    assert i0c + (end - cut4) <= dur(v72) + 0.5 / FPS, (i0c + (end - cut4), dur(v72))
    c.pic(v72, i0c, cut4, end, '7', source=V / 'cut3-lip-7-2-v3.mp4')
    c.dub('vox-sandra', dub72, i0c, i0c + (end - cut4), cut4, f'beat 7 7-2 (lip-sync dub, x{k72:.2f} with its shot)', chain=[TILE])
    c.line(b7, 3, 'woman', t_s, d_s, LINES[('7', 2)]['text'], 'kai')
    m['s6'] = t0
    m['row18'] = {'6-0': (t0, 0.0, k6), '7d-0': (cut1, i0d, k7d0), '7-0': (cut2, i0s, k70), '7d-1': (cut3, i0b, k7d1),
                  '7-2': (cut4, i0c, k72)}
    if D17:
        c.flags.append('Beats 6-7, round 19 (Kai at3777: the speed-up read as sped-up footage): every talking shot at natural '
                       'speed. 6-0 Sandra: the v3 clip and voice (it fitted best of everything tried). 7d-0 Derek: a NEW talking '
                       'clip (Flow, Omni Flash, from the approved still) with a fast re-voice laid unbroken at x1.02. 7-0 Sandra: '
                       'the same clip, re-voiced to it (x1.08, one take). 7d-1 Derek: the same clip, re-voiced to it (x0.97). '
                       '7-2 Sandra: a NEW talking clip with her original voice at x1.12. Each pairing picked by a joint fit of the '
                       'voice loudness on the tracked mouth (voice-row-fit.py); no voice placed before a mouth opens.')
    c.flags.append('Beats 6-7, round 18 (faster voices): every lip-synced shot and its dub sped by the same factor, so the '
                   f'mouths stay where they were fitted: 6-0 x{k6:.2f}, 7d-0 x{k7d0:.2f} (its line was already at 1.15 against the '
                   f'voice master, so capped there), 7-0 x{k70:.2f}, 7d-1 x{k7d1:.2f}, 7-2 x{k72:.2f}; frame sampling, no '
                   f'interpolation. "Again." (over Derek) x{AGAIN_TEMPO}, "Five years underground," (over Derek) '
                   f'x{min(s7[0]["tempo"], OFFFACE_MAX):.2f}. {ROW18_GAP:g} s between lines.')
    return c.close(b7, end)


RT01_D15 = 3.0  # round 17: the bots turning away at the door, the whole stand-down now (no HUD)


def row_on_derek(c):
    """Round 21 (Kai, 6 Nov, picked 'Re-edit around her'): Sandra's face stays only on her opening line (6-0, which
    measured in sync). 'and you still can't put a seat down' (7-0) and 'Yeah, the world ended. Doesn't mean you get to stop
    having manners.' (7-2) play over Derek taking it: his shot before each runs on through her line. Measured on the
    tracked mouth: in both Derek clips his mouth is shut from ~3.6 s to the end, so the run-ons (ping-ponged past 6 s)
    show him silent. Voices untouched."""
    v = c.video
    k70 = next(i for i, x in enumerate(v) if 'lip-7-0' in x['file'])
    k72 = next(i for i, x in enumerate(v) if 'lip-7-2' in x['file'])
    for k in (k70, k72):
        v[k - 1]['dur'] = fr(v[k - 1]['dur'] + v[k]['dur'])
    for k in sorted((k70, k72), reverse=True):
        del v[k]
    c.flags.append('Beats 6-7, round 21 (Kai: Sandra\'s lip sync not good, re-edit around her): back to round 19\'s clips (no '
                   'LatentSync). Sandra on screen only for "Derek. You\'ve left the seat up again."; "and you still can\'t put a seat '
                   'down" and "Yeah, the world ended. Doesn\'t mean you get to stop having manners." play over Derek taking it '
                   '(his mouth shut, measured), each Derek shot running on through her line, ping-ponged past its 6 s.')


def rest_d15(c, t, m):
    """Round 17 (Kai, 5 Nov): the brutal kill-bot cut. After "Mind how you go.": hard cut to the row (6-7), one kill bot
    tears past Maddie (9a, the first bot we see), the call trimmed to three lines (11), the wide approach (10b), the bots
    turning away at the door (12, no HUD: the red/green screens are saved for the bunker TV), "That was close." Beats 1-4,
    8, 9b and 10a are gone."""
    # ---- 6-7: the row, exactly as round 16, from a hard cut (round 18: sped, picture and voice together)
    t = row_d16(c, t, m, LINES) if D16 else row_d8(c, t, m, LINES)
    if D19:
        row_on_derek(c)
    if D18:  # Kai at3874: no bot tearing past Maddie (and no wobble): straight to the tanks on the motorway
        b = c.beat('9a', 'The kill bots on the motorway', t, act='Kill mode',
                   see='The pack races down the abandoned motorway in its own dust: the first time we see them.')
        c.pic(V / 'cut3-V8.mp4', V8_IN18, t, t + D9A18, '9a')
        m['s9a'] = t
        c.flags.append(f'Beat 9a (round 20, Kai at3874/at4171): the bot tearing past Maddie is cut; the scene goes straight from '
                       f'the row to the tanks on the motorway (V8 {V8_IN18:g}-{V8_IN18 + D9A18:g} s). We see the pack twice: here, '
                       'and racing across the field to the bunker. No KILL MODE or STAND DOWN screens.')
        t = c.close(b, t + D9A18)
        return call_d18(c, t, m)
    # ---- 9a: one kill bot tears past Maddie
    b = c.beat('9a', 'One kill bot tears past Maddie', t, act='Kill mode',
               see='The first kill bot we see: high over the street, it passes close and exits bottom-left, Maddie jolts, '
                   'a plume of dust hangs.')
    c.pic(V / 'cut3-V1.mp4', V1_IN, t, t + D9A, '9a')
    m['s9a'] = t
    t = c.close(b, t + D9A)
    # ---- 11: the call, three lines
    s11 = t
    b = c.beat('11', 'Maddie calls her boss', s11, act='Kill mode',
               see="Maddie's hatch, the boss-hotline antenna. Three lines; the race (far) under the boss's two.")
    v3, v8 = V / 'cut3-V3.mp4', V / 'cut3-V8.mp4'
    calls = [('bot', A1 / '11-0-bot-b.wav', "Boss, I've just seen a bot in kill mode. Which must mean it's detected an "
                                            'organic signal.'),
             ('ai', 1, None), ('ai', 3, None)]
    if D16:
        calls[0] = ('bot', MADDIE18['11-0'], calls[0][2])
    if D17:  # Kai at4194: lose "No, thank you. I will handle it." -- straight from 'simulations again' to the next shot
        calls = calls[:2]
    tt = s11 + 2.0  # the antenna first
    starts = []
    for k, (who, src, text) in enumerate(calls):
        if who == 'ai':
            tk, text = Take(SUNO_A / BOSS[src]), BOSS_TEXT[src]
            if src == 3:  # Kai at4564: no second 'Maddie'
                tk, text = Take(SUNO_A / BOSS[3].replace('.wav', '-noname.wav')), 'No, thank you. I will handle it.'
            if D16 and boss18(src):
                tk = Take(boss18(src))
            e = c.say('vox-ai', tk, tt, '11', f'beat 11 boss line {src}' + (f' (r18 re-record {tk.path.name})' if D16 and boss18(src) else ''),
                      chain=[SPEAKER], lufs=-17)
        else:
            e = c.say('vox-maddie', Take(src), tt, '11', 'beat 11 Maddie 0')
        c.line(b, k, who, tt, e - tt, text, 'kai')
        starts.append((tt, e, who))
        tt = e + GAP
    end11 = fr(starts[-1][1] + TAIL)
    if D17:  # Kai at4230: no cut back to V3 -- the call ends on the far race under 'simulations again', then 10b
        a1 = fr(starts[1][0] - CUT_PRE)
        assert 3.5 + (end11 - a1) <= dur(v8) + 0.5 / FPS, (end11 - a1, dur(v8))
        c.pic(v3, 0.0, s11, a1, '11')
        c.pic(v8, 3.5, a1, end11, '11')
        m['s11'], m['calls'], m['end11'], m['v8cuts'] = s11, starts, end11, [(a1, end11)]
        c.flags.append(f'Beat 11 (round 19, Kai at4194/at4230): two lines, her report and "making fun of my simulations again?"; '
                       f'"No, thank you. I will handle it." is cut. V3 (the hatch) to the boss\'s line, then the far race (V8) '
                       f'under it to the cut to the wide approach: no cut back to V3.')
        t = c.close(b, end11)
        return rest_d15_after_call(c, t, m)
    a1, a3 = fr(starts[1][0] - CUT_PRE), fr(starts[2][0] - CUT_PRE)
    # V3 throughout, a 2.25 s cutaway to the far race (V8) on each of the boss's lines (back-to-back lines: the second
    # cutaway follows straight on if they overlap)
    cuts = [s11, a1, fr(a1 + 2.25), max(a3, fr(a1 + 2.25)), fr(max(a3, a1 + 2.25) + 2.25), end11]
    srcs = [(v3, 0.0), (v8, 3.5), (v3, 2.0), (v8, 5.75), (v3, 4.0)]
    for (src, i0), x, z in zip(srcs, cuts, cuts[1:]):
        if z > x:
            c.pic(src, i0, x, z, '11')
    c.flags.append(f'Beat 11 (round 17): three lines, Maddie\'s report, "making fun of my simulations", "No, thank you. I will handle it."; '
                   f'"No, honestly, it\'s real..." and the malware offer are cut. {end11 - s11:.1f} s on V3 with the far race (V8) '
                   'cut in on each of the boss\'s lines, as before.')
    m['s11'], m['calls'], m['end11'] = s11, starts, end11
    m['v8cuts'] = [(cuts[1], cuts[2]), (cuts[3], cuts[4])]
    t = c.close(b, end11)
    return rest_d15_after_call(c, t, m)


V8_IN18, D9A18 = 0.0, 4.0  # round 20: the motorway, its first 4 s (the pack nearest, most dust)
MADDIE20 = {'11-0': AU / 'voice3' / 'r20' / '11-0-bot-b.wav', '10b-0': AU / 'voice3' / 'r20' / '10b-0-bot-b.wav'}
LINE20 = {'11-0': 'Boss, can you see those bots? In kill mode. They must have detected an organic signal.',
          '10b-0': "Quick, boss, hurry up! They're nearly there."}


def call_d18(c, t, m):
    """Round 20 (Kai at4079/at4171): Maddie calls the boss with the new line, and we stay on her (V3) for the boss's
    reply too; then the wide approach."""
    s11 = t
    b = c.beat('11', 'Maddie calls her boss', s11, act='Kill mode',
               see="Maddie's hatch, the boss-hotline antenna. Her report and the boss's reply, on her the whole time.")
    v3 = V / 'cut3-V3.mp4'
    tt, starts = s11 + 2.0, []
    for k, who in enumerate(('bot', 'ai')):
        if who == 'bot':
            e = c.say('vox-maddie', Take(MADDIE20['11-0']), tt, '11', 'beat 11 Maddie 0 (round 20 line)')
            text = LINE20['11-0']
        else:
            tk = Take(boss18(1)) if boss18(1) else Take(SUNO_A / BOSS[1])
            e = c.say('vox-ai', tk, tt, '11', f'beat 11 boss line 1 ({tk.path.name})', chain=[SPEAKER], lufs=-17)
            text = BOSS_TEXT[1]
        c.line(b, k, who, tt, e - tt, text, 'kai')
        starts.append((tt, e, who))
        tt = e + GAP
    end11 = fr(starts[-1][1] + TAIL)
    c.pic(v3, 0.0, s11, end11, '11')  # past 8 s V3 ping-pongs (she hardly moves), as in earlier rounds
    m['s11'], m['calls'], m['end11'], m['v8cuts'] = s11, starts, end11, []
    c.flags.append('Beat 11 (round 20, Kai at4079/at4171): her new line, "' + LINE20['11-0'] + '", then the boss\'s reply with '
                   'the picture staying on Maddie (V3) throughout; no cutaway.')
    t = c.close(b, end11)
    return rest_d15_after_call(c, t, m)


def rest_d15_after_call(c, t, m):
    v3 = V / 'cut3-V3.mp4'
    # ---- 10b: the wide approach, Maddie over it
    b = c.beat('10b', 'The wide approach', t, act='Kill mode',
               see='Long lens through the grass: the pack races along the foot of the slope, the bunker door small and high on '
                   'the right. Maddie over it.')
    tk = Take(MADDIE20['10b-0'] if D18 else MADDIE18['10b-0'] if D16 else A1 / '10b-0-bot-a.wav')
    e = c.say('vox-maddie', tk, t + LEAD, '10b', 'beat 10b Maddie')
    c.line(b, 0, 'bot', t + LEAD, e - t - LEAD, LINE20['10b-0'] if D18 else "Well, you'd better bloody hurry up, boss. They're nearly there.", 'kai')
    d10b = fr(max(5.0, e + TAIL - t))
    c.pic(V / 'cut3-WA02.mp4', 0, t, t + d10b, '10b')
    m['s10b'], m['l10b'] = t, (t + LEAD, e)
    t = c.close(b, t + d10b)
    # ---- 12: the bots turn away at the door (RT01, no HUD); Maddie
    s12 = t
    b = c.beat('12', 'The stand-down', s12, act='The gate',
               see='No HUD: from the ridge, the pack turns away from the bunker door and rolls off down the slope. Then Maddie, '
                   'shaky with relief: "That was close."')
    c.pic(V / 'cut3-RT01.mp4', RT01_IN, s12, s12 + RT01_D15, '12')
    s_v3 = fr(s12 + RT01_D15)
    tk = Take(MADDIE18['12-0']) if D16 else Take(close_only(pathlib.Path(A3['media']) / MADDIE12['file'], c.dir))
    e = c.say('vox-maddie', tk, s_v3 + LEAD, '12', 'beat 12 Maddie: That was close.')
    c.line(b, 0, 'bot', s_v3 + LEAD, e - s_v3 - LEAD, 'That was close.', 'kai')
    end12 = fr(e + TAIL + 0.4)
    c.pic(v3, 3.0, s_v3, end12, '12')
    c.flags.append(f'Beat 12 (round 17): no HUD (Kai: the red KILL MODE and green STAND DOWN are saved for the bunker TV). '
                   f'RT01 from {RT01_IN} s for {RT01_D15:g} s is the stand-down, then Maddie on V3: "That was close." (the line as '
                   'it has been since your 2 Nov note, the take from after its pause; the full "Good job. That was close." take is there if wanted).')
    c.flags.append('Round 17: beats 1-4 (roundabout, V13r3, V14, the patrol over the lens, the patrol HUD and the muffled row under it), '
                   'beat 8 (KILL MODE HUD), 9b (the dust) and 10a (the far race) are cut.')
    m['s12'], m['peace'], m['s_v3'], m['l12'] = s12, s12, s_v3, (s_v3 + LEAD, e)
    t = c.close(b, end12)
    c.total = t
    return c


def audio_a_d15(c):
    """Round 17's sound: beat 0 as round 16; no patrol music; the chase (C3) arrives with the bot tearing past Maddie,
    ducked under the call and her 10b line, its break-off landing as the pack turns away (beat 12); no HUD sounds."""
    m, total = c.m, c.total
    mx = C.Mix(total)
    voices(c, mx)
    sfx = json.loads((SFX / 'index.json').read_text())
    RADIO = sfx['filters']['M0_tinny_radio']
    fx = sfx_adder(mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}
    # ---- M0, her radio: exactly as rounds 15-16
    hello, down, up, d0, bye = m['hello'][0], m['racket'][1], m['bye'][1] - 1.3, en['0'], m['bye'][1]
    hp = m['holo']['p']
    x = C.level(C.decode(C.MUSIC['M0'], 0.0, m['holo']['h'], af=RADIO), rms=-23)
    x *= C.env(len(x), [(0, 0), (0.3, 1), (hello - 0.25, 1), (hello, 0.2), (down - 0.1, 0.2), (down + 0.7, 0),
                        (len(x) / SR, 0)])
    mx.add('mus-M0-radio', x, 0.0, C.MUSIC['M0'], 'M0 her radio (tinny GPOM track), the opening')
    y = C.level(C.decode(C.MUSIC['M0'], max(0.0, C.DROP - (up - hp)), d0 - hp, af=RADIO), rms=-23)
    y *= C.env(len(y), [(0, 0), (up - 0.3 - hp, 0), (up + 0.3 - hp, 0.35), (bye - hp, 0.35), (bye + 0.3 - hp, 1),
                        (d0 - 0.03 - hp, 1), (d0 - hp, 0)])
    mx.add('mus-M0-radio', y, hp, C.MUSIC['M0'], 'M0 her radio, back after the fade-up (the drop on "Mind how you go")')
    # ---- C3 the chase: from the bot tearing past Maddie (9a) to the stand-down; its break-off (one low held note)
    # lands as the pack turns away (beat 12), and the note rings on under "That was close."
    s2, stop = m['s9a'], m['peace']
    d = stop - s2
    tail = min(dur(C3) - C3_BREAK, total - stop)
    assert d <= C3_BREAK, d
    x = C.decode(C3, C3_BREAK - d, d + tail)
    x = C.level(x, rms=-18, peak=-1)
    da = m['calls'][0][0] - 0.3 - s2
    db = m['calls'][-1][1] + 0.2 - s2
    e10b = m['l10b'][1] - s2
    x *= C.env(len(x), [(0, 0.0), (0.15, 1), (da, 1), (da + 0.4, 0.22), (db, 0.22), (db + 0.4, 1),
                        (m['l10b'][0] - s2 - 0.2, 1), (m['l10b'][0] - s2, 0.22), (e10b, 0.22), (e10b + 0.3, 1),
                        (len(x) / SR - 1.5, 1), (len(x) / SR, 0)])
    mx.add('mus-C3-chase', x, s2, C3, 'C3 the chase (low strings), from the bot tearing past her')
    c.flags.append(f'Music (round 17): no patrol music (P1/P2 gone with beats 1-4 and 8). C3 the chase comes in with the bot '
                   f'tearing past Maddie (9a), starting {C3_BREAK - d:.1f} s into the take so its break-off lands as the pack turns '
                   f'away (beat 12); ducked to -13 dB under the call and her 10b line; its held note rings under "That was close."')
    # ---- sfx: beat 0 as round 16
    H = m['holo']
    wind = wind_file()
    fx('sfx-wind', wind, 0, H['h'] + 0.5, rms=-34, fi=1.0, fo=1.5, tile=True, what='wind (ffmpeg), the street')
    fx('sfx-wind', wind, H['h'] - 1.0, H['p'] - H['h'] + 2.0, src_in=7.0, rms=-46, fi=1.5, fo=1.5, tile=True,
       what='wind, a low bed under the hologram')
    fx('sfx-wind', wind, H['p'] - 0.5, en['0'] - H['p'] + 0.5, src_in=13.0, rms=-34, fi=2.0, fo=0.05, tile=True,
       what='wind, the street again (to the hard cut)')
    loop_wheels(fx, 'sfx-maddie', 0.0, H['sw'] + 1.0, rms=-31, fi=0.5, fo=1.0, what='her wheels (loop), fading with the picture')
    loop_wheels(fx, 'sfx-maddie', H['b'], en['0'] - H['b'], rms=-31, fi=1.0, fo=0.05, what='her wheels (loop), rolling again')
    for k in np.arange(8.5, en['0'] - 0.5, 2.5):
        if H['h'] - 0.5 <= k < H['p']:
            continue
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-36, what='beacon blip')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-oh.wav', hello - 0.55, rms=-30, what='beep: startled (she sees us)')
    fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', down - 0.05, rms=-32, what='servo: she turns the radio down')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-deflate.wav', m['went'][1] + 0.05, rms=-32, what='beep: deflate (after "went.")')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-thinking.wav', m['mattered'][1] + 0.1, rms=-34, what='beep: thinking (into the hologram)')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-happy.wav', m['bye'][1] + 0.05, rms=-31, what='beep: happy (bye)')
    # ---- 6-7: the tiled room
    fx('sfx-rooms', SFX / 'fs767306-room-tiled-public-bathroom.mp3', st['6'], en['7'] - st['6'], src_in=10, rms=-42,
       fi=0.02, fo=0.05, what='tiled room tone')
    if D18:  # ---- 9a (round 20): the motorway, the pack in its dust
        s = st['9a']
        fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, D9A18 + 0.3, rms=-28, fi=0.05, fo=0.4, what='tank tracks, the pack')
        fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, D9A18 + 1.0, src_in=40, rms=-30, fi=0.05,
           fo=1.0, what='engines (into the call)')
        fx('sfx-wind', wind, s, D9A18, src_in=25.0, rms=-40, fi=0.05, fo=0.3, tile=True, what='wind, the motorway')
    s = st['9a'] - V1_IN
    if not D18:  # the pass (placed in clip time, so they follow V1_IN)
        loop_wheels(fx, 'sfx-maddie', st['9a'], 3.0 - V1_IN, rms=-34, fi=0.05, fo=0.2, what='her wheels, trundling')
        fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['9a'], 3.4 - V1_IN, rms=-26, fi=0.05, fo=0.6, what='tank tracks')
        fx('sfx-maddie', MS / 'derived-maddie-killbot-dust-whoosh.wav', s + 1.6, peak=-3, af='pan=stereo|c0=c1|c1=c0',
           what='kill bot dust whoosh, past her')
        fx('sfx-maddie', MS / 'derived-maddie-servo-turn-b.wav', s + 3.0, rms=-30, what='servo: she jolts')
        fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s + 3.0, en['9a'] - (s + 3.0) + 1.5, src_in=30,
           rms=-32, fo=1.5, what='the kill bot, going away (into the call)')
        fx('sfx-wind', wind, st['9a'], en['9a'] - st['9a'], src_in=25.0, rms=-38, fi=0.05, fo=0.3, tile=True, what='wind, the street')
    # ---- 11: hatch and antenna on V3; the far engines on each V8 cutaway; the beacon on the boss's words
    fx('sfx-maddie', MS / 'derived-maddie-hatch-open.wav', m['s11'] + 0.02, rms=-26, what='hatch')
    fx('sfx-maddie', MS / 'derived-maddie-antenna-extend.wav', m['s11'] + 0.4, rms=-26, what='antenna extends')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-ack-double.wav', m['s11'] + 1.45, rms=-32, what='beep: line open')
    for a, z in m['v8cuts']:
        fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', a, z - a + 0.3, src_in=40, rms=-31,
           fi=0.05, fo=0.3, what='engines, far (cutaway)')
    for a, e, who in m['calls']:
        if who == 'ai':
            for k in np.arange(a, e, 0.9):
                fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-34, what='beacon on his words')
    # ---- 10b: the close race
    s = st['10b']
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, en['10b'] - s, src_in=10, rms=-30, fi=0.05,
       fo=0.2, what='engines, close')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, en['10b'] - s, rms=-30, peak=-3, fo=0.3, what='tracks, close')
    fx('sfx-killbots', SFX / 'fs189446-killbot-jet-flyby.mp3', s - 0.3, 2.5, src_in=4, rms=-32, peak=-3, fi=0.3, fo=0.8,
       what='two tear past the camera (under her line)')
    # ---- 12: the pack turns away (no HUD sounds); wind on the downs to the end
    s = st['12']
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, RT01_D15 + 1.5, rms=-30, fi=0.1, fo=2.0,
       what='the pack turns away')
    fx('sfx-wind', wind, s, total - s, src_in=20, rms=-36, fi=0.5, fo=0.5, tile=True, what='wind on the downs')
    return mx


def audio_a(c):
    if D15:
        return audio_a_d15(c)
    m, total = c.m, c.total
    mx = C.Mix(total)
    voices(c, mx)
    sfx = json.loads((SFX / 'index.json').read_text())
    RADIO = sfx['filters']['M0_tinny_radio']
    fx = sfx_adder(mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}

    # ---- music
    # M0 her radio (tinny GPOM track): playing from the first frame, -14 dB under her first three phrases, down to
    # nothing after "...turn this racket down", creeping back in under "Mind how you go" and up as she finishes, cued
    # so the track's drop lands there (whisper lost her words with it any louder).
    hello = m['hello'][0]
    down = m['racket'][1]
    up = m['bye'][1] - 1.3
    d0 = en['0']
    bye = m['bye'][1]
    if D13:
        # The radio is already at nothing from "racket" to just before "Mind how you go", so it plays in two pieces:
        # the opening exactly as round 14 (from the top of the track), cut at the hologram; then from the pull-out,
        # cued so the drop lands on "Mind how you go" as before.
        hp = m['holo']['p']
        x = C.level(C.decode(C.MUSIC['M0'], 0.0, m['holo']['h'], af=RADIO), rms=-23)
        x *= C.env(len(x), [(0, 0), (0.3, 1), (hello - 0.25, 1), (hello, 0.2), (down - 0.1, 0.2), (down + 0.7, 0),
                            (len(x) / SR, 0)])
        mx.add('mus-M0-radio', x, 0.0, C.MUSIC['M0'], 'M0 her radio (tinny GPOM track), the opening')
        y = C.level(C.decode(C.MUSIC['M0'], max(0.0, C.DROP - (up - hp)), d0 - hp, af=RADIO), rms=-23)
        y *= C.env(len(y), [(0, 0), (up - 0.3 - hp, 0), (up + 0.3 - hp, 0.35), (bye - hp, 0.35), (bye + 0.3 - hp, 1),
                            (d0 - 0.03 - hp, 1), (d0 - hp, 0)])
        mx.add('mus-M0-radio', y, hp, C.MUSIC['M0'], 'M0 her radio, back after the pull-out (the drop on "Mind how you go")')
    else:
        x = C.level(C.decode(C.MUSIC['M0'], C.DROP - up, d0, af=RADIO), rms=-23)
        x *= C.env(len(x), [(0, 0), (0.3, 1), (hello - 0.25, 1), (hello, 0.2), (down - 0.1, 0.2), (down + 0.7, 0),
                            (up - 0.3, 0), (up + 0.3, 0.35), (bye, 0.35), (bye + 0.3, 1), (d0 - 0.03, 1), (d0, 0)])
        mx.add('mus-M0-radio', x, 0.0, C.MUSIC['M0'], 'M0 her radio (tinny GPOM track)')
    # Patrol: P1 (solo cello + felt piano) under beat 1-2, crossfading into P2 (cold quartet) for the HUD (3-4),
    # dead on the hard cut to the lavatory; P2 returns under kill mode (8), out at 9a where C3 starts.
    a, z = st['1'], st['3']
    x = C.fades(C.level(C.decode(P1, 0.0, z - a + 1.0), rms=-21, peak=-3), 0.3, 1.0)
    mx.add('mus-P1-patrol', x, a, P1, 'P1 the patrol (cello + felt piano)')
    a, z = st['3'] - 1.0, st['6']
    x = C.fades(C.level(C.decode(P2, 1.0, z - a), rms=-22, peak=-3), 1.0, 0.03)
    mx.add('mus-P2-patrol', x, a, P2, 'P2 their eyes (cold quartet)')
    a, z = st['8'], st['9a']
    x = C.fades(C.level(C.decode(P2, 12.0, z - a + 0.3), rms=-19, peak=-3), 0.2, 0.3)
    mx.add('mus-P2-patrol', x, a, P2, 'P2 kill mode (its loud stretch)')
    # C3 the chase: 9a to the stand-down, ducked under the call; its break-off (one low held note) lands on STAND DOWN
    # and the held note rings on under the pack filing away.
    s2, stop = m['s9a'], m['peace']
    d = stop - s2
    tail = min(dur(C3) - C3_BREAK, total - stop)
    da = m['calls'][0][0] - 0.3 - s2
    db = m['calls'][-1][1] + 0.2 - s2
    if d <= C3_BREAK:
        x = C.decode(C3, C3_BREAK - d, d + tail)
        c3_note = f'C3 starts {C3_BREAK - d:.1f} s into the take so its break-off lands on STAND DOWN.'
    else:
        seam, xf = da + 3.0, 1.5
        rest = d - seam
        off = C3_BREAK - rest
        p1 = C.decode(C3, 0, seam + xf)
        p2 = C.decode(C3, off - xf, rest + xf + tail)
        n, k = int(seam * SR), int(xf * SR)
        w = np.linspace(0, np.pi / 2, k)[:, None]
        x = np.concatenate([p1[:n], p1[n:n + k] * np.cos(w) + p2[:k] * np.sin(w), p2[k:]])
        c3_note = (f'C3 (60 s) is shorter than its {d:.1f} s run to STAND DOWN: it plays 0-{seam:.1f} s, then '
                   f'crossfades (1.5 s, under the duck) to {off:.1f} s so its break-off lands on STAND DOWN.')
    x = C.level(x, rms=-18, peak=-1)
    e10b = m['l10b'][1] - s2
    x *= C.env(len(x), [(0, 1), (da, 1), (da + 0.4, 0.22), (db, 0.22), (db + 0.4, 1), (m['l10b'][0] - s2 - 0.2, 1),
                        (m['l10b'][0] - s2, 0.22), (e10b, 0.22), (e10b + 0.3, 1), (len(x) / SR - 1.5, 1),
                        (len(x) / SR, 0)])
    mx.add('mus-C3-chase', x, s2, C3, 'C3 the chase and the call (low strings)')
    c.flags.append(c3_note + ' Ducked to -13 dB under the call and -13 dB under Maddie\'s 10b line.')
    c.flags.append('Music: both patrol picks are in, so you can hear each: P1 (cello + felt piano) under the roaming, '
                   'P2 (cold quartet) under the HUD and kill mode. Pick one and it can run the whole patrol (my call).')

    # ---- sfx
    wind = wind_file()
    if D13:
        # The street carries on through the swoop; under the hologram (her presentation) only a low wind bed; the street
        # comes back with the pull-out. She is parked in the swoop and the pull-out, so her wheels stop for both.
        H = m['holo']
        fx('sfx-wind', wind, 0, H['h'] + 0.5, rms=-34, fi=1.0, fo=1.5, tile=True, what='wind (ffmpeg), the street')
        fx('sfx-wind', wind, H['h'] - 1.0, H['p'] - H['h'] + 2.0, src_in=7.0, rms=-46, fi=1.5, fo=1.5, tile=True,
           what='wind, a low bed under the hologram')
        fx('sfx-wind', wind, H['p'] - 0.5, en['3'] - H['p'] + 0.5, src_in=13.0, rms=-34, fi=2.0, fo=0.05, tile=True,
           what='wind, the street again (from the pull-out)')
        loop_wheels(fx, 'sfx-maddie', 0.0, H['sw'] + (1.0 if D14 else 1.5), rms=-31, fi=0.5, fo=1.0 if D14 else 1.5,
                    what='her wheels (loop), fading with the picture' if D14 else 'her wheels (loop), stopping in the swoop')
        loop_wheels(fx, 'sfx-maddie', H['b'], en['0'] - H['b'], rms=-31, fi=1.0 if D14 else 0.4, fo=0.3, what='her wheels (loop), rolling again')
        for k in np.arange(8.5, en['0'] - 0.5, 2.5):
            if H['h'] - 0.5 <= k < H['p']:
                continue
            fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-36, what='beacon blip')
        c.flags.append(f"Beat 0 sound (round 15): the street (wind, wheels, beacon) runs on through the swoop; from "
                       f"{H['h']:.1f} s to {H['p']:.1f} s, under the hologram, only wind at -46 dB RMS (12 dB under the "
                       "street's) and her voice; the street comes back up with the pull-out. Her wheels stop in the swoop "
                       "(she is parked in it) and roll again when we are back on the front shot. The radio is already "
                       "silent from \"racket\" until \"Mind how you go\", as before; it returns on its drop.")
        if D14:
            c.flags[-1] = (f"Beat 0 sound (round 16): the street (wind, wheels, beacon) runs on under the bridge line and fades down "
                           f"with the picture ({H['sw']:.1f}-{H['h']:.1f} s); under the hologram ({H['h']:.1f}-{H['p']:.1f} s) only wind "
                           "at -46 dB RMS and her voice; the street comes back up with the fade-up, her wheels rolling again. The radio "
                           "is silent from \"racket\" until \"Mind how you go\", and its drop still lands there.")
    else:
        fx('sfx-wind', wind, 0, en['3'], rms=-34, fi=1.0, fo=0.05, what='wind (ffmpeg)')
        loop_wheels(fx, 'sfx-maddie', 0.0, en['0'], rms=-31, fi=0.5, fo=0.3, what='her wheels (loop)')
        for k in np.arange(8.5 if D8 else 0.5, en['0'] - 0.5, 2.5):  # d8 (Kai at50): no blips under the opening tune
            fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-36, what='beacon blip')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-oh.wav', hello - 0.55, rms=-30, what='beep: startled (she sees us)')
    fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', down - 0.05, rms=-32, what='servo: she turns the radio down')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-deflate.wav', m['went'][1] + 0.05, rms=-32,
       what='beep: deflate (after "went.")')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-thinking.wav', m['mattered'][1] + 0.1, rms=-34,
       what='beep: thinking (the long pause)')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-happy.wav', m['bye'][1] + 0.05, rms=-31, what='beep: happy (bye)')
    # Beat 1-3: the kill bots.
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', st['1'], st['4'] - st['1'], src_in=2, rms=-28,
       fi=0.3, fo=0.03, what='engines round the ring, and down the street')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', m['v14'], 6.0, rms=-26, fi=0.4, fo=0.4,
       what='tracks under the arch (V14)')
    fx('sfx-killbots', SFX / 'fs824121-killbot-servo.mp3', m['v14'] + 4.6, 1.2, src_in=1, rms=-28, fo=0.3,
       what='turret swings on us')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['2'], en['2'] - st['2'] + 0.5, rms=-22, peak=-3,
       fo=0.4, what='tracks closing in')
    fx('sfx-killbots', SFX / 'fs824121-killbot-servo.mp3', st['3'], en['4'] - st['3'], src_in=1, rms=-32, fo=0.05,
       what='servo whine')
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', st['3'], en['4'] - st['3'], rms=-38, fo=0.03, what='CCTV hiss')
    # Beats 6-7: the tiled room.
    fx('sfx-rooms', SFX / 'fs767306-room-tiled-public-bathroom.mp3', st['6'], en['7'] - st['6'], src_in=10, rms=-42,
       fi=0.05, fo=0.05, what='tiled room tone')
    # Beat 8: hiss, the red flip, engines.
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', st['8'], en['8'] - st['8'], rms=-40, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', SFX / 'synth-killbot-red-flip.wav', m['flip8'] - 0.05, peak=-6, what='red flip tone')
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', m['flip8'], en['8'] - m['flip8'] + 0.4,
       src_in=20, rms=-24, fi=0.1, fo=0.4, what='engines, the chase')
    # 9a: the pass (V1 closest at ~2.8 s of the clip; the whoosh file peaks at 1.2 s, panned L->R: flipped, it exits
    # left). Placed in clip time, so they follow V1_IN.
    s = st['9a'] - V1_IN
    loop_wheels(fx, 'sfx-maddie', st['9a'], 3.0 - V1_IN, rms=-34, fi=0.1, fo=0.2, what='her wheels, trundling')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['9a'], 3.4 - V1_IN, rms=-26, fi=0.1, fo=0.6,
       what='tank tracks')
    fx('sfx-maddie', MS / 'derived-maddie-killbot-dust-whoosh.wav', s + 1.6, peak=-3, af='pan=stereo|c0=c1|c1=c0',
       what='kill bot dust whoosh, past her')
    fx('sfx-maddie', MS / 'derived-maddie-servo-turn-b.wav', s + 3.0, rms=-30, what='servo: she jolts')
    # 9b: inside the dust; grit falls as it clears; she is still.
    s = st['9b']
    fx('sfx-maddie', SFX / 'derived-dust-falling-12s.wav', s, en['9b'] - s, rms=-30, fi=0.05, fo=0.8,
       what='grit falling as the dust settles')
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, 2.0, src_in=30, rms=-34, fo=1.5,
       what='the kill bot, going away')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-oh.wav', s + 1.7, rms=-28, what='beep: startled "oh"')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-uh-oh.wav', s + 3.2, rms=-30, what='beep: uh-oh')
    # 10a: the far race.
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', st['10a'], en['10a'] - st['10a'], src_in=30,
       rms=-30, fi=0.2, fo=0.3, what='engines, far')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['10a'], en['10a'] - st['10a'], rms=-32, fo=0.3,
       what='tracks, far')
    # 11: hatch and antenna on V3; the far engines on each V8 cutaway; the beacon on the boss's words.
    fx('sfx-maddie', MS / 'derived-maddie-hatch-open.wav', m['s11'] + 0.02, rms=-26, what='hatch')
    fx('sfx-maddie', MS / 'derived-maddie-antenna-extend.wav', m['s11'] + 0.4, rms=-26, what='antenna extends')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-ack-double.wav', m['s11'] + 1.45, rms=-32, what='beep: line open')
    for a, z in m['v8cuts']:
        fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', a, z - a + 0.3, src_in=40, rms=-31,
           fi=0.05, fo=0.3, what='engines, far (cutaway)')
    for a, e, who in m['calls']:
        if who == 'ai':
            for k in np.arange(a, e, 0.9):
                fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-34, what='beacon on his words')
    # 10b: the close race.
    s = st['10b']
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, en['10b'] - s, src_in=10, rms=-30, fi=0.05,
       fo=0.2, what='engines, close')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, en['10b'] - s, rms=-30, peak=-3, fo=0.3,
       what='tracks, close')
    fx('sfx-killbots', SFX / 'fs189446-killbot-jet-flyby.mp3', s - 0.3, 2.5, src_in=4, rms=-32, peak=-3, fi=0.3, fo=0.8,
       what='two tear past the camera (under her line)')
    # 12: on board, the brake, STAND DOWN; the pack files away.
    s = st['12']
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, 3.9, src_in=20, rms=-21, fo=0.5,
       what='engine, on board')
    fx('sfx-killbots', SFX / 'fs824121-killbot-servo.mp3', s + 3.3, 1.4, src_in=1, rms=-24, fo=0.4, what='brakes')
    fx('sfx-killbots', SFX / 'fs132929-explosion-rubble-debris.mp3', s + 4.4, 2.6, rms=-30, fi=0.2, fo=1.0,
       what='grit and dust rolling over the hull')
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', s, 7.0, rms=-40, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', SFX / 'synth-killbot-red-flip.wav', m['peace'] - 0.05, peak=-8,
       af='asetrate=48000*1.26,aresample=48000', what='STAND DOWN flip tone (the red flip, pitched up)')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s + 7.0, 5.5, rms=-30, fi=0.3, fo=2.5,
       what='the pack files away')
    fx('sfx-wind', wind, s + 7.0, total - s - 7.0, src_in=20, rms=-36, fi=1.0, fo=0.5, what='wind on the downs')
    return mx


# ---------------------------------------------------------------- scene B

def scene_b():
    c = Cut('B', 'gpom-second-half-B-rough3', 'Cut 3 B Timeline', 'GPOM second half · cut 3 · scene B: Maddie at the door',
            'Scene B of cut 3, beats 14a-17b: Maddie at the bunker door, the tannoy, the doors open, the old lady, '
            'the door slams. '
            'Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you '
            "type. Tell Claude when you're done.")
    if D1:
        c.meta['intro'] = ('Scene B, round 2: the doorstep in your words, draft 2H from the dialogue page (your pick, 27 Oct): '
                           '"nobody really won", the time machine, only his data goes back, Sandra\'s "Amen", the thought '
                           'experiment, the hundred answering at once, Derek, "Come back tomorrow". Play it, click any '
                           'beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you type. Tell '
                           "Claude when you're done.")
    if D2:
        c.meta['intro'] = ('Scene B, round 3: the short doorstep, draft 2J from the dialogue page (your pick, 28 Oct, "The '
                           'price on the table"): no resistance. "There\'s a way we can fix this. Together." / "How\'s '
                           'that?", the time machine, it runs on them, Derek\'s "I\'m in", "Come back in the morning". Play '
                           'it, click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you '
                           "type. Tell Claude when you're done.")
    if BR:
        c.meta['intro'] = ('Scene B, round 4: the bridge (your call, 28 Oct: "by spelling it out it\'s boring, and removes '
                           'mystery"). No doorstep talk. Maddie asks for a quick chat; the old lady looks at her; the door '
                           'shuts on her; behind it, a hundred voices. Then scene C: they come out. Play it, click any '
                           'beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you type. Tell '
                           "Claude when you're done.")
    m = c.m
    t = 0.0
    # ---- 14a: she rolls up to the plain door
    b = c.beat('14a', 'Maddie at the door', t, act='The door',
               see='Maddie rolls up to the shut bunker door and settles. No wrecks, no smoke.')
    c.pic(V / 'cut3-V5.mp4', 0, t, t + 6.5, '14a')
    c.flags.append('Beat 14a (V5) was shot as a departure and reversed: she arrives facing slightly back the way she '
                   'came.')
    t = c.close(b, 6.5)

    # ---- 14b: the tannoy over Sandra and Derek, stopped dead mid-row; then the crowd looking up
    s = t
    b = c.beat('14b', 'The tannoy', s, act='The door',
               see="Maddie's voice on the tannoy over Sandra and Derek mid-row (we never see the speaker). They stop "
                   'dead. Cut to the crowd looking up.')
    p0, l0 = pick('14b', 0, phrase=0, fx=True)
    p1, l1 = pick('14b', 0, phrase=1, fx=True)
    a0 = fr(s + 1.0)  # click and whine first
    e0 = c.say('vox-tannoy', p0, a0, '14b', 'beat 14b phrase 0 (tannoy)', lufs=-17)
    a1 = fr(e0 + LINES[('14b', 0)]['gaps'][0]['seconds'])
    e1 = c.say('vox-tannoy', p1, a1, '14b', 'beat 14b phrase 1 (tannoy)', lufs=-17)
    c.line(b, 0, 'bot', a0, e1 - a0, LINES[('14b', 0)]['text'] + ' (on the tannoy)', 'kai')
    end = fr(e1 + TAIL + 0.6)
    cut1 = fr(s + 2.6)
    cut2 = fr(a1 - CUT_PRE)
    c.pic(V / 'cut3-lip-7-0-muted.mp4', 4.9, s, cut1, '14b', source=V / 'cut3-lip-7-0.mp4')
    c.pic(V / 'cut3-lip-7-1-muted.mp4', 2.6, cut1, cut2, '14b', source=V / 'cut3-lip-7-1.mp4')
    c.pic(V / 'cut2-N3.mp4', 0, cut2, end, '14b')
    c.flags.append('Beat 14b: Sandra and Derek "stopped dead" are the silent ends of their talking clips (7-0 after '
                   'her line, 7-1 after his), muted: no new footage of them stopping exists.')
    m['s14b'], m['tan'], m['rowpic'] = s, (a0, e1), (s, cut2)
    t = c.close(b, end)

    # ---- 15: hard cut, the doors already open, Maddie rolls in
    s = t
    b = c.beat('15', 'Hello', s, act='The door',
               see='Hard cut: the doors already open, Maddie rolls in. We do not see the humans properly yet.')
    tt = s + LEAD
    for i in (0, 1):
        tk, letter = pick('15', i)
        e = c.say('vox-maddie', tk, tt, '15', f'beat 15 line {i} bot')
        c.line(b, i, 'bot', tt, e - tt, LINES[('15', i)]['text'], 'kai')
        tt = e + GAP
    end = fr(max(s + 4.0, tt - GAP + TAIL))
    # Kai's note at772 (round 1): Maddie OUTSIDE the doors, in the beat-17 doorway shot. Kai's pick (23 Oct, picks
    # page b2-15): v1, still b15-hello-outside-2-a with its bunting made small and calm, animated with her staying on
    # the threshold (Omni 1.1 Flash, 8 s). She hardly moves, so the ping-pong past 8 s does not show.
    c.pic(V / 'cut3-B15r4-v1-calm-bunting.mp4', 0.0, s, end, '15')
    m['s15'] = s
    t = c.close(b, end)

    # ---- 17: shot / reverse shot. The old lady (lip-synced, her voice in the clips) and Maddie (V11).
    s17 = t
    b = c.beat('17', 'The old lady and Maddie', s17, act='The meeting',
               see='The old lady among the crowd, the others in shadow; Maddie over her shoulder in the big doorway. '
                   'Shot / reverse shot.')
    v11 = V / 'cut3-V11.mp4'
    BY = {0: 'kai', 1: 'kai', 2: 'kai', 3: 'kai'}
    lady = []
    if BR:
        # The bridge: no words. The old lady (her back to us) looks at the robot in her doorway; the door shuts on it.
        # Behind the shut door, the hundred decide, unheard (17b). Scene C opens on them coming out.
        b['title'], b['act'] = 'The look', 'The door'
        b['see'] = ('The old lady from behind, looking at Maddie small in the big doorway. Nobody speaks. Then the door '
                    'shuts.')
        look = 3.5
        c.pic(v11, 0.0, s17, s17 + look, '17')
        m['l17_0'], m['lady'], m['s17'] = s17 + 1.2, lady, s17
        slam = fr(s17 + look)
        m['slam'] = m['turn'] = slam
        t = c.close(b, slam)
        b = c.beat('17b', 'Behind the door', t, act='The door',
                   see='Outside: Maddie alone at the shut steel door, waiting. Behind it, muffled, a hundred voices '
                       'start up: the vote, heard but not understood. Hard cut to scene C: the door open, them coming '
                       'out.')
        hold = 6.0
        # V5's tail still drifts (she was shot driving off, reversed), so she waits on its settled frame (6.45 s) with
        # a slow push towards the door: the camera moves, she doesn't.
        wait = V / 'cut3-V5-wait-push.mp4'
        if not wait.exists():
            n = int(round(hold * FPS))
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', '6.45', '-i', str(V / 'cut3-V5.mp4'),
                            '-frames:v', '1', '-vf', f"scale=5120:2880,zoompan=z='1+0.06*on/{n}':d={n}:"
                            "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1280x720:fps=24", *ENC, str(wait)],
                           check=True)
        c.pic(wait, 0.0, t, t + hold, '17b', source=V / 'cut3-V5.mp4')
        c.flags.append('Beat 17 and 17b, round BR (the bridge, Kai 28 Oct): the doorstep talk is cut. Beat 17 is a '
                       f'{look:g} s silent hold on V11 (her back, Maddie in the doorway); 17b is V5\'s settled frame '
                       '(Maddie at the shut door) with a slow 6% push, made in ffmpeg: a still, so she does not move. No '
                       'new Flow footage. The vote is muffled walla (fs653920) behind the door, no words.')
        t = c.close(b, t + hold)
        c.total = t
        return c

    def lip(name, t0, i0, out):
        wav, at, end_, ph = lipinfo(name)
        c.pic(V / f'cut3-lip-{name}-muted.mp4', i0, t0, t0 + out - i0, '17', source=V / f'cut3-lip-{name}.mp4')
        lady.append((t0, i0, out))
        return wav, at, end_

    def dub(wav, t0, i0, i1, what):
        c.dub('vox-lady', wav, i0, i1, t0, what, chain=[CORRIDOR])

    # 17-0, cut to Maddie for its last 0.3 s (the voice overruns the mouth)
    wav, at, end_, ph0 = lipinfo('17-0')
    if D2:  # 2J keeps only her first sentence: the take and its mouth stop after "loved."
        end_ = ph0[0][2]
    i0 = at - LEAD
    mouth_end = end_ - 0.32
    lip('17-0', s17, i0, mouth_end)
    dub(wav, s17, i0, end_ + 0.1, 'beat 17 line 0 lady (lip-sync dub)')
    l0a, l0e = s17 + LEAD, s17 + end_ - i0
    c.line(b, 0, 'lady', l0a, l0e - l0a, ph0[0][0] if D2 else LINES[('17', 0)]['text'], BY[0])
    v11_a = fr(s17 + mouth_end - i0)

    def maddie_line(i, tt, phrases=None):
        r = LINES[('17', i)]
        if 'phrases' in r:
            a = tt
            for p in range(len(r['phrases'])):
                tk, _ = pick('17', i, phrase=p)
                tt = c.say('vox-maddie', tk, tt, '17', f'beat 17 line {i} phrase {p} bot', chain=[CORRIDOR])
                if p + 1 < len(r['phrases']):
                    tt += r['gaps'][p]['seconds']
            c.line(b, i, 'bot', a, tt - a, r['text'], BY[i])
            return tt
        tk, _ = pick('17', i)
        e = c.say('vox-maddie', tk, tt, '17', f'beat 17 line {i} bot', chain=[CORRIDOR])
        c.line(b, i, 'bot', tt, e - tt, r['text'], BY[i])
        return e

    if D1:
        # Round D1 (27 Oct): draft 2H from the dialogue page, Kai's pick. Words: scene B's script.json; takes and picks:
        # voices-d1.json (voice3.py --round D1). Line 0 keeps its lip-synced take; everything after it plays on V11
        # (Maddie past the old lady's shoulder, her back to us, so no lip-sync owed), except the hundred answering at
        # once, which cuts to them looking up (N3, as in 14b). Sandra, Derek and the hundred are off screen, down the
        # corridor behind her (OFF on top of the corridor's room, and quieter).
        script = json.loads((S.SCENES / 'second-half-b-the-door' / 'script.json').read_text())
        rows = {r['i']: r for r in json.loads((S.SCENES / 'second-half-b-the-door' / f'voices-{TAG}.json').read_text())['lines']}
        # the gap before a line: Sandra's "Amen" and the hundred come in quick, the old lady's "Derek." snaps, the
        # rushed last line is tight; Maddie lets "Amen" land before her thought experiment
        before = {6: 0.45, 13: 0.25, 14: 0.7, 15: 0.3, 16: 0.4, 18: 0.15, 20: 0.2}
        if D2:  # 2J: "How's that?" comes straight back; Derek jumps in quick, her "Derek." snaps, then a beat before
            # "Come back in the morning."
            before = {2: 0.3, 6: 0.25, 7: 0.15, 8: 0.6}
        e, crowd = l0e, None
        for i, ln in enumerate(script['lines']):
            if i == 0 or ln['who'] == 'sfx':
                continue
            row, who, off = rows[i], ln['who'], bool(ln.get('off'))
            chain, lufs = ([CORRIDOR, OFF], -19.0) if off else ([CORRIDOR], -16.0)
            a = tt = e + before.get(i, GAP)
            if who == 'crowd':
                tt = c.say(STEM[who], Take(V3 / row['stack']), a, '17',
                           f'beat 17 line {i}: the hundred answer at once (six voices stacked)', chain=chain, lufs=-18.0)
                crowd = (fr(a - CUT_PRE), fr(tt + 0.4))
            else:
                for take, g in d1_takes(row):
                    tt = c.say(STEM[who], take, tt, '17', f'beat 17 line {i} {who}' + (' (off)' if off else ''),
                               chain=chain, lufs=lufs) + g
            c.line(b, i, who, a, tt - a, shown(ln['text']), ln['by'])
            e = tt
        slam = fr(e + 0.25)
        if crowd:
            c.pic(v11, 0.0, v11_a, crowd[0], '17')
            c.pic(V / 'cut2-N3.mp4', 1.0, crowd[0], crowd[1], '17')
            c.pic(v11, 3.0, crowd[1], slam, '17')
            v11_b = crowd[1]
        else:  # 2J: no crowd answer, so V11 (Maddie past her shoulder) holds to the door
            c.pic(v11, 0.0, v11_a, slam, '17')
            v11_b = v11_a
    else:
        e = maddie_line(1, l0e + GAP)
        e = maddie_line(2, e + GAP)
        # 17-3 on her
        wav, at, end_, _ = lipinfo('17-3')
        i0 = at - CUT_PRE
        t3 = fr(e + GAP - CUT_PRE)
        c.pic(v11, 0.0, v11_a, t3, '17')
        out = end_ + 0.2
        lip('17-3', t3, i0, out)
        dub(wav, t3, i0, out, 'beat 17 line 3 lady (lip-sync dub)')
        l3a = t3 + at - i0
        c.line(b, 3, 'lady', l3a, end_ - at, LINES[('17', 3)]['text'], BY[3])
        v11_b = fr(t3 + out - i0)
        # 17-4 .. 17-13: Kai's 23 Oct words (the debate folded in), voiced in round B2 (voice3.py --round B2, picks in
        # scenes/second-half-b-the-door/voices.json). No new picture yet: everything after 17-3 plays on V11 (Maddie past
        # the old lady's shoulder), ping-ponged, including the old lady's new lines (her back is to us; no lip-sync owed
        # for the rough). [pause] / [big pause] are the phrase gaps from voices.json.
        by = {ln['i']: ln for ln in VOICES_B['lines']}

        def new_line(i, tt):
            ln, a = by[i], tt
            who = ln['who']
            for p, ph in enumerate(ln['phrases']):
                tk = Take(V3 / next(t['file'] for t in ph['takes'] if t['take'] == ph['pick']))
                tt = c.say(f"vox-{'maddie' if who == 'bot' else 'lady'}", tk, tt, '17',
                           f"beat 17 line {i}" + (f" phrase {p}" if len(ln['phrases']) > 1 else '') + f" {who}",
                           chain=[CORRIDOR])
                if p + 1 < len(ln['phrases']):
                    tt += ln['gaps'][p]['seconds']
            c.line(b, i, who, a, tt - a, ln['text'], 'kai')
            return tt

        e = l3a + (end_ - at)
        for i in range(4, 14):
            # 17-11 opens on '...Yeah.': a beat of her taking the hit first; 17-13 is rushed, so it comes in tight
            e = new_line(i, e + {11: GAP + 0.6, 13: 0.2}.get(i, GAP))
        slam = fr(e + 0.25)
        c.pic(v11, 3.0, v11_b, slam, '17')
    m['slam'] = slam
    t = c.close(b, slam)

    # ---- 17b: the door slams; Maddie rolls away down the hill (Kai, 23 Oct). Kai's pick (picks page b2-17b): v1,
    # still b17b-turn-away-2-a with calm bunting; the re-roll b17b-v1-r2, where she drives down towards us in her own
    # tracks and passes out of frame at about 7.3 s, leaving the empty hill. All 8 s play, then hard cut to scene C.
    b = c.beat('17b', 'Maddie turns away', t, act='The meeting',
               see='The door slams. Maddie rolls away from the shut bunker door, down the hill towards us and out of '
                   'frame: the humans will have time. Then hard cut to scene C.')
    hold = 8.0
    c.pic(V / 'shb-b17b-v1-r2-shb-b17b-v1-calm-bunting.mp4', 0.0, t, t + hold, '17b')
    if D2:
        c.flags.append('Beat 17, round D2: draft 2J from the dialogue page (your pick, 28 Oct: "The price on the table"). '
                       'Her first line keeps its lip-synced take, cut after "loved."; her "Derek." reuses its 2H take; every '
                       'other line is new, picked by measurement (voices-d2.json), nobody has listened. Picture: V11 '
                       '(Maddie past her shoulder) under all the talk; her new lines are on her back, not lip-synced.')
    elif D1:
        c.flags.append('Beat 17, round D1: draft 2H from the dialogue page (your pick, 27 Oct; Sandra says only "Amen"). '
                       'Her first line keeps its lip-synced take; every other line is new, picked by measurement '
                       '(voices-d1.json), nobody has listened. Picture: V11 (Maddie past her shoulder) ping-ponged under '
                       'the talk, cut to the hundred looking up (N3) while they all answer at once. Her new lines are on '
                       'her back, not lip-synced; new coverage of her face is owed if you want it.')
    else:
        c.flags.append('Beat 17: everything after the old lady\'s second line plays on V11, ping-ponged (about '
                       f'{t - v11_b:.0f} s): her new lines (17-6, 8, 10, 13) are on her back, not lip-synced; new '
                       'coverage of her face is owed if Kai wants it.')
    m['s17'], m['lady'], m['turn'] = s17, lady, t
    m['l17_0'] = l0a
    t = c.close(b, t + hold)
    c.total = t
    return c


def audio_b(c):
    m, total = c.m, c.total
    mx = C.Mix(total)
    voices(c, mx)
    fx = sfx_adder(mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}
    # ---- music: M6 Maddie's theme from 14a, under the tannoy (ducked) and the doors, out on the old lady's
    # first line (cut 2's placement, retimed). No music under the lip-synced conversation, as cut 2.
    m6_end = m['l17_0'] + 0.4
    d = m6_end
    x = C.level(C.decode(C.MUSIC['M6'], 0, d), rms=-26, peak=-3)
    a0, e1 = m['tan']
    x *= C.env(len(x), [(0, 0), (0.8, 1), (a0 - 0.2, 1), (a0 + 0.2, 0.6), (e1, 0.6), (e1 + 0.5, 1), (d - 1.5, 1),
                        (d, 0)])
    mx.add('mus-M6-maddie', x, 0.0, C.MUSIC['M6'], "M6 Maddie's theme")
    # ---- sfx
    wind = wind_file()
    fx('sfx-wind', wind, 0, en['14a'], src_in=10, rms=-36, fi=0.8, fo=0.05, what='wind on the downs')
    loop_wheels(fx, 'sfx-maddie', 0.0, 3.7, rms=-30, fi=0.3, fo=0.05, what='her wheels, rolling up')
    fx('sfx-maddie', MS / 'derived-maddie-wheels-stop.wav', 3.6, rms=-30, what='wheels stop')
    fx('sfx-maddie', SFX / 'fs701647-bunting-fabric-flap.mp3', 0, en['14a'], rms=-36, fi=0.3, fo=0.5,
       what='bunting flapping')
    fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', 5.5, rms=-34, what='beacon blip')
    s = st['14b']
    r0, r1 = m['rowpic']
    fx('sfx-rooms', SFX / 'fs767306-room-tiled-public-bathroom.mp3', r0, r1 - r0, src_in=10, rms=-42, fi=0.05, fo=0.1,
       what='tiled room tone')
    fx('sfx-tannoy', SFX / 'synth-tannoy-click.wav', s + 0.1, peak=-8, what='tannoy click')
    fx('sfx-tannoy', SFX / 'fs489566-tannoy-feedback-short.mp3', s + 0.3, rms=-26, peak=-10, fo=0.3,
       what='feedback whine')
    fx('sfx-tannoy', SFX / 'fs530037-tannoy-pa-static.mp3', s + 0.2, e1 - s + 0.2, src_in=10, rms=-38, fi=0.2, fo=0.3,
       what='crackle')
    fx('sfx-tannoy', SFX / 'synth-tannoy-click.wav', e1 + 0.25, peak=-10, what='tannoy click off')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', r1, en['15'] - r1, rms=-40, fi=0.4, fo=1.0,
       what='the crowd shifting')
    s = st['15']
    loop_wheels(fx, 'sfx-maddie', s, 2.0, rms=-32, fi=0.1, fo=0.05, what='wheels on concrete')
    fx('sfx-maddie', MS / 'derived-maddie-wheels-stop.wav', s + 1.95, rms=-32, what='wheels stop')
    fx('sfx-maddie', SFX / 'fs701647-bunting-fabric-flap.mp3', s, en['15'] - s, src_in=4, rms=-38, fi=0.5, fo=0.8,
       what='bunting')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-hello.wav', s + 0.05, rms=-32, what='beep: hello')
    s = st['17']
    fx('sfx-rooms', SFX / 'fs767306-room-tiled-public-bathroom.mp3', s, en['17'] - s, src_in=40, rms=-44, fi=0.3,
       fo=0.6, what='corridor tone')
    fx('sfx-wind', wind, s, en['17'] - s, src_in=30, rms=-44, fi=0.5, fo=0.6, what='wind through the open doors')
    if BR:  # the bridge: the look, the slam, then outside at the shut door with the hundred muffled behind it
        fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', s + 1.4, rms=-36, what='servo: she tilts up to her')
        t = m['turn']
        fx('sfx-door', SFX / 'fs406197-blastdoor-metal-slam.mp3', t - 0.30, rms=-20, peak=-3, fo=0.4,
           what='the door shuts on her')
        fx('sfx-wind', wind, t, en['17b'] - t, src_in=40, rms=-34, fi=0.05, fo=0.3, what='wind on the downs, outside')
        fx('sfx-crowd', SFX / 'fs653920-crowd-small-walla.mp3', t + 0.8, en['17b'] - t - 0.8, src_in=5, rms=-40,
           fi=2.0, fo=0.15, af=MUFFLED, what='behind the door: a hundred voices, the vote, no words')
        fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', t + 2.6, rms=-36, what='servo: she waits')
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', t + 4.2, rms=-36, what='beacon blip')
        c.flags.append('Beat 17b: the shut is fs406197 (the slam, CC0), its hit on the cut; the voices behind the door '
                       'are fs653920 (crowd walla) through the muffled filter, rising, cut dead on the cut to scene C.')
        return mx
    for k in np.arange(s + 9.0, en['17'] - 3.0, 13.0):  # every 13 s through the talk
        fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', k, rms=-36, what='servo: she nudges')
    # ---- 17b: the slam (fs406197, its hit at 0.30 s, lands on the cut to outside), then the downs: wind, her wheels
    # coming closer as she drives past us (out of frame at about 7.3 s), her beacon
    t = m['turn']
    fx('sfx-door', SFX / 'fs406197-blastdoor-metal-slam.mp3', t - 0.30, rms=-20, peak=-3, fo=0.4, what='the door slams')
    if D1:  # 2H: "behind it, voices start up": the hundred through the shut steel door, fading as she rolls away
        fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', t + 0.2, 5.0, src_in=20, rms=-44, fi=0.3, fo=2.5,
           af=MUFFLED, what='behind the door: the hundred start talking')
    fx('sfx-wind', wind, t, en['17b'] - t, src_in=40, rms=-34, fi=0.05, fo=0.6, what='wind on the downs, outside')
    loop_wheels(fx, 'sfx-maddie', t + 0.3, 7.0, rms=-30, fi=2.5, fo=0.6, what='wheels: she drives past us')
    fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', t + 3.4, rms=-36, what='beacon blip')
    c.flags.append('Beat 17b: the door slam is fs406197 (CC0, already credited in sfx/CREDITS.md), placed so its hit '
                   'lands on the cut; the hello beep under "Hello!" in 15 is my addition to Maddie\'s sound kit.')
    return mx


# ---------------------------------------------------------------- shared audio

def wind_file():
    p = AU / 'cut2' / 'src' / 'synth-wind-60s.wav'
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i',
                        'anoisesrc=d=60:c=brown:r=48000:a=0.6,highpass=f=60,lowpass=f=700,tremolo=f=0.12:d=0.7,'
                        'aformat=channel_layouts=stereo', str(p)], check=True)
    return p


def sfx_adder(mx):
    def fx(stem, p, t, dur=None, src_in=0.0, rms=None, peak=None, fi=0.0, fo=0.0, af=None, what='', tile=False):
        x = C.decode(p, src_in, None if tile else dur, af)
        if tile and dur:
            n = int(round(dur * SR))
            x = np.tile(x, (int(np.ceil(n / len(x))), 1))[:n]
        x = C.fades(C.level(x, rms, peak), fi, fo)
        mx.add(stem, x, t, p, what or pathlib.Path(p).stem)
    return fx


def loop_wheels(fx, stem, t, d, what, **kw):
    """Her 8 s seamless wheel loop, as long as needed."""
    fx(stem, MS / 'derived-maddie-wheels-loop-8s.wav', t, d, what=what, tile=True, **kw)


_lufs = {}


def lufs_of(x):
    key = (x.shape, float(np.abs(x).sum()))
    if key not in _lufs:
        tmp = ROOT / '_lufs.wav'
        C.write_wav(tmp, x)
        try:
            _lufs[key] = C.integrated(tmp)
        except (IndexError, ValueError):
            _lufs[key] = C.rms_db(x)
        tmp.unlink()
    return _lufs[key]


def voices(c, mx):
    """Every take at its loudness, rooms on it, sample-aligned (gain only: nothing here shifts time). Each placed line
    is also written as its own file (lines/NN-<stem>.wav, filters and loudness baked in, before the mix gain) so a
    Premiere build can put every voice on its own track and slide it by eye."""
    ldir = c.dir / 'lines'
    ldir.mkdir(exist_ok=True)
    for p in ldir.glob('*.wav'):
        p.unlink()
    for k, v in enumerate(c.voices):
        af = ','.join(v['chain']) or None
        if v.get('whole'):
            # a lip dub: one gain for the whole dub (measured on its speech), then the window
            full = C.decode(v['src'], 0, None, af)
            g = 10 ** ((v['lufs'] - lufs_of(full)) / 20)
            a = int(round(v['i'] * SR))
            x = full[a:a + int(round(v['d'] * SR))] * g
            x = C.fades(x, 0.01, 0.03)
        else:
            x = C.decode(v['src'], v['i'], v['d'] + (0.4 if af else 0.0), af)  # rooms ring on a little
            x = x * 10 ** ((v['lufs'] - lufs_of(x)) / 20)
            x = C.fades(x, 0.005, 0.03)
            if v['cut'] is not None:
                stop = v['cut'] - v['t']
                if stop <= 0:
                    continue
                x = x[:int(stop * SR)]
                x = x * C.env(len(x), [(0, 1), (max(0, stop - 1.5), 1), (stop, 0)])[:len(x)]
        mx.add(v['stem'], x.astype(np.float32), v['t'], v['src'], v['what'])
        v['line_file'] = str(ldir / f"{k:02d}-{v['stem']}.wav")
        C.write_wav(pathlib.Path(v['line_file']), x)


def write(c, mx):
    stems_dir = c.dir / 'stems'
    stems_dir.mkdir(parents=True, exist_ok=True)
    for p in stems_dir.glob('*.wav'):
        p.unlink()
    n = int(round(c.total * SR))
    summed = sum(s[:n] for s in mx.stems.values())
    tmp = c.dir / 'mix-raw.wav'
    C.write_wav(tmp, summed)
    lufs = C.integrated(tmp)
    g = 10 ** ((-16.0 - lufs) / 20)
    tracks = []
    order = sorted(mx.stems, key=lambda k: (['vox', 'mus', 'sfx'].index(k.split('-')[0]), k))
    for k, name in enumerate(order):
        p = stems_dir / f'{k + 1:02d}-{name}.wav'
        C.write_wav(p, mx.stems[name][:n] * g)
        tracks.append(dict(track=f'A{k + 1}', name=name, file=str(p), start=0.0,
                           peak_db=round(float(20 * np.log10(np.max(np.abs(mx.stems[name][:n] * g)) + 1e-12)), 1)))
    C.write_wav(tmp, summed * g)
    mix = c.dir / 'mix.wav'
    # true-peak-ish ceiling: 4x oversampled limiter at -2 dBFS (room for the AAC encode), then back to 48 kHz
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(tmp), '-af',
                    'aresample=192000,alimiter=limit=0.794:level=false:attack=2:release=60,aresample=48000',
                    '-c:a', 'pcm_s24le', str(mix)], check=True)
    tmp.unlink()
    got = C.integrated(mix)
    print(f'{c.key}: mix {got:.1f} LUFS (raw {lufs:.1f}, gain {20 * np.log10(g):+.1f} dB), {len(tracks)} stems')
    # the HUD meters read the stems they listen to, exactly as placed
    for h in c.huds:
        a, b = int(round(h['t0'] * SR)), int(round((h['t0'] + h['d']) * SR))
        x = sum(mx.stems[s][a:b] for s in h['meter'] if s in mx.stems)
        h['wav'] = str(c.dir / 'hud' / f"{h['name']}-meter.wav")
        C.write_wav(pathlib.Path(h['wav']), x)
    return tracks, mix


def make_huds(c):
    for h in c.huds:
        src = pathlib.Path(h['src'])
        base = src
        if h['d'] > dur(src) + 0.5 / FPS:
            base = pingpong(src, 0.0, h['d'], c.vdir / f"{src.stem}-i0-d{h['d']:.3f}.mp4")
        out = c.vdir / f"{h['name']}.mp4"
        trimmed = c.vdir / f"{h['name']}-base.mp4"
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{h.get('ss', 0.0):.4f}", '-i', str(base), '-t', f"{h['d']:.4f}", '-vf',
                        f'fps={FPS}', *ENC, str(trimmed)], check=True)
        subprocess.run([sys.executable, str(HERE / 'hud.py'), str(trimmed), str(out), '--audio', h['wav'],
                        '--no-audio-out', *h['args']], check=True)
        trimmed.unlink()
        if base != src:
            for cl in c.video:
                if cl.get('hud') == h['name']:
                    cl['looped'] = True


def edl(c, tracks, mix, mx):
    beats = [{k: b[k] for k in ('id', 'title', 'start', 'dur', 'see', 'act', 'lines')} for b in c.beats]
    for b in beats:
        b['lines'].sort(key=lambda x: (x['t'] is None, x['t'] or 0, x['i']))
    video = [{k: v[k] for k in ('file', 'in', 'dur', 'start', 'beat', 'source', 'looped')} for v in c.video]
    data = dict(sequence=c.seq, **c.meta, fps=FPS, sample_rate=SR, total=c.total, beats=beats, video=video,
                audio=tracks, mix=str(mix), events=mx.events,
                voices=[{k: v.get(k) for k in ('stem', 'src', 'i', 'd', 't', 'chain', 'lufs', 'what', 'cut', 'line_file')}
                        for v in c.voices],  # per-line placements (source in-point i), for a Premiere build
                flags=c.flags + [
                    'Nobody has listened to this cut: every level, duck and sound placement is measured, not heard.'],
                preview=str(c.dir / 'preview.mp4'))
    (c.dir / 'edl.json').write_text(json.dumps(data, indent=1, ensure_ascii=False))
    return data


# Flow's clips are limited range with overshoots (luma 3-245) and the HUD's black panels reach 0: clamp to
# legal limited range (16-235 luma, 16-240 chroma) so tag and content agree (docs/video-fx/delivery.md).
LEGAL = ',format=yuv420p,limiter=min=16:max=235:planes=1,limiter=min=16:max=240:planes=6'


def preview(c, data):
    parts = c.dir / 'preview-parts'
    parts.mkdir(exist_ok=True)
    lst = []
    for k, v in enumerate(data['video']):
        out = parts / f'{k:03d}.mp4'
        n = int(round(v['dur'] * FPS))
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{v['in']:.4f}", '-i', v['file'],
                        '-vf', f'scale=1280:720,fps={FPS},setsar=1', '-frames:v', str(n), *ENC, str(out)], check=True)
        lst.append(f"file '{out}'")
    (parts / 'list.txt').write_text('\n'.join(lst) + '\n')
    pic = parts / 'picture.mp4'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(parts / 'list.txt'),
                    '-c', 'copy', str(pic)], check=True)
    draw = ','.join(
        f"drawtext=text='{b['id']}':x=w-tw-16:y=12:fontsize=22:fontcolor=white@0.7:box=1:boxcolor=black@0.4:"
        f"enable='between(t,{b['start']:.3f},{b['start'] + b['dur'] - 0.001:.3f})'" for b in data['beats'])
    out = c.dir / 'preview.mp4'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(pic), '-i', data['mix'], '-map', '0:v', '-map',
                    '1:a', '-vf', draw + LEGAL, '-c:v', 'libx264', '-crf', '20', '-preset', 'medium',
                    '-r', str(FPS), '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709',
                    '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '256k', '-ar', str(SR), '-movflags', '+faststart',
                    '-shortest', str(out)], check=True)
    tot = probe(out)
    sheet = c.dir / 'preview-sheet.jpg'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(out), '-vf',
                    f"select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,{tot / 48:.3f})',scale=320:-2,"
                    "drawtext=text='%{pts\\:hms}':x=6:y=6:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.5,"
                    "tile=6x8", '-vsync', 'vfr', '-frames:v', '1', str(sheet)], check=True)
    for p in parts.glob('*'):
        p.unlink()
    parts.rmdir()
    print(f'{out} {tot:.2f}s; sheet {sheet}')


def run(key, do_preview=True):
    c = scene_a() if key == 'A' else scene_b()
    c.extend()
    mx = audio_a(c) if key == 'A' else audio_b(c)
    tracks, mix = write(c, mx)
    make_huds(c)
    data = edl(c, tracks, mix, mx)
    print(f'{c.key}: total {c.total:.2f}s, {len(c.video)} clips, {len(tracks)} stems')
    for b in data['beats']:
        print(f"  beat {b['id']:>3} {b['start']:7.2f} +{b['dur']:6.2f}  {b['title']}")
    if do_preview:
        preview(c, data)


if __name__ == '__main__':
    keys = [a for a in sys.argv[1:] if not a.startswith('--') and a != TAG] or ['A', 'B']
    for k in keys:
        run(k, '--no-preview' not in sys.argv)
