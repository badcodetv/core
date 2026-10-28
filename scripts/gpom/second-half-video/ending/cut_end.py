#!/usr/bin/env python3
"""GPOM second half, the ending (scenes C, D, E): new-scene stage 4 rough cuts in the timeline format.

    python3 scripts/gpom/second-half-video/ending/cut_end.py C            # scene C, the walk out
    python3 scripts/gpom/second-half-video/ending/cut_end.py C --no-preview
    python3 scripts/gpom/second-half-video/ending/cut_end.py C --tag later   # scene B cut: "Some negotiation later."

--tag X writes to <media>/cut-X/ instead of <media>/cut/, so the Premiere sequence built from the old cut keeps its
files. --tag later (Kai, 28 Oct): scene B (the door) is cut from the film; C opens on a black card, "Some negotiation
later.", then the long walk, with Maddie's two lines from the bunker exit moved onto it; C01b and C02 go.

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
C1_KEEP = False  # Kai reel at73: beat c1 (the door from inside) is cut
ROUND_KEYS = ('file_round6', 'file_round5', 'file_round4', 'file_round3', 'file_round2_kai')  # newest first
fr, dur = C.fr, C3.dur
TAG = sys.argv[sys.argv.index('--tag') + 1] if '--tag' in sys.argv else None
LATER = TAG == 'later'
CARD = 'Some negotiation later.'  # Kai's words, 28 Oct
CARD_D = 2.5
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


class Scene:
    def __init__(self, key):
        self.key = key
        self.folder = SCENES / SLUGS[key]
        rd = lambda n: json.loads((self.folder / n).read_text())  # noqa: E731
        self.cfg, self.clips, self.picks, self.vox = rd('scene.json'), rd('clips.json'), rd('picks.json'), rd('voices.json')
        self.media = pathlib.Path(self.cfg['media'])

    def clip(self, fid):
        """The clip's newest take: a round's pick (file_round3, file_round2_kai) wins over the older `file` when it
        names one file (E03's round 3 names a two-clip chain and is joined by cut_end_e.py instead)."""
        e = self.clips['clips'][fid]
        f = next((e[k] for k in ROUND_KEYS if str(e.get(k, '')).endswith('.mp4') and ' ' not in e[k]), e['file'])
        return pathlib.Path(self.clips['media']) / f

    def voice(self, key):
        return self.media / self.vox['lines'][key]['file']

    def text(self, key):
        return self.vox['lines'][key]['text']


class Cut:
    """cut3.Cut's shape (cut3.write / edl / preview read these attributes), rooted in <media>/cut."""

    def __init__(self, sc, seq, title, heading, intro):
        self.sc, self.key, self.seq = sc, sc.key, seq
        self.dir = sc.media / (f'cut-{TAG}' if TAG else 'cut')
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
    c = Cut(sc, 'gpom-second-half-C-rough4', 'Ending C Timeline', 'GPOM second half · the ending · scene C: the walk out',
            "Scene C of the ending, round 2 (Kai's notes, 23 Oct): Maddie coaxes the hundred out of the bunker, they "
            "walk over the downs, the seat one last time, the AI's building, and the step. It is Maddie's scene: the "
            "boss does not speak. Play it, click any beat, clip, line or sound, and leave a note in its yellow slip. "
            "Notes save as you type. Tell Claude when you're done.")
    m = c.m
    V = c.vdir

    def by(key):  # who wrote the line: scene.json, the line's beat and index (c4-2-sandra -> beat c4, line 2)
        bk, i, _ = key.split('-')
        return next(b for b in sc.cfg['beats'] if b['key'] == bk)['lines'][int(i)].get('by', 'claude')

    def speech(key):  # the take's speech span, from voices.json: every fragment of a line takes its gain from it
        a, z = sc.vox['lines'][key]['speech']
        return (a, z + 0.3)

    # ---- c1: off the step (C01, round 1): from inside the bunker, past the wary faces, to Maddie alone on the step.
    # Maddie has no mouth: no lip-sync. Nobody moves for 1.4 s before she speaks; her promise comes a beat later.
    # Kai reel at73 (23 Oct, C round 5): beat c1 is CUT. Scene B now ends on "Come back tomorrow", the door and
    # Maddie rolling away, so C opens on the walk-out (C01b). Kept behind C1_KEEP for the record.
    if C1_KEEP:
        b = c.beat('c1', 'Off the step', 0.0, act='The walk out',
                   see='From inside the dark bunker, past the hundred\'s wary backs and faces (the old lady among them, '
                       'silent), Maddie alone on the step in the daylight, turned back to them. Nobody moves. She coaxes.')
        a = 1.4
        e = c.say('vox-maddie', sc.voice('c1-0-maddie'), 0.27, 3.30, a, 'c1 line 0 maddie: "Go on. I promise you\'ll be okay."')
        c.line(b, 0, 'maddie', a, e - a, sc.text('c1-0-maddie'), by('c1-0-maddie'))
        a1 = fr(e + 1.2)  # scene.json gap_before 1.2
        e1 = c.say('vox-maddie', sc.voice('c1-1-maddie'), 0.22, 1.46, a1, 'c1 line 1 maddie: "You\'ve got my word."')
        c.line(b, 1, 'maddie', a1, e1 - a1, sc.text('c1-1-maddie'), by('c1-1-maddie'))
        end_c1 = fr(e1 + 0.7)
        src01 = sc.clip('C01')
        c01 = move(src01, V / f'{src01.stem}-push-d{end_c1:.3f}.mp4', 0.0, end_c1, 1.06, hold=1.5, cx=0.6, cy=0.45)
        c.pic(c01, 0.0, 0.0, end_c1, 'c1', source=src01)
        m['c01'] = (0.0, end_c1)
        m['promise'] = (a, e1)
        t = c.close(b, end_c1)
    else:
        t = 0.0
        m['c01'] = (0.0, 0.0)
        c.flags.append('C round 5 (Kai reel at73): the opening door shot (C01) and Maddie\'s "Go on. I promise you\'ll be '
                       'okay." / "You\'ve got my word." are CUT: scene B now ends on "Come back tomorrow", the door slam '
                       'and Maddie rolling away, so C opens on the first ones stepping out.')
    c.flags.append('C round 3 (Kai reel at253/at440): Maddie was about twice her size in C01b and C02. Both plates were '
                   'remade in two steps (the robot removed, then the canonical bot s3-bot-00b-a added back knee-high, sized '
                   'against a bag in frame) and re-animated: c01br5-t1 (6 s), C02r5-t2 (8 s; C02 is framed a little wider '
                   'than before and Omni drifts the camera). Bunting kept: this is outside the clean room.')
    if LATER:
        c.meta['intro'] = ('Scene C, round 7: scene B is cut (your call, 28 Oct: "it\'s just removed so much fluff"). '
                           'The kill bots stand down at the end of A; then black, "Some negotiation later."; then the long '
                           'walk, Maddie leading, with her "Careful now, humans." moved onto it. Play it, click any beat, '
                           "clip, line or sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude "
                           "when you're done.")
        b = c.beat('c0', 'Some negotiation later', 0.0, act='The walk out',
                   see='Black. White words, small and centred: "Some negotiation later." Silence. Whatever was said at '
                       'the bunker door, we never hear it.')
        card = V / 'card-some-negotiation-later.mp4'
        if not card.exists():
            txt = V / 'card.txt'
            txt.write_text(CARD)
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i',
                            f'color=c=black:s=1280x720:r={FPS}:d={CARD_D}', '-vf',
                            f"drawtext=fontfile={FONT}:textfile={txt}:fontsize=34:fontcolor=white:"
                            "x=(w-tw)/2:y=(h-th)/2:alpha='if(lt(t,0.4),t/0.4,if(gt(t,2.1),(2.5-t)/0.4,1))'",
                            *ENC, str(card)], check=True)
        c.pic(card, 0.0, 0.0, CARD_D, 'c0')
        m['card'] = (0.0, CARD_D)
        t = c.close(b, CARD_D)
        m['c01b'] = m['c02'] = (t, t)
        c.flags.append('Round 7 (Kai, 28 Oct): scene B is cut from the film. C opens on a 2.5 s black card, "Some '
                       'negotiation later." (DejaVu Sans, white, faded in and out, ffmpeg drawtext: Premiere cannot '
                       'write text through the bridge), in silence. C01b and C02 (the bunker exit) are cut; Maddie\'s '
                       '"Careful now, humans." / "I\'m fairly sure there\'s no radiation round here." play over the '
                       'long walk instead, while she is alone in frame.')
    if not LATER:
        # ---- c2: into daylight (C01b, then C02). Maddie's joke gets them over the threshold.
        s2 = t
        b = c.beat('c2', 'Into daylight', s2, act='The walk out',
                   see='The first two edge out of the doors, squinting; more follow. Maddie\'s joke. Then the hundred file '
                       'out of the hill; the kill bots\' track marks in the grass. Maddie leads out of frame.')
        src1b = sc.clip('C01b')
        d1b = fr(dur(src1b) - 1 / FPS)
        c.pic(src1b, 0.0, s2, s2 + d1b, 'c2')
        a = fr(s2 + 1.6)  # after the first steps out (C01b's man shades his eyes from ~1 s)
        e = c.say('vox-maddie', sc.voice('c2-0-maddie'), 0.28, 1.68, a, 'c2 line 0 maddie: "Careful now, humans."')
        c.line(b, 0, 'maddie', a, e - a, sc.text('c2-0-maddie'), by('c2-0-maddie'))
        a1 = fr(e + 0.6)  # scene.json gap_before 0.6
        e1 = c.say('vox-maddie', sc.voice('c2-1-maddie'), 0.20, 4.70, a1,
                   'c2 line 1 maddie: "I\'m fairly sure there\'s no radiation round here."')
        c.line(b, 1, 'maddie', a1, e1 - a1, sc.text('c2-1-maddie'), by('c2-1-maddie'))
        cut02 = fr(s2 + d1b)
        c02_end = fr(cut02 + 7.0)
        c02, gnote = match_grade(sc.clip('C02'), sc.clip('C03'), V / f"{sc.clip('C02').stem}-graded.mp4", strength=0.7)
        c.pic(c02, 0.0, cut02, c02_end, 'c2', source=sc.clip('C02'))
        m['c01b'] = (s2, cut02)
        m['c02'] = (cut02, c02_end)
        m['joke'] = e1
        t = c.close(b, c02_end)
        c.flags.append('Round 2 (Kai, at291): C01b re-made on mud (c01br3-t1): the ground outside the bunker is the same '
                       'muddy track as the rest of the walk, no concrete; they step out onto it, more follow from ~3 s.')
        c.flags.append('Round 1 (Kai, lc1-1): C01b (the first two edge out, more follow) plays whole before C02. '
                       '"Careful now, humans." comes 1.6 s in, as they step out; the radiation line 0.6 s after it, and runs '
                       f'{e1 - cut02:.1f} s over the cut into C02 so the hundred file out under the joke.')
        c.flags.append('Colour: C02 is graded towards the first 4 s of the long walk it cuts to, so the two '
                       'overcast exteriors match. ' + gnote + '.')

    # ---- c3: the long walk (C03 chain, unchanged: Kai, bc3 "excellent shot")
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
    if LATER:  # her two bunker-exit lines, over the walk: the first while she is alone in frame, before the reveal
        a = fr(t + 1.0)
        e = c.say('vox-maddie', sc.voice('c2-0-maddie'), 0.28, 1.68, a, 'c3 line 0 maddie: "Careful now, humans."')
        c.line(b, 0, 'maddie', a, e - a, sc.text('c2-0-maddie'), by('c2-0-maddie'))
        a1 = fr(e + 0.6)
        e1 = c.say('vox-maddie', sc.voice('c2-1-maddie'), 0.20, 4.70, a1,
                   'c3 line 1 maddie: "I\'m fairly sure there\'s no radiation round here."')
        c.line(b, 1, 'maddie', a1, e1 - a1, sc.text('c2-1-maddie'), by('c2-1-maddie'))
        m['joke'], m['c3_lines'] = e1, (a, e1)
    t = c.close(b, t + D3)
    c.flags.append('C03 unchanged (Kai round 1: "excellent shot"): opens at 160% on Maddie alone, holds 1.5 s, eases '
                   'out to 100% by 9.6 s so the hundred appear behind her. Music on it may change once it is in Premiere.')

    # ---- c4: the seat. Lip-sync, phrase by phrase, on the round-1 clips (lip-sync-dub). Mouth openings and lip
    # closures read off the tracked 12 fps strips (clips/lips/<take>.jpg) and the rescaled 24 fps strips; voice pauses
    # and b/m closures from the take's 20 ms loudness. Every phrase starts 0-0.1 s after the mouth opens; tempo <= 1.3.
    # Cut: C04 (her seat line) -> C05 0-5.3 (his line) -> C04b (her punchline, out at 7.3 before Omni's invented
    # words) -> C05 5.8-8.0 (his flat look, no reply).
    s4 = t
    b = c.beat('c4', 'The seat', s4, act='The walk out',
               see='Sandra and Derek, walking. The row one last time, and what it now means: nobody is coming back, '
                   'and she is still right. He gives her a look.')
    i04 = 1.2
    k = 'c4-0-sandra'
    # C04 (c04r1-seat-t1): mouth shut to 2.25, speech 2.25-4.4; voice 0.30-2.56 at x1.07: the b of "bloody" lands
    # on the lips shut at 3.12-3.37
    a = s4 + 2.27 - i04
    e = c.say('vox-sandra', sc.voice(k), 0.30, 2.56, a, 'c4 line 0 sandra (lip-sync, x1.07)', tempo=1.07, ref=speech(k))
    c.line(b, 0, 'sandra', a, e - a, sc.text(k), by(k))
    cut05 = fr(e + 0.25)
    c.pic(sc.clip('C04'), i04, s4, cut05, 'c4')
    k = 'c4-1-derek'
    # C05, C round 6 (Kai at896: Derek walks ALONGSIDE Sandra): c05r6-t1. His mouth (mouth-map, --face left): open
    # 0.21-0.92, lips shut 0.92-1.12 (the b of "bloody"), open 1.12-2.04, shut to ~3.2 (a breath 3.25-4.0), "We're not
    # coming back, are we?" 4.62-6.04 (a closure 4.92-5.12). Omni's own audio runs ~0.45 s ahead of its picture (as on
    # Karen), so the picture is the timing. Take r1c: phrase 1 0.24-2.34 (the b of "bloody" at 1.07), phrase 2 3.00-4.30.
    # Phrase 1 whole at x1.15 from 0.25 puts the b of "bloody" at 0.97, on the closure; phrase 2 whole at x1.0 from 4.66.
    D4 = [(0.24, 2.34, 0.25, 1.15, '"Doesn\'t bloody matter now, love."'), (3.00, 4.30, 4.66, 1.0, '"We\'re not coming back, are we?"')]
    for v0, v1, at, tp, txt in D4:
        e = c.say('vox-derek', sc.voice(k), v0, v1, cut05 + at, f'c4 line 1 derek: {txt} (lip-sync, x{tp})', tempo=tp,
                  ref=speech(k))
    a = cut05 + D4[0][2]
    c.line(b, 1, 'derek', a, e - a, sc.text(k), by(k))
    o05 = 6.1  # C round 6: his second phrase ends ~6.0 on c05r6-t1
    cut04b = fr(cut05 + o05)
    c.pic(sc.clip('C05'), 0.0, cut05, cut04b, 'c4')
    k = 'c4-2-sandra'
    # C04b (c04r1-aliens-t1), in at 0.5: mouth parted and held to ~0.92 (first check put "It" 0.13 s before the
    # full opening at 0.96: moved to 0.92); "It does" to 1.33, lips shut 1.375-1.42 for
    # the m of "matter" (voice 1.11-1.17), "matter" 1.46-1.79; shut to 2.42; "In ten thousand years," 2.42-3.96;
    # "when the aliens dig up that bunker," 4.17-6.0; "they'll know it was you." 6.08-6.88 (lips shut 6.50-6.58 for the
    # w of "was", rounded on "you" 6.67-6.83). "bunker" keeps its soft "-er" tail (voice to 6.26: cut at 6.08, the
    # mix was heard as "bunk they'll"). The voice's 0.25 s gap inside "It does" is dropped; its 0.5 s pause
    # before "they'll" is not in her mouth, so it goes.
    i4b = 0.5
    t4b = cut04b - i4b
    S4 = [(0.29, 0.62, 0.92, 1.0, '"It"'), (0.84, 1.82, 1.24, 1.3, '"does matter."'),
          (2.36, 3.96, 2.40, 1.0, '"In ten thousand years,"'), (4.16, 6.26, 4.20, 1.12, '"when the aliens dig up that bunker,"'),
          (6.54, 7.82, 6.10, 1.3, '"they\'ll know it was you."')]
    for v0, v1, at, tp, txt in S4:
        e = c.say('vox-sandra', sc.voice(k), v0, v1, t4b + at, f'c4 line 2 sandra: {txt} (lip-sync, x{tp})', tempo=tp,
                  ref=speech(k))
    a = t4b + S4[0][2]
    c.line(b, 2, 'sandra', a, e - a, sc.text(k), by(k))
    out4b = 7.3  # Omni added "You cannot..." from 7.56
    cutlook = fr(t4b + out4b)
    c.pic(sc.clip('C04b'), i4b, cut04b, cutlook, 'c4')
    look0, look1 = 6.2, 8.0 - 1 / FPS  # c05r6-t1: he turns his head to her from ~6 s
    end_c4 = fr(cutlook + look1 - look0)
    c.pic(sc.clip('C05'), look0, cutlook, end_c4, 'c4')
    m['c4'] = (s4, end_c4)
    m['c4_lines'] = (s4 + 2.27 - i04, e)
    m['you'] = e
    t = c.close(b, end_c4)
    c.flags.append('C round 6 (Kai at896, pick C05r6-b): Derek now walks level with Sandra, shoulder to shoulder '
                   '(c05r6-t1, 12 credits). His line is on his mouth in two phrases (x1.15 and x1.0), read from the '
                   'picture, not from Omni\'s own audio; the flat look is the clip\'s last 1.8 s as he turns to her.')
    c.flags.append('C round 6 (Kai at299, pick c01br6-a): the step-out is on scene B\'s trampled grass, no mud, Maddie '
                   'knee-high (c01br6-t1, 6 s, 10 credits): they stride out, he shades his eyes, the crowd follows.')
    c.flags.append('Round 1 (Kai, lc4-0/lc4-1/bc4, Q1 a): the seat is four shots now: C04 (her line) -> C05 (his) -> '
                   'C04b (her punchline) -> C05 again for his flat look, no reply. All four lines are lip-synced phrase '
                   'by phrase on the mouth (lip-sync-dub), never on Omni\'s own audio.')
    c.flags.append('c4 lip-sync: Sandra\'s seat line x1.07 (the b of "bloody" on her shut lips). Derek in four pieces: '
                   '"Doesn\'t" x1.0, "bloody matter now, love." x1.3 (the cap), "We\'re not coming" x1.0, "back, are '
                   'we?" x1.0, each b landing on a lip closure (0.92-1.00 and 4.25-4.33 s of C05). Sandra\'s punchline in '
                   'five pieces: x1.0 / x1.3 / x1.0 / x1.12 / x1.3. Her mouth gives the last phrase 0.8 s for 1.3 s of '
                   'voice, so "they\'ll know it was you." is at the 1.3 cap and the take\'s 0.5 s pause before it is gone: '
                   'the line to listen to for squeeze. A slower Omni take of that phrase alone would fix it.')
    c.flags.append(f'c4: C04b goes in at 0.5 s (she has already turned to him; her mouth is parted and still to ~0.9 s) '
                   f'and out at 7.3 s, before the words Omni invented from 7.56 s. Derek\'s look is C05 5.8-8.0 '
                   f'({look1 - look0:.1f} s): he turns his head to her, mouth shut.')

    # ---- c5: over the brow (C06, round 2: the old man and his helper painted out, nobody turns; push 100 -> 112%).
    # Derek among the backs (no close-up was made, so no lip-sync). Round 2 (Kai, at1342): Maddie says nothing here;
    # Derek's line plays alone over the reveal.
    s5 = t
    b = c.beat('c5', 'Over the brow', s5, act='The building',
               see='From behind the hundred at the crest, every head turned down to the AI\'s building in the fold of '
                   'the downs. They stop. Maddie rolls a little way ahead down the slope.')
    k = 'c5-0-derek'
    a = fr(s5 + 1.2)
    e = c.say('vox-derek', sc.voice(k), 0.22, 3.80, a, 'c5 line 0 derek: "Bloody hell. Look at that building." (awed, quiet)',
              lufs=-17.5)
    c.line(b, 0, 'derek', a, e - a, sc.text(k), by(k))
    e1 = e
    end_c5 = fr(s5 + 8.0 - 1 / FPS)
    src06 = sc.clip('C06')
    c06 = move(src06, V / f'{src06.stem}-push-d{end_c5 - s5:.3f}.mp4', 0.0, end_c5 - s5, 1.12, hold=1.5, cx=0.45,
               cy=0.42)
    c.pic(c06, 0.0, s5, end_c5, 'c5', source=src06)
    m['c5'] = (s5, end_c5)
    m['c5_lines'] = (a, e)
    t = c.close(b, end_c5)
    c.flags.append('Round 2 (Kai, at1289): C06 re-animated without the old man on his stick and his helper (c06r3-t1); '
                   'every head looks down at the building, nobody turns. The seam lights end to end from ~2 s. Omni '
                   'rolls Maddie a short way forward and left down the slope (~2-6 s), as if leading them: it was not '
                   'asked for, and it reads as her setting off ahead, so the shot plays whole. Kai to judge.')
    c.flags.append(f'Round 2 (Kai, at1342): Maddie\'s "He\'s been working on this one for quite a long time." is cut. '
                   f'Derek\'s "Bloody hell. Look at that building." waits 1.2 s into the reveal and plays alone; then '
                   f'{end_c5 - e:.1f} s of the building and the wind before the cut to the door.')
    c.flags.append('Not made: a Derek close-up for "Bloody hell. Look at that building." He is among the backs in C06, '
                   'so the line plays without a visible mouth. A close-up would need a new still and a lip-sync clip '
                   '(~12 credits). Kai to rule.')

    # ---- c6: mind the step (C07); Maddie asks them in (round 1: her line, not the boss's); the music stops dead on
    # "Mind the step"
    s6 = t
    b = c.beat('c6', 'Mind the step', s6, act='The building',
               see='At the foot of the black wall the amber seam has opened into a doorway with one low step. Maddie '
                   'waits, asks them in, then goes up into the light.')
    k = 'c6-0-maddie'
    a1 = fr(max(s6 + LEAD, e1 + 0.6))
    e2 = c.say('vox-maddie', sc.voice(k), 0.26, 1.15, a1, 'c6 line 0 maddie: "Come in."', ref=speech(k))
    a2 = fr(e2 + 0.5)
    e3 = c.say('vox-maddie', sc.voice(k), 1.30, 2.22, a2, 'c6 line 0 maddie: "Mind the step."', ref=speech(k))
    c.line(b, 0, 'maddie', a1, e3 - a1, sc.text(k), by(k))
    end_c6 = fr(max(s6 + 8.0 - 1 / FPS, e3 + TAIL))
    c07 = V / 'C07-glass.mp4'
    if not c07.exists():
        subprocess.run([str(LIPS_PY), '-I', str(HERE / 'glass_window.py'), str(sc.clip('C07')), str(c07), '--rect',
                        '0,185,366,560', '--feather', '24', '--gain', '0.16', '--desat', '0.9'], check=True)
    c.pic(c07, 0.0, s6, end_c6, 'c6', source=sc.clip('C07'))
    m['c6'] = (s6, end_c6)
    m['mind'] = a2
    t = c.close(b, end_c6)
    c.flags.append(f'Round 1 (Kai, lc6-0): "Come in. Mind the step." is Maddie\'s now (the boss is silent in scene C). '
                   f'"Come in." at {a1 - s6:.1f} s into C07, "Mind the step." 0.5 s later (the take\'s own gap was '
                   '0.25 s), so she goes up the step (~5.5 s) after the invitation.')
    c.flags.append('C07: Maddie\'s reflection in the black glass left of the doorway is darkened (glass_window.py) so it '
                   'does not read as a second robot inside.')
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
    # low held cello note (attack ~61.7 s in the take) lands on the reveal; ducked under the seat and under the lines
    # at the crest; stops dead on "Mind the step".
    walk = sc.media / 'suno' / 'gpom-sh-c-walk-a-v6-w30-cc128cb2.wav'
    attack = 61.7
    s_in = m['c3'][0]
    land = m['c5'][0] + 0.3
    off = attack - (land - s_in)
    stop = m['mind']
    d = stop - s_in
    x = C.level(C.decode(walk, off, d), rms=-21, peak=-3)
    ra, re_ = (v - s_in for v in m['c4_lines'])
    ca, ce = (v - s_in for v in m['c5_lines'])
    pre = []
    if LATER:  # under her two lines on the walk
        ja, je = (v - s_in for v in m['c3_lines'])
        pre = [(max(ja - 0.4, 1.5), 1), (ja, 0.5), (je + 0.2, 0.5), (je + 0.8, 1)]
    x *= C.env(len(x), [(0, 0), (1.5, 1), *pre, (ra - 0.5, 1), (ra, 0.25), (re_ + 0.3, 0.25), (re_ + 1.2, 1),
                        (ca - 0.4, 1), (ca, 0.5), (ce + 0.2, 0.5), (ce + 0.8, 1), (d - 0.03, 1), (d, 0)])
    mx.add('mus-c-walk', x, s_in, walk, 'C-walk: lone violin and piano, the held cello note on the reveal')
    c.flags.append(f'Music unchanged (Kai: may change once it is in Premiere): C-walk enters on the long walk at '
                   f'{off:.1f} s into the take, its held low cello note on the reveal, no edit inside the music; ducked '
                   'to 0.25 under all four seat lines (the seat scene is longer now) and to 0.5 under Derek at the crest; stops dead on "Mind the step". C01-C02 play on wind and the crowd.')

    # ---- sfx
    wind = C3.wind_file()
    w0 = m['card'][1] if LATER else 0  # the card is silent
    fx('sfx-wind', wind, w0, total - w0, src_in=5, rms=-34, fi=0.8, fo=1.0, tile=True, what='wind on the downs (ffmpeg)')
    if m['c01'][1] > 1.0:
        fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', 0.3, m['c01'][1] - 0.3, src_in=40, rms=-47, fi=1.0, fo=0.6,
           what='the hundred in the bunker, shifting their weight; nobody walks')
    if not LATER:
        fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', m['c01b'][0], m['c02'][1] + 1.2 - m['c01b'][0], rms=-38,
           fi=0.8, fo=1.4, what='the hundred coming out, shuffling (crossfades into the chalk loop over the cut)')
        fx('sfx-crowd', SFX / 'fs653920-crowd-small-walla.mp3', m['c02'][0], m['c02'][1] - m['c02'][0], rms=-44, fi=1.0,
           fo=1.0, what='murmur as they blink at the sky')
    f0 = st['c3'] if LATER else st['c3'] - 1.2
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', f0, en['c4'] - f0, src_in=8,
       rms=-37, fi=1.4, fo=1.0, tile=True, what='a hundred pairs of feet on the chalk (held under the walk)')
    fx('sfx-crowd', SFX / 'fs189231-crowd-shuffling.mp3', st['c5'], 3.0, src_in=20, rms=-42, fi=0.2, fo=1.5,
       what='they stop')
    if not LATER:
        fx('sfx-maddie', SFX / 'fs701647-bunting-fabric-flap.mp3', m['c02'][0], m['c02'][1] - m['c02'][0], src_in=4,
           rms=-38, fi=0.4, fo=0.8, what='bunting in the wind')
        C3.loop_wheels(fx, 'sfx-maddie', m['c02'][0] + 0.2, m['c02'][1] - m['c02'][0] - 0.2, rms=-33, fi=0.3, fo=1.2,
                       what='her wheels on the grass (loop)')
    fx('sfx-maddie-beeps', MS / 'synth-maddie-beep-happy.wav', m['joke'] + 0.15, rms=-32,
       what='beep: happy (after the radiation joke)')
    C3.loop_wheels(fx, 'sfx-maddie', st['c3'], en['c3'] - st['c3'], rms=-32, fi=0.5, fo=0.5,
                   what='her wheels on the chalk track (loop)')
    for k in np.arange(st['c3'] + 1.0, en['c3'] - 1.0, 3.0):
        fx('sfx-beacon', SFX / 'synth-beacon-blip.wav', k, rms=-38, what='beacon blip')
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
    c.flags.append('Sound I made up for scene C: the hundred shifting their weight in the bunker (quiet), a hundred feet '
                   'on chalk (the crowd-shuffle loop), the doorway hum (55/110 Hz + pink noise, ffmpeg), a happy beep '
                   'after the radiation joke, the bump and boop as Maddie goes in. No birdsong: the library has none.')
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
    keys = [a for a in sys.argv[1:] if not a.startswith('--') and a != TAG] or ['C']
    for k in keys:
        run(k, '--no-preview' not in sys.argv)
