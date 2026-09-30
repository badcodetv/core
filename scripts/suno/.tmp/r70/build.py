import json, re, os, itertools
SRC='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r69/merge.json'
OUT=os.path.dirname(os.path.abspath(__file__))
prev=json.load(open(SRC))
CAST="Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "

STYLE={}
STYLE['garage']=(
 "Skippy UK garage two-step at 174, swung hats and a bassline that bounces instead of growling, the beat "
 "hitting hard from the very first bar with no intro. Cheap synth strings stab on the offbeat with the "
 "shuffle, never a pad and never a melody. Chopped amen fills at every section turn. Warm, bouncy and "
 "mid-forward, like a pirate radio rip, night-bus melancholy. "
 + CAST + "talky and conversational, telling you a story at four in the morning, long unhurried sixteen-bar "
 "verses, riding the shuffle rather than the snare.")

STYLE['reese']=(
 "Dark minimal drum and bass at 174, a dry sparse two-step roller with almost nothing in it, and a filthy "
 "reese bass that IS the tune, growing meaner every section. It starts on that reese alone for four bars, "
 "no drums at all. One solo violin holds a long line an octave above the reese and bends where it bends, "
 "nothing else orchestral anywhere. Narrow, cold and sub-heavy, mixed so the bass is the loudest thing "
 "after the drums. "
 + CAST + "low and murky, several octaves down, drawing single words right out with menace, unhurried but "
 "never dragging.")

STYLE['jungle']=(
 "Breakneck jungle at 174: chopped amen breaks rolling and re-chopping every bar, ragga swing, reverse "
 "crashes into every turn, a deep round sub under it. It opens with a room of men singing the hook on "
 "their own, no drums and no instruments. A church organ answers them at the turns, and the room comes "
 "back on every hook. Big, live and room-y, like a rave taped off the desk. "
 + CAST + "short sharp eight-bar bursts traded fast between them, high energy, hyping each other, every "
 "bar landing clean and on the grid.")

STYLE['piano']=(
 "Rolling drum and bass at 174 with a soft break, brushed hats and a deep round sub that rolls rather than "
 "bites. A grand piano opens it alone on a slow falling figure, three lines before any drums, then the "
 "beat lands on 'you keep on walking'. The piano answers him at the end of every line and comes back an "
 "octave higher each section. Wide, warm and tape-soft, night-bus melancholy. "
 + CAST + "hurt and close, half-speaking and half-singing the ends of lines, flat and raw and never tuned, "
 "unhurried and clear.")

BASE=("American accent, American vocal, US rap, trap, autotune, pitch-corrected vocals, female vocal, cheesy, "
 "steady rap pace, double-time, motormouth, shouting, screaming, roaring, major key, tempo change, slow "
 "tempo, half time, jump up, wobble bass, neurofunk, dubstep, EDM drops, glossy production, happy, "
 "uplifting, orchestral bed, symphony orchestra, full orchestra, string section")
CROSS={
 'garage':"church organ, grand piano, solo violin, male choir, crowd vocals, amen assault, jungle",
 'reese': "church organ, grand piano, synth strings, male choir, crowd vocals, garage shuffle, handclaps",
 'jungle':"grand piano, solo violin, synth strings, garage shuffle, two-step garage",
 'piano': "church organ, male choir, crowd vocals, synth strings, garage shuffle, jungle",
}
EXCLUDE={k: BASE+", "+CROSS[k] for k in STYLE}

DUR={'garage':190,'reese':185,'jungle':175,'piano':190}
VOICE={
 'garage':"talky and conversational, unhurried, riding the shuffle",
 'reese': "low and murky, drawing single words out, menacing",
 'jungle':"short sharp bursts, high energy, clean on the grid",
 'piano': "hurt and close, half-speaking half-singing the line ends",
}
OPENCUE={
 'garage':"[Verse 1 | the beat already rolling | gruff grime MC, close and bitter]",
 'reese': "[Verse 1 | the reese alone, no drums | gruff grime MC, close and bitter]",
 'jungle':"[Verse 1 | straight off the hook, no drums yet | gruff grime MC, close and bitter]",
 'piano': "[Verse 1 | piano alone, no drums | gruff grime MC, close and bitter]",
}
DROPCUE={'garage':"[Drop | the record opens up on this line]",
         'reese':"[Drop | the drums arrive on this line]",
         'jungle':"[Drop | the amen drops on this line]",
         'piano':"[Drop | the beat lands on this line]"}

def words_only(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
base=prev['lyrics']
LYR={}
for k in STYLE:
    l=base
    l=l.replace("[Verse 1 | gruff grime MC, close and bitter]", OPENCUE[k])
    l=l.replace("[Drop | the beat arrives on this line]", DROPCUE[k])
    l=l.replace("[gruff grime MC, hurt and insistent, fast and clear]",
                f"[gruff grime MC, hurt and insistent, {VOICE[k]}]")
    l=l.replace("[cold grime MC, clipped and cold, fast and clear]",
                f"[cold grime MC, clipped and cold, {VOICE[k]}]")
    assert words_only(l)==words_only(base), f"{k}: WORDS CHANGED"
    assert l.count('\n')==base.count('\n')
    assert VOICE[k] in l, f"{k}: voice cue not applied"
    LYR[k]=l

def lc(a,b):
    best=0
    for i in range(len(a)):
        for j in range(len(b)):
            m=0
            while i+m<len(a) and j+m<len(b) and a[i+m]==b[j+m]: m+=1
            best=max(best,m)
    return best
worst=0
for (ka,a),(kb,bb) in itertools.combinations(STYLE.items(),2):
    n=lc(a,bb); pct=100*n/min(len(a),len(bb))
    print(f"  shared {ka}/{kb}: {n} chars = {pct:.1f}%")
    worst=max(worst,pct)
for k in STYLE:
    print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])} dur={DUR[k]}")
assert all(len(STYLE[k])<=1000 and len(EXCLUDE[k])<=1000 for k in STYLE)
assert worst < 40, f"MEEK: {worst:.0f}%"
ALLOWED = ", night-bus melancholy. " + CAST
def longest_str(a,b):
    best=""
    for i in range(len(a)):
        for j in range(len(b)):
            m=0
            while i+m<len(a) and j+m<len(b) and a[i+m]==b[j+m]: m+=1
            if m>len(best): best=a[i:i+m]
    return best
for x,y in itertools.combinations(STYLE,2):
    run=longest_str(STYLE[x],STYLE[y])
    assert run in ALLOWED, f"{x}/{y} shares production language: {run[:80]!r}"
print(f"  worst shared = {worst:.1f}% (cast = {len(CAST)} chars) ✅ bold")
for k in STYLE:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":LYR[k],"model":"v6",
      "title":f"camping-r70-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":DUR[k],"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ wrote 4 specs")
