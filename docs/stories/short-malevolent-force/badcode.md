# The Malevolent Force

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode horror short (9:16, 20.8 s): one trip to the corner shop for bread, shot like a haunting, the price climbing
50p → £1 → £5 → £50. The point: inflation is not weather; someone decides who gets the new money first (whoever stands
nearest the printer), and you meet it last, at the till. The force is never seen and never one person. No voice; an
end card, then the logo. State: rough cut 2 built in Premiere (`short-malevolent-force-1-malevolent-force-r2`), saved,
agreed cut on Drive. Owed: export from Premiere, delivery QC, gatekeeper.

**Next: more horror, the force more visible** (Jack and Kai, 17 Nov morning call,
[notes](../../misc/2026-11-17-morning-meeting.md)): a **ghostly hand** rapidly snatches the price tags, or waves over the
money, and the price changes. Kai: it makes it scarier and funnier. In progress (2026-11-18): **the hand is picked**: burnt, soot-black, cracked like old tarmac with a dull ember glow in the
cracks, long hooked fingers, nails like split slate, a thread of smoke; only hand and wrist, coming down from the dark
above, lit by the shop's teal. Picked: shot 4 `HS4-a`, shot 6 `HS6-b`.
**Jumpscare figure (Jack, 2026-11-18):** a matte black, thin figure with a smooth, round, featureless head, almost a
silhouette (as in `JS3-top-b`, the reference for every new shot of it; never grey or lit like a face). On screen
for a few frames with a strings stab. Picked: crouched on top of the shelving `JS3-top-b`, half behind the door `JS2-door-b`,
only in the mirror `JS5-mirror-b`; the aisle peek (out of the back door, scuttling backwards, never turning) is in round 7. Unclear: whether Jack keeps the figure as a rule change (the force was "never a person"). The finish is the **subtle VHS**
(`scripts/shorts/vhs_finish.sh`). All six horror pieces are animated and picked (round 8, `scenes/malevolent-force/picks.md`). Rough cut 2 stands until
rough cut 3 is built with them.

## Look
- Status: look.md still says EXPLORING with no ruling written; in practice every shot is picked from Jack's reference.
- Jack's reference photo `scenes/malevolent-force/reference/jack-r2-shop-doorway.png`: a corner-shop doorway at night,
  cheap colour film, fluorescent teal; soft, washed-out, grainy. The stills came out darker and sharper; soften in the grade.
- Nobody in any frame. The force shows only as light, blank notes on the floor and the prices it leaves.
- Shots: 1 FO2-c street (`mf-01-w2`) · 2 PR2-e door opens (`mf-02`) · 3 PR2-c aisle (`mf-03-w2`) · 4 PR2-b 50p loaf,
  brownout flips the label to £1 then £5 (`mf-04-b`) · 5 FO2-d convex mirror, blank notes (`mf-05-b`) · 6 FL4-b freezer lid by
  the door glass, lightning flash, prices swap (`mf-06-f4b-swap`) · end card · lightning then logo.
- Stills Nano Banana 2; clips Omni 1.2 Flash, Frames, 9:16, 8 s, locked camera. Flow project `0153219b-e10c-46ac-b2a7-5b50200e19fe`.

## Sound
- Status: LOCKED. Music = **vibes1**, https://suno.com/song/f7b238d2-fbb9-4ee1-9b9d-5d9600291c27 (prompt
  `inharmonic-vibraphone` in `songs/r2-track/round.json`): Silent Hill-style ambient, instrumental only. Runs 0-15 s,
  faded over its last second; the card plays in silence.
- No voice at all. A thunder hit under the logo flash is optional, not decided.

## Story-only rules
- The evil is a force, never one person: never blame or show a person. Since 17 Nov it may show **a ghostly hand** (only a
  hand: no face, no body, no one you could name).
- Price changes happen in the edit: only the price cards change, pasted onto their exact region from the brightest flash
  frame; the setting stays identical before and after.
- End card (Jack): "Based on true events. Coming to a shop near you."
- The chocolate bar is the Freddo gag: "10p" crossed out, "£12" beside it.
- Blur shot 1's "BREAD £50" window card (it spoils the end) and shot 2's legible "WALKERS" spinner.
- The logo ending: 2.6 s black, two lightning flashes, the logo file on #050607. Logo is the file, never Flow.
- Suno tracks for this short are instrumental only. Run the Flow runner outside the Bash sandbox (inside, it loses every download).

## Flow project
- `0153219b-e10c-46ac-b2a7-5b50200e19fe` — scenes/malevolent-force

Open the part's project before its first Flow call; never use it for another story.

## Library pieces in use
Picked by Jack, 2026-11-18, for the "more horror" pass (from: clean room, real photo, VHS camcorder, hauntology,
suspense strings). Copied and adapted here; the library entries are not live rules.
- **Real photo (Unsplash):** the ghostly hand starts from a real photo of a hand, found with
  `python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>"`, picked on a picks page, then given to Flow as the
  reference so the hand looks real, not AI. The prompt only says what the hand does.
- **VHS camcorder look, as a finish:** the cut is treated like caught-on-tape footage: soft and horizontally smeared,
  colour bleed (reds bloom, shadows go muddy green), chroma noise, a tracking-noise band and brief dropouts at the bottom,
  a burned-in REC / date stamp. Kept 9:16. Applied in the edit (ffmpeg), the same chain on every shot, never asked of
  Flow: models make "VHS" bright neon synthwave and garble the stamp. Dull and muddy, not purple and cyan.
- **Suspense strings:** a strings-only suspense cue: a short rising two-to-four-note ostinato, tremolo violins, a low
  double-bass pedal, dissonant chords left unresolved, near silence broken by shrieking violin stabs, timed to hit as
  the hand snatches. Instrumental, no drums, no synth, no choir. Suno drifts to "epic trailer" braams and resolves the
  dissonance: exclude epic, hybrid, braam, trailer, drums. Stabs on picture are placed in the edit. Whether it replaces
  vibes1 or sits under it: Jack picks.

## Where the detail is
- [README.md](./README.md) (Premiere track list), [scenes/malevolent-force/brief.md](./scenes/malevolent-force/brief.md) (beats), [look.md](./look.md), [sound.md](./sound.md)
- Every ruling: [scenes/malevolent-force/picks.md](./scenes/malevolent-force/picks.md); music takes: [songs/r2-track/takes.md](./songs/r2-track/takes.md)
- Timeline https://claude.ai/artifact/2xC772Jtzb5LNK5qWYYFFX · mood board https://claude.ai/artifact/K5CptJtk7JHuW8KCHeHvrY · picks https://claude.ai/artifact/QBTVPj1nBbqbyfbPwF11ju
