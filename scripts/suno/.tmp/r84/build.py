import json, os, re
# r84 — Jack 2026-09-26. Two briefs, one round:
#  A) "make songs more like" Make It Bun Dem (youtube BGpzGu9Yp6Y): reggae dubstep is the main thing, a SMALL amount
#     of VARIED pop elements, and the voice like the reference's. Voice heard by Gemini on two verse clips
#     (12–52 s, 118–168 s): young male Jamaican singjay, bright + chesty, commanding, chant with a minor-key lilt,
#     syncopated and behind the beat, phrase-ends doubled, upfront, slapback echo. Its grit is NOT written:
#     Jack's r82 rule, no gravel words for Camping voices. Its 6–8 words/bar is NOT written: never double-time.
#  B) experiment: the reggae with the vibe of Disconnect (youtube bE3Kvqyef_E). Gemini unavailable (429/503);
#     MEASURED only: ~172 BPM, drop -5.8 LUFS / centroid 3.9 kHz (loud, bright), intro -15.8 LUFS. The rest
#     (euphoric-melancholic anthemic D&B, big emotional chords) is unverified prior knowledge.
# Words: r81's cue-free box, no bracket cues (Jack r81: complete freedom). Male vocal only (canon).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LY=open(f'{T}/r81/lyrics.txt').read().strip()
STD="double-time, double-time rap, fast rap, rapid-fire flow, chopper rap, speed rap, motormouth, autotune, pitch-corrected vocals, gravelly voice, female vocal, American accent"
VOICE="A young Jamaican singjay leads, male, bright and chesty with a commanding edge, half-chanting, half-singing in patois with a minor-key lilt, fiery and full of feeling, syncopated and laid back behind the beat, the ends of his phrases doubled for weight, upfront with a short slapback echo, every word clear."
BUN="Reggae dubstep at 140, half-time: a punchy kick on the one, a sharp metallic snare cracking on the three, swung offbeat hats, a clean round sub walking under offbeat brass skanks. Snare rolls build into drops where the bass tears into a growling formant wobble and a screeching laser lead, then back to the clean riddim. Dub sirens, tape echo, a dub breakdown to end."
L={
 'bunpop-keys': dict(style=BUN+" A touch of pop: warm bright piano chords and handclaps lift the hook, and he sings the hook clean and catchy. "+VOICE,
  exclude=STD+", synth pluck, four-on-the-floor, glossy, choir, strings, trap, reggaeton, tropical house, drum and bass"),
 'bunpop-gloss': dict(style=BUN+" A touch of pop: a bright, hooky synth pluck riff answers him, a polished wide radio mix, and a short filtered pop lift into each drop. "+VOICE,
  exclude=STD+", piano, handclaps, choir, strings, trap, reggaeton, tropical house, drum and bass, lo-fi, tape hiss"),
 'disconnect-roll': dict(style="Rolling drum and bass at 174 married to reggae: a fast, crisp two-step breakbeat and a deep, rolling, driving bass, with an offbeat organ skank and a dub siren woven through, while the voice rides the slow half-time pulse like a reggae riddim. Euphoric and heartbroken at once: big emotional minor chords, wide lush pads, a soaring anthemic festival drop, bright, huge and loud. He sings the hook big and open. "+VOICE,
  exclude=STD+", wobble, brostep, screeching lead, trap, jungle, amen break, lo-fi, tape hiss, choir, strings, dubstep"),
 'disconnect-switch': dict(style="Reggae at 87, heavy one-drop, rimshot on the three, a warm walking sub and offbeat organ skank, dub echo on his line-ends. Then the pulse doubles into euphoric, rolling drum and bass at 174: a crisp two-step break, a huge rolling bass, big emotional minor chords and wide shimmering pads, bright, loud and arena-sized, his voice still riding the slow pulse on top. It drops back into the reggae and lifts again. "+VOICE,
  exclude=STD+", wobble, brostep, screeching lead, trap, jungle, amen break, choir, strings, piano, lo-fi"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r84-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[40,60],durationSec=240,
           variety='off',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LY)
    assert '[' not in d['lyrics']
    for w in ('gravel','gruff','growl','hoarse','rasp','bark'):
        assert w not in re.sub(r'growling formant wobble','',d['style']).lower(), (k,w)
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000, (k,len(d['style']))
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
