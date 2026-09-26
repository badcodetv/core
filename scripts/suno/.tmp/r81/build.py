import json, os, re
# r81 — Jack 2026-09-26 after r80: "we have lost the aggression and it has got too pop … not enough reggae.
# … remove [the structural prompts] and just have complete freedom with the song. … make versions of
# 3a433539 [r77 jamrock w40] … more reggae less pop, but keep pop music elements, maybe change up the
# reggae voice in each generation."
# Voice research 2026-09-26: gruff deejay / chanter / toaster sit heavy and slow; hardcore + 'ragga' pull
# toward fast chat, so 'laid back behind the beat' is the positive pacing instruction in every lane.
# Base = r77 jamrock (3a433539). Changes: (1) NO structure anywhere — every [cue] out of the lyrics (a blank
# line between sections is the only layout), no timing words in Style; (2) one reggae VOICE per lane,
# lane clause first; (3) aggression back via delivery words (never speed); (4) two pop elements only:
# a polished punchy mix and a catchy hook.
R77='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r77'
OUT=os.path.dirname(os.path.abspath(__file__))
src=json.load(open(f'{R77}/jamrock.json'))
wo=lambda t: re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()

# Lyrics: section-header cues become a blank line; speaker labels just go.
lines=[]
for ln in src['lyrics'].split('\n'):
    m=re.fullmatch(r'\s*\[([^\]]*)\]\s*',ln)
    if m:
        if re.match(r'(Verse|Chorus|Bridge|Final Chorus)',m.group(1)) and lines: lines.append('')
        continue
    lines.append(ln)
LYR='\n'.join(lines).strip()
assert '[' not in LYR and wo(LYR)==wo(src['lyrics'])

BED=("Heavy half-time reggae riddim at 80: a deep punchy kick, a dry cracking rimshot snare, an organ bubble "
     "and a muted guitar skank on the offbeat, a massive overdriven sound-system sub carrying the tune, dub sirens, tape delay "
     "and spring reverb thrown off the line-ends and the snare, a church organ. Dark, heavy and menacing. "
     "Polished punchy modern mix, crisp top end, wide stereo, a catchy hook the room says with him.")
CAST=("{v} Two of them trade the verses, loud and in front, aggressive and cutting, laid back behind the beat on the slow "
      "half-time pulse, heavy and unhurried, every word clear. Every vocal sound is a word from the lyrics.")
VOICES={
 'gravel':   "Deep gravel-throated ragga deejays, rough, growling and barking the lines from the chest.",
 'fire':     "Fiery Rasta chanters, fire-and-brimstone, wailing held vowels, long chanted lines, preaching and raging.",
 'hardcore': "Hardcore dancehall deejays, hoarse, gritty and menacing, clipped hard consonants, one line per bar, snarling with contempt.",
 'soundsystem': "Old-school seventies sound-system toasters, bold and commanding, chanting over the dub, raw and proud.",
 'singjay':  "Raspy ragga singjays, half chatting half singing, a torn, gravelly voice, bitter and hard.",
}
exc=src['exclude']
# audit: aggression is being asked for, polish is a kept pop element
for w in ['shouting','roaring','glossy production']:
    assert f', {w},' in exc, w; exc=exc.replace(f', {w},',',')
for k,v in VOICES.items():
    d=dict(src)
    d['style']=v+' '+BED+' '+CAST.format(v='').strip()
    e=exc
    if k=='singjay':
        for w in ['singing','sung hook']:
            assert f', {w},' in e; e=e.replace(f', {w},',',')
        e+=', sung verses, smooth vocals'
    d['exclude']=e; d['lyrics']=LYR; d['title']=f'camping-r81-{k}'
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1)
    print(k, len(d['style']), len(d['exclude']))
open(f'{OUT}/lyrics.txt','w').write(LYR)
