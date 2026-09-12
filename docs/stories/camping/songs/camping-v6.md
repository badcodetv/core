---
title: Camping — the live v6 sheet (arena direction)
status: DRAFT round a1 — awaiting Kai's ruling on the questions in §2 and an explicit yes before any credit is spent. Nothing generated.
brief: Jack, 2026-08-27 — "we have lost the aggression and the pace, experiment with different genres over the drum and bass." Kai, 2026-09-12 — the reference band is Imagine Dragons (https://en.wikipedia.org/wiki/Imagine_Dragons).
words_canon: ./camping.md  # §4 — frozen, not a variable in this sheet
predecessor: ./camping-sheet.md  # the v5.5 genre sweep, archived 2026-09-10
accepted_v55: ./camping.md  # the round-17 accepted boxes, un-rerunnable since v5.5 retired
workspace: camping-duet
model: v6
bpm: 174
---

# Camping on v6 — the arena direction

**Why this file exists.** Suno retired v5.5 on 2026-09-09, so the accepted round-17 sheet
([`camping.md`](./camping.md)) **cannot be re-run as written** — a v6 run is a new song. This is the
v6 successor sheet. The v5.5 genre sweep ([`camping-sheet.md`](./camping-sheet.md)) stays where it
is as history.

**The words are frozen.** [`camping.md`](./camping.md) §4 is canon and is not a variable in any
round here. Jack's video is cut to [`camping-released.md`](./camping-released.md); changing a word
would break a picture that already exists.

## 1. The reference, translated

Kai named **Imagine Dragons** on 2026-09-12. The band name never goes in the Style box — Suno
strips artist names — so it is translated into sound. Not all of it survives contact with this song,
and that is the point of writing the split down:

| Imagine Dragons trait | Producible here? | How it enters the box |
|---|---|---|
| Huge stomping percussion and handclaps | ✅ yes | `huge stomping floor toms and handclaps doubling the chopped breakbeat` — the single biggest change from the accepted box, and the direct answer to "lost the pace" |
| Half-shouted, strained male lead with dynamic lifts | ✅ yes, and it is what we already want | `half-shouted and strained, rising in force`; verse two `hardening into a shout` |
| Heavy reverb, big-room scale | ✅ yes | `drenched in reverb` |
| Electronic / dubstep-adjacent low end | ✅ yes — this is compatible with the Reese/neuro sub we already ask for | `filthy dubstep-adjacent sub` |
| Chant-along hooks | 🟡 **partly** — this song has no chorus and nothing sung. The only doubled moments in the words are the bridge's `[both men together, doubled]` and the outro | left OUT of the Style box in a1; see question Q2 |
| Big sung anthemic chorus, major-key lift | 🔴 **no** — it is the one thing the song cannot have. `never sung` survives every round | stays banned |

## 2. 🔴 Questions owed a ruling before a1 runs

- **Q1 — the exclude list.** The accepted list bans `live rock band`, `epic trailer music`,
  `power chords`, `uplifting` and `major key`. The first three are the Imagine Dragons sound and
  are **unbanned** below. `uplifting` and `major key` are **still banned**, because the song is
  bitter and the register is the one thing Jack has never complained about. Confirm, or unban them
  too as a later single variable.
- **Q2 — the chant.** Should the doubled bridge/outro lines become an explicit stomp-and-chant
  moment (arena's actual hook mechanism), or does that read as the "big chorus" we have banned for
  seventeen rounds? Not in a1 either way.
- **Q3 — the baseline.** The accepted boxes were never run on v6, so an arena take's faults cannot
  be cleanly attributed between "v6 changed it" and "arena changed it". A v6 baseline of the
  accepted boxes costs 20 credits. Recommendation: **skip it** — Jack's note is directional and the
  "before" in his ear is the released take, not a v6 control. Log the confound instead of paying
  for it.
- **Q4 — tempo.** Jack's brief is genres *over* the drum and bass, so a1 keeps 174 and asks for the
  stomp on top. Imagine Dragons' own records sit far slower (Radioactive ~136, Believer ~125). If
  a1 comes back busy rather than heavy, the next single variable is the arrangement's *density*,
  not the BPM — the picture is cut to a 174 track.

## 3. Round a1 — `arena`

**One variable, named before pasting:** this is a **prompt round** — Style and Exclude move together
as one atom ([`session-method.md`](../../../suno-gpt/session-method.md) §"One variable per round"),
lyrics frozen. No slider is touched; `explore`'s own two cells are the slider spread.

🔴 **The atom section below holds exactly three fences and nothing else.** Both readers work by
fence *position*, not by label, so one extra example fence inside the section silently shifts every
box by one — measured 2026-09-12: a `bash` fence at the top made `extract` return the shell command
as the Style box and drop the lyrics entirely. Any other snippet goes outside the heading, like
these.

### `arena` — the a1 atom

🔑 **All three boxes live under this one heading, in order — Style, Exclude styles, Lyrics.**
That is what `suno.mts extract` reads (it slices to the next heading and takes the first three
fences) and what `scripts/suno/measure-boxes.py` names them by. Splitting them across separate
`###` headings makes `extract` throw `expected at least style + excludes… found 1`, and — worse —
a two-fence section is padded with an **empty** lyrics box, which Suno reads as INSTRUMENTAL.
Measured, not assumed: it threw exactly that on this file's first draft, 2026-09-12.

**Style — 980 chars.** The box carries `maxLength="1000"` and truncates **silently**, so the tail
(where the bans live) is what gets lost. Re-measure after every edit with
`python3 scripts/suno/measure-boxes.py docs/stories/camping/songs/camping-v6.md` — never estimate.

```
Arena rock over UK drum and bass at 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat, never sung. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and strained, rising in force. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room, hardening into a shout. Huge stomping floor toms and handclaps doubling the chopped breakbeat, drenched in reverb. Four steps: one long low detuned synth note alone; then the voice over a low palm-muted electric guitar riff, one short figure repeating, never a solo; then the stomp and the dry break under the vocal; then the drop — toms and claps at full weight, filthy dubstep-adjacent sub and a screaming detuned wavetable lead cut against it, so the stomp and the break are one piece of music. Every four bars the drums tear into a chopped amen roll for a whole bar. Grim and bitter, played straight, steady tempo.
```

**What moved from the accepted box, and why each clause is there:**

| Change | Reason |
|---|---|
| `Dark UK drum and bass, neurofunk` → `Arena rock over UK drum and bass` | the genre tag owns the vocalist pool and the whole register. This is the variable. `British post-punk spoken word` **stays** — it is what holds the British middle-aged casting (`camping.md` §2) |
| added `huge stomping floor toms and handclaps… drenched in reverb` | the reference's actual engine, and the answer to "lost the pace" |
| `half-shouted and half-muttered, bone dry` → `half-shouted and strained, rising in force` | the reference's strained lift. `half-muttered` was doing the same flattening work `deadpan` did in the g1 sweep |
| verse two gains `hardening into a shout` | a dynamic lift the accepted box never asked for |
| `Reese sub` → `filthy dubstep-adjacent sub` | same frequency job, the reference's texture |
| the unity sentence kept verbatim in shape (`so the stomp and the break are one piece of music`) | `camping.md` §2 calls it load-bearing: without it the second layer sounds bolted on |
| `Grim and bitter, played straight, steady tempo` kept | the register is not under test |

**Exclude styles — 865 chars, 75 terms.**

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, autotune, harmonies, country vocal, southern vocal, americana, twang, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, US rap, transatlantic, southern drawl, ragga MC, toasting, Jamaican accent, dancehall vocal, soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, choir, orchestral strings, violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, lead guitar, shredding, guitar strumming, acoustic guitar, wah, reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honky-tonk, liquid dnb, jump up, pop, lo-fi, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, double time, tempo change, half-time, slow tempo
```

| Change from the accepted list | Reason |
|---|---|
| **unbanned** `live rock band`, `epic trailer music`, `power chords` | all three *are* the reference. Keeping them would have silently fought the whole round — the exact bug that cost the g1 sweep three rounds (`camping-sheet.md` §"Per-lane four-box atoms") |
| **added** `country vocal`, `southern vocal`, `americana`, `twang` | evidenced, not defensive: on v6 "rock still drifts to a country/southern vocal (3/3, even with Max Mode)" — [`files/suno-v6.md`](../../../suno-gpt/files/suno-v6.md) §9. An arena-rock tag walks straight into it |
| **kept banned** `uplifting`, `major key`, every sung/melodic term, `half-time`, `double time`, `tempo change`, `slow tempo` | the register and the pace. Q1 |
| **kept banned** every non-British vocal pool | casting; the released take's men are the song |

**Lyrics — frozen.** Copied verbatim from [`camping.md`](./camping.md) §4, which stays the words
canon. This fence is the **paste source** for v6 and the only one any v6 runner reads; the guard
below proves the two have not drifted. 🔴 Never edit this fence to change a word — edit
`camping.md` §4 and re-run the guard.

```lyrics
[Intro — 8 bars | one long low detuned synth note, completely alone, held and slowly filtering open | a texture, not a tune, no melody | distant city hum far underneath | no drums, no bass, no guitar]
[Verse 1 | gravelly ranting voice | the low synth note holds underneath | no drums and no bass for the first half of this verse, then a dry chopped breakbeat comes in under the vocal and runs to the drop | amen rolls tearing across every fourth bar | the words never stop, no instrumental passage in this verse]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whisper, conspiratorial]
but I bet, that you paid for your wheels on tick!
[shout, full chest]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[change tone to spoken word]
I can't live like this forever
[shouting]
I might be insane but I do want change, 
let's see what we can arrange!
now, I insist that I hold that door
[shout, cracking, begging]
please sir, can I FUCKIN, have some more?
[Drop — instrumental, 8 bars, no vocals | the kit hits full weight and the sub bass drops for the first time | amen rolls tearing across every fourth bar | the guitar drops out here | the wavetable lead tears in over the break]
[Beat Transition]
[Verse 2 | well-spoken posh voice, a completely different man | full-weight drum and bass carries straight on, drums flip, colder synths, sharper hats | amen rolls tearing across every fourth bar | the same guitar riff returns underneath, unchanged | nothing else playing at all]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto sneer]
What about if we taxed the rich?
[shout, angry]
what the fuck you think this is, BITCH!
[well-spoken posh voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Drop — instrumental, 8 bars, no vocals | everything heavier and more distorted than the first drop — neuro bass growling underneath, the amen rolls harder and longer, the lead screaming higher]
[Beat Transition]
[Bridge | the turn | drums strip right back, intimate | the two men trade, both close and dry in the same cold room now | the guitar riff sparser and quieter here, still one repeating figure, never a tune]
[gravelly ranting voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[well-spoken posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men together, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | well-spoken posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly ranting voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[well-spoken posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly ranting voice]
yet I don't begrudge you,
it's us and them now
[pause | well-spoken posh voice]
well we don't have long
[Outro — 8 bars | both voices together | diminuendo, voice, guitar and bass dissolve into static]
and by the time it hits, we'll be gone
[end]
```

### Settings

Model **v6**. `explore` sets its own two cells — v6 at weirdness 30 / Style Influence 75, and
v6-wild at weirdness 60 / Style Influence 60, Variety off, Max Mode off, Personalize off.
No saved Voice (a Voice binds the lead slot for the whole track and has no section scope — it is
what made Bob and Tarquin the same man on the released take).

## 4. Round log

| Round | Variable | Cost | Verdict |
|---|---|---|---|
| a1 | the arena atom (Style + Exclude together) | 20 credits, **unspent** | ⬜ awaiting Kai's yes |

## 5. Reading and checking this sheet

**Read it with these two commands, both free.** Neither connects to a browser or spends anything:

```bash
# the three boxes, as JSON
npx tsx scripts/suno/suno.mts extract docs/stories/camping/songs/camping-v6.md 'a1 atom'
# every box length, with the 1,000-char Style cap enforced
python3 scripts/suno/measure-boxes.py docs/stories/camping/songs/camping-v6.md
```

A section key must be **unique in the whole file** and must not appear above its own heading:
`extract` takes the FIRST match and slices from there, so a key that also appears in prose (or in
a documented command like the one above) returns an empty section. That is why these commands live
*below* the atom — measured 2026-09-12.

### The words guard

🔴 **Do not copy `camping.md` §4's verbatim check into this sheet.** It is DEAD and its own Watch
items say so: its baseline is `camping-released.md`, which carries the *pre-2026-08-25* words, so
it "now fails on ~80 words by design" and "cannot tell drift from the rewrite". Re-measured
2026-09-12: 419 released words against 393 in the sheet — it still fails. A check that always
fails is a check nobody reads.

**So this sheet's guard is byte-identity against the canon instead.** That is the invariant that
actually matters here: the words are frozen, so the only question is whether this paste source has
drifted from `camping.md` §4. It is exact, it cannot rot, and it passes today.

```bash
# from the repo root — exit 0 = the v6 paste source still IS the canon
python3 - <<'EOF'
import re, io, sys
d = "docs/stories/camping/songs"
def block(p):
    return re.search(r"```lyrics\n(.*?)\n```", io.open(f"{d}/{p}", encoding="utf-8").read(), re.S).group(1)
a, b = block("camping.md"), block("camping-v6.md")
print("v6 paste source is byte-identical to camping.md §4:", a == b, "|", len(a), "vs", len(b), "chars")
sys.exit(0 if a == b else 1)
EOF
```

✅ **Passes 2026-09-12** — 3,928 chars each, byte-identical.

**What is still owed, and is not this thread's call.** `camping.md`'s Watch items ask for a new
verbatim baseline — "the current block, frozen, once these words are signed off". Pinning this
sheet to `camping.md` §4 does not supply it: the released take and the canon genuinely disagree by
about eighty words after the 2026-08-25 rewrite, and deciding which is right is a words question,
so it belongs to Kai and not to a v6 style round.
