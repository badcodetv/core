"""1F3 (Kai's round 23 timeline notes, 10 Nov): new words for f01, f03, f05, f07a; f02 re-voiced whole with "They got married!" excited;
a new line f04b after f04. Cuts the picked takes into clips-1f3/<id>.wav at faster-whisper word times (no Gemini listen), cards each
(parent = the take), links the unchanged clips (s01-s03, f04, f06 placeholder, f07b) beside them, and writes lines-1f3.json.
Text = script.json (docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/script.json) with [stage directions] stripped.
Takes (check-1f3.py on words-1f3.json / words-1f3b.json): f01n-1, f02n-4 (pyin: 'sorry' half soft at 173 Hz, 'They got married!'
+9 dB and well up in pitch; f02n-3 is the calmer backup), f03n-1, f04b-1, f05n-1 (whisper splits 'story verse', as 1F2's accepted
f05-3 did; every other word exact; n-2..n-4 also mishear 'writing'), f07an-1 (f07an-2 rushed at 3.4 w/s).
f06 = Kai's pick 1C, voiced 10 Nov: F06_TAKE=f06n-2 (take-f06n.txt, [sarcastic] on the last two sentences; whisper writes 'd'you' as 'do you',
every other word exact, 19.3 s of speech, no gap over 1.2 s; n-1/n-3 slower, f06p-1 untagged and mishears 'selfless')."""
import json, subprocess, pathlib, os
H = pathlib.Path(__file__).parent; ROOT = H.parents[2]
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f'); C = O / 'clips-1f3'; C.mkdir(exist_ok=True)
W = {}
for j in ['words-1f3.json', 'words-1f3b.json', 'words-1f3-f06.json']:
    if (O / j).exists(): W.update(json.load(open(O / j)))
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
S = json.load(open(ROOT / 'docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/script.json'))
T = {l['id']: l['text'] for l in S['lines'] if 'id' in l}
NEW = [('f01', 'f01n-1', 'bead1', T['f01']), ('f02', 'f02n-4', 'bead2', T['f02']), ('f03', 'f03n-1', 'bead3', T['f03']),
       ('f04b', 'f04b-1', 'settle', "[back on the one timeline] And as you make your decisions and write your story, all those maybes settle into what really happens."),
       ('f05', 'f05n-1', 'river', T['f05']),
       ('f07a', 'f07an-1', 'arcDraw', "[the camera rises; the arc draws in] My boss has been hard at work building a time machine, so he could go back and fix all this. Problem is, it takes consciousness to drive it. And that all went away with you.")]
F06 = os.environ.get('F06_TAKE')   # set when the final f06 is voiced, e.g. F06_TAKE=f06n-1
if F06: NEW.append(('f06', F06, 'flyDown', T['f06']))
old = {l['id']: l for l in json.load(open(H / 'lines-1f2.json'))}
new = {}
for cid, tk, beat, text in NEW:
    src = O / f'take-{tk}.wav'; ws = W[str(src)]; TT = dur(src)
    i = max(0, ws[0][1] - .08); o = min(TT, ws[-1][2] + .35)
    f = C / f'{cid}.wav'
    if f.is_symlink(): f.unlink()   # a linked unchanged clip being replaced: never write through the link into clips/
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}','-af','afade=t=out:st=%.3f:d=0.04' % (o-i-.04),str(f)], check=True)
    heard = ' '.join(w[0] for w in ws)
    new[cid] = dict(id=cid, take=tk, beat=beat, street=False, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
                    heard=heard, words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws])
    print(cid, new[cid]['dur'], heard)
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice', '--engine', 'gemini-tts',
                    '--tool', 'design/2026-11-05-gpom-meeting/voice-1f/split-1f3.py (ffmpeg cut at faster-whisper word times)', '--parent', str(src),
                    '--why', f'hologram 1F3 line {cid} (Kai round 23 timeline notes, 10 Nov); take picked as whisper-verbatim, no dead air',
                    '--prompt', text, '--input', f'heard={heard}', '--input', 'record=design/2026-11-05-gpom-meeting/voice-1f/lines-1f3.json',
                    '--setting', f'src_in={i:.2f}', '--setting', f'src_out={o:.2f}'], check=True, stdout=subprocess.DEVNULL)
ORDER = ['b01', 's01', 's02', 's03', 'f01', 'f02', 'f03', 'f04', 'f04b', 'f05', 'f06', 'f07a', 'f07b']
recs = []
for cid in ORDER:
    if cid in new: recs.append(new[cid]); continue
    r = dict(old[cid]); lk = C / f'{cid}.wav'
    if lk.is_symlink() or lk.exists(): lk.unlink()
    lk.symlink_to(f'../clips/{cid}.wav'); r['file'] = str(lk)
    if cid == 'f06': r['placeholder'] = 'the 1F2 f06 clip; Kai is picking new words'
    recs.append(r)
json.dump(recs, open(H / 'lines-1f3.json', 'w'), indent=1, ensure_ascii=False)
print([(r['id'], r['dur']) for r in recs])
