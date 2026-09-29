import json, re, os
D=os.path.dirname(os.path.abspath(__file__))
R71=json.load(open('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'))
def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
# Jack/Kai 2026-09-24: ragga dancehall, not English/grime; no big structural instructions; Bob's verse
# has ONE energy step, at "cash from the bank", and no change anywhere else inside either half.
STYLE_CUT={'jamrock':"It opens on a low tense drone with him alone, quiet and begging, and the riddim slams in with the siren on 'you keep on walking'. ",
           'bundem':"It opens on the synth-brass with him alone, quiet and begging, and the first drop lands on 'you keep on walking'. "}
L=[("[Verse 1 | riddim stripped back | gruff MC, quiet, close and begging, unhurried]\n",
    "[Verse 1 | gruff MC, quiet, close and begging, unhurried]\n"),
   ("[Drop | everything drops in on this line]\n",""),
   ("[gruff MC, hurt and insistent, heavy and unhurried, every word clear]\n",""),
   ("cash from the bank",
    "[Verse 1, second half | gruff MC, more energy from here, same tempo, heavy and unhurried, every word clear]\ncash from the bank"),
   ("[gruff MC, raw, close to cracking, unhurried]\n",""),
   ("[gruff MC, a bitter plea]\n",""),
   ("[Verse 2 | straight in, no break | ","[Verse 2 | "),
   ("[Chorus | the beat cuts dead for the first line, then everything back, spoken flat]","[Chorus | spoken flat]"),
   ("[Final Chorus | everything at once, the whole room","[Final Chorus | the whole room")]
for k in ['jamrock','bundem']:
    d=json.load(open(f'{D}/{k}.json'))
    assert d['style'].count(STYLE_CUT[k])==1
    d['style']=d['style'].replace(STYLE_CUT[k],'').replace("Two English MCs trade the verses, loud","Two ragga dancehall MCs trade the verses, toasting, loud")
    lyr=d['lyrics']
    for a,b in L:
        assert lyr.count(a)==1,(k,a); lyr=lyr.replace(a,b)
    lyr=re.sub(r'\b(both )?MC(s?)\b', lambda m:(m.group(1) or '')+'ragga MC'+m.group(2), lyr)
    d['lyrics']=lyr
    assert wo(lyr)==wo(R71['lyrics']), k
    for bad in ['english','grime','drop','slams','lands on','you keep on walking\'']:
        assert bad not in d['style'].lower() or bad=='drop' and k=='bundem', (k,bad)
    json.dump(d, open(f'{D}/{k}.json','w'), indent=1)
    print(k, 'style', len(d['style']))
a=json.load(open(f'{D}/jamrock.json'))['lyrics']; b=json.load(open(f'{D}/bundem.json'))['lyrics']
assert a==b; print(a.split('[Chorus')[0])
