---
title: Camping (duet re-cut)
status: round 14 drafted (synths + guitar) — rounds 1-13 generated and diagnosed; the orchestral direction is abandoned
released_take: ./camping-released.md
history: ./camping-prompt-history.md
bpm: 174
model: v5.5
settings: style influence 75 · weirdness 30 · audio influence n/a (fresh generation) · NO saved Voice
voices: [bob, tarquin]
---
# Camping — the song

**The live prompt sheet for the "Camping" track.** Same words as the released take, rebuilt
from the ground up as a **true duet**: the released version used a saved Voice, so Bob and
Tarquin came out sounding like the same man.

**Nothing here changes a word.** The lyrics are the released ones, verified line by line
(see §4). What changed is everything *around* the words — casting, arrangement, timing,
pronunciation.

| | |
|---|---|
| **The four boxes to paste** | §1–§4 below, plus §5 settings |
| **The released take** | [`./camping-released.md`](./camping-released.md) — Jack's video is built on it |
| **How we got here** | [`./camping-prompt-history.md`](./camping-prompt-history.md) — fourteen rounds, what failed and why |
| **The general lessons** | promoted into [`docs/suno-gpt/`](../../../suno-gpt/README.md) — they apply to any track |

---

## The contrast stack

Six axes, no accents and no demographics. Every one is something Suno renders readily,
and the **Tradition** row is the load-bearing one — it decides who the model casts.

| | Bob | Tarquin |
|---|---|---|
| **Pitch** | low, deep | higher, light |
| **Texture** | gravelly, torn, smoke-worn | clean, smooth, crisp |
| **Tradition** | British post-punk spoken-word rant | BBC English newsreader register |
| **Delivery** | ranted over the beat, half-shouted, half-muttered | spoken, unhurried, talking down at you |
| **Age/class** | weathered, fifties, working-men's club | late forties, plummy, boardroom |
| **Room** | close, dry | wide, roomy |

**One fixed short label per man, repeated identically** — `[gravelly ranting voice]`
and `[well-spoken posh voice]`. Not a freshly-worded description each time: varied
wording reads as a new character, and consistency is the thing the model latches
onto.

---

## The four Suno boxes — current, round 13

**This is the live prompt.** Paste **all four** boxes every round; never trust what a box
already contains. Everything below this heading is current; the round log above and the
appendices below (§4a–§4c) are **history and reasoning**, kept because the diagnoses are
reusable — they are not instructions, and nothing in them is pasted anywhere.

### 1. My Taste

Swap in for the session, restore your house profile after. My Taste biases every
generation, cannot be turned off, and can only be replaced.

```
Vocals: British post-punk spoken word — two white British men in their late forties and fifties, ranting and talking over the beat rather than singing. One is low, gravelly, smoke-worn and nasal, half-shouting and half-muttering into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, precise and unhurried, talking down at you from a wide room. Ranted spoken word over sung melody, every time. Raw over polished.

Music: dark UK drum and bass and neurofunk at 174 BPM, minor key. Rolling Reese bass, deep sub, chopped amen breaks, industrial stabs. Arrangements that climb in steps and hold things back: a track that opens on one unaccompanied instrument and does not show its full weight until the drop. Space used as an instrument: long empty stretches, one sound at a time, nothing playing that does not need to. Big aggressive wavetable synthesizers doing the work an orchestra would do elsewhere: screaming detuned leads, hard-synced and formant-morphing, growling gnarly mid-range, filters swept by hand. No orchestral instruments and no piano anywhere. Cold, grimy, relentless, and rock steady in tempo from start to finish. A British record, made in Britain, about Britain.

Register: bleak, bitter and angry, played completely straight. Whatever is funny lives in the words alone — the music never winks, never nudges, never plays along.

Subject: British class, money, work, and the people the economy left behind.
```

### 2. Style

**Under 1,000 characters, and it runs close.** A maxed box outvotes its own vocal clauses,
and these voices took four rounds to win — so the arrangement clause is always the first
suspect when casting regresses, and always the first thing trimmed. The live trim ledger
is in §4c.

**Two load-bearing clauses that must never be cut.** `British post-punk spoken word` is
what holds the casting: the genre tag owns the vocalist pool, and a pool carries a whole
**performer** — accent, age, class and race as one package. Post-punk spoken word's
default performer is a middle-aged white British man ranting over a beat, which is Bob;
grime's is a young Black British MC, which is why grime was dropped. And the **unity
sentence** (`so the synth and the break are one piece of music, not a remix of one by the
other`) is what stops the second layer sounding bolted on.

**If the voices drift American again**, the genre tag is the cause — grime used to carry
the nationality. Escalate `British post-punk` and add `Britpop` before adding any rap
genre back.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one is a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two hands to a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note, no melody; then the voice over it with a low palm-muted single-note electric guitar riff underneath — distorted rock tone, one short figure repeating low down, never a solo, never chords; then a dry chopped breakbeat under the vocal, no bassline; then the drop, guitar out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it, so synth and break are one piece of music, not a remix of one by the other. An amen break rolls in as a fill at the end of every eight bars. Ranted and spoken throughout. Grim and bitter, played straight, one steady tempo throughout.
```

### 3. Exclude Styles

`double time` and `tempo change` are in here specifically to answer the timing
fault — the exclude box takes what you want gone as positive keywords.

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, autotune, harmonies, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, US rap, transatlantic, southern drawl, ragga MC, toasting, Jamaican accent, dancehall vocal, soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, choir, orchestral strings, violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, lead guitar, shredding, guitar strumming, power chords, acoustic guitar, wah, live rock band, epic trailer music, reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honky-tonk, liquid dnb, jump up, pop, lo-fi, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, major key, double time, tempo change, half-time, slow tempo
```

`backing vocals` and `harmonies` stay out of the excludes — we're not using the
backing slot this round, but banning it outright tends to strangle more than it
protects.

### 4. Lyrics

**Words verbatim — verified, not assumed.** Every word of the released take
([`./camping-released.md`](./camping-released.md)) is present and unchanged. Four tokens are **respelt**,
which changes the spelling and not the word: `parra lettic`, `shatoe nerf doo pap`,
`blaow`, and `the last part` (a deliberate correction of the released `a cast part`).
Line breaks differ in five places — see §4a — and those change timing, not words. Re-run
the check after any edit:

```bash
# from docs/stories/camping/songs/ — strips cues, punctuation and respellings, then diffs
python3 - <<'EOF'
import re,io,difflib
def lyr(p):
    b=re.search(r'```lyrics\n(.*?)```',io.open(p,encoding='utf-8').read(),re.S).group(1)
    return [l.strip().strip('()') for l in b.split('\n') if l.strip() and not l.strip().startswith('[')]
def norm(ls):
    t=' '.join(ls).lower()
    for x,y in [('parra lettic','paralytic'),('shatoe nerf doo pap','W'),('châteauneuf-du-pap','W'),
                ('blaow','blough'),('the last part','a cast part')]:
        t=t.replace(x,y)
    return ' '.join(re.sub(r'[^a-z ]','',t).split())
a,b=norm(lyr('camping-released.md')),norm(lyr('camping.md'))
print("IDENTICAL:",a==b)
for d in difflib.unified_diff(a.split(),b.split(),lineterm='',n=2):
    if d[0] in '-+' and not d.startswith(('---','+++')): print(" ",d)
EOF
```

**Structural rules the sheet obeys**, each bought with a failed round: **zero
parentheses** (they are a mix-position mechanism, not a name tag — round 1); **one cue per
section**, carrying the voice label in fixed repeated wording; **no cue inside a verse**,
because every mid-verse bracket tried inserted an instrumental gap (rounds 6–10) — a
section *header* carries the mid-verse arrangement change instead; and **no `half-time`
anywhere**, a known Suno blind spot that thins the arrangement instead of halving the
drums.

```lyrics
[Intro — 8 bars | one long low detuned synth note, completely alone | held, slowly filtering open, cold and menacing, growing in threat | a texture, not a tune: no melody, no phrase, no notes changing | distant city hum far underneath | no drums, no bass, no guitar]
[Verse 1 | gravelly ranting voice — a weathered British man in his fifties, low, smoke-worn, nasal | ranted over the beat, half-shouted and half-muttered, close and bone dry | the low synth note holds underneath | a low palm-muted single-note electric guitar riff comes in with the voice and runs the whole verse — a distorted, overdriven rock guitar tone, hard and dirty, played tight and dry on the bottom strings | the same short figure repeating steadily, changing note only every bar or two — not a solo, no chords, no strumming, no fast runs | no drums and no bass for the first half of this verse, then a dry chopped breakbeat comes in underneath the vocal and runs to the drop, with a chopped amen break rolling in as a fill at the end of every eight bars | a short hard synth stab starts repeating underneath once the beat is in | the words never stop and there is no instrumental passage anywhere in this verse]
Once again and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you KEEP ON WALKING through that Wait trose door
presenting yourself with your shiny teeth
fucking sense of entitlement and self belief
I get that you think your deals are slick
but I bet that you paid for your wheels on tick!
cash from the bank for your wank tank
let me count up all the cans that I drank
I'm not alone and I'm sick of this crap
this widening gap, now let's — go snap snap
crackle and pop, I want change,
not from your pocket but at the top
in the meantime though let me hold that door
please sir, can I FUCKIN, have some more?
[Drop — instrumental, 16 bars, no vocals | the kit hits full weight and the sub bass drops for the first time | heavy Reese bass, dark and relentless | a chopped amen break rolls in as a fill at the end of every eight bars | the guitar drops out here | a screaming detuned wavetable lead tears in over the break — hard-synced, bending, formant-morphing, gnarly mid-range, cutting against the drums]
[Beat Transition]
[Verse 2 | well-spoken posh voice — a completely different man, same age, light, crisp, plummy BBC English | talking down at you, unhurried, from a wide open room, smug and mocking | full-weight drum and bass carries straight on, drums flip, colder synths, sharper hats | a chopped amen break rolls in as a fill at the end of every eight bars | the same low palm-muted distorted electric guitar riff returns underneath, same tone, steady and unchanged | nothing else playing at all]
you are intent on living in a tent
get fucked all day and pay no rent
it's a lack of work ethic, quite pathetic
getting parra lettic and you just don't get it
prospects exist and you just resist
and now I insist that you just stop the grift
What about if we taxed the rich?
Oh my, here's the sitch, SPEAK TO THE HAND BITCH!
I work hard to pay for my yard
an I pay my tax on all my stacks
you want change but my pockets are empty
the only thing I'm changing
is the lanes in my M3
if you worked hard, then you could have plenty, fenty,
all you seem to now do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Drop — instrumental, 16 bars, no vocals | heavier and more distorted, neuro bass growl | the amen break fills come harder and more chopped than the first drop | the lead synth harsher and more distorted than the first drop, screaming higher, more bend and more formant movement | growling neuro bass underneath it all]
[Beat Transition]
[Bridge | the turn | drums strip right back, intimate | the two men trade, both close and dry in the same cold room now]
[gravelly ranting voice]
Oh shit, here we both are, living in a car
park, in the rain and the dark, fast start
[well-spoken posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men together, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now, blaow
[well-spoken posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly ranting voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[well-spoken posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly ranting voice]
yet I don't begrudge you, let's get along
let's make a happy ending for this song
[well-spoken posh voice]
well we don't have long and it might go wrong
[Outro — 8 bars | both voices together | diminuendo, voice and bass dissolve into static]
but by the time it hits, we'll be gone
[end]
```

### 4a. The timing pass — why lines land off the bar

**The mechanism.** Suno allocates a musical **phrase per lyric line**, then fits that
line's syllables into it. Delivery speed is syllable density per line — no tempo
instruction touches it. And the compounding rule: **the first line of a section sets
the bar length for the whole section**, and every later line is force-fit into that
same slot. A section that runs 9 syllables → 15 doesn't smoothly speed up. It
**crams** — and cramming is what "rushed, and not starting at the start of the bar"
sounds like.

**What the measurements said.** Only 5 of 48 lines were genuinely over the density
ceiling, so this was never mainly a speed problem — it was a **consistency** problem.
Before the pass:

| Section | Range | Mean |
|---|---|---|
| Verse 1 | 7–12 | 9.7 |
| Verse 2 | 8–**14** | 10.4 |
| Bridge | 9–**15** | **11.4** |

The bridge was worst on both counts, which is where it would be most audible.
After the pass: bridge max 15 → 13, mean 11.4 → 10.0.

**The second mechanism, and it explains the off-the-bar feel specifically.** Suno puts
vocal stress on the downbeat. A line that opens with a run of unstressed function
words — *"and you looking to…"*, *"in having the manager…"*, *"the only thing I'm
changing…"* — is a pickup, so the model either starts it early or crams it to force
alignment. **Mismatched stress reads as rushed even at a safe syllable count.**

### The three levers, none of which change a word

1. **Line breaks — the strongest.** Each line gets its own phrase, so splitting a
   15-syllable line into 7 + 8 halves the density *and* buys a second bar. This is the
   main tool, and it costs nothing but layout.
2. **Commas — a comma marks a stress boundary; the pause is the side effect.** Tested
   on the GPOM chorus: what matters is **how many stress units you carve the line
   into**, not how many commas you used. Two commas beat zero *and* beat three on the
   same line. Say the line aloud as you'd perform it and put a comma where you'd
   breathe — usually two or three units, never one-per-word.
3. **Don't describe metre in the Style box.** Tested trap: `one word per beat, locked
   to the grid` reads as precision but *is* a slow, drawled delivery. Describe the
   density you want (`rattled off fast, no space between the words`), never a beat count.

**Asymmetry worth knowing:** a line that's too short gets **stretched**, which sounds
deliberate. A line that's too long gets **crammed**, which sounds broken. When in
doubt, break it shorter.

**Multiple spaces do nothing.** Not a documented mechanism — Suno's pause vocabulary is
the comma (a beat), the full stop (full break + pitch reset), the line break (longer
pause), the ellipsis (trailing drift) and a hyphen inside a word (stretches the note).
The double space in the snap-snap line has been swapped for an em dash, which is a real
longer-than-a-comma pause.

### What changed in the lyrics block above

Words untouched. Five lines re-shaped:

| Line | Was | Now |
|---|---|---|
| `the only thing I'm changing / is the lanes in my M3` | 14 syl, one line | 7 + 6, split |
| `in having the manager / or any of the c-suite about` | **15 syl** — worst in the song | 7 + 8, split |
| `you see as it turns out, / there is very little clout,` | 13 syl | 6 + 7, split at its own comma |
| `if you worked hard, then you could have plenty, fenty,` | 13 syl, 2 stress units | comma added → 3 units |
| `now let's — go snap snap` | double space | em dash |

Revert any of them by rejoining the lines — nothing else depends on the split.

**Still over budget and deliberately left:** `and sicker than when the government
debased us` (13). Every available break falls mid-clause and would read worse than the
cram. If it rushes, that's the one to hand to Studio.

### If it still drifts — Studio warp and quantize

The honest ceiling: the lyric sheet gets the phrasing close, **Studio gets it exact.**
This is the literal answer to "the line doesn't start at the start of the bar", and it
works after generation on any clip:

1. Open the song in Studio, set BPM to **Manual** and type 174 — auto-detect drifts.
2. Click the vocal clip's waveform to drop a **warp marker** at the drifting point (or
   auto-place markers at every transient).
3. Drag the marker to where the syllable should land. Time-stretches without changing
   pitch.
4. **Quantize** snaps the marked points to the tempo grid.
5. Coarser, non-destructive alternative: click the clip, `4` for the sidebar, set
   **Clip Settings → `On Beat`** rather than `Original Tempo` — locks the whole clip to
   the project grid.
6. If you split to fix a region, finish with **Heal Edits** to blend the seam.

**And re-roll before any of this.** Phrasing varies between takes on an identical sheet;
a re-roll is cheaper than surgery.

### 4b. Pronunciation fixes — respelling is not a word change

Suno has **no dictionary and no IPA**: it sounds words out from English spelling
patterns. So the fix for a mispronounced word is always to **spell it the way it
should sound**, not the way it's spelt. The word you hear is unchanged — only the
spelling that produces it. That keeps the released lyric intact.

| Was | Now | Why |
|---|---|---|
| `paralytic` → `paraletic` → `paralettic` → **`parra lettic`** | Took three goes, and the failures are the interesting part. The rhyme chain is **ethic / pathetic / paralytic / get it**, all on a short *-et-*, and the `y` spelling pulls the stressed vowel long. But **both single-word respellings kept coming out "paralytic"** — because they still *look like* the word, so the model recognises it and normalises back to the dictionary pronunciation. **Splitting it into two words defeats the recognition**, which is exactly why the wine worked. `parra` (double r → short *a*), `lettic` (double t → short *e*, as in athletic). Four syllables either way, so no timing cost. |
| `Châteauneuf-du-Pap` | `shatoe nuff doo pap` → `shatoe narf doo pap` → **`shatoe nerf doo pap`** | Two faults in one word, and the second is the interesting one. The middle token then took one more pass by ear: `nuff` sat wrong, and `narf` reads as */nahf/* in a non-rhotic British mouth, which is closer to the French *neuf*. **The risk to know:** `ar` is only r-less if the voice stays British — if the accent ever drifts American this is the token that will sprout an R. The rest of the line was right first time. |
| `BLOUGH` → **`blaow`** | Came out as neither `blow` nor `blau` — a mumbled `bleh`. **`-ough` is the least soundable-out cluster in English**: it maps to at least seven different vowels (*through, though, tough, cough, bough, thorough, hiccough*), so a model working from spelling patterns has no way to pick, and on a **nonsense** word there is no dictionary entry to fall back on either. `blaow` is an attested spelling (the grime/hip-hop ad-lib) that can only be read one way, and it lands the `allow / now / blaow` chain. |

**Why the wine came out slow, and it wasn't the model being careless: a hyphen inside
a word is a documented brake.** It makes the vocalist hold and bend the note.
`Châteauneuf-du-Pap` carries **two** of them, so the line was being explicitly
instructed to stretch exactly where it needed to rattle. Dropping the hyphens is the
speed fix; the phonetic respelling is the pronunciation fix; and the circumflex goes
because a model sounding words out from English patterns has no use for a French
diacritic.

The line stays comma-free on purpose — no punctuation reads as a **wall of words that
gets rushed**, and rushed is the brief here. The `pap` spelling is load-bearing for the
rhyme with `crap` in the line above, so it survives the respelling.

**The rule both fixes share, and it's the reusable one: when a respelling keeps getting
overridden, the model is recognising the underlying word — break it into separate words
so it can't.** A single respelt token is still a token; two short ones aren't the word
any more. Escalation ladder: respell → double the consonants → **split into words**.
Ladder for this one if `parra lettic` still fails: `pa ra lettic`, then `parra let ick`.

**The split rung is only available to multi-syllable words.** `paralytic` and
`Châteauneuf-du-Pape` are four syllables each, so they had syllables to redistribute
across two tokens at no timing cost. A **monosyllable cannot be split** without adding a
beat to the line. For one-syllable words the ladder is shorter: **respell to an attested
spelling** (one a human writer would actually use, so the model has seen it) → **double
the vowel** (`blaaow`) → give it its own stress unit with a comma. `blaow` is rung one;
`blaaow` is the untested fallback.

**And take the word out of ALL CAPS if it isn't a real word.** Caps are already on our
known-unreliable list as an emphasis mechanic, but on an invented word they carry a
second, worse risk: an unfamiliar all-caps token reads as an **initialism**, and the
model tries to spell it out or gives up and mumbles. The other shouts in this song —
`KEEP ON WALKING`, `FUCKIN`, `SPEAK TO THE HAND BITCH!` — are real words and can't be
misread that way, so they stay. **Caps are a risk in proportion to how unfamiliar the
token is.** The shout is carried by the spelling instead: `blaow` *is* a shout in the
tradition it comes from.

The comma before it is restored from the released take as well. A comma marks a stress
boundary, so `now, blaow` gives the payoff word its own unit to land on rather than
tacking it onto the tail of the previous phrase — which is where a one-word shout wants
to be.

**Consistency rule:** if either word ever recurs, spell it the same way every time —
inconsistent respelling reintroduces the error.

**Still intermittent, deliberately untouched:** `pathetic` occasionally not landing in
the chain. Intermittent means **re-roll**, not rewrite — don't respell a word that
mostly works. If it becomes reliable-bad, `pathettic` is the untested fallback (the
double consonant biasing the vowel short); try it once and keep it only if it wins.

### 4c. The second layer — six attempts, and what finally fit

**The short version, because this took six rounds.** Camping wanted *something* besides
voice and drums. Five attempts came from outside the track's own genre and all five
failed: GPOM's strings (sounded like GPOM), a dub piano and horn section (upbeat and
bouncy), a glockenspiel and French horn (whimsical, and it made them sing). **The sixth
tries the obvious thing instead — the synthesizers the genre already uses.**

**Two rules came out of it that are worth more than the arrangement itself:**

1. **A melodic accompaniment invites a melodic vocal.** The glock and horn gave the model
   a tune under the verses, and it handed that tune to the singer — four rounds of casting
   work undone by the *accompaniment*, with no vocal clause touched. **If a spoken-word
   delivery starts drifting sung, look at what is playing underneath it.** The synth layer
   is deliberately a *texture* under the verses (one held, filtering note; one repeating
   stab) and only becomes a *lead* in the drops, where there is no vocal to influence.
2. **When five wordings of the same idea each fail differently, the category is wrong,
   not the wording.** Each orchestral attempt was fixed correctly and then failed in a new
   way. That pattern is the signal to change direction rather than iterate again.

**How the synths are worded.** Serum is the reference sound but **its name is not in the
prompt** — plugin brand names are unreliable at best and an alias-collision risk at worst
(see `skank`, below). The transferable term is **`wavetable`**, plus the behaviours that
make the sound: `screaming detuned wavetable lead, hard-synced, bending, formant-morphing,
gnarly mid-range`. `My Taste` adds `no orchestral instruments and no piano anywhere`, which is the
line holding six rounds of orchestral wreckage out of the track — narrowed from
`no acoustic instruments` in round 14, which was broad enough to block the guitar too.

**Note on "dancehall".** Read as **dancefloor** D&B — big-room, main-stage synths — not
the Jamaican genre, which is excluded along with the rest of the reggae direction.

### 5. Settings

Style influence **75** · weirdness **30** · **no saved Voice** · model **v5.5**.

**No saved Voice is deliberate and load-bearing.** A Voice binds the lead slot for the
whole track — it has no section scope — which is exactly what made Bob and Tarquin
identical on the released take. Weirdness sits at 30 because a cue-heavy sheet wants
obedience over invention.

### If the delivery goes flat

Stripping the cues is deliberate and it may cost performance — the released take's
delivery came from them. If the take fixes the timing but the verses read
monotonous, re-add **only these four**, on their own lines, and nothing else:

```
[whisper, conspiratorial]   → before "but I bet that you paid for your wheels on tick!"
[shout, full chest]         → before "cash from the bank for your wank tank"
[shout, cracking, begging]  → before "please sir, can I FUCKIN, have some more?"
[mocking falsetto sneer]    → before "What about if we taxed the rich?"
```

Four cues across the whole song, at the four moments that actually change. That's
the level the research calls minimal, and it keeps the peaks without chopping the
verses into micro-sections.

---

## If a round still gives one voice — cut on the drop

Likely, and worth planning for now: **stop asking one generation to be two men.**
Camping's 16-bar drop is still a natural edit point, and every source — ours and the
web's — lands in the same place: generate separately, assemble in production.

1. **Generation A — Bob's half.** Intro + verse 1 + drop. Style box describes
   **one** voice: the low gravelly one. Lyrics box carries verse 1 only.
2. **Generation B — Tarquin's half.** Verse 2 + drop, against the **same** style
   foundation but describing **only** the high clean voice.
3. **Generation C — the bridge.** This is the one place a single-generation duet
   has a real chance: short alternating complete lines is the pattern that
   stabilises best. Same four-axis contrast, short repeated labels.
4. **Join at the drops** in any DAW, or in Studio with BPM set to Manual.

The win is that the voices never share a generation, so there is nothing to
average and nothing to swap. Casting stops being probabilistic. Say the word and
I'll write the click-path, including the settings for each generation.

**A saved Voice per character becomes correct at this point** — one Voice per
generation is exactly the supported case, and it's the strongest version of this
plan. It's what a Voice is for; round 1's mistake was attaching one to a track
that needed two.

---

## Watch items

- **"AI"** in the bridge may render as a word rather than the letters. If so,
  respell `A-I` consistently everywhere it appears.
- **ALL CAPS** ("KEEP ON WALKING", "FUCKIN") is not a reliable shout mechanic on its own,
  and the sheet no longer carries the bracket cues that used to back them. If those lines
  lose their force, the fix is the four-cue re-add list in *"If the delivery goes flat"*.
  Both are safe to leave capitalised because they are **real words**; `blough` was not,
  and its caps were dropped for exactly that reason (§4b).
- **Verbatim: verified 2026-08-21, and it now is.** Three words had drifted and were
  restored — `getting`/`paying` back to `get`/`pay`, and the missing `an` before
  *"I pay my tax"*. The only intentional departures are the four respellings and
  `the last part`, all listed in §4. **Re-run the check in §4 after every lyric edit**;
  drift is silent and none of these were noticed by ear.
- **One interpretive call:** the final line, unattributed in the released lyric,
  is cued as **both men together**. Change it to the high clean voice alone if you
  want the released reading.

