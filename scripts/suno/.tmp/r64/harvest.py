import sys, json, re, pathlib
t = sys.stdin.read(); rows = json.loads(re.search(r'\[.*\]', t, re.S).group(0))
g = {}
for r in rows: g.setdefault(r['title'], []).append([r['songId'], r['dur']])
p = pathlib.Path('scripts/suno/.tmp/r64/takes.json')
for k, v in json.loads(p.read_text()).items():
    if k not in g: g[k] = v
p.write_text(json.dumps(g, indent=2))
for k in sorted(g): print(k, len(g[k]), [x[0][:8] for x in g[k]])
print('lanes:', len(g), 'takes:', sum(len(v) for v in g.values()))
