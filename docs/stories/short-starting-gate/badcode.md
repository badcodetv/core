# The Starting Gate

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, aim ~17 s): a horse race where new money is the starting gun. SHARES and HOUSES fly out of the
stalls; WAGES doesn't leave its stall for eleven years and nine months. BadCode, in the mask, commentates. The point: when
new money is made, it lifts what people own first and what people earn last. The way out: the next race has one gate, and
everybody goes at once. State: rough cut 5 (35.3 s) on https://claude.ai/artifact/TXEaJCgufUovmCNUKgf5oX, in Premiere as `short-starting-gate-1-starting-gate-r5` (in sync) and on Drive (agreed cut); outro: the BadCode logo painted on WAGES' flank as he walks (`scripts/shorts/gate_flank_logo.py`); clips https://claude.ai/artifact/9ARwdm6AFEXxd9iwjowGsd; stills https://claude.ai/artifact/F8iA9UCLU774eYU5VeyokZ.

## Look
Jack, 2026-11-22: "use unsplash". Real-looking photographs of an English racecourse on a grey, wet day: starting stalls,
the turf, the rail, the stands, a commentary box. Each still's layout comes from an Unsplash photo given to Flow as the
reference; the prompt only says what changes. Status: EXPLORING (no references picked yet).
Flow project: `c1e0c728-9d37-442a-a858-915e0be94176` ("Nov 22 - 11:36"). Stills Nano Banana 2.1, 9:16. BadCode stills attach `docs/brand/balaclava/mask-reference.jpg` with the brand's one line.

## Sound
Music: not decided — run story-style. Voice: LOCKED, comm-b (Jack, 2026-11-22): "A man in his early sixties from Malton in North Yorkshire…", `voice_ih3z7r9gfkkb`, per-line styles (page https://claude.ai/artifact/CfsbNwaWAwxA5We9Ukxikz; designs in `voices-designed.json`, lines and per-line styles in `scenes/starting-gate/cleanroom/voice-r1.json`). Every spoken line is an AI Studio voice (cast fresh with voice-casting; English, with a
named region, never just "British"). Any Suno track is music and sound only.

## Cast
- **BadCode, the commentator:** in the BadCode balaclava (below), in the commentary box with binoculars. Heard as the
  race commentary; seen in the box. His clothes are Not decided (found on the mood board).
- **The runners (LOCKED, Jack 2026-11-22: "consistent across all stills"; anchor still `stills/r1/GATE-a.jpg`):**
  - SHARES: dark bay horse; jockey in maroon silks with mustard-yellow sleeves, pink-and-purple cap.
  - HOUSES: grey (dappled white) horse; jockey in black silks with orange sides, black cap.
  - WAGES: chestnut horse with a white blaze; jockey in maroon, green and blue panelled silks, green-and-red cap.
  - The words SHARES / HOUSES / WAGES in plain black capitals on white cloth; words in the picture only there and on the fact line.
- **The setting (LOCKED, same anchor):** galvanised grey steel starting stalls, white running rails, a grey grandstand,
  wet green turf, flat overcast light, drizzle. Every still attaches GATE-a as the reference for these.
- **BadCode's mask is tweed** (Jack, 2026-11-22: "make his mask tweed"): brown tweed cloth, with the brand's white ring
  and red triangle; no skin, gloves.

## Story-only rules
- The script's lines are Claude's draft (`by: claude`); Jack and Kai write the jokes and rule the way out.
- **Claims:** say "new money lifts what people own first, and what they earn last". Never "the Bank hands money to the
  rich", never "guaranteed". The fact on screen is exactly: UK real regular pay passed its 2008 peak in December 2019, by
  £1 a week, on the ONS's CPIH measure (sources in [script.md](./script.md)). Re-check it against the ONS before release.
- The way out (one gate for everyone) is Claude's: no BadCode government policy on record. Say so until one exists.
- No real person, jockey, racecourse name, bookmaker or broadcaster: invented or unnamed only.
- Run `scripts/variations/fresh.py --story short-starting-gate` over every new prompt and line, and say the result.
- **Cut the final section: end on the horses still in the mud** (meeting 2026-11-24, `docs/misc/2026-11-24-meeting.md`; Gemini's notes, to be done by Jack).

## Library pieces in use
- **Real photo as the look** (Jack): an Unsplash photo is each still's layout, given to Flow as the reference; the prompt
  says only what changes. Never an AI figure pasted into a real photo.
- **Clean room** (Jack: "no pollution"): prompts written by a sealed writer from one brief in `scenes/starting-gate/cleanroom/`.
- **The BadCode balaclava:** anyone in it is BadCode in person. Navy knit balaclava, a large white ring stitched round the
  whole face, the red triangle over the wearer's LEFT eye (on the right of the picture), no skin showing anywhere, gloves.
  No mouth, so his lines need no lip-sync.

## Where the detail is
- [README.md](./README.md), [script.md](./script.md), [look.md](./look.md), [sound.md](./sound.md),
  rulings [scenes/starting-gate/picks.md](./scenes/starting-gate/picks.md)
