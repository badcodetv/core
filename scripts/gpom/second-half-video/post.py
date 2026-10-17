#!/usr/bin/env python3
"""Render the second half's post-only frames in ffmpeg: the camera layer the options gave to
Premiere or ffmpeg, so every frame has a clip before the edit (Kai, 17 Oct 2026).

What is NOT here yet, on purpose: on-screen text (HUD, waveform, voice tags, timestamps) and any
beacon pulse that must hit a spoken word. Both wait for the audio and the text pass.

Output matches the Omni clips: 1280x720, 24 fps, yuv420p, limited range tagged bt709, no audio.

    python3 scripts/gpom/second-half-video/post.py [key ...]
"""
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import shots as S  # noqa: E402

FPS = 24
ENC = ['-an', '-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
       '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
# 1376x768 stills -> 16:9 crop -> 1280x720, full-range JPEG converted to limited on the way.
FIT = 'crop=1365:768,scale=1280:720:in_range=full:out_range=limited:flags=lanczos'
GRAIN = 'noise=alls=7:allf=t'
# A hand-held camera at rest: two incommensurate sines per axis, about 6 px peak (camera-shake ~10).
SHAKE = ("scale=1344:756,crop=1280:720:x='32+5*sin(t*6.1)+3*sin(t*13.7)':y='18+4*sin(t*7.9)+2*sin(t*15.3)'")


def still(sid):
    return S.still_path(sid)


def ease(p):  # smoothstep on a clipped 0..1 expression, for zoompan
    q = f'clip({p},0,1)'
    return f'({q}*{q}*(3-2*{q}))'


def hold(sid, secs, extra=''):
    vf = f'{FIT},{SHAKE},{GRAIN}' + (f',{extra}' if extra else '')
    return ['-loop', '1', '-framerate', str(FPS), '-t', str(secs), '-i', still(sid), '-vf', vf]


def zoom(sid, secs, z0, z1, hold_in, move):
    n_in, n_mv = hold_in * FPS, move * FPS
    z = f'{z0}+({z1}-{z0})*{ease(f"(on-{n_in})/{n_mv}")}'
    # Upscale first so zoompan's integer crop steps are sub-pixel at output size (no stair-step jitter).
    vf = (f'{FIT},scale=3840:2160:flags=lanczos,zoompan=z=\'{z}\':x=\'iw/2-iw/zoom/2\':y=\'ih/2-ih/zoom/2\''
          f':d=1:s=1280x720:fps={FPS},{GRAIN}')
    return ['-loop', '1', '-framerate', str(FPS), '-t', str(secs), '-i', still(sid), '-vf', vf]


def chairs_light(secs=4):
    # Lit plate over a dimmed copy, revealed by a spiral key: outer chairs first, the hub last.
    # k = (angle + 3*(1-r)) / 4; a pixel is lit once the sweep T passes k. Then a slow 4-degree turn.
    t = f'clip((T-0.3)/3.0,0,1)'
    a = '(atan2(Y-H/2,X-W/2)+PI)/(2*PI)'
    r = 'min(hypot(X-W/2,Y-H/2)/(H*0.62),1)'
    alpha = f"255*clip(({t}-({a}+3*(1-{r}))/4)*25,0,1)"
    fc = (f"[0:v]{FIT},split[a][b];[a]eq=brightness=-0.28:contrast=0.75:gamma=0.85:saturation=0.6[dim];"
          f"[b]format=yuva420p,geq=lum='lum(X,Y)':cb='cb(X,Y)':cr='cr(X,Y)':a='{alpha}'[lit];"
          f"[dim][lit]overlay=format=auto,scale=1408:792,rotate=a='t/{secs}*4*PI/180':ow=1280:oh=720,{GRAIN}[v]")
    return ['-loop', '1', '-framerate', str(FPS), '-t', str(secs), '-i', still('L3-wafer-pattern'),
            '-filter_complex', fc, '-map', '[v]']


def beacon_fade(secs=6, cx=779, cy=264):
    # Pulses that slow down and weaken, then nothing: intervals 1.0, 1.2, 1.4, 1.7 s.
    pulses = [(0.4, 1.0), (1.4, 0.85), (2.6, 0.65), (4.0, 0.45), (5.7, 0.25)]
    i = '+'.join(f'{amp}*gt(T,{tk})*exp(-(T-{tk})*4)' for tk, amp in pulses)
    glow = f"255*min(1,({i})*exp(-((X-60)*(X-60)+(Y-60)*(Y-60))/(2*16*16)))"
    fc = (f"[0:v]{FIT},{SHAKE},{GRAIN}[base];"
          f"color=c=0xffb030:s=120x120:r={FPS}:d={secs},format=yuva420p,"
          f"geq=lum='lum(X,Y)':cb='cb(X,Y)':cr='cr(X,Y)':a='{glow}'[g];"
          f"[base][g]overlay=x={cx - 60}:y={cy - 60}:format=auto[v]")
    return ['-loop', '1', '-framerate', str(FPS), '-t', str(secs), '-i', still('SB25a'),
            '-filter_complex', fc, '-map', '[v]']


def cctv(src, secs=6):
    # The self-destruct replayed as the bunker's own security footage: grey, barrel, noise, scan lines, 12 fps.
    # Grey by hue=s=0 and explicit neutral chroma in geq: format=gray let garbage chroma back in (green/magenta).
    vf = ("hue=s=0,lenscorrection=k1=-0.22:k2=0.03,eq=contrast=1.25:brightness=0.02,"
          "noise=alls=22:allf=t,geq=lum='lum(X,Y)*(0.86+0.14*mod(Y,3)/2)':cb=128:cr=128,vignette=PI/4,fps=12,"
          f"fps={FPS},format=yuv420p")
    return ['-i', src, '-t', str(secs), '-vf', vf]


V = S.OUT
JOBS = {
    # 4: the sweep stops dead on the first ping; the waveform and tags come in the text pass.
    '04': hold('P1-pov-cctv-hud-voices', 3, 'noise=alls=14:allf=t'),
    # 11: held bot, the AI's words to come; the beacon pulse is keyed to them once the audio exists.
    '11': hold('SB11a', 9),
    # 13: the row carries on: the tail of 7's second speaker.
    '13': ['-ss', '5', '-i', str(V / 'sh-07-2-SB07c.mp4'), '-t', '3', '-vf', 'null'],
    # 16: the apology, a very slow push toward the bot over 10 s.
    '16': zoom('SBCANTa', 10, 1.0, 1.08, 1.5, 8),
    # 18a: the revolt line over the crowd (the other canteen angle); 18b: 12 replayed as CCTV.
    '18a': hold('SBCANTb', 2.5),
    '18b': cctv(str(V / 'sh-12-SB12a.mp4')),
    '21': hold('L5-bunny-suits', 2.5),
    # 23: tight on the wafer's colours, then the scale is given: 250% to 100%.
    '23': zoom('L9-wafer-portal', 5, 2.5, 1.0, 0.75, 4),
    '24': chairs_light(),
    '27': beacon_fade(),
}

if __name__ == '__main__':
    want = sys.argv[1:] or list(JOBS)
    for key in want:
        out = V / f'sh-{key}-post.mp4'
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', *JOBS[key], *ENC, str(out)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(key, 'ok' if r.returncode == 0 else 'FAIL ' + r.stderr[-400:], out.name)
