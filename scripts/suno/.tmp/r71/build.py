import json, re, os, itertools
BASEDIR='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r70'
OUT=os.path.dirname(os.path.abspath(__file__))
CAST="Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
# 🔑 held VERBATIM from r70 jungle — "keep the vibe of the beats"
BEAT=("Breakneck jungle at 174: chopped amen breaks rolling and re-chopping every bar, ragga swing, reverse "
      "crashes into every turn, a deep round sub under it. ")
WORDS=("Every vocal sound in the record is a word from the lyrics: no humming, no ooh-ing, no whoops, "
       "nothing wordless anywhere. ")

STYLE={}
ROOM={
 'wordsonly':("It opens with a room of men saying the hook together on their own, flat and low, no drums and no "
              "instruments. A church organ answers them at the turns, and the room says the hook with him every "
              "time. "),
 'solo':     ("It opens with him alone on the hook, flat and close, no drums and no instruments and nobody with "
              "him. A church organ answers him at the turns, and he carries every hook on his own. "),
 'lastonly': ("It opens with a church organ alone at the turns of a slow figure, no drums. He carries the hooks "
              "on his own, and a room of men only joins him for the very last one, saying it flat and low. "),
}
FOOT="Big, live and room-y, like a rave taped off the desk. "
TAIL=("eight-bar bursts traded between them, heavy and unhurried, every bar landing clean and on the grid, "
      "never hurried and never dragging.")
for k in ROOM: STYLE[k]=BEAT+ROOM[k]+WORDS+FOOT+CAST+TAIL

BAN=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, hype man, crowd shouts, whoops, vocal riffs, "
 "sung harmonies, shouting, screaming, roaring, American accent, US rap, trap, autotune, "
 "pitch-corrected vocals, female vocal, cheesy, steady rap pace, lazy flow, double-time, motormouth, "
 "major key, tempo change, slow tempo, half time, jump up, wobble bass, neurofunk, dubstep, EDM drops, "
 "glossy production, happy, uplifting, orchestral bed, symphony orchestra, full orchestra, string section, "
 "grand piano, solo violin, synth strings, garage shuffle, two-step garage")
XCROSS={'wordsonly':"", 'solo':", backing vocals, male choir, crowd vocals, gang vocals",
        'lastonly':", gang vocals"}
EXCLUDE={k: BAN+XCROSS[k] for k in ROOM}

VOICE="hurt and insistent, heavy and unhurried, every word clear"
CH={
 'wordsonly':("[Chorus | the hook, the room saying it with him, words only]",
              "[Final Chorus | everything at once, the whole room saying it with him, words only]"),
 'solo':     ("[Chorus | the hook, him alone, no other voices]",
              "[Final Chorus | everything at once, still him alone on the hook]"),
 'lastonly': ("[Chorus | the hook, him alone, no other voices]",
              "[Final Chorus | everything at once, a room of men joining him for the first time, words only]"),
}
def words_only(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
base=json.load(open(f'{BASEDIR}/jungle.json'))['lyrics']
LYR={}
for k in ROOM:
    l=base
    l=l.replace("[Verse 1 | straight off the hook, no drums yet | gruff grime MC, close and bitter]",
                "[Verse 1 | no drums yet | gruff grime MC, close and bitter]")
    l=l.replace("[Drop | the amen drops on this line]","[Drop | the amen drops on this line]")
    l=l.replace("[gruff grime MC, hurt and insistent, short sharp bursts, high energy, clean on the grid]",
                f"[gruff grime MC, {VOICE}]")
    l=l.replace("[cold grime MC, clipped and cold, short sharp bursts, high energy, clean on the grid]",
                f"[cold grime MC, clipped and cold, {VOICE}]")
    l=l.replace("[Chorus | the hook, the room joining in]", CH[k][0])
    l=l.replace("[Final Chorus | everything at once, the whole room]", CH[k][1])
    assert words_only(l)==words_only(base), f"{k}: WORDS CHANGED"
    assert l.count('\n')==base.count('\n')
    assert 'high energy' not in l and 'short sharp bursts' not in l, f"{k}: fast cue survived"
    LYR[k]=l

def longest(a,b):
    best=""
    for i in range(len(a)):
        for j in range(len(b)):
            m=0
            while i+m<len(a) and j+m<len(b) and a[i+m]==b[j+m]: m+=1
            if m>len(best): best=a[i:i+m]
    return best
# 🔑 DEEPENING round, not a variety round: the beat, the anti-ooh clause, the production
# sentence and the cast are MEANT to be identical. The only thing that may differ is the room.
ALLOWED=[BEAT, ". "+WORDS+FOOT+CAST+TAIL]
for x,y in itertools.combinations(STYLE,2):
    r=longest(STYLE[x],STYLE[y])
    print(f"  shared {x}/{y}: {len(r)} chars = {100*len(r)/min(len(STYLE[x]),len(STYLE[y])):.0f}%")
    assert any(r in A for A in ALLOWED), f"{x}/{y}: {r[:60]!r}"
for k in STYLE:
    print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])}")
assert all(len(STYLE[k])<=1000 and len(EXCLUDE[k])<=1000 for k in STYLE)
for k in STYLE:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":LYR[k],"model":"v6",
      "title":f"camping-r71-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":190,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ r71: 3 specs (the shared text IS the brief — beat held verbatim, anti-ooh clause, cast)")
