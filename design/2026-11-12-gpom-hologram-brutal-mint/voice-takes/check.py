"""Brutal + mint take check (copied from voice-1f/check-1f3.py): whisper words vs the text, gaps, pace, loudness, peak (clipping)."""
import json, re, subprocess, sys, pathlib
O = '/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-brutal-mint/'
W = json.load(open(O + 'words.json')); H = pathlib.Path(__file__).parent
norm = lambda s: re.sub(r"[^a-z' ]", ' ', re.sub(r'\[[^\]]*\]', ' ', s.lower().replace('’', "'"))).replace("'", '').split()
def loud(f):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1]), float(re.findall(r'Peak:\s+(-?[\d.inf]+) dBFS', e)[-1])
for f, ws in sorted(W.items()):
    tk = f.split('take-')[1].rsplit('-', 1)[0]
    want = norm(open(H / f'take-{tk}.txt').read()); got = norm(' '.join(w[0] for w in ws))
    T = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
    gaps = [(a[0], round(b[1] - a[2], 2)) for a, b in zip(ws, ws[1:]) if b[1] - a[2] > .6]
    sp = ws[-1][2] - ws[0][1]; I, pk = loud(f)
    print(f"{f.split('/')[-1]:18s} {'OK  ' if want == got else 'DIFF'} T {T:5.2f} speech {sp:5.2f} {len(got)/sp:.2f} w/s  {I:.1f} LUFS peak {pk:.1f}  tail {T-ws[-1][2]:.2f} gaps {gaps}")
    if want != got: print('    got ', ' '.join(got))
