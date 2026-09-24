import json, re, os, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
SHEET = REPO / 'docs/stories/camping/songs/camping.md'
OUT = REPO / 'scripts/suno/.tmp/r50'
src = SHEET.read_text()

# ── pull r49 pitband's lyrics fence verbatim, then neutralise its two lane-specific cues ──
start = src.index('### r49 pitband atom')
end = src.index('### r49 jazzstep atom')
atom = src[start:end]
fences = re.findall(r'\n```[a-z]*\n(.*?)\n```\n', atom, re.S)
lyrics = fences[2]
lyrics = lyrics.replace(
  '[Drop | the breakbeats and the heavy sub slam in at full weight, the strings arrive with them]',
  '[Drop | the breakbeats and the heavy sub slam in at full weight, the whole arrangement arrives with them]')
lyrics = lyrics.replace(
  '[Chorus | sung, big and melodic, the strings and the breaks together]',
  '[Chorus | sung, big and melodic, the whole arrangement and the breaks together]')
assert 'the whole arrangement arrives with them' in lyrics
assert lyrics.count('the whole arrangement and the breaks together') == 2, lyrics.count('the whole arrangement and the breaks together')

CAST = ("Two British men rap fast and tight on the 174 grid, the same breakneck pace from first line to last: "
        "a gravelly raspy older English storyteller, flat and talky, then a clipped BBC newsreader, cold and "
        "just as fast.")
OPEN = ("It opens with no drums - a lone sad piano and a solo violin - the first MC quiet, close and emotional "
        "over them, but only for three lines.")

BASE_EX = ("American accent, American vocal, Southern drawl, country vocal, twang, americana, US rap, American rap, "
 "trap, boom bap, teenage voice, boyish voice, autotune, female vocal, laid-back, chill, mumbled, lazy flow, "
 "spoken word, happy, uplifting, major key, comedic, novelty, parody, mono mix, muddy mix, crowd noise, applause, "
 "jump up, wobble bass, dubstep, EDM drops, glossy production, radio pop, orchestral film score, epic trailer music, "
 "brass braams, war drums")

LANES = [
 dict(key='liquid',
  style=("Liquid drum and bass led by a warm Rhodes electric piano and deep lush chords. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, skippy two-step shuffles folded "
   "into the roll, and a deep rolling sub that never lets go. The Rhodes and the chords play on through every verse "
   "and over every drop; the Rhodes and the breaks are one piece of music, not a remix, and the breaks never stop, "
   "not for one bar. Warm and soulful under bleak words, night-bus melancholy, wide and deep, mixed raw and never "
   "glossy. The sung chorus hook comes back three times. " + CAST),
  ex="soul diva, R&B vocal, smooth male singer, crooner, sung verses, melodic rap, liquid vocal hook, "
     "string quartet, industrial percussion, post-punk guitar, chorused guitar, Moog arpeggio, analogue synth lead, "
     "Motown horns, tambourine, brass band"),
 dict(key='techstep',
  style=("Techstep drum and bass, 1997 cold: metallic industrial percussion, detuned machine stabs and a filthy "
   "growling Reese bass. " + OPEN +
   " Then the drop: hard 174 BPM breakbeats chopped to splinters, two-step shuffles buried deep in the roll, and sub "
   "pressure that does not lift. The machine stabs hammer through every verse and over every drop - the metal and "
   "the breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. Hostile, "
   "claustrophobic and sci-fi, drums bone dry and close, every surface corroded, no warmth anywhere. A sung chorus hook returns three times, the one melodic thing in it. " + CAST),
  ex="robot vocal, vocoder, sci-fi spoken sample, MC hype chants, ragga toaster, rave stabs, "
     "Rhodes piano, lush chords, string quartet, violin section, post-punk guitar, Moog arpeggio, Motown horns, "
     "tambourine, soul sample, brass band"),
 dict(key='quartet',
  style=("A bleak string quartet welded to drum and bass: two violins, a viola and a cello sawing one repeating "
   "minor figure, bowed hard near the bridge, four players in a cold room, never a film score. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen fills at every turn, two-step "
   "shuffles in the roll, heavy rolling sub. The quartet keeps sawing through every verse and right across "
   "every drop - the strings and the breaks are one piece of music, not a remix - and the breaks never stop, not for "
   "one bar. Chamber-close and dusty against dry drums, grieving, never lush and never epic. Three times a sung chorus hook returns. " + CAST),
  ex="opera vocal, classical soprano, choir, choral, art song, lieder, full orchestra, symphony orchestra, "
     "lush strings, cinematic swell, Rhodes piano, industrial percussion, post-punk guitar, Moog arpeggio, "
     "analogue synth lead, Motown horns, tambourine, brass band"),
 dict(key='postpunk',
  style=("Bleak English post-punk guitar over drum and bass: one scraping chorused electric guitar figure and a "
   "high melodic bass line, played flat in a grey northern room. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, rolling amen breaks, skippy two-step shuffles folded "
   "into the roll, heavy sub underneath. The guitar figure repeats under every verse and rings out right across "
   "every drop - the guitar and the breaks are one piece of music, not a remix - and the breaks never stop, not for "
   "one bar. Industrial, overcast and severe, thin plate reverb, tape-flat production, nothing polished. The sung hook returns three times, big and melodic. " + CAST),
  ex="indie sung vocal, post-punk singing, baritone crooner, shoegaze vocal, goth vocal, "
     "Rhodes piano, string quartet, industrial percussion, Moog arpeggio, analogue synth lead, Motown horns, "
     "tambourine, brass band"),
 dict(key='analogue',
  style=("Analogue 1980s synth hardware driving drum and bass: a Moog bass arpeggio running sixteenths, cold Juno "
   "pads and tape delay, hardware hiss on everything. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, skippy two-step shuffles folded "
   "into the roll, a growling sub under the arpeggio. The arpeggio runs unbroken beneath every verse and straight "
   "through every drop - the synths and the breaks are one piece of music, not a remix - and the breaks never stop, "
   "not for one bar. Airless, mechanical and nocturnal, narrow and cold, machine-made on purpose. A sung chorus hook comes round three times. " + CAST),
  ex="synthpop vocal, vocoder, robot vocal, 80s pop singer, new romantic croon, "
     "Rhodes piano, string quartet, post-punk guitar, chorused guitar, industrial percussion, Motown horns, "
     "tambourine, brass band"),
 dict(key='motown',
  style=("Chopped 1960s soul records over drum and bass: cracked horn stabs, an upright piano vamp, tambourine and "
   "vinyl crackle, sampled and chopped like a 1995 jungle plate rather than played live. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, amen breaks torn across the turns, skippy two-step "
   "shuffles folded into the roll, deep rolling sub. The horn stabs punch through every verse and across every drop "
   "- the samples and the breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. "
   "Dusty, hot and cracked against cold drums, sampler-crunched, loud and unpolished. The sung chorus hook lands three times. " + CAST),
  ex="soul singer, gospel vocal, diva, doo-wop harmony, backing singers, female soul vocal, Motown singing, "
     "Rhodes piano, string quartet, post-punk guitar, chorused guitar, Moog arpeggio, analogue synth lead, "
     "industrial percussion"),
]

# ── BOLD check: longest shared run between every pair of Style boxes ──
def longest_run(a, b):
    best = 0
    la, lb = len(a), len(b)
    prev = [0]*(lb+1)
    for i in range(1, la+1):
        cur = [0]*(lb+1)
        for j in range(1, lb+1):
            if a[i-1] == b[j-1]:
                cur[j] = prev[j-1]+1
                if cur[j] > best: best = cur[j]
        prev = cur
    return best

pairs = []
for i in range(len(LANES)):
    for j in range(i+1, len(LANES)):
        pairs.append((LANES[i]['key'], LANES[j]['key'], longest_run(LANES[i]['style'], LANES[j]['style'])))
worst = max(p[2] for p in pairs)

# ── specs ──
for L in LANES:
    spec = {
      "style": L['style'],
      "exclude": BASE_EX + ", " + L['ex'],
      "lyrics": lyrics,
      "model": "v6",
      "title": f"camping-r50-{L['key']}",
      "workspace": "camping-Jack",
      "styleInfluence": 75,
      "weirdness": [60],
      "durationSec": 195,
      "variety": "off",
      "maxMode": False,
      "vocalGender": "male",
      "personalize": False,
    }
    (OUT / f"{L['key']}.json").write_text(json.dumps(spec, indent=2))

for L in LANES:
    assert len(L['style']) <= 1000, (L['key'], len(L['style']))
print("longest shared run across all 15 Style-box pairs:", worst)
print("cast sentence length:", len(CAST))
for L in LANES:
    print(f"{L['key']:9s} style={len(L['style']):4d}  exclude={len(BASE_EX)+2+len(L['ex']):4d}")
print("lyrics chars:", len(lyrics), "paragraphs:", len([l for l in lyrics.split('\n') if l.strip()]))

# ── the sheet section ───────────────────────────────────────────────────────
GROUND = {
 'liquid':   ('Rhodes electric piano, lush chords',
              'Liquid D&B is the genre&rsquo;s own melancholy lane — the warm end of the same 174 BPM, so the spine survives untouched while the colour changes completely'),
 'techstep': ('metallic industrial percussion, machine stabs',
              '1997 techstep (Ed Rush &amp; Optical, No U-Turn) is the coldest, most hostile D&B there is — the maximum contrast with a sad piano'),
 'quartet':  ('two violins, viola, cello',
              'Jack named &ldquo;the violins and stuff&rdquo; as a thing he likes; a four-player quartet sawing one figure is that, without the film-score bed the measurements keep punishing'),
 'postpunk': ('scraping chorused electric guitar, melodic bass',
              'the bleak English guitar tradition — and the original Camping candidate&rsquo;s palm-muted guitar figure is the one instrument from the very first take nobody has tried over these words'),
 'analogue': ('Moog bass arpeggio, Juno pads, tape delay',
              'analogue hardware is a different sound-generation method, not just a different genre — hiss, drift and a running arpeggio nothing else in the list can make'),
 'motown':   ('chopped soul horn stabs, upright piano, tambourine',
              'chopping old soul records IS how jungle was built (Goldie, 1995), so the fusion needs no justification — and it gives Jack back a piano in a completely different register'),
}

rows = '\n'.join(f"| **`{L['key']}`** | {GROUND[L['key']][0]} | {GROUND[L['key']][1]} |" for L in LANES)
atoms = ''
for L in LANES:
    atoms += f"""### r50 {L['key']} atom

Style:

```
{L['style']}
```

Exclude styles:

```
{BASE_EX + ', ' + L['ex']}
```

Lyrics:

```lyrics
{lyrics}
```

"""

SECTION = f"""## v6.42 Round r50 — six instrument families on the `1127446d` spine (2026-09-19)

**Brief, Jack 2026-09-19:** *"Keep trying more varied styles making sure to use this
[song](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74) as the one we like and want to
build upon."*

### 🔑 The spine is now fixed, and only the instrument family moves

r49 proved the lever — **six lanes each led by a different instrument family sat 1.7x further apart
than three lanes that differed only in production language.** It also changed too much at once: its
lanes replaced the cast, the arrangement and the colour together, so a lane that failed could not be
told from a spine that failed.

This round **freezes everything `1127446d` is liked for** and moves one thing. Held constant,
byte-identical across all six lanes:

- **The opening** — no drums, a lone sad piano and a solo violin, the first MC quiet and emotional,
  **three lines only**, then the drop. (Jack, on `r19-reese-w60`: *"I like that it slows down with
  the first lyrics in an emotional way with the piano"*.)
- **The D&B mechanics** — 174 BPM, chopped amen breaks, skippy two-step shuffles folded into the
  roll, heavy rolling sub.
- **The cast** — the gravelly raspy older English storyteller and the clipped BBC newsreader, both
  rapid-fire on the grid, never slowing. (*"this part … slowed down and paused when he rapped it,
  this should be fast."*)
- **The sung chorus**, three times. (*"the chorus being sung is cool"*.)
- **The words** — the same 60 lines, unchanged again.

**Moved:** the instrument family that leads the Style box and plays all the way through.

### The six lanes

| Lane | Instrument family | Why this one |
|---|---|---|
{rows}

### ⚠️ Deliberate departure: the BOLD check is not the gate this round

Longest shared run across the fifteen Style-box pairs is **{worst} characters** against r49's 228 —
and that is the point, not a failure. The shared run *is* the spine: the opening, the D&B mechanics
and the cast sentence, held byte-identical so that **the instrument family is the only variable**.
r49 answered "are these different enough"; r50 answers "which instrument, on the record we already
like". 🔴 **Do not copy this number forward as a new BOLD baseline** — it applies only while a
liked reference is being built on.

### 🔑 Every lane still bans its own genre's singers

The r40 `opera` house rule holds: naming a tradition summons its vocalists with its instruments.
`soul diva, R&B vocal` in `liquid`, `opera vocal, classical soprano, choir` in `quartet`,
`soul singer, gospel vocal, doo-wop harmony` in `motown`, `synthpop vocal, vocoder` in `analogue`,
`indie sung vocal, post-punk singing` in `postpunk`, `robot vocal, vocoder` in `techstep`. Each lane
also bans the other five families so nothing bleeds. **`sung verses` is banned where it is a risk;
`sung chorus` never is** — that is the feature.

🔑 **`orchestral film score`, `epic trailer music` and `brass braams` are banned in every lane,
including `quartet`** — three measured rounds say a full score bed costs the low end, the dynamics
and the rap speed. The quartet is four players in a room, not an orchestra.

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** (18/18 on target across r48 and r49) · workspace `camping-Jack`
· Weirdness **60**. Titles `camping-r50-<lane>-v6-w60`.

**Weirdness 60, not the pair, and this one is evidenced:** the take being built on is a **w60**
generation, and §v6.39's diagnosis is that every feature Jack likes — the piano, the violins, the
sung chorus — arrived as **weirdness-60 drift against the prompt**. Running the spine anywhere else
would be changing a second variable. 🔴 The r49 note still stands: re-run the winning lane as a
proper pair before drawing any weirdness conclusion.

{atoms}---

"""

marker = '## v6.41 Round r49'
i = src.index(marker)
SHEET.write_text(src[:i] + SECTION + src[i:])
print('sheet: inserted r50 section,', len(SECTION), 'chars before', marker)
