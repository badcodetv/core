# The Magic Money Tree — look

> The look for this story only. Read before any still or clip (new-image, scene-images,
> scene-animation, flow-prompt). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

This story has two pieces of film with two different looks:

1. **The documentary**, *The Future He Never Saw* ([`storyboard.md`](./storyboard.md), recut agreed
   1 October 2026 in [`direction-2026-10-01.md`](./direction-2026-10-01.md)).
2. **Money For Something**, the topical comedy show from the same story folder
   (`money-for-something*.md`).

**Status:**
- **Documentary:** EXPLORING — Kai, 11 September 2026: *"visual treatment is not locked"*; story first.
  What is settled is the material (real archive footage, heavily, Jack 1 Oct) and the verb cards. A silent
  rough-cut preview exists (2026-09-30, worktree `mmt-rough-cut`), not yet noted by Kai.
- **Money For Something:** LOCKED per episode by Jack's picks — the back-room club set (plate B,
  10 Oct; plate P1, 14 Oct) and, from 25 Oct, the balaclava host **D1** on that set (plate H1).
- **The song's video:** EMPTY.

## In one paragraph

**Documentary:** an archive documentary — genuine historical footage, mostly British Crown films of
1945–52 and public-domain stills, mixed with clearly distinguishable illustration or generated imagery
where nothing real exists (Kai, 11 Sept). Each dated beat carries **one verb on a card** — `1923 · SHAKE`,
`1948 · PLANT` — so the ending is a receipt the viewer has already read with the sound off. The war
builds in flashes, then silence on *"how did we pay for it"*, then money printing building (Jack, 1 Oct).
**Money For Something:** a 2003 standard-definition recording of a back-room comedy club: brick, a bare
tree hung with pound notes, empty oxblood armchairs, a television on red beer crates, a pint; warm amber
spotlight from high left against the television's cold blue. The host is BadCode in person: a hand-knitted
cream balaclava with the logo as its face, no skin anywhere.

## Preamble(s)

**Documentary:** none written. The test the storyboard sets before any aesthetic system: a text-first
assembly (scene cards, verb cards, scratch voice) must hold a listener *"without attractive images"*
([`storyboard.md`](./storyboard.md) §7).

**Money For Something, the host (D1)** — Jack's pick, verbatim opening of the D1 prompt
([`characters/host-v2-balaclava.md`](./characters/host-v2-balaclava.md) round 2):

```
Photograph a presenter on a tiny local-access television set, taken on a Ricoh GR compact from slightly above, framed a little off-centre and not quite level.
```

The host on the club set is made by **reference, not by description**: attach `mfs-balaclava-host-ref`
(Jack's D1 still) then `mfs-club-plate-P1`; the man is not described
(`scripts/money-for-something/oct26/prompts/plate-H1.txt`). Settings: Nano Banana 2 · 16:9 · x2 · Flow project
`cb27208c-4b16-426d-9144-c394f2735c15` ("mmt jack").

## Rules for this story

Documentary:
- **Real people are archive-only, never generated** (Keynes the only historical exception in older
  treatments; the storyboard now says *do not generate fake archival testimony*). No picture of Baroness
  Mone: newspaper headline screenshots instead (Kai, 2026-09-29).
- **Footage is cleared before it ships** — [`footage.md`](./footage.md) is the ledger; Crown films of
  1945–52 are usable, **picture only** (their audio is not free) (Kai, 2026-09-29); no spend ("£170 for
  one clip is too much"). BBC clips: text cards, with a card-only version kept ready for every clip scene.
  Kai's "ask for forgiveness" remark (1 Oct) is not yet a ruling.
- **Verb cards** on every dated beat; May's clip or card runs long enough for *shake* to be heard or read.
- **Germany 1923** is public-domain stills only (Bain/LoC, Rol and Meurisse/BnF).
- **Illustration and generated imagery must be clearly distinguishable** from archive.
- **Generated stills are colour only, never black-and-white** (Jack, 2026-10-01, on seven Dunkirk style
  tests: *"they look all the same"* — [`magic-money-tree-jack.md`](./magic-money-tree-jack.md)). Real
  archive stays as it is.
- 🔴 **OPEN — is the documentary register this story's?** The 2026-08-26 cinematography sweep
  proposed the documentary register (visible imperfection: grain, unstable framing, uneven exposure,
  a camera reacting a beat late) "for the money film" (`docs/cinematography/registers.md` §3). Never
  ruled by Kai or Jack. If adopted, ruling R6 holds: borrowing vérité codes for *invented* footage of
  a *real* subject manufactures "this really happened" — money creation is a true subject, so flag
  every use. (Moved from the shared cinematography docs, 2026-10-29.)
- **Style tests are reviewed in Flow, not saved to a Desktop folder**; their prompts are recorded in
  [`magic-money-tree-jack.md`](./magic-money-tree-jack.md) (Jack, 2026-10-01).

Money For Something:
- **One locked frame per monologue**; the camera never moves so the screen can be replaced with a mask.
- **The television is a plain blue "no signal" screen** in the plate; pictures and cards go in afterwards.
- **"A scripted television comedy… an actor plays a made-up character"**, never "television studio" or
  "newsreader" (refused as reputational risk).
- **Host v2 shows no skin**; the logo is the face: a thin black ring with a small red triangle with rounded
  corners high inside it, over one eye ([`docs/brand/`](../../brand/README.md)). Place it by landmark, not
  left/right.
- **Anti-slop (round 2, 25 Oct):** describe the capture, not the beauty; one humble camera and stock
  (Kodak Gold 200, Ektachrome or Ilford HP5; not Portra 400 or CineStill); no quality words; one named
  light; off-centre, not level, something in the foreground, the host mid-action; wear and mess in the set;
  exact materials; no undefined text. Every prompt ends `Thanks.`
- **Cards, "third style"** (`build-topical-cards3.py`): Inter Tight, left aligned, sentence case, a small
  tracked label with a coloured dot, one big number in the accent colour, the source in small grey type on
  a hairline, photo darkened by a gradient from the left; lines slide up and fade in.
- **The money on the tree is English pound sterling, never dollars** — say so in every still and clip
  prompt (Jack, 2026-10-04).
- **Never write audience, laughter, applause, comedy or newsreader in a talking-clip prompt** (each one
  summoned crowd noise or was refused); name the sound as the speaker's voice plus an empty room's hum
  (Jack ruled out studio laughter, 4 Oct).
- Video: Omni 1.1 Flash, **Frames**, 720p, 8 s (Ingredients re-stages the room). Host v2 talks off screen
  (TTS), so a few stock movement clips from plate H1 are reused.

## Anchors

- Documentary footage on disk: `/mnt/d/badcode-videos/magic-money-tree/clips/` (masters in `clips/_masters/`,
  picture-only conforms per scene) — [`footage.md`](./footage.md) §12. Silent rough-cut preview:
  `D:\badcode-videos\magic-money-tree\previews\rough-cut-preview.mp4` (2026-09-30).
- Money For Something room references: [`characters/roundtable-clear-stage-reference-v2.jpg`](./characters/roundtable-clear-stage-reference-v2.jpg)
  (Flow `mfsroomrefv2.jpg`, Jack's pick 4 Oct; use this, not v1), [`roundtable-set-reference.jpg`](./characters/roundtable-set-reference.jpg).
- Plates (Jack's disk, `...\animation\money for something\`): plate B (`stills\plate-B.jpg`, Jack's pick
  10 Oct), plate P1 (`2026\stills\plate-P1-a.jpg`), plate H1 (`2026-10-26\stills\plate-H1-a.jpg`).
- Host v2 D1 still: in Flow project `d5559719-088b-4f35-ab61-31b0feb4b502` ("Oct 25 - 09:56"), uploaded to
  `cb27208c` as `mfs-balaclava-host-ref`.

## Cast

Money For Something (Flow project `cb27208c`):
- **The Host (v1, Oct)** — Flow Character `65e090db-11a1-4dce-bc6c-c182f4213f4a`, portrait
  [`characters/host-dishevelled-comic.jpg`](./characters/host-dishevelled-comic.jpg) (also
  [`host-portrait-v2.jpg`](./characters/host-portrait-v2.jpg), [`host-body.jpg`](./characters/host-body.jpg)).
- **The Host (v2, from 25 Oct)** — the balaclava, D1; no Flow Character (reference only).
- **The quiz panel** — The British Soldier `5895147c-5392-4ac0-ace9-34742b8ec24e`, The German Soldier
  `5e09ee82-7f79-4c2e-9aee-b5ebcca1d2d0`, The Politician `6baccdfb-7353-4559-829d-8fe253eb7b1f`; portraits
  [`characters/british-soldier-portrait.jpg`](./characters/british-soldier-portrait.jpg),
  [`german-soldier-portrait.jpg`](./characters/german-soldier-portrait.jpg),
  [`politician-portrait.jpg`](./characters/politician-portrait.jpg) (v2 and body plates beside them),
  generated from the 9c room reference ([`money-for-something.md`](./money-for-something.md) §"The cast and
  their voices in Flow").
- 2026 episode extras: Podcast Host `8b194ea9`, Water Boss `c74386ce`, HS2 Reporter `da033493`.

Documentary: **the soldier through the ages** (1 Oct direction) — not designed, not cast. Unknown whether
he is a ghost, and what he is called.

## Places

- Documentary: Dunkirk, Germany 1923, a 1940s war economy, 1948 NHS wards and council homes, the Bank of
  England, a 2017 Question Time, Covid — all from archive where possible.
- Money For Something: the back-room comedy club (brick, the tree with pound notes, armchairs, the
  television on red beer crates).

## Never

- A generated likeness of a living person, or fake archival testimony.
- Archive audio from the Crown films.
- A picture of Baroness Mone.
- An undefined screen or sign (it fills with invented writing).
- The words *news, newsreader, television studio* in a Flow prompt for the show.

## Per part

- **The soldier interviews** (recut): the narrator interviews him at each age; *"the war interview is
  played real"* (Kai, 1 Oct); the modern half is slapstick, the soldier with his head in his hands; an
  empty chair for 1923. Not designed yet.

## History

- **The fable treatments** (Keynes talking to a tree on a St James's Park bench, the grove of central-bank
  mulberries, the winter ending) — archived in [`archive/2026-09-11-superseded/`](./archive/2026-09-11-superseded/README.md).
- **The legacy comic** at `/comics/magic-money-tree` and its panel prompts in [`storyboard/`](./storyboard/README.md)
  — not this documentary's look.
- **The 15-minute cut** (28 Sept) → three minutes (1 Oct).
- **Money For Something, the 1975 game-show look** (2–4 Oct 2026, superseded by the back-room club set,
  plate B, 10 Oct): a realistic 1975 British TV studio on tube-camera videotape, 4:3, Nano Banana 2, a
  money tree on stage; host v1 the dishevelled comic (Flow Character `65e090db`, Jack's pick 2 Oct from five
  looks); room-and-cast reference round 9's 9c (`mfsclearstageref.jpg`, Jack 3 Oct: *"this one is great"*).
  Prompts in [`money-for-something.md`](./money-for-something.md).
- **Money For Something host v2 round 1** (25 Oct, A/B/C): too perfectly arranged; round 2's eight designs
  gave D1.
