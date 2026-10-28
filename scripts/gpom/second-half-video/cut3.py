#!/usr/bin/env python3
"""GPOM second half, cut 3: two rough cuts in the new-scene timeline format (scripts/scene/timeline.py).

    python3 scripts/gpom/second-half-video/cut3.py A          # scene A, the kill bots (beats 0-12; round 3)
    python3 scripts/gpom/second-half-video/cut3.py B          # scene B, Maddie at the door (14a-17b; round B2)
    python3 scripts/gpom/second-half-video/cut3.py A B --no-preview
    python3 scripts/gpom/second-half-video/cut3.py A B --tag d1   # Kai's dialogue-page picks (1D, 2H), 27 Oct

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
D1 = TAG in ('d1', 'd2')  # the dialogue-page rounds: d1 = drafts 1D + 2H (27 Oct), d2 = draft 2J (28 Oct, scene B)
D2 = TAG == 'd2'
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
    d = json.loads((LIP / f'cut3-lip-{name}-phrases.json').read_text())
    ph = [(p['text'], p['at'], p['at'] + (p['to'] - p['from']) / p['tempo']) for p in d['phrases']]
    return LIP / f'cut3-lip-{name}-dub.wav', ph[0][1], max(p[2] for p in ph), ph


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


def beat0_d1():
    """(phrases [(Take, gap after, text, line)], lines [(i, text, by)]) for beat 0 in draft 1D."""
    script = json.loads((S.SCENES / 'second-half-a-killbots' / 'script.json').read_text())
    rows = {r['i']: r for r in json.loads((S.SCENES / 'second-half-a-killbots' / 'voices-d1.json').read_text())['lines']}
    seq, lines = [], []
    for i, ln in enumerate(script['lines']):
        tk = d1_takes(rows[i])
        for p, (take, g) in enumerate(tk):
            last = p == len(tk) - 1
            seq.append((take, D1_LINE_GAP.get(i, 0.0) if last else g, rows[i]['phrases'][p]['text'], i))
        lines.append((i, shown(ln['text']), ln['by']))
    return seq, lines


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
    m = c.m

    # ---- 0: the continuous travelling shot (eight chained clips), ~5 s of radio first, Kai's new opening
    v6 = V / 'cut3-beat0-continuous-x.mp4'
    graded, note = regrade_v6(v6, c.vdir / 'cut3-beat0-continuous-x-graded.mp4')
    c.flags.append(note.replace('six chained clips', 'eight chained clips').replace('48 s', '64 s'))
    if D1:
        seq, d1_lines = beat0_d1()
    else:
        seq = [(Take(p), g, text, k) for k, (p, g, text) in enumerate(BEAT0)]
    span = sum(tk.d + g for tk, g, _, _ in seq)
    have = dur(v6)
    lead = fr(min(6.5, max(5.0, have - span - 1.5)))
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
    else:
        c.flags.append(f'Beat 0: {lead:.2f} s of Maddie rolling with her radio before "Oh, hello!" (Kai asked for about '
                   f'5 s). Her twelve phrases with Kai\'s pauses (1.6 s after "Oh, hello!", 2.5 s after "...he misses '
                   f'you") run {span:.1f} s; the 8-clip shot ({have:.1f} s) is cut {end0 - talk_end:.1f} s after "Mind how '
                   f'you go", {have - end0:.1f} s before its own end. Speech is not slowed.')
    if not D1:
        c.flags.append('Beat 0 takes: Kai\'s audition picks for the new phrases ("Oh, hello!" c, "didn\'t notice you" a, '
                   '"racket down" a, "It\'s his tune" c, "Anyway..." a); the unchanged phrases keep their round-0 takes. Whisper '
                   'hears take c of "It\'s his tune" as "This is June" (takes a and b are there if your ear agrees).')
    c.pic(graded, 0.0, 0.0, end0, '0', source=v6)
    if D1:  # by phrase text: "Sorry about the racket." is where the radio goes down
        at = {text: st for (_, _, text, _), st in zip(seq, starts)}
        m['hello'], m['racket'], m['bye'] = starts[0], at['Sorry about the racket.'], starts[-1]
        m['went'], m['mattered'] = at['went.'], at['We understand that now...']
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
    rows = [('6', 'woman', '6-0', '6-0', LINES[('6', 0)]['text']),
            ('7', 'man', '7d-0c', '7d-0', 'Oh, sorry, sorry, love.'),
            ('7', 'woman', '7-0', '7-0', LINES[('7', 0)]['text']),
            ('7', 'man', '7d-1c', '7d-1', 'But the world ended, Sandra!'),
            ('7', 'woman', '7-2', '7-2', LINES[('7', 2)]['text'])]
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
    tt = s11 + 2.0  # the antenna first
    starts = []
    for k, (who, src, text) in enumerate(calls):
        if who == 'ai':
            tk, chain, text = Take(SUNO_A / BOSS[src]), [SPEAKER], BOSS_TEXT[src]
            e = c.say('vox-ai', tk, tt, '11', f'beat 11 boss line {src}', chain=chain, lufs=-17)
        else:
            tk = Take(src)
            e = c.say('vox-maddie', tk, tt, '11', f'beat 11 Maddie {k // 2}')
        c.line(b, k, who, tt, e - tt, text, 'kai')
        starts.append((tt, e, who))
        tt = e + GAP
    end11 = fr(starts[-1][1] + TAIL)
    # V3 throughout, with a 2.25 s cutaway to the far race (V8) on the boss's first and last lines
    a1, a3 = fr(starts[1][0] - CUT_PRE), fr(starts[5][0] - CUT_PRE)
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
    peace = 3.6
    c.huds.append(dict(name='hud-12', src=str(v4), d=7.0, args=['--state', 'kill', '--lock', '0',
                                                                 '--flip-to', f'peace@{peace}'],
                       meter=['sfx-killbots'], t0=s12))
    c.pic(c.vdir / 'hud-12.mp4', 0.0, s12, s12 + 7.0, '12', source=v4, hud='hud-12')
    c.pic(V / 'cut3-V10r.mp4', 0, s12 + 7.0, s12 + 12.5, '12')
    s_v3 = fr(s12 + 12.5)
    tk = Take(pathlib.Path(A3['media']) / MADDIE12['file'])
    e = c.say('vox-maddie', tk, s_v3 + LEAD, '12', 'beat 12 Maddie: Good job. That was close.')
    c.line(b, 0, 'bot', s_v3 + LEAD, e - s_v3 - LEAD, 'Good job. [pause] That was close.', 'kai')
    end12 = fr(e + TAIL + 0.4)
    c.pic(v3, 3.0, s_v3, end12, '12')
    c.flags.append('Beat 12: the HUD now reads STAND DOWN (status RETURN TO PATROL), drawn by hud.py in ffmpeg. V10r '
                   '(Kai\'s pick A) plays 0-5.5 s: they file away one at a time; cut before the nearest bot grows its '
                   'long gun barrel (~5-7 s). They still never visibly turn (the still already has them facing away).')
    c.flags.append('Beat 12 (round 3, Kai at4098): the boss\'s last line is gone; Maddie says "Good job." (pause) "That was '
                   'close." (round 3b, Kai at4138: "boss" cut out of the take, not re-voiced). Take a of four (voices.json): her cheeky Style/Pace replaced for this line, a soft '
                   '"Whew." from the [sighs] tag, its 4.25 s pause cut to ~1.85 s. Take c is the clean one without the sigh.')
    m['s12'], m['peace'], m['s_v3'], m['l12'] = s12, fr(s12 + peace), s_v3, (s_v3 + LEAD, e)
    t = c.close(b, end12)
    c.total = t
    return c


def audio_a(c):
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
    x = C.level(C.decode(C.MUSIC['M0'], C.DROP - up, d0, af=RADIO), rms=-23)
    bye = m['bye'][1]
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
    fx('sfx-wind', wind, 0, en['3'], rms=-34, fi=1.0, fo=0.05, what='wind (ffmpeg)')
    loop_wheels(fx, 'sfx-maddie', 0.0, en['0'], rms=-31, fi=0.5, fo=0.3, what='her wheels (loop)')
    for k in np.arange(0.5, en['0'] - 0.5, 2.5):
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
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(base), '-t', f"{h['d']:.4f}", '-vf',
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
    keys = [a for a in sys.argv[1:] if not a.startswith('--')] or ['A', 'B']
    for k in keys:
        run(k, '--no-preview' not in sys.argv)
