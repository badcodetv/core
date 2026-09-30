import json, os, re
# r82 — Jack 2026-09-26 on 3a433539 (r77 jamrock w40): "the deep gravel throated part … is ruining it …
# when i said aggression i meant the passion in the fast paced reggae voice". Applies the seven ideas:
# passion not gravel · intensity not tempo · r79 pop mix sentence verbatim · dark minor pluck (inside that
# sentence) · organ carries the chords, synth brass banned · half-sung singjay hook · melodica riff
# (lane `melodica`) or a live horn riff doubling the hook (lane `horns`). Lyrics = r81's cue-free box.
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'
OUT=os.path.dirname(os.path.abspath(__file__))
r77=json.load(open(f'{T}/r77/jamrock.json')); r79=json.load(open(f'{T}/r79/poppolish.json'))
LYR=open(f'{T}/r81/lyrics.txt').read()
wo=lambda t: re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
assert wo(LYR)==wo(r77['lyrics']) and '[' not in LYR
MIX=("Polished radio-ready mix, crisp punchy compressed drums, the sub loud and round, a crisp open top end, wide stereo, "
     "a dark minor-key synth pluck hooking the loop, a wide warm pad lifting under every hook.")
assert MIX in r79['style']   # word for word from r79 poppolish
VOICE="Fiery, commanding ragga deejays, urgent and full of feeling, every line meant, laid back behind the beat."
BED=("Heavy half-time reggae hip-hop riddim at 80: a deep punchy kick on the one, a dry cracking rimshot snare on the three, "
     "tight eighth-note hats, a massive warm walking sub carrying the tune, sparse and dark, dub sirens, "
     "tape delay and spring reverb thrown off his line-ends and the snare. A church organ carries the chords.")
LANE={'melodica':"A melodica plays the catchy riff, dark and plaintive, answering every line.",
      'horns':"Live trumpet, trombone and tenor sax play a punchy riff doubling the hook."}
HOOK=("The hook is a passionate singjay, half chatting half singing, catchy, natural and untuned. Every vocal sound is a word "
      "from the lyrics. Two ragga dancehall MCs trade the verses, toasting, loud and in front, one "
      "fiery and commanding, one clipped and cold, unhurried, every word clear.")
exc=r79['exclude']
for w in ['singing','sung hook','melodic chorus','soulful vocal']:   # the half-sung hook is now asked for
    assert f', {w},' in exc, w; exc=exc.replace(f', {w},',',')
exc+=', sung verses, smooth R&B tenor, synth brass, gravelly voice, growling, gruff, raspy voice'
for k,lane in LANE.items():
    d={kk:r77[kk] for kk in ['model','styleInfluence','weirdness','durationSec','variety','maxMode','vocalGender','personalize','workspace']}
    d['style']=' '.join([VOICE,BED,lane,MIX,HOOK]); e=exc
    if k=='horns': assert ', brass band,' in e; e=e.replace(', brass band,',',')
    d.update(exclude=e, lyrics=LYR, title=f'camping-r82-{k}')
    for bad in ['gravel','gruff','growl','hoarse','rasp','bark','chest','deep voice']: assert bad not in d['style'].lower(), bad
    print(len(d["style"]),len(d["exclude"])); assert len(d["style"])<=1000 and len(d["exclude"])<=1000
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1); print(k, len(d['style']), len(d['exclude']), d['weirdness'], d['durationSec'])
