import json, os
# r90 — Jack 2026-09-27, the same brief for the 4th time: "We have lost the aggresive rasta vocals…" → the lever changes this
# round, not just the voice: the VOICE SENTENCE IS FRONT-LOADED in every Style box and opens on a pool word whose default
# performer is aggressive (ragga / militant roots / dancehall badman) — suno-prompt skill: the genre word picks the vocalist
# pool and front-loading is the fix for a stubborn word. The reference is SWEET pop-reggae with a soulful woman, which pulls
# the pool the wrong way — hence also `female vocal, romantic, lovers rock, R&B` banned (lane-justified: the reference's own voice).
# Reference: "Rihanna - No Love Allowed (Reggae Version) | Musical Styles" (youtube Ffm6uHx49uM, 3:50; Brazilian reggae
# channel). Gemini (3.5-flash; flash-preview quota spent; seg 2 unheard): one-drop 76–88, kick + rimshot on three, swung
# eighth hats, deep melodic syncopated bass, clean offbeat guitar/organ stabs, brass pads in the pre-chorus, hall reverb,
# high-feedback tape delay on vocal tails, smooth rolled-off top; intimate verse → intense soaring chorus with harmonies.
# Research: the original (Unapologetic, 2012, prod. No I.D.) is "a bubbly, dubbed-out groove" nodding to Barbados; its story
# is love locked up by the police. Carry-over audited incl. r87–r89.
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
BASE="double-time, chopper, raspy, gravelly, female vocal, romantic, lovers rock, R&B, "
L={
 'ragga': dict(
  style="Ragga deejay vocal, furious and Jamaican, toasting hard with fire in every word, stabbing the syllables, heated and relentless, laid back in the pocket. The riddim: a bubbly, dubbed-out pop-reggae one-drop, 76 bpm, kick and rimshot on three, clean offbeat organ stabs, a deep syncopated bass, brass pads rising, feedback tape delay repeating his final words, and a dubstep sub that falls under every hook.",
  exclude=BASE+"sweet, crooning, smooth, gentle"),
 'warrior': dict(
  style="Militant roots warrior chant, a Rasta commander leading the charge, marching words, stern, loud and unbending, every line an order. Under him a half-time reggae march at 88, rimshot cracking, a heavy walking bass, guitar chops, hall reverb, and when he hits the hook the ground drops into a massive dubstep wobble, then marches on.",
  exclude=BASE+"sweet, crooning, pop, playful, brass pads"),
 'badman': dict(
  style="Dancehall badman deejay, menacing, cold, low-pitched and hard, threatening every line, sneering, dangerous, stalking the beat without ever hurrying. A dark minor version of a dubbed-out reggae groove: sparse rimshot one-drop, a bass that prowls, organ stabs drenched in echo, dub siren, and dubstep drops in which the bass snarls like a dog on a chain.",
  exclude=BASE+"sweet, crooning, singing, bright, brass, harmonies, playful"),
 'belter': dict(
  style="Rasta roots singer belting with fury: the verses chatted hard and bitter, then the hook sung at full power, soaring, anguished and furious, cracking with emotion, male harmonies roaring behind him. A polished pop-reggae groove, one-drop, eighty beats a minute, with offbeat guitar, a melodic rounded bass, swelling brass pads before each hook, hall reverb, and a dubstep sub pulse under the big moments.",
  exclude=BASE+"sweet, crooning, gentle, whispered, falsetto"),
 'babylon': dict(
  style="Conscious Rasta deejay raging at Babylon and the police, confrontational, shouting down the system, righteous anger boiling over, clear and hard, sitting back on the groove. The riddim: sirens and handclaps over a rolling one-drop, 84 bpm, a thick bubbling bass, choppy guitar, echo on the snare, then dubstep breakdowns with a crushing half-time sub and screaming siren sweeps.",
  exclude=BASE+"sweet, crooning, smooth, brass, harmonies"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r90-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
