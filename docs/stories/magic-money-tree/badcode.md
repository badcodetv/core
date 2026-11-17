# The Magic Money Tree

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
"We can't afford it" is a choice; the real limit is the work, not the money. A country can **shake** its
money, **starve** it or **plant** it. Told three ways from this folder: a short archive **documentary**
(*The Future He Never Saw*, being recut to ~3 min: a sarcastic narrator interviews a WW2 soldier at each
age of his life), **Money For Something** (a deadpan topical comedy show, now cut as shorts), and a **song**.
Not in the first release.

## Parts
- Documentary — `storyboard.md`, `storyboard-loose-2026-10-01.md` — recut agreed 1 Oct; resume at the loose storyboard, scene 2 (who is the soldier).
- Money For Something — `money-for-something*.md` — 2026 year-in-news cut 3 built (unwatched); weekly shorts on Premiere timelines (26 Oct), Jack's lines owed; Paraguay shorts presenter on a mood board (`scenes/paraguay-presenter/`). Not ruled as the film by Kai.
- The song "Magic Money Tree" — `songs/magic-money-tree.md` — lyrics in progress, genre open.
- **Each part has its own look and sound. Don't carry one part's look into another.**

## Look
**Documentary** — EXPLORING (visual treatment not locked). Real archive footage, heavily: mostly British
Crown films of 1945–52 (picture only) and public-domain stills; illustration or generated imagery only
where nothing real exists, and clearly distinguishable from archive. Generated stills are colour, never
black-and-white. One verb card on every dated beat (`1923 · SHAKE`, `1948 · PLANT`). The soldier is not
designed or cast. No preamble: a text-first assembly must hold without attractive images.

**Money For Something** — LOCKED per episode by Jack's picks. A 2003 standard-definition recording of a
back-room comedy club: brick, a bare tree hung with pound notes, empty oxblood armchairs, a television on
red beer crates showing a plain blue "no signal" screen, a pint; warm amber spotlight from high left
against the television's cold blue. Host v2 is the balaclava host **D1**: hand-knitted cream balaclava,
the logo as the face (thin ring, small red triangle with rounded corners, over one eye — place it by
landmark), grey suit, black roll-neck, black knitted gloves, no skin. Made **by reference, not
description**: attach `mfs-balaclava-host-ref` then `mfs-club-plate-P1`; the man is not described. Nano
Banana 2 · 16:9 · x2 · Flow project `cb27208c` ("mmt jack"). Video: Omni 1.2 Flash, Frames, 720p, 8 s, one
locked frame per monologue. Cards: the "third style" (`build-topical-cards3.py`). Paraguay presenter: EXPLORING (mood board).

**Song video** — Not decided — run story-style.

## Sound
- **Documentary narration:** EXPLORING. After the recut: an "incredibly sarcastic" narrator (AI Studio) and a real-sounding old soldier, played real. Score minimal, documentary, never over a word, never dramatic. Neither voice built. A Suno scored-narration draft exists (pre-recut words; settings unruled).
- **Money For Something narrator:** AI Studio `Zubenelgenubi`, accent British (Brixton), nothing else in the boxes. LOCKED. One take in ten drifts: compare against the reference take.
- **On-camera voices (Oct episodes, Flow):** Host v1 `Sadachbia`, British Soldier `Algenib`, German Soldier `Alnilam`, Politician `Umbriel`; Podcast Host `Fenrir`, Water Boss `Schedar`, HS2 Reporter `Zubenelgenubi`. LOCKED.
- **Host v2 (balaclava):** TTS over stock movement clips, mouth never seen; voice EMPTY (a short AI Studio round, deadpan, unhurried, British, is suggested).
- **Song:** EXPLORING — four verses money / shake / starve / plant, hook "you can't SHAKE it — you PLANT it"; Kai writes every bar and is choosing the genre (an unproven jump-up D&B box sits in the sheet; a bar song was liked, not ruled).

## Story-only rules
- Real people: archive only, never generated; no fake archival testimony; no picture of Baroness Mone (headline screenshots); scene 11a needs a legal read first.
- Footage is cleared before it ships ([footage.md](./footage.md)); Crown-film audio is never used; no spend.
- Money is English pound sterling, never dollars — say so in every still and clip prompt.
- For the show, never write *audience, laughter, applause, comedy, newsreader, news* or *television studio* in a Flow prompt; say "a scripted television comedy… an actor plays a made-up character"; name the sound as the voice plus an empty room's hum; end a Flow line with "No music and no singing".
- Never an undefined screen or sign (it fills with invented writing). Every prompt ends `Thanks.`
- Read straight: ridiculous jokes with a straight face, no studio laughter. Jack writes the jokes.
- Anti-slop for show stills: describe the capture, one humble camera and stock, one named light, off-centre, something in the foreground, wear in the set, no quality words.
- Song: never "we printed the war"; "Keynesian" never a lyric; never the liquid / spoken-word version.

## Flow project
None recorded yet. Create one with `flow_create_project` before the first Flow call, and write its id here.

## Library pieces in use
- none yet

## Where the detail is
- [look.md](./look.md) · [sound.md](./sound.md) · [README.md](./README.md) · [RESUME.md](./RESUME.md) (documentary) · [money-for-something-RESUME.md](./money-for-something-RESUME.md) (the show)
- Documentary: [direction-2026-10-01.md](./direction-2026-10-01.md), [storyboard-loose-2026-10-01.md](./storyboard-loose-2026-10-01.md), [storyboard.md](./storyboard.md) (facts and sources), [footage.md](./footage.md), [rough-cut/](./rough-cut/README.md)
- Show: [money-for-something-2026-10-26-shorts-script.md](./money-for-something-2026-10-26-shorts-script.md), [money-for-something-2026-production.md](./money-for-something-2026-production.md), [characters/host-v2-balaclava.md](./characters/host-v2-balaclava.md), [money-for-something.md](./money-for-something.md) (cast and voices)
- Song: [songs/magic-money-tree.md](./songs/magic-money-tree.md) · narration draft [songs/narration.md](./songs/narration.md)

Unclear: the documentary narrator — scored Suno narration (29 Sept) or a sarcastic AI Studio narrator (1 Oct recut); the newer points to AI Studio but it is not ruled.
