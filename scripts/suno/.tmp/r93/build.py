import json, os
# r93 — Jack 2026-09-27 (7th time, same words); built off "Damian Marley ft. Eminem - Reggae is Life" (youtube 5eQHur_rCU4,
# Mohib Beats — an AI-made fan track, not a real collab: the channel's other upload is titled "Official AI Music Video").
# Heard (flash-preview for seg 1, flash-lite for 2-4; librosa ~83): one-drop 83-95, tight dry acoustic kit, rim-click, thick
# melodic DI bass, sharp offbeat staccato guitar, Hammond / e-piano, spring reverb + tape delay throws; a soulful tenor on the
# hook, and a percussive patois toaster whose aggression "comes from … the explosive delivery of consonants", "pushing chest
# voice, not screaming", "urgent lyrical delivery", "steady, fast pace"; seg 4 = a hip-hop/reggae bounce with a Jamaican rapper.
# 🔑 DIAGNOSIS: r87–r91 all told the voice to be slow ("never rushing", "behind the beat", "laid back", "slow and huge") on a
# 240 s Duration that spreads 66 lines thin — slow reads as NOT aggressive; Jack at r82 wanted "the PASSION in the fast paced
# reggae voice". So: urgency/drive words, the slow family banned, Duration 240 → 205. Double-time stays banned (standing).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
BASE="double-time, chopper, raspy, gravelly, growl, female vocal, soft vocal, breathy, mellow, crooning, lazy flow, drowsy, sleepy, laid-back vocal, "
L={
 'lifeline': dict(
  style="Hard patois toaster, male, explosive consonants, pushing chest voice, urgent and driving, attacking every verse, while a strong soaring tenor belting the hook with fire. Roots one-drop, 86 bpm, tight dry kit with rim clicks, a thick melodic bass, sharp staccato offbeat guitar, Hammond underneath, spring reverb and tape throws on the vocal tails, with dubstep sub-bass surging under each hook.",
  exclude=BASE+"trap, synth brass, steel pan"),
 'urgent': dict(
  style="Rasta singjay, male, urgent and pressing forward, part singing, part chanting, pushing hard from the chest, every consonant exploding, fast steady pace, voice climbing when the anger rises. A warm woody one-drop at 90, electric piano chords, offbeat skank, deep round bass, and heavy dubstep weight dropping in beneath the loudest lines.",
  exclude=BASE+"organ, horns, trap, whispered"),
 'bounce': dict(
  style="Jamaican deejay rapping over reggae, male, punchy staccato flow, forward-leaning and hungry, every bar pushed hard, confident and cutting. A reggae hip-hop bounce at 88, punchy kick, crisp handclap snare, choppy upstroke guitar, a warm pulsing bass, and a half-speed dubstep drop with a crushing wobble.",
  exclude=BASE+"one-drop, organ, sung hook, choir"),
 'westindian': dict(
  style="West Indian roots singer, male, mature, rich and passionate, belting with a driving pace, singing hard with conviction and heat, chatting the rapid lines with bite. A driving rolling one-drop at 92, heavy saturated bass, bright washy cymbals, a warm organ, spring reverb and offbeat delay throws, and dubstep sub-bass climbing under the choruses.",
  exclude=BASE+"falsetto, trap, clap, electric piano"),
 'percussive': dict(
  style="Percussive ragga deejay, male, low baritone, loud and punchy, spitting each syllable like a drum hit, hard attack, restless and relentless, pressing ahead of the groove. A dry, tight, eighty-four bpm one-drop, rim clicks, a rubbery DI bass, staccato guitar stabs, tape delay throws, and snarling dubstep drops that hand the song to the bass.",
  exclude=BASE+"singing, sung hook, organ, horns"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r93-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=205,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
