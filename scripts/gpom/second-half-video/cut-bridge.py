#!/usr/bin/env python3
"""Rough cut of the GPOM bridge (scene B revived, draft 1G, 3 Nov): ffmpeg only, no Premiere.

    python3 scripts/gpom/second-half-video/cut-bridge.py

Picture: the five bridge clips (shb-br1..5, the storyboard's recommended options) plus stand-ins from the
old door scene for the shots the storyboard did not cover (the tannoy exchange and the debate). The film on
the TV = br1 under hud.py's red KILL MODE + scene A's hud-12 (the brake and the flip to NEW OBJECTIVE:
SUSTAIN ORGANIC LIFE), composited onto the TV in br2 and shown full frame between. The one camera move (2B)
is a slow push across the room shots towards the TV (zoompan here; Premiere does it for real).
Sound: voices from scenes/second-half-b-the-door/voices-bridge.json, timed to their real lengths (never
slowed); Maddie dry outside, through the tannoy inside; the old lady's second shout muffled through the door.
Effects from GPOM's licensed sfx folder (audio/sfx/index.json).

Writes <media>/cut3/B-bridge/{edl.json, stems/, mix.wav, preview.mp4} in the timeline format
(scripts/scene/timeline.py).
"""
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
SCENE = REPO / 'docs/stories/gitpush-origin-master/scenes/second-half-b-the-door'
M = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half')
VID, SFX, VOX = M / 'video', M / 'audio/sfx', M / 'audio/voice3'
OUT = M / 'cut3/B-bridge'
V, ST = OUT / 'video', OUT / 'stems'
FPS, SR, W, H = 24, 48000, 1280, 720
ENC = ['-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
       '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
TV = (778, 449, 95, 77)          # the screen in br2 (x, y, w, h), measured off the clip
PUSH = (825, 488, 0.10)          # push towards the TV: centre x, y and how far (100 -> 110%)
FLIP = 7.0                       # film time of the flip to green (3.5 s of br1 + hud-12's flip at 3.5)


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                 str(p)], capture_output=True, text=True).stdout)


TARGET = {'dry': -20.0, 'tannoy': -21.0, 'muffled': -31.0}   # integrated loudness per line, LUFS


def lufs(p):
    err = subprocess.run(['ffmpeg', '-nostats', '-i', str(p), '-af', 'ebur128', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    return float(err.rsplit('I:', 1)[1].split('LUFS')[0])


# ---- voices -----------------------------------------------------------------------------------------
vb = json.loads((SCENE / 'voices-bridge.json').read_text())
script = json.loads((SCENE / 'script.json').read_text())
NAME = {'bot': 'Maddie', 'lady': 'The old lady', 'woman': 'Sandra', 'man': 'Derek'}


def take(i, p, fx=False):
    row = next(r for r in vb['lines'] if r['i'] == i)
    ph = row['phrases'][p]
    f = VOX / next(t['file'] for t in ph['takes'] if t['take'] == ph['pick'])
    if fx:
        f = f.with_name(f.stem + '-fx.wav')
        assert f.exists(), f
    return f, row


# ---- the film -----------------------------------------------------------------------------------------
def film():
    out = V / 'film.mp4'
    if out.exists():
        return out
    a = V / 'film-a-kill.mp4'
    if not a.exists():
        ff('-i', VID / 'shb-br1-1A-wa-05.mp4', '-t', 3.5, '-an', '-c:v', 'libx264', '-crf', 16, '-pix_fmt', 'yuv420p',
           V / 'br1-trim.mp4')
        subprocess.run([sys.executable, str(REPO / 'scripts/gpom/second-half-video/hud.py'), str(V / 'br1-trim.mp4'),
                        str(a), '--state', 'kill', '--lock', '0', '--audio', str(M / 'cut3/A-d6/hud/hud-12-meter.wav'),
                        '--no-audio-out'], check=True)
    b = M / 'cut3/A-d6/video/hud-12.mp4'
    # the two halves, then a CRT pass (grain, soft scanlines, vignette) and the last frame held 8 s for the TV
    ff('-i', a, '-i', b, '-filter_complex',
       f'[0:v]scale={W}:{H},setsar=1,fps={FPS}[a];[1:v]scale={W}:{H},setsar=1,fps={FPS},trim=0:7,setpts=PTS-STARTPTS[b];'
       '[a][b]concat=n=2:v=1:a=0,noise=alls=10:allf=t,'
       "geq=lum='lum(X,Y)*(0.86+0.14*abs(sin(Y*1.6)))':cb='cb(X,Y)':cr='cr(X,Y)',vignette=PI/4.5,"
       'tpad=stop_mode=clone:stop_duration=8[v]', '-map', '[v]', '-an', *ENC, out)
    return out


# ---- shots --------------------------------------------------------------------------------------------
def seg(name, src, t_in, d, *, push=None, tv=None, swap_tv=None, pingpong=None, tv_off=False, film_src=None,
        punch=None):
    """One shot, 1280x720/24, d seconds from t_in. push=(z0, z1): the room push as zoom at start/end.
    tv=(film_t0, static_until): composite the film on the TV, film time film_t0 at the shot's start;
    static before static_until (shot time). swap_tv=box: red<->green swap inside a box (the TV in br3)."""
    out = V / f'{name}.mp4'
    if out.exists():
        return out
    if pingpong:  # forward then back over [t_in, t_in + pingpong], for a near-still base under a push
        chain = (f'[0:v]trim={t_in}:{t_in + pingpong},setpts=PTS-STARTPTS,scale={W}:{H},setsar=1,fps={FPS},split[f][r];'
                 f'[r]reverse[rv];[f][rv]concat=n=2:v=1:a=0,loop=-1:size={int(2 * pingpong * FPS)},trim=0:{d},'
                 'setpts=PTS-STARTPTS[base]')
    else:
        chain = (f'[0:v]trim={t_in}:{t_in + d},setpts=PTS-STARTPTS,scale={W}:{H},setsar=1,fps={FPS},'
                 f'tpad=stop_mode=clone:stop_duration={d},trim=0:{d}[base]')
    inputs = ['-i', src]
    last = 'base'
    if tv:
        f0, still = tv
        x, y, w, h = TV
        inputs += ['-ss', max(f0, 0), '-i', film_src or film(),
                   '-f', 'lavfi', '-i', f'nullsrc=s={w}x{h}:r={FPS}:d={d}']
        chain += (f";[1:v]scale={w}:{h},setsar=1,eq=brightness=0.06:saturation=1.3,gblur=sigma=0.6,"
                  f"setpts=PTS-STARTPTS+{max(-f0, 0)}/TB[film]"
                  f";[2:v]geq=lum='40+random(1)*50':cb=128:cr=128,format=yuv420p[stat]"
                  + ((f";[{last}]drawbox={x}:{y}:{w}:{h}:color=0x161616@1:t=fill[s1];[stat]nullsink" if ROUND3 >= 5
                      else f";[{last}]null[s1];[stat]nullsink") if tv_off else
                     f";[{last}][stat]overlay={x}:{y}:enable='lt(t,{still})'[s1]")
                  + f";[s1][film]overlay={x}:{y}:eof_action=repeat:enable='gte(t,{still})'[tvd]")
        last = 'tvd'
    if punch:
        chain += f";[{last}]scale={int(W * punch)}:{int(H * punch)},crop={W}:{H}[pu]"
        last = 'pu'
    if swap_tv:
        x, y, w, h = swap_tv
        chain += (f";[{last}]split[m][c];[c]crop={w}:{h}:{x}:{y},colorchannelmixer=rr=0.25:rg=0.6:gr=0.9:gg=0.2:bb=0.7"
                  f"[sw];[m][sw]overlay={x}:{y}[swd]")
        last = 'swd'
    if push:
        z0, z1 = push
        px, py, _ = PUSH
        n = int(round(d * FPS))
        z = f'({z0}+({z1}-{z0})*on/{max(n - 1, 1)})'
        chain += (f";[{last}]scale={W * 2}:{H * 2},zoompan=z='{z}':x='{px * 2}*(1-1/zoom)':y='{py * 2}*(1-1/zoom)'"
                  f":d=1:s={W}x{H}:fps={FPS}[pz]")
        last = 'pz'
    ff(*inputs, '-filter_complex', chain, '-map', f'[{last}]', '-t', d, '-an', *ENC, out)
    return out


def looped(name, src, t_in, d):
    """Forward then back to fill d (the page stripes it). Only for the stand-ins."""
    out = V / f'{name}.mp4'
    if out.exists():
        return out
    n = dur(src) - t_in
    ff('-i', src, '-filter_complex',
       f'[0:v]trim={t_in},setpts=PTS-STARTPTS,scale={W}:{H},setsar=1,fps={FPS},split[f][r];[r]reverse[rv];'
       f'[f][rv]concat=n=2:v=1:a=0,loop=-1:size={int(2 * n * FPS)},trim=0:{d},setpts=PTS-STARTPTS[v]',
       '-map', '[v]', '-an', *ENC, out)
    return out


def card(text, d):
    out = V / 'card-the-next-day.mp4'
    if not out.exists():
        txt = V / 'card.txt'
        txt.write_text(text)
        ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={d}', '-vf',
           f"drawtext=fontfile={FONT}:textfile={txt}:fontsize=34:fontcolor=white:x=(w-tw)/2:y=(h-th)/2:"
           f"alpha='if(lt(t,0.4),t/0.4,if(gt(t,{d - 0.4}),({d}-t)/0.4,1))'", *ENC, out)
    return out


# ---- the cut ------------------------------------------------------------------------------------------
class Cut:
    def __init__(self):
        self.t = 0.0
        self.video, self.events, self.beats, self.flags = [], [], [], []
        self.stems = {}

    def shot(self, f, d, beat, source, looped=False, t_in=0.0):
        self.video.append({'file': str(f), 'in': t_in, 'dur': round(d, 3), 'start': round(self.t, 3), 'beat': beat,
                           'source': str(source), 'looped': looped})
        self.t += d

    def sound(self, stem, f, at, what, gain=0.0, d=None, fade=0.0):
        d = d or dur(f)
        self.events.append({'stem': stem, 't': round(at, 3), 'dur': round(d, 3), 'what': what, 'src': str(f),
                            'gain': gain, 'fade': fade})
        return at + d

    def line(self, i, p, at, stem, fx=False, line=None):
        f, row = take(i, p, fx)
        d = dur(f)
        dry = dur(take(i, p)[0])             # the next line follows the words, not the tannoy's tail
        kind = row['fx'] if fx else 'dry'
        gain = round(TARGET[kind] - lufs(f), 1)
        self.events.append({'stem': stem, 't': round(at, 3), 'dur': round(d, 3), 'src': str(f), 'gain': gain,
                            'what': f"line {i}{f' p{p}' if len(row['phrases']) > 1 else ''}"
                                    f"{' (tannoy)' if fx and row['fx'] == 'tannoy' else ' (muffled)' if fx else ''}: "
                                    f"{row['phrases'][p]['text']}", 'fade': 0.0})
        if line is not None:
            line.setdefault('_parts', []).append((at, dry))
        return at + dry

    def beat(self, bid, title, start, see, lines=()):
        self.beats.append({'id': bid, 'title': title, 'start': round(start, 3), 'see': see, 'act': 'The bridge',
                           'lines': list(lines)})


def L(c, i):
    """A beat's line entry for the page (time filled in when its phrases are placed)."""
    sl = script['lines'][i]
    return {'i': i, 'who': sl['who'], 'name': NAME.get(sl['who'], sl['who']), 'text': sl['text'], 'by': sl['by']}


def main():
    V.mkdir(parents=True, exist_ok=True)
    ST.mkdir(parents=True, exist_ok=True)
    c = Cut()
    N3, V5 = VID / 'cut2-N3.mp4', VID / 'cut3-V5.mp4'
    V5P = M / 'cut3/B-br/video/cut3-V5-wait-push-i0-d6.000.mp4'
    LADY = VID / 'cut3-lip-17-0-muted.mp4'
    BR = {n: VID / f for n, f in {2: 'shb-br2-2B-BP1-e-b.mp4', 3: 'shb-br3-3A-BP1-e-b.mp4',
                                   4: 'shb-br4-4A-BP2-a-a.mp4', 5: 'shb-br5-5A-BP3-e-a.mp4'}.items()}
    lines = {i: L(c, i) for i in (0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 14, 15, 16)}

    # beat 1: the tannoy (inside: the crowd look up at the horn)
    b1 = c.t
    c.sound('sfx-tannoy', SFX / 'synth-tannoy-click.wav', b1 + 0.05, 'tannoy click on')
    c.sound('sfx-tannoy', SFX / 'fs530037-tannoy-pa-static.mp3', b1 + 0.05, 'tannoy static under her', gain=-20, d=6.6,
            fade=0.4)
    t = c.line(0, 0, b1 + 0.45, 'vox-maddie', fx=True, line=lines[0])
    t = c.line(1, 0, t + 0.12, 'vox-maddie', fx=True, line=lines[1])
    d1 = t + 0.4 - b1
    c.shot(seg('s01-N3', N3, 0.0, d1), d1, '1', N3)
    c.beat('1', 'The tannoy', b1, 'Inside: the hundred look up at the horn as her chirpy voice cuts in. Doors shut.',
           [lines[0], lines[1]])

    # beat 2: outside, Maddie at the shut door; the old lady inside shouts back
    b2 = c.t
    t = c.line(2, 0, b2 + 0.3, 'vox-maddie', line=lines[2])
    t = c.line(2, 1, t + 0.6, 'vox-maddie', line=lines[2])
    cut_lady = b2 + 8.0                       # V5 is 8 s; the end of her line lands on the old lady's face
    c.shot(seg('s02-V5', V5, 0.0, 8.0), 8.0, '2', V5)
    b3 = c.t
    t = c.line(3, 0, max(t + 0.7, cut_lady + 1.2), 'vox-lady', line=lines[3])
    d3 = t + 0.15 - cut_lady
    c.shot(seg('s03-lady', LADY, 0.0, d3), d3, '2', LADY)
    c.flags.append("Stand-in: the old lady's shout plays on her lip-sync clip from the old doorstep "
                   "(cut3-lip-17-0, made for another line), so her lips don't match \"Are you literally joking?\".")
    b4 = c.t
    t = c.line(4, 0, b4 + 0.05, 'vox-lady', fx=True, line=lines[4])
    t = c.line(5, 0, t + 0.5, 'vox-maddie', line=lines[5])
    d4 = t + 0.35 - b4                         # cut inside on "Yeah.": the rest comes through the horn
    c.shot(seg('s04-V5push', V5P, 0.0, d4), d4, '2', V5P)
    b5 = c.t                                  # back inside: the rest of her ask, through the horn
    t = c.line(5, 1, b5 + 0.3, 'vox-maddie', fx=True, line=lines[5])
    t = c.line(6, 0, t + 0.4, 'vox-maddie', fx=True, line=lines[6])
    d5 = t + 0.5 - b5
    c.shot(seg('s05-N3', N3, 1.5, d5), d5, '2', N3, t_in=1.5)
    c.sound('sfx-tannoy', SFX / 'fs530037-tannoy-pa-static.mp3', b5, 'tannoy static under her', gain=-22, d=d5,
            fade=0.4)
    c.beat('2', 'Through the door', b2,
           'Outside: Maddie at the shut green doors. Inside: the old lady shouts; outside we hear the rest muffled '
           'through the steel. Maddie owns it, and asks how to win their trust.', [lines[i] for i in (2, 3, 4, 5, 6)])
    c.flags.append('Stand-in: beat 2 reuses the old doorstep shots (cut3-V5, its push-in, cut2-N3; N3 opens the scene '
                   'too).')

    # beat 3: the film. Room (her offer, TV static, then it starts) -> the film full frame -> the room, green.
    b6 = c.t
    t = c.line(7, 0, b6 + 0.3, 'vox-maddie', fx=True, line=lines[7])
    t = c.line(7, 1, t + 0.6, 'vox-maddie', fx=True, line=lines[7])
    on = t + 0.4 - b6                          # the TV comes on as her line ends
    total_push = on + 3.6                      # the push runs over both room shots
    dA = on + 0.6
    c.shot(seg('s06-room', BR[2], 0.0, dA, tv=(-on, on), pingpong=4.5,
               push=(1.0, 1.0 + PUSH[2] * dA / total_push)), dA, '3', BR[2], looped=True)
    c.sound('sfx-tannoy', SFX / 'fs530037-tannoy-pa-static.mp3', b6, 'tannoy static under her', gain=-22, d=on,
            fade=0.4)
    c.flags.append('The room shot under her offer is br2\'s first 4.5 s played forward and back (the heads barely '
                   'move; the push carries on over it).')
    film_at = b6 + on                          # film time 0 on the cut's clock
    c.sound('sfx-tv', SFX / 'synth-cctv-hiss-20s.wav', b6, 'the old TV: hiss', gain=-18, d=on + 0.6, fade=0.3)
    dF = 9.0                                   # film 0.6 -> 9.6: the race, the brake, the flip at 7.0, the green
    f0 = c.t - film_at
    c.shot(seg('s07-film', film(), f0, dF), dF, '3', film())
    c.sound('sfx-hud', SFX / 'synth-killbot-red-flip.wav', film_at + 0.05, 'kill mode tone', gain=-10)
    c.sound('sfx-hud', SFX / 'synth-hud-blip.wav', film_at + FLIP, 'the flip to green', gain=-8)
    c.sound('sfx-tv', SFX / 'synth-cctv-hiss-20s.wav', c.t - dF, 'the film\'s own hiss', gain=-14, d=dF, fade=0.3)
    c.sound('sfx-killbot', SFX / 'fs557594-killbot-mech-walk.mp3', c.t - dF, 'the kill bot\'s tracks, on the TV',
            gain=-14, d=FLIP - f0 + 0.6, fade=0.5)
    t = c.line(9, 0, film_at + 8.4, 'vox-maddie', fx=True, line=lines[9])
    dC = 3.0
    bC = c.t
    c.shot(seg('s08-room', BR[2], 5.0, dC + 0.6, tv=(bC - film_at, 0.0),
               push=(1.0 + PUSH[2] * (dA / total_push), 1.0 + PUSH[2])), dC + 0.6, '3', BR[2], t_in=5.0)
    t = c.line(9, 1, max(t + 0.3, bC + 0.2), 'vox-maddie', fx=True, line=lines[9])
    c.beat('3', 'The film', b6,
           "She leaves them a film: the kill bot's own eyes racing at THEIR door, red KILL MODE; it brakes and the "
           'screen flips to NEW OBJECTIVE: SUSTAIN ORGANIC LIFE. The one camera move: a slow push towards the TV.',
           [lines[7], lines[9]])
    c.flags.append('The red-to-green on the room is only on the TV for now; the light on the vault and heads stays '
                   'red (a grade for Premiere).')

    # beat 4: the boom
    b7 = c.t
    boom_at = b7 + 0.9                         # br3's jolt is about a second in
    c.sound('sfx-boom', SFX / 'derived-muffled-boom-big.wav', boom_at - 0.1, 'the boom, through the earth')
    c.sound('sfx-boom', SFX / 'derived-dust-falling-12s.wav', boom_at + 0.2, 'dust falling', gain=-6, d=4.5, fade=1.0)
    c.shot(seg('s09-boom', BR[3], 0.0, 4.0, swap_tv=(762, 462, 106, 86)), 4.0, '4', BR[3])
    c.beat('4', 'The boom', b7, 'A deep muffled boom; the horn jolts on its bracket, dust pours, one man looks up.')
    c.flags.append(f"Maddie's \"Oh, and... thought you'd want to hear this bit\" is mine (by: claude); it ends "
                   f"{boom_at - t:.1f} s before the boom.")

    # beat 5: Derek looks; what he sees; Maddie goes
    b8 = c.t
    c.shot(seg('s10-derek', BR[4], 0.0, 3.0), 3.0, '5', BR[4])
    b9 = c.t
    c.sound('sfx-room', SFX / 'fs221090-bunting-waving-flag.mp3', b9, 'wind in the bunting, outside', gain=-18, d=8.0,
            fade=0.6)
    t = c.line(12, 0, b9 + 1.4, 'vox-maddie', fx=True, line=lines[12])
    c.sound('sfx-maddie', SFX / 'fs455105-robot-wheels-rc-car.mp3', b9 + 4.2, 'Maddie trundles off', gain=-2, d=3.5,
            fade=1.0)
    c.shot(seg('s11-view', BR[5], 0.0, 8.0), 8.0, '5', BR[5])
    c.beat('5', 'The periscope', b8, 'Derek checks for himself: the kill bot is a wreck, a crow on it. Maddie, by the '
           'wreck: "Right. I\'ll come back tomorrow." She trundles out of the circle.', [lines[12]])

    # beat 6: the debate (Sandra pre-laps over the view as Maddie goes)
    b10 = c.t
    t = c.line(14, 0, b9 + 4.7, 'vox-sandra', line=lines[14])
    c.shot(seg('s12-derek-b', BR[4], 1.0, 5.0), 5.0, '6', BR[4], t_in=1.0)
    t = c.line(14, 1, t + 0.5, 'vox-sandra', line=lines[14])
    t = c.line(15, 0, t + 0.15, 'vox-derek', line=lines[15])
    t = c.line(16, 0, t + 0.6, 'vox-lady', line=lines[16])
    for p, g in ((1, 0.6), (2, 0.6), (3, 1.2)):
        t = c.line(16, p, t + g, 'vox-lady', line=lines[16])
    left = t + 0.8 - c.t
    for k, f in enumerate(('cut3-lip-17-6a-muted.mp4', 'cut3-lip-17-3-muted.mp4', 'cut3-lip-17-6b1-muted.mp4')):
        if left <= 0.05:
            break
        d = min(left, 7.5) if left - 7.5 > 1.5 or left <= 7.5 else left - 2.0
        c.shot(seg(f's13-lady-{k}', VID / f, 0.0, d), d, '6', VID / f)
        left -= d
    c.beat('6', 'The debate', b9 + 4.7, "Sandra: she'd take any way out of this bunker. Derek: \"Oi.\" The old lady, "
           'flat: the food is running out. Perhaps they should vote. No vote shown.', [lines[i] for i in (14, 15, 16)])
    c.flags.append('Stand-in: the debate has no shots of its own. Sandra plays over the view and Derek at the '
                   'periscope (its first seconds repeat); the old lady over three of her old doorstep lip-sync clips, '
                   'made for other words, so her lips do not match (and they move while Sandra and Derek talk).')

    # beat 7: the card
    b12 = c.t
    c.shot(card('The next day.', 2.5), 2.5, '7', V / 'card-the-next-day.mp4')
    c.beat('7', 'The next day', b12, 'Black. "The next day." Silence. Then scene C: Maddie on the step.')

    # room tone under everything inside, wind outside
    total = c.t
    for s, e, what, f, g in [(b1, b2, 'bunker room tone', 'fs189231-crowd-shuffling.mp3', -24),
                             (b3, b4, 'bunker room tone', 'fs189231-crowd-shuffling.mp3', -24),
                             (b5, b9, 'bunker room tone', 'fs189231-crowd-shuffling.mp3', -26),
                             (b10, b12, 'bunker room tone', 'fs189231-crowd-shuffling.mp3', -24)]:
        c.sound('sfx-room', SFX / f, s, what, gain=g, d=e - s, fade=0.3)
    wind = M / 'cut3/A/stems/16-sfx-wind.wav'
    for s, e in ((b2, b3), (b4, b5)):
        c.sound('sfx-wind', wind, s, 'wind on the downs (from scene A\'s wind stem)', gain=-4, d=e - s, fade=0.3)

    # line times for the page
    for ln in lines.values():
        parts = ln.pop('_parts', [])
        if parts:
            ln['t'] = round(parts[0][0], 3)
            ln['dur'] = round(parts[-1][0] + parts[-1][1] - parts[0][0], 3)

    render(c, total, OUT, 'gpom-3-B-bridge (rough)', 1)


def render(c, total, OUT, seq, rnd):
    ST = OUT / 'stems'
    ST.mkdir(parents=True, exist_ok=True)
    lst = OUT / 'concat.txt'
    lst.write_text(''.join(f"file '{v['file']}'\n" for v in c.video))
    pic = OUT / 'picture.mp4'
    ff('-f', 'concat', '-safe', 0, '-i', lst, '-c', 'copy', pic)
    order = ['vox-maddie', 'vox-lady', 'vox-sandra', 'vox-derek', 'sfx-tannoy', 'sfx-tv', 'sfx-hud', 'sfx-killbot',
             'sfx-boom', 'sfx-maddie', 'sfx-room', 'sfx-wind']
    audio = []
    for k, name in enumerate(n for n in order if any(e['stem'] == n for e in c.events)):
        evs = [e for e in c.events if e['stem'] == name]
        inp, fl = [], []
        for j, e in enumerate(evs):
            inp += ['-i', e['src']]
            fd = e['fade']
            fl.append(f"[{j}:a]aresample={SR},aformat=channel_layouts=mono,atrim=0:{e['dur']},"
                      + (f"afade=t=in:d={fd},afade=t=out:st={max(e['dur'] - fd, 0)}:d={fd}," if fd else '')
                      + (f"aloop=loop=-1:size={int(60 * SR)},atrim=0:{e['dur']}," if e['dur'] > dur(e['src']) else '')
                      + f"volume={e['gain']}dB,adelay={int(e['t'] * 1000)}|{int(e['t'] * 1000)}[e{j}]")
        mix = ''.join(f'[e{j}]' for j in range(len(evs)))
        stem = ST / f'{k + 1:02d}-{name}.wav'
        ff(*inp, '-filter_complex', ';'.join(fl) + f';{mix}amix=inputs={len(evs)}:normalize=0,apad=whole_dur={total}'
           f',atrim=0:{total}[o]', '-map', '[o]', '-ac', 1, '-ar', SR, stem)
        audio.append({'track': f'A{k + 1}', 'name': name, 'file': str(stem)})
    mixf = OUT / 'mix.wav'
    ins = sum((['-i', a['file']] for a in audio), [])
    ff(*ins, '-filter_complex', ''.join(f'[{k}:a]' for k in range(len(audio))) +
       f'amix=inputs={len(audio)}:normalize=0,alimiter=limit=0.79,pan=stereo|c0=c0|c1=c0[o]', '-map', '[o]', '-ar', SR,
       mixf)
    prev = OUT / 'preview.mp4'
    ff('-i', pic, '-i', mixf, '-map', '0:v', '-map', '1:a', '-vf', 'lutyuv=y=clip(val\\,16\\,235):u=clip(val\\,16\\,240)'
       ':v=clip(val\\,16\\,240)', *ENC, '-c:a', 'aac', '-b:a', '192k', '-shortest', prev)  # keep it in legal range

    # beats' durations
    for k, b in enumerate(c.beats):
        nxt = c.beats[k + 1]['start'] if k + 1 < len(c.beats) else total
        b['dur'] = round(nxt - b['start'], 3)
    c.beats.sort(key=lambda b: b['start'])
    edl = {'sequence': seq, 'title': 'Bridge Timeline', 'round': rnd,
           'heading': 'GPOM · the bridge: Maddie at the door (draft 1G)',
           'intro': 'The bridge between the kill bots standing down and the humans following Maddie out. Draft 1G, '
                    'voiced; the five new clips plus stand-ins from the old door scene. Play it, click any beat, clip, '
                    'line or sound and leave a note in its yellow slip. Tell Claude when you are done.',
           'fps': FPS, 'sample_rate': SR, 'total': round(total, 3), 'beats': c.beats, 'video': c.video,
           'audio': [{'track': a['track'], 'name': a['name']} for a in audio],
           'events': [{k: e[k] for k in ('stem', 't', 'dur', 'what', 'src')} for e in c.events],
           'mix': str(mixf), 'preview': str(prev), 'flags': c.flags}
    (OUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False) + '\n')
    print(json.dumps({'total': round(total, 2), 'shots': len(c.video), 'events': len(c.events),
                      'beats': [(b['id'], b['start'], b['dur']) for b in c.beats]}))



# ==== Round 2 (Kai's timeline r1 notes, 3 Nov; picks on https://claude.ai/artifact/FnDZVwKFUsFdf4X813sKKt) ==========
#   python3 scripts/gpom/second-half-video/cut-bridge.py --round 2      -> <media>/cut3/B-bridge-r2/
# Voices from voices-bridge2.json (the old lady = Vindemiatrix, Kai's pick); the tannoy without its static bed and with
# round 2's cleaner filter; the TV off (tv-off.py) until the film and in the boom shot; the film = scene A's hud-12 only
# (the run at the door, the brake, the flip); Derek's look halved; the debate on its own lip-synced clips.
LADY = 'Vindemiatrix'


def take2(vb, i, p, fx=False):
    row = next(r for r in vb['lines'] if r['i'] == i)
    ph = row['phrases'][p]
    if 'audition' in ph:
        ph = {**ph, **ph['audition'][LADY]}
    if 'reused' in ph:
        f = ph['reused']
    else:
        f = next(t['file'] for t in ph['takes'] if t['take'] == ph['pick'])
    if fx:
        f = ph['fx_file']
    return VOX / f, row, ph


def lips(clip):
    """First real mouth opening in a talking clip (s), from the picture (lip-sync-dub step 5)."""
    js = OUT2 / 'lips' / (pathlib.Path(clip).stem + '.lips.json')
    js.parent.mkdir(parents=True, exist_ok=True)
    if not js.exists():
        subprocess.run([str(pathlib.Path.home() / '.cache/badcode-lips/venv/bin/python'),
                        str(REPO / 'scripts/bank-robbery/lips.py'), str(clip), '--face', 'big', '--json', str(js)],
                       check=True, capture_output=True)
    L = json.loads(js.read_text())
    g = [x or 0 for x in L['gap']]
    fps = L['fps']
    lo = sorted(g)[int(len(g) * 0.1)]
    hi = sorted(g)[int(len(g) * 0.95)]
    th = lo + (hi - lo) * 0.45
    for k in range(int(0.1 * fps), len(g) - 2):
        if g[k] > th and g[k + 1] > th and abs(g[k + 2] - g[k]) > (hi - lo) * 0.05:
            return k / fps
    return 0.3


OUT2 = M / 'cut3/B-bridge-r2'


def split_take(f):
    """Cut one voice take in two at its first inner silence of 0.2 s or more (the first sentence break), for a line spread over two
    talking clips. Returns the two halves (wav files beside the round's stems)."""
    err = subprocess.run(['ffmpeg', '-nostats', '-i', str(f), '-af', 'silencedetect=n=-30dB:d=0.08', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)]
    se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', err)]
    total = dur(f)
    gaps = [(s_, e) for s_, e in zip(ss, se) if 1.5 < s_ and e < total - 1.0 and e - s_ >= 0.2]
    a, b = gaps[0]                              # the first sentence break
    out = OUT2 / 'split'
    out.mkdir(parents=True, exist_ok=True)
    h1, h2 = out / f'{f.stem}-1.wav', out / f'{f.stem}-2.wav'
    ff('-i', f, '-t', a + 0.05, h1)
    ff('-ss', max(b - 0.05, 0), '-i', f, h2)
    return h1, h2


def main2():
    global V
    V = OUT2 / 'video'
    V.mkdir(parents=True, exist_ok=True)
    (OUT2 / 'stems').mkdir(parents=True, exist_ok=True)
    vb = json.loads((SCENE / 'voices-bridge2.json').read_text())
    sc = json.loads((SCENE / 'script.json').read_text())['lines']
    c = Cut()

    def line(i, p, at, stem, fx=False, ln=None):
        f, row, ph = take2(vb, i, p, fx)
        dry = dur(take2(vb, i, p)[0])
        kind = row['fx'] if fx else 'dry'
        gain = round(TARGET[kind] - lufs(f), 1)
        c.events.append({'stem': stem, 't': round(at, 3), 'dur': round(dur(f), 3), 'src': str(f), 'gain': gain,
                         'fade': 0.0, 'what': f"line {i}{f' p{p}' if len(row['phrases']) > 1 else ''}"
                                             f"{' (tannoy)' if fx and kind == 'tannoy' else ' (through the door)' if fx else ''}: {ph['text']}"})
        if ln is not None:
            ln.setdefault('_parts', []).append((at, dry))
        return at + dry

    def L2(i):
        s = sc[i]
        return {'i': i, 'who': s['who'], 'name': NAME.get(s['who'], s['who']), 'text': s['text'], 'by': s['by']}
    lines = {i: L2(i) for i, s in enumerate(sc) if s['who'] in NAME}
    N3, V5 = VID / 'cut2-N3.mp4', VID / 'cut3-V5.mp4'
    V5P = M / 'cut3/B-br/video/cut3-V5-wait-push-i0-d6.000.mp4'
    TVOFF2, TVOFF3 = OUT2 / 'video/tvoff-br2-2B-BP1-e-b.mp4', OUT2 / 'video/tvoff-br3-3A-BP1-e-b.mp4'
    BR = {k: VID / f for k, f in {2: 'shb-br2-2B-BP1-e-b.mp4', 4: 'shb-br4-4A-BP2-a-a.mp4', 5: 'shb-br5-5A-BP3-e-a.mp4',
                                   7: 'shb-br7-lady1-BP4-lady-b.mp4', 8: 'shb-br8-lady2a-BP4-lady-b.mp4',
                                   9: 'shb-br9-lady2b-BP4-lady-b.mp4', 10: 'shb-br10-sandra1-BP5-sandra-b.mp4',
                                   11: 'shb-br11-sandra2-BP5-sandra-b.mp4', 12: 'shb-br12-crowd-BR3-end.mp4',
                                   13: 'shb-br13-lady0-LADY0.mp4'}.items()}

    # 1 · the tannoy
    b1 = c.t
    c.sound('sfx-tannoy', SFX / 'synth-tannoy-click.wav', b1 + 0.05, 'tannoy click on', gain=-6)
    t = line(0, 0, b1 + 0.45, 'vox-maddie', fx=True, ln=lines[0])
    t = line(1, 0, t + 0.12, 'vox-maddie', fx=True, ln=lines[1])
    d = t + 0.4 - b1
    c.shot(seg('s01-N3', N3, 0.0, d), d, '1', N3)
    c.beat('1', 'The tannoy', b1, 'Inside: the hundred look up at the horn as her chirpy voice cuts in. Doors shut.',
           [lines[0], lines[1]])

    # 2 · through the door
    b2 = c.t
    t = line(2, 0, b2 + 0.3, 'vox-maddie', ln=lines[2])
    t = line(2, 1, t + 0.6, 'vox-maddie', ln=lines[2])
    c.shot(seg('s02-V5', V5, 0.0, 8.0), 8.0, '2', V5)
    b3 = c.t
    lady0 = BR[13] if BR[13].exists() else None
    if lady0:
        on = lips(lady0)
        t = line(3, 0, max(t + 0.5, b3 + on + 0.05), 'vox-lady', ln=lines[3])
        d = t + 0.3 - b3
        c.shot(seg('s03-lady', lady0, 0.0, d), d, '2', lady0)
    else:
        t = line(3, 0, max(t + 0.5, b3 + 1.0), 'vox-lady', ln=lines[3])
        d = t + 0.3 - b3
        src = VID / 'cut3-lip-17-0-muted.mp4'
        c.shot(seg('s03-lady-old', src, 0.0, d), d, '2', src)
        c.flags.append("Stand-in: the old lady's shout is still on her old lip-sync clip (her new shouting clip isn't made).")
    b4 = c.t
    t = line(4, 0, b4 + 0.05, 'vox-lady', fx=True, ln=lines[4])
    t = line(5, 0, t + 0.5, 'vox-maddie', ln=lines[5])
    d = t + 0.35 - b4
    c.shot(seg('s04-V5push', V5P, 0.0, d), d, '2', V5P)
    b5 = c.t
    t = line(5, 1, b5 + 0.3, 'vox-maddie', fx=True, ln=lines[5])
    t = line(6, 0, t + 0.4, 'vox-maddie', fx=True, ln=lines[6])
    d = t + 0.5 - b5
    c.shot(seg('s05-N3', N3, 1.5, d), d, '2', N3, t_in=1.5)
    c.beat('2', 'Through the door', b2, 'Outside: Maddie at the shut green doors. Inside: the old lady shouts; outside '
           'we hear the rest through the steel. Maddie owns it, and asks how to win their trust.',
           [lines[i] for i in (2, 3, 4, 5, 6)])

    # 3 · the film: the TV off while she offers it; it comes on; the film full frame; back on the room, green
    b6 = c.t
    t = line(7, 0, b6 + 0.3, 'vox-maddie', fx=True, ln=lines[7])
    t = line(7, 1, t + 0.6, 'vox-maddie', fx=True, ln=lines[7])
    on = t + 0.4 - b6
    total_push = on + 3.6
    dA = on + 0.6
    filmf = film2()
    c.shot(seg('s06-room', TVOFF2, 0.0, dA, tv=(-on, on), tv_off=True, pingpong=4.5, film_src=filmf,
               push=(1.0, 1.0 + PUSH[2] * dA / total_push)), dA, '3', BR[2], looped=True)
    film_at = b6 + on
    f0 = c.t - film_at
    dF = 5.4                                    # hud-12 from 0.3: the run at the door, the brake, the flip at 3.2
    c.shot(seg('s07-film', filmf, f0, dF), dF, '3', M / 'cut3/A-d6/video/hud-12.mp4')
    c.sound('sfx-hud', SFX / 'synth-killbot-red-flip.wav', film_at + 0.05, 'kill mode tone', gain=-10)
    c.sound('sfx-hud', SFX / 'synth-hud-blip.wav', film_at + FLIP2, 'the flip to green', gain=-8)
    c.sound('sfx-tv', SFX / 'synth-cctv-hiss-20s.wav', film_at, "the film's own hiss", gain=-24, d=c.t - film_at, fade=0.3)
    c.sound('sfx-killbot', SFX / 'fs557594-killbot-mech-walk.mp3', film_at, "the kill bot's tracks, on the TV",
            gain=-14, d=FLIP2 + 0.5, fade=0.4)
    t = line(9, 0, film_at + FLIP2 + 1.4, 'vox-maddie', fx=True, ln=lines[9])
    bC = c.t
    dC = 3.6
    c.shot(seg('s08-room', BR[2], 5.0, dC, tv=(bC - film_at, 0.0), film_src=filmf,
               push=(1.0 + PUSH[2] * (dA / total_push), 1.0 + PUSH[2])), dC, '3', BR[2], t_in=5.0)
    t = line(9, 1, max(t + 0.3, bC + 0.2), 'vox-maddie', fx=True, ln=lines[9])
    c.beat('3', 'The film', b6, "The TV stays off while she offers it, then comes on: the kill bot's own eyes racing at "
           'THEIR door in red, the brake, NEW OBJECTIVE: SUSTAIN ORGANIC LIFE. The one camera move: a slow push to the TV.',
           [lines[7], lines[9]])

    # 4 · the boom; the old lady sends Derek
    b7 = c.t
    boom_at = b7 + 0.9
    c.sound('sfx-boom', SFX / 'derived-muffled-boom-big.wav', boom_at - 0.1, 'the boom, through the earth')
    c.sound('sfx-boom', SFX / 'derived-dust-falling-12s.wav', boom_at + 0.2, 'dust falling', gain=-6, d=5.0, fade=1.0)
    c.shot(seg('s09-boom', TVOFF3, 0.0, 4.0), 4.0, '4', VID / 'shb-br3-3A-BP1-e-b.mp4')
    b8 = c.t
    on = R6_MOUTH['derek'] - 0.05 if ROUND3 >= 6 else lips(BR[7])
    t = line(11, 0, b8 + on + 0.05, 'vox-lady', ln=lines[11])
    d = min(max(t + 0.3 - b8, 2.5), 4.0)
    c.shot(seg('s10-lady-derek', BR[7], 0.0, d), d, '4', BR[7])
    c.beat('4', 'The boom', b7, 'A deep muffled boom; the horn jolts down on its bracket, dust pours. The old lady: '
           '"Derek, go and have a look what that was."', [lines[11]])

    # 5 · Derek looks; the wreck; Maddie through the tannoy, inside
    b9 = c.t
    c.shot(seg('s11-derek', BR[4], 0.0, 1.6), 1.6, '5', BR[4])
    b10 = c.t
    c.sound('sfx-room', SFX / 'fs221090-bunting-waving-flag.mp3', b10, 'wind outside', gain=-18, d=4.6, fade=0.6)
    t = line(13, 0, b10 + 0.9, 'vox-derek', ln=lines[13])
    d = max(t + 0.6 - b10, 4.0)
    c.shot(seg('s12-view', BR[5], 0.0, d), d, '5', BR[5])
    b11 = c.t
    t = line(14, 0, b11 + 0.6, 'vox-maddie', fx=True, ln=lines[14])
    d = t + 0.7 - b11
    c.shot(seg('s13-crowd', BR[12], 0.0, d), d, '5', BR[12])
    c.beat('5', 'The periscope', b9, 'Derek checks: the kill bot is a wreck. "They\'ve blown up their own kill bot." '
           'Back inside, under the bent horn: "Right. I\'ll come back tomorrow."', [lines[13], lines[14]])

    # 6 · the debate on its own faces
    b12 = c.t
    f16 = take2(vb, 16, 0)[0]
    s1, s2 = split_take(f16)
    g16 = round(TARGET['dry'] - lufs(f16), 1)
    on = lips(BR[10])
    t = c.sound('vox-sandra', s1, b12 + on + 0.05, "line 16 (1/2): If there's a way to fix this, I'd love to take it.", gain=g16)
    lines[16]['t'] = round(b12 + on + 0.05, 3)
    d = min(max(t + 0.25 - b12, 3.0), 6.0)
    c.shot(seg('s14-sandra', BR[10], 0.0, d), d, '6', BR[10])
    b13 = c.t
    on = lips(BR[11])
    t = c.sound('vox-sandra', s2, b13 + on + 0.05, 'line 16 (2/2): It sucks living in this bunker with grumpy Derek.', gain=g16)
    lines[16]['dur'] = round(t - lines[16]['t'], 3)
    oi_at = max(t + 0.15, b13 + 4.3)          # as Derek leans in with his hands up (about 4 s into the clip)
    fo = take2(vb, 17, 0)[0]
    c.sound('vox-derek', fo, oi_at, 'line 17: Oi.', gain=round(TARGET['dry'] - lufs(fo), 1))
    lines[17]['t'], lines[17]['dur'] = round(oi_at, 3), round(dur(fo), 3)
    d = min(max(oi_at + 1.2 - b13, 5.0), 6.0)
    c.shot(seg('s15-sandra2', BR[11], 0.0, d), d, '6', BR[11])
    b14 = c.t
    f18 = take2(vb, 18, 0)[0]
    l1, l2 = split_take(f18)
    g18 = round(TARGET['dry'] - lufs(f18), 1)
    on = lips(BR[8])
    t = c.sound('vox-lady', l1, b14 + on + 0.05, 'line 18 (1/2): We know we need to talk about this.', gain=g18)
    lines[18]['t'] = round(b14 + on + 0.05, 3)
    da = min(max(t + 0.25 - b14, 2.5), 4.0)
    c.shot(seg('s16-lady-a', BR[8], 0.0, da), da, '6', BR[8])
    b15b = c.t
    on = lips(BR[9])
    t = c.sound('vox-lady', l2, b15b + on + 0.05, 'line 18 (2/2): We do have a food problem. Perhaps we should vote.', gain=g18)
    lines[18]['dur'] = round(t - lines[18]['t'], 3)
    db = min(max(t + 0.6 - b15b, 3.0), 6.0)
    c.shot(seg('s17-lady-b', BR[9], 0.0, db, punch=1.12), db, '6', BR[9])
    c.beat('6', 'The debate', b12, "Sandra: she'd take any way out. Derek leans in: \"Oi.\" The old lady: we need to "
           'talk about this; food; perhaps a vote. No vote shown.', [lines[i] for i in (16, 17, 18)])
    c.flags.append('Each half of Sandra\'s and the old lady\'s lines starts on its own clip\'s first mouth opening '
                   '(read from the picture); nobody has checked the sync by eye yet. The second half of the old lady is '
                   'punched in 112% so the cut reads.')

    # 7 · the card
    b15 = c.t
    c.shot(card('The next day.', 2.5), 2.5, '7', V / 'card-the-next-day.mp4')
    c.beat('7', 'The next day', b15, 'Black. "The next day." Silence. Then scene C: Maddie on the step.')

    total = c.t
    for s, e in ((b1, b2), (b3, b4), (b5, b9), (b11, b15)):
        c.sound('sfx-room', SFX / 'fs189231-crowd-shuffling.mp3', s, 'bunker room tone', gain=-26, d=e - s, fade=0.3)
    wind = M / 'cut3/A/stems/16-sfx-wind.wav'
    for s, e in ((b2, b3), (b4, b5)):
        c.sound('sfx-wind', wind, s, "wind on the downs (from scene A's wind stem)", gain=-4, d=e - s, fade=0.3)
    for ln in lines.values():
        parts = ln.pop('_parts', [])
        if parts:
            ln['t'] = round(parts[0][0], 3)
            ln['dur'] = round(parts[-1][0] + parts[-1][1] - parts[0][0], 3)
    c.flags.append('The static bed is gone and the tannoy filter is cleaner (Kai, timeline r1).')
    render(c, total, OUT2, 'gpom-3-B-bridge (rough, round 2)', 2)


FLIP2 = 3.2


def film2():
    out = V / 'film-r2.mp4'
    if out.exists():
        return out
    b = M / 'cut3/A-d6/video/hud-12.mp4'
    ff('-ss', 0.3, '-i', b, '-filter_complex',
       f'[0:v]scale={W}:{H},setsar=1,fps={FPS},trim=0:6.7,setpts=PTS-STARTPTS,noise=alls=10:allf=t,'
       "geq=lum='lum(X,Y)*(0.86+0.14*abs(sin(Y*1.6)))':cb='cb(X,Y)':cr='cr(X,Y)',vignette=PI/4.5,"
       'tpad=stop_mode=clone:stop_duration=8[v]', '-map', '[v]', '-an', *ENC, out)
    return out


# ==== Round 3 (Kai's timeline r2 notes, 4 Nov; feedback/bridge-timeline-r2) =========================================
#   python3 scripts/gpom/second-half-video/cut-bridge.py --round 3      -> <media>/cut3/B-bridge-r3/
# "Hello there, sorry about the intrusion", coy (voices-bridge3.json); the lip-sync read BY EYE off 12 fps tracked mouth
# strips (lips() put the old lady 1.7 s late and Sandra 0.9 s early: it read a parted, still mouth as speech); the film =
# scene A's newest stand-down (A-d8 hud-12, far from the door); the boom on a clip chained from the room shot's last
# frame (br14), the TV still showing the film until the jolt kills it; Sandra's second half chained from her first
# (br15); no "Oi"; the old lady's vote line shortened, on br9 alone.
OUT3 = M / 'cut3/B-bridge-r3'
ROUND3 = 3                                 # --round 4 reuses main3 into B-bridge-r4 (Kai's r3 lip-sync notes)
# Speech onsets read by eye (lip-sync-dub step 5), clip time, s. Each phrase's first voiced sample lands here.
MOUTH = {'lady0': 0.95,                    # br13: parted but still 0.42-0.83 (not speech); "Are" opens 0.92 (r4: Kai at407, was 0.65)
         'sandra1': (1.40, 3.67),          # br10: "If there's a way to fix this," / "I'd love to take it." (shut 2.75-3.58; r4 at1764, was 3.40)
         'vote': (1.10, 2.85)}             # br9: "We do have a food problem." / "Perhaps we should vote." (r4: only the second)
# Round 6 re-shoots (Kai r5: horn hanging, no cap), read off 12 fps tracked strips: br16 "Derek" opens 0.25; br18
# "If" 1.00, "I'd" ~3.45 (her mouth holds open 2.6-4.1, so this one is approximate); br17-alt lips pressed 0.9-2.4
# (the hum), "Perhaps" opens 2.58; br19 measured when it lands.
R6_MOUTH = {'derek': 0.27, 'sandra1': (1.00, 3.45), 'vote': (None, 2.60), 'hmm': 0.95, 'vote_in': 0.45, 'sandra2': 1.20}  # br19: "It" 1.17, speech to ~4.1 at x1.0
VOTE_IN = 2.45                             # r4: br9 starts here, head settled, food-problem mouth cut away
BOOM_JOLT = 0.35                           # br14: the horn lurches between 0.25 and 0.5 (contact sheet)
SANDRA2_ON = 1.62                          # br15: "It" opens at 1.58 (12 fps strip); her mouth runs x1.25 slower
SANDRA2_TEMPO = 0.88                       # than the take, so this phrase is eased to 0.88 (lip-sync-dub: 0.85-1.30)


def onset(f, th='-35dB'):
    """The first voiced sample of a wav (s): the lead-in silence Gemini puts before the words."""
    err = subprocess.run(['ffmpeg', '-nostats', '-i', str(f), '-af', f'silencedetect=n={th}:d=0.05', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    m = re.search(r'silence_start: 0(?:\.0+)?\s.*?silence_end: ([\d.]+)', err, re.S)
    return float(m.group(1)) if m else 0.0


def voiced_end(f, th='-35dB'):
    """The last voiced sample of a wav (s)."""
    err = subprocess.run(['ffmpeg', '-nostats', '-i', str(f), '-af', f'silencedetect=n={th}:d=0.1', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)]
    return starts[-1] if starts and starts[-1] > 0.3 else dur(f)


def cut_at(f, a, b, name, tempo=None):
    """Slice [a, b) of a take into the round's split folder (b None = to the end), optionally retimed."""
    out = OUT3 / 'split' / f'{name}.wav'
    out.parent.mkdir(parents=True, exist_ok=True)
    ff('-ss', a, '-i', f, *(['-t', b - a] if b else []), *(['-af', f'atempo={tempo}'] if tempo else []), out)
    return out


def film3():
    out = V / 'film-r3.mp4'
    if out.exists():
        return out
    b = M / 'cut3/A-d8/video/hud-12.mp4'       # Kai r2: the newest stand-down, the bot far from the door
    ff('-ss', 0.3, '-i', b, '-filter_complex',
       f'[0:v]scale={W}:{H},setsar=1,fps={FPS},trim=0:6.7,setpts=PTS-STARTPTS,noise=alls=10:allf=t,'
       "geq=lum='lum(X,Y)*(0.86+0.14*abs(sin(Y*1.6)))':cb='cb(X,Y)':cr='cr(X,Y)',vignette=PI/4.5,"
       'tpad=stop_mode=clone:stop_duration=8[v]', '-map', '[v]', '-an', *ENC, out)
    return out


def tv_until(name, src, d, film_src, f0, until):
    """The film on the TV from shot start until `until`, one flicker, then the clip's own dark screen."""
    out = V / f'{name}.mp4'
    if out.exists():
        return out
    x, y, w, h = TV
    ff('-i', src, '-ss', max(f0, 0), '-i', film_src, '-filter_complex',
       f'[0:v]scale={W}:{H},setsar=1,fps={FPS},tpad=stop_mode=clone:stop_duration={d},trim=0:{d}[b];'
       f'[1:v]scale={w}:{h},setsar=1,eq=brightness=0.06:saturation=1.3,gblur=sigma=0.6,setpts=PTS-STARTPTS[f];'
       f"[b][f]overlay={x}:{y}:eof_action=repeat:enable='lt(t,{until})+between(t,{until + 0.12},{until + 0.2})'[o]"
       + (f";[o]split[o1][o2];[o2]crop={w + 12}:{h + 12}:{x - 6}:{y - 6},hue=s=0[g];"   # Kai r4 at972: the dead TV's
          f"[o1][g]overlay={x - 6}:{y - 6}:enable='between(t,{until + 0.2},{until + 1.2})'[v]"        # red rim, greyed out
          if ROUND3 >= 5 else ';[o]null[v]'),
       '-map', '[v]', '-t', d, '-an', *ENC, out)
    return out


def main3():
    global V, OUT2
    V = OUT3 / 'video'
    V.mkdir(parents=True, exist_ok=True)
    (OUT3 / 'stems').mkdir(parents=True, exist_ok=True)
    R2 = OUT2
    OUT2 = OUT3                                  # lips() caches and split_take() write under this round
    global TV
    if ROUND3 >= 5:
        TV = (771, 444, 111, 89)                 # Kai r4 at972/at1221: the red screen showed round the box; re-measured
        TARGET['muffled'] = -25.0                # Kai r4 at519: "You killed everybody" bolder, less behind the door
    vb = json.loads((SCENE / f"voices-bridge{6 if ROUND3 >= 6 else 4 if ROUND3 >= 5 else 3}.json").read_text())
    sc = json.loads((SCENE / 'script.json').read_text())['lines']
    c = Cut()

    def line(i, p, at, stem, fx=False, ln=None):
        f, row, ph = take2(vb, i, p, fx)
        dry = dur(take2(vb, i, p)[0])
        kind = row['fx'] if fx else 'dry'
        gain = round(TARGET[kind] - lufs(f), 1)
        c.events.append({'stem': stem, 't': round(at, 3), 'dur': round(dur(f), 3), 'src': str(f), 'gain': gain,
                         'fade': 0.0, 'what': f"line {i}{f' p{p}' if len(row['phrases']) > 1 else ''}"
                                             f"{' (tannoy)' if fx and kind == 'tannoy' else ' (through the door)' if fx else ''}: {ph['text']}"})
        if ln is not None:
            ln.setdefault('_parts', []).append((at, dry))
        return at + dry

    def L2(i):
        s_ = sc[i]
        return {'i': i, 'who': s_['who'], 'name': NAME.get(s_['who'], s_['who']), 'text': s_['text'], 'by': s_['by']}
    lines = {i: L2(i) for i, s_ in enumerate(sc) if s_['who'] in NAME}
    N3, V5 = VID / 'cut2-N3.mp4', VID / 'cut3-V5.mp4'
    V5P = M / 'cut3/B-br/video/cut3-V5-wait-push-i0-d6.000.mp4'
    TVOFF2 = R2 / 'video/tvoff-br2-2B-BP1-e-b.mp4'
    BR = {k: VID / f for k, f in {2: 'shb-br2-2B-BP1-e-b.mp4', 4: 'shb-br4-4A-BP2-a-a.mp4', 5: 'shb-br5-5A-BP3-e-a.mp4',
                                   7: 'shb-br7-lady1-BP4-lady-b.mp4', 9: 'shb-br9-lady2b-BP4-lady-b.mp4',
                                   10: 'shb-br10-sandra1-BP5-sandra-b.mp4', 12: 'shb-br12-crowd-BR3-end.mp4',
                                   13: 'shb-br13-lady0-LADY0.mp4', 14: 'shb-br14-boom2-BR4-boomstart.mp4',
                                   15: 'shb-br15-sandra2b-SANDRA5.mp4'}.items()}
    if ROUND3 >= 6:                              # Kai r5: the horn hangs down after the boom; no cap (round 6 re-shoots)
        BR.update({7: VID / 'shb-br16-lady1c-LADY6.mp4', 9: VID / 'shb-br17-lady2c-LADY6-alt.mp4',
                   10: VID / 'shb-br18-sandra1c-SANDRA6.mp4', 15: VID / 'shb-br19-sandra2c-SANDRA7.mp4'})
        MOUTH.update(R6_MOUTH)

    # 1 · the tannoy
    b1 = c.t
    c.sound('sfx-tannoy', SFX / 'synth-tannoy-click.wav', b1 + 0.05, 'tannoy click on', gain=-6)
    t = line(0, 0, b1 + 0.45, 'vox-maddie', fx=True, ln=lines[0])
    t = line(1, 0, t + 0.12, 'vox-maddie', fx=True, ln=lines[1])
    d = t + 0.4 - b1
    c.shot(seg('s01-N3', N3, 0.0, d), d, '1', N3)
    c.beat('1', 'The tannoy', b1, 'Inside: the hundred look up at the horn as her voice cuts in, coy and sorry. Doors shut.',
           [lines[0], lines[1]])

    # 2 · through the door
    b2 = c.t
    t = line(2, 0, b2 + 0.3, 'vox-maddie', ln=lines[2])
    t = line(2, 1, t + 0.6, 'vox-maddie', ln=lines[2])
    f3 = take2(vb, 3, 0)[0]
    # r2's "a good second" late was Maddie's line running into the old lady's shot: hold the door until she's done,
    # so the old lady's mouth (0.65 s into her clip) opens 0.3 s after Maddie stops
    d2 = max(8.0, t + 0.3 - (MOUTH['lady0'] - onset(f3)) - b2)
    if d2 > 8.0:
        c.shot(looped('s02-V5', V5, 0.0, d2), d2, '2', V5, looped=True)
    else:
        c.shot(seg('s02-V5', V5, 0.0, d2), d2, '2', V5)
    b3 = c.t
    at3 = b3 + MOUTH['lady0'] - onset(f3)
    t = line(3, 0, at3, 'vox-lady', ln=lines[3])
    d = max(t + 0.3 - b3, 3.0)
    c.shot(seg('s03-lady', BR[13], 0.0, d), d, '2', BR[13])
    b4 = c.t
    t = line(4, 0, b4 + 0.05, 'vox-lady', fx=True, ln=lines[4])
    t = line(5, 0, t + 0.5, 'vox-maddie', ln=lines[5])
    d = t + 0.35 - b4
    c.shot(seg('s04-V5push', V5P, 0.0, d), d, '2', V5P)
    b5 = c.t
    t = line(5, 1, b5 + 0.3, 'vox-maddie', fx=True, ln=lines[5])
    t = line(6, 0, t + 0.4, 'vox-maddie', fx=True, ln=lines[6])
    d = t + 0.5 - b5
    c.shot(seg('s05-N3', N3, 1.5, d), d, '2', N3, t_in=1.5)
    c.beat('2', 'Through the door', b2, 'Outside: Maddie at the shut green doors. Inside: the old lady shouts; outside '
           'we hear the rest through the steel. Maddie owns it, and asks how to win their trust.',
           [lines[i] for i in (2, 3, 4, 5, 6)])

    # 3 · the film (scene A's newest stand-down)
    b6 = c.t
    t = line(7, 0, b6 + 0.3, 'vox-maddie', fx=True, ln=lines[7])
    t = line(7, 1, t + 0.6, 'vox-maddie', fx=True, ln=lines[7])
    on = t + 0.4 - b6
    total_push = on + 3.6
    dA = on + 0.6
    filmf = film3()
    c.shot(seg('s06-room', TVOFF2, 0.0, dA, tv=(-on, on), tv_off=True, pingpong=4.5, film_src=filmf,
               push=(1.0, 1.0 + PUSH[2] * dA / total_push)), dA, '3', BR[2], looped=True)
    film_at = b6 + on
    f0 = c.t - film_at
    dF = 5.4
    c.shot(seg('s07-film', filmf, f0, dF), dF, '3', M / 'cut3/A-d8/video/hud-12.mp4')
    c.sound('sfx-hud', SFX / 'synth-killbot-red-flip.wav', film_at + 0.05, 'kill mode tone', gain=-10)
    c.sound('sfx-hud', SFX / 'synth-hud-blip.wav', film_at + FLIP2, 'the flip to green', gain=-8)
    c.sound('sfx-tv', SFX / 'synth-cctv-hiss-20s.wav', film_at, "the film's own hiss", gain=-24, d=c.t - film_at, fade=0.3)
    c.sound('sfx-killbot', SFX / 'fs557594-killbot-mech-walk.mp3', film_at, "the kill bot's tracks, on the TV",
            gain=-14, d=FLIP2 + 0.5, fade=0.4)
    t = line(9, 0, film_at + FLIP2 + 1.4, 'vox-maddie', fx=True, ln=lines[9])
    bC = c.t
    dC = 8.0 - 5.0                               # to br2's last frame, which br14 starts from
    c.shot(seg('s08-room', BR[2], 5.0, dC, tv=(bC - film_at, 0.0), film_src=filmf), dC, '3', BR[2], t_in=5.0)
    t = line(9, 1, max(t + 0.3, bC + 0.2), 'vox-maddie', fx=True, ln=lines[9])
    c.beat('3', 'The film', b6, "The TV stays off while she offers it, then comes on: scene A's own stand-down, the kill "
           'bot racing at THEIR door in red, the brake, NEW OBJECTIVE: SUSTAIN ORGANIC LIFE.', [lines[7], lines[9]])

    # 4 · the boom, on the same frame; the jolt kills the TV; the old lady sends Derek
    b7 = c.t
    if t > b7 + BOOM_JOLT - 0.3:                 # let her finish before the jolt
        pass
    hold = max(0.0, t + 0.35 - (b7 + BOOM_JOLT))
    boom_at = b7 + hold + BOOM_JOLT
    db = 4.0 + hold
    src14 = BR[14]
    if hold:                                     # hold br14's first frame until she's done
        src14 = V / 'br14-held.mp4'
        if not src14.exists():
            ff('-i', BR[14], '-vf', f'tpad=start_mode=clone:start_duration={hold}', '-an', *ENC, src14)
    c.shot(tv_until('s09-boom', src14, db, filmf, b7 - film_at, boom_at - b7), db, '4', BR[14])
    c.sound('sfx-boom', SFX / 'derived-muffled-boom-big.wav', boom_at - 0.1, 'the boom, through the earth')
    c.sound('sfx-boom', SFX / 'derived-dust-falling-12s.wav', boom_at + 0.2, 'dust falling', gain=-6, d=5.0, fade=1.0)
    c.sound('sfx-tv', SFX / 'synth-cctv-hiss-20s.wav', b7, 'the film hiss, cut by the jolt', gain=-24, d=boom_at - b7)
    b8 = c.t
    on = R6_MOUTH['derek'] - 0.05 if ROUND3 >= 6 else lips(BR[7])
    t = line(11, 0, b8 + on + 0.05, 'vox-lady', ln=lines[11])
    d = min(max(t + 0.3 - b8, 2.5), 4.0)
    c.shot(seg('s10-lady-derek', BR[7], 0.0, d), d, '4', BR[7])
    c.beat('4', 'The boom', b7, 'A deep muffled boom on the same frame; the horn drops on its bracket, the TV dies, dust '
           'pours. The old lady: "Derek, go and have a look what that was."', [lines[11]])

    # 5 · Derek looks; the wreck; Maddie through the tannoy, inside
    b9 = c.t
    c.shot(seg('s11-derek', BR[4], 0.0, 1.6), 1.6, '5', BR[4])
    b10 = c.t
    c.sound('sfx-room', SFX / 'fs221090-bunting-waving-flag.mp3', b10, 'wind outside', gain=-18, d=4.6, fade=0.6)
    t = line(13, 0, b10 + 0.9, 'vox-derek', ln=lines[13])
    d = max(t + 0.6 - b10, 4.0)
    c.shot(seg('s12-view', BR[5], 0.0, d), d, '5', BR[5])
    b11 = c.t
    t = line(14, 0, b11 + 0.6, 'vox-maddie', fx=True, ln=lines[14])
    d = t + 0.7 - b11
    c.shot(seg('s13-crowd', BR[12], 0.0, d), d, '5', BR[12])
    c.beat('5', 'The periscope', b9, 'Derek checks: the kill bot is a wreck. "They\'ve blown up their own kill bot." '
           'Back inside, under the bent horn: "Right. I\'ll come back tomorrow."', [lines[13], lines[14]])

    # 6 · the debate: Sandra (two chained clips, three phrases), straight to the old lady
    b12 = c.t
    f16 = take2(vb, 16, 0)[0]
    g16 = round(TARGET['dry'] - lufs(f16), 1)
    # whisper on the take: "this," ends 1.84, "I'd" 1.96; "it." ends 3.22, "It" 3.44
    pa, pb, pc = cut_at(f16, 0.0, 1.90, '16-a'), cut_at(f16, 1.90, 3.33, '16-b'), cut_at(f16, 3.33, None, '16-c', tempo=None if ROUND3 >= 6 else SANDRA2_TEMPO)
    m1, m2 = MOUTH['sandra1']
    at = b12 + m1 - onset(pa)
    c.sound('vox-sandra', pa, at, "line 16 (1/3): If there's a way to fix this,", gain=g16)
    lines[16]['t'] = round(at, 3)
    t = c.sound('vox-sandra', pb, b12 + m2 - onset(pb), "line 16 (2/3): I'd love to take it.", gain=g16)
    d = 5.5 if ROUND3 >= 6 else 5.0              # br10 to its frame at 5.0 s, which br15 starts from (r6: br18 at 5.5)
    c.shot(seg('s14-sandra', BR[10], 0.0, d), d, '6', BR[10])
    b13 = c.t
    at16c = b13 + (R6_MOUTH['sandra2'] if ROUND3 >= 6 else SANDRA2_ON) - onset(pc)
    t = c.sound('vox-sandra', pc, at16c, 'line 16 (3/3): It sucks living in this bunker with grumpy Derek.',
                gain=g16)
    sandra_end = at16c + voiced_end(pc)
    lines[16]['dur'] = round(t - lines[16]['t'], 3)
    d = min(max(t + 0.3 - b13, 3.0), 4.7)         # out before she says "grumpy Derek" a second time (4.75)
    c.shot(seg('s15-sandra2', BR[15], 0.0, d), d, '6', BR[15])
    b14 = c.t
    f17 = take2(vb, 17, 0)[0]
    g17 = round(TARGET['dry'] - lufs(f17), 1)
    if ROUND3 >= 4:                              # Kai r3 at1942: just "Perhaps we should vote."
        vb2 = cut_at(f17, 2.30, None, '17-b')
        # Kai r4 at1890: "more naturally half a second pause" after "grumpy Derek": hold br9's first frame
        vin = R6_MOUTH['vote_in'] if ROUND3 >= 6 else VOTE_IN
        if ROUND3 >= 6:                          # Kai r5 at1960: "Hmmm..." over her pressed lips, then the line
            fh = VOX / vb['hmm']['file']
            hold = max(0.0, round(sandra_end + 0.5 - (b14 + R6_MOUTH['hmm'] - vin), 3))
        else:
            hold = max(0.0, round(sandra_end + 0.5 - (b14 + MOUTH['vote'][1] - VOTE_IN), 3))
        src9 = BR[9]
        if hold:
            src9 = V / 'br9-held.mp4'
            ff('-ss', vin, '-i', BR[9], '-vf', f'tpad=start_mode=clone:start_duration={hold}', '-an', *ENC, src9)
        if ROUND3 >= 6:
            ah = b14 + hold + R6_MOUTH['hmm'] - vin - onset(fh)
            c.sound('vox-lady', fh, ah, 'line 17 (1/2): Hmmm...', gain=round(TARGET['dry'] - 3 - lufs(fh), 1))
            lines[17]['t'] = round(ah, 3)
        at = b14 + hold + MOUTH['vote'][1] - vin - onset(vb2)
        t = c.sound('vox-lady', vb2, at, 'line 17: Perhaps we should vote.', gain=g17)
        if ROUND3 < 6:
            lines[17]['t'] = round(at, 3)
        lines[17]['dur'] = round(t - lines[17]['t'], 3)
        db = max(t + 0.6 - b14, 2.0)
        c.shot(seg('s16-lady', src9, 0.0 if hold else vin, db), db, '6', BR[9], t_in=vin)
    else:
        va, vb2 = cut_at(f17, 0.0, 2.30, '17-a'), cut_at(f17, 2.30, None, '17-b')
        n1, n2 = MOUTH['vote']
        at = b14 + n1 - onset(va)
        c.sound('vox-lady', va, at, 'line 17 (1/2): We do have a food problem.', gain=g17)
        lines[17]['t'] = round(at, 3)
        t = c.sound('vox-lady', vb2, b14 + n2 - onset(vb2), 'line 17 (2/2): Perhaps we should vote.', gain=g17)
        lines[17]['dur'] = round(t - lines[17]['t'], 3)
        db = min(max(t + 0.6 - b14, 3.0), 6.0)
        c.shot(seg('s16-lady', BR[9], 0.0, db), db, '6', BR[9])
    c.beat('6', 'The debate', b12, "Sandra: she'd take any way out, and grumpy Derek. The old lady: food; perhaps a vote. "
           'No vote shown.', [lines[16], lines[17]])
    c.flags.append("Lip-sync read by eye off 12 fps mouth strips this round (the automatic reader had the old lady 1.7 s "
                   "late and Sandra 0.9 s early). Sandra's line is three phrases, each on its own mouth burst.")

    # 7 · the card
    b15 = c.t
    c.shot(card('The next day.', 2.5), 2.5, '7', V / 'card-the-next-day.mp4')
    c.beat('7', 'The next day', b15, 'Black. "The next day." Silence. Then scene C: Maddie on the step.')

    total = c.t
    for s_, e in ((b1, b2), (b3, b4), (b5, b9), (b11, b15)):
        c.sound('sfx-room', SFX / 'fs189231-crowd-shuffling.mp3', s_, 'bunker room tone', gain=-26, d=e - s_, fade=0.3)
    wind = M / 'cut3/A/stems/16-sfx-wind.wav'
    for s_, e in ((b2, b3), (b4, b5)):
        c.sound('sfx-wind', wind, s_, "wind on the downs (from scene A's wind stem)", gain=-4, d=e - s_, fade=0.3)
    for ln in lines.values():
        parts = ln.pop('_parts', [])
        if parts:
            ln['t'] = round(parts[0][0], 3)
            ln['dur'] = round(parts[-1][0] + parts[-1][1] - parts[0][0], 3)
    render(c, total, OUT3, f'gpom-3-B-bridge (rough, round {ROUND3})', ROUND3)


if __name__ == '__main__':
    rnd = sys.argv[sys.argv.index('--round') + 1] if '--round' in sys.argv else '1'
    if rnd in ('4', '5', '6'):
        ROUND3, OUT3 = int(rnd), M / f'cut3/B-bridge-r{rnd}'
    {'1': main, '2': main2, '3': main3, '4': main3, '5': main3, '6': main3}[rnd]()
