"""1F2 (copied from the 1F finish.py; only the beads version is rendered, so `finish.py beads` now also writes edit.json and voice.wav). After record.mjs: voice.wav (the hologram lines at their starts), edit.json, the 24 fps picture mp4, the contact sheet, recipe cards.
`finish.py beads` = the render with the bead stills (record.mjs --media bead-media-1f2.json into frames-beads/): picture + contact sheet only."""
import json, subprocess, pathlib, sys
BEADS = sys.argv[1:] == ['beads']; TAG = '-beads' if BEADS else ''; FR = 'frames-beads' if BEADS else 'frames'
H = pathlib.Path(__file__).parent; ROOT = H.parents[1]
R = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f2-24')
E = json.load(open(H / 'edit-1f2.json')); TD = E['marks']['TD']
L = {l['id']: l for l in json.load(open(ROOT / 'design/2026-11-05-gpom-meeting/voice-1f/lines-1f2.json'))}
(R / 'edit.json').write_text(json.dumps(E, indent=1, ensure_ascii=False))
# voice: every hologram clip placed at its start on the hologram clock (48 kHz stereo, TD long)
ids = list(E['clips']); ins = sum([['-i', L[k]['file']] for k in ids], [])
fl = ';'.join(f"[{i}]aresample=48000,adelay={int(E['clips'][k]['start']*1000)}:all=1[a{i}]" for i, k in enumerate(ids))
fl += ';' + ''.join(f'[a{i}]' for i in range(len(ids))) + f'amix=inputs={len(ids)}:normalize=0,apad,atrim=0:{TD:.3f}[o]'
vw = R / 'hologram-1f2-24fps-voice.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', fl, '-map', '[o]', '-ac', '2', '-ar', '48000', str(vw)], check=True)
pic = R / f'hologram-1f2{TAG}-24fps-picture.mp4'
if not pic.exists(): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '24', '-i', str(R / FR / '%05d.jpg'), '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', str(pic)], check=True)
both = R / 'hologram-1f2-24fps.mp4'
if not BEADS: subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(pic), '-i', str(vw), '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', str(both)], check=True)
# contact sheet: the moments that must land, each labelled with its time and word
m = E['marks']; st = E['clips']
def at(cid, word, d=0):
    return st[cid]['start'] + next(x[1] for x in L[cid]['words'] if x[0].lower().startswith(word)) + d
SK = E['stack']
K = [(.9, 'opening: the empty shelves'), *[(t + .45, n.lower() + ': lands') for n, t in zip(SK['labels'][:5], SK['lay'][:5])], (SK['quarks'] + .55, 'quarks: standard model'), (SK['leptons'] + .5, 'leptons light'),
     (SK['lay'][5] + .45, 'mathematics: lands'), (SK['s02'] + 2.5, 'every bit of it: whole stack'), (SK['missing'] + .5, 'something missing: slot'), (SK['consc'] + .5, 'CONSCIOUSNESS: slot lights'),
     (SK['depart'] + 1.2, 'the light drops'), (m['light_lands'] + .5, 'lands at bead 1'),
     (m['toast'] + .3, 'toast: bead 1'), (m['sorry'] + .3, 'sorry: bead 2'), (m['married'] + .3, 'married: bead 3'), (at('f03', 'qualia', .3), 'qualia: glow'),
     (m['cloud_blooms'] + .8, 'multiverse: bloom'), (sum(E['exc'][0]) / 2, 'visit 1'), (sum(E['exc'][1]) / 2, 'visit 2'), (sum(E['exc'][2]) / 2, 'visit 3'),
     (m['yet_flash'] - .25, 'just before yet'), (m['yet_flash'] + .1, 'YET: flash'), (m['yet_flash'] + 1.0, 'collapse'), (at('f05', 'story', .3), 'storyverse: river'),
     (at('f05', 'writing'), 'writing it'), (m['arrive_side_view'], 'realise: side view'), (at('f06', 'training', .2), 'training data'), (m['arc_draws'] - .3, 'just before go back'),
     (m['arc_draws'] + .4, 'GO BACK: arc draws'), (m['arc_draws'] + 2.6, 'arc drawn'), (m['screen_off'] - .2, 'hold'), (m['screen_off'] + .5, 'screen off')]
tiles = []
for i, (t, lab) in enumerate(K):
    f = R / FR / f'{round(t * 24):05d}.jpg'; o = R / f'_c{i:02d}.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f), '-vf', f"scale=480:-1,drawtext=text='{t:.2f}s  {lab.replace(":", " -")}':fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6:x=8:y=8", str(o)], check=True); tiles.append(o)
cs = R / f'contact-1f2{TAG}.jpg'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', str(t)] for t in tiles], []), '-filter_complex', ''.join(f'[{i}]' for i in range(len(tiles))) + f'xstack=inputs={len(tiles)}:layout=' + '|'.join(f'{(i%4)*480}_{(i//4)*270}' for i in range(len(tiles))), str(cs)], check=True)
for t in tiles: t.unlink()
# recipe cards
why = "hologram 1F2 (Kai timeline note 10 Nov: b02 cut; opens on the materialist stack, each layer on its word, the empty slot lights warm on 'Consciousness' and its light drops into bead 1), then as 1F: toast/sorry/married beads on their words, glow under qualia, bloom on 'multiverse', flash on 'yet', side view on 'realise', arc on 'go back'"
P = ['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card']
common = ['--why', why, '--input', 'page=design/2026-11-10-gpom-hologram-1f2/index.html', '--input', 'builder=design/2026-11-10-gpom-hologram-1f2/make.py',
          '--input', 'voice=design/2026-11-05-gpom-meeting/voice-1f/lines-1f2.json', '--input', 'stack=design/2026-11-10-gpom-hologram-1f2/stack.js', '--setting', 'fps=24', '--setting', 'size=1920x1080', '--setting', f'timing={R / "edit.json"}']
media = ['--setting', 'bead_media=design/2026-11-10-gpom-hologram-1f2/bead-media-1f2.json', '--input', 'derek=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/derek-a.jpg', '--input', 'sandra=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/sandra-a.jpg', '--input', 'wedding=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/wedding-a.jpg'] if BEADS else ['--setting', 'bead_media=none']
subprocess.run(P + [str(pic), '--kind', 'video', '--engine', 'three.js', '--tool', 'design/2026-11-10-gpom-hologram-1f2/record.mjs (headless Chrome, window.hologram.frameAt) + ffmpeg x264, 24 fps', *common, *media], check=True)
if BEADS:
    subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f2/finish.py (ffmpeg adelay+amix)', '--parent', str(L['s01']['file']), *common], check=True)
    subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f2/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True); print('beads', pic, cs); sys.exit()
subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f2/finish.py (ffmpeg adelay+amix)', '--parent', str(L['f01']['file']), *common], check=True)
subprocess.run(P + [str(both), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f2/finish.py (ffmpeg mux)', '--parent', str(pic), *common], check=True)
subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', 'design/2026-11-10-gpom-hologram-1f2/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True)
print('TD', TD, 'voice', vw, 'pic', pic)
