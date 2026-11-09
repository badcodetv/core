"""Check each 1F take: whisper words vs the text, and any dead gap over 2 s (incl. lead/tail)."""
import json, re, sys, pathlib
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f')
W = json.load(open(sys.argv[1]))
norm = lambda s: re.sub(r"[^a-z' ]", ' ', s.lower().replace('’', "'")).split()
for f, ws in W.items():
    tk = pathlib.Path(f).stem.replace('take-', '').split('-')[0]; tag = pathlib.Path(f).stem.replace('take-', '')
    want = norm(open(pathlib.Path(__file__).with_name(f'take-{tk}.txt')).read())
    got = norm(' '.join(w[0] for w in ws))
    gaps = [(round(a[2], 2), round(b[1] - a[2], 2)) for a, b in zip(ws, ws[1:]) if b[1] - a[2] > 1.2]
    print(tag, 'OK' if want == got else 'DIFF', 'gaps>1.2', gaps, 'end', ws[-1][2] if ws else None)
    if want != got: print('   want', ' '.join(want)); print('   got ', ' '.join(got))
