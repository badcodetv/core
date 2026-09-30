import json, re, pathlib
REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
SHEET = REPO / 'docs/stories/camping/songs/camping.md'
OUT = REPO / 'scripts/suno/.tmp/r52'
src = SHEET.read_text()

start = src.index('### r51 liquid atom'); end = src.index('### r51 techstep atom')
lyrics = re.findall(r'\n```[a-z]*\n(.*?)\n```\n', src[start:end], re.S)[2]
assert '[gruff MC]' in lyrics

CAST = ("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
        "both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and "
        "never slowing for a punchline.")
OPEN = ("It opens with no drums - a lone sad piano and a solo violin - the first MC quiet and emotional over "
        "them, but only for three lines.")
def DOM(x): return f"The drums and the sub are the loudest thing in the mix throughout; the {x} sits under them, never in front."

BASE_EX = ("American accent, American vocal, Southern drawl, country vocal, twang, americana, US rap, American rap, "
 "trap, boom bap, teenage voice, boyish voice, autotune, female vocal, laid-back, chill, mumbled, lazy flow, "
 "spoken word, happy, uplifting, major key, comedic, novelty, parody, mono mix, muddy mix, crowd noise, applause, "
 "jump up, wobble bass, dubstep, EDM drops, glossy production, radio pop, "
 "orchestral film score, epic trailer music, brass braams, war drums, full orchestra, symphony orchestra, "
 "string section, lush strings, chamber music, classical arrangement, baroque, concerto, orchestral bed")

LANES = [
 dict(key='sinogrime',
  style=("Sinogrime over drum and bass: plucked guqin and koto figures, pentatonic bells and kung-fu-film stabs, "
   "icy and ornamental. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles, heavy "
   "rolling sub. The plucked strings ring through every verse and across every drop - the east and the breaks are "
   "one piece of music, not a remix - and the breaks never stop, not one bar. " + DOM('guqin') +
   " Cold, glinting and hard, dry bells against dry drums. The sung chorus hook comes back three times. " + CAST),
  ex="Chinese vocal, Mandarin vocal, erhu solo, guzheng recital, world music, new age, meditation, "
     "harmonica, slide guitar, post-punk guitar, Moog arpeggio, Motown horns, Hammond organ, bagpipes, steel pan, "
     "Rhodes piano"),
 dict(key='bleep',
  style=("Sheffield bleep and bass welded to drum and bass: naked sine bleeps, a colossal clean sub that moves "
   "the room, nothing else. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles, and that sub "
   "under all of it. The bleeps pulse through every verse and across every drop - the bleeps and the breaks are "
   "one piece of music, not a remix - and the breaks never stop, not one bar. " + DOM('bleeps') +
   " Spartan, enormous and northern, almost nothing in the mix but weight. A sung chorus hook returns three "
   "times. " + CAST),
  ex="acid house, 303 squelch, rave hoover, happy hardcore, trance lead, "
     "harmonica, slide guitar, post-punk guitar, Motown horns, Hammond organ, bagpipes, steel pan, guqin, koto, "
     "Rhodes piano, brass band"),
 dict(key='bassline',
  style=("Sheffield bassline and speed garage crossed with drum and bass: hard Korg organ stabs and a warped "
   "wobbling garage bass, Niche club weight. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles cut hard, "
   "deep sub. The organ stabs punch through every verse and across every drop - the stabs and the breaks are one "
   "piece of music, not a remix - and the breaks never stop, not one bar. " + DOM('organ stabs') +
   " Rowdy, northern and cheap in the best way, unpolished. The sung hook returns three times. " + CAST),
  ex="4x4 house beat, diva vocal, garage singer, funky house, donk, happy hardcore, "
     "harmonica, slide guitar, post-punk guitar, Motown horns, bagpipes, steel pan, guqin, koto, Rhodes piano, "
     "brass band"),
 dict(key='drumfunk',
  style=("Drumfunk: hyper-detailed breakbeat science at 174 BPM, endless micro-edits of the amen and the apache, "
   "snares tumbling over each other, almost no melody at all. " + OPEN +
   " Then the drop: the breaks take the whole record - chopped, re-chopped and never repeating, ghost notes and "
   "rolls filling every gap, one deep sub holding the bottom. The drums ARE the tune; there is nothing under the "
   "verses but breaks and sub, and the breaks never stop, not one bar. The drums are the loudest thing in the mix "
   "throughout and nothing is allowed in front of them. Dry, technical, relentless and cold. A sung chorus hook "
   "returns three times, the only melody. " + CAST),
  ex="melodic pads, lead synth, piano house, ambient wash, "
     "harmonica, slide guitar, post-punk guitar, Motown horns, Hammond organ, bagpipes, steel pan, guqin, koto, "
     "Rhodes piano, brass band, Moog arpeggio"),
 dict(key='smallpipes',
  style=("Northumbrian smallpipes over drum and bass: a bellows-blown chanter on one staccato modal figure, three "
   "drones under it, cold north-east England. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles, heavy "
   "rolling sub. The pipes keep piping through every verse and across every drop - the pipes and the breaks are "
   "one piece of music, not a remix - and the breaks never stop, not one bar. " + DOM('pipes') +
   " Bleak, ancient and rained-on, reedy against hard dry drums. The sung hook returns three times. " + CAST),
  ex="Highland bagpipes, military pipe band, ceilidh band, folk singer, sea shanty, morris dancing, jig, reel, "
     "harmonica, slide guitar, post-punk guitar, Motown horns, Hammond organ, steel pan, guqin, koto, Rhodes piano"),
 dict(key='steelpan',
  style=("A Notting Hill steel band welded to drum and bass: tenor and cello pans on one minor figure, played slow "
   "and mournful, never carnival-happy. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, ragga-jungle two-step, deep "
   "rolling sub. The pans ring through every verse and across every drop - the pans and the breaks are one piece "
   "of music, not a remix - and the breaks never stop, not one bar. " + DOM('pans') +
   " Metallic, grieving and wet, pans outdoors against dry drums. The sung chorus lands three times. " + CAST),
  ex="soca, calypso vocal, carnival crowd, whistles, party chant, patois vocal, dancehall toaster, happy, festive, "
     "harmonica, slide guitar, post-punk guitar, Motown horns, Hammond organ, bagpipes, guqin, koto, Rhodes piano"),
]
over = []
for L in LANES:
    if len(L['style']) > 1000: over.append((L['key'], len(L['style'])))
    spec = {"style": L['style'], "exclude": BASE_EX + ", " + L['ex'], "lyrics": lyrics,
            "model": "v6", "title": f"camping-r52-{L['key']}", "workspace": "camping-Jack",
            "styleInfluence": 75, "weirdness": [60], "durationSec": 195,
            "variety": "off", "maxMode": False, "vocalGender": "male", "personalize": False}
    (OUT / f"{L['key']}.json").write_text(json.dumps(spec, indent=2))
    print(f"{L['key']:11s} style={len(L['style']):4d} exclude={len(spec['exclude']):4d}")
print('OVER CAP:', over)

GROUND = {
 'sinogrime': ('guqin, koto, pentatonic bells, kung-fu-film stabs',
  '[Sinogrime](https://grime.fandom.com/wiki/Sinogrime) — a **real 2003 grime subgenre**: Wiley, Jammer, Terror Danjah and Ruff Sqwad sampling kung-fu films and East Asian instruments ([Radii](https://radii.co/article/sinogrime-explained)). The one lane that fuses with the grime cast by *lineage*, not by force'),
 'bleep': ('naked sine bleeps, a colossal clean sub',
  '[Bleep techno](https://en.wikipedia.org/wiki/Bleep_techno) — Sheffield/Bradford 1989-90, Warp, LFO and Unique 3. **It is jungle&rsquo;s actual ancestor:** Fabio and Grooverider played LFO at Rage, the night jungle was born, and its sub-bass obsession became the jungle trademark ([Kmag](https://kmag.co.uk/bleep-bass-breaks-real-roots-of-jungle/), [DJ Mag](https://djmag.com/features/how-lfos-frequencies-became-benchmark-90s-bleep-techno))'),
 'bassline': ('Korg organ stabs, warped speed-garage bass',
  '[Bassline / 4x4](https://en.wikipedia.org/wiki/Bassline_(music_genre)) — South Yorkshire, out of the Niche club in Sheffield, **police-raided working-class club music** ([DJ Mag](https://djmag.com/features/history-bassline)). The most on-message scene in the list for a song about who got left behind'),
 'drumfunk': ('the breakbeats themselves — almost no melody',
  '[Drumfunk](https://rateyourmusic.com/genre/drumfunk/) — Paradox, Alaska, Equinox, Seba: hyper-detailed break science, **basslines and melody stripped back to put the drums front and centre** ([Ableton](https://www.ableton.com/en/blog/paradox-breakbeat-mastery/)). 🔑 **This lane exists to answer "not enough drum and bass" directly** — it is the one where the drums *are* the tune'),
 'smallpipes': ('bellows-blown chanter, three drones',
  '[Northumbrian smallpipes](https://en.wikipedia.org/wiki/Northumbrian_smallpipes) — north-east England, **closed chanter so the articulation is naturally staccato**, modal and drone-based, which is why it sits on a breakbeat where Highland pipes would not. The Darkening (2018-) already fuse them with electronics'),
 'steelpan': ('tenor and cello pans, one minor figure',
  'Notting Hill Carnival steel band — the Caribbean lineage jungle actually comes from, the same root as r49&rsquo;s `ragga` lane, but a **pitched-percussion** family nothing else here touches. Played slow and minor on purpose: the satire trap is real and carnival-happy would wreck the song'),
}
TAKES = {
 'sinogrime': ('265aac39-d11a-4229-a4e8-08e198b02f29','75620a76-1b05-4a65-9430-d5389f503b93'),
 'bleep': ('34570090-1ad5-46da-a28b-dec987865409','c3691721-cfa8-47a1-a8c0-e3a16487cf34'),
 'bassline': ('9362a930-d7ae-4d8b-b22c-4435452ec671','ff126806-2d05-42d2-a35d-fe60cb66ef10'),
 'drumfunk': ('cfbddf22-7bca-4037-acfc-3654de391e95','b00ade72-4f0d-426f-b29a-a3930a85b6b1'),
 'smallpipes': ('10f33b70-c720-4f13-9e69-3c5a052ba355','fd9a88a9-6136-4f39-9dee-9f95a0232a18'),
 'steelpan': ('97634c19-b764-4a3f-91d9-163123ee9199','bcce24b8-fe81-422f-9818-82954f262d2d'),
}
rows = '\n'.join(f"| **`{L['key']}`** | {GROUND[L['key']][0]} | {GROUND[L['key']][1]} |" for L in LANES)
takerows = '\n'.join(f"| `{k}` | [{a[:8]}](https://suno.com/song/{a}) · [{b[:8]}](https://suno.com/song/{b}) |" for k,(a,b) in TAKES.items())
atoms = ''
for L in LANES:
    atoms += (f"### r52 {L['key']} atom\n\nStyle:\n\n```\n{L['style']}\n```\n\nExclude styles:\n\n```\n"
              f"{BASE_EX + ', ' + L['ex']}\n```\n\nLyrics:\n\n```lyrics\n{lyrics}\n```\n\n")

SECTION = f"""## v6.44 Round r52 — six researched fusions, all with a lineage to 174 (2026-09-19)

**Brief, Jack 2026-09-19:** *"Please try different styles by researching the internet for what would
work with [`1127446d`](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74), to make
variations of it, plus all of the rules i have said that need to be in the song."*

### 🔑 The lane-picking rule this round adds: choose scenes with a real lineage to 174 BPM

r49 and r51 picked instrument families for **contrast** and grounded them afterwards. This round
picks them the other way round: web research first, and a lane only ships if the fusion **already
happened in British music**. Four of the six are not fusions at all — they are D&B's own family
tree. That is the cheapest insurance against a lane sounding bolted on, which is the failure the
unity sentence exists to patch.

### The six lanes

| Lane | Instrument family | Grounding |
|---|---|---|
{rows}

### ✅ Every rule you have given, and where it lives in these boxes

| Rule | Where it is |
|---|---|
| **Build on `1127446d`** | the spine is byte-identical to r50/r51: the opening, the 174 mechanics, the sung chorus, the words |
| **Three lines slow and emotional, then drop and get fast** | `OPEN` clause in every Style box + the `[Drop]` cue after line three |
| **Fast from there, never slowing** | `rapid-fire on the 174 grid and never slowing for a punchline` — a **positive**, never a `slow tempo` ban |
| **Always the grime voice** | r43's proven cast sentence, verbatim, in all six |
| **Sung chorus** | stated in every Style box; `sung chorus` is never in an exclude list |
| **No classical leading** | no bowed-string lane exists; classical **bed** words banned in all six; the solo violin survives in the three-line opening only |
| **Drum and bass throughout** | `the breaks never stop, not one bar` + the unity sentence, per lane |
| **Not enough drum and bass** | the balance clause — *"the drums and the sub are the loudest thing in the mix throughout"* — **plus `drumfunk`, a whole lane where the drums are the tune** |
| **Varied** | six instrument families, none used in r49-r51, each leading the first tokens |
| **British** | all six scenes are British; nationality rides on the genre word, never on adjectives |
| **Words unchanged** | same 60 lines, again |

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** · workspace `camping-Jack` · Weirdness **60**. Titles
`camping-r52-<lane>-v6-w60`. Identical to r50 and r51, so all three rounds compare directly.

### Generated 2026-09-19 — 6 Creates, 12 takes, workspace `camping-Jack`

**Credits 10,680 → 10,620 — 10 per Create, 60 for the round.**

| Lane | Takes |
|---|---|
{takerows}

⬜ **Not measured and not heard.** 🔴 **Watch `steelpan` for the satire trap** — a steel band is the
one lane here whose default register is *happy*, and the Style box fights it with words alone
(`slow and mournful`, `never carnival-happy`, plus `soca, calypso, carnival crowd, festive` in the
excludes). If it comes back cheerful, that is the trap firing and the lane should be dropped, not
re-worded.

{atoms}---

"""
i = src.index('## v6.43 Round r51')
s2 = src[:i] + SECTION + src[i:]
s2 = s2.replace("RESUME HERE — round r51 (§v6.43, the grime cast and no classical lane, 12 takes, 2026-09-19) is generated and waiting on Jack's ear; r49's and r50's takes are also unheard, and r50 is superseded.",
 "RESUME HERE — rounds r51 (§v6.43, the grime cast, no classical lane) and r52 (§v6.44, six researched fusions with a real lineage to 174) are both generated, 24 takes, 2026-09-19, waiting on Jack's ear; r49's takes are also unheard and r50 is superseded.")
SHEET.write_text(s2)
print('sheet: r52 inserted')
