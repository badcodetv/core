import json, os, re
# r83 — Jack 2026-09-26: a NEW song "based entirely off" Dub Zone's mix (youtube kTSQfQOEJMk), reggae with
# some dubstep, Camping's words unchanged, otherwise complete freedom. Nothing inherited from r77–r82 but the
# words and the standing never-double-time rule (+ autotune, Jack's "too cheesy").
# Gemini heard 3 of 4 samples (0:40, 37:40, 57:40; 19:40 unheard, API 503): one-drop ~80 or half-time 135–140,
# melodica lead mournful/minor, a horn section taking the B-section, spring-reverbed guitar skank + low 16th organ
# bubble, dub siren + drop-outs to bass-and-drums, tape delay on the last snare of a phrase, warm dark vintage mix;
# sample 1 = a clean smooth male singer singing doom words over a breezy groove.
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
B=[b.strip() for b in open(f'{T}/r81/lyrics.txt').read().split('\n\n')]
assert len(B)==7 and B[2]==B[4]==B[6]
def lyr(tags): return '\n\n'.join(f'[{t}]\n{b}' if t else b for t,b in zip(tags,B))
STD="double-time, double-time rap, fast rap, rapid-fire flow, chopper rap, speed rap, motormouth, autotune, pitch-corrected vocals"
L={
 'rootsstep': dict(
  style="Roots dub reggae meets dubstep at 140, half-time one-drop: kick and side-stick together on the three, a deep round sub rolling a minor riff, a spring-reverbed guitar skank on the offbeat, a quiet rolling organ bubble, a mournful melodica carrying the tune and a warm horn section taking over in the chorus. Dub drop-outs to bass and drums, a dub siren, tape delay thrown off the last snare of the phrase. The drops turn the sub into a slow, deep, heavy dubstep wobble under the same one-drop, then fall back into the dub. Warm, dark, smoky, spacious, vintage tape. A roots reggae singer, male, Jamaican, mournful and soulful, rich and in tune, sings the verses and the hook, every word clear, unhurried.",
  exclude=STD+", screeching lead, brostep, riser, EDM build, trap, pop, bright, female vocal, choir, strings, piano, rock guitar",
  tags=['Intro: melodica over drums and bass','','Chorus','Drop','Chorus','Dub break','Final Chorus']),
 'sunnydoom': dict(
  style="Breezy modern reggae at 80, clean one-drop, rimshot on the three, tight closed hats, a round melodic walking bassline, a clean muted guitar skank and organ stab, a bright plaintive melodica hook between lines, polished hi-fi, crisp and warm. A smooth young male singer, clear English accent, sings the words sweetly and calmly as if nothing is wrong, the doom in the words against the sunshine in the music. Then the ground gives way: the hook drops into a dark, crushing half-time dubstep bass, heavy growling wobble and a deep sub, the singer still calm on top, then back to the sunshine. Plate reverb and timed delay on the voice and the melodica.",
  exclude=STD+", ragga, toasting, rap, gravelly voice, shouting, vintage tape hiss, lo-fi, spring reverb, dub siren, horns, trap hats, female vocal, choir, strings",
  tags=['Verse','','Chorus','Verse','Chorus','Bridge','Final Chorus']),
 'deepdub': dict(
  style="Deep dub and meditative dubstep at 140, half-time: a bone-dry kick and a cracking side-stick, hypnotic steppers pressure, a vast clean sub-bass rolling underneath like weather, sparse spring-reverbed skank chords that throw into long feedback echo, a distant melodica phrase answering, a single horn hit echoing into the dark. The whole thing drops out to just bass and voice, then crashes back in. Smoky, nocturnal, dark and wide, tape-saturated, huge low end, very sparse. A Rasta chanter, deep-set and fiery, chants and half-sings the lines with total conviction, laid back behind the beat, every word clear, his line-ends thrown into dub echo.",
  exclude=STD+", wobble, growl bass, brostep, screeching lead, riser, EDM, pop, polished, bright, major key, female vocal, choir, strings, piano, guitar solo",
  tags=['Intro','','Chorus','','Chorus','Bass and voice only','Final Chorus']),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r83-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[40,60],durationSec=240,
           variety='off',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=lyr(v['tags']))
    wo=lambda t: re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
    assert wo(d['lyrics'])==wo(open(f'{T}/r81/lyrics.txt').read())
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000, (k,len(d['style']))
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
