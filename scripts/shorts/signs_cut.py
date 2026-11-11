#!/usr/bin/env python3
"""Signs (BadCode Short #33): rough cut (2026-11-11).

    python3 scripts/shorts/signs_cut.py

9:16, no words. A: the street of signs, the green bin goes out (01, slow push). B: the lid, a glow switches on under it
(02, hard push into the lid). C: inside the bin looking up: the real BadCode stacked logo flickers on in the lid's panel
with a glow (03 + docs/brand/logo/badcode-stacked-reversed-2400.png, composited here, never drawn by Flow).
A1 = each clip's own Omni sound (checked for speech), A2 = the neon hum and click under the logo (ffmpeg synth).
Writes <media>/cut/edl.json (timeline format, scripts/scene/timeline.py), stems, overlay.mov and preview.mp4.
"""
# style-lint: story=short-signs (this cut script belongs to one short)
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-signs/scenes/signs'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID = MEDIA / 'video'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
SFX_LUFS = -30

# (beat, clip, in, dur, zoom_to, focus_x, focus_y): the push is eased from 1.0 to zoom_to toward (focus_x, focus_y) of the frame
SHOTS = [('street', 'sg-01-ST1-a.mp4', 0.0, 4.5, 1.08, 0.62, 0.55),
         ('lid', 'sg-02-LD2-b-a.mp4', 1.0, 3.0, 1.9, 0.62, 0.62),
         ('inside', 'sg-03-IN1-b.mp4', 0.5, 4.5, 1.0, 0.5, 0.5)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
TOTAL = round(t, 3)
# The logo in the lid's square panel (measured on 03 at 1080x1920: x 378-718, y 632-972)
PANEL_CX, PANEL_CY, LOGO_H = 548, 802, 290
T_ON = starts[2] + 1.0                                   # flickers on 1 s into the inside shot
FLICKER = f"between(t,{T_ON:.2f},{T_ON + 0.08:.2f})+between(t,{T_ON + 0.22:.2f},{T_ON + 0.27:.2f})+gte(t,{T_ON + 0.4:.2f})"
SEE = {'street': 'Dusk, a terrace with every party\'s sign out front; the green bin goes out to the kerb.',
       'lid': 'The green bin at the kerb; a cool glow switches on under its lid; push in.',
       'inside': 'Inside the bin, looking up: the BadCode logo and name flicker on in the lid.'}
TITLES = {'street': 'A. The street of signs', 'lid': 'B. Into the bin', 'inside': 'C. Inside, looking up'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    parts, sfx = [], []
    for i, (beat, clip, tin, d, z, fx, fy) in enumerate(SHOTS):
        n = int(round(d * FPS))
        # eased push (smoothstep) done in ffmpeg for the rough; Premiere redoes it as a Scale keyframe pair
        zexpr = f"1+({z}-1)*(3*pow(on/{n},2)-2*pow(on/{n},3))"
        out = CUT / f'v{i}-{beat}.mp4'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
           f"zoompan=z='{zexpr}':x='{fx}*iw-iw/zoom/2':y='{fy}*ih-ih/zoom/2':d=1:s={W}x{H}:fps={FPS},"
           'scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
        parts.append(out)
        sp = CUT / f's{i}-{beat}.wav'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-vn', '-af',
           f'loudnorm=I={SFX_LUFS}:TP=-6,afade=t=in:d=0.08,afade=t=out:st={d - 0.08}:d=0.08', '-ar', 48000, '-ac', 2, sp)
        sfx.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture-raw.mp4')

    # The logo: white ring + red triangle + name, with a soft glow behind, flickering on like a sign warming up.
    lw = int(LOGO_H * 2400 / 3008)
    x, y = PANEL_CX - lw // 2, PANEL_CY - LOGO_H // 2
    logo_fc = (f"[1]scale={lw}:{LOGO_H},format=rgba,split[lg][lb];"
               f"[lb]pad={lw + 160}:{LOGO_H + 160}:80:80:color=black@0,gblur=sigma=22,colorchannelmixer=aa=0.85[glow]")
    ff('-i', CUT / 'picture-raw.mp4', '-i', LOGO, '-filter_complex',
       logo_fc + f";[0][glow]overlay={x - 80}:{y - 80}:enable='{FLICKER}'[g];[g][lg]overlay={x}:{y}:enable='{FLICKER}',"
       'scale=in_range=full:out_range=limited,format=yuv420p[v]', '-map', '[v]', *ENC, CUT / 'picture.mp4')
    ff('-f', 'lavfi', '-i', f'color=c=black@0.0:s={W}x{H}:r={FPS}:d={TOTAL},format=rgba', '-i', LOGO, '-filter_complex',
       logo_fc + f";[0][glow]overlay={x - 80}:{y - 80}:format=auto:enable='{FLICKER}'[g];[g][lg]overlay={x}:{y}:format=auto:enable='{FLICKER}'[o]",
       '-map', '[o]', '-t', TOTAL, '-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '16', CUT / 'overlay.mov')

    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in sfx))
    world = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, world)
    # Neon: a 100 Hz hum with harmonics and a slow wobble, a click on each flicker, from T_ON to the end.
    hum = CUT / 'sfx-neon.wav'
    dur = TOTAL - T_ON
    ff('-f', 'lavfi', '-i', f"aevalsrc='0.5*sin(2*PI*100*t)+0.25*sin(2*PI*200*t)+0.12*sin(2*PI*300*t)+0.05*sin(2*PI*1200*t)':s=48000:d={dur}",
       '-f', 'lavfi', '-i', f"aevalsrc='(lt(mod(t,0.22),0.012))*0.9*sin(2*PI*2500*t)':s=48000:d=0.45",
       '-filter_complex',
       f"[0]tremolo=f=6:d=0.15,afade=t=in:d=0.4,volume='if(lt(t,0.4),gt(mod(t,0.22),0.1),1)':eval=frame[h];[h][1]amix=inputs=2:normalize=0,"
       f"loudnorm=I=-28:TP=-6,adelay=delays={int(T_ON * 1000)}:all=1,apad=whole_dur={TOTAL}", '-ar', 48000, '-ac', 2, hum)
    ff('-i', CUT / 'picture.mp4', '-i', world, '-i', hum, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    notes = SCENE / 'cut-notes.json'
    rnd = json.loads(notes.read_text()).get('round', 1) if notes.exists() else 1
    beats = [{'id': s[0], 'title': TITLES[s[0]], 'start': starts[i], 'dur': s[3], 'see': SEE[s[0]], 'lines': []} for i, s in enumerate(SHOTS)]
    edl = {'sequence': f'shorts-33-signs-r{rnd}', 'title': 'Signs Timeline',
           'heading': f'BadCode Shorts ▲ Signs, rough cut {rnd}',
           'intro': 'The three picked shots with the pushes, the real BadCode logo flickering on in the lid, the street sound and a neon hum. No words. Note anything: a beat, a shot, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / s[1]), 'in': s[2], 'start': starts[i], 'dur': s[3], 'beat': s[0], 'source': str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'sfx-world', 'file': str(world)}, {'track': 'A2', 'name': 'sfx-neon', 'file': str(hum)}],
           'events': [{'stem': 'sfx-world', 't': starts[i], 'dur': s[3], 'what': f"{s[0]}: clip's own sound", 'src': str(VID / s[1])} for i, s in enumerate(SHOTS)]
                     + [{'stem': 'sfx-neon', 't': round(T_ON, 2), 'dur': round(dur, 2), 'what': 'neon hum + flicker clicks as the logo lights', 'src': str(hum)}],
           'flags': ['The pushes are ffmpeg stand-ins; in Premiere they become eased Scale keyframes.',
                     'No music (sound.md is empty).']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'logo_on': T_ON, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
