#!/usr/bin/env python3
"""GPOM second half, cut 3: two rough cuts in the new-scene timeline format (scripts/scene/timeline.py).

    python3 scripts/gpom/second-half-video/cut3.py A          # scene A, the kill bots (beats 0-12)
    python3 scripts/gpom/second-half-video/cut3.py B          # scene B, Maddie at the door (14a-17)
    python3 scripts/gpom/second-half-video/cut3.py A B --no-preview

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
NAMES = {'ai': 'The AI (through Maddie)', 'bot': 'Maddie', 'woman': 'Sandra', 'man': 'Derek', 'lady': 'The old lady'}
LINES = {(r['beat'], r['i']): r for r in json.loads((V3 / 'lines.json').read_text())}
CAST = json.loads((S.SCENES / 'second-half-cut3-cast.json').read_text())
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
        self.dir = ROOT / key
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


# ---------------------------------------------------------------- scene A

def scene_a():
    c = Cut('A', 'gpom-second-half-A-rough3', 'Cut 3 A Timeline', 'GPOM second half · cut 3 · scene A: the kill bots',
            'Scene A of cut 3, beats 0-12: Maddie on the high street to the stand-down at the bunker door. Play it, '
            'click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you type. '
            "Tell Claude when you're done.")
    m = c.m

    # ---- 0: the continuous travelling shot, Maddie's new words with Kai's pauses
    v6 = V / 'cut3-beat0-continuous.mp4'
    graded, note = regrade_v6(v6, c.vdir / 'cut3-beat0-continuous-graded.mp4')
    c.flags.append(note)
    picks = CAST['maddie_beat0']
    gaps = {(g['after']['line'], g['after']['phrase']): g['seconds'] for g in CAST['gaps']}
    texts = {(r['line'], r['phrase']): r['text'] for r in json.loads((V3 / 'manifest.json').read_text())['maddie']}
    order = sorted(picks, key=lambda k: tuple(int(x) for x in k[1:].split('-')))
    phrases = []
    for k in order:
        ln, p = (int(x) for x in k[1:].split('-'))
        phrases.append((ln, p, Take(AU / picks[k])))
    seq = []
    for j, (ln, p, tk) in enumerate(phrases):
        nxt = phrases[j + 1] if j + 1 < len(phrases) else None
        g = 0.0 if nxt is None else (gaps.get((ln, p), 0.6) if nxt[0] == ln else GAP)
        seq.append((ln, p, tk, g))
    span = sum(tk.d + g for _, _, tk, g in seq)
    have = dur(v6)
    lead = min(2.4, max(LEAD, have - span - TAIL))
    b = c.beat('0', 'Maddie on the high street', 0.0, act='Maddie',
               see='One unbroken travelling shot: the camera backs up the ruined high street and Maddie rolls after it, '
                   'chatting, her radio playing the tune; down on "Oh, hello!", back up on "Mind how you go".')
    s = lead
    placed = {}
    for ln, p, tk, g in seq:
        a = s
        s = c.say('vox-maddie', tk, s, '0', f'beat 0 line {ln} phrase {p}')
        placed.setdefault(ln, [a, s])[1] = s
        s += g
    talk_end = placed[5][1]
    end0 = fr(talk_end + TAIL)
    if end0 > have + 0.1:
        c.flags.append(f'Beat 0: the speech plus lead and tail runs {end0:.2f} s against the {have:.2f} s shot; the shot '
                       'ping-pongs at its end. Speech is not slowed.')
    else:
        end0 = min(end0, fr(have))  # the frame rounding of eleven placements can overrun by a frame or two
        c.flags.append(f'Beat 0: Maddie\'s eleven phrases (Kai\'s picked takes, the manifest\'s pauses) run {span:.1f} s, '
                       f'{have - span:.1f} s shorter than the {have:.2f} s shot. Rather than end the shot early, the spare '
                       f'time goes before "Oh, hello!" ({lead:.2f} s, cut 2 used 2.4 s) so her radio is heard before she '
                       f'turns it down; the shot plays whole and ends {end0 - talk_end:.2f} s after "Mind how you go" '
                       '(my call). Speech is not slowed.')
    for ln in range(6):
        ps = [(p, tk) for l2, p, tk, _ in seq if l2 == ln]
        text = ' [pause] '.join(texts[(ln, p)] for p, _ in ps)
        c.line(b, ln, 'bot', placed[ln][0], placed[ln][1] - placed[ln][0], text, 'kai')
    c.pic(graded, 0.0, 0.0, end0, '0', source=v6)
    m['l0'] = placed[0]
    m['l5'] = placed[5]
    m['b0'] = (0.0, end0)
    m['phr0'] = [(ln, p, a) for (ln, p, _, _), a in zip(seq, [v['t'] for v in c.voices])]
    t = c.close(b, end0)

    # ---- 1-2: the roundabout and the patrol, as cut 2
    b = c.beat('1', 'The roundabout', t, act='The hunt', see='Kill bots everywhere.')
    c.pic(V / 'sh-01-P1-roundabout.mp4', 0, t, t + 4.0, '1')
    t = c.close(b, t + 4.0)
    b = c.beat('2', 'Patrol, low and huge', t, act='The hunt', see='A kill bot rolls over the lens.')
    c.pic(V / 'sh-02-P1-patrol-blockbuster.mp4', 0, t, t + 4.5, '2')
    t = c.close(b, t + 4.5)

    # ---- 3-4: their eyes, one moving HUD view (sh-03 throughout), the meter reading the muffled row
    s3 = t
    b3 = c.beat('3', 'Their eyes: the kill-bot HUD', s3, act='The hunt',
                see='The kill bot\'s own view keeps moving down the street; the new HUD (patrol, teal). '
                    'The meter starts to twitch as the row reaches it through the earth.')
    s4 = fr(s3 + 3.0)
    p0 = take_named('6', 0, 'b', phrase=0, fx=True)
    p1 = take_named('6', 0, 'a', phrase=1, fx=True)
    r0 = fr(s4 - 0.6)
    e0 = c.say('vox-muffled-row', p0, r0, '4', 'the row, muffled: "Derek. You\'ve left the seat up."', lufs=-27)
    r1 = fr(e0 + 0.6)
    e1 = c.say('vox-muffled-row', p1, r1, '4', 'the row, muffled: "Again."', lufs=-27)
    t = c.close(b3, s4)
    b4 = c.beat('4', 'Ping. Organic signal: lock', s4, act='The hunt',
                see='Three pings, ORGANIC SIGNAL - LOCK. No freeze: the view keeps rolling while it listens.')
    c.line(b4, 0, 'woman', r0, e1 - r0, "(muffled) Derek. You've left the seat up. [pause] Again.", 'kai')
    end4 = fr(max(s4 + 3.0, e1 + TAIL))
    sh03 = V / 'sh-03-P1-pov-cctv-hud-patrol.mp4'
    hud = dict(name='hud-34', src=str(sh03), d=fr(end4 - s3), args=['--state', 'patrol', '--lock', f'{s4 - s3:.3f}'],
               meter=['vox-muffled-row'], t0=s3)
    c.huds.append(hud)
    c.pic(c.vdir / 'hud-34.mp4', 0.0, s3, s4, '3', source=sh03, hud='hud-34')
    c.pic(c.vdir / 'hud-34.mp4', s4 - s3, s4, end4, '4', source=sh03, hud='hud-34')
    c.flags.append('Beats 3-4: both run on sh-03 (one moving view, the HUD drawn by hud.py). Cut 2\'s beat 4 clip '
                   'sh-04-post is a held still with a red waveform baked in, so it would freeze and double the HUD.')
    c.flags.append('Beats 3-4: the muffled row starts 0.6 s before the pings so the meter is already moving when the '
                   'bot locks on (my call).')
    m['s3'], m['s4'], m['end4'] = s3, s4, end4
    t = c.close(b4, end4)

    # ---- 6-7: the row, lip-synced, full volume, hard cut
    rows = [('6', 0, 'woman', '6-0'), ('7', 0, 'woman', '7-0'), ('7', 1, 'man', '7-1'), ('7', 2, 'woman', '7-2')]
    info = [lipinfo(n) for _, _, _, n in rows]
    ins = [0.0] + [max(0.0, at - CUT_PRE) for _, at, _, _ in info[1:]]
    beats = {}
    for k, ((bid, i, who, name), (wav, at, end, ph)) in enumerate(zip(rows, info)):
        if bid not in beats:
            beats[bid] = c.beat(bid, {'6': 'The lavatory', '7': 'The row, up close'}[bid], t, act='The row',
                                see={'6': 'Hard cut to full volume: Sandra, lip-synced.',
                                     '7': 'Sandra and Derek, shot by shot, lip-synced.'}[bid])
            if k:
                c.close(beats[rows[k - 1][0]], t)
        i0 = ins[k]
        out = end + (GAP - (info[k + 1][1] - ins[k + 1])) if k + 1 < len(rows) else end + TAIL
        clip = V / f'cut3-lip-{name}-muted.mp4'
        c.pic(clip, i0, t, t + out - i0, bid, source=V / f'cut3-lip-{name}.mp4')
        stem = {'woman': 'vox-sandra', 'man': 'vox-derek'}[who]
        c.dub(stem, wav, i0, out, t, f'beat {bid} line {i} (lip-sync dub)', chain=[TILE])
        c.line(beats[bid], i, who, t + at - i0, end - at, LINES[(bid, i)]['text'], 'kai')
        t = fr(t + out - i0)
    m['s6'] = beats['6']['start']
    t = c.close(beats['7'], t)
    c.flags.append("Beat 7: Derek's line plays take b, the one his talking clip carries (take a read as "
                   "'the world ends at sundry').")

    # ---- 8: same HUD, patrol -> KILL MODE; the row muffled under it as a bed
    s8 = t
    b = c.beat('8', 'KILL MODE ENGAGED', s8, act='Kill mode',
               see='The same HUD on the racing view: patrol, then it flips red. The muffled row keeps the meter moving.')
    flip = 1.5
    d8 = 4.5
    s9 = fr(s8 + d8)
    cutoff = fr(s9 + 0.8)
    tt = s8 + LEAD
    for i, letter in ((0, 'a'), (1, 'b'), (2, 'b')):
        tk = take_named('7', i, letter, fx=True)
        who = LINES[('7', i)]['who']
        if tt < cutoff:
            e = c.say('vox-muffled-row', tk, tt, '8', f'the row, muffled: beat 7 line {i}', lufs=-27, cut=cutoff)
            c.line(b, i, who, tt, min(e, cutoff) - tt, '(muffled) ' + LINES[('7', i)]['text'], 'kai')
            tt = e + GAP
    sh08 = V / 'sh-08-K5-pov-red-race-hud-kill.mp4'
    c.huds.append(dict(name='hud-8', src=str(sh08), d=d8, args=['--state', 'patrol', '--lock', '0',
                                                                  '--flip-to', f'kill@{flip}'],
                       meter=['vox-muffled-row'], t0=s8))
    c.pic(c.vdir / 'hud-8.mp4', 0.0, s8, s9, '8', source=sh08, hud='hud-8')
    m['flip8'] = fr(s8 + flip)
    t = c.close(b, s9)

    # ---- 9a / 9b: one kill bot tears past Maddie; Maddie in the dust
    b = c.beat('9a', 'One kill bot tears past Maddie', t, act='Kill mode',
               see='High over the street: the tank passes close, Maddie jolts, a plume of dust hangs.')
    c.pic(V / 'cut3-V1.mp4', 0, t, t + 5.0, '9a')
    m['s9a'] = t
    t = c.close(b, t + 5.0)
    b = c.beat('9b', 'Whoa: Maddie in the dust', t, act='Kill mode',
               see='Close on Maddie in the dust: she leaps clear on all six wheels, lands, settles. A startled beep.')
    c.pic(V / 'cut3-V2.mp4', 0, t, t + 5.5, '9b')
    m['s9b'] = t
    t = c.close(b, t + 5.5)
    c.flags.append('Beat 9b (V2): Maddie jumps clear of the road on all six wheels, bigger than "rocks back"; it may read '
                   'as too comic.')

    # ---- 10a: the far race
    b = c.beat('10a', 'The far race', t, act='Kill mode', see='From the footbridge: the pack races away down the motorway.')
    v8 = V / 'cut3-V8.mp4'
    c.pic(v8, 0, t, t + 3.5, '10a')
    m['s10a'] = t
    t = c.close(b, t + 3.5)

    # ---- 11: the boss hotline, then the call; the AI's lines open on the far race
    s11 = t
    b = c.beat('11', 'Maddie calls her boss', s11, act='Kill mode',
               see="Maddie's hatch, the boss-hotline antenna. The call; the race (still far) under the AI's lines.")
    v3 = V / 'cut3-V3.mp4'
    calls = [('11', 0, 'bot', False, 'kai'), ('11', 1, 'ai', True, 'claude'), ('11', 2, 'bot', False, 'kai'),
             ('11', 3, 'ai', True, 'kai')]
    tt = s11 + 2.0  # the antenna first
    starts, chosen = [], []
    for bid, i, who, fx, by in calls:
        tk, letter = pick(bid, i, fx=fx)
        chosen.append(f'11-{i} take {letter}')
        stem = 'vox-ai' if who == 'ai' else 'vox-maddie'
        e = c.say(stem, tk, tt, '11', f'beat 11 line {i} {who}')
        c.line(b, i, who, tt, e - tt, LINES[(bid, i)]['text'], by)
        starts.append((tt, e, who))
        tt = e + GAP
    end11 = fr(starts[-1][1] + TAIL)
    cuts = [s11, starts[1][0] - CUT_PRE, starts[1][0] - CUT_PRE + 2.25, starts[3][0] - CUT_PRE,
            starts[3][0] - CUT_PRE + 2.25, end11]
    srcs = [(v3, 0.0), (v8, 3.5), (v3, 2.0), (v8, 5.75), (v3, 4.0)]
    for (src, i0), a, z in zip(srcs, cuts, cuts[1:]):
        c.pic(src, i0, a, z, '11')
    c.flags.append(f'Beat 11 takes: {", ".join(chosen)} (the smaller internal gap). The call runs '
                   f'{end11 - s11:.1f} s on 8 s of V3, so V3 ping-pongs from 2 s in, after the antenna moves; the AI\'s '
                   'two lines open on 2.25 s of V8 each, then cut back to Maddie.')
    c.flags.append('Beat 11: V3\'s plate already has the hatch open, so the hatch sound plays on the cut and the antenna '
                   'sound on its little jerk (about 1.3 s in).')
    m['s11'], m['calls'], m['end11'] = s11, starts, end11
    m['v8cuts'] = [(cuts[1], cuts[2]), (cuts[3], cuts[4])]
    t = c.close(b, end11)

    # ---- 10b: the close race, Maddie over it
    b = c.beat('10b', 'The close race', t, act='Kill mode',
               see='Low in the grass: the pack converges on the bunker door. Maddie over it.')
    tk, letter = pick('11c', 0)
    e = c.say('vox-maddie', tk, t + LEAD, '10b', 'beat 11c line 0 bot')
    c.line(b, 0, 'bot', t + LEAD, e - t - LEAD, LINES[('11c', 0)]['text'], 'kai')
    d10b = fr(max(5.0, e + TAIL - t))
    c.pic(V / 'cut3-V9.mp4', 0, t, t + d10b, '10b')
    c.flags.append('Beat 10b (V9): five kill bots, not the three asked for: two burst in past the camera.')
    m['s10b'] = t
    t = c.close(b, t + d10b)

    # ---- 12: on board, kill -> PEACE as it brakes; they file away; the AI's punchline on Maddie
    s12 = t
    b = c.beat('12', 'The stand-down', s12, act='The gate',
               see='On board one kill bot: red KILL MODE racing at the door, it brakes and flips to green PEACE MODE. '
                   'The pack turns and files away down the hill. Then the boss, through Maddie.')
    v4 = V / 'cut3-V4.mp4'
    peace = 3.6
    c.huds.append(dict(name='hud-12', src=str(v4), d=7.0, args=['--state', 'kill', '--lock', '0',
                                                                 '--flip-to', f'peace@{peace}'],
                       meter=['sfx-killbots'], t0=s12))
    c.pic(c.vdir / 'hud-12.mp4', 0.0, s12, s12 + 7.0, '12', source=v4, hud='hud-12')
    c.pic(V / 'cut3-V10.mp4', 0, s12 + 7.0, s12 + 13.0, '12')
    s_v3 = fr(s12 + 13.0)
    tk, letter = pick('12', 0, fx=True)
    e = c.say('vox-ai', tk, s_v3 + LEAD, '12', 'beat 12 line 0 ai')
    c.line(b, 0, 'ai', s_v3 + LEAD, e - s_v3 - LEAD, LINES[('12', 0)]['text'], 'kai')
    end12 = fr(e + TAIL + 0.4)
    c.pic(v3, 3.0, s_v3, end12, '12')
    c.flags.append('Beat 12: the punchline "See? I told you I knew what malware was." plays over a return to Maddie\'s '
                   'antenna close-up (V3), not over V10, because his voice comes out of her speaker (my call).')
    c.flags.append('Beat 12: the HUD meter on V4 reads the kill bots\' engine sound (no voice is near it there).')
    m['s12'], m['peace'], m['s_v3'], m['ai12'] = s12, fr(s12 + peace), s_v3, (s_v3 + LEAD, e)
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
    # M0 her radio, as cut 2: down to nothing on "Oh, hello!", back up for "Mind how you go" (the last ~1.3 s of
    # her last phrase), cued so the GPOM track's drop lands there; hard cut to the roundabout.
    hello = m['l0'][0]
    up = m['l5'][1] - 1.3
    d0 = en['0']
    x = C.level(C.decode(C.MUSIC['M0'], C.DROP - up, d0, af=RADIO), rms=-23)
    x *= C.env(len(x), [(0, 0), (0.3, 1), (hello - 0.1, 1), (hello + 0.5, 0), (up - 0.3, 0), (up + 0.3, 1),
                        (d0 - 0.03, 1), (d0, 0)])
    mx.add('mus-M0-radio', x, 0.0, C.MUSIC['M0'], 'M0 her radio (tinny GPOM track)')
    # S1 the hunt: beats 1-3, dead on the first ping.
    d = st['4'] - st['1']
    x = C.fades(C.level(C.decode(C.MUSIC['S1'], 0.33, d), rms=-17, peak=-1), 0.15, 0.03)
    mx.add('mus-S1-hunt', x, st['1'], C.MUSIC['S1'], 'S1 the hunt')
    # S2 the chase: on the red flip, ducked under the call, back up for the close race, dead on PEACE MODE.
    # The cue is longer than the 44.8 s take, so it jumps (1.5 s crossfade) inside the duck to the part of
    # the take that ends on the stand-down.
    s2, stop = m['flip8'], m['peace']
    d = stop - s2
    src_len = dur(C.MUSIC['S2'])
    da = m['calls'][0][0] - 0.3 - s2
    db = m['calls'][-1][1] + 0.2 - s2
    if d <= src_len - 0.2:
        x = C.decode(C.MUSIC['S2'], 0, d)
        seam_note = ''
    else:
        seam = da + 3.0
        xf = 1.5
        rest = d - seam
        off = src_len - rest - 0.3
        p1 = C.decode(C.MUSIC['S2'], 0, seam + xf)
        p2 = C.decode(C.MUSIC['S2'], off - xf, rest + xf)
        n, k = int(seam * SR), int(xf * SR)
        w = np.linspace(0, np.pi / 2, k)[:, None]
        x = np.concatenate([p1[:n], p1[n:n + k] * np.cos(w) + p2[:k] * np.sin(w), p2[k:]])
        seam_note = (f'S2 (the chase take, {src_len:.1f} s) is shorter than its {d:.1f} s cue: it plays 0-{seam:.1f} s, '
                     f'then crossfades (1.5 s, under the duck) to {off:.1f} s so its last stretch lands on PEACE MODE.')
    x = C.level(x, rms=-18, peak=-1)
    x *= C.env(len(x), [(0, 1), (da, 1), (da + 0.4, 0.22), (db, 0.22), (db + 0.4, 1), (d - 0.02, 1), (d, 0)])
    mx.add('mus-S2-chase', x, s2, C.MUSIC['S2'], 'S2 the chase')
    if seam_note:
        c.flags.append(seam_note)

    # ---- sfx
    wind = wind_file()
    fx('sfx-wind', wind, 0, en['3'], rms=-34, fi=1.0, fo=0.05, what='wind (ffmpeg)')
    # Beat 0: her wheels under the whole shot, beacon blips, a few beeps on her thoughts.
    loop_wheels(fx, 'sfx-maddie', 0.0, en['0'], rms=-31, fi=0.5, fo=0.3, what='her wheels (loop)')
    for k in np.arange(0.5, en['0'] - 0.5, 2.5):
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-36, what='beacon blip')
    ph = {(ln, p): a for ln, p, a in m['phr0']}
    end_of = {(v['what']): v['t'] + v['d'] for v in c.voices}
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-hello.wav', ph[(0, 0)] - 0.55, rms=-30, what='beep: hello')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-deflate.wav', end_of['beat 0 line 1 phrase 2'] + 0.05, rms=-32,
       what='beep: deflate (after "went.")')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-thinking.wav', end_of['beat 0 line 4 phrase 0'] + 0.1, rms=-34,
       what='beep: thinking (the long pause)')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-happy.wav', m['l5'][1] + 0.05, rms=-31, what='beep: happy (bye)')
    # Beats 1-3: the kill bots.
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', st['1'], st['4'] - st['1'], src_in=2, rms=-28,
       fi=0.3, fo=0.03, what='engines round the ring')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['2'], en['2'] - st['2'] + 0.5, rms=-22, peak=-3,
       fo=0.4, what='tracks closing in')
    fx('sfx-killbots', SFX / 'fs824121-killbot-servo.mp3', st['3'], en['4'] - st['3'], src_in=1, rms=-32, fo=0.05,
       what='servo whine')
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', st['3'], en['4'] - st['3'], rms=-38, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', SFX / 'synth-hud-blip.wav', st['3'] + 0.3, peak=-12, what='HUD tone')
    fx('sfx-hud', SFX / 'synth-killbot-three-pings.wav', st['4'], peak=-6, what='three pings')
    # Beats 6-7: the tiled room.
    fx('sfx-rooms', SFX / 'fs767306-room-tiled-public-bathroom.mp3', st['6'], en['7'] - st['6'], src_in=10, rms=-42,
       fi=0.05, fo=0.05, what='tiled room tone')
    # Beat 8: hiss, the red flip, engines.
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', st['8'], en['8'] - st['8'], rms=-40, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', SFX / 'synth-killbot-red-flip.wav', m['flip8'] - 0.05, peak=-6, what='red flip tone')
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', m['flip8'], en['8'] - m['flip8'] + 0.4,
       src_in=20, rms=-24, fi=0.1, fo=0.4, what='engines, the chase')
    # 9a: the pass (V1 closest at ~2.8 s; the whoosh file peaks at 1.2 s, panned L->R: flipped, it exits left).
    s = st['9a']
    loop_wheels(fx, 'sfx-maddie', s, 3.0, rms=-34, fi=0.2, fo=0.2, what='her wheels, trundling')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, 3.4, rms=-26, fi=0.3, fo=0.6, what='tank tracks')
    fx('sfx-maddie', MS / 'derived-maddie-killbot-dust-whoosh.wav', s + 1.6, peak=-3, af='pan=stereo|c0=c1|c1=c0',
       what='kill bot dust whoosh, past her')
    fx('sfx-maddie', MS / 'derived-maddie-servo-turn-b.wav', s + 3.0, rms=-30, what='servo: she jolts')
    # 9b: she leaps (~1.8 s) and lands (~3.5 s).
    s = st['9b']
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-oh.wav', s + 1.85, rms=-26, what='beep: startled "oh"')
    fx('sfx-maddie', MS / 'derived-maddie-wheels-stop.wav', s + 3.4, rms=-30, what='she lands and settles')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-uh-oh.wav', s + 4.3, rms=-30, what='beep: uh-oh')
    # 10a: the far race.
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', st['10a'], en['10a'] - st['10a'], src_in=30,
       rms=-30, fi=0.2, fo=0.3, what='engines, far')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', st['10a'], en['10a'] - st['10a'], rms=-32, fo=0.3,
       what='tracks, far')
    # 11: hatch and antenna on V3; the far engines on each V8 cutaway; the beacon on the AI's words.
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
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, en['10b'] - s, src_in=10, rms=-22, fi=0.05,
       fo=0.2, what='engines, close')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s, en['10b'] - s, rms=-22, peak=-3, fo=0.3,
       what='tracks, close')
    fx('sfx-killbots', SFX / 'fs189446-killbot-jet-flyby.mp3', s - 0.3, 2.5, src_in=4, rms=-24, peak=-3, fi=0.3, fo=0.8,
       what='two tear past the camera')
    # 12: on board, the brake, PEACE; the pack files away.
    s = st['12']
    fx('sfx-killbots', SFX / 'fs522673-killbot-drone-engine-flyby.mp3', s, 3.9, src_in=20, rms=-21, fo=0.5,
       what='engine, on board')
    fx('sfx-killbots', SFX / 'fs824121-killbot-servo.mp3', s + 3.3, 1.4, src_in=1, rms=-24, fo=0.4, what='brakes')
    fx('sfx-killbots', SFX / 'fs132929-explosion-rubble-debris.mp3', s + 4.4, 2.6, rms=-30, fi=0.2, fo=1.0,
       what='grit and dust rolling over the hull')
    fx('sfx-hud', SFX / 'synth-cctv-hiss-20s.wav', s, 7.0, rms=-40, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', SFX / 'synth-killbot-red-flip.wav', m['peace'] - 0.05, peak=-8,
       af='asetrate=48000*1.26,aresample=48000', what='PEACE flip tone (the red flip, pitched up)')
    fx('sfx-killbots', SFX / 'fs557594-killbot-mech-walk.mp3', s + 7.0, 6.0, rms=-30, fi=0.3, fo=2.5,
       what='the pack files away')
    fx('sfx-wind', wind, s + 7.0, total - s - 7.0, src_in=20, rms=-36, fi=1.0, fo=0.5, what='wind on the downs')
    a, e = m['ai12']
    for k in np.arange(a, e, 0.9):
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-34, what='beacon on his words')
    return mx


# ---------------------------------------------------------------- scene B

def scene_b():
    c = Cut('B', 'gpom-second-half-B-rough3', 'Cut 3 B Timeline', 'GPOM second half · cut 3 · scene B: Maddie at the door',
            'Scene B of cut 3, beats 14a-17: Maddie at the bunker door, the tannoy, the doors open, the old lady. '
            'Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you '
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
    c.pic(V / 'sh-15-r2-SBHELLOa.mp4', 1.0, s, end, '15')
    m['s15'] = s
    t = c.close(b, end)

    # ---- 17: shot / reverse shot. The old lady (lip-synced, her voice in the clips) and Maddie (V11).
    s17 = t
    b = c.beat('17', 'The old lady and Maddie', s17, act='The meeting',
               see='The old lady among the crowd, the others in shadow; Maddie over her shoulder in the big doorway. '
                   'Shot / reverse shot.')
    v11 = V / 'cut3-V11.mp4'
    BY = {0: 'kai', 1: 'kai', 2: 'kai', 3: 'kai', 4: 'kai', 5: 'claude', 6: 'claude', 7: 'claude'}
    lady = []

    def lip(name, t0, i0, out):
        wav, at, end_, ph = lipinfo(name)
        c.pic(V / f'cut3-lip-{name}-muted.mp4', i0, t0, t0 + out - i0, '17', source=V / f'cut3-lip-{name}.mp4')
        lady.append((t0, i0, out))
        return wav, at, end_

    def dub(wav, t0, i0, i1, what):
        c.dub('vox-lady', wav, i0, i1, t0, what, chain=[CORRIDOR])

    # 17-0, cut to Maddie for its last 0.3 s (the voice overruns the mouth)
    wav, at, end_, _ = lipinfo('17-0')
    i0 = at - LEAD
    mouth_end = end_ - 0.32
    lip('17-0', s17, i0, mouth_end)
    dub(wav, s17, i0, end_ + 0.1, 'beat 17 line 0 lady (lip-sync dub)')
    l0a, l0e = s17 + LEAD, s17 + end_ - i0
    c.line(b, 0, 'lady', l0a, l0e - l0a, LINES[('17', 0)]['text'], BY[0])
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
    e = maddie_line(4, l3a + (end_ - at) + GAP)
    e = maddie_line(5, e + GAP)
    # 17-6: a long pause (lines.json lead 1.2 s), then "Well." on her, then the two halves of the second phrase
    lead6 = LINES[('17', 6)].get('lead', 1.2)
    wav_a, at_a, end_a, _ = lipinfo('17-6a')
    well = e + GAP + lead6
    t6a = fr(well - at_a)
    c.pic(v11, 3.0, v11_b, t6a, '17')
    wav_b1, at_b1, end_b1, _ = lipinfo('17-6b1')
    wav_b2, at_b2, end_b2, _ = lipinfo('17-6b2')
    i_b1 = max(0.0, at_b1 - CUT_PRE)
    gap6 = LINES[('17', 6)]['gaps'][0]['seconds']
    out_a = end_a + (gap6 - (at_b1 - i_b1))
    lip('17-6a', t6a, 0.0, out_a)
    dub(wav_a, t6a, 0.0, out_a, 'beat 17 line 6 lady, part a (lip-sync dub)')
    t_b1 = fr(t6a + out_a)
    i_b2 = at_b2 - CUT_PRE
    out_b1 = end_b1 + (GAP - (at_b2 - i_b2))
    lip('17-6b1', t_b1, i_b1, out_b1)
    dub(wav_b1, t_b1, i_b1, out_b1, 'beat 17 line 6 lady, part b1 (lip-sync dub)')
    t_b2 = fr(t_b1 + out_b1 - i_b1)
    out_b2 = end_b2 + 0.2
    lip('17-6b2', t_b2, i_b2, out_b2)
    dub(wav_b2, t_b2, i_b2, out_b2, 'beat 17 line 6 lady, part b2 (lip-sync dub)')
    e6 = t_b2 + end_b2 - i_b2
    c.line(b, 6, 'lady', well, e6 - well, LINES[('17', 6)]['text'], BY[6])
    v11_c = fr(t_b2 + out_b2 - i_b2)
    e = maddie_line(7, e6 + GAP)
    end = fr(e + 1.0)
    c.pic(v11, 5.0, v11_c, end, '17')
    c.flags.append('Beat 17-0: the old lady\'s voice runs about 0.3 s past her mouth on "...meeting him", so the picture '
                   'cuts to Maddie (V11) for that last 0.3 s.')
    c.flags.append('Beat 17: the long pause before her "Well." (1.2 s) sits mostly on Maddie waiting (V11), because '
                   'her talking clip has only 0.46 s before she speaks.')
    c.flags.append(f'Beat 17: Maddie\'s lines are long (17-2 is 11.4 s, 17-4 + 17-5 about 19 s), so the 8 s V11 '
                   'ping-pongs for most of them; a cutaway to the old lady listening would break the holds, but no '
                   'silent footage of her exists beyond a second or two.')
    c.flags.append('Beat 17 words: lines 0-4 follow Kai\'s note on beat 17 closely (marked kai, worded by Claude in draft '
                   'A, which Kai approved); 5-7 are Claude\'s additions (marked claude).')
    m['s17'], m['lady'], m['fair'] = s17, lady, e
    m['l17_0'] = l0a
    t = c.close(b, end)
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
    for k in np.arange(s + 9.0, en['17'] - 3.0, 13.0):
        fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', k, rms=-36, what='servo: she nudges')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-boop-ok.wav', m['fair'] + 0.15, rms=-32, what='beep: boop (ok)')
    c.flags.append('Beat 17: a low "ok" boop after "Fair." and the hello beep under "Hello!" in 15 are my additions to '
                   "Maddie's sound kit.")
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
    """Every take at its loudness, rooms on it, sample-aligned (gain only: nothing here shifts time)."""
    for v in c.voices:
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
                audio=tracks, mix=str(mix), events=mx.events, flags=c.flags + [
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
