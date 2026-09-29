#!/usr/bin/env python3
"""Fetch cleared stills from Wikimedia Commons into the film's scene folders.
Exact titles are fetched as given; 'search:' entries take the first hit whose title contains the key.
Writes one receipt per file (the Commons API response, verbatim) and a status table."""
import json, os, re, sys, time, hashlib, urllib.parse, urllib.request
CLIPS='/mnt/d/badcode-videos/magic-money-tree/clips'
RECEIPTS='/home/kai/projects/badcode/badcode/docs/footage'
HERE=os.path.dirname(os.path.abspath(__file__))
UA={'User-Agent':'BadCode-footage-ledger/1.0 (documentary research; sequential, low volume)'}
API='https://commons.wikimedia.org/w/api.php'
OKLIC=re.compile(r'^(CC0|Public domain|PDM|CC BY \d|OGL)',re.I)
import csv
_FAILED=set(r[1] for r in csv.reader(open(HERE+'/stills-status.tsv'),delimiter='\t') if len(r)>2 and r[2]=='FAILED')
ITEMS_ALL=[
 ('s02a-germany-1923','In a Berlin Bank LCCN2014716642.jpg'),
 ('s02a-germany-1923','search:LCCN2014715614'),
 ('s02a-germany-1923','search:LCCN2014715613'),
 ('s02a-germany-1923','search:LCCN2014715612'),
 ('s02a-germany-1923','search:LCCN2014715615'),
 ('s02a-germany-1923','search:LCCN2014715608'),
 ('s02a-germany-1923','13-1-23 Essen patrouille de dragons.jpg'),
 ('s02a-germany-1923','search:btv1b9024458p'),
 ('s02a-germany-1923','search:GER-110-Reichsbanknote-500 Million Mark'),
 ('s02a-germany-1923','search:GER-116-Reichsbanknote-10 Billion Mark'),
 ('s02a-germany-1923','search:GER-127a-Reichsbanknote-500 Billion Mark'),
 ('s02a-germany-1923','Reichsbanknote Zwanzig Milliarden Mark (20 milliards), 2016.12.1.4.jpg'),
 ('s03-unemployed-builder','search:btv1b53249445h'),
 ('s03-unemployed-builder','search:btv1b532494442'),
 ('s04-the-word-actually','Technical School- Training at Tottenham Polytechnic, Middlesex, England, UK, 1944 D21395.jpg'),
 ('s04-the-word-actually','Post War Planning and Reconstruction in Britain- Repairing Bomb Damaged Housing D24219.jpg'),
 ('s04-the-word-actually','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25712'),
 ('s04-the-word-actually','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25714'),
 ('s04-the-word-actually','search:Grenadier Guardsmen Build Emergency Housing in Windsor D25716'),
 ('s04-the-word-actually','search:Construction of Temporary Housing D24228'),
 ('s07-victory','search:Ve Day Celebrations in London D24584'),
 ('s07-victory','search:Ve Day Celebrations in London D24586'),
 ('s07-victory','search:Ve Day Celebrations in London D24587'),
 ('s10a-new-money','Northern Rock Queue.jpg'),
 ('s10a-new-money','Lehman Brothers-NYC-20080915.jpg'),
 ('s10a-new-money','Bank of England Facade.jpg'),
 ('s10a-new-money','Bank-of-England.jpg'),
 ('s10a-new-money','Threadneedle Street doors, Bank of England.jpg'),
 ('s10b-outgrown','search:Bestanddeelnr 910-7302'),
 ('s11-another-shift','Chancellor of the Exchequer George Osborne (6128163568).jpg'),
 ('s11-another-shift','Budget 2014; Chancellor George Osborne delivering his Budget Statement.jpg'),
 ('s11-another-shift','Theresa May (2016).jpg'),
 ('s11-another-shift','Theresa May 2017 election speech outside 10 Downing Street.jpg'),
 ('s11a-money-was-found','10 Downing Street COVID-19 press conference, 20 March 2020.png'),
 ('s11a-money-was-found','Royal Courts of Justice 2019.jpg'),
 ('s11a-money-was-found','search:Ambassador Earl Miller joined the inaugural PPE gown shipment'),
]
ITEMS=[(s,x) for s,x in ITEMS_ALL]
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
_done=[r for r in csv.reader(open(HERE+'/stills-status.tsv'),delimiter='\t')][1:]
_keep=[tuple(r) for r in _done if r[2]!='FAILED']
rows=[('scene','file','result','pixels','bytes','licence','artist','sha1_ok','commons_title')]
rows+=_keep
for scene,spec in ITEMS:
    title=resolve(spec); time.sleep(2)
    if title and re.sub(r'[:?*"<>|]','',title[5:]) not in _FAILED: continue
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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(i['url'],headers=UA),timeout=300) as r: data=r.read()
            if hashlib.sha1(data).hexdigest()==i.get('sha1'):
                open(dest,'wb').write(data); ok='yes'; break
        except Exception as ex:
            pass
        time.sleep(120*(attempt+1))
    rows.append((scene,name,'OK' if ok=='yes' else 'FAILED',f"{i['width']}x{i['height']}",str(i.get('size','')),lic,artist,ok,title))
    time.sleep(20)
open(f'{HERE}/stills-status.tsv','w').write('\n'.join('\t'.join(r) for r in rows)+'\n')
print('\n'.join('\t'.join(r[:8]) for r in rows))
