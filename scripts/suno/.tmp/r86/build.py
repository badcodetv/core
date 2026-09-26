import json, os, re
# r86 — Jack 2026-09-26: combine r77 bundem take 2ffbd6b9 with "Gnome Dub — 90 Minutes of Psychedelic Dub Reggae"
# (youtube NX_QMlFxDSw, Futuristic Sound). Built ONLY from r77 bundem + this reference — r85 (desert) is not an input.
# Four 60 s samples (3:00, 25:00, 50:00, 75:00) played + recorded, no download; heard by gemini-3-flash-preview.
# Heard: one-drop ~85 and half-time ~140 (one sample 4/4 steppers); a deep CLEAN melodic sub is the loudest thing;
# mournful airy trumpet / brass lead, synth flute, a bubbling squelchy acid synth; offbeat organ/piano chops;
# spring-reverb snare; long tape feedback delay; filter sweeps; drop-outs to bass + echo; sirens; swirling phased pads;
# modern-clean with 70s character. Measured darker + wider than the take: centroid 1.4–2.0 kHz vs 3.85 kHz,
# side/mid -12..-13 dB vs -18 dB. Not carried: its female/wordless vocal textures (canon men; words-only rule).
# The take's double-time bridge (2:08): bans + the bridge's slow cue kept. Voice: gruff -> fiery (Jack's r82 rule).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
r77=json.load(open(f'{T}/r77/bundem.json'))
LY=r77['lyrics'].replace('gruff ragga MC','fiery ragga MC')
HOOK=" The hook comes quick, a room of men saying it with him flat and low, words only. Every vocal sound is a word from the lyrics, nothing wordless anywhere. Two ragga dancehall MCs trade the verses, toasting, loud and in front, one fiery and raw, one clipped and cold, riding the slow half-time pulse, heavy and unhurried, every word clear."
EX=r77['exclude']+", brostep, screeching lead"
L={
 'gnome-step': "Psychedelic reggae dubstep at 140, half-time: kick on the one, a woody snare cracking on the three with a spring reverb splash, a deep, clean, melodic sub walking loud under offbeat organ chops. A mournful trumpet answers him with long tape echo, and a bubbling acid synth squelches in the gaps. Snare rolls build into drops where the sub swells into a slow, deep, rounded wobble, then back to the riddim. Dub drop-outs to bass and echo, filter sweeps, a dub siren, swirling phased pads, dark and wide."+HOOK,
 'gnome-dub': "Psychedelic dub reggae at 85, heavy one-drop: a round kick and woody snare on the three with a spring reverb splash, tight hats, a deep, clean, melodic sub carrying the tune, offbeat organ chops. A mournful trumpet and an airy flute trade phrases drenched in tape feedback echo, a bubbling acid synth swirls through. The sub swells into a heavy half-time dubstep weight for the hook, then falls back. Dub drop-outs to bass and echo, filter sweeps, sirens, phased pads, dark, wide and hypnotic."+HOOK,
}
for k,s in L.items():
    d=dict(model='v6',title=f'camping-r86-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[40,60],durationSec=240,
           variety='off',maxMode=False,vocalGender='male',personalize=False,style=s,exclude=EX,lyrics=LY)
    for w in ('gravel','gruff','hoarse','rasp','bark','growl','oud','darbuka','desert'):
        assert not re.search(r'\b'+w, (s+LY).lower()), (k,w)
    ex=[x.strip() for x in EX.split(',')]
    for w in ('organ','trumpet','flute','acid','dubstep','reverb','sirens','pads','one-drop','wobble'):
        assert w not in ex, (k,w)
    assert re.sub(r'\[[^\]]*\]','',LY)==re.sub(r'\[[^\]]*\]','',r77['lyrics'])
    assert len(s)<=1000 and len(EX)<=1000
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(s),len(EX))
