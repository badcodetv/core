"""Split the 1F takes into one clip per line at faster-whisper word times (no Gemini listen). Writes lines-1f.json.
Takes picked by check.py (whisper verbatim, no dead gap over 2 s): b01-4, b02-3, f03-2, f05-3; f07 re-voiced as two paragraphs (f07p-1) so 'we would.' lands as a full stop; the rest first take."""
import json, subprocess, pathlib
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f')
W = {}
for j in ['words.json', 'words-2.json', 'words-3.json', 'words-4.json']: W.update(json.load(open(O / j)))
def words(take): return W[str(O / f'take-{take}.wav')]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
S = json.load(open(pathlib.Path(__file__).parents[3] / 'docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/script.json'))
T = {l['id']: l['text'] for l in S['lines'] if 'id' in l}
f07b_at = next(i for i, w in enumerate(words('f07p-1')) if w[0].lower().startswith('but'))
# id, take, beat, script text (with its [direction]), first word index, last word index (inclusive), street?
L = [
 ('b01', 'b01-4', 'street', T['b01'], 0, None, True),
 ('b02', 'b02-3', 'street', T['b02'], 0, None, True),
 ('f01', 'f01',   'bead1',  T['f01'], 0, None, False),
 ('f02', 'f02',   'bead2',  T['f02'], 0, None, False),
 ('f03', 'f03-2', 'bead3',  T['f03'], 0, None, False),
 ('f04', 'f04',   'maybes', T['f04'], 0, None, False),
 ('f05', 'f05-3', 'river',  T['f05'], 0, None, False),
 ('f06', 'f06',   'flyDown',T['f06'], 0, None, False),
 ('f07a','f07p-1',  'arcDraw',"Anyway, if we could go back and fix it, we would.", 0, f07b_at - 1, False),
 ('f07b','f07p-1',  'street', "But the patrol's out. Please, mind how you go.", f07b_at, None, True),
]
out = []
for cid, tk, beat, text, a, b, street in L:
    ws = words(tk); src = O / f'take-{tk}.wav'; TT = dur(src)
    b = len(ws) - 1 if b is None else b
    prv = ws[a - 1][2] if a > 0 else 0
    i = max(0, prv + .05, ws[a][1] - .08)
    nxt = ws[b + 1][1] if b + 1 < len(ws) else TT
    o = min(TT, ws[b][2] + .35, nxt - .05)
    f = O / 'clips' / f'{cid}.wav'
    ar = ['-ar', '48000'] if street else []
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}',*ar,'-af','afade=t=out:st=%.3f:d=0.04' % (o-i-.04),str(f)], check=True)
    rec = dict(id=cid, take=tk, beat=beat, street=street, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
               heard=' '.join(w[0] for w in ws[a:b+1]), words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws[a:b+1]])
    out.append(rec); print(cid, rec['dur'], rec['heard'][:90])
json.dump(out, open(pathlib.Path(__file__).with_name('lines-1f.json'), 'w'), indent=1, ensure_ascii=False)
