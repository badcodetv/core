import json, os
# r89 — Jack 2026-09-27 (same words as r88's brief): aggressive Rasta reggae vocals ALWAYS, the voice varying per song;
# built off ONE reference: "Liquid Rasta | Deep Underwater Dub | Futuristic Sound" (youtube GY1ni6Uwzn0, 2 h psychedelic dub mix).
# Heard (Gemini, 5 × 60 s clips played on channel 1; flash-preview quota ran out, clips 1+3 re-heard on 3.5-flash; clip 3's
# second half and clip 5 were ADVERTS): slow one-drop 72-80, offbeat guitar skank, warm deep melodic sub, melodica/organ and
# a vintage vibrato synth lead, heavy tape delay + feedback echo, filter sweeps, spring reverb on the snare, hall reverb,
# soft pads, rolled-off top ("underwater"), processed female vocal chops as texture, resonant bubbling filter.
# Research: psydub = flanging/phasing, LPF sweeps like live fader rides; the aggressive reggae voice types are the fire
# chanter, the percussive ragga toaster, the rebel roots wailer, the Nyabinghi chant leader, the clashing deejays.
# Voices differ from r88's five (young deejay, preacher, dancehall deejay, singjay, elder). Carry-over audited (r87, r88 incl).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
L={
 'firechant': dict(
  style="Deep underwater dub, one-drop at 74, the whole band low-passed as if heard through the sea, a melodica and offbeat skank drowned in tape echo, bubbling resonant filter. Then the filter tears open and a colossal dubstep sub erupts beneath. Over it a Rasta fire chanter, blazing and furious, spiritual wrath in every line, chanting like he is burning Babylon down, sharp and ferocious, hurling 'fire!' between lines, unrushed and heavy on the beat.",
  exclude="double-time, chopper, raspy, gravelly, calm, mellow, crooning, sweet, lovers rock, female lead"),
 'rebelwail': dict(
  style="Spacious liquid dub reggae at 78, a warm Hammond, spring-reverbed snare, a skanking guitar dripping echo, a deep round bass singing the melody, hall reverb like an ocean cave, and whenever the band falls away the sub bends and wobbles like dubstep. A rebel roots singer, high and cutting, wailing the words in pure anger, sung with his whole chest, pleading then accusing, raw, defiant and on fire, each line ending in a cry thrown into echo.",
  exclude="double-time, chopper, raspy, gravelly, toasting, rap, sweet, crooning, lovers rock, soft, female lead, drum machine"),
 'nyabinghi': dict(
  style="Nyabinghi drums meet cosmic dub: a funde heartbeat and a repeater drum rolling over a slow 140 half-time dubstep kick, a bottomless sub, drone pads, bubbles and feedback echoes swirling, phaser on everything, deep and ritual. A Nyabinghi chant leader, fierce and incantatory, commanding like a war drum, calling down judgement line by line with total authority, every hook a battle cry, ancient and furious.",
  exclude="double-time, chopper, raspy, gravelly, guitar, horns, pop, bright, sweet, crooning, calm, female lead"),
 'clash': dict(
  style="Soundclash from the deep: a murky one-drop with a vintage vibrato synth lead and tape echo, that snaps into huge 140 half-time dubstep with a growling, gnashing bass wobble, then sinks back underwater. Two Rasta deejays clashing, one sharp and high, one booming and low, trading the verses like insults, hostile, cocky and aggressive, each trying to bury the other, toasting hard but never rushing, patois thick.",
  exclude="double-time, chopper, raspy, gravelly, singing, crooning, mellow, calm, sweet, choir, female lead, acoustic"),
 'alien': dict(
  style="Futuristic space dub, a slow alien-planet one-drop, 72 bpm: flanged skank, a quivering vintage synth lead, ghostly female vocal chops smeared in delay, a resonant arpeggio bubbling like water, filter sweeps opening and closing like breath, and a heavy dubstep sub rolling in waves. A Rasta deejay broadcasting from the future through an echo chamber, commanding and furious, spitting warnings with cold fury, every word clear and heavy, dropping behind the beat.",
  exclude="double-time, chopper, raspy, gravelly, crooning, sweet, mellow, acoustic, horns, organ, bright pop"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r89-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
