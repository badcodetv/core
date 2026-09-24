"""r55 — film-score lanes, and the vocal-pacing stack.

Brief (Jack, 2026-09-21, after r54): *"none of those were the right pacing vocally, please make a
faster paced grime rapper rap to the beat of the drum and bass, with orchestral stuff interwoven in
it, please make horror vibes, then action, adventure, thriller, please do film score genres."*

Four lanes = four film-score genres. The variety axis is the SCORE this time, so the d&b is written
as drum MECHANICS per lane (suno-v6.md §9: "name the drum mechanics, not the sub-genre" — a lazy
`liquid DnB` came back as two-step; an engineered breakcore/jungle prompt worked on both models).

The pacing stack, four levers at once because three of them have failed alone before:
  1. DURATION 195 -> 155 s. Same words in 20% less time is the one lever that cannot be ignored
     by a prompt box; v6 obeys a set duration to about +/-1 s (r48: 12/12, r54: 24/24).
  2. The flow written in MUSICAL UNITS, not adjectives: eighth notes on the 174 grid with
     sixteenth-note bursts, two syllables to every beat.
  3. The GAPS banned explicitly - no pause at a line end, never a bar left empty.
  4. Excludes carry the slow-delivery family plus the new pause family.
"""
import json, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r55'
LYR = json.loads((REPO / 'scripts/suno/.tmp/r54/brass.json').read_text())['lyrics']

# ── the cast: standing rule, verbatim since r43 ─────────────────────────────
CAST = ("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped "
        "and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire "
        "on the 174 grid and never slowing for a punchline.")

# ── NEW: the flow written in musical units, not adjectives ──────────────────
FLOW = ("They ride the break in eighth notes with sixteenth bursts, two syllables a beat, "
        "consonants like percussion, no pause at a line's end, never a bar left empty.")

GUARDS = ("American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, "
          "female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, "
          "lazy flow, slow flow, half-time flow, steady rap pace, measured delivery, sparse flow, "
          "pausing between lines, empty bars, spoken word, rapping behind the beat, off-grid vocal, "
          "drifting tempo, tempo change, rubato, comedic, novelty, parody")

FAMILY = {
    'horror':    "shrieking violins, string shrieks, prepared piano, bowed metal, sul ponticello",
    'action':    "low brass hits, taiko, war drums, heroic brass, brass ostinato",
    'adventure': "french horn theme, soaring strings, orchestral tambourine, sleigh bells",
    'thriller':  "ticking pizzicato, clock percussion, muted piano, cold sustained bass",
}

LANES = [
  dict(
    key='horror',
    mech="174 BPM drum and bass: rapid chopped amen breaks, hyperdetail percussion, a distorted sub.",
    score="Scored like a horror film: shrieking violin clusters, bowed metal, prepared piano.",
    job="The shrieks land on the snare and the low strings saw the sub's own notes: the score plays the drums' rhythm, one machine, never a soundtrack over a track.",
    open="Opens on the prepared piano alone, no drums, two lines, already flat out.",
    build="Under line three the violins climb in semitones and the breaks stutter in early.",
    mix="Drums and sub loudest, breaks never stopping, everything on one 174 grid.",
    prod="Dry, close, horrible, no reverb to hide in.",
    ban="lush strings, orchestral bed, ambient, calm, pretty, major key, uplifting",
    cue_open="a prepared piano thudding alone, no drums at all",
    cue_build="the violins climbing in semitones and the breaks stuttering in early",
    cue_drop="the amen and the distorted sub tear in, violin shrieks landing on the snare",
    cue_chorus="the shrieking strings take the chorus with the break",
    cue_bridge="the breaks at their heaviest, bowed metal under every line",
    cue_last="the prepared piano returns under the break",
  ),
  dict(
    key='action',
    mech="174 BPM drum and bass: machine-tight breaks, a morphing Reese, hard rolling percussion.",
    score="Scored like an action film: pounding low brass hits, taiko doubling the kick, a minor-key brass ostinato.",
    job="The taiko sits inside the break as an extra drum and the brass hits land only where the break leaves a hole: part of the kit, not a layer above it.",
    open="Opens on one low brass note and a taiko hit, no drums, two lines, flat out.",
    build="Under line three the taiko doubles and doubles and the brass climbs.",
    mix="Break and Reese stay louder than the brass throughout, one 174 grid.",
    prod="Huge, hard, punchy, mastered loud, no air.",
    ban="lush strings, orchestral bed, ambient, gentle, pretty, sentimental, major key",
    cue_open="one low brass note and a single taiko hit, no drums at all",
    cue_build="the taiko doubling and doubling and the brass climbing a step at a time",
    cue_drop="the machine-tight break and the Reese slam in with the brass on the same beat",
    cue_chorus="the brass takes the chorus alongside the break",
    cue_bridge="the breaks at their heaviest, taiko inside every bar",
    cue_last="one low brass note returns over the break",
  ),
  dict(
    key='adventure',
    mech="174 BPM drum and bass: rolling jungle breaks, big warm sub, tumbling fills.",
    score="Scored like an adventure film in a minor key: a heroic french horn theme, sweeping strings, orchestral tambourine.",
    job="The horn theme is cut into short answers between the MCs' lines and the tambourine rides the break's hats: the score arrives as rhythm, never a bed.",
    open="Opens on a lone french horn, no drums, two lines, spat fast over it.",
    build="Under line three the strings sweep up and the break rolls in under them.",
    mix="Drums and sub above the orchestra throughout, break unbroken, one 174 grid.",
    prod="Wide, warm, cinematic but dirty, tape on the drums.",
    ban="lush strings, orchestral bed, ambient, cheerful, festive, major key, fanfare, triumphant",
    cue_open="a lone french horn, no drums at all",
    cue_build="the strings sweeping up and the break rolling in underneath",
    cue_drop="the jungle break and the warm sub arrive, the horn answering across the top",
    cue_chorus="the horns and strings take the chorus with the break",
    cue_bridge="the breaks at their heaviest, horns answering each line",
    cue_last="the lone french horn returns over the break",
  ),
  dict(
    key='thriller',
    mech="174 BPM drum and bass: cold skippy breaks, tight snares, a low Reese that creeps.",
    score="Scored like a thriller: a ticking pizzicato ostinato, muted piano notes, one cold low string.",
    job="The pizzicato ticks sixteenths against the break like a clock and the piano answers the snare: timekeeping inside the drums, never atmosphere over them.",
    open="Opens on the ticking pizzicato alone, no drums, two lines, close and fast.",
    build="Under line three the ticking speeds up and the low string slides up into the drop.",
    mix="Break and Reese loudest, no gaps in the drums, everything on one 174 grid.",
    prod="Cold, tight, narrow, clinical.",
    ban="lush strings, orchestral bed, ambient, warm, pretty, major key, jazzy",
    cue_open="a ticking pizzicato ostinato alone, no drums at all",
    cue_build="the ticking speeding up and a low string sliding upward into the drop",
    cue_drop="the cold skippy break and the creeping Reese come in, the pizzicato ticking on through",
    cue_chorus="the pizzicato and the strings take the chorus with the break",
    cue_bridge="the breaks at their heaviest, the piano answering every snare",
    cue_last="the ticking pizzicato returns under the break",
  ),
]


def style(l):
    return ' '.join([l['mech'], l['score'], l['job'], l['open'], l['build'], l['mix'], l['prod'],
                     CAST, FLOW])


def exclude(l):
    others = [FAMILY[k] for k in FAMILY if k != l['key']]
    return ', '.join([GUARDS] + others + [l['ban']])


def lyrics(l):
    t = LYR
    t = t.replace(
        "[Verse 1 | one tolling low piano note and a lone trombone, no drums at all | gruff MC, quiet and close, urgent and already tense]",
        f"[Verse 1 | {l['cue_open']} | gruff MC, close and quiet but already at full speed]")
    t = t.replace(
        "[Verse 1 continues — no pause, the same MC carrying straight on | a timpani roll speeding up and a snare roll doubling underneath, the tension climbing into the drop]",
        f"[Verse 1 continues — no pause, the same MC carrying straight on | {l['cue_build']}]")
    t = t.replace(
        "[Drop | the amen and the sub tear in at full weight and the brass stabs land on the same beat]",
        f"[Drop | {l['cue_drop']}]")
    t = t.replace(
        "[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]",
        "[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]")
    t = t.replace(
        "[Chorus | sung, big and melodic, the brass takes the chorus alongside the break]",
        f"[Chorus | sung, big and melodic, {l['cue_chorus']}]")
    t = t.replace(
        "[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]",
        "[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]")
    t = t.replace(
        "[Bridge | the two MCs trade lines, the breaks at their heaviest, brass stabs answering every line]",
        f"[Bridge | the two MCs trade lines at full speed, {l['cue_bridge']}]")
    t = t.replace(
        "[Chorus | sung, the last time, the lone trombone returns over the break]",
        f"[Chorus | sung, the last time, {l['cue_last']}]")
    return t


rows = []
for l in LANES:
    s, e, ly = style(l), exclude(l), lyrics(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    assert l['cue_open'] in ly and 'double-time from here' in ly, l['key']
    assert 'trombone' not in ly and 'timpani roll' not in ly, (l['key'], 'r54 cue left behind')
    spec = {
        "style": s, "exclude": e, "lyrics": ly,
        "model": "v6",
        "title": f"camping-r55-{l['key']}",
        "workspace": "camping-Jack",
        "styleInfluence": 80,
        "weirdness": [30, 60],
        "durationSec": 155,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }
    (OUT / f"{l['key']}.json").write_text(json.dumps(spec, indent=2) + "\n")
    rows.append((l['key'], len(s), len(e), ly.count('\n') + 1))

for k, sl, el, lp in rows:
    print(f"{k:10} style={sl:4}  exclude={el:4}  lyricLines={lp}")
print(f"\nshared per lane: cast {len(CAST)} + flow {len(FLOW)} = {len(CAST)+len(FLOW)} chars")

md = ["""## v6.47 Round r55 — film-score lanes, and the vocal-pacing stack (2026-09-21)

**Brief, Jack 2026-09-21, after hearing r54:** *"none of those were the right pacing vocally, please
make a faster paced grime rapper rap to the beat of the drum and bass, with orchestral stuff
interwoven in it, please make horror vibes, then action, adventure, thriller, please do film score
genres."*

### 🔴 Say the known risk once, then build it

Three measured rounds (r43 Zimmer, r47 `cinematic`, r48 `grimescore`) found that **the more
film-score a Camping lane carries, the slower the rap gets** — r48's score lane measured 4.6
vocal-band onsets/sec against 5.4 for the take Jack had already called too slow — along with the
weakest low end and the smallest dynamic range. r55 is a deliberate run *at* that finding because
Jack asked for it, so every lane carries the counter-guards: the score is given a **rhythmic job
inside the kit**, the drums are stated as louder than the orchestra, and the pacing stack below is
run at full strength. **If the film-score lanes come back slow again, that is the fourth
confirmation and the answer is a different genre axis, not a different wording.**

### The pacing stack — four levers, because three of them have failed alone

| # | Lever | Why this one |
|---|---|---|
| 1 | 🔑 **Duration 195 s → 155 s** | The same words in 20% less time. It is the only pacing lever that is not a prompt box, and v6 obeys a set duration to about ±1 s — 12/12 takes at r48, 24/24 at r54. Nothing in the Style box can quietly ignore it |
| 2 | **The flow written in musical units** — *eighth notes with sixteenth bursts, two syllables a beat* | Practitioner consensus is that adjectives lose to subdivisions ([HookGenius](https://hookgenius.app/learn/suno-hiphop-prompts/)). 🔑 The arithmetic matters: at 174 BPM sixteenths is 11.6 syllables/sec, which is not a human — **eighths (5.8/sec) with 16th bursts is what fast means here**, and asking for 16ths outright would have produced a chipmunk or been ignored |
| 3 | **The gaps banned** — *no pause at a line's end, never a bar left empty*, plus `[gruff MC, double-time… straight into the next line with no pause]` | r54's takes lost time *between* lines, not inside them |
| 4 | **Excludes carry the pause family** — `sparse flow, pausing between lines, empty bars, half-time flow, slow flow` on top of the standing slow-delivery bans | Delivery bans are the safe place for slowness; tempo bans strangle the opening (r53) |

### The lanes

The variety axis is the **film-score genre**, so the d&b is written as **drum mechanics per lane**,
not as a subgenre noun — `suno-v6.md` §9 has the v6 data point for that (a lazy `liquid DnB` came
back as two-step drums; an engineered breakcore/jungle prompt worked on both models).

| Lane | Score | Drums | The score's job inside the kit |
|---|---|---|---|
| `horror` | shrieking violin clusters, bowed metal, prepared piano | rapid chopped amen, hyperdetail percussion, distorted sub | shrieks land **on the snare**, low strings saw the sub's own notes |
| `action` | pounding low brass, taiko, minor-key brass ostinato | machine-tight breaks, morphing Reese | taiko is **an extra drum inside the break**; brass only in the holes |
| `adventure` | heroic french horn theme in a minor key, sweeping strings, tambourine | rolling jungle breaks, big warm sub, tumbling fills | horn cut into **short answers between the MCs' lines**; tambourine rides the break's hats |
| `thriller` | ticking pizzicato, muted piano, one cold low string | cold skippy breaks, tight snares, creeping Reese | pizzicato **ticks sixteenths against the break like a clock**; piano answers the snare |

### Settings

v6 · Style Influence **80** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 155 s** · workspace `camping-Jack` · weirdness **30 and 60**, a pair per
lane. 8 Creates, 16 takes.

⬜ **The untested lever we still own: Max Mode.** Suno aims it squarely at *songs over two minutes*
and at keeping vocals consistent across a whole track, and every Camping take is over three minutes.
We have never switched it on. It is a slider round, so it costs nothing to design —
`docs/suno-gpt/files/suno-v6.md` §8b.
"""]

for l in LANES:
    md.append(f"\n### r55 {l['key']} atom\n\nStyle:\n\n```\n{style(l)}\n```\n\nExclude styles:\n\n"
              f"```\n{exclude(l)}\n```\n\nLyrics:\n\n```lyrics\n{lyrics(l)}\n```\n")

(OUT / 'section.md').write_text('\n'.join(md))
print('wrote', OUT / 'section.md')
