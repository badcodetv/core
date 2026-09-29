"""r54 — six BOLD lanes. Every lane changes BOTH the orchestral family AND the d&b subgenre.

Brief (Jack, 2026-09-21): r53's timing went weird; the rap must be fast and ON the beat; the
opening was too slow before the drop and should be an exciting build-up; the orchestral layer and
the d&b must be layered so they complement each other; and the orchestra and the drums have been
the same in every round, so make massively varied versions of all of them.

Shared across lanes, deliberately and by ruling: the WORDS, the r43 grime cast sentence
(camping-always-the-grime-voice), and the 174 d&b + on-grid constraint the brief itself names.
Everything else — subgenre, instrument family, the orchestra's JOB, the build device, the
production sentence, the ban list — is written fresh per lane.
"""
import json, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r54'
R53 = json.loads((REPO / 'scripts/suno/.tmp/r53/optimised.json').read_text())
LYR = R53['lyrics']

# ── the cast: standing rule, verbatim since r43 ──────────────────────────────
CAST = ("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped "
        "and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire "
        "on the 174 grid and never slowing for a punchline.")

# ── guards that protect the cast and the brief; musical bans are per lane ────
GUARDS = ("American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, "
          "female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, "
          "lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, "
          "off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody")

# ── every lane bans every other lane's family and genre ──────────────────────
FAMILY = {
    'brass':    "low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band",
    'cello':    "solo cello, double bass, sawing strings, string quartet, chamber strings",
    'bells':    "tubular bells, glockenspiel, celesta, gongs, chimes, music box",
    'woodwind': "bass clarinet, flute, flutter-tongue flute, oboe, woodwinds",
    'spiccato': "spiccato strings, staccato string ostinato, violin section, string stabs",
    'noir':     "muted trumpet, upright bass, walking bass, brushed drums, jazz, swing",
}
GENRE = {
    'brass':    "jungle, amen jungle, ragga jungle",
    'cello':    "techstep, neurofunk",
    'bells':    "rollers, dancefloor drum and bass",
    'woodwind': "liquid drum and bass, liquid funk",
    'spiccato': "darkstep, amen assault",
    'noir':     "jazzstep, jazzy jungle",
}

LANES = [
  dict(
    key='brass',
    genre="Jungle, 174 BPM, minor key, chopped amen breaks, grime over the top.",
    open="Opens with no drums: one tolling low piano note and a lone trombone, two lines, tense from bar one.",
    build="Under line three a timpani roll speeds up and a snare roll doubles to sixteenths: a build, not a ballad.",
    drop="Then the drop, the amen tearing in with a huge rolling sub, brass landing on the same beat.",
    job="Trombone and tuba stab in the holes the break leaves, timpani doubling every kick: brass as percussion, written into the drums, not laid over them.",
    mix="Drums and sub loudest throughout, break never stopping, all of it on one 174 grid, every rapped line square on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Dubplate-loud, overdriven, tape-hot, like a 1994 white label.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, glossy production, radio pop",
    cue_open="one tolling low piano note and a lone trombone, no drums at all",
    cue_build="a timpani roll speeding up and a snare roll doubling underneath, the tension climbing into the drop",
    cue_drop="the amen and the sub tear in at full weight and the brass stabs land on the same beat",
    cue_chorus="the brass takes the chorus alongside the break",
    cue_bridge="the breaks at their heaviest, brass stabs answering every line",
    cue_last="the lone trombone returns over the break",
  ),
  dict(
    key='cello',
    genre="Techstep, 174 BPM, minor key, cold and mechanical, grime over the top.",
    open="Opens with no drums: a solo cello and a double bass sawing one dark riff, two lines close over them.",
    build="Under line three the bowing hardens and a low filter opens, hauling the track into the drop: rising, never slow.",
    drop="Then the drop, surgical metallic breaks, machine hats, a morphing Reese bass.",
    job="The cello plays that Reese riff an octave up, note for note, so bass and strings are one instrument doubling itself, and the double bass answers each MC with two plucked notes.",
    mix="Break and Reese loudest, unbroken to the end, one rigid 174 grid, the rap exactly on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Surgical, wide and cold, airless, every transient sharpened.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, warm, mellow, organic, live band",
    cue_open="a solo cello and a double bass sawing one dark riff, no drums at all",
    cue_build="the bowing hardening and a low filter opening underneath, hauling the track up into the drop",
    cue_drop="surgical breaks and a morphing Reese slam in, the cello doubling the bass riff an octave up",
    cue_chorus="the cello and the Reese play the hook together under the break",
    cue_bridge="the breaks at their heaviest, the double bass plucking between the lines",
    cue_last="the solo cello returns alone over the break",
  ),
  dict(
    key='bells',
    genre="Rolling dancefloor drum and bass, 174 BPM, minor key, grime over the top.",
    open="Opens with no drums: tubular bells tolling, a glockenspiel picking a cold figure, two lines close.",
    build="Under line three a gong swells and the hats come in alone, doubling and doubling: a fast build, not a slow intro.",
    drop="Then the drop, a relentless rolling break and a deep round sub that never lets go.",
    job="The bells ring on the first beat of every eighth bar like a clock, the glockenspiel doubles the hi-hats note for note, a gong marks each turn: metal as percussion, cut into the break.",
    mix="Drums and sub own the mix, no gaps, one steady 174 grid, the rapping dead on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Huge, glossy, reverberant, long metal tails, loud for a club rig.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, lo-fi, tape hiss, muddy mix",
    cue_open="tubular bells tolling and a glockenspiel over them, no drums at all",
    cue_build="a gong swelling and the hats arriving alone, doubling and doubling into the drop",
    cue_drop="the rolling break and the deep sub slam in, a bell ringing across the first bar",
    cue_chorus="the bells ring out through the chorus over the break",
    cue_bridge="the breaks at their heaviest, a gong on every turn",
    cue_last="the tubular bells return alone over the break",
  ),
  dict(
    key='woodwind',
    genre="Dark liquid drum and bass, 174 BPM, minor key, grime over the top.",
    open="Opens with no drums: a bass clarinet low and slow, a flute breathing above it, two lines close.",
    build="Under line three the flute flutter-tongues and a soft riser climbs, the room tightening bar by bar into the drop.",
    drop="Then the drop, warm rolling breaks with a deep sub beneath them, smooth but heavy.",
    job="The bass clarinet runs a counter-line an octave above the sub, note for note, and the flute answers each rapped line in the gap at the bar's end: a third voice trading with the MCs, never a pad.",
    mix="Break and sub loudest, no holes, a constant 174 grid, every line landing on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Warm, deep and close, soft tape saturation, night-bus melancholy.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, harsh, industrial, distorted",
    cue_open="a bass clarinet low and slow with a flute breathing above it, no drums at all",
    cue_build="the flute flutter-tonguing and a soft riser climbing underneath, tightening into the drop",
    cue_drop="warm rolling breaks and a deep sub arrive, the bass clarinet doubling the sub an octave up",
    cue_chorus="the flute carries the hook with the break underneath",
    cue_bridge="the breaks at their heaviest, the flute answering each line",
    cue_last="the bass clarinet returns under the break",
  ),
  dict(
    key='spiccato',
    genre="Darkstep, 174 BPM, minor key, fast and violent, grime over the top.",
    open="Opens with no drums: a dry spiccato string figure bouncing in sixteenths, no sustain, two lines spat over it.",
    build="Under line three the strings climb a step at a time and a distorted riser rips up beneath: pure tension, over fast.",
    drop="Then the drop, an amen assault, breaks tumbling and tearing, a filthy distorted sub.",
    job="That figure never stops and never swells: short dry sixteenths locked to the break, playing the drums' own pattern back at them, a rhythm part inside the kit.",
    mix="Drums and sub loudest in the room, breaks never stopping, one 174 grid, the rap flat on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Dry, brutal, nearly mono, no reverb anywhere, clipped at the edges.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, legato strings, sustained strings, ambient, reverb-drenched",
    cue_open="a dry spiccato string figure bouncing in sixteenths, no drums at all",
    cue_build="the strings climbing a step at a time and a distorted riser ripping underneath",
    cue_drop="the amen assault and the distorted sub tear in, the strings locking to the break",
    cue_chorus="the strings hammer through the chorus with the break",
    cue_bridge="the breaks at their heaviest, the strings sawing under every line",
    cue_last="the dry strings return alone over the break",
  ),
  dict(
    key='noir',
    genre="Jazzstep, 174 BPM, minor key, smoky and dangerous, grime over the top.",
    open="Opens with no drums: an upright bass walking, a muted trumpet smearing above it, two lines tired and close.",
    build="Under line three brushes race on a snare and the walking bass doubles its speed into the drop, a few bars only.",
    drop="Then the drop, chopped funk breaks and a fat round sub, swung but locked hard.",
    job="The upright bass walks under the sub the whole way and the muted trumpet answers the MCs with one smeared phrase between their bars: players in the room with the break, not sampled over it.",
    mix="Break and sub loudest, drums never out, one hard 174 grid under the swing, every line on the beat.",
    hook="A big sung chorus hook three times, the only sung thing.",
    prod="Smoky, room-recorded, valve warmth, hiss left in.",
    ban="orchestral film score, epic trailer music, symphony orchestra, lush strings, digital, surgical, clinical",
    cue_open="an upright bass walking and a muted trumpet smearing above it, no drums at all",
    cue_build="brushes racing on a snare and the walking bass doubling its speed into the drop",
    cue_drop="chopped funk breaks and a fat sub slam in, the upright bass walking on underneath",
    cue_chorus="the muted trumpet takes the chorus over the break",
    cue_bridge="the breaks at their heaviest, the trumpet answering between the lines",
    cue_last="the muted trumpet returns over the break",
  ),
]

def style(l):
    parts = [l['genre'], l['open'], l['build'], l['drop'], l['job'], l['mix'], l['hook'],
             l['prod'], CAST]
    parts = [p[0] if isinstance(p, tuple) else p for p in parts]
    return ' '.join(parts)


def exclude(l):
    others = [FAMILY[k] for k in FAMILY if k != l['key']] + [GENRE[k] for k in GENRE if k != l['key']]
    return ', '.join([GUARDS] + others + [l['ban']])


def lyrics(l):
    t = LYR
    # 1. the opening cue — r53's "slow and emotional" is exactly the complaint; it becomes tense
    t = t.replace(
        "[Verse 1 | a lone sad piano and a solo violin, no drums at all | gruff MC, quiet and close, slow and emotional]",
        f"[Verse 1 | {l['cue_open']} | gruff MC, quiet and close, urgent and already tense]")
    # 2. the BUILD. A [Build] tag inserts an instrumental with no vocal (suno-tag-mechanics), so the
    #    proven workaround is a "Verse 1 continues" tag: structural enough to re-decide the
    #    arrangement, and a verse is the sung part, so there is nothing to fill with music.
    t = t.replace(
        "now, let me explain, how I'm just poor",
        f"[Verse 1 continues — no pause, the same MC carrying straight on | {l['cue_build']}]\n"
        "now, let me explain, how I'm just poor")
    t = t.replace(
        "[Drop | the breakbeats and the heavy sub slam in at full weight, the whole arrangement arrives with them]",
        f"[Drop | {l['cue_drop']}]")
    t = t.replace(
        "[gruff MC, rapid-fire from here to the end, never slowing]",
        "[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]")
    t = t.replace(
        "[Chorus | sung, big and melodic, the whole arrangement and the breaks together]",
        f"[Chorus | sung, big and melodic, {l['cue_chorus']}]")
    t = t.replace(
        "[Bridge | the two MCs trade lines, the beat and the score at their biggest]",
        f"[Bridge | the two MCs trade lines, {l['cue_bridge']}]")
    t = t.replace(
        "[Chorus | sung, the last time, the piano and the solo violin return under the break]",
        f"[Chorus | sung, the last time, {l['cue_last']}]")
    return t


rows = []
for l in LANES:
    s, e, ly = style(l), exclude(l), lyrics(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s)-1000))
    assert "[Verse 1 continues" in ly and ly.count("I can't live like this forever") >= 10
    spec = {
        "style": s, "exclude": e, "lyrics": ly,
        "model": "v6",
        "title": f"camping-r54-{l['key']}",
        "workspace": "camping-Jack",
        "styleInfluence": 80,
        "weirdness": [30, 60],
        "durationSec": 195,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }
    (OUT / f"{l['key']}.json").write_text(json.dumps(spec, indent=2) + "\n")
    rows.append((l['key'], len(s), len(e), ly.count('\n') + 1))

# BOLD check: the longest run of text shared between any two lanes' Style boxes.
def longest_common(a, b):
    best = ''
    for i in range(len(a)):
        for j in range(len(a), i + len(best), -1):
            if a[i:j] in b:
                best = a[i:j]
                break
    return best

styles = {l['key']: style(l) for l in LANES}
worst = ('', '', '')
for i, x in enumerate(LANES):
    for y in LANES[i + 1:]:
        c = longest_common(styles[x['key']], styles[y['key']])
        if len(c) > len(worst[2]):
            worst = (x['key'], y['key'], c)

for k, sl, el, lp in rows:
    print(f"{k:9} style={sl:4}  exclude={el:4}  lyricLines={lp}")
print(f"\nBOLD check — longest shared run: {len(worst[2])} chars "
      f"({100*len(worst[2])//len(styles[worst[0]])}% of {worst[0]}) between {worst[0]} and {worst[1]}")
print(f"  shared text: {worst[2][:120]!r}")

# ── the sheet section, generated so sheet and specs cannot drift ─────────────
md = ["""## v6.46 Round r54 — six lanes, varied on BOTH axes (2026-09-21)

**Brief, Jack 2026-09-21, on the r53 optimised pair:** *"the optimised ones made the timing weird,
the rap should be fast and to the beat, the beginning was too slow before the drop, it should be an
exciting build up until then and the blend of orchestral elements with the drum and bass grime voice
mix has not been done well enough, they should all be layered and compliment each other… the
orchestral elements have been all the same, as well as the drum and bass, so make massively varied
versions of all of them."* Reference to build on, again:
[1127446d](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74).

### The diagnosis — why the last three rounds sounded like one record

r50–r53 varied **one** axis. Every lane opened on *"a lone sad piano and a solo violin"*, every lane
said *"174 BPM UK drum and bass at full weight, chopped amen breaks"*, and only the guest instrument
moved (guqin, steelpan, smallpipes, organ…). So the orchestral **opening** and the **drums** were
literally the same text in every lane — which is exactly the complaint. r54 varies **both axes at
once**: a different d&b subgenre *and* a different instrument family *and* a different job for that
family, per lane.

### The four fixes, and where each one lands

| Complaint | Fix | Where it goes |
|---|---|---|
| **"the timing went weird"** | an explicit grid lock in every Style box — *one 174 grid, every rapped line square on the beat* — plus `drifting tempo, tempo change, rubato, rapping behind the beat, off-grid vocal` in every Exclude | Style + Exclude. Practitioner consensus is that a constant-tempo clause measurably reduces v6 drift ([MixMasterAI](https://www.mixmasterai.co/suno-prompts/fix/wrong-tempo), [GenX Notes](https://blog.genxnotes.com/en/fix-suno-bpm-tempo-drift/)) |
| **"the rap should be fast and to the beat"** | the r43 cast sentence kept verbatim, and the rapid-fire cue restated **at the drop** (`every line landing square on the beat`) | Style + the lyric cue |
| **"too slow before the drop — make it an exciting build up"** | r53's opening cue literally said **`slow and emotional`**; it now reads `urgent and already tense`, the opening is **two lines not three**, and line three gets a **build device** that differs per lane (timpani roll, filter sweep, gong + doubling hats, flutter-tongue riser, climbing strings, racing brushes) | lyric cue + Style |
| **"the orchestral and the d&b aren't layered / don't complement"** | every lane states the orchestra's **rhythmic job** against the break — doubling the kick, doubling the Reese an octave up, doubling the hi-hats, answering the MC in the bar gap, playing the drums' own pattern — instead of describing a texture | Style, the `job` clause |

🔑 **The build is written as `[Verse 1 continues — no pause…]`, never `[Build]`.** A `[Build]` tag
reliably inserts eight **instrumental** bars with no vocal, and three explicit denials did not stop
it — the noun wins (`docs/suno-gpt/files/suno-tag-mechanics.md`). A `Verse` tag is just as
structural, so Suno re-decides the arrangement, but a verse is the sung part, so there is nothing to
fill with music.

### The six lanes

| Lane | Subgenre | Family | The orchestra's job | Build device | Production |
|---|---|---|---|---|---|
| `brass` | jungle / amen | trombone, tuba, timpani | stabs in the break's holes, timpani doubles every kick | timpani roll + snare roll to 16ths | 1994 white label, tape-hot |
| `cello` | techstep | solo cello, double bass | plays the Reese riff an octave up, note for note | bowing hardens + filter opens | surgical, cold, airless |
| `bells` | rollers | tubular bells, glockenspiel, gongs | bells as a clock, glockenspiel doubles the hi-hats | gong swell + hats doubling | glossy, reverberant, club-loud |
| `woodwind` | dark liquid | bass clarinet, flute | counter-line above the sub; flute answers each rapped line | flutter-tongue + soft riser | warm, close, tape, night-bus |
| `spiccato` | darkstep | dry spiccato strings | 16ths locked to the break, playing the drums' pattern back | strings climb + distorted riser | dry, brutal, nearly mono |
| `noir` | jazzstep | upright bass, muted trumpet | bass walks under the sub; trumpet answers between bars | brushes race + bass doubles up | smoky, valve, room, hiss |

### Settings

v6 · Style Influence **80** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** · workspace `camping-Jack` · **weirdness 30 and 60**, a pair per
lane. 12 Creates, 24 takes.

### BOLD check

Longest shared run between any two Style boxes: **232 characters (23%)** — and it is **only the
r43 cast sentence**, which the rules explicitly allow to be shared. No shared production language,
no shared opening, no shared drum description. (r52's lanes shared ~640 characters including the
opening, the balance clause and the unity clause.)
"""]

for l in LANES:
    md.append(f"\n### r54 {l['key']} atom\n\nStyle:\n\n```\n{style(l)}\n```\n\nExclude styles:\n\n"
              f"```\n{exclude(l)}\n```\n\nLyrics:\n\n```lyrics\n{lyrics(l)}\n```\n")

(OUT / 'section.md').write_text('\n'.join(md))
print('\nwrote', OUT / 'section.md')
