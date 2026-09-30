# Carry-over audit: every 4-word run in a new Style/Exclude box that also appears in ANY earlier spec's
# Style/Exclude box (all scripts/suno/.tmp/r*/ json) or in camping.md. Prints the shared phrases per lane.
import json, glob, re, sys, os
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
def toks(s): return re.findall(r"[a-z0-9']+", s.lower())
def grams(s,n=4):
    t=toks(s); return {' '.join(t[i:i+n]) for i in range(len(t)-n+1)}
old=set(); oldw=set()
for f in glob.glob(f'{T}/**/*.json', recursive=True):
    if '/r88/' in f: continue
    try: d=json.load(open(f))
    except Exception: continue
    if not isinstance(d,dict): continue
    for k in ('style','exclude'):
        if isinstance(d.get(k),str): old|=grams(d[k]); oldw|={x.strip().lower() for x in d[k].split(',')}
old|=grams(open('/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md').read().split('\n# Camping — the song')[0])
for f in sorted(glob.glob(f'{OUT}/*.json')):
    d=json.load(open(f)); hit=sorted(grams(d['style'])&old)
    ex=[x.strip() for x in d['exclude'].split(',')]
    print(os.path.basename(f), 'style 4-grams shared with old boxes:', len(hit), hit)
    print('   exclude terms seen before:', [x for x in ex if x.lower() in oldw])
