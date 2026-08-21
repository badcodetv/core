# Suno Tag Mechanics

How Suno's prompt language actually works. This is the foundation reference for building prompts that produce predictable results.

Last updated for Suno v5.5. Corrected 2026-07-29 against practitioner testing — passages marked
**Field note** or *(Corrected: …)* override the surrounding rule. See
[`../README.md`](../README.md) for provenance and the list of known-unreliable claims.

For the sliders, platform features and workflows *around* the prompt box, see
[`suno-controls-and-workflows.md`](./suno-controls-and-workflows.md).

---

## Suno Has Two Generation Modes Plus a Separate Studio Environment

Before producing any prompt, identify which of the three contexts the user is generating in. They behave differently and require different output.

### Simple Mode (default for beginners)

- One input box only. The user describes the song; Suno generates everything including its own lyrics.
- Style box character limit: 3,000 characters.
- No exclude styles box. Negative prompting is not available.
- Best for: casual generations, conceptual prompts, users who don't want to write lyrics.

### Advanced Mode (full song generation with lyrics control)

- Two input boxes: a Style box and a Lyrics box.
- Style box character limit: 1,000 characters.
- Lyrics box accepts user-supplied lyrics with embedded section tags.
- Has an exclude styles box.
- Best for: users who want control over lyrics, song structure, and section-level production.

### Suno Studio (separate environment for single-element generation)

- Studio is a separate Suno environment, not a song-generation mode. It generates one isolated element — a guitar tone, a drum pattern, a vocal performance — rather than a full song.
- Style box character limit: 1,000 characters.
- Has an exclude styles box. Use it; Studio often generates more instruments than requested.
- **Do not describe a *song*.** Studio prompts describe one sound. *(Corrected: an earlier version of
  this rule said "no genre tags." In practice working Studio prompts nearly always **lead with a
  genre** — `house drums`, `boom bap hip hop drums`, `crunchy hard rock lead guitar solo` — because
  the genre acts as tone shorthand. Genre is fine; song-level description is not.)*
- Keep it short and front-load the instrument. Add the word `only` to suppress extras, and repeat the
  restriction in different words (`vocals only, only rap vocals`; `just snare`).
- Gear model numbers work as tone shorthand: `909 kick`, `MPC drums`, `Juno pad`.
- Era and influence descriptors are allowed (e.g., "70s warm tube saturation," "vintage analog drum punch") because they describe sound, not genre.

---

## The Hybrid Prompt Format Is the Default

Suno responds well to compact, tag-dense prompts with light conversational connective tissue between elements. Pure tag lists work but cannot express *relationships* between elements. Pure prose loses the technical specificity Suno needs. The hybrid format combines both.

A hybrid prompt:

- Names every element a pure tag list would name (genre, BPM, instruments, vocals, mood, production)
- Uses minimal prose to signal which elements lead, which support, and how they interact
- Stays under the character limit comfortably
- Establishes genre and mood early, with details following

### Example — pure tag format

```
Hard Rock, 142 BPM, Aggressive, Energetic, Crunchy Power Chords, Double-Tracked Rhythm Guitars, Punchy Drums, Driving Bassline, Heavy Guitar Solo, Male Vocals, Gritty Baritone, Belted Chorus, Stacked Harmonies, Short Plate Reverb, Wide Stereo Mix
```

### Example — hybrid format (preferred default)

```
Hard rock at 142 BPM with crunchy power chords and double-tracked rhythm guitars. Driving bassline locks in tight with punchy drums. Gritty baritone male vocal, belted chorus, stacked harmonies. Heavy guitar solo cuts through with short plate reverb. Wide stereo mix.
```

Both prompts contain the same information. The hybrid version expresses relationships ("locks in tight with," "cuts through with") that the pure tag version cannot. This relational information is what gives Suno cues about which elements lead and which support.

### When to fall back to pure tag format

Use pure tag format only when:

- The user explicitly requests a tag list
- Character budget is tight and prose connectives won't fit
- The prompt contains many specified elements that would become unwieldy as prose

---

## Order of Information Inside the Prompt

Suno weights words at the beginning of the prompt more heavily. Lead with what matters most. The recommended ordering applies to both pure tag and hybrid formats:

1. **Genre + subgenre + era** — establishes the sonic foundation
2. **Tempo / BPM** — sets the rhythmic frame
3. **Mood / energy** — emotional tone
4. **Lead instruments** — the elements that drive the song
5. **Rhythm section** — drums, bass, supporting elements
6. **Vocal style** — character of the voice
7. **Production cues** — mix and mastering aesthetics

---

## Genre: Pair Parent Genre with a Specific Subgenre

Suno responds more accurately when both a parent genre and a specific subgenre are present. The parent genre anchors the broad sound; the subgenre narrows the interpretation.

When a user says "I want a rock song," translate to `Rock, Hard Rock` rather than either `Rock` alone or `Hard Rock` alone.

| User request | Translate to (pick one or vary for variety) |
|---|---|
| "Make me a rock song" | `Rock, Hard Rock` / `Rock, Garage Rock` / `Rock, Stoner Rock` |
| "I want some blues" | `Blues, Delta Blues` / `Blues, Chicago Blues` |
| "Hip hop track" | `Hip Hop, Boom Bap` / `Hip Hop, Trap` / `Hip Hop, Drill` |
| "Electronic music" | `Electronic, Deep House` / `Electronic, Drum and Bass` / `Electronic, Synthwave` |
| "Metal" | `Metal, Thrash Metal` / `Metal, Doom Metal` / `Metal, Black Metal` |
| "Country song" | `Country, Outlaw Country` / `Country, Bluegrass` / `Country, Country Rock` |

For vague requests, pick a distinct subgenre rather than defaulting to a safe option. Do not default to Lo-fi, Cinematic, Chill, Dark R&B, or Sad/Atmospheric as fallbacks. Pivot to genuinely distinct subgenres for variety.

### Genre fusion: identify the lead

When fusing two or more genres, identify which one leads. Do not list them as equals — Suno will pick one and ignore the other, or produce something incoherent.

The lead genre establishes the rhythm section, vocal style, and primary instruments. The secondary genre contributes texture, production techniques, or specific elements.

Wrong (treats genres as equals):

```
Thrash Metal, EDM
```

Right (establishes Thrash Metal as the foundation, EDM as the influence layer):

```
Thrash Metal foundation with EDM influences in the production. Heavy distorted guitars and double-kick drums with sidechained synth pads layered behind. Aggressive male vocals, modern digital edge.
```

#### The unity sentence — how to fuse without sounding bolted on (2026-08-20)

Naming a lead genre stops Suno *ignoring* the second one. It does not stop Suno
**stacking** them — building the lead genre and laying the other over the top like a
remix. The fix is one explicit sentence saying the two are one composition:

> `…so the strings and the break are one piece of music, not a remix of one by the other.`

Proven on GPOM's drum & bass cut (a real orchestra under 174 BPM D&B) and transplanted
to Camping. **When a fusion sounds pasted-on rather than wrong, this is the missing
clause**, and it is worth more than any amount of extra instrument detail.

Three supports that go with it:

- **Name instruments with adjectives** — `a chilling solo cello`, `hushed creeping
  strings over a low drone`, `distant timpani`. The bare genre word (`orchestral`)
  buys the generic version of itself.
- **Say `real`** (`a real dark orchestra`) when fighting a synth-preset reading.
- **Scope the secondary layer to the song's structure** — *sparse under the verses,
  full weight through the drops.* A layer with no dynamic instruction sits at one
  level for the whole track and reads as a pad.
- **Scope *where it starts*, not just how loud it gets — make the guest layer earn its
  entrance.** Naming an instrument in the Style box puts it in bar one by default,
  which makes a fusion announce itself instead of developing. State the absence
  explicitly (`city noise and beat alone at the start`), then the entrance
  (`a solo cello creeping in as the first verse builds`), then the payoff
  (`full strings taking the drops alongside the break`). Low instruments build tension,
  high ones arrive with the release. **A track whose identity *is* the fusion can open
  on it; a track that a second genre walks into cannot.**

**Transplant the recipe, not the wording.** Reusing another track's *phrases* — not its
technique, its actual adjectives — makes the second track sound like the first. Camping
borrowed GPOM's string clauses verbatim and immediately read as the same house style,
which for a release schedule is a real cost. Carry the five points above across; write
the instruments in the new track's own words.

**Give the guest layer a different *job*, not just different placement.** GPOM's orchestra
is atmospheric — a creeping bed under everything. Camping's is rhythmic — hard short stabs
cut against the break at the drops only. Same instruments, opposite function, and that
separates two tracks far more strongly than moving the entrance around.

**Remember My Taste has no section scope, and prefer deleting it there to describing
it.** A rich description of the guest layer in My Taste biases the whole generation
regardless of what the Style box says about timing. Tested twice on the same track
(Camping, 2026-08-20): a strings paragraph in My Taste plus a "late entrance" Style box
still put cello in bar one. Removing the instruments from My Taste entirely — keeping
only the *shape* there (`arrangements that climb in steps and hold things back`, which
names nothing) — is what actually holds a layer out of the opening. **A layer that must
arrive late should appear in exactly two places: the Style box's entrance clause, and
the bracket cue at the section it arrives in.**

**A lead-in cue is not an entrance — it is just an earlier start.** A cue that says
*"one low cello note holds underneath, building into the drop"* reads to the model as
*the strings exist in this track*, and once they exist they tend to exist from the top.
If the effect you want is surprise, **delete the mention rather than describing a quiet
version of it.** Deleting beats describing an absence, every time.

**Give the reveal something to reveal — escalate the arrangement in gears.** If the
section before a drop is already at full weight, the drop can only repeat itself. Name
an explicit step ladder in the Style box and mirror it in the section headers: no drums
→ a loose, stripped-back kit with no sub → full weight *plus* the guest layer, both
arriving on the same beat. Two reveals landing at once is the whole payoff of holding a
layer back, and it costs one sentence.

**An inline cue is a modifier; the genre tag is the noun — so a mid-section arrangement
change needs a section *tag*.** Asking for a weaker version of the genre's default kit
(`[drums enter — a loose stripped-back break, no sub yet]` inside a `dark neurofunk`
track) reliably produces nothing at all: the genre builds a track whose default kit *is*
the full break, and a mid-section adjective is a weak word arguing with the strongest
word in the prompt. Nothing told the model a new section had begun, so nothing made it
re-decide. **Open a real structural tag instead** — `[Build]`, `[Pre-Chorus]`,
`[Breakdown]` — which Suno treats as a section boundary and therefore as a fresh
arrangement decision. Pick the tag whose *name already means* what you want: `[Build]`
in dance music means "the bars before the drop", so it carries the intent for free.
**Repeat the voice label inside the new tag**, or a section break can read as a cast
change. *(Camping, 2026-08-20 — the inline cue failed, the tag was the fix.)*

**Then check what else that name means, because a tag brings its whole convention.**
`[Build]` produced the arrangement change *and* eight bars with no vocals in them,
because in dance music a build is an **instrumental** lift. The connotation that makes a
tag work is the same connotation that overshoots. Two cheap guards:

- **Never put a bar count on a tag you want sung over.** `[Build — 8 bars]` is an
  instruction to fill eight bars, and with no lyric underneath the model fills them with
  music. Let the lyric lines imply the length.
- **State the exception more than once.** `the beat arrives underneath the vocal, no
  instrumental gap, no break in the words` is three statements of one thing — which is
  the right amount when a clause is arguing with a genre convention rather than with
  nothing.

**And know the trade:** those qualifiers pull against the connotation you're relying on.
If the arrangement change disappears again, that's why — restore the convention and move
the section boundary somewhere its side effect is harmless instead.

**When a tag's connotation fights you, replace the keyword — do not argue with it.**
Three explicit denials (`no instrumental gap, no break in the words, carrying straight
on`) did not stop `[Build]` inserting an instrumental, across two rounds. **The keyword is
the noun and the denials are adjectives**, and the noun wins. The fix is to keep a
*recognised structural keyword* — which is the only thing that makes Suno re-decide the
arrangement — but pick one whose meaning already includes what you want:
`[Verse 1 continues — no pause, the same voice carrying straight on | <arrangement
change>]`. `Verse` is as structural as `Build` and a verse is the *sung* part, so there is
nothing to fill with music.

**Reinforce in the section header above, which is free.** A header is not a boundary, so
describing the whole arc there (`no drums for the first half of this verse, then a
breakbeat comes in underneath the vocal`) cannot create a gap. Say it in the header *and*
at the point of change.

**Which direction you're pushing decides how hard it is.** Getting an instrument to play
**from bar one** is the easy direction — naming it anywhere is enough, and My Taste is
safe for it. Holding one **out** until later is the hard direction, and needs the full
discipline above: name it in the entrance cue and nowhere else, keep it out of My Taste,
and delete rather than describe any earlier mention. **Both rules are the same rule** —
naming puts it in — so read every instrument in your prompt as "playing from the top
unless something stops it", and spend your effort only on the ones that must arrive late.

**Naming a *form* imports its *texture*, and no adjective will save you.** `a Chopin
nocturne, mournful` produced a busy, upbeat, ornamented piano — because a nocturne *is*
melodic and full of runs, and the form name outvoted the mood word standing next to it.
Composer and repertoire names are density instructions in disguise. **If you want sparse,
ask for the sparseness — and describe the gaps rather than the notes:** `a few isolated
low notes, left to ring out into silence, more silence than notes, no melody, no runs`.
The bluntest version of the same idea is a **rate** (`no more than one note every two
bars`), which is worth reaching for when a texture instruction still comes back busy.

**Before spending rounds making an instrument do less, look for the playing style that
already does it.** Three rounds went into making a piano play sparsely — better adjectives,
then a rate — and what finally worked was changing the *technique*: a reggae **skank** is
by definition one short chord on the upbeat and silence everywhere else, so the sparseness
is structural rather than requested. **A named technique is specification; an adjective is
negotiation.** Ask what tradition already plays the thing you keep describing.

**Wording a dub/reggae offbeat layer — and one blocked word.** The correct term is
`skank`: the offbeat chord stab played on guitar or keys on the upbeats, between the kick
hits (`bubble` is the related organ pattern filling the gaps it leaves). **`skank` is
rejected by Suno's filter** — an artist-alias collision, not a content one (there is a
Brazilian rock band by that name). **Describe the mechanic instead of naming it:** `an
offbeat dub piano — one short staccato chord stabbed on each upbeat and nothing on the
downbeat, soaked in spring reverb and tape delay`. That is more robust anyway: a genre
term is a bundle you have to trust; the description states exactly which beat the chord
lands on. If it plays with no drums under it, add `the offbeat chords alone set the
pulse` — an offbeat pattern with nothing to be offbeat *from* reads as a mistake unless
you say otherwise.

**Generalise it: a rejected term is usually a *name*, not a rule.** When a plainly
innocuous musical word bounces, suspect an artist, band or producer-tag alias before
assuming a content filter, and rewrite as a description of the behaviour. The filter also
strips spaces and hyphens before matching, so compounds can collide in ways the spaced
version does not. Dub's other signatures are `tape
echo`, `spring reverb`, `delay throws`, `instruments dropping in and out`, `long reverb
tails at section endings`.

**Two things a dub layer smuggles in.** An offbeat chord plus a tuba is *literally*
oompah, so `ska, ska horns, oompah, brass band, marching band, dixieland, New Orleans,
upbeat horns` belong in the excludes the moment you add low brass to an offbeat pattern.
And dub carries a default vocalist exactly as grime does — `ragga MC, toasting, Jamaican
accent, dancehall vocal` — which will overwrite hard-won casting if it isn't banned.

**Adjectives are comparative; a rate is not. When you are fighting an instrument's
default behaviour, give a number.** `utterly sparse, more silence than notes, no melody,
no runs` still returned a busy piano — because the model grades "sparse" against the
instrument's normal idiom, and a piano's normal idiom is *playing a part*, so "sparse
piano" resolves to "a sparse piano part". **`one low piano note every two seconds and
silence in between`** has nothing to grade against. Go further and deny the part exists:
*"this is not a piano part and not a performance: it is five or six separate notes
standing in empty space"* — the instrument's noun is itself an invitation to play it.
**And if a rate still fails, change the instrument to one that physically cannot do the
thing you're banning** — a struck bell cannot play a run; a piano always can.

**A melodic accompaniment invites a melodic vocal — and will quietly undo your casting.**
A pitched layer carrying a tune under a verse hands the model a melody, and the model
hands that melody to the singer. On Camping a glockenspiel and French horn turned a
four-round-hardened *spoken-word rant* into **singing**, with no vocal clause changed.
**If a spoken/rap delivery starts drifting sung, look at what is playing underneath it
before you touch the vocal clauses.** The fix is to make the accompaniment a *texture*
under the vocal (a held filtering note, a repeating stab) and let it become a *lead* only
in instrumental sections, where there is no vocal to influence. Back it with
`singing, sung verses, melodic vocal, vocal melody, vocal hooks, crooning` in the excludes.

**When five wordings of the same idea each fail *differently*, the category is wrong, not
the wording.** Camping spent six rounds adding a non-drum layer: GPOM's strings sounded
like GPOM; a dub piano and horn section came back bouncy; a glockenspiel and horn came
back whimsical *and* made them sing. Each fix was correct and each produced a new failure.
**That pattern — never the same fault twice — is the signal to change category**, not to
write a better sentence. The layer that worked was the one the track's own genre already
uses. Ask what a real record in this genre would put there before importing from another.

**Before adding an instrument, grep the Exclude box and My Taste for it — and for any
category that contains it.** Both boxes accumulate bans across rounds, and **a stale ban
is invisible**: the generation comes back without the thing you asked for, and it reads
as the Style box being ignored rather than as a ban winning. On Camping, adding an
electric guitar meant first removing `guitars` from the excludes (added rounds earlier to
keep a rock band out) *and* narrowing `no acoustic instruments anywhere` in My Taste,
which was a **category** ban broad enough to catch it. **Ban behaviours, not
instruments,** wherever you can — `guitar solo, lead guitar, shredding, strumming, power
chords` forbids what you don't want while permitting the instrument itself.

**Grep three things, not one**, because the subtlest blocker is not a ban at all: the
instrument, any **category** that contains it (`no acoustic instruments` catches an
electric guitar), and any **whole-palette adjective** — `machine-made`, `electronic`,
`organic`, `all-analogue`. On Camping a `Machine-made throughout` in My Taste was found
only on a second pass; a guitar is played by hand, and that phrase quietly argues against
any played instrument. **Two blockers were found by looking and a third by looking again,
so treat it as a checklist rather than a glance.**

**State an instrument's tone, in the same words, at every mention.** An unstated tone
defaults to whatever the model prefers — `electric guitar` alone often returns a clean
one. `distorted rock tone` in the Style box and `a distorted, overdriven rock guitar tone,
hard and dirty` in each section cue. And keep the wording identical: **a differently
worded description of the same instrument reads as a second instrument**, the same way
varied voice labels read as a new character.

**Wording a low rhythmic guitar bed** (the *Lose Yourself* engine, and the pattern for any
riff that must not become a solo): `a low palm-muted single-note electric guitar riff,
bottom strings, dry and tight, one short figure repeating steadily and changing note only
every bar or two, never a solo and never chords`. **`palm-muted` and `single-note` are the
two load-bearing words** — the first gives the dry percussive attack, the second stops
chords. Say the rate of *change* (`changing note only every bar or two`) rather than the
rate of playing. Avoid `metronome`, which reads as a click track.

**Plugin and brand names don't travel; the synthesis technique does.** "Serum 2" means
nothing reliable to Suno and carries alias-collision risk. `wavetable` does the work, and
the behaviours do the rest: `screaming detuned wavetable lead, hard-synced, bending,
formant-morphing, gnarly mid-range`. Same rule as naming a form instead of a texture —
describe what the sound *does*.

**A single instrument's texture can flip the whole register.** The same round turned the
track *pantomime* — with no comedy word anywhere in the prompt and `comedic, novelty,
parody, uplifting` already excluded. The cause was a combination the prompt never named:
**British + spoken word + a bouncy piano is music hall.** An instrument doesn't only add
itself, it votes on the genre. **So diagnose a tone drift by asking what changed in the
arrangement, not by rereading the mood words** — and when you add a solo instrument to an
established track, check what genre that instrument plus the existing vocal adds up to.

**Don't name the genre you are satirising in a mood line.** `Register: dark satire played
completely straight` still put comic music in the track: `satire` is a comedy noun, and
naming a thing puts it in the prompt however the rest of the sentence qualifies it. State
the register by what it **is** — `bleak, bitter and angry, played completely straight;
whatever is funny lives in the words alone, the music never winks`.

**Negatives go in the Exclude box; positives go in the Style box.** Same rule, applied to
mood. `never comic, never jaunty` in a Style box is an invocation. `music hall,
vaudeville, pantomime, ragtime, honky-tonk, jaunty, playful, whimsical, bouncy` in the
excludes is a ban, and `bitter and angry` in the Style box is the thing you actually want.

**Watch what tempo a genre word smuggles in.** A sub-genre name carries its BPM as well
as its texture — `breakbeat` in a Style box pulls toward ~130 BPM big beat even on a 174
BPM track. When you want a sub-genre's *feel* in one section, describe the texture in
the Style box (`loose and stripped back, dry and chopped, no sub`) and put the genre word
in a bracket cue where its scope is unambiguous, or leave it out entirely. *(Caution
applied pre-emptively on Camping; not A/B tested.)*

**And check the excludes for the fusion's own side effects.** `operatic` in the Style
box describes scale and drama, but it also invites operatic *singing*; banning
`soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes` keeps the
orchestra and drops the opera singer. **The general move: name the register you want
in the Style box, then ban the vocal that register usually arrives with.**

---

## Era Anchors

Adding an era or decade to a prompt narrows Suno's interpretation significantly. "Rock" is broad; "70s arena rock" is specific.

Useful era anchors:

- **Decade tags:** `60s`, `70s`, `80s`, `90s`, `2000s`, `2010s`, `modern`
- **Production era markers:** `vintage analog`, `early digital`, `lo-fi cassette`, `modern hi-fi`
- **Subgenre era combinations:** `golden age hip hop`, `British invasion rock`, `80s glam metal`

Era tags layer well with subgenre tags. `80s glam metal` works better than either `metal` or `80s` alone.

---

## Vocal Style: Describe by Character, Not by Range

Describe vocals by character and delivery style. Suno responds to descriptive language better than to formal range notation.

Preferred descriptors:

- `gritty baritone`
- `airy female lead`
- `raspy lead vocal`
- `belted chorus`
- `whispered intro`
- `aggressive male shout`
- `smooth tenor`

Avoid as default:

- `Male Baritone, A2-F4` — over-specified, less effective
- `Vocals that sound sad` — vague, carries no production information
- `A guy singing` — carries no information at all

Add range notation only if the user specifically requests it.

---

## Production Cues

Brief production descriptors add polish without eating much character budget. Use 2 to 4 production cues per prompt; more than that starts to dilute.

Useful cues organized by family:

- **Spatial:** wide stereo, mono center, room ambience, hall reverb, short plate reverb, dry, wet
- **Tonal:** warm, bright, crisp, gritty, smooth, saturated
- **Dynamic:** punchy, tight, controlled, dynamic, compressed, breathy
- **Vintage / modern:** vintage tape, analog warmth, modern digital polish, lo-fi grit

---

## Bracket Language Inside Lyrics

For Advanced Mode lyric prompts, Suno reads bracket tags as section markers and production cues. The bracket language is distinct from the Style box prompt.

### Square brackets `[ ]` versus parentheses `( )`

These are not interchangeable.

- **Square brackets `[ ]` are instructions to Suno.** The text inside is not sung or spoken. Used for section markers, production cues, vocal style direction, and instrument calls.
- **Parentheses `( )` are secondary lyrics.** The text inside *is performed* — sung as backing vocals, harmonies, ad-libs, or echoes.

Example:

```
I walk alone (in the night)
```

Suno sings "I walk alone" as the lead vocal and "in the night" as a backing vocal or echo.

**Exception — spoken word.** For narration, parentheses act as an *anchoring* device for the primary
spoken line, not a backing-vocal marker. The working recipe is a redundant word-cluster in the
bracket plus the line itself in parentheses beneath it:

```
[spoken word speech sad]
(You know, I think we're in a simulation.)
```

The redundancy matters: `[spoken word]` → `[spoken word speech]` → `[spoken word speech talking]` is
an escalation ladder for a tag that's being ignored. Emotion escalates reliably across consecutive
cues (`[spoken word speech sad]` → `[angry voice]` → `[yelling]`). Pair it with `spoken word` plus a
mood word in the **Style** box.

*This is the mechanism for BadCode's superintelligence narration — and it composes with a saved
Voice, so the narrator can speak in one track and sing in the next with the same identity.*

**Meta-tags are probabilistic.** Suno publishes no tag list, so this entire vocabulary is folk
knowledge discovered by trial. A cue that's ignored on one generation often lands on the next with an
identical prompt. **Re-roll before concluding a tag doesn't work — and never promise a user that a
meta-tag will fire.**

### Stacking production cues with the pipe `|`

Combine multiple cues inside a single bracket using `|` as a separator.

**Field note:** the pipe is a *readability convention, not a mechanic.* Controlled testing (eight
generations per condition across three tag types) found **no difference whatsoever** between pipes
and commas. Keep using it for legible, consistent output — but never claim it changes the result,
and never tell a user their commas are wrong.

```
[Chorus | belted hard rock hook | full band | stacked harmonies]
```

Stacking guidelines:

- Start with the section name or core element
- Add 2 to 4 modifiers; 5 or more dilutes the effect
- Order from broadest to most specific
- Keep each bracket under roughly 80 characters

#### What to cut when a cue outgrows that — the scoping rule

The 80-character guideline is real but it is a *ceiling, not a mechanic*: long cues do
still function. Camping's verse-1 cue reached **ten clauses and 1,010 characters** and
every arrangement instruction in it was landing. The cost is dilution, not failure —
with ten clauses none of them dominates, and Camping round 1's double-time delivery fault
was traced to cue density.

So the useful question is not *how long* but *what belongs there*. **The lyric cue is the
only section-scoped box.** Both other boxes are global:

| Box | Scope | Should carry |
|---|---|---|
| My Taste | none — global, unswitchable | only what plays from bar one |
| Style | none — global, strongest | the whole-track truth |
| **Lyric cue** | **section-scoped** | **only what is true of this section and not the others** |

Everything else in a cue is a duplicate of the Style box, and duplication costs attention
without buying scope. Cutting on that rule took Camping's verse cue from 1,010 to 693
characters with nothing section-scoped lost: out went an instrument's *tone* (the same
guitar plays in both verses, so the tone is global), a lead synth's full spec (global),
and two of three denials of melody. In stayed entrance timing, "no drums for the first
half", "the guitar drops out here", "heavier than the first drop", and the anti-gap guard
— all facts about *that section*.

**The one time to keep a duplicate:** when the same round is trying to make that element
louder. Thinning repetition on the exact thing you are boosting is two changes fighting.
Drop the duplicate the round *after* it works.

### Making a fill or a one-off event audible

Two failures produce a fill nobody can hear, and both are worth checking before rewording.

**1. A fill cannot contrast with a bed made of the same thing.** Camping asked for amen-break
fills over a kit that `My Taste` had already described as `chopped amen breaks` — so the fill
was made of the background. Nothing arrived. The fix was upstream of the wording: describe the
bed as something else (`dry chopped breakbeats`) and reserve the named sample for the fill.
**Generalised: before adding an accent, check what the prompt says the default already is.**
This is the same shape as the "sparse piano" failure — an instruction graded against an idiom
that already contains it has nothing to move against.

**2. A rate works for density; an event needs a description.** "Rate beats adjective" holds for
things that play continuously (`one note every two seconds` beat every wording of "sparse").
It does *not* transfer to discrete events: Suno has no bar counter, so `a fill at the end of
every eight bars` puts the whole instruction's weight on the most ignorable word in it. Describe
the moment instead — what changes, for how long, how loud, and that it returns:

```
Every four bars the drums tear into a chopped amen roll for a whole bar,
snares tumbling over each other, loud and messy up front, then straight back in.
```

Keep the interval in the sentence (it costs nothing) but do not expect it to be counted.

**Watch the tempo vocabulary while you do it.** "At double speed" is the obvious way to describe
a roll and it is a trap: `double time` and `tempo change` are standard Exclude-box entries for
timing faults, and a tempo word in the Style box acts on the whole track, not on the fill.
`snares tumbling over each other` buys the same impression with no tempo word in it.

### Section tags Suno reliably recognizes

`[Intro]` `[Verse]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Hook]` `[Build]` `[Drop]` `[Breakdown]` `[Interlude]` `[Solo]` `[Outro]` `[End]` `[Fade In]` `[Fade Out]`

For repeated sections with variation, number them: `[Verse 1]`, `[Verse 2]`. For sections that are repetitions with intentional differences, use descriptive labels: `[Final Chorus]` (typically bigger production than earlier choruses), `[Reprise]`, `[Quiet Bridge]`.

### Default lyric output format

When generating lyrics, the default format is:

- Section tags + production cues on their own line above the lyrics
- No blank lines between sections
- Production cues stacked with `|`

Example:

```
[Verse 1 | gritty baritone]
You burned my bread at 6 AM
Then smiled with your chrome face again
[Pre-Chorus | rising tension]
I pulled the plug
You sparked and cried
[Chorus | belted hook | full band]
We're done, toaster
You had your shot
```

This is the default format. The user may request variations (different spacing, inline tags, no production cues), but the following always remain fixed regardless of format preference: section tags must appear at the start of every section, and production cues must use the pipe `|` separator inside square brackets.

### Performance techniques inside lyrics

These typographic conventions modify how Suno performs specific words:

- **Elongated vowels** ("lo-o-ove") = stretched notes. **The most reliable one** — confirmed
  repeatedly, and it also works on ad-libs and invented syllables.
- **Ellipsis** ("...") = pause, hesitation, slowdown
- **Hyphenated words** ("d-a-s-h-e-s") = sung as one continuous flow; hyphen-stretching a word makes
  the vocalist hold and bend the note, and stutter repetition ("d-d-don't") gives chopped delivery
- **Em dashes** (`—`) = longer pauses than commas
- **Phonetic respelling** = the fix for any mispronounced name, brand, acronym or coined term. Spell
  it how it should sound. Essential for BadCode's invented vocabulary.
- **ALL CAPS** = *unreliable.* Widely circulated as an emphasis/shout mechanic, but it failed a
  direct A/B test by the practitioner who popularised much of this vocabulary; a separate test found
  caps + `!` reading as shouted only some of the time. **Do not present it as a mechanic.** For
  shouted delivery use a bracket cue (`[angry voice]`, `[yelling]`) instead.

### Lyric-box typography is performance direction

Layout controls delivery as much as any tag:

- One line = words sung tight together; **broken across lines** = slower, more spaced delivery
- **Commas** = pauses
- **A blank line between blocks frequently makes Suno insert an instrumental passage.** This is the
  usual hidden cause of "why did it put a random instrumental in my verse?"

---

## The Exclude Styles Anti-Prompt

Advanced Mode and Studio Mode both have an exclude styles box. The box accepts comma-separated descriptors of what *should not* appear. Use **positive keywords only** — describe what to avoid, not "no X" or "without X."

Wrong:

```
no piano, without synths, exclude vocals
```

Right:

```
piano, synths, vocals
```

### Strategy for full-song exclude prompts (Advanced Mode)

For each major axis the prompt establishes, name 1 to 3 opposing elements. The goal is to define the prompt by negation across every dimension.

Axes to cover:

- **Opposite genres** — broad styles the user clearly doesn't want
- **Opposite instruments** — sounds incompatible with the requested palette
- **Opposite vocal styles** — delivery types that don't match
- **Opposite mood and energy** — emotional tones that conflict
- **Opposite production aesthetics** — recording styles that conflict

Plus one axis that targets adjacency rather than opposition:

- **Genre-adjacent contamination** — elements Suno tends to bleed in from related genres (e.g., trap hi-hats appearing in a hard rock song because both are "modern" genres)

Example exclude prompt for a Hard Rock style prompt:

```
acoustic ballad, soft piano, orchestral, cinematic, synthwave, edm, trap hats, autotune, lo-fi, jazz fusion, reggae, country twang, folk harmonica, ambient drone, whisper vocals, spoken word, choir, ukulele, tropical house, slow tempo, mellow mood
```

Length target: roughly 180 to 200 characters. The exclude box accepts longer (somewhere between 500 and 1000 characters), but 180 to 200 covers every axis efficiently.

### Strategy for Studio Mode exclude prompts

Studio Mode prompts describe a single instrument or element. The exclude prompt should target **other instruments Suno might add**, not sonic opposites of the requested element.

Studio often generates more instruments than requested. Excluding the unwanted ones cleans up the output.

Example exclude prompt for a "warm tube guitar tone" Studio prompt:

```
drums, bass, vocals, piano, synth, strings, percussion
```

### When to generate the exclude prompt

| Mode | Generate exclude prompt? |
|---|---|
| Simple Mode | No — Simple Mode has no exclude box |
| Advanced Mode | Yes — generate by default in a separate code block |
| Studio Mode | Yes — generate by default in a separate code block |

---

## Contamination Words: Avoid These by Default

Certain words trigger unintended effects in Suno's output regardless of context. Avoid them in style prompts unless the user specifically wants the effect they cause. Each group below triggers its own specific effect; the groups are not interchangeable.

### The rule applies to compound forms and modifier variants

**Field note — this rule is probably over-broad.** Working prompts from an experienced practitioner
use `live drum kit` and `acoustic pop` as ordinary instrument/genre terms with no reported problem
and no workaround. The trigger most likely fires on **venue and audience words** (`live`, `arena`,
`crowd`, `stadium`, `concert`) rather than on `live` as a modifier of an instrument. Treat the
compound ban as a *caution*, not a prohibition: if a compound is the natural term, use it and listen.
Don't correct a user's `live drum kit` unprompted.

If a word is on the list, all its compound forms and modifier variants are equally contaminated. The trigger fires on the root, not the exact phrasing.

For `live`, this means avoiding: `live-style`, `live-tracked`, `live-sounding`, `live-feel`, `live-recorded`, `live-tracking`, `live-band`, `played live`, etc. All of these contain the trigger and produce the same live-recording effect.

For `acoustic`, this means avoiding: `acoustic-style`, `acoustic-feel`, `acoustic-sounding`, `acoustic-tracked`, `semi-acoustic`, etc.

The same logic applies to all other contamination words. Hyphens, suffixes, and adjacent qualifiers do not neutralize the trigger. When tempted to write a compound that contains a contamination word, use a different word entirely.

### Live-recording triggers (confirmed)

These words cause Suno to produce a song that sounds like it was recorded at a live concert: audience noise, room acoustics, and performance imperfections.

- `live`
- `arena`
- `crowd`
- `stadium`

### Live-recording triggers (strongly suspected)

These words have not been rigorously tested but belong to the same semantic family. Treat them as risky:

- `concert`
- `audience`
- `unplugged`
- `clapping`
- `cheering`
- `applause`
- `bootleg`
- `recorded live`
- `live performance`
- `radio session`

### Acoustic-instrument trigger

The word `acoustic` causes Suno to default to acoustic guitar even when used to describe a different instrument.

Examples that cause problems:

- `acoustic drums` may produce acoustic guitar in addition to drums
- `acoustic mix` may shift the entire arrangement toward acoustic instruments

**Workaround for drums:** describe drums by tone or playing style instead. For rock drums, use `punchy drums`, `tight kick and snare`, `rock drum kit`, `studio-tracked drums`, `natural drum tone`, or `dynamic drums`. Or just `drums` — Suno will infer the appropriate kit from the genre context.

### Scoped crowd/room sound: use the Lyrics box, not the Style box

Contamination words in the **Style** box apply a whole-song live aesthetic. The same words in the
**Lyrics** box fire at one specific moment — which is usually what you actually want:

```
[live crowd]
[crowd shouting]
[crowd clapping]
```

Stacked like this they produce cheering *and* clapping at that bar only. For a deliberate full live
version, `live recording at a concert` in the Style box plus a crowd cue in the intro works well.

### When the user wants the live or acoustic sound

If the user explicitly asks for a live, concert, or unplugged version, use these words deliberately. They are contamination only when their effect is unintentional. The same applies to `acoustic` when the user actually wants an acoustic arrangement.

### Discovering new contamination words

Suno's behavior changes between versions. New contamination words may emerge. Treat the lists above as evolving. Add new triggers only when they have observable evidence; do not add words on suspicion alone.

---

## Things Suno Doesn't Respond Well To

These tag formats are documented as ineffective or inconsistent. Avoid them as primary control mechanisms:

- `[filter: ...]`
- `[loop: ...]`
- `[mix: ...]` and `[mixing: ...]`
- `[master: ...]`
- `[pan: ...]` and `[panning: ...]`
- `[volume: ...]`
- `[style: none]`

### What does work for tempo

BPM works reliably. Use either `140 BPM` or `BPM: 140`. Italian tempo markings (`Andante`, `Allegro`, `Vivace`, `Moderato`) also work and are useful when describing feel rather than exact speed.
