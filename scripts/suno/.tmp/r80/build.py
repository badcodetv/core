import json, os
# r80 — Jack 2026-09-26 on ae937a18 (= camping-r79-poppolish-v6-w40): likes it; more pop, keep the reggae
# vibes. References (NEVER named in a box): Post Malone, Drake, Rihanna, MAGIC! "Rude", Shaggy "Angel" /
# "It Wasn't Me", Sean Kingston "Beautiful Girls", Rihanna "Pon de Replay", Iyaz "Replay".
# 🔑 Every reference has a SUNG hook over toasted/rapped verses ("It Wasn't Me" = gruff toaster verses +
# smooth singer hook = our exact cast). So the hook is sung from r80 — Jack's references override the
# r41 words-only rule. Autotune stays banned (r66 "too cheesy"), never double-time.
# Listen of ae937a18 (docs/listening/log/2026-09-26-115443-…): the hook ALREADY came out sung by a clean
# soaring male tenor; organ bubble + muted guitar skank tucked back; ~83 BPM steppers, minor. Verse 2 went
# DOUBLE-TIME 1:37-2:24 (rule broken) — 'sharper' cue swapped for 'harder, still slow'.
# Frozen: r79 poppolish's mix sentence (the liked take), the MC verse cast, r77 verse words.
R79='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r79'
OUT=os.path.dirname(os.path.abspath(__file__))
src=json.load(open(f'{R79}/poppolish.json'))
OLD_HOOK="The hook comes quick, a room of men saying it with him flat and low, words only. "
CAST=("Every vocal sound is a word from the lyrics, nothing wordless anywhere. "
      "Two ragga dancehall MCs trade the verses, toasting, loud and in front, one gruff and raw, "
      "one clipped and cold, riding the slow half-time pulse, heavy and unhurried, every word clear.")
MIX=("Polished radio-ready mix, crisp punchy compressed drums, the sub loud and round, a crisp open top end, "
     "wide stereo.")
assert src['style'].count(OLD_HOOK+CAST)==1
for w in ["Polished radio-ready mix, crisp punchy compressed drums, the sub loud and round,","wide stereo"]:
    assert w in src['style']
SUNG="The hook is sung by one clean, soaring male tenor, a simple catchy melody, natural and untuned. "
LANES={
 # It Wasn't Me / Angel — the two-voice split: gravelly toaster verses, smooth R&B singer hook.
 'toasterhook': ("Reggae hip-hop crossover pop at 90: a laid-back hip-hop pocket with a dancehall accent, "
   "a funky walking bassline, a muted offbeat guitar skank, an organ bubble, a dub siren at the turns. ",
   SUNG.replace("clean, soaring male tenor","smooth, soaring male R&B tenor"), True),
 # Rude — reggae pop fusion, one-drop band, big sung chorus.
 'onedroppop': ("Reggae pop fusion, one-drop at 72: live drums with the rimshot on the three, a clean "
   "offbeat guitar skank, a round melodic bassline, bright organ bubble, tape delay on the line-ends. ",
   SUNG.replace("a simple catchy melody","a big simple sing-along chorus"), True),
 # Beautiful Girls / Replay — doo-wop reggae pop, fifties loop, bright chords under grim words.
 'doowop': ("Doo-wop reggae pop at 65, half-time: a fifties bass-and-chord loop, a sparse offbeat skank, "
   "an organ bubble, finger snaps, a light one-drop, the sweet bright chords against the bitter words. ",
   SUNG, True),
 # Pon de Replay / Work — minor dancehall pop, handclap riddim, chanted call-and-response hook.
 'clapriddim': ("Minor-key dancehall pop at 100: a syncopated handclap riddim, big bouncing dancehall "
   "drums, a deep sub, an organ bubble and muted skank tucked underneath, dub echo on the line-ends. ",
   "The hook is a chant: the MC calls it and a room answers it back, catchy and repeated, words only. ", False),
 # Controlla / One Dance / Post Malone — nocturnal minor dancehall, reverb-wet sung hook.
 'nightdancehall': ("Nocturnal minor-key dancehall pop at 92: a sparse dancehall drum with a dry rim, a deep "
   "sub, hypnotic minor piano chords, a muted guitar skank, an organ bubble, wet arena reverb on the hook. ",
   SUNG.replace("clean, soaring","soft, melancholy"), False),
}
base_exc=src['exclude']
for k,(bed,hook,major_ok) in LANES.items():
    d=dict(src)
    d['style']=bed+MIX+' '+hook+CAST
    e=base_exc
    if hook is not LANES['clapriddim'][1]:
        for w in ['singing','sung hook','melodic chorus','soulful vocal','crooning']:
            assert f', {w},' in e or e.startswith(w+',') , w
            e=e.replace(f', {w},',',')
        e+=', sung verses'
    if major_ok:
        for w in ['major key','happy','uplifting']:
            assert f', {w},' in e, w
            e=e.replace(f', {w},',',')
    if k=='nightdancehall': e=e.replace(', trap,',',')
    d['exclude']=e
    lyr=src['lyrics']
    if hook is not LANES['clapriddim'][1]:
        lyr=lyr.replace('[Chorus | the room says the hook with him, spoken flat, words only]','[Chorus | sung by the soaring male tenor]')
        lyr=lyr.replace('[Chorus | spoken flat]','[Chorus | sung by the soaring male tenor]')
        lyr=lyr.replace('[Final Chorus | the whole room saying it with him, spoken flat, words only]','[Final Chorus | sung by the soaring male tenor]')
        assert lyr.count('[Chorus | sung by the soaring male tenor]')==2 and '[Final Chorus | sung' in lyr
    else:
        lyr=lyr.replace('[Chorus | the room says the hook with him, spoken flat, words only]','[Chorus | the MC calls, the room chants it back, words only]')
        lyr=lyr.replace('[Chorus | spoken flat]','[Chorus | the MC calls, the room chants it back, words only]')
        lyr=lyr.replace('[Final Chorus | the whole room saying it with him, spoken flat, words only]','[Final Chorus | the MC calls, the room chants it back, words only]')
    import re
    wo=lambda t: re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
    assert wo(lyr)==wo(src['lyrics'])
    assert lyr.count('[cold ragga MC, sharper, still unhurried]')==1
    lyr=lyr.replace('[cold ragga MC, sharper, still unhurried]','[cold ragga MC, harder, still slow and unhurried]')
    d['lyrics']=lyr
    d['title']=f'camping-r80-{k}'
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000, (k,len(d['style']),len(d['exclude']))
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1)
    print(k, len(d['style']), len(d['exclude']), 'major-ok' if major_ok else 'minor', 'sung' if 'sung by' in lyr else 'chant')
