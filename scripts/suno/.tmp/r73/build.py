import json, re, os, itertools
BASE='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'
OUT=os.path.dirname(os.path.abspath(__file__))
prev=json.load(open(BASE))

# 🔒 FROZEN — the four things Jack named on 36d0b981. Identical in every lane, on purpose.
FROZEN=("No drums at first: three lines of him alone, quiet and begging, then the beat drops on 'you keep on "
 "walking'. The hook comes quick, a room of men saying it with him flat and low, words only. Every vocal "
 "sound is a word from the lyrics, nothing wordless anywhere. "
 "Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
 "eight-bar bursts traded between them, heavy and unhurried, every bar landing clean and on the grid, never "
 "hurried and never dragging.")

# 🔑 The lane clause goes FIRST — Suno weights the opening tokens hardest, so what differs is read first.
LANE={
 'spiccato':("Tight rolling drum and bass at 174, crisp dry snare, hats sprinting. Short spiccato violin stabs "
   "lock to the hats and play the break's own pattern back, and one lone violin answers him at the end of "
   "every bar. Chopped amen fills at every section turn. Close, dry, precise and mid-forward, like a pirate "
   "radio rip. "),
 'harpcello':("Loose broken-beat drum and bass at 174, swung and off-kilter. A harp runs one arpeggio under the "
   "break like a hi-hat pattern, and low cellos double the sub an octave up in long bowed lines. Warm, wide "
   "and slightly blurred, the low end round rather than sharp, everything sitting a fraction behind the beat. "),
 'dubecho':("Half-stepping drum and bass at 174 with big gaps in it and a heavy offbeat skank chord, tape echo "
   "throwing the ends of his lines away across a long spring reverb, one siren sweeping the stereo field. "
   "Cavernous and wet, enormous empty space between the hits, the sub landing like a door closing. "),
 'machine':("Relentless mechanical drum and bass at 174 with no swing in it at all, snares layered with metallic "
   "clicks, hi-passed pots and pans on the kick, banging pipes and a construction-site clang for percussion, a "
   "distorted machine loop grinding underneath. Cold, abrasive and inhuman, mixed narrow and hard with no air "
   "in it at all. "),
 'square':("Skippy drum and bass at 174 built on one eight-bar loop with very clear single hits and no "
   "percussion layers at all. Detuned square-wave stabs and a gliding sine lead carry the whole tune, the "
   "filter opening a little further at every turn, a twisty gliding bass underneath. Boxy, cheap, cold and "
   "deliberately unpolished, like it was made on a games console. "),
}
STYLE={k: LANE[k]+FROZEN for k in LANE}

BAN=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, hype man, crowd shouts, whoops, vocal riffs, "
 "sung harmonies, shouting, screaming, roaring, American accent, US rap, trap, autotune, "
 "pitch-corrected vocals, female vocal, cheesy, steady rap pace, lazy flow, slow flow, double-time, "
 "motormouth, major key, tempo change, slow tempo, half time, jump up, wobble bass, neurofunk, dubstep, "
 "EDM drops, glossy production, happy, uplifting, orchestral bed, symphony orchestra, full orchestra, "
 "string section, church organ, grand piano")
XC={
 'spiccato': ", harp, cello, tape echo, spring reverb, square-wave lead, sine lead, metallic percussion",
 'harpcello':", spiccato, violin stabs, tape echo, spring reverb, square-wave lead, sine lead, metallic percussion",
 'dubecho':  (", harp, cello, spiccato, violin stabs, square-wave lead, sine lead, metallic percussion, "
              "ragga MC, toasting, Jamaican accent, dancehall vocal, ska, oompah, brass band"),
 'machine':  ", harp, cello, spiccato, violin stabs, tape echo, spring reverb, square-wave lead, sine lead",
 'square':   ", harp, cello, spiccato, violin stabs, tape echo, spring reverb, metallic percussion",
}
EXCLUDE={k: BAN+XC[k] for k in LANE}

def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
lyr=prev['lyrics'].replace(
 "[Verse 1 | no drums yet | gruff grime MC, close and bitter]",
 "[Verse 1 | no drums at all | gruff grime MC, quiet, close and begging, unhurried]")
assert wo(lyr)==wo(prev['lyrics']) and lyr.count('\n')==prev['lyrics'].count('\n')
assert 'begging' in lyr and 'the room saying it with him, words only' in lyr

def longest(a,b):
    best=""
    for i in range(len(a)):
        for j in range(len(b)):
            m=0
            while i+m<len(a) and j+m<len(b) and a[i+m]==b[j+m]: m+=1
            if m>len(best): best=a[i:i+m]
    return best
for x,y in itertools.combinations(STYLE,2):
    r=longest(STYLE[x],STYLE[y])
    assert (FROZEN in r and len(r)-len(FROZEN)<=4) or r in FROZEN, f"{x}/{y} shares LANE language: {r[:70]!r}"
    print(f"  shared {x}/{y}: {len(r)} chars = {100*len(r)/min(len(STYLE[x]),len(STYLE[y])):.0f}%  (= the frozen spine)")
for k in STYLE: print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])} lane={len(LANE[k])}")
assert all(len(STYLE[k])<=1000 and len(EXCLUDE[k])<=1000 for k in STYLE)
for k in STYLE:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":lyr,"model":"v6",
      "title":f"camping-r73-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":190,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ r73: 5 specs — lane clause first, frozen spine after, lyrics identical across lanes")
