# Camping

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
Tarquin, the trader who helped cause 2008, meets Bob, the man it ruined, outside Waitrose; an ayahuasca
trip drops Tarquin five years forward into Bob's tent, after AI has taken even his job. The point: the
crash's cost landed on the wrong man, and it is coming for the other one too. Two parts: a narrated story
film and a music video. **Don't carry one part's look or sound into the other.**

## Parts
- **Story film** — `scenes/story/` — Jack's cut, Premiere `0 synced` (Kai: the latest). Timeline page https://claude.ai/artifact/4Haz6YZqwWsCAJSMv5dyAE. Open: Tarquin's ending (he may wake as a banker with a changed mission; which film and what happens to beats 10–12 not said).
- **Music video** — `mv-song2/` (with `mv-balaclava/`, `mv-action/`, `mv-r10/`) — Premiere `camping song 2 beat 9`, built, awaiting Jack. Timeline page https://claude.ai/artifact/WbEmR8LxhyoT4LSjL1nbjM

## Story film

**Look — LOCKED.** A hyper-realistic documentary press photograph on 35mm: fine natural grain, muted
cool-neutral colour, flat overcast or motivated light, no lens flares, a calm observational eye. Ordinary
class-coded British places; the environment carries the argument. Warmth only in three places: the wank
tank's gold headlights, the ceremony fire, the fire in the ruins (scenes 10–12 go near-black with that fire
as the key). The
verbatim preambles per kind of frame are in [look.md](./look.md#preambles); every prompt ends
`Compose for a 16:9 frame.` then `Thanks.` Cast: `@Tarquin` `29e97ae3…`, `@Bob` `7566666e…` and variants in
Flow project `camping-v2` (`9b729074…`); the tent is blue and grey; the wank tank is a blacked-out BMW X8,
plate `BAD C0DE`. Clips: Omni 1.2 Flash.

**Sound — LOCKED voices.** Narrator Nell (AI Studio `Kore`, profile
[nell-kore.md](./narration/profiles/nell-kore.md)): low, controlled, sarcastic, north London; anger banked
down, never flatness. Tarquin `Zubenelgenubi`, Bob `Algenib`. Score: nine instrumental Suno cues
([songs/score.md](./songs/score.md)), EXPLORING; the crash is silent; one motif bookends the film.

**Working on it (Kai, 2026-11-27):** the film is made like every other story now: new shots are generated on
the scene tools (`scene-images` → `scene-animation`), new lines voiced in the locked voices, cut on the local
timeline. The old Camping-only rules (imagery by hand only, scene-numbered narration rules from the first
build) were deleted as outdated; Flow's prompt rules live in `docs/rules/flow.md`.

## Music video

**Look — EXPLORING.** Built on the earlier Bob-and-Tarquin music-video picture: every rap-to-camera shot
is now one of two BadCode balaclava men (a rough sleeper in "Duct Tape Armour", a posh man in "Estate
Tweed Squire"), grounded, rapping in a Ghostface Killah stage manner; action shots of the real Bob and
Tarquin (Flow Characters) sit on their lyric lines; a stadium opening and a bridge face-off. Every
balaclava: white ring, red triangle over the wearer's LEFT eye, never any skin, full gloves
([brand rule](../../brand/README.md)). Stills NB2 16:9 ×2 with the picked mask as reference, one prompt per
Flow project; clips Omni. Clean room: web research and sealed writers, run verbatim.

**Sound.** "Song 2" (`song 2 maybe (audio).wav`, 220.7 s): the Camping song rearranged, a new sung hook
"I can't live like this forever", cut to its beat (Jack's black-and-flash stutter on the drops). Unclear:
which Suno take song 2 is; [sound.md](./sound.md) has the released drum & bass take as LOCKED and the
reggae re-cut as EXPLORING, and its "the men never sing" rule conflicts with song 2's sung hook. Song rules
that stand: two voices that never blend, never double-time rap, no American accents, the words are fixed.

**Voice lessons from this song's Suno rounds** (moved here 2026-11-18 from the suno skills, where they sat as
examples): `UK grime influence` kept both men British but cast them as young MCs, when they are a weathered
fifty-something and a City banker; stripping the accent words and losing `UK grime` in the same edit brought
both back American. The fix is to name a performance tradition, not the age or class. Candidates written up
then, never picked: `British post-punk spoken word` for Bob, a BBC-announcer register for Tarquin. Also: a
fill over a bed that already is that fill never arrives (an amen fill over `chopped amen breaks`); three words
went missing across nine rounds of lyric edits, so diff the lyrics against the released sheet every round.

**Story-only rules (MV)**
- Jack's notes on a built cut: make only the noted changes, change nothing else.
- Check every clip for skin, fingerless gloves and a lost triangle or ring before it goes in.

## Flow project
- `9b36496c-9bad-48dc-bead-2691d115a4fe` — mv-action
- `76a7474d-c201-4f7c-8492-3b2c684de501` — mv-balaclava
- `72255ea1-f3e6-4714-b415-a5cc21ab3bc0` — mv-r10

Open the part's project before its first Flow call; never use it for another story.

## Library pieces in use
- none yet

## Where the detail is
- [look.md](./look.md) (full record and history), [sound.md](./sound.md), [README.md](./README.md)
- Film: [story.md](./story.md), [shot-list.md](./shot-list.md), [prompts.md](./prompts.md), [narration-brief.md](./narration-brief.md), [characters/tarquin.md](./characters/tarquin.md), [narration/ai-studio-cast.md](./narration/ai-studio-cast.md)
- MV: [mv-song2/README.md](./mv-song2/README.md), [mv-balaclava/picks.md](./mv-balaclava/picks.md), [mv-action/README.md](./mv-action/README.md), [mv-r10/scene.json](./mv-r10/scene.json)
