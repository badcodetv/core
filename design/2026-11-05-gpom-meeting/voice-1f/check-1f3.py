"""1F3 take check (check.py + [audio tags] stripped from the wanted text): whisper words vs the text, gaps over 1.2 s, lead/tail, pace."""
import json, re, sys, pathlib, subprocess
W = json.load(open(sys.argv[1]))
norm = lambda s: re.sub(r"[^a-z' ]", ' ', re.sub(r'\[[^\]]*\]', ' ', s.lower().replace('’', "'"))).replace("'", '').split()
for f, ws in W.items():
    tag = pathlib.Path(f).stem.replace('take-', ''); tk = tag.split('-')[0]
    want = norm(open(pathlib.Path(__file__).with_name(f'take-{tk}.txt')).read()); got = norm(' '.join(w[0] for w in ws))
    T = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
    gaps = [(round(a[2], 2), round(b[1] - a[2], 2)) for a, b in zip(ws, ws[1:]) if b[1] - a[2] > 1.2]
    sp = ws[-1][2] - ws[0][1]
    print(f"{tag:10s} {'OK  ' if want == got else 'DIFF'} words {len(got)} speech {sp:5.2f}s ({len(got)/sp:.2f} w/s) lead {ws[0][1]:.2f} tail {T-ws[-1][2]:.2f} gaps>1.2 {gaps}")
    if want != got: print('   want', ' '.join(want)); print('   got ', ' '.join(got))
