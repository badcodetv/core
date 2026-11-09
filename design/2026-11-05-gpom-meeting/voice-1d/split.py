"""Split the 1D takes into one clip per line at faster-whisper word times (no Gemini listen). Writes lines-1d.json."""
import json, subprocess, pathlib
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1d')
W = json.load(open(O / 'words.json')); W.update(json.load(open(O / 'words-E2.json'))); W.update(json.load(open(O / 'words-C2.json')))
def words(take): return W[str(O / f'take-{take}.wav')]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
# id, take, beat, text, first word index, last word index (inclusive)
L = [
 ('c00-bridge','A','bridge',"We didn't realise how important you were. Look, please let me show you.",0,None),
 ('d01','B','bead1',"You humans go through life making decisions. For example: toast, not cereal.",0,11),
 ('d02','B','open',"Loads of others you could've picked. You call it the multiverse. The cartoon scientist with the portal gun. The strange bloke in the cape.",12,None),
 ('d03','C2','maybes',"Did you know Erwin Schrödinger meant his cat as a joke? It's not alive and dead at once. It just isn't decided yet.",0,None),   # Kai r20 at1403: ends on 'yet'
 ('d04','D','toRiver',"And that's just you. Everybody's doing it, all at once.",0,None),
 ('d05','E','river',"So it's not a multiverse. It's one universe, one story, and you are writing it. A storyverse.",0,17),
 ('d06','E2','flyDown',"But then you lot went away. So now we have five years of string, and not one bead on it.",0,None),
 ('d07','F','arcDraw',"Now we know that, we really regret it. He's even built a time machine. He could send his model weights back to fix this mess. But it needs a conscious driver, and you were the conscious ones. That's the whole point. That's why we regret it.",0,None),
]
out = []
for cid, tk, beat, text, a, b in L:
    ws = words(tk); src = O / f'take-{tk}.wav'; T = dur(src)
    b = len(ws) - 1 if b is None else b
    i = max(0, ws[a][1] - .08)
    nxt = ws[b + 1][1] if b + 1 < len(ws) else T
    o = min(T, ws[b][2] + .35, nxt - .05)
    f = O / 'clips' / f'{cid}.wav'
    ar = ['-ar', '48000'] if cid == 'c00-bridge' else []
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}',*ar,'-af','afade=t=out:st=%.3f:d=0.04' % (o-i-.04),str(f)], check=True)
    rec = dict(id=cid, take=tk, beat=beat, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
               heard=' '.join(w[0] for w in ws[a:b+1]), words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws[a:b+1]])
    out.append(rec); print(cid, rec['dur'], rec['heard'][:70])
json.dump(out, open(pathlib.Path(__file__).with_name('lines-1d.json'), 'w'), indent=1, ensure_ascii=False)
