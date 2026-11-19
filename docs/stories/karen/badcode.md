# Karen Will Lead the Revolution

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A New York middle manager fired by an AI (Sean AI) weaponises complaining: "I want to speak to your manager"
climbs from a Midtown phone box to the President, at the moment the AI fires him too. Point: act, don't lie
there. Two videos: a **narrated story film** (ends on Sean AI's card, the sacked President calling Karen back,
"To be continued"; no stated moral) and a **music video** for the song "All Day to Complain" (about 4:10).

## Parts
- Story film — `scenes/story/` — on its timeline page at **cut r3** (2026-11-18): Kai's notes to 2:08 attempted in one cut (`scripts/karen/story-cut-r3.py`; office → calling everyone re-cut, Viral onward still Jack's `Karen v4` render). r3b (19 Nov): the same cut with no clip sound (Kai's rule below), on the same page; Kai paused noting 19 Nov (26 notes on the page, dumped to `scenes/story/feedback/timeline-r3-2026-11-19/`); pick up from there, nothing answered yet. Premiere still holds only `Karen v4`. Names for the first three calls (Kai): Martha (receptionist), Clive (local council), Harriet (borough representative).
- Music video — `scenes/music-video/` — final cut frozen 2026-11-09 (Kai's hand edit on `karen-music-r4`).
- **The two have different looks and different Karens. Don't carry one part's look or voice into the other.**

## Look
Status: LOCKED. Karen's imagery is Jack's, made by hand in Flow; generate only when Kai or Jack asks.
- **Super-8 STYLE LOCK** (main register): a capture emulation, not a period — grain, gate-weave, halation,
  soft edges, punchy warm colour, over an unmistakably **present-day New York**. Vibrancy belongs to the
  stock, restraint to the scene. Paste the STYLE LOCK block verbatim from [look.md](./look.md) §Preamble;
  New York walk plates add the CANDID CLAUSE after it.
- **Illustrated register** (title sequences, and the music video's choruses): flat mid-century poster
  illustration in matte gouache, navy/charcoal against amber, faces undrawn; mid-century style,
  present-day world. Block verbatim in look.md. Don't cast `@Karen` here: likeness is hair mass,
  silhouette, wardrobe.
- **Story film exceptions:** Act 2 god's-eye aerials are photoreal, no grain; the Act 3 phone-screen plate
  is the one phone-camera frame; the ending is human-scale, one warm lamp, cold city glow, faces withheld.
- **Music video:** choruses = cartoon (illustrated register), verses = photographic footage; picture
  changes on the beat.
- Cast: Flow Characters `Karen` (`f26355cb…`), `Susan` (`05d2f68b…`), `Aarron` (`3b541072…`) in Flow project
  `da8feea7`; references in `characters/img/`. Sean AI is a screen, never a face (gold for the takeover).
  The President is "a man in a dark suit", fictional, from behind. Tarquin = Flow Character `@Tarquin`.
- Engines: stills Nano Banana (Pro for the acts, 2 for the ending), 16:9; clips Omni 1.2 Flash, 8 s, camera locked.

## Sound
- **Song "All Day to Complain":** 86 BPM boom bap built from telephone hold-muzak, arranged like a 60s
  spy-thriller score (unresolved minor ninth, chromatic upright bass, muted trumpet, brushed drums,
  touch-tone beeps); a mature New York alto *performing* the whine, band-passed telephone clerks, a small
  sweet choir. Base = Take C (round 16, Kai-endorsed); EXPLORING, no keeper since round 20; a new round
  needs a v6 sheet. Boxes verbatim in [sound.md](./sound.md).
- **Narrator (story film):** AI Studio `Algenib`, model `gemini-3.1-flash-tts-preview`, accent Neutral,
  Style/Pace empty; a dry, wry American storyteller from the future, anger banked down, never deep or
  booming. Profile: [narration/profiles/narrator-algenib.md](./narration/profiles/narrator-algenib.md). LOCKED.
- **No clip sound (Kai, 2026-11-19):** the Flow clips' own audio is never heard in the story film. Only the narration, the
  music and sound effects placed on the timeline on purpose. (Jack's v4 Premiere cut had the clips' sound on A1; r3b drops it.)
- **Ending voices:** the President `Charon`, Tarquin `Zubenelgenubi`. LOCKED in the cut.
- **Karen's voice:** story film = natural, grounded (Flow base voice `Gacrux`); music video = the song's performed whine.
- **Score:** EMPTY — six cues in [narration/score.md](./narration/score.md); stem-split an accepted song take first.

## Story-only rules
- No legible text anywhere in a generated frame; Sean AI's UI and "To be continued" go in post.
- Present-day or it's a reject: name the no-era-shift twice.
- Film set, not news: never *news, reporter, broadcast, live, television, President* in a prompt.
- Cast, never describe a face; Flow's personality field stays empty on every Character.
- The phone box is a fixed point (the accepted §2h kiosk still); in Act 2 sameness is the point.
- Two figures in relative motion merge: shoot two-handers as singles; crowds are stills.
- Satire played straight: the joke is in the words, never the music; no comedic/novelty in Style; no franchise or artist names in any box; the tempo never changes.
- Write `Ay-Eye Sean` in TTS transcripts.

## Flow project
None recorded yet. Create one with `flow_create_project` before the first Flow call, and write its id here.

## Library pieces in use
- none yet

## Where the detail is
- [look.md](./look.md) (blocks verbatim, anchors, cast) · [sound.md](./sound.md) (song boxes, voices) · [prompts.md](./prompts.md) (Flow ledger)
- Story: [story.md](./story.md) (storyboard; the 15 Oct and 19 Oct rulings at the top win) · [shot-list.md](./shot-list.md) · [narration/script-v2-brief.md](./narration/script-v2-brief.md)
- Story film timeline page: https://claude.ai/artifact/3Mw9ucc4wRiDESP2nhgAdC
- Music video: [song-map.md](./scenes/music-video/song-map.md), [catalogue.md](./scenes/music-video/catalogue.md), [new-cartoon-shots.md](./scenes/music-video/new-cartoon-shots.md); timeline page https://claude.ai/artifact/BxoWfvnpr7AFeo3T4Hm7DE

Unclear: which song take the music video uses — sound.md says no keeper since round 20 at 86 BPM, the music video's song map measures 89.1 BPM.
