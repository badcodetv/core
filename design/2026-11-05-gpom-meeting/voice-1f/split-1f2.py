"""1F2 (Kai's timeline note, 10 Nov): b02 is cut; the hologram opens on the materialist stack, voiced as three new lines s01-s03.
Cuts the picked takes into clips/s01..s03.wav at faster-whisper word times (no Gemini listen), cards each (parent = the take),
and writes lines-1f2.json = the 1F record minus b02, plus s01-s03 (f01..f07b reused untouched, not re-voiced).
Takes (check.py on words-s.json / words-s2.json): s01-3 (the brisk one; whisper writes 'Societies made' for the homophone
'Society's made', every other word exact; s01-1 is the strictly-exact but 2.5 s slower backup), s02-1, s03-2."""
import json, subprocess, pathlib
H = pathlib.Path(__file__).parent; ROOT = H.parents[2]
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f')
W = {}
for j in ['words-s.json', 'words-s2.json']: W.update(json.load(open(O / j)))
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
NEW = [
 ('s01', 's01-3', 'stack', "[brisk; the stack, the camera descending, each layer landing on its word] Right. This is how you lot saw the world. Society's made of people. People are made of cells. Cells are chemistry. Chemistry's atoms. Atoms are quarks and leptons. And under all that… the maths."),
 ('s02', 's02-1', 'stackBack', "[pull back: the whole stack; beside it an empty outlined slot] Every bit of it's real. But we've worked out there's something missing."),
 ('s03', 's03-2', 'slot', "[the slot lights up warm] Consciousness. Yours. It's as fundamental as quarks and leptons."),
]
old = [l for l in json.load(open(H / 'lines-1f.json')) if l['id'] != 'b02']
out = []
for cid, tk, beat, text in NEW:
    src = O / f'take-{tk}.wav'; ws = W[str(src)]; TT = dur(src)
    i = max(0, ws[0][1] - .08); o = min(TT, ws[-1][2] + .35)
    f = O / 'clips' / f'{cid}.wav'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}','-af','afade=t=out:st=%.3f:d=0.04' % (o-i-.04),str(f)], check=True)
    heard = ' '.join(w[0] for w in ws)
    rec = dict(id=cid, take=tk, beat=beat, street=False, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
               heard=heard, words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws])
    out.append(rec); print(cid, rec['dur'], heard)
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice', '--engine', 'gemini-tts',
                    '--tool', 'design/2026-11-05-gpom-meeting/voice-1f/split-1f2.py (ffmpeg cut at faster-whisper word times)', '--parent', str(src),
                    '--why', f'hologram 1F2 line {cid}: the materialist stack opening (Kai timeline note, 10 Nov); take picked as whisper-verbatim',
                    '--prompt', text, '--input', f'heard={heard}', '--input', 'record=design/2026-11-05-gpom-meeting/voice-1f/lines-1f2.json',
                    '--setting', f'src_in={i:.2f}', '--setting', f'src_out={o:.2f}'], check=True)
# b01 (street) first, then the hologram in order: s01-s03, f01..f07a, then f07b (street)
recs = [old[0]] + out + old[1:]
json.dump(recs, open(H / 'lines-1f2.json', 'w'), indent=1, ensure_ascii=False)
print([r['id'] for r in recs])
