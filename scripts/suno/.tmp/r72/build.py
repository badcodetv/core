import json, re, os, itertools
BASE='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r70/reese.json'
OUT=os.path.dirname(os.path.abspath(__file__))
prev=json.load(open(BASE))
CAST="Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
WORDS=("Every vocal sound is a word from the lyrics: no humming, no ooh-ing, no whoops, nothing wordless. ")

STYLE={}
STYLE['reesegarage']=(
 "A filthy reese bass IS the tune of this record, growing meaner every section, and it sits on a skippy UK "
 "garage two-step at 174 with swung hats and a shuffle that bounces. Reese and shuffle together from the "
 "very first bar, no intro. Cheap synth strings stab on the offbeat against them, never a pad. Chopped amen "
 "fills at every section turn. " + WORDS +
 "Warm, bouncy and mid-forward, like a pirate radio rip, night-bus melancholy. "
 + CAST + "talky and conversational, telling it to you at four in the morning, long unhurried verses.")

STYLE['reeseamen']=(
 "A filthy reese bass IS the tune of this record, growing meaner every section, dragged across breakneck "
 "chopped amen breaks at 174 that roll and re-chop every bar, ragga swing, reverse crashes into every turn. "
 "It starts on that reese alone for four bars with no drums. A room of men says the hook with him, flat and "
 "low, words only. " + WORDS +
 "Big, live and room-y, like a rave taped off the desk. "
 + CAST + "eight-bar bursts traded between them, heavy and unhurried, landing clean on the grid.")

STYLE['reesehalf']=(
 "A filthy reese bass IS the whole record at 174, growing meaner every section, with the drums pulled right "
 "back to a dry sparse roller that has almost nothing in it, a rimshot and a hat and the sub. It opens on "
 "one solo violin and that reese together, no drums at all, the violin holding a long line an octave above "
 "it and bending where it bends. " + WORDS +
 "Narrow, cold and enormous underneath, nothing else in the room. "
 + CAST + "low and murky, several octaves down, drawing single words right out with menace.")

BAN=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, hype man, crowd shouts, whoops, vocal riffs, "
 "sung harmonies, shouting, screaming, roaring, American accent, US rap, trap, autotune, "
 "pitch-corrected vocals, female vocal, cheesy, steady rap pace, lazy flow, double-time, motormouth, "
 "major key, tempo change, slow tempo, half time, jump up, wobble bass, neurofunk, dubstep, EDM drops, "
 "glossy production, happy, uplifting, orchestral bed, symphony orchestra, full orchestra, string section, "
 "church organ, grand piano")
XC={'reesegarage':", solo violin, male choir, crowd vocals, backing vocals, jungle, amen assault",
    'reeseamen':  ", solo violin, synth strings, garage shuffle, two-step garage",
    'reesehalf':  ", synth strings, garage shuffle, two-step garage, male choir, crowd vocals, backing vocals, amen assault"}
EXCLUDE={k: BAN+XC[k] for k in STYLE}
DUR={'reesegarage':190,'reeseamen':185,'reesehalf':190}
VOICE={'reesegarage':"talky and unhurried, riding the shuffle",
       'reeseamen':"heavy and unhurried, clean on the grid",
       'reesehalf':"low and murky, drawing single words out, menacing"}
OPENCUE={'reesegarage':"[Verse 1 | the reese and the shuffle already rolling | gruff grime MC, close and bitter]",
         'reeseamen':"[Verse 1 | the reese alone, no drums | gruff grime MC, close and bitter]",
         'reesehalf':"[Verse 1 | the violin and the reese alone, no drums | gruff grime MC, close and bitter]"}
CH={'reesegarage':("[Chorus | the hook, him alone, no other voices]","[Final Chorus | everything at once, still him alone on the hook]"),
    'reeseamen':("[Chorus | the hook, the room saying it with him, words only]","[Final Chorus | everything at once, the whole room saying it with him, words only]"),
    'reesehalf':("[Chorus | the hook, him alone, no other voices]","[Final Chorus | everything at once, still him alone on the hook]")}

def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
base=prev['lyrics']; LYR={}
for k in STYLE:
    l=base
    l=l.replace("[Verse 1 | the reese alone, no drums | gruff grime MC, close and bitter]", OPENCUE[k])
    l=l.replace("[gruff grime MC, hurt and insistent, low and murky, drawing single words out, menacing]",
                f"[gruff grime MC, hurt and insistent, {VOICE[k]}]")
    l=l.replace("[cold grime MC, clipped and cold, low and murky, drawing single words out, menacing]",
                f"[cold grime MC, clipped and cold, {VOICE[k]}]")
    l=l.replace("[Chorus | the hook, the room joining in]", CH[k][0])
    l=l.replace("[Final Chorus | everything at once, the whole room]", CH[k][1])
    assert wo(l)==wo(base), f"{k}: WORDS CHANGED"
    assert l.count('\n')==base.count('\n')
    assert VOICE[k] in l, f"{k}: voice cue missing"
    LYR[k]=l

def longest(a,b):
    best=""
    for i in range(len(a)):
        for j in range(len(b)):
            m=0
            while i+m<len(a) and j+m<len(b) and a[i+m]==b[j+m]: m+=1
            if m>len(best): best=a[i:i+m]
    return best
ALLOWED=[". "+WORDS, WORDS, ". "+CAST, "A filthy reese bass IS the "]
worst=0
for x,y in itertools.combinations(STYLE,2):
    r=longest(STYLE[x],STYLE[y]); pct=100*len(r)/min(len(STYLE[x]),len(STYLE[y])); worst=max(worst,pct)
    print(f"  shared {x}/{y}: {len(r)} chars = {pct:.0f}%  -> {r[:45]!r}")
    assert any(r in A for A in ALLOWED), f"{x}/{y} shares production language: {r[:70]!r}"
for k in STYLE: print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])} dur={DUR[k]}")
assert all(len(STYLE[k])<=1000 and len(EXCLUDE[k])<=1000 for k in STYLE)
assert worst < 40, f"MEEK {worst:.0f}%"
for k in STYLE:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":LYR[k],"model":"v6",
      "title":f"camping-r72-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":DUR[k],"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print(f"✅ r72: 3 specs · worst shared {worst:.0f}% (cast + the anti-ooh clause only)")
