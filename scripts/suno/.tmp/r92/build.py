import json, os
# r92 — Jack 2026-09-27 (6th time, same words): aggressive Rasta reggae vocals always, voice varied; built off
# "STRICTLY DUB • Best of TRIPPY Dub Groove 2023 • Special Coffeeshop Selection [Seven Beats Music]" (youtube VVmgwyRyk_M).
# Heard (gemini-3.5-flash-lite — the full models are out of quota — 4 × 60 s): slow hypnotic trippy dub ~86-90 (librosa);
# sparse organic kit, rimshots, wet shakers + woodblocks in slapback; a hypnotic four-note sub ostinato; ghostly delay-drenched
# guitar skank + single-note lines through a low-pass sweep; spring reverb, long tape feedback, filtered sirens, phased pads;
# dark, warm, saturated, rolled-off highs; one four-on-the-floor dub-club track (clip 3); only voice = calm French spoken word.
# Research: D-Echo Project (PT) blends dub/funk/jazz/electronica; Mountaindub = dub/psybient. Suno guides: TONE and technique
# words carry a voice more reliably than mood words, and a laid-back reggae bed pulls against "aggressive" — so this round the
# front-loaded voice sentence is written in TONE/TECHNIQUE words (loud, powerful, chest voice, hard attack, projected, megaphone)
# and the excludes ban soft TIMBRES (soft, breathy, whispered, mellow). Gravel stays banned (Jack r82). Carry-over audited.
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
BASE="double-time, chopper, raspy, gravelly, female vocal, soft vocal, breathy, whispered, mellow, crooning, spoken word, "
L={
 'ostinato': dict(
  style="Ragga toaster, male, loud and powerful, hard chest voice, every syllable struck with a hard attack, patois, forceful. Beneath him: slow hypnotic dub, a four-note sub-bass figure repeating like a spell, sparse rimshots, woodblocks and shakers bouncing in slapback, a ghostly guitar skank in a low-pass sweep, while dubstep sub-bass hits like a lorry under his hooks.",
  exclude=BASE+"French, four-on-the-floor, bright pop"),
 'megaphone': dict(
  style="Militant Rasta street orator, male, projected and loud like he is shouting through a megaphone, clipped, cutting, every word hurled into the street, commanding. Dark, phased, trippy dub underneath: deep kick, snare with a long spring tail, swirling tape echo, filtered sirens drifting across, heavy saturated low end, a wall of dubstep sub rising where he is loudest.",
  exclude=BASE+"French, sweet, pop, acoustic"),
 'clubdub': dict(
  style="Dancehall deejay, male, sharp and punchy, staccato bursts, loud shouted edges on the ends of phrases, hyped and hard. A dub club groove, kick on all four beats, deep sub pumping with the kick, rolling electronic hats, pitched-down chant loops in reverb, filter sweeps, then half-speed dubstep breakdowns, a thick wobbling bass.",
  exclude=BASE+"French, one-drop, acoustic, sweet"),
 'booming': dict(
  style="Deep-voiced Rasta deejay, male, low booming chest voice, heavy and forceful, huge projection, words dropped like hammers, dread and uncompromising. A slow warm trippy dub with a haunted single-note guitar melody lost in delay, sparse organic drums, wet percussion, rolled-off highs, and massive dubstep sub pressure beneath each hook.",
  exclude=BASE+"French, high-pitched, four-on-the-floor"),
 'beltdub': dict(
  style="Rasta singjay, male, belting in a high powerful chest voice, strained with intensity, loud and ringing, flipping into hard-hitting chat between sung lines. A dark hypnotic dub with ambient synth leads held long, a tape echo spiralling into self-oscillation, spring reverb crashes, filtered sirens, and dubstep drops with the sub-bass snarling.",
  exclude=BASE+"French, falsetto, four-on-the-floor, acoustic"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r92-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
