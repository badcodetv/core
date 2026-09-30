import json, os
# r88 — Jack 2026-09-27: "we have lost the aggressive rasta vocals, that should always stay reggae and aggressive, but make
# the voice vary, whilst remaining reggae in each song." Built off ONE reference: Damian Marley ft. Nas, "Road To Zion"
# (youtube I3g7UkOf5u4; prod. Stephen Marley; samples Ella Fitzgerald "Russian Lullaby"; ~92-93 bpm).
# Gemini (gemini-3-flash-preview) on four segments: reggae-swung boom-bap at ~92, knocking kick, wood-crack snare, round
# melodic bass, a minor-key plucked (kora/acoustic) loop and a melancholy Rhodes, a sampled sung hook loop, dub throws on
# vocals, vinyl crackle, warm analogue; Jamaican deejay with sharp aggressive consonants, behind the beat, sung chanted hook,
# shouted ad-libs. Research: Damian's fire comes from the hardcore dancehall deejays he saw at Sunsplash; his production
# studies Sly & Robbie's early-80s digital roots. Nothing from r87 or earlier (carryover.py). Voices: aggressive + Rasta +
# reggae in all five, a DIFFERENT voice in each; never gravel/rasp words (Jack r82); never double-time (standing rule).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
L={
 'zionwalk': dict(
  style="Conscious reggae-rap crossover, 92 bpm, a knocking boom-bap kit with a reggae swing, a wood-crack snare, a round melodic bass walking under a sorrowful minor loop plucked on kora and nylon guitar, a sampled soul voice looping the hook far away, vinyl crackle, warm analogue saturation, dub echo flung off his last words, a deep sub dropping in under the hook. A young Rasta deejay with righteous fire, spitting every consonant like a punch, furious and precise, riding behind the beat, then chanting the hook with his chest out. Shouted 'boom' and 'yeah man' ad-libs in the echo.",
  exclude="double-time, chopper, raspy, gravelly, mellow, crooning, American rapper, trap hats, orchestra, wobble bass"),
 'pulpit': dict(
  style="Dark militant reggae, 140 bpm, its body a slow dubstep crawl: slow crushing drums, an offbeat skank chop, a mournful minor Rhodes phrase repeating like a warning, and a massive dubstep sub that rises and roars at every turn of the song. A Rasta preacher at the pulpit, thundering and prophetic, chanting judgement on Babylon with total fury, deep chest voice, every line a sermon, measured and heavy with long echoes on his last words. Black, heavy, cinematic, reverb-soaked.",
  exclude="double-time, chopper, raspy, gravelly, sweet, crooning, pop, bright, kora, acoustic, vinyl crackle, horns"),
 'bashment': dict(
  style="Hardcore digital dancehall riddim, early eighties drum machine and a fat synth bassline, stark and minimal, a Casio-style stab, snare cracking like a gunshot, then dubstep drops: the synth bass mutates into a filthy, snarling wobble and the drums go half speed. A dancehall deejay in full fury, explosive, hyped and confrontational, punching every word out at the crowd, commanding the dance, patois heavy, riding the riddim tight but never rushing. Sound system hype, raw and loud, lo-fi digital grit.",
  exclude="double-time, chopper, raspy, gravelly, singing, crooning, mellow, piano, strings, kora, organ, polished"),
 'singjay': dict(
  style="Roots one-drop, 80 bpm, rimshot and kick landing together, a deep walking bass, a Hammond holding soft chords, a looped sampled singer wailing a two-word hook from an old record, dub delays everywhere, crackle and warmth. Then the bass drops into a slow dubstep weight under the one-drop. A Rasta singjay, high tenor, burning with passion, flipping between soaring sung cries and furious chatted bursts, pleading then attacking, raw emotion, always sitting late on the pulse.",
  exclude="double-time, chopper, raspy, gravelly, autotune, boom-bap, drum machine, piano, horns, brostep, trap"),
 'elder': dict(
  style="An old 1940s jazz lullaby record, strings and a clarinet, crackling and warped, chopped into a sorrowful minor loop over hard-hitting reggae hip-hop beats with a bottomless dubstep sub-bass, dub siren, spring echo. A Rasta elder deejay with a deep, commanding voice, bitter and fiery, toasting like he has seen it all and is done being patient, every word hard and clear, lazy on the beat but hitting like a hammer, the hook chanted as a warning. Dusty, smoky, cavernous, huge low end.",
  exclude="double-time, chopper, raspy, gravelly, youthful, sweet, crooning, synth, drum machine, bright, kora, pop"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r88-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
