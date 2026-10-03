#!/usr/bin/env python3
"""Fetch cleared stills from Wikimedia Commons into the film's scene folders.
Exact titles are fetched as given; 'search:' entries take the first hit whose title contains the key.
Writes one receipt per file (the Commons API response, verbatim) and a status table."""
import json, os, re, sys, time, hashlib, urllib.parse, urllib.request
CLIPS='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/clips'
RECEIPTS=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../../../footage'))
HERE=os.path.dirname(os.path.abspath(__file__))
UA={'User-Agent':'BadCode-footage-ledger/1.0 (documentary research; sequential, low volume)'}
API='https://commons.wikimedia.org/w/api.php'
OKLIC=re.compile(r'^(CC0|Public domain|PDM|CC BY \d|OGL)',re.I)
ITEMS=json.load(open(sys.argv[1])) if len(sys.argv)>1 else [
 ('s07-quick-fire','In a Berlin Bank LCCN2014716642.jpg'),
 ('s07-quick-fire','search:LCCN2014715614'),
 ('s07-quick-fire','search:LCCN2014715613'),
 ('s07-quick-fire','search:LCCN2014715612'),
 ('s07-quick-fire','search:LCCN2014715615'),
 ('s07-quick-fire','search:LCCN2014715608'),
 ('s07-quick-fire','13-1-23 Essen patrouille de dragons.jpg'),
 ('s07-quick-fire','search:btv1b9024458p'),
 ('s07-quick-fire','search:GER-110-Reichsbanknote-500 Million Mark'),
 ('s07-quick-fire','search:GER-116-Reichsbanknote-10 Billion Mark'),
 ('s07-quick-fire','search:GER-127a-Reichsbanknote-500 Billion Mark'),
 ('s07-quick-fire','Reichsbanknote Zwanzig Milliarden Mark (20 milliards), 2016.12.1.4.jpg'),
 ('s07-quick-fire','search:btv1b53249445h'),
 ('s07-quick-fire','search:btv1b532494442'),
 ('s08-plant','Technical School- Training at Tottenham Polytechnic, Middlesex, England, UK, 1944 D21395.jpg'),
 ('s08-plant','Post War Planning and Reconstruction in Britain- Repairing Bomb Damaged Housing D24219.jpg'),
 ('s08-plant','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25712'),
 ('s08-plant','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25714'),
 ('s08-plant','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25716'),
 ('s08-plant','search:Construction of Temporary Housing D24228'),
 ('s09-sound-off','Northern Rock Queue.jpg'),
 ('s09-sound-off','Lehman Brothers-NYC-20080915.jpg'),
 ('s09-sound-off','Bank of England Facade.jpg'),
 ('s09-sound-off','Bank-of-England.jpg'),
 ('s09-sound-off','Threadneedle Street doors, Bank of England.jpg'),
 ('s09-sound-off','Chancellor of the Exchequer George Osborne (6128163568).jpg'),
 ('s09-sound-off','Budget 2014; Chancellor George Osborne delivering his Budget Statement.jpg'),
 ('s01-cold-open','Theresa May (2016).jpg'),
 ('s01-cold-open','Theresa May 2017 election speech outside 10 Downing Street.jpg'),
 ('s09-sound-off','10 Downing Street COVID-19 press conference, 20 March 2020.png'),
]
def api(params):
    q=API+'?'+urllib.parse.urlencode(dict(params,format='json'))
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(q,headers=UA),timeout=60) as r: return json.load(r)
        except Exception as e:
            time.sleep(8*(attempt+1))
    return {}
def resolve(spec):
    if not spec.startswith('search:'): return 'File:'+spec
    key=spec[7:]
    d=api({'action':'query','list':'search','srsearch':key,'srnamespace':6,'srlimit':10})
    hits=[h['title'] for h in d.get('query',{}).get('search',[])]
    tail=key.split()[-1].lower()
    for h in hits:
        if tail in h.lower(): return h
    return hits[0] if hits and len(hits)==1 else None
rows=[('scene','file','result','pixels','bytes','licence','artist','sha1_ok','commons_title')]
for scene,spec in ITEMS:
    title=resolve(spec); time.sleep(2)
    if not title: rows.append((scene,spec,'NOT FOUND','','','','','','')); continue
    d=api({'action':'query','titles':title,'prop':'imageinfo','iiprop':'url|size|sha1|mime|extmetadata'})
    p=list(d.get('query',{}).get('pages',{}).values() or [{}])[0]
    if 'imageinfo' not in p: rows.append((scene,spec,'MISSING','','','','','',title)); continue
    i=p['imageinfo'][0]; e=i.get('extmetadata',{})
    lic=e.get('LicenseShortName',{}).get('value','')
    artist=re.sub(r'<[^>]+>','',e.get('Artist',{}).get('value','')).strip()[:60]
    name=re.sub(r'[:?*"<>|]','',title[5:])
    slug=re.sub(r'[^A-Za-z0-9._-]+','_',name)[:120]
    json.dump(d,open(f'{RECEIPTS}/commons--{slug}.json','w'),indent=1,ensure_ascii=False)
    if not OKLIC.match(lic):
        rows.append((scene,name,'SKIPPED licence',f"{i['width']}x{i['height']}",'',lic,artist,'',title)); continue
    os.makedirs(f'{CLIPS}/{scene}',exist_ok=True); dest=f'{CLIPS}/{scene}/{name}'
    ok='no'
    if os.path.exists(dest) and hashlib.sha1(open(dest,'rb').read()).hexdigest()==i.get('sha1'): ok='yes'
    for attempt in range(0 if ok=='yes' else 4):
        try:
            with urllib.request.urlopen(urllib.request.Request(i['url'],headers=UA),timeout=120) as r: data=r.read()
            if hashlib.sha1(data).hexdigest()==i.get('sha1'):
                open(dest,'wb').write(data); ok='yes'; break
        except Exception as ex:
            print('retry',name,repr(ex)[:120],flush=True)
        time.sleep(10*(attempt+1))
    rows.append((scene,name,'OK' if ok=='yes' else 'FAILED',f"{i['width']}x{i['height']}",str(i.get('size','')),lic,artist,ok,title))
    time.sleep(3)
open(f'{HERE}/'+(os.path.basename(sys.argv[1])+'.status.tsv' if len(sys.argv)>1 else 'stills-status.tsv'),'w').write('\n'.join('\t'.join(r) for r in rows)+'\n')
print('\n'.join('\t'.join(r[:8]) for r in rows))
