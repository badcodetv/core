import json, re, os
R71='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'
R75='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r75/raggajungle.json'
OUT=os.path.dirname(os.path.abspath(__file__))
r71=json.load(open(R71)); r75=json.load(open(R75))

# Jack 2026-09-24: 36d0b981, but sounding like two references (heard in full by Gemini, logs
# docs/listening/log/2026-09-24-1028*-ref-*). Never name the artists in a box. Never double-time rap.
LANE={
 'jamrock':("Heavy half-time reggae hip-hop riddim at 80: a deep punchy kick on the one, a dry cracking "
   "rimshot snare on the three, tight eighth-note hats, a massive warm walking sub carrying the tune. One "
   "hypnotic loop, sparse and dark, a dub siren sweeping in at every section, tape delay and spring reverb "
   "thrown off his line-ends and the snare. It opens on a low tense drone with him alone, quiet and begging, "
   "and the riddim slams in with the siren on 'you keep on walking'. "),
 'bundem':("Reggae dubstep at 140, half-time: kick on the one, a sharp metallic snare cracking on the three, "
   "reggae swing in the offbeat hats, a clean round sub walking under offbeat synth-brass skanks for the "
   "verses. Snare rolls and risers build into drops where the bass turns into a tearing, growling formant "
   "wobble with a screeching laser lead, then back to the clean riddim. Dub sirens, long tape echo on his "
   "line-ends, a sparse dub-echo breakdown to end. It opens on the synth-brass with him alone, quiet and "
   "begging, and the first drop lands on 'you keep on walking'. "),
}
SHARED=("A church organ answers at the turns. The hook comes quick, a room of men saying it with him flat "
 "and low, words only. Every vocal sound is a word from the lyrics, nothing wordless anywhere. Two English "
 "grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, riding the slow "
 "half-time pulse, heavy and unhurried, every word clear.")
STYLE={k: LANE[k]+SHARED for k in LANE}

BASE=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, vocal chops, hype man, crowd shouts, whoops, "
 "vocal riffs, sung harmonies, singing, sung hook, melodic chorus, soulful vocal, crooning, roots reggae "
 "singer, lovers rock, shouting, screaming, roaring, American accent, US rap, trap, autotune, "
 "pitch-corrected vocals, female vocal, cheesy, double-time, double-time rap, fast rap, rapid-fire flow, "
 "chopper rap, speed rap, motormouth, major key, happy, uplifting, glossy production, reggaeton, tropical "
 "house, ska, oompah, orchestral bed, symphony orchestra, string section, grand piano")
EXCLUDE={
 'jamrock': BASE+", brass band, dubstep, wobble bass, EDM drops, drum and bass, jungle, amen break, risers",
 'bundem':  BASE+", drum and bass, jungle, amen break, trance, big room",
}

def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
R=[("[Verse 1 | one-drop riddim, organ skank | gruff grime MC, quiet, close and begging, unhurried]",
    "[Verse 1 | riddim stripped back | gruff grime MC, quiet, close and begging, unhurried]"),
   ("[gruff grime MC, rising, close to cracking]","[gruff grime MC, raw, close to cracking, unhurried]"),
   ("[Chorus | the hook, the room saying it with him, words only]",
    "[Chorus | the room says the hook with him, spoken flat, words only]"),
   ("[cold grime MC, sharper]","[cold grime MC, sharper, still unhurried]"),
   ("[Chorus | the beat cuts dead for the first line, then everything back]",
    "[Chorus | the beat cuts dead for the first line, then everything back, spoken flat]"),
   ("[Bridge | the two grime MCs trade lines, close and overlapping]",
    "[Bridge | the two grime MCs take turns, slow and heavy, space between every line]"),
   ("[Final Chorus | everything at once, the whole room saying it with him, words only]",
    "[Final Chorus | everything at once, the whole room saying it with him, spoken flat, words only]")]
lyr=r75['lyrics']
for a,b in R:
    assert lyr.count(a)==1, a
    lyr=lyr.replace(a,b)
assert wo(lyr)==wo(r71['lyrics']) and lyr.count('\n')==r71['lyrics'].count('\n')
cues=' '.join(re.findall(r'\[[^\]]*\]',lyr)).lower()
for bad in ['fast','breakneck','sprint','on the grid','double','overlapping','rising','marley','skrillex','jamrock']:
    assert all(bad not in s.lower() for s in STYLE.values()) and bad not in cues, bad
for k in STYLE:
    print(f"{k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])}")
    assert len(STYLE[k])<=1000 and len(EXCLUDE[k])<=1000
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":lyr,"model":"v6",
      "title":f"camping-r76-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":240,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ r76: 2 lanes, lyrics canon-identical, Duration 240")
