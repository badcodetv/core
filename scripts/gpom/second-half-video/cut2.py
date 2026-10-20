#!/usr/bin/env python3
"""GPOM second half, cut 2 part 1 (beats 0-18): picture order, re-timing to the real voices, the mix.

Not run directly: timing.py, extend.py, rough_audio.py and rough_place.py hand over to this module
when called with `--cut2`, so their old 29-frame path (and the old rough cut) is untouched.

    python3 scripts/gpom/second-half-video/timing.py --cut2       # audio/cut2/rough-cut2.json
    python3 scripts/gpom/second-half-video/extend.py --cut2       # video/rt2/*.mp4 (longer clips)
    python3 scripts/gpom/second-half-video/rough_audio.py --cut2  # stems, mix, edl.json, preview
    python3 scripts/gpom/second-half-video/rough_place.py --cut2 count|eval A B

Source of truth: the `cut2` block of second-half-audio-plan.json (words, music, sfx rows) and the
voiced takes in audio/voice2/takes.json. Timing rules are build-cut-plan.py's (LEAD/GAP/TAIL), with
the real take lengths in place of the words-a-second estimate. A beat never gets shorter than its
base (the first-assembly length of its frame, or NEW_LEN for a new beat); dialogue stays inside its
beat; speech is never slowed: picture grows by ping-pong (extend.py's method), never the voice.

Outputs (media only, under clips/second-half/):
  audio/cut2/rough-cut2.json   beats, clips, lines (timing.py)
  audio/cut2/stems/*.wav       one 32-bit float wav per sound track, all starting at t=0 of the cut
  audio/cut2/mix.wav           reference full mix (the stems summed, limited)
  audio/cut2/edl.json          every video clip and every stem, for the Premiere build
  cut2-preview.mp4             picture + mix, ffmpeg render, plus cut2-preview-sheet.jpg
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

FPS, SR = 24, 48000
LEAD, GAP, TAIL = 0.4, 0.35, 0.6          # build-cut-plan.py
CUT_PRE = 0.15                            # a picture cut lands this long before the line it cuts to
AUDIO = S.CLIPS / 'audio'
V2 = AUDIO / 'voice2'
SFX = AUDIO / 'sfx'
C2 = AUDIO / 'cut2'
RC2 = C2 / 'rough-cut2.json'
RT2 = S.OUT / 'rt2'
SIM = S.CLIPS.parent / 'simulation' / 'video'
REC = pathlib.Path('/mnt/c/Users/kai/Desktop/suno-recordings')
PREVIEW = S.CLIPS / 'cut2-preview.mp4'
SEQ = 'gpom-second-half-rough2'
MUSIC = {
    'M0': S.CLIPS.parent / 'gpom-main-track.mp3',                       # the GPOM track itself
    'S1': REC / 'gpom-sh2-s1b-v6-w30-9222bb47.wav',                     # Cover; 0.33 s lead-in silence
    'S2': REC / 'gpom-sh2-s2b-v6-w30-647f6507.wav',
    'M6': REC / 'gpom-s4-bed2-wondering-v6-w25-a6cf12f5.wav',           # gpom-sim-bed2, Maddie's theme
    'S3': REC / 'gpom-sh2-s3-a-v6-w30-fca27332.wav',                    # the Hundred theme, cornet
}
DROP = 70.3  # the drum & bass drop in gpom-main-track.mp3 (rough_audio.py)
ORDER = ['0', '1', '2', '3', '4', '6', '7', '8', '9', '10', '11', '11b', '12', '13', '14a', '14b', '14', '15',
         '17', '18']


def v(name):
    return S.OUT / name


# Base length of each beat (the first-assembly length of its frame, edl.py; new beats per
# build-cut-plan.py's NEW_LEN, 14a lengthened so Maddie reaches the doors) and its picture: segments
# in order, each running until an anchor: ('line', i) cuts CUT_PRE before line i, ('abs', x) at x s
# into the beat, ('end',) at the beat's end. A segment longer than its source ping-pongs (extend).
BEATS = {
    '0': dict(base=0, lead=2.4, post=2.5, pic=[      # rolls up 2 s before she speaks; ~3 s roll-off after
        (SIM / '08-r1-arrival.mp4', 0.0, ('abs', 4.0)),
        (SIM / '09-s3-robot.mp4', 0.0, ('line', 3)),
        (SIM / '10-r2-robot.mp4', 0.0, ('lineend', 5)),
        (SIM / '08-r1-arrival.mp4', 5.0, ('end',))]),
    '1': dict(base=4.0, pic=[(v('sh-01-P1-roundabout.mp4'), 0.0, ('end',))]),
    '2': dict(base=4.5, pic=[(v('sh-02-P1-patrol-blockbuster.mp4'), 0.0, ('end',))]),
    '3': dict(base=3.0, pic=[(v('sh-03-P1-pov-cctv-hud-patrol.mp4'), 0.0, ('end',))]),
    '4': dict(base=3.0, pic=[(v('sh-04-post.mp4'), 0.0, ('end',))]),
    '6': dict(base=3.5, pic=[(v('sh-06-B5-the-lavatory.mp4'), 0.0, ('end',))]),
    '7': dict(base=7.0, pic=[
        (v('sh-07-1-SB07a.mp4'), 0.0, ('line', 1)),
        (v('sh-07-2-SB07c.mp4'), 0.0, ('line', 2)),
        (v('sh-07-1-SB07a.mp4'), 2.0, ('end',))]),
    # Same POV as the ping with the muffled row playing, then the red flip.
    '8': dict(base=4.0, flip=1.25, pic=[
        (v('sh-04-post.mp4'), 0.0, ('abs', 1.25)),
        (v('sh-08-K5-pov-red-race-hud-kill.mp4'), 0.0, ('end',))]),
    '9': dict(base=3.0, pic=[(v('sh-09-c-SB09a.mp4'), 0.0, ('end',))]),
    '10': dict(base=4.0, pic=[(v('sh-10-K9-downs-aerial.mp4'), 0.0, ('end',))]),
    '11': dict(base=9.0, pic=[(v('sh-11-post.mp4'), 0.0, ('end',))]),
    '11b': dict(base=2.0, pic=[(v('sh-11-post.mp4'), 4.5, ('end',))]),
    '12': dict(base=3.0, pic=[(v('sh-12-SB12a.mp4'), 0.0, ('end',))]),
    '13': dict(base=3.0, pic=[(v('cut2-N1.mp4'), 0.0, ('end',))]),
    '14a': dict(base=6.5, pic=[(v('cut2-N2.mp4'), 0.0, ('end',))]),
    '14b': dict(base=0.0, lead=1.0, pic=[(v('cut2-N3.mp4'), 0.0, ('end',))]),   # click + whine first
    '14': dict(base=6.0, lead=2.0, pic=[(v('sh-14-SBDOORa.mp4'), 0.0, ('end',))]),  # crowd as the doors part
    '15': dict(base=4.0, pic=[(v('sh-15-r2-SBHELLOa.mp4'), 1.0, ('end',))]),
    # The old lady (N4) and Maddie (the N4r2-rev still, a slow push), then the CCTV replay (the old 18b)
    # from "Look.", with Maddie's next line over it.
    '17': dict(base=4.0, extra_gap={4: 1.75}, pic=[
        (v('cut2-N4.mp4'), 0.0, ('line', 1)),
        (v('cut2-N4rev-hold.mp4'), 0.0, ('line', 2)),
        (v('cut2-N4.mp4'), 0.5, ('line', 3)),
        (v('cut2-N4rev-hold.mp4'), 6.0, ('lineend', 3)),
        (v('sh-18b-post.mp4'), 0.0, ('abs+', 'lineend', 3, 6.0)),   # Maddie's next line ends inside it
        (v('cut2-N4.mp4'), 1.5, ('end',))]),
    # The circle: Maddie (18a), the apology over the wide (old 16), the AI on 18a, the murmur on the
    # faces (N3), Derek over the wide, the old lady close (old 17 plate) to the end.
    '18': dict(base=2.5, post=2.5, pic=[
        (v('sh-18a-post.mp4'), 0.0, ('line', 1)),
        (v('sh-16-post.mp4'), 0.0, ('line', 2)),
        (v('sh-18a-post.mp4'), 0.0, ('line', 3)),
        (v('cut2-N3.mp4'), 3.0, ('line', 4)),
        (v('sh-16-post.mp4'), 4.0, ('line', 5)),
        (v('sh-17-M3-old-lady-blockbuster.mp4'), 0.0, ('end',))]),
}
BED = {'8'}         # beat 8's lines are the muffled row as a bed: placed, but they do not size the beat
STAGGER = 0.3       # crowd voices, a beat apart
FLAGS = [
    'Beat 0 picture: Kai\'s frame (the ruined high street, bot on the centre line) is simulation/video/'
    '08-r1-arrival.mp4. Her ~38 s of talk is held on the two close bot clips from the same street '
    '(09-s3-robot, 10-r2-robot, ping-ponged), then the tail of 08-r1 as she rolls at the camera.',
    'M0: no tinny-radio version of the GPOM track by Kai was found on disk; made here with the sfx '
    'agent\'s M0_tinny_radio filter. The source is cued so the drop lands on "Mind how you go".',
    'Beat 17: Maddie\'s lines are on a slow push over the N4r2-rev still (video/cut2-N4rev-hold.mp4, made '
    'here); no clip of that angle exists.',
    'Beat 18: no new circle shots exist, so it reuses 18a (Maddie in the circle), the old 16 wide (the '
    'apology) and the old 17 plate (the old lady close) for "I\'m going"; the murmur sits on N3 (faces '
    'under the tannoy).',
    'Beat 12: the white flash frame on each explosion is not in the picture; owed in Premiere.',
    'Wind (beat 0, 1-3) is synthesised in ffmpeg: the sfx shortlist has no wind recording.',
]


def fr(s):
    return round(s * FPS) / FPS


def probe(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def plan():
    return json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())


# ---------------------------------------------------------------- timing

def takes():
    """Lines per beat from voice2/takes.json: [(i, who, [files], kind)] in order."""
    rows = json.loads((V2 / 'takes.json').read_text())
    out = {}
    for r in rows:
        f = r.get('fx') if r.get('fxKind') in ('speaker', 'tannoy', 'muffled') else r['file']
        kind = r.get('fxKind') or ('crowd' if r['who'] == 'crowd' else 'dry')
        lines = out.setdefault(r['beat'], [])
        if lines and lines[-1][0] == r['i']:
            lines[-1][2].append(f)
        else:
            lines.append((r['i'], r['who'], [f], kind))
    return out


def timing():
    C2.mkdir(parents=True, exist_ok=True)
    make_hold()
    cut = {b['id']: b for b in plan()['cut2']['beats']}
    assert list(cut) == ORDER, f'cut2 beat order changed: {list(cut)}'
    tk = takes()
    beats, clips, lines, t = [], [], [], 0.0
    for bid in ORDER:
        spec, start = BEATS[bid], t
        s = start + spec.get('lead', LEAD)
        placed = []
        for i, who, files, kind in tk.get(bid, []):
            s += spec.get('extra_gap', {}).get(i, 0)
            if who == 'crowd':
                ds = [probe(V2 / f) for f in files]
                for j, (f, d) in enumerate(zip(files, ds)):
                    lines.append(dict(beat=bid, i=i, who=who, file=f, t=fr(s + STAGGER * j), dur=d, kind=kind))
                d = max(STAGGER * j + dj for j, dj in enumerate(ds))
            else:
                d = probe(V2 / files[0])
                lines.append(dict(beat=bid, i=i, who=who, file=files[0], t=fr(s), dur=d, kind=kind))
            placed.append((i, fr(s), fr(s + d)))
            s += d + GAP
        talk_end = placed[-1][2] if placed and bid not in BED else start
        dur = max(spec['base'], (talk_end + TAIL - start) if placed and bid not in BED else 0) + spec.get('post', 0)
        dur = fr(dur)
        at = {i: (a, b) for i, a, b in placed}

        def anchor(a):
            if a[0] == 'end':
                return start + dur
            if a[0] == 'abs':
                return start + a[1]
            if a[0] == 'line':
                return at[a[1]][0] - CUT_PRE
            if a[0] == 'lineend':
                return at[a[1]][1] + CUT_PRE
            if a[0] == 'abs+':
                return at[a[2]][1] + CUT_PRE + a[3]
            raise ValueError(a)

        c0 = start
        for src, i0, a in spec['pic']:
            c1 = fr(anchor(a))
            d = fr(c1 - c0)
            if d <= 0:
                raise SystemExit(f'beat {bid}: empty segment {src.name}')
            have = probe(src)
            clips.append(dict(file=str(src), t=fr(c0), **{'in': i0}, dur=d, beat=bid,
                              extend=fr(max(0.0, i0 + d - have))))
            c0 = c1
        assert abs(c0 - (start + dur)) < 1e-6, (bid, c0, start + dur)
        beats.append(dict(id=bid, title=cut[bid]['title'], start=fr(start), dur=dur, lines=placed,
                          flip=spec.get('flip')))
        t = fr(start + dur)
    out = dict(total=t, beats=beats, clips=clips, lines=lines, flags=FLAGS)
    RC2.write_text(json.dumps(out, indent=1))
    print(f'total {t:.2f}s  ({len(clips)} clips, {len(lines)} voice takes)')
    for b in beats:
        print(f"  beat {b['id']:>3} {b['start']:7.2f} +{b['dur']:6.2f}  {b['title']}")
    for c in clips:
        if c['extend']:
            print(f"  extend beat {c['beat']:>3} {pathlib.Path(c['file']).name:38s} {c['dur']:5.2f}s (+{c['extend']:.2f})")


def make_hold():
    """Beat 17's reverse angle: the N4r2-rev still as a 24 s slow push (no clip of it exists)."""
    out = S.OUT / 'cut2-N4rev-hold.mp4'
    if out.exists():
        return
    still = S.CLIPS / 'storyboard' / 'cut2' / 'N4r2-rev.jpg'
    n = 24 * FPS
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(still), '-vf',
                    f"scale=2560:-2,zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                    f":d={n}:s=1280x720:fps={FPS}", '-frames:v', str(n), *ENC, str(out)], check=True)


# ---------------------------------------------------------------- extend

ENC = ['-an', '-r', '24', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def extend():
    rc = json.loads(RC2.read_text())
    RT2.mkdir(exist_ok=True)
    for c in rc['clips']:
        if c['extend'] <= 0:
            continue
        src = pathlib.Path(c['file'])
        i, d = c['in'], c['dur']
        out = RT2 / f"{src.stem}-i{i:g}-d{d:.3f}.mp4"
        have = probe(src) - i
        reps = int(np.ceil(d / (2 * have)))
        unit = int(round(2 * have * FPS))
        # Forward, then reversed, looped until long enough (extend.py's ping-pong), cut to length.
        fc = (f'[0:v]trim=start={i},setpts=PTS-STARTPTS,fps={FPS},split[f][r];[r]reverse[b];[f][b]concat=n=2:v=1,'
              f'loop=loop={reps}:size={unit}:start=0,setpts=N/{FPS}/TB[v]')
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-filter_complex', fc, '-map', '[v]',
                        '-t', f'{d:.4f}', *ENC, str(out)], check=True)
        got = probe(out)
        if got + 1 / FPS < d:
            raise SystemExit(f'{out.name}: {got:.2f}s < {d:.2f}s')
        c['src'], c['file'], c['in'], c['extend'] = c['file'], str(out), 0.0, 0.0
        print(f"beat {c['beat']:>3} {src.name} -> rt2/{out.name} {d:.2f}s")
    RC2.write_text(json.dumps(rc, indent=1))


# ---------------------------------------------------------------- audio

def decode(path, src_in=0.0, dur=None, af=None):
    cmd = ['ffmpeg', '-loglevel', 'error', '-ss', f'{src_in:.4f}']
    if dur is not None:
        cmd += ['-t', f'{dur:.4f}']
    cmd += ['-i', str(path)]
    if af:
        cmd += ['-af', af]
    cmd += ['-ac', '2', '-ar', str(SR), '-f', 'f32le', '-']
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


def rms_db(x):
    m = np.sqrt(np.mean(x ** 2, axis=1))
    act = m[m > 10 ** (-60 / 20)]
    return 20 * np.log10(np.sqrt(np.mean(act ** 2))) if len(act) else -120.0


def level(x, rms=None, peak=None):
    """Scale to an RMS (dBFS, over the non-silent part) and/or a peak ceiling (dBFS)."""
    g = 1.0
    if rms is not None:
        g = 10 ** ((rms - rms_db(x)) / 20)
    if peak is not None:
        p = np.max(np.abs(x)) * g
        if p > 10 ** (peak / 20):
            g *= 10 ** (peak / 20) / p
    return x * g


def env(n, pts):
    """Piecewise-linear gain over n samples from [(t, gain)] (seconds from the event start)."""
    ts = np.array([p[0] for p in pts]) * SR
    gs = np.array([p[1] for p in pts])
    return np.interp(np.arange(n), ts, gs)[:, None]


def fades(x, fi=0.0, fo=0.0):
    n = len(x)
    pts = [(0, 0 if fi else 1), (fi, 1), (max(fi, n / SR - fo), 1), (n / SR, 0 if fo else 1)]
    return x * env(n, pts)


class Mix:
    def __init__(self, total):
        self.n = int(round(total * SR)) + SR
        self.stems, self.events = {}, []

    def add(self, stem, x, t, src='', what=''):
        buf = self.stems.setdefault(stem, np.zeros((self.n, 2), np.float32))
        a = int(round(t * SR))
        b = min(self.n, a + len(x))
        if b > a:
            buf[a:b] += x[:b - a]
        self.events.append(dict(stem=stem, t=round(float(t), 3), dur=round(len(x) / SR, 3), src=str(src), what=what))


VOX = {'bot': 'vox-maddie', 'ai': 'vox-ai', 'woman': 'vox-sandra', 'man': 'vox-derek', 'lady': 'vox-lady',
       'crowd': 'vox-crowd'}
TILE = 'aecho=0.8:0.5:35|60:0.22|0.12'        # rough_audio.py's tiled room
CORRIDOR = 'aecho=0.8:0.4:50|90:0.18|0.1'


def audio():
    rc = json.loads(RC2.read_text())
    sfx = json.loads((SFX / 'index.json').read_text())
    RADIO = sfx['filters']['M0_tinny_radio']
    total = rc['total']
    B = {b['id']: b for b in rc['beats']}
    start = {k: b['start'] for k, b in B.items()}
    end = {k: b['start'] + b['dur'] for k, b in B.items()}
    L = {(b['id'], i): (a, e) for b in rc['beats'] for i, a, e in b['lines']}
    mx = Mix(total)
    src_dir = C2 / 'src'
    src_dir.mkdir(parents=True, exist_ok=True)

    # Voices: dialogue at one loudness; the muffled row and the crowd lower; rooms on the row and corridor.
    for ln in rc['lines']:
        who, kind, b = ln['who'], ln['kind'], ln['beat']
        chain = []
        if who in ('woman', 'man') and b in ('6', '7'):
            chain.append(TILE)
        if b == '17':
            chain.append(CORRIDOR)
        if kind == 'muffled':
            chain.append('loudnorm=I=-27:TP=-6')
            stem = 'vox-muffled-row'
        elif kind == 'tannoy':
            chain.append('loudnorm=I=-17:TP=-2')
            stem = 'vox-tannoy'
        elif who == 'crowd':
            chain.append('loudnorm=I=-23:TP=-3')
            stem = VOX[who]
        else:
            chain.append('loudnorm=I=-16:TP=-1.5:LRA=11')
            stem = VOX[who]
        x = decode(V2 / ln['file'], af=','.join(chain))
        if b == '8':
            # The row through the earth under the POV and the chase; gone by the end of beat 9.
            stop = end['9'] - ln['t']
            if stop <= 0:
                continue
            x = x[:int(stop * SR)]
            x = x * env(len(x), [(0, 1), (max(0, stop - 1.5), 1), (stop, 0)])[:len(x)]
        mx.add(stem, x, ln['t'], V2 / ln['file'], f"beat {b} line {ln['i']} {who}")

    # ---- music
    # M0 her radio: the GPOM track, tinny; down to nothing on "Oh, hello!", back up on "Mind how you go"
    # (the last ~1.3 s of her last line), cued so the drop lands there; hard cut to the roundabout.
    l0, l5 = L[('0', 0)], L[('0', 5)]
    up = l5[1] - 1.3 - start['0']
    d0 = end['0'] - start['0']
    x = level(decode(MUSIC['M0'], DROP - up, d0, af=RADIO), rms=-23)
    hello = l0[0] - start['0']
    x *= env(len(x), [(0, 0), (0.3, 1), (hello - 0.1, 1), (hello + 0.5, 0), (up - 0.3, 0), (up + 0.3, 1),
                      (d0 - 0.03, 1), (d0, 0)])
    mx.add('mus-M0-radio', x, start['0'], MUSIC['M0'], 'M0 her radio (tinny GPOM track)')
    # S1 the hunt: beats 1-3, dead on the first ping.
    d = start['4'] - start['1']
    x = fades(level(decode(MUSIC['S1'], 0.33, d), rms=-17, peak=-1), 0.15, 0.03)
    mx.add('mus-S1-hunt', x, start['1'], MUSIC['S1'], 'S1 the hunt')
    # S2 the chase: on the red flip; ducked under Maddie's call (11 and 11b); dead on the first explosion.
    s2 = start['8'] + B['8']['flip']
    d = start['12'] - s2
    x = level(decode(MUSIC['S2'], 0, d), rms=-18, peak=-1)
    da, db = L[('11', 0)][0] - 0.3 - s2, L[('11b', 0)][1] - s2
    x *= env(len(x), [(0, 1), (da, 1), (da + 0.4, 0.22), (db, 0.22), (db + 0.3, 1), (d - 0.02, 1), (d, 0)])
    mx.add('mus-S2-chase', x, s2, MUSIC['S2'], 'S2 the chase')
    # M6 Maddie's theme: from 14a, under the tannoy and the doors, out on the old lady's first line.
    m6_end = L[('17', 0)][0] + 0.4
    d = m6_end - start['14a']
    x = level(decode(MUSIC['M6'], 0, d), rms=-26, peak=-3)
    ta = L[('14b', 0)]
    x *= env(len(x), [(0, 0), (0.8, 1), (ta[0] - start['14a'] - 0.2, 1), (ta[0] - start['14a'] + 0.2, 0.6),
                      (ta[1] - start['14a'], 0.6), (ta[1] - start['14a'] + 0.5, 1), (d - 1.5, 1), (d, 0)])
    mx.add('mus-M6-maddie', x, start['14a'], MUSIC['M6'], "M6 Maddie's theme")
    # S3 the hymn: under the AI's apology; out for Derek's "Fuck that"; back on "I'm going"; to the end.
    s3 = L[('18', 1)][0] - 0.5
    d = total - s3
    x = level(decode(MUSIC['S3'], 0, d), rms=-25, peak=-3)
    f0, going = L[('18', 4)][0] - s3, L[('18', 5)][1] - 1.0 - s3
    x *= env(len(x), [(0, 0), (2.0, 1), (f0 - 0.4, 1), (f0, 0), (going, 0), (going + 0.8, 1.25), (d - 1.2, 1.25),
                      (d, 0)])
    mx.add('mus-S3-hymn', x, s3, MUSIC['S3'], 'S3 the hymn (cornet)')

    # ---- sfx
    def fx(stem, name, t, dur=None, src_in=0.0, rms=None, peak=None, fi=0.0, fo=0.0, af=None, what=''):
        p = name if isinstance(name, pathlib.Path) else SFX / name
        x = decode(p, src_in, dur, af)
        x = fades(level(x, rms, peak), fi, fo)
        mx.add(stem, x, t, p, what or p.stem)

    wind = src_dir / 'synth-wind-60s.wav'
    if not wind.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i',
                        'anoisesrc=d=60:c=brown:r=48000:a=0.6,highpass=f=60,lowpass=f=700,tremolo=f=0.12:d=0.7,'
                        'aformat=channel_layouts=stereo', str(wind)], check=True)
    # Wind down the empty street and round the ring (beats 0-3).
    fx('sfx-wind', wind, 0, end['3'], rms=-34, fi=1.0, fo=0.05, what='wind (ffmpeg)')
    # Beat 0: her wheels and beacon.
    fx('sfx-maddie', 'fs468517-robot-wheels-suitcase-street.mp3', 0, end['0'], src_in=5, rms=-33, fi=0.5,
       fo=1.0, what='her wheels on tarmac')
    for k in np.arange(0.5, end['0'] - 0.5, 2.5):
        fx('sfx-beacon', 'synth-beacon-blip.wav', k, rms=-36, what='beacon blip')
    # Beats 1-3: the kill bots.
    fx('sfx-killbots', 'fs522673-killbot-drone-engine-flyby.mp3', start['1'], start['4'] - start['1'], src_in=2,
       rms=-28, fi=0.3, fo=0.03, what='engines round the ring')
    fx('sfx-killbots', 'fs557594-killbot-mech-walk.mp3', start['2'], end['2'] - start['2'] + 0.5, rms=-22,
       peak=-3, fo=0.4, what='tracks closing in')
    fx('sfx-killbots', 'fs824121-killbot-servo.mp3', start['3'], end['3'] - start['3'], src_in=1, rms=-28,
       fo=0.03, what='servo whine')
    fx('sfx-hud', 'synth-cctv-hiss-20s.wav', start['3'], end['3'] - start['3'], rms=-36, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', 'synth-hud-blip.wav', start['3'] + 0.3, peak=-12, what='HUD tone')
    # Beat 4: the three pings (0 / 1.1 / 2.2 s), the row muffled under them (voice stem above).
    fx('sfx-hud', 'synth-killbot-three-pings.wav', start['4'], peak=-6, what='three pings')
    fx('sfx-hud', 'synth-cctv-hiss-20s.wav', start['4'], end['4'] - start['4'], rms=-40, fo=0.03, what='CCTV hiss')
    # Beats 6-7 and 13: the tiled room.
    for a, b in (('6', '7'), ('13', '13')):
        fx('sfx-rooms', 'fs767306-room-tiled-public-bathroom.mp3', start[a], end[b] - start[a], src_in=10,
           rms=-42, fi=0.05, fo=0.05, what='tiled room tone')
    # Beat 8: the hiss under the POV, the red flip, then engines through 8-10 and the fly-past at 9.
    flip = start['8'] + B['8']['flip']
    fx('sfx-hud', 'synth-cctv-hiss-20s.wav', start['8'], flip - start['8'], rms=-40, fo=0.03, what='CCTV hiss')
    fx('sfx-hud', 'synth-killbot-red-flip.wav', flip - 0.05, peak=-6, what='red flip tone')
    fx('sfx-killbots', 'fs522673-killbot-drone-engine-flyby.mp3', flip, start['11'] - flip, src_in=20, rms=-24,
       fi=0.1, fo=1.5, what='engines, the chase')
    fx('sfx-killbots', 'fs189446-killbot-jet-flyby.mp3', start['9'] - 0.6, end['9'] - start['9'] + 2.5, src_in=4,
       rms=-22, peak=-3, fi=0.3, fo=1.0, what='three machines tearing past Maddie')
    fx('sfx-killbots', 'fs557594-killbot-mech-walk.mp3', start['10'], end['10'] - start['10'], rms=-28, fo=0.5,
       what='tracks across the downs')
    # Beats 11 and 18: the beacon pulses on the AI's words.
    for key in [k for k in L if k[0] in ('11', '11b', '18')]:
        ln = next(x for x in rc['lines'] if x['beat'] == key[0] and x['i'] == key[1])
        if ln['who'] != 'ai':
            continue
        a, e = L[key]
        for k in np.arange(a, e, 0.9):
            fx('sfx-beacon', 'synth-beacon-blip.wav', k, rms=-34, what='beacon on his words')
    # Beat 12: three explosions; the ringing after.
    s12 = start['12']
    fx('sfx-explosions', 'fs177556-explosion-massive.mp3', s12, 6.0, rms=-13, peak=-1, fo=2.0, what='explosion 1')
    fx('sfx-explosions', 'fs189779-explosion-big-boom.mp3', s12 + 0.8, 5.0, rms=-15, peak=-1, fo=2.0,
       what='explosion 2')
    fx('sfx-explosions', 'fs189779-explosion-big-boom.mp3', s12 + 1.6, 4.0, rms=-16, peak=-1.5, fo=1.5,
       af='asetrate=48000*0.84,aresample=48000', what='explosion 3 (pitched down)')
    fx('sfx-explosions', 'fs132929-explosion-rubble-debris.mp3', s12 + 1.0, end['12'] - s12 - 1.0 + 0.3,
       rms=-22, fo=0.3, what='debris')
    ring_at = s12 + 1.7
    fx('sfx-ringing', 'synth-tinnitus-ring-10s.wav', ring_at, start['14a'] - ring_at + 0.5, rms=-34, fi=0.4,
       fo=1.5, what='ringing after')
    # Beat 13: muffled booms through the rock, dust.
    s13 = start['13']
    fx('sfx-muffled', 'derived-muffled-boom-massive.wav', s13, 4.0, rms=-20, peak=-3, fo=1.5, what='muffled boom')
    fx('sfx-muffled', 'derived-muffled-boom-big.wav', s13 + 0.7, 3.0, rms=-23, peak=-4, fo=1.5,
       what='muffled boom 2')
    fx('sfx-muffled', 'derived-dust-falling-12s.wav', s13, end['13'] - s13 + 0.3, rms=-32, fi=0.2, fo=0.3,
       what='dust falling')
    # 14a: wheels skidding up to the doors, bunting, crackling metal.
    s = start['14a']
    fx('sfx-maddie', 'fs468517-robot-wheels-suitcase-street.mp3', s, end['14a'] - s - 0.8, src_in=30, rms=-26,
       fi=0.3, fo=0.6, what='her wheels racing up')
    fx('sfx-maddie', 'fs701647-bunting-fabric-flap.mp3', s, end['14a'] - s, rms=-32, fi=0.3, fo=0.5,
       what='bunting flapping')
    fx('sfx-explosions', 'fs560510-explosion-debris-short.mp3', s, end['14a'] - s, src_in=3, rms=-32, fi=0.5,
       fo=0.5, what='crackling wreckage')
    # 14b: tannoy click, feedback whine, crackle under her voice.
    s = start['14b']
    fx('sfx-tannoy', 'synth-tannoy-click.wav', s + 0.1, peak=-8, what='tannoy click')
    fx('sfx-tannoy', 'fs489566-tannoy-feedback-short.mp3', s + 0.3, rms=-26, peak=-10, fo=0.3,
       what='feedback whine')
    fx('sfx-tannoy', 'fs530037-tannoy-pa-static.mp3', s + 0.2, end['14b'] - s - 0.2, src_in=10, rms=-38,
       fi=0.2, fo=0.3, what='crackle')
    fx('sfx-tannoy', 'synth-tannoy-click.wav', L[('14b', 0)][1] + 0.2, peak=-10, what='tannoy click off')
    # 14: the blast doors.
    s = start['14']
    fx('sfx-doors', 'fs406197-blastdoor-metal-slam.mp3', s + 0.1, rms=-18, peak=-2, what='door clang')
    fx('sfx-doors', 'fs500547-blastdoor-heavy-mechanical.mp3', s + 0.4, end['14'] - s - 0.4, src_in=2, rms=-22,
       peak=-3, fi=0.2, fo=0.8, what='door grind')
    # 15: wheels on concrete, bunting.
    s = start['15']
    fx('sfx-maddie', 'fs468517-robot-wheels-suitcase-street.mp3', s, 3.0, src_in=50, rms=-32, fi=0.3, fo=0.8,
       what='wheels on concrete')
    fx('sfx-maddie', 'fs701647-bunting-fabric-flap.mp3', s, end['15'] - s, src_in=4, rms=-36, fi=0.5, fo=0.8,
       what='bunting')
    # 17: corridor tone; the CCTV replay plays dry and tinny.
    fx('sfx-rooms', 'fs767306-room-tiled-public-bathroom.mp3', start['17'], end['17'] - start['17'], src_in=40,
       rms=-44, fi=0.3, fo=0.3, what='corridor tone')
    cctv = next(c for c in rc['clips'] if c['beat'] == '17' and 'sh-18b' in (c.get('src') or c['file']))
    fx('sfx-cctv', 'fs177556-explosion-massive.mp3', cctv['t'], cctv['dur'], rms=-26, fo=0.1, af=RADIO,
       what='CCTV replay, tinny')
    # 18: the canteen, a hundred people shifting, the murmur rising under the crowd lines.
    s = start['18']
    fx('sfx-rooms', 'fs625112-room-canteen-crowd.mp3', s, total - s, src_in=5, rms=-44, fi=0.5, fo=1.0,
       what='canteen tone')
    fx('sfx-crowd', 'fs189231-crowd-shuffling.mp3', s, min(21.0, total - s), rms=-38, fi=0.5, fo=1.5,
       what='a hundred people shifting')
    m = L[('18', 3)]
    fx('sfx-crowd', 'fs653920-crowd-small-walla.mp3', m[0] - 1.0, m[1] - m[0] + 2.5, src_in=3, rms=-30, fi=1.0,
       fo=1.2, what='the murmur rising')

    # ---- write: one global gain so the stems sum to a mix at about -16 LUFS; stems float, mix limited
    stems_dir = C2 / 'stems'
    stems_dir.mkdir(parents=True, exist_ok=True)
    for p in stems_dir.glob('*.wav'):
        p.unlink()
    n = int(round(total * SR))
    summed = sum(s[:n] for s in mx.stems.values())
    tmp = C2 / 'mix-raw.wav'
    write_wav(tmp, summed)
    lufs = integrated(tmp)
    g = 10 ** ((-16.0 - lufs) / 20)
    tracks = []
    order = sorted(mx.stems, key=lambda k: (['vox', 'mus', 'sfx'].index(k.split('-')[0]), k))
    for k, name in enumerate(order):
        p = stems_dir / f'{k + 1:02d}-{name}.wav'
        write_wav(p, mx.stems[name][:n] * g)
        tracks.append(dict(track=f'A{k + 1}', name=name, file=str(p), start=0.0,
                           peak_db=round(float(20 * np.log10(np.max(np.abs(mx.stems[name][:n] * g)) + 1e-12)), 1)))
    write_wav(tmp, summed * g)
    mix = C2 / 'mix.wav'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(tmp), '-af', 'alimiter=limit=0.891:level=false',
                    '-c:a', 'pcm_s24le', str(mix)], check=True)
    tmp.unlink()
    edl = dict(sequence=SEQ, fps=FPS, sample_rate=SR, total=rc['total'],
               beats=[dict(id=b['id'], title=b['title'], start=b['start'], dur=b['dur']) for b in rc['beats']],
               video=[dict(file=c['file'], **{'in': c['in']}, dur=c['dur'], start=c['t'], beat=c['beat'],
                           source=c.get('src', c['file'])) for c in rc['clips']],
               audio=tracks, mix=str(mix), events=mx.events, flags=rc['flags'])
    (C2 / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(f'mix {integrated(mix):.1f} LUFS (raw {lufs:.1f}, gain {20 * np.log10(g):+.1f} dB), {len(tracks)} stems')
    for t in tracks:
        print(f"  {t['track']:>3} {t['name']:18s} peak {t['peak_db']:6.1f} dB")


def write_wav(p, x):
    x = np.ascontiguousarray(x, dtype=np.float32)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                    '-c:a', 'pcm_f32le', str(p)], input=x.tobytes(), check=True)


def integrated(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(p), '-af', 'ebur128', '-f', 'null', '-'],
                       capture_output=True, text=True)
    line = [ln for ln in r.stderr.splitlines() if ln.strip().startswith('I:')][-1]
    return float(line.split()[1])


# ---------------------------------------------------------------- preview

def preview():
    edl = json.loads((C2 / 'edl.json').read_text())
    parts = C2 / 'preview-parts'
    parts.mkdir(exist_ok=True)
    lst = []
    for k, c in enumerate(edl['video']):
        out = parts / f'{k:03d}.mp4'
        vf = f'scale=1280:720,fps={FPS},setsar=1'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{c['in']:.4f}", '-i', c['file'],
                        '-t', f"{c['dur']:.4f}", '-vf', vf, '-frames:v', str(int(round(c['dur'] * FPS))),
                        *ENC, str(out)], check=True)
        lst.append(f"file '{out}'")
    (parts / 'list.txt').write_text('\n'.join(lst) + '\n')
    pic = parts / 'picture.mp4'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(parts / 'list.txt'),
                    '-c', 'copy', str(pic)], check=True)
    # Burn the beat number in the corner so notes can name it.
    draw = ','.join(
        f"drawtext=text='{b['id']}':x=w-tw-16:y=12:fontsize=22:fontcolor=white@0.7:box=1:boxcolor=black@0.4:"
        f"enable='between(t,{b['start']:.3f},{b['start'] + b['dur'] - 0.001:.3f})'" for b in edl['beats'])
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(pic), '-i', edl['mix'], '-map', '0:v', '-map', '1:a',
                    '-vf', draw, '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:a', 'aac', '-b:a', '256k', '-shortest', str(PREVIEW)], check=True)
    sheet = S.CLIPS / 'cut2-preview-sheet.jpg'
    tot = probe(PREVIEW)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(PREVIEW), '-vf',
                    f"select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,{tot / 48:.3f})',scale=320:-2,"
                    "drawtext=text='%{pts\\:hms}':x=6:y=6:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.5,"
                    "tile=6x8", '-vsync', 'vfr', '-frames:v', '1', str(sheet)], check=True)
    for p in parts.glob('*'):
        p.unlink()
    parts.rmdir()
    print(f'{PREVIEW} {tot:.2f}s; sheet {sheet}')


# ---------------------------------------------------------------- Premiere placement (phase 3)

def place(argv):
    """premiere_eval body placing edl.json on SEQ: picture on V1 (in/out), each stem on its own audio
    track at 0. Items addressed by Premiere id from <cache>/premiere-ids-cut2.json ({path: id}),
    written from the import results; the sequence needs len(audio) audio tracks."""
    import os
    edl = json.loads((C2 / 'edl.json').read_text())
    if argv[0] == 'count':
        print(len(edl['video']) + len(edl['audio']))
        return
    ids = json.loads((pathlib.Path(os.environ['HOME']) / '.cache/badcode-gpom-second-half/premiere-ids-cut2.json')
                     .read_text())
    rows = [[ids[c['file']], c['start'], c['in'], c['dur'], 'v', 0] for c in edl['video']]
    rows += [[ids[a['file']], 0, 0, 0, 'a', k] for k, a in enumerate(edl['audio'])]
    a, b = int(argv[1]), int(argv[2])
    print("""const plan=%s;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!=='%s') return {error:'wrong sequence',name:seq.name};
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002);
let done=0; const fail=[];
for(const [id,t,i,d,kind,tr] of plan){ try{
  const item=await helpers.resolveProjectItem(project,id); const clip=ppro.ClipProjectItem.cast(item);
  if(kind==='v'){
    helpers.withTransaction(project,'rough2 in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
    helpers.withTransaction(project,'rough2 place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,0)));
    helpers.withTransaction(project,'rough2 clear',ca=>ca.addAction(clip.createClearInOutPointsAction()));
  } else {
    helpers.withTransaction(project,'rough2 place audio',ca=>ca.addAction(ed.createOverwriteItemAction(item,helpers.secondsToTick(t),0,tr)));
  }
  done++; }catch(e){ fail.push([id,t,String(e&&e.message||e).slice(0,120)]); } }
const saved=await project.save();
return {done,fail,saved,range:[%d,%d]};""" % (json.dumps(rows[a:b], separators=(',', ':')), SEQ, a, min(b, len(rows))))
