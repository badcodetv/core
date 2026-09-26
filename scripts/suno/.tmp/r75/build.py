import json, re, os, itertools
R71='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'
R74='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r74/onedrop230.json'
OUT=os.path.dirname(os.path.abspath(__file__))
r71=json.load(open(R71)); r74=json.load(open(R74))

# Jack 2026-09-24: r74 "lost all other elements from the song i referenced" — put 36d0b981's themes
# back (amen drop, church organ at the turns, the room saying the hook, the rave-off-the-desk sound)
# around the reggae passage. And NEVER double-time rap: the MCs ride the slow pulse over the breaks.
REGGAE=("a one-drop reggae riddim with ragga swing: rim click on the three, a warm walking sub, a clean "
 "organ skanking on the offbeats, his line-ends thrown into feedback delay. ")
LANE={
 'raggajungle':("Ragga jungle at 174 that opens as "+REGGAE+
   "Three lines of him alone on it, quiet and begging, then a snare roll and the amen breaks drop on 'you keep "
   "on walking', chopped and rolling, reverse crashes into every turn, a deep sub growling under it, the organ "
   "skank riding on over the breaks. "),
 'switch':("Verses on "+REGGAE+
   "It opens on the riddim with him alone, quiet and begging. Every hook flips into ragga jungle at 174, amen "
   "breaks chopped and rolling, reverse crashes, a deep sub growling, then drops back to the riddim for the "
   "next verse. "),
}
SHARED=("A church organ answers at the turns. The hook comes quick, a room of men saying it with him flat and "
 "low, words only. Every vocal sound is a word from the lyrics, nothing wordless anywhere. Big, live and "
 "room-y, like a rave taped off the desk. Two English grime MCs trade the verses, loud and in front, one "
 "gruff and raw, one clipped and cold, riding the slow half-time pulse under the breaks, heavy and "
 "unhurried, every word clear.")
STYLE={k: LANE[k]+SHARED for k in LANE}

# r71's bans, audited: dropped `slow tempo, half time, lazy flow, steady rap pace, tempo change` (they ban
# the pace / the flip). Fast-rap family and reggae's singer family added (r74 sang the hook).
EXCLUDE=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, hype man, crowd shouts, whoops, vocal riffs, "
 "sung harmonies, singing, sung hook, melodic chorus, soulful vocal, crooning, roots reggae singer, "
 "lovers rock, shouting, screaming, roaring, American accent, US rap, trap, autotune, pitch-corrected "
 "vocals, female vocal, cheesy, double-time, double-time rap, fast rap, rapid-fire flow, chopper rap, "
 "speed rap, motormouth, major key, happy, uplifting, glossy production, jump up, wobble bass, "
 "dubstep, EDM drops, reggaeton, tropical house, ska, brass band, oompah, orchestral bed, symphony "
 "orchestra, string section, grand piano")

def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
lyr=r74['lyrics'].replace("[Verse 1 | organ, sub and rim click only | gruff grime MC, quiet, close and begging, unhurried]",
  "[Verse 1 | one-drop riddim, organ skank | gruff grime MC, quiet, close and begging, unhurried]"
 ).replace("[the full riddim comes in on this line]","[Drop | everything drops in on this line]")
assert wo(lyr)==wo(r71['lyrics']) and lyr.count('\n')==r71['lyrics'].count('\n')
cues=' '.join(re.findall(r'\[[^\]]*\]',lyr)).lower()
for bad in ['fast','breakneck','sprint','on the grid','double']:
    assert all(bad not in s.lower() for s in STYLE.values()) and bad not in cues, bad
for k in STYLE:
    print(f"{k}: style={len(STYLE[k])} exclude={len(EXCLUDE)}"); assert len(STYLE[k])<=1000
assert len(EXCLUDE)<=1000
for k in STYLE:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE,"lyrics":lyr,"model":"v6",
      "title":f"camping-r75-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":230,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ r75: 2 lanes, lyrics canon-identical, Duration 230")
