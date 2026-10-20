"""Every mood-board still in r1-motions.json -> a Flow video job (video-jobs.json `extra`).
Numbers stay stable as stills are added. Kai 19 Oct: animate every still, each a different way."""
import json, pathlib
D = pathlib.Path(__file__).parent
m = json.load(open(D / 'r1-motions.json'))
order = ['RK1', 'HD1', 'SL1', 'EC1', 'SH1', 'MA1', 'ET1', 'TN1']
ids = sorted(m, key=lambda i: (order.index(i[:3]) if i[:3] in order else 99, i))
try:
    old = {e['still']: e['n'] for e in json.load(open(D / 'video-jobs.json'))['extra']}
except Exception:
    old = {}
nxt = max(old.values(), default=0)
for i in ids:
    if i not in old:
        nxt += 1
        old[i] = nxt
lock = 'The camera does not move.'
jobs = {'duration': 6, 'skip': [], 'extra': [
    {'key': f'mb{old[i]:02d}', 'n': old[i], 'still': i, 'duration': 6,
     'motion': f'{lock} {m[i]} {lock}', 'character': None,
     'why': 'Kai 19 Oct (away): animate every mood-board still, each a different way'} for i in ids]}
json.dump(jobs, open(D / 'video-jobs.json', 'w'), indent=1)
print(len(ids), 'jobs')
