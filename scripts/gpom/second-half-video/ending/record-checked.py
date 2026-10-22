#!/usr/bin/env python3
"""Record Suno takes with `suno.mts record`, checking each against its listed length.

`recordTake` can read the PREVIOUS song's duration off the player (the playbar's link updates before
the <audio> src does), so a recording comes back truncated, padded, or with the last song's tail in
it (seen 21 Oct 2026, GPOM ending round A). This wrapper re-records until the recorded duration is
within TOL seconds of the length the takes list shows, up to TRIES times, and reports a miss.

  python3 record-checked.py <outDir> <takes.txt>
takes.txt lines: "<title>  <m:ss>  https://suno.com/song/<uuid>" (the `takes --links` format).
No downloads: this only plays the take in the create page and records the sound.
"""
import json, os, re, subprocess, sys

REPO = '/home/kai/projects/badcode/badcode'
TOL, TRIES = 1.5, 4
out, listing = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for line in open(listing):
    m = re.search(r'(\S+)\s+(\d+):(\d\d)\s+https://suno.com/song/([0-9a-f-]{36})', line)
    if not m:
        continue
    title, want, sid = m.group(1), int(m.group(2)) * 60 + int(m.group(3)), m.group(4)
    ok = False
    for t in range(TRIES):
        r = subprocess.run(['npx', 'tsx', 'scripts/suno/suno.mts', 'record', sid], cwd=REPO,
                           env={**os.environ, 'LISTEN_MEDIA_ROOT': out}, capture_output=True, text=True, timeout=400)
        js = [l for l in r.stdout.splitlines() if l.startswith('{')]
        if not js:
            print(f'{title} {sid[:8]} try {t + 1}: ERROR {(r.stderr or r.stdout).strip()[-200:]}', flush=True)
            continue
        got = json.loads(js[-1])['durationSec']
        ok = abs(got - want) <= TOL
        print(f'{title} {sid[:8]} try {t + 1}: recorded {got:.2f}s, listed {want}s {"OK" if ok else "MISMATCH"}', flush=True)
        if ok:
            break
    if not ok:
        print(f'{title} {sid[:8]}: GAVE UP', flush=True)
print('ALLDONE', flush=True)
