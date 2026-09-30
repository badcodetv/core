import json, os
# r91 — Jack 2026-09-27 (5th time, same words): aggressive Rasta reggae vocals always, voice varied; built off
# "Vintage Dub Reggae | Roots Rasta Classics | The Best Raggae" (youtube eRqugbxaK14, 33 min mix).
# Heard: 5 × 60 s clips; flash + flash-preview + 3.1-pro quotas ALL spent → described on gemini-3.5-flash-lite (lower
# confidence). Despite the title the mix is modern DIGITAL reggae/dancehall: drum machine one-drop/steppers, deep round sub,
# synth-brass pads carrying hooks, a steel-pan/marimba pluck hook, delay throws and plate on vocal endings, male patois voices
# half-sung half-chatted, passionate, "uplifting and defiant". Clip 1 = instrumental hip-hop (probably an ad; ignored).
# librosa: 129–136 = a ~65–68 reggae pulse read double. Research: 70s roots brought a "wailing"/"thunderous" dread vocal;
# deejays toasted in chant cadences on police brutality (Big Youth, U-Roy). Voice FRONT-LOADED as r90. Carry-over audited.
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
BASE="double-time, chopper, raspy, gravelly, female vocal, lovers rock, "
L={
 'thunder': dict(
  style="Thunderous dread chanter, a Rasta voice booming like a storm over the town, wailing and roaring the words, massive and wrathful, rolling each line out slow and huge. Under him: a stark digital reggae riddim, drum machine one-drop, a deep rounded sub, synth-brass swells, and a dubstep bass that detonates beneath every hook.",
  exclude=BASE+"sweet, crooning, gentle, smooth, pop, steel pan"),
 'sufferah': dict(
  style="Sufferer's cry: a ghetto youth singjay, high and desperate, raging for the poor, half-singing half-shouting his grievance, bitter, hurt and furious, voice breaking with anger. Digital reggae one-drop, a steel-pan pluck hook, round sub, echo repeats trailing him, and when his anger peaks the low end collapses into dubstep weight.",
  exclude=BASE+"sweet, crooning, calm, smooth, brass, choir"),
 'digital': dict(
  style="Mid-eighties digital ragga deejay, cocky and attacking, percussive syllables punched like drum hits, fierce, bold, trash-talking, riding the riddim hard. A stark drum machine riddim, a fat synth bass, a marimba-style pluck, reverb claps, then crushing dubstep sections at half speed with the synth bass growling.",
  exclude=BASE+"singing, crooning, sweet, mellow, brass, acoustic, organ"),
 'scorn': dict(
  style="Scornful Rasta chat-over deejay, mocking and sarcastic, laughing at the rich man, sneering and cutting, contemptuous, every word a jab, never hurried. A modern digital reggae groove, steppers kick, synth-brass stabs answering his lines, deep sub, echoing rimshots, dubstep drops that stomp on the beat like a boot.",
  exclude=BASE+"singing, crooning, sweet, gentle, steel pan, choir"),
 'defiant': dict(
  style="Defiant roots singer, full-throated and passionate, a Jamaican voice singing with fury and conviction, uplifting but angry, fists up, hitting the high notes hard, chatting the fast lines with fire. Digital reggae with a synth-brass section carrying the hooks, a round bouncing sub, sixteenth shakers, echoes flung off the close of each phrase, and dubstep sub swells under the choruses.",
  exclude=BASE+"sweet, crooning, whispered, falsetto, steel pan"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r91-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
