"""1F3 (copied from the 1F2 finish.py; only the beads version is rendered, so `finish.py beads` now also writes edit.json and voice.wav). After record.mjs: voice.wav (the hologram lines at their starts), edit.json, the 24 fps picture mp4, the contact sheet, recipe cards.
`finish.py beads` = the render with the bead stills (record.mjs --media bead-media-1f3.json into frames-beads/): picture + contact sheet only."""
import json, subprocess, pathlib, sys
BEADS = sys.argv[1:] == ['beads']; TAG = '-beads' if BEADS else ''; FR = 'frames-beads' if BEADS else 'frames'
H = pathlib.Path(__file__).parent; ROOT = H.parents[1]
R = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f3-24')
E = json.load(open(H / 'edit-1f3.json')); TD = E['marks']['TD']
L = {l['id']: l for l in json.load(open(ROOT / 'design/2026-11-05-gpom-meeting/voice-1f/lines-1f3.json'))}
(R / 'edit.json').write_text(json.dumps(E, indent=1, ensure_ascii=False))
# voice: every hologram clip placed at its start on the hologram clock (48 kHz stereo, TD long)
ids = list(E['clips']); ins = sum([['-i', L[k]['file']] for k in ids], [])
fl = ';'.join(f"[{i}]aresample=48000,adelay={int(E['clips'][k]['start']*1000)}:all=1[a{i}]" for i, k in enumerate(ids))
fl += ';' + ''.join(f'[a{i}]' for i in range(len(ids))) + f'amix=inputs={len(ids)}:normalize=0,apad,atrim=0:{TD:.3f}[o]'
vw = R / 'hologram-1f3-24fps-voice.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', fl, '-map', '[o]', '-ac', '2', '-ar', '48000', str(vw)], check=True)
pic = R / f'hologram-1f3{TAG}-24fps-picture.mp4'
if not pic.exists(): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '24', '-i', str(R / FR / '%05d.jpg'), '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', str(pic)], check=True)
both = R / 'hologram-1f3-24fps.mp4'
if not BEADS: subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(pic), '-i', str(vw), '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', str(both)], check=True)
# contact sheet: the moments that must land, each labelled with its time and word
m = E['marks']; st = E['clips']
def at(cid, word, d=0, n=0):
    return st[cid]['start'] + [x[1] for x in L[cid]['words'] if x[0].lower().startswith(word)][n] + d
SK = E['stack']
K = [(.9, 'opening: outlines before fill'), *[(t + .45, n.lower() + ': lands') for n, t in zip(SK['labels'][:5], SK['lay'][:5])], (SK['quarks'] + .55, 'quarks: standard model'),
     (SK['lay'][5] + .45, 'mathematics: lands'), (SK['missing'] + .5, 'something missing: slot'), (SK['consc'] + .5, 'CONSCIOUSNESS: slot lights'), (m['light_lands'] + .5, 'lands at bead 1'),
     (m['toast'] + .3, 'toast: bead 1'), (m['sorry'] + .3, 'sorry: bead 2'), (m['married'] + .3, 'married: bead 3'), (at('f03', 'qualia', .3), 'qualia: glow'),
     (m['cloud_blooms'] + .8, 'multiverse: bloom'), (at('f04', 'real', .2), 'real distraction: no zoom'), (m['did_you_know'] + .05, 'DID YOU KNOW: zoom starts'), (m['cat_alive'], 'cat alive'),
     (E['exc'][0][1] + .05, 'out'), (m['cat_dead'], 'cat dead'), (m['yet_flash'] - .25, 'just before yet'), (m['yet_flash'] + .1, 'YET: flash'), (m['yet_flash'] + 1.0, 'collapse'),
     (m['one_timeline_f04b'] + 1.5, 'f04b: one timeline'), (m['one_timeline_f04b'] + 6, 'f04b: settle'), (m['to_river'] + 1.5, 'all of you: river'), (at('f05', 'each', .2), 'each of you: inside'),
     (at('f05', 'story', .3, 1), 'story of history'), (m['leave_river'] + 1.2, 'leaving the river'), (m['arrive_square_on'] + .2, 'SQUARE-ON: rests'), (m['rise'] - .3, 'f07a: before the rise'),
     (m['rise'] + 1.6, 'time machine: RISING'), (m['arc_draws'] + 1.2, 'go back: arc draws'), (m['arc_draws'] + 3.0, 'arc drawn'), (m['screen_off'] + .5, 'screen off')]
tiles = []
for i, (t, lab) in enumerate(K):
    f = R / FR / f'{round(t * 24):05d}.jpg'; o = R / f'_c{i:02d}.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f), '-vf', f"scale=480:-1,drawtext=text='{t:.2f}s  {lab.replace(":", " -")}':fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6:x=8:y=8", str(o)], check=True); tiles.append(o)
cs = R / f'contact-1f3{TAG}.jpg'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', str(t)] for t in tiles], []), '-filter_complex', ''.join(f'[{i}]' for i in range(len(tiles))) + f'xstack=inputs={len(tiles)}:layout=' + '|'.join(f'{(i%4)*480}_{(i//4)*270}' for i in range(len(tiles))), str(cs)], check=True)
for t in tiles: t.unlink()
# recipe cards
why = "hologram 1F3 (Kai round 23 timeline notes, 10 Nov): new f01/f03/f05/f07a words, f02 re-voiced, f04b added; brighter stack outlines, a real INDIVIDUAL figure, no blur artefacts in the cloud, two cat nodes visited alive then dead from Did you know, the one string under f04b, into the river sooner, one square-on resting view that rises for the time machine; f06 " + ("PLACEHOLDER (the 1F2 clip)" if E.get("placeholder") else "final")
P = ['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card']
common = ['--why', why, '--input', 'page=design/2026-11-10-gpom-hologram-1f3/index.html', '--input', 'builder=design/2026-11-10-gpom-hologram-1f3/make.py',
          '--input', 'voice=design/2026-11-05-gpom-meeting/voice-1f/lines-1f3.json', '--input', 'stack=design/2026-11-10-gpom-hologram-1f3/stack.js', '--setting', 'fps=24', '--setting', 'size=1920x1080', '--setting', f'timing={R / "edit.json"}']
media = ['--setting', 'bead_media=design/2026-11-10-gpom-hologram-1f3/bead-media-1f3.json', '--input', 'derek=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/derek-a.jpg', '--input', 'sandra=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/sandra-a.jpg', '--input', 'wedding=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/wedding-a.jpg', *sum([['--input', f'cat{k[1]}=' + str((H / v['src']).resolve())] for k, v in json.load(open(H / 'bead-media-1f3.json')).items() if k.startswith('c')], [])] if BEADS else ['--setting', 'bead_media=none']
subprocess.run(P + [str(pic), '--kind', 'video', '--engine', 'three.js', '--tool', 'design/2026-11-10-gpom-hologram-1f3/record.mjs (headless Chrome, window.hologram.frameAt) + ffmpeg x264, 24 fps', *common, *media], check=True)
if BEADS:
    subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f3/finish.py (ffmpeg adelay+amix)', '--parent', str(L['s01']['file']), *common], check=True)
    subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f3/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True); print('beads', pic, cs); sys.exit()
subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f3/finish.py (ffmpeg adelay+amix)', '--parent', str(L['f01']['file']), *common], check=True)
subprocess.run(P + [str(both), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f3/finish.py (ffmpeg mux)', '--parent', str(pic), *common], check=True)
subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f3/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True)
print('TD', TD, 'voice', vw, 'pic', pic)
