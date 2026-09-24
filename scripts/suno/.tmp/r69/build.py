import json, re, os
SRC='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r68/violin.json'
OUT=os.path.dirname(os.path.abspath(__file__))
prev=json.load(open(SRC))

# ── the merged body: sentences taken from BOTH liked takes' own Style boxes ──
BODY=("174 BPM drum and bass with grime over it: a solid punchy beat, full breakbeats and a heavy rolling "
 "sub, never jump up, and the track builds from there. Skippy two-step garage shuffles folded into the drum "
 "and bass, a dark reese bass that grows meaner every section, chopped amen fills at every section turn, "
 "cheap synth strings, handclaps on the backbeat, a church organ at the turns. A room of men answers him on "
 "the hook, low and close. Night-bus melancholy. ")
CAST=("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
      "fast and clear, never rushing and never slowing for a punchline.")
OPENING={
 'merge':   "",
 'beatfirst':"The beat hits hard from the very first bar, no intro. ",
 'opencold':"It opens with no drums: a piano and a lone violin, the first MC close for three lines, then the "
            "beat lands on 'you keep on walking'. ",
}
STYLE={k: BODY+OPENING[k]+CAST for k in OPENING}

EXCLUDE=("American accent, American vocal, US rap, trap, teenage voice, falsetto, autotune, pitch-corrected "
 "vocals, female vocal, gospel choir, cheesy, jump up, wobble bass, neurofunk, dubstep, EDM drops, glossy "
 "production, happy, uplifting, major key, slow tempo, half time, tempo change, britpop, folk, pub rock, "
 "steady rap pace, double-time, motormouth, shouting, screaming, roaring, orchestral bed, symphony orchestra, "
 "full orchestra, string section")

# ── lyrics: the canon words, cues stripped back hard ──
CUES=[
 ("[Verse 1 | no drums, only the piano and the strings the track opens on | gruff grime MC, quiet, close and bitter, three lines only]",
  "[Verse 1 | gruff grime MC, close and bitter]"),
 ("[Drop | one beat of silence, then the break and the Reese arrive together on this line, whole and controlled rather than louder]",
  "[Drop | the beat arrives on this line]"),
 ("[gruff grime MC from here, hurt and insistent, aggressive but held back, low and murky, fast but every word clear, landing hard on every beat without raising his voice, never rushing and never pausing mid-line]",
  "[gruff grime MC, hurt and insistent, fast and clear]"),
 ("[gruff grime MC, more insistent, hurt, voice close to cracking but never shouting]",
  "[gruff grime MC, rising, close to cracking]"),
 ("[gruff grime MC, a bitter plea, voice breaking]", "[gruff grime MC, a bitter plea]"),
 ("[Chorus | the gruff grime MC says each line, the room answers the last three words back low and close, half-spoken in unison, nobody sings and nobody shouts]",
  "[Chorus | the hook, the room joining in]"),
 ("[Verse 2 | straight in, no break, the beat fuller than verse one | cold grime MC, fast but every word clear, clipped, cold and contemptuous, quiet menace rather than volume, every consonant landing]",
  "[Verse 2 | straight in, no break | cold grime MC, clipped and cold, fast and clear]"),
 ("[cold grime MC, sharper and colder, biting]", "[cold grime MC, sharper]"),
 ("[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything returns fuller than the first chorus | the room answering low and close, nobody sings and nobody shouts]",
  "[Chorus | the beat cuts dead for the first line, then everything back]"),
 ("[Bridge | straight in, no break, the beat at its fullest | the two grime MCs trade lines fast and clear, close and overlapping, both hurt, neither raising his voice]",
  "[Bridge | the two grime MCs trade lines, close and overlapping]"),
 ("[Final Chorus | the fullest moment of the record, everything at once, the whole room answering every line straight back at him low and close, nobody sings and nobody shouts]",
  "[Final Chorus | everything at once, the whole room]"),
]
def words_only(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
base=prev['lyrics']
for a,b in CUES:
    assert a in base, "CUE NOT FOUND: "+a[:70]
    base=base.replace(a,b)
assert words_only(base)==words_only(prev['lyrics']), "LYRIC WORDS CHANGED"
assert base.count('\n')==prev['lyrics'].count('\n')
assert base.count('grime MC')>=12

LYR={}
for k in OPENING:
    l=base
    if k=='beatfirst':
        l=l.replace("[Drop | the beat arrives on this line]","[Drop | the record opens up on this line]")
    LYR[k]=l
    assert words_only(l)==words_only(prev['lyrics'])

cue_chars=sum(len(c) for c in re.findall(r'\[[^\]]*\]', base))
print(f"  cues: {cue_chars} chars (was {sum(len(c) for c in re.findall(r'[[][^]]*[]]', prev['lyrics']))})")
for k in OPENING:
    print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE)}")
assert all(len(STYLE[k])<=1000 for k in STYLE) and len(EXCLUDE)<=1000
for k in OPENING:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE,"lyrics":LYR[k],"model":"v6",
      "title":f"camping-r69-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":185,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ wrote 3 specs · lyric lines", base.count(chr(10))+1)
