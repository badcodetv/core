import json, re, os
IN='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r76'
OUT=os.path.dirname(os.path.abspath(__file__))
# Jack/Kai 2026-09-24: r76's sound is close — change NOTHING in Style/Exclude except removing every
# "grime" reference (the grime overlay fights the reggae). Lyrics shared by both lanes.
def degrime(s): return s.replace('grime MCs','MCs').replace('grime MC','MC')
for k in ['jamrock','bundem']:
    d=json.load(open(f'{IN}/{k}.json'))
    old=dict(d)
    for f in ['style','exclude','lyrics']: d[f]=degrime(d[f])
    for f in ['style','exclude','lyrics']: assert 'grime' not in d[f].lower(), (k,f)
    # prove the ONLY change is the word "grime " removed
    for f in ['style','exclude','lyrics']: assert old[f].replace('grime ','')==d[f], (k,f)
    d['title']=f'camping-r77-{k}'
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1)
    print(k, {f: len(old[f])-len(d[f]) for f in ['style','exclude','lyrics']}, 'chars removed')
