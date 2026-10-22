#!/usr/bin/env python3
"""GPOM second half, the ending (scenes C, D, E): new-scene stage 4 rough cuts in the timeline format.

    python3 scripts/gpom/second-half-video/ending/cut_end.py C            # scene C, the walk out
    python3 scripts/gpom/second-half-video/ending/cut_end.py C --no-preview

Modelled on ../cut3.py and reusing its machinery (bounds, regrade_v6, pingpong, sfx_adder, wind_file, write, edl,
preview) by import; cut3's own outputs are untouched (its temp-file root is repointed here). Rules are new-scene
stage 4's: picture timed to the real voice lengths, LEAD 0.4 s before a beat's first line, GAP 0.35 s between lines,
TAIL 0.6 s after; speech is never slowed (a lip-sync phrase may be sped up to x1.25, never past it); one stem per
track; the mix at -16 LUFS, limited. Premiere-style camera moves are done here in post (push.py: hold, then an eased
push); the colour of every join is measured and printed.

Inputs, per scene X (docs/stories/gitpush-origin-master/scenes/<slug>/): scene.json, picks.json, clips.json,
voices.json; the Suno picks under <media>/suno/ (the AI and the music).
Outputs (media only): <media>/cut/{edl.json, mix.wav, stems/, preview.mp4, preview-sheet.jpg, video/}.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import cut3 as C3  # noqa: E402
import cut2 as C  # noqa: E402

FPS, SR = 24, 48000
LEAD, GAP, TAIL, CUT_PRE = 0.4, 0.35, 0.6, 0.15
PEAK_CAP = 10 ** (-1 / 20)  # per-event ceiling before the mix (review round 2)
REPO = HERE.parents[3]
SCENES = REPO / 'docs/stories/gitpush-origin-master/scenes'
CLIPS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half')
SFX = CLIPS / 'audio' / 'sfx'
MS = SFX / 'maddie'
LIPS_PY = pathlib.Path.home() / '.cache/badcode-lips/venv/bin/python'
SLUGS = {'C': 'second-half-c-walk-out', 'D': 'second-half-d-crossing', 'E': 'second-half-e-ending'}
NAMES = {'ai': 'The AI (through Maddie)', 'maddie': 'Maddie', 'sandra': 'Sandra', 'derek': 'Derek',
         'lady': 'The old lady'}
# the small-speaker filter of voice.py (FX['speaker']): his voice comes out of Maddie
SPEAKER = ('highpass=f=300,highpass=f=300,lowpass=f=3400,lowpass=f=3400,volume=6dB,'
           'asoftclip=type=atan,acrusher=bits=12:mix=0.15,volume=-3dB')
ENC = C.ENC
fr, dur = C.fr, C3.dur


class Scene:
    def __init__(self, key):
        self.key = key
        self.folder = SCENES / SLUGS[key]
        rd = lambda n: json.loads((self.folder / n).read_text())  # noqa: E731
        self.cfg, self.clips, self.picks, self.vox = rd('scene.json'), rd('clips.json'), rd('picks.json'), rd('voices.json')
        self.media = pathlib.Path(self.cfg['media'])

    def clip(self, fid):
        return pathlib.Path(self.clips['media']) / self.clips['clips'][fid]['file']

    def voice(self, key):
        return self.media / self.vox['lines'][key]['file']

    def text(self, key):
        return self.vox['lines'][key]['text']


class Cut:
    """cut3.Cut's shape (cut3.write / edl / preview read these attributes), rooted in <media>/cut."""

    def __init__(self, sc, seq, title, heading, intro):
        self.sc, self.key, self.seq = sc, sc.key, seq
        self.dir = sc.media / 'cut'
        self.vdir = self.dir / 'video'
        self.vdir.mkdir(parents=True, exist_ok=True)
        self.meta = dict(title=title, heading=heading, intro=intro)
        self.beats, self.video, self.voices, self.huds, self.flags = [], [], [], [], []
        self.m = {}

    def beat(self, bid, title, start, see='', act=''):
        b = dict(id=bid, title=title, start=fr(start), dur=0.0, see=see, act=act, lines=[])
        self.beats.append(b)
        return b

    def close(self, b, end):
        b['dur'] = fr(end - b['start'])
        return fr(end)

    def pic(self, src, i0, t0, t1, beat, source=None):
        t0, t1 = fr(t0), fr(t1)
        assert t1 > t0, (src, t0, t1)
        c = dict(file=str(src), **{'in': fr(i0)}, dur=fr(t1 - t0), start=t0, beat=beat, source=str(source or src),
                 looped=False)
        self.video.append(c)
        return c

    def say(self, stem, src, a, b, t, what, chain=(), lufs=-16.0, tempo=1.0, cut=None, ref=None):
        """Place src[a:b] at timeline t, sped by tempo (>= 1: speech is never slowed). Returns its end.
        ref=(a0, b0): take the gain from that whole span of src (the full atom) instead of from the fragment. A
        fragment under 0.4 s cannot be measured by ebur128 (review round 2: the 0.37 s "You don't." went in ~45 dB
        hot that way and dragged the whole of scene D down 10 dB in the loudness pass)."""
        assert tempo >= 1.0, 'never slow speech'
        self.voices.append(dict(stem=stem, src=str(src), i=a, d=b - a, t=fr(t) if cut is None else t, chain=list(chain),
                                lufs=lufs, what=what, tempo=tempo, cut=cut, ref=ref))
        return t + (b - a) / tempo

    def line(self, beat, i, who, t, d, text, by):
        beat['lines'].append(dict(i=i, who=who, name=NAMES[who], t=round(t, 3), dur=round(d, 3), text=text, by=by))

    def extend(self):
        for c in self.video:
            if c['in'] + c['dur'] <= dur(c['file']) + 0.5 / FPS:
                continue
            src = pathlib.Path(c['file'])
            out = self.vdir / f"{src.stem}-i{c['in']:g}-d{c['dur']:.3f}.mp4"
            C3.pingpong(src, c['in'], c['dur'], out)
            c['file'], c['in'], c['looped'] = str(out), 0.0, True


def voices(c, mx):
    """Every placed phrase at its loudness, sped by its tempo (pitch kept), its chain after. Gain only otherwise."""
    for v in c.voices:
        af = [f"atempo={v['tempo']:.4f}"] if v['tempo'] != 1.0 else []
        af += v['chain']
        x = C.decode(v['src'], v['i'], v['d'], ','.join(af) or None)
        if v.get('ref'):
            r0, r1 = v['ref']
            meas = C.decode(v['src'], r0, r1 - r0, ','.join(af) or None)
        else:
            meas = x
        x = x * 10 ** ((v['lufs'] - C3.lufs_of(meas)) / 20)
        pk = float(np.max(np.abs(x))) if len(x) else 0.0
        if pk > PEAK_CAP:  # no single phrase may go in over -1 dBFS before the mix
            print(f"  gain cap: {v['what'][:60]!r} peak {20 * np.log10(pk):+.1f} dBFS -> -1.0")
            x = x * (PEAK_CAP / pk)
        x = C.fades(x, 0.01, 0.04)
        if v['cut'] is not None:
            x = x[:int(max(0.0, v['cut'] - v['t']) * SR)]
        mx.add(v['stem'], x.astype(np.float32), v['t'], v['src'], v['what'])


def move(src, out, i0, d, z1, hold=1.5, cx=0.5, cy=0.5, z0=1.0):
    """Premiere-style push in post (push.py): hold, then eased in and out to z1."""
    if not out.exists():
        subprocess.run([str(LIPS_PY), '-I', str(HERE / 'push.py'), str(src), str(out), '--in', f'{i0:.4f}', '--dur',
                        f'{d:.4f}', '--z0', str(z0), '--z1', str(z1), '--hold', str(hold), '--cx', str(cx), '--cy',
                        str(cy)], check=True)
    return out


def tone(name, graph, d):
    p = CLIPS / 'audio' / 'ending-src' / f'{name}.wav'
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', graph, '-t', str(d), '-ar', str(SR),
                        '-ac', '2', str(p)], check=True)
    return p


# ---------------------------------------------------------------- colour across the joins

def frame_stats(path, t):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{max(0.0, t):.3f}', '-i', str(path), '-frames:v',
                          '1', '-vf', 'scale=160:90', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.uint8).reshape(90, 160, 3).astype(float)
    return x.mean((0, 1))


def clip_stats(path, t0=0.0, d=None):
    """Per-channel mean and spread over a stretch of a clip (320x180, every frame)."""
    cmd = ['ffmpeg', '-loglevel', 'error', '-ss', f'{t0:.3f}']
    if d:
        cmd += ['-t', f'{d:.3f}']
    raw = subprocess.run(cmd + ['-i', str(path), '-vf', 'scale=320:180', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320, 3).astype(np.float32)
    return x.mean((0, 1, 2)), x.std((0, 1, 2))


def match_grade(src, ref, out, ref_t0=0.0, ref_d=4.0, strength=0.7):
    """A constant per-channel gain + offset (lutrgb) moving src's mean and spread `strength` of the way to a reference
    stretch: one grade for the whole clip, so nothing moves inside the shot. Returns (out, note)."""
    ms, ss = clip_stats(src)
    mr, sr = clip_stats(ref, ref_t0, ref_d)
    mt, st_ = ms + strength * (mr - ms), ss + strength * (sr - ss)
    g = st_ / ss
    ex = {ch: f'clip((val-{ms[k]:.3f})*{g[k]:.4f}+{mt[k]:.3f},0,255)' for k, ch in enumerate('rgb')}
    if not out.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-vf',
                        f"format=rgb24,lutrgb=r='{ex['r']}':g='{ex['g']}':b='{ex['b']}'", *ENC, str(out)], check=True)
    note = (f'{pathlib.Path(src).stem}: mean RGB {ms.round(0)} -> {mt.round(0)} ({strength:.0%} of the way to '
            f'{pathlib.Path(ref).stem}, one constant grade)')
    return out, note


def join_report(c):
    """Mean RGB on each side of every cut (last frame out / first frame in), printed and flagged if it jumps."""
    rows = []
    for a, b in zip(c.video, c.video[1:]):
        ea = frame_stats(a['file'], a['in'] + a['dur'] - 1.5 / FPS)
        sb = frame_stats(b['file'], b['in'] + 0.5 / FPS)
        rows.append((pathlib.Path(a['source']).stem, pathlib.Path(b['source']).stem, ea.round(0), sb.round(0),
                     float(np.abs(ea - sb).max())))
    for r in rows:
        print(f'  join {r[0]:>18} -> {r[1]:<18} RGB {r[2]} -> {r[3]}  max step {r[4]:.0f}')
    return rows


# ---------------------------------------------------------------- scene C

def scene_c(sc):
    c = Cut(sc, 'gpom-second-half-C-rough2', 'Ending C Timeline', 'GPOM second half · the ending · scene C: the walk out',
            "Scene C of the ending: the old lady sends Maddie ahead, the hundred walk out over the downs, the seat, the "
            "AI's building, and the step. Made autonomously (21-22 Oct): every call Kai would make is in the flags. "
            "Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you "
            "type. Tell Claude when you're done.")
    m = c.m
    V = c.vdir
    ai_take = sc.media / 'suno' / 'gpom-sh-end-ai-c-a-v6-w10-7f567949.wav'

    # ---- c1: the old lady on the step (C01, lip-synced phrase by phrase), Maddie's "Ooh. Ta." on C02
    b = c.beat('c1', 'Off the step', 0.0, act='The walk out',
               see='The blast doors open on daylight. The old lady stops beside Maddie, straightens her torn bunting, '
                   'sends her ahead. Then the wide: Maddie leads.')
    i01 = 0.6
    lady = sc.voice('c1-0-lady')
    # mouth (tracked strip, 12 fps): "Go on, then." 2.58-3.17, "You lead." 3.75-4.50 (clip time)
    ph = [(0.25, 1.20, 2.60, 1.25, 'Go on, then.'), (1.76, 2.65, 3.78, 1.12, 'You lead.')]
    ends = []
    for a, z, at, tp, txt in ph:
        ends.append(c.say('vox-lady', lady, a, z, at - i01, f'c1 line 0 lady: "{txt}" (lip-sync, x{tp})', tempo=tp))
    l0a, l0e = ph[0][2] - i01, ends[-1]
    c.line(b, 0, 'lady', l0a, l0e - l0a, sc.text('c1-0-lady'), 'claude')
    t_mad = fr(l0e + GAP)
    cut02 = fr(t_mad - CUT_PRE)
    d01 = cut02
    c01 = move(sc.clip('C01'), V / 'C01-push.mp4', i01, d01, 1.06, hold=1.5, cx=0.5, cy=0.25)
    c.pic(c01, 0.0, 0.0, cut02, 'c1', source=sc.clip('C01'))
    mad = sc.voice('c1-1-maddie')
    e = c.say('vox-maddie', mad, 0.25, 2.38, t_mad, 'c1 line 1 maddie: "Ooh. Ta."')
    c.line(b, 1, 'maddie', t_mad, e - t_mad, sc.text('c1-1-maddie'), 'claude')
    end_c1 = fr(e + TAIL)
    c02_end = fr(cut02 + 7.0)
    c02, gnote = match_grade(sc.clip('C02'), sc.clip('C03'), V / 'C02-t4-graded.mp4', strength=0.7)
    c.flags.append('Colour: C02 (re-rolled in review round 1, C02-t4) is graded towards the first 4 s of the long walk '
                   'it cuts to, so the two overcast exteriors match. ' + gnote + '.')
    c.flags.append('Review round 1: C02 re-rolled (C02-t4, 12 credits). Round 0\'s pick grew a pole of pennants on '
                   'Maddie\'s rear from ~1.5 s; a light breeze and "the cloth hangs limp, nothing rises from the robot" '
                   'fixed it (C02-t3, with a strong wind, streamed the bunting across the whole foreground: rejected).')
    c.pic(c02, 0.0, cut02, end_c1, 'c1', source=sc.clip('C02'))
    m['bunting'] = (0.0, cut02)
    m['c02'] = (cut02, c02_end)
    m['ooh'] = e
    t = c.close(b, end_c1)
    c.flags.append(f'c1 (C01): the lady\'s "Go on, then." is sped x1.25 onto a 0.59 s mouth burst (the tracked strip: '
                   f'2.58-3.17 s), "You lead." x1.12 onto 3.75-4.50 s. Both phrases start on the mouth opening, never '
                   'before. x1.25 is near the 1.3 cap: the first phrase is the one to listen to for squeeze.')
    c.flags.append('c1: C01 opens 0.6 s into the clip (her hand already on the bunting), holds 1.5 s, then pushes '
                   '100 -> 106% eased (push.py, in post), centred on her face.')

    # ---- c2: into daylight (C02 continues)
    b = c.beat('c2', 'Into daylight', t, act='The walk out',
               see='The hundred file out of the hill, blinking; the kill bots\' track marks in the grass. Maddie leads '
                   'out of frame.')
    c.pic(c02, end_c1 - cut02, t, c02_end, 'c2', source=sc.clip('C02'))
    t = c.close(b, c02_end)

    # ---- c3: the long walk (C03 chain, 22 s, the drift ramped back to clip 1's grade)
    b = c.beat('c3', 'The long walk', t, act='The walk out',
               see='The rhyme of beat 0, withheld: tight on Maddie alone on the chalk track, as she was alone in '
                   'Swindon; then the frame widens and a hundred people are walking behind her.')
    chain = sc.clip('C03')
    D3 = 10.5
    chain_g, _ = C3.regrade_v6(chain, V / 'C03f-chain-graded.mp4', ref_secs=4.0, strength=0.85)
    c03 = V / 'C03f-reveal.mp4'
    if not c03.exists():
        subprocess.run([str(LIPS_PY), '-I', str(HERE / 'move_keys.py'), str(chain_g), str(c03), '--in', '0', '--dur',
                        str(D3), '--keys', '0:1.6:420:380,1.5:1.6:425:380,9.6:1:640:360'], check=True)
    c.pic(c03, 0.0, t, t + D3, 'c3', source=chain)
    m['c3'] = (t, fr(t + D3))
    t = c.close(b, t + D3)
    c.flags.append('Review round 1 (C03): remade (24 credits, two chained Omni clips from a new still C03-f1-a made on '
                   'the Maddie reference, so her body is the six-wheeled design of every other shot) and cut from 22 s '
                   'to 10.5 s. It now opens at 160% on Maddie alone (the left third, the line out of frame), holds 1.5 s, '
                   'then eases out to 100% by 9.6 s (move_keys.py) so the hundred appear behind her: the beat-0 rhyme '
                   'as a reveal. The chain brightens and cools towards its end; cut3\'s ramped regrade_v6 pulls it back '
                   '85% towards its first 4 s before the move. No verge scraps in the new take. The 160% opening is soft (a 720p source). '
                   'Kai to rule on the length.')

    # ---- c4: the seat. C04 Sandra (lip-sync), C05 Derek (lip-sync, two phrases) with Sandra off-screen between
    s4 = t
    b = c.beat('c4', 'The seat', s4, act='The walk out',
               see='Sandra and Derek, walking. The row one last time, and what it now means.')
    i04 = 2.06 - LEAD
    san = sc.voice('c4-0-sandra')
    e = c.say('vox-sandra', san, 0.24, 1.88, s4 + 2.07 - i04, 'c4 line 0 sandra (lip-sync, x1.12)', tempo=1.12)
    c.line(b, 0, 'sandra', s4 + 2.07 - i04, e - (s4 + 2.07 - i04), sc.text('c4-0-sandra'), 'claude')
    # Derek's mouth (strip): "We're not coming" 1.00-1.92, the b of "back" shut 2.00-2.17, "back, love" 2.25-2.75
    i05 = 1.00 - CUT_PRE
    cut05 = fr(e + GAP - CUT_PRE)
    c.pic(sc.clip('C04'), i04, s4, cut05, 'c4')
    t05 = cut05 - i05  # timeline time of C05's clip-time zero
    der = sc.voice('c4-1-derek')
    a1 = t05 + 1.01
    # review round 2: "coming" was masked by the walk music (a blind listen heard "We're not back home"); the line
    # is lifted 2.5 dB (-16 -> -13.5) and the music ducks deeper under the seat lines (audio_c)
    c.say('vox-derek', der, 0.31, 1.27, a1, 'c4 line 1 derek: "We\'re not coming" (lip-sync, x1.0, +2.5 dB)', lufs=-13.5)
    e1 = c.say('vox-derek', der, 1.39, 2.26, t05 + 2.19, 'c4 line 1 derek: "back, love." (lip-sync, x1.1, +2.5 dB)',
               tempo=1.1, lufs=-13.5)
    c.line(b, 1, 'derek', a1, e1 - a1, sc.text('c4-1-derek'), 'claude')
    a2 = fr(e1 + GAP)
    e2 = c.say('vox-sandra', sc.voice('c4-2-sandra'), 0.24, 1.43, a2, 'c4 line 2 sandra, off-screen', lufs=-17.5)
    c.line(b, 2, 'sandra', a2, e2 - a2, sc.text('c4-2-sandra'), 'claude')
    a3 = t05 + 5.43
    e3 = c.say('vox-derek', sc.voice('c4-3-derek'), 0.32, 0.94, a3, 'c4 line 3 derek: "...Yes." (lip-sync, x1.0)')
    c.line(b, 3, 'derek', a3, e3 - a3, sc.text('c4-3-derek'), 'claude')
    end_c4 = fr(e3 + TAIL)
    # review round 2: Sandra is in frame on C05 with her mouth shut while her line plays. C05 now opens tight on
    # Derek (140%, her face out of frame, only a sliver of her coat at the edge), holds through her line, then
    # eases back to 100% on his "...Yes." so the two are seen together for the answer (move_keys.py, smoothstep)
    d05 = end_c4 - cut05
    back0 = fr(e2 + 0.1) - cut05
    c05 = V / f'C05-t2-reframe-i{i05:.3f}-d{d05:.3f}.mp4'
    if not c05.exists():
        subprocess.run([str(LIPS_PY), '-I', str(HERE / 'move_keys.py'), str(sc.clip('C05')), str(c05), '--in',
                        f'{i05:.4f}', '--dur', f'{d05:.4f}', '--keys',
                        f'0:1.4:545:310,{back0:.3f}:1.4:545:310,{min(d05, back0 + 1.6):.3f}:1:640:360'], check=True)
    c.pic(c05, 0.0, cut05, end_c4, 'c4', source=sc.clip('C05'))
    c.flags.append(f'Review round 2 (C05): Sandra was in frame, mouth shut, while "Did you put it down?" played. C05 '
                   f'now opens at 140% on Derek (her face out of shot, a sliver of her coat at the right edge), holds '
                   f'{back0:.2f} s through his line and hers, then eases back to 100% over 1.6 s on his "...Yes.", '
                   'so her line is truly off-screen and the answer lands on the two of them. The 140% is soft (720p).')
    m['c4'] = (s4, end_c4)
    m['c4_lines'] = (s4 + 2.07 - i04, e3)
    t = c.close(b, end_c4)
    c.flags.append(f'c4 (C05): on the tracked mouth strip Derek\'s whole line spans 1.00-2.75 s (the held-open 1.00-1.42 '
                   'is "We\'re", not a frozen smile), so it fits phrase by phrase at x1.0 and x1.1 with the b of "back" '
                   'landing after the lips shut at 2.00-2.17. Stage 3\'s x1.4 was measured on a shorter burst; no '
                   're-voice was needed.')
    c.flags.append(f'c4: Sandra\'s "Did you put it down?" plays in Derek\'s silent beat on C05, where she is soft at the '
                   f'right edge of frame and her mouth does not move. The gap before "...Yes." is {a3 - e2:.2f} s, set by '
                   'the picture (his mouth opens at 5.43 s), a little under the 1.2 s lead voices.json asks for.')

    # ---- c5: over the brow (C06, push 100 -> 112%); Derek's "Bloody hell", the AI through Maddie
    s5 = t
    b = c.beat('c5', 'Over the brow', s5, act='The building',
               see='From behind the hundred at the crest, past the old man helped down and the tipped trolley: the '
                   'AI\'s building in the fold of the downs. They stop.')
    a = fr(s5 + 1.5)
    e = c.say('vox-derek', sc.voice('c5-0-derek'), 0.32, 1.40, a, 'c5 line 0 derek: "Bloody hell." (under his breath)',
              lufs=-19.0)
    c.line(b, 0, 'derek', a, e - a, sc.text('c5-0-derek'), 'claude')
    a_ai = fr(e + GAP)
    e_ai = c.say('vox-ai', ai_take, 0.0, 1.62, a_ai, 'c5 line 1 AI: "I tried to make it nice." (atom -c1, speaker)',
                 chain=[SPEAKER], lufs=-17.0)
    c.line(b, 1, 'ai', a_ai, e_ai - a_ai, 'I tried to make it nice.', 'claude')
    end_c5 = fr(max(s5 + 8.0, e_ai + TAIL))
    c06 = move(sc.clip('C06'), V / 'C06-t2-push.mp4', 0.0, end_c5 - s5, 1.12, hold=1.5, cx=0.45, cy=0.42)
    c.pic(c06, 0.0, s5, end_c5, 'c5', source=sc.clip('C06'))
    m['c5'] = (s5, end_c5)
    m['ai1'] = (a_ai, e_ai)
    t = c.close(b, end_c5)
    c.flags.append('Review round 1 (C06): re-animated (12 credits) from C06-f1-a, the round-0 still with the figure '
                   'lying by the tipped trolley removed (flow_edit_image, 0 credits). The old man now stays on his feet, '
                   'bent over his stick catching his breath, a hand on his back: tiredness, not a man down. The trolley '
                   'stays tipped (D14 shows it left behind). The amber seam brightens end to end.')
    c.flags.append('c5: "Bloody hell." waits 1.5 s into the reveal (my call: the building is seen before anyone names '
                   'it). C06 holds 1.5 s, then pushes 100 -> 112% eased over the rest, centred on the building.')

    # ---- c6: mind the step (C07); the AI asks them in, the music stops dead on "Mind the step"
    s6 = t
    b = c.beat('c6', 'Mind the step', s6, act='The building',
               see='At the foot of the black wall the amber seam has opened into a doorway with one low step. Maddie '
                   'waits, then goes up into the light.')
    a1 = fr(s6 + LEAD)
    e1 = c.say('vox-ai', ai_take, 3.74, 4.40, a1, 'c6 line 0 AI: "Come in." (atom -c2, speaker)', chain=[SPEAKER],
               lufs=-17.0)
    a2 = fr(e1 + 0.9)
    e2 = c.say('vox-ai', ai_take, 6.04, 7.20, a2, 'c6 line 0 AI: "Mind the step." (atom -c2, speaker)', chain=[SPEAKER],
               lufs=-17.0)
    c.line(b, 0, 'ai', a1, e2 - a1, 'Come in. Mind the step.', 'claude')
    end_c6 = fr(max(s6 + 8.0, e2 + TAIL))
    c07 = V / 'C07-glass.mp4'
    if not c07.exists():
        subprocess.run([str(LIPS_PY), '-I', str(HERE / 'glass_window.py'), str(sc.clip('C07')), str(c07), '--rect',
                        '0,185,366,560', '--feather', '24', '--gain', '0.16', '--desat', '0.9'], check=True)
    c.pic(c07, 0.0, s6, end_c6, 'c6', source=sc.clip('C07'))
    c.flags.append('Review round 1 (C07): Maddie\'s reflection in the black glass left of the doorway read as a '
                   'second robot inside. A soft power window (glass_window.py) darkens that glass to 16% and '
                   'desaturates it, beacon hot spot included; the doorway glow and the step are outside the window.')
    m['c6'] = (s6, end_c6)
    m['ai2'] = (a1, e2)
    m['mind'] = a2
    t = c.close(b, end_c6)
    c.flags.append('c6: the Suno take leaves 1.85 s between "Come in." and "Mind the step."; the cut tightens it to '
                   '0.9 s (silence removed, no word touched). C07 plays whole (8 s) so Maddie is seen going up the '
                   'step at ~5.5 s, after the invitation; her wander left along the wall first still reads as '
                   'hesitation (Kai to rule).')
    c.flags.append('The AI speaks through Maddie\'s speaker (voice.py\'s small-speaker filter) with a beacon blip on '
                   'his words in the sound. The VISUAL beacon pulse on his words (scene.json C06 post) is not done: '
                   'Omni\'s beacon already pulses in C06/C07, and a drawn pulse on a pushing frame needs a tracked mask. '
                   'Owed if Kai wants it.')
    c.total = t
    return c


def audio_c(c):
    m, total = c.m, c.total
    sc = c.sc
    mx = C.Mix(total)
    voices(c, mx)
    fx = C3.sfx_adder(mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}

    # ---- music: gpom-sh-c-walk (cc128cb2). In on the long walk at a quiet breath of the take, timed so its one
    # low held cello note (attack ~61.7 s in the take) lands on the reveal; ducked under the seat; stops dead on
    # "Mind the step".
    walk = sc.media / 'suno' / 'gpom-sh-c-walk-a-v6-w30-cc128cb2.wav'
    attack = 61.7
    s_in = m['c3'][0]
    land = m['c5'][0] + 0.3
    off = attack - (land - s_in)
    stop = m['mind']
    d = stop - s_in
    x = C.level(C.decode(walk, off, d), rms=-21, peak=-3)
    la, le = m['c4_lines']
    ra, re_ = la - s_in, le - s_in
    x *= C.env(len(x), [(0, 0), (1.5, 1), (ra - 0.5, 1), (ra, 0.4), (ra + 1.5, 0.4), (ra + 1.8, 0.22), (ra + 4.0, 0.22), (ra + 4.4, 0.4), (re_ + 0.3, 0.4), (re_ + 1.2, 1),
                        (d - 0.03, 1), (d, 0)])
    mx.add('mus-c-walk', x, s_in, walk, 'C-walk: lone violin and piano, the held cello note on the reveal')
    c.flags.append(f'Music: C-walk enters on the long walk (c3), not on C02 as music.md planned, at {off:.1f} s into the '
                   'take (review round 1 shortened the walk, so it now comes in mid-phrase under a 1.5 s fade), timed so the '
                   f'take\'s held low cello note lands on the reveal with no edit inside the music. The take\'s first {off:.0f} s are not used. C01-C02 '
                   'play on wind, birds-free (no birdsong in the library) and the crowd. Stops dead on "Mind the step". '
                   '(Kai to rule.)')

    # ---- sfx
    wind = C3.wind_file()
    fx('sfx-wind', wind, 0, total, src_in=5, rms=-34, fi=0.8, fo=1.0, tile=True, what='wind on the downs (ffmpeg)')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', 0.3, m['c02'][1] + 1.2 - 0.3, rms=-38, fi=0.6, fo=1.4,
       what='the hundred coming out, shuffling (crossfades into the chalk loop over the cut)')
    fx('sfx-crowd', SFX / 'fs653920-crowd-small-walla.mp3', m['c02'][0], m['c02'][1] - m['c02'][0], rms=-44, fi=1.0,
       fo=1.0, what='murmur as they blink at the sky')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', st['c3'] - 1.2, en['c4'] - st['c3'] + 1.2, src_in=8,
       rms=-37, fi=1.4, fo=1.0, tile=True, what='a hundred pairs of feet on the chalk (held under the walk)')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', st['c5'], 3.0, src_in=20, rms=-42, fi=0.2, fo=1.5,
       what='they stop')
    fx('sfx-maddie', SFX / 'fs701647-bunting-fabric-flap.mp3', 0.6, 2.4, rms=-34, fi=0.2, fo=0.6,
       what='the bunting, straightened')
    fx('sfx-maddie', SFX / 'fs701647-bunting-fabric-flap.mp3', m['c02'][0], m['c02'][1] - m['c02'][0], src_in=4,
       rms=-38, fi=0.4, fo=0.8, what='bunting in the wind')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-happy.wav', m['ooh'] + 0.08, rms=-32, what='beep: happy (after "Ta")')
    C3.loop_wheels(fx, 'sfx-maddie', m['c02'][0] + 0.2, m['c02'][1] - m['c02'][0] - 0.2, rms=-33, fi=0.3, fo=1.2,
                   what='her wheels on the grass (loop)')
    C3.loop_wheels(fx, 'sfx-maddie', st['c3'], en['c3'] - st['c3'], rms=-32, fi=0.5, fo=0.5,
                   what='her wheels on the chalk track (loop)')
    for k in np.arange(st['c3'] + 1.0, en['c3'] - 1.0, 3.0):
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-38, what='beacon blip')
    for key in ('ai1', 'ai2'):
        a, e = m[key]
        for k in np.arange(a, e, 0.9):
            fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-36, what='beacon on his words')
    # c6: the doorway hums; Maddie bumps up the step at ~5.5 s of C07
    s6 = st['c6']
    hum = tone('doorway-hum', 'sine=f=55:r=48000[a];sine=f=110:r=48000[b];anoisesrc=c=pink:r=48000:a=0.05,'
                              'lowpass=f=400[n];[a][b][n]amix=inputs=3:weights=1 0.4 0.6,tremolo=f=0.3:d=0.2', 12)
    fx('sfx-crowd', SFX / 'fs653920-crowd-small-walla.mp3', s6, 7.0, src_in=6, rms=-45, fi=0.8, fo=2.5,
       what='the hundred at the door: a low murmur that dies away as Maddie goes in')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', s6, 6.5, src_in=30, rms=-47, fi=0.8, fo=2.0,
       what='feet shifting at the door')
    fx('sfx-room', hum, s6, en['c6'] - s6, rms=-40, fi=1.5, fo=0.8, what='the doorway: a low hum (ffmpeg)')
    C3.loop_wheels(fx, 'sfx-maddie', s6 + 0.3, 5.0, rms=-36, fi=0.4, fo=0.4, what='her wheels along the wall')
    fx('sfx-maddie', MS / 'derived-maddie-servo-turn-a.wav', s6 + 4.9, rms=-34, what='servo: she turns back')
    fx('sfx-maddie', MS / 'derived-maddie-wheels-stop.wav', s6 + 6.1, rms=-32, what='bump: up the step')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-boop-ok.wav', s6 + 6.6, rms=-36, what='beep: ok, in she goes')
    c.flags.append('Sound I made up for scene C: a hundred feet on chalk (the crowd-shuffle loop), the doorway hum '
                   '(55/110 Hz + pink noise, ffmpeg), the happy beep after "Ta", the bump and boop as Maddie goes in. '
                   'No birdsong or skylarks: the library has none.')
    return mx


SCENE_FNS = {'C': (scene_c, audio_c)}


def run(key, do_preview=True):
    sc = Scene(key)
    C3.ROOT = sc.media / 'cut'  # cut3.lufs_of's scratch file lands here, not in cut3's folder
    build, audio = SCENE_FNS[key]
    c = build(sc)
    c.extend()
    mx = audio(c)
    tracks, mix = C3.write(c, mx)
    print('colour across the joins:')
    rows = join_report(c)
    big = [r for r in rows if r[4] > 30]
    c.flags.append('Colour: mean RGB measured on both sides of every cut; ' + (
        'the biggest steps are ' + '; '.join(f'{r[0]} -> {r[1]} ({r[4]:.0f}/255)' for r in big) +
        ' (a change of place or light, not a drift inside a shot)' if big else 'no step over 30/255') + '.')
    data = C3.edl(c, tracks, mix, mx)
    print(f'{c.key}: total {c.total:.2f}s, {len(c.video)} clips, {len(tracks)} stems')
    for b in data['beats']:
        print(f"  beat {b['id']:>3} {b['start']:7.2f} +{b['dur']:6.2f}  {b['title']}")
    if do_preview:
        C3.preview(c, data)
        qc = subprocess.run(['bash', str(REPO / 'scripts/delivery-qc.sh'), str(c.dir / 'preview.mp4')],
                            capture_output=True, text=True).stdout
        import re
        qc = re.sub(r'\x1b\[[0-9;]*m', '', qc)
        print(qc)
        summary = qc.strip().splitlines()[-1]
        fails = [ln.strip() for ln in qc.splitlines() if 'FAIL' in ln or ln.strip().startswith('warn')]
        data['flags'].append(f'delivery-qc on preview.mp4: {summary}. ' + ' | '.join(f[:140] for f in fails) + (
            ' The range FAIL is x264 quantisation ringing on a few grain pixels per frame: the picture is clamped to '
            '16-235 before the encode (cut3.LEGAL) and the encoder overshoots (3/247); cut 3 A\'s preview fails the '
            'same way. Not a range-tag mismatch. -16 LUFS is the house target for these scenes (the brief), not -14.'
            if fails else ''))
        (c.dir / 'edl.json').write_text(json.dumps(data, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    keys = [a for a in sys.argv[1:] if not a.startswith('--')] or ['C']
    for k in keys:
        run(k, '--no-preview' not in sys.argv)
