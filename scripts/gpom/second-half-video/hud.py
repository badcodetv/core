#!/usr/bin/env python3
"""The kill-bot HUD: one design, three states, built in ffmpeg so it is exact and reusable.

Kai's notes on cut 2 (20 Oct 2026): one HUD for the kill bots, the same layout before and after
kill mode (calm colour, then it flips red), with a LIVE sound meter drawn from the real muffled
row so it twitches on every word, and no freeze frames. Used in beats 3, 4, 8 and the new door
shot in beat 12 (kill -> peace at the door).

    hud.py IN.mp4 OUT.mp4 --state patrol|kill|peace|flip@SEC --audio ROW.wav [--lock@SEC]
           [--flip-to kill@SEC] [--flip-to peace@SEC] [--audio-at SEC] [--unit KB-07]
           [--no-audio-out] [--zoom 1.0]

  --state flip@3.2          shorthand for --state patrol --flip-to kill@3.2
  --state kill --flip-to peace@4.0   the stand-down at the door (green STAND DOWN)
  --flip-to may repeat: --state patrol --flip-to kill@2 --flip-to peace@6
  --lock@2.0 (or --lock 2.0)  'ORGANIC SIGNAL - LOCK' and the lock brackets appear at 2.0 s
  --audio-at 0.4            the wav starts 0.4 s into the clip (meter and output audio both)
  --no-audio-out            silent output (the meter still reads the wav)

The picture underneath keeps playing: the HUD is drawn over every frame and the clip is never
held. Output is the clip's own length, 1280x720, 24 fps, yuv420p, limited range tagged bt709 (the
same as post.py), with the wav muxed as AAC unless --no-audio-out.

What the layout does, all in one place below (LAYOUT): the dark panels sit exactly over where Veo
baked its own HUD text into sh-03 / sh-08 (top-left unit text, top-right AUDIO ON, the bottom
audio trace), so our live version replaces the baked one rather than fighting it.
"""
import argparse
import pathlib
import re
import subprocess
import sys
import tempfile

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
W, H, FPS = 1280, 720, 24
ENC = ['-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
       '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']

# State colour (HUD lines and text) and the picture grade under it. Change a look here, nowhere else.
STATES = {
    'patrol': dict(col='0x5EE6D0', grade='hue=s=0.18,colorchannelmixer=rr=0.82:gg=0.98:bb=1.0,eq=contrast=1.06',
                   mode='PATROL 07', status='SWEEP  //  NO CONTACT', banner='SCANNING'),
    'kill':   dict(col='0xFF3B2F', grade='hue=s=0,colorchannelmixer=rr=1.18:gg=0.36:bb=0.32,eq=contrast=1.12:brightness=0.02',
                   mode='KILL MODE', status='WEAPONS FREE', banner='KILL MODE ENGAGED'),
    'peace':  dict(col='0x46FF7E', grade='hue=s=0,colorchannelmixer=rr=0.42:gg=1.04:bb=0.55,eq=contrast=1.04',
                   mode='STAND DOWN', status='RETURN TO PATROL', banner='STAND DOWN'),  # Kai 21 Oct: not PEACE MODE
}

# LAYOUT (1280x720)
M, ARM, TH = 26, 74, 4                      # corner brackets: margin, arm length, thickness
TL = (52, 46, 610, 92)                      # top-left panel x, y, w, h (covers baked unit text)
TR = (1000, 46, 228, 50)                    # top-right panel (covers baked AUDIO ON)
MP = (300, 540, 680, 146)                   # meter panel (covers baked audio trace)
WAVE = (MP[0] + 14, MP[1] + 44, 452, 88)    # live waveform inside the meter panel
BARS = (MP[0] + 482, MP[1] + 44, 176, 88)   # live level bars (16 bands x 11 levels, 11x8 px cells)
CX, CY = W // 2, H // 2 - 10                # reticle centre
LOCK_Y = 172                                # lock label row (covers baked ORGANIC SIGNAL DETECTED)
BAN_Y = 452                                 # banner row (covers baked KILL MODE ENGAGED)


def parse():
    argv = []
    for a in sys.argv[1:]:  # accept --lock@2.0 and flip-to forms written with @
        m = re.fullmatch(r'--(lock|audio-at)@([\d.]+)', a)
        argv += [f'--{m.group(1)}', m.group(2)] if m else [a]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('inp')
    p.add_argument('out')
    p.add_argument('--state', default='patrol')
    p.add_argument('--flip-to', action='append', default=[])
    p.add_argument('--audio', required=True)
    p.add_argument('--audio-at', type=float, default=0.0)
    p.add_argument('--lock', type=float)
    p.add_argument('--unit', default='KB-07')
    p.add_argument('--zoom', type=float, default=1.0)
    p.add_argument('--no-audio-out', action='store_true')
    a = p.parse_args(argv)
    segs = []
    if a.state.startswith('flip@'):
        segs = [('patrol', 0.0), ('kill', float(a.state[5:]))]
    else:
        assert a.state in STATES, f'unknown state {a.state}'
        segs = [(a.state, 0.0)]
    for f in a.flip_to:
        s, t = f.split('@')
        assert s in STATES, f'unknown state {s}'
        segs.append((s, float(t)))
    segs.sort(key=lambda x: x[1])
    return a, segs


def probe_dur(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'csv=p=0', str(path)]).decode().strip())


def peak_db(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(path), '-af', 'volumedetect', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    m = re.search(r'max_volume: (-?[\d.]+) dB', r)
    return float(m.group(1)) if m else 0.0


class Text:
    """drawtext via textfile= so no label ever needs filtergraph escaping."""

    def __init__(self, tmp):
        self.tmp, self.n = pathlib.Path(tmp), 0

    def __call__(self, s, x, y, size, col, alpha=1.0, bold=False, enable=None, box=None):
        self.n += 1
        f = self.tmp / f't{self.n}.txt'
        f.write_text(s)
        o = (f"drawtext=fontfile={FONT_B if bold else FONT}:textfile={f}:x={x}:y={y}:fontsize={size}"
             f":fontcolor={col}@{alpha}:expansion=normal")
        if box:
            o += f':box=1:boxcolor={box}:boxborderw=10'
        if enable:
            o += f":enable='{enable}'"
        return o


def box(x, y, w, h, col, t='fill', enable=None):
    o = f'drawbox=x={x}:y={y}:w={w}:h={h}:color={col}:t={t}'
    return o + (f":enable='{enable}'" if enable else '')


def brackets(x, y, w, h, arm, th, col, enable=None):
    """Four L-shaped corners round a rectangle."""
    out = []
    for cx, cy, sx, sy in ((x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        hx = cx if sx > 0 else cx - arm
        vy = cy if sy > 0 else cy - arm
        out.append(box(hx, cy if sy > 0 else cy - th, arm, th, col, enable=enable))
        out.append(box(cx if sx > 0 else cx - th, vy, th, arm, col, enable=enable))
    return out


def hud(state, a, txt, lock_on):
    """Return the filter chain (list) that draws the HUD for one state, over a graded picture."""
    s = STATES[state]
    c = s['col']
    f = [s['grade'], 'drawgrid=w=iw:h=4:t=1:c=black@0.16', 'vignette=PI/4.2', 'noise=alls=6:allf=t']
    f += brackets(M, M, W - 2 * M, H - 2 * M, ARM, TH, f'{c}@0.95')
    # panels: dark, nearly opaque, so they hide what Veo baked in underneath
    for (x, y, w, h) in (TL, TR, MP):
        f.append(box(x, y, w, h, 'black@0.88'))
        f.append(box(x, y, w, h, f'{c}@0.55', t=2))
    # top-left: unit, mode, sector + a live clock
    f.append(txt(f'UNIT {a.unit}  //  {s["mode"]}', TL[0] + 14, TL[1] + 12, 28, c, bold=True))
    f.append(txt(f'SWN-04  //  {s["status"]}', TL[0] + 14, TL[1] + 54, 24, c, alpha=0.9))
    # top-right: audio live, with a blinking dot
    f.append(box(TR[0] + 16, TR[1] + 17, 16, 16, c, enable='lt(mod(t,1),0.6)'))
    f.append(txt('AUDIO  LIVE', TR[0] + 44, TR[1] + 11, 26, c, bold=True))
    # centre reticle: crosshair with a gap, dot, and range ticks
    g, L = 18, 34
    f += [box(CX - g - L, CY - 1, L, 3, f'{c}@0.9'), box(CX + g, CY - 1, L, 3, f'{c}@0.9'),
          box(CX - 1, CY - g - L, 3, L, f'{c}@0.9'), box(CX - 1, CY + g, 3, L, f'{c}@0.9'),
          box(CX - 2, CY - 2, 5, 5, c)]
    for i in range(-3, 4):  # horizon ticks
        if i:
            f.append(box(CX + i * 70 - 1, CY - 7, 3, 14, f'{c}@0.55'))
    # meter panel: label row (the waveform and bars are overlaid later, live from the wav)
    f.append(txt('AUDIO  //  SUBSURFACE  //  MUFFLED', MP[0] + 14, MP[1] + 12, 22, c, bold=True))
    f.append(txt('LVL', BARS[0] + BARS[2] - 44, MP[1] + 12, 22, c, bold=True))
    f.append(box(WAVE[0], WAVE[1] + WAVE[3] // 2, WAVE[2], 1, f'{c}@0.35'))  # zero line
    # the lock: brackets snap in (three sizes), label blinks for a second then holds
    # lock row and banner row: fixed-width boxes that are ALWAYS there, in every state, so the
    # layout never changes and they always hide the text Veo baked into sh-08
    LB, BB = (352, LOCK_Y - 12, 576, 56), (370, BAN_Y - 12, 540, 80)
    for (x, y, w, h) in (LB, BB):
        f.append(box(x, y, w, h, 'black@0.98'))
        f.append(box(x, y, w, h, f'{c}@0.6', t=2))
    T = lock_on if (lock_on is not None and state != 'peace') else None
    idle = 'NO TARGET' if state == 'peace' else 'SIGNAL SEARCH ...'
    f.append(txt(idle, '(w-text_w)/2', LOCK_Y, 32, c, alpha=0.55, enable=f'lt(t,{T})' if T is not None else None))
    if T is not None:
        # the lock: brackets snap in (three sizes), label blinks for a second then holds
        for sz, t0, t1 in ((180, T, T + 0.12), (130, T + 0.12, T + 0.24), (96, T + 0.24, 1e9)):
            f += brackets(CX - sz // 2, CY - sz // 2, sz, sz, 22, 3, c, enable=f'between(t,{t0},{t1})')
        en = f'gte(t,{T})*(gte(t,{T + 1})+lt(mod(t-{T},0.24),0.15))'
        label = 'ORGANIC SIGNAL — LOCK' if state == 'patrol' else 'ORGANIC SIGNAL — TARGET'
        f.append(txt(label, '(w-text_w)/2', LOCK_Y, 32, c, bold=True, enable=en))
        f.append(txt('BEARING 214   RANGE %{eif:max(40,1300-(t-' + str(T) + ')*60):d} M   HUMAN x2',
                     '(w-text_w)/2', LOCK_Y + 58, 22, c, alpha=0.9, enable=f'gte(t,{T})', box='black@0.7'))
    f.append(txt(s['banner'], '(w-text_w)/2', BAN_Y, 44, c, bold=True, alpha=0.6 if state == 'patrol' else 1.0))
    return f


def main():
    a, segs = parse()
    dur = probe_dur(a.inp)
    gain = -1.0 - peak_db(a.audio)  # meter only: peak-normalise so a quiet muffled row still fills it
    tmp = tempfile.mkdtemp(prefix='hud-')
    txt = Text(tmp)
    n = len(segs)
    delay = int(round(a.audio_at * 1000))
    fc = []
    zoom = f',scale={int(W * a.zoom)}:{int(H * a.zoom)},crop={W}:{H}' if a.zoom != 1.0 else ''
    fc.append(f'[0:v]scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1,format=rgb24{zoom},split={n}' +
              ''.join(f'[v{i}]' for i in range(n)))
    pad = f'adelay={delay}|{delay},apad,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS'
    fc.append(f'[1:a]aformat=channel_layouts=mono,{pad},volume={gain:.2f}dB,' + ('asplit=2[aw][ab]' if a.no_audio_out else 'asplit=3[aw][ab][ao]'))
    # live waveform: white on transparent, sqrt scale so speech reads big
    # (squashed hard so every word fills the box, then thickened: a meter, not a measurement)
    fc.append(f'[aw]volume=10dB,acompressor=threshold=0.06:ratio=5:attack=3:release=120:makeup=4,'
              f'alimiter=limit=0.95,showwaves=s={WAVE[2]}x{WAVE[3]}:mode=p2p:rate={FPS}:scale=sqrt:'
              f'draw=full:colors=white,format=gray,dilation,dilation=coordinates=24,split={n}' + ''.join(f'[w{i}]' for i in range(n)))
    # level bars: a 16-band spectrum of 0-600 Hz (the muffled row lives there), drawn tiny and
    # blown up with nearest-neighbour into LED cells, then a grid cuts the cells apart
    fc.append(f'[ab]aresample=1200,showfreqs=s=16x11:mode=bar:ascale=sqrt:fscale=lin:win_size=32:'
              f'colors=white,fps={FPS},scale={BARS[2]}:{BARS[3]}:flags=neighbor,format=gray,'
              f'drawgrid=w={BARS[2] // 16}:h=8:t=2:c=black,split={n}' + ''.join(f'[b{i}]' for i in range(n)))
    for i, (state, t0) in enumerate(segs):
        c = STATES[state]['col']
        chain = ','.join(hud(state, a, txt, a.lock))
        # tint = a plane of the state colour with the meter as its alpha
        fc.append(f'color=c={c}:s={WAVE[2]}x{WAVE[3]}:r={FPS}:d={dur:.3f},format=rgba[cw{i}];[cw{i}][w{i}]alphamerge[wt{i}]')
        fc.append(f'color=c={c}:s={BARS[2]}x{BARS[3]}:r={FPS}:d={dur:.3f},format=rgba[cb{i}];[cb{i}][b{i}]alphamerge[bt{i}]')
        fc.append(f'[v{i}]{chain}[h{i}]')
        fc.append(f'[h{i}][wt{i}]overlay={WAVE[0]}:{WAVE[1]}:format=auto[hw{i}]')
        fc.append(f'[hw{i}][bt{i}]overlay={BARS[0]}:{BARS[1]}:format=auto[s{i}]')
    last = 's0'
    for i in range(1, n):
        t = segs[i][1]
        fc.append(f"[{last}][s{i}]overlay=0:0:enable='gte(t,{t})'[m{i}]")
        last = f'm{i}'
    # the flip: two frames of white, then a short tear (rows shoved sideways) so the switch hits
    flashes = []
    for state, t in segs[1:]:
        flashes.append(box(0, 0, W, H, 'white@0.55', enable=f'between(t,{t},{t + 1 / FPS})'))
        flashes.append(box(0, 0, W, H, f'{STATES[state]["col"]}@0.35', enable=f'between(t,{t + 1 / FPS},{t + 3 / FPS})'))
    fc.append(f'[{last}]' + (','.join(flashes) + ',' if flashes else '') + 'format=yuv420p[vout]')
    script = pathlib.Path(tmp) / 'graph.txt'
    script.write_text(';\n'.join(fc))
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', a.inp, '-i', a.audio, '-filter_complex_script', str(script),
           '-map', '[vout]']
    if a.no_audio_out:
        cmd += ['-an']
    else:
        # output audio: the wav at its true level, placed at --audio-at, clip length
        script.write_text(';\n'.join(fc) + f';\n[ao]volume={-gain:.2f}dB,aresample=48000[aout]')
        cmd += ['-map', '[aout]', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000']
    cmd += ENC + ['-t', f'{dur:.3f}', a.out]
    pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True)
    print(a.out)


if __name__ == '__main__':
    main()
