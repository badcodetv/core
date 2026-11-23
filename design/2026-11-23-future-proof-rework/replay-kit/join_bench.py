import json, sys
issue_path, a_path, b_path = sys.argv[1:4]
base = issue_path[:-5]
d = json.load(open(issue_path)); clerk = json.load(open(base + '.side.clerk.json')); c = json.load(open(base + '.side.rival.json'))
A = json.load(open(a_path)); B = json.load(open(b_path))
extra = {s['id']: s for s in clerk.get('extra_sources', [])}
have = {s['id'] for s in d['sources']}
def nxt(): return 's%d' % (max(int(s['id'][1:]) for s in d['sources'] + list(extra.values())) + 1)
def fix(ans):
    ids = []
    for sid in ans.get('sources', []):
        if sid not in have and sid in extra: d['sources'].append(extra[sid]); have.add(sid)
        if sid in have: ids.append(sid)
    for ns in ans.get('new_sources', []):
        sid = nxt(); s = {'id': sid, **{k: ns[k] for k in ('title', 'publisher', 'url')}}
        if ns.get('date'): s['date'] = ns['date']
        d['sources'].append(s); have.add(sid); ids.append(sid)
    return ids
bench = []
for sid, ans, eng, model in (('A', A, 'claude', 'claude-sonnet-5-5'), ('B', B, 'claude', 'claude-sonnet-5-5'), ('C', c, c.get('engine', 'codex'), c.get('model', 'codex'))):
    bench.append({'id': sid, 'title': ans['title'] if len(ans['title']) <= 70 else ans['title'][:70].rsplit(' ', 1)[0], 'answer': ans['answer'], 'engine': eng, 'model': model, 'blind': True, 'sources': fix(ans)})
d['bench'] = bench; d['stage'] = 'bench'; d['made_by']['workers'].append('sim-bench')
json.dump({'A': A, 'B': B}, open(base + '.side.bench.json', 'w'), indent=1, ensure_ascii=False)
json.dump(d, open(issue_path, 'w'), indent=1, ensure_ascii=False)
print('joined', [b['title'] for b in bench])
