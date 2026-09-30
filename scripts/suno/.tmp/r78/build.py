import json, re, os
IN='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r77'
OUT=os.path.dirname(os.path.abspath(__file__))
R71=json.load(open('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'))
def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
# Jack 2026-09-24: r77's style is THE style. One experiment: much lower, gravelly voices (his refs: two
# deep, gravelly ragga MCs — never named in a box). Only the voice words move.
OLD_CAST="Two ragga dancehall MCs trade the verses, toasting, loud and in front, one gruff and raw, one clipped and cold,"
NEW_CAST=("Two ragga dancehall MCs with deep, low, gravelly voices trade the verses, toasting from the chest, "
          "rough and husky, loud and in front, one gruff and raw, one clipped and cold,")
BANS=", high-pitched vocals, nasal vocals, thin voice, young voice"
for k in ['jamrock','bundem']:
    d=json.load(open(f'{IN}/{k}.json')); o=dict(d)
    assert d['style'].count(OLD_CAST)==1
    d['style']=d['style'].replace(OLD_CAST,NEW_CAST)
    d['exclude']=d['exclude']+BANS
    d['lyrics']=re.sub(r'ragga MC', 'deep gravelly ragga MC', d['lyrics'])
    assert wo(d['lyrics'])==wo(R71['lyrics'])
    # prove nothing else moved
    assert d['style'].replace(NEW_CAST,OLD_CAST)==o['style'] and d['exclude'][:len(o['exclude'])]==o['exclude']
    assert d['lyrics'].replace('deep gravelly ragga MC','ragga MC')==o['lyrics']
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000
    d['title']=f'camping-r78-{k}'
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1)
    print(k, len(d['style']), len(d['exclude']))
