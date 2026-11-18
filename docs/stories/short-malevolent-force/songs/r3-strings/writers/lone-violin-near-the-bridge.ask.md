You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-18, picking which library pieces the "more horror" pass takes in (his selected option, verbatim):
"Sound: suspense strings — Stabbing strings and rising dread, timed to hit as the hand snatches."

Then, asked whether to start the strings round: "go thanks"

## What happened in earlier rounds (facts)

- The track is the whole audio of a ~17-second vertical short (BadCode Shorts, "The Malevolent Force"): buying bread at a British corner shop at night, shot like a haunting. No voice anywhere (Jack, 2026-11-16: "No voice, one end card"). Shorts Suno tracks are music and sounds only, never speech (Jack, 2026-11-15).
- The current cut's music is an ambient track (picked 2026-11-16); this round replaces it with suspense strings (Jack's pick above). The end card and logo after the picture play in silence.
- The picture now, in order (rough cut 3, 2026-11-18): 0-1.6 s the only lit corner shop at 3am; 1.6-3.5 s the glass door swings open by itself, then for half a second a dark figure behind the frame; 3.5-6.5 s down the aisle a black figure peeks from the back door and scuttles back, then drops off the top of the shelving; 6.5-10.4 s a burnt hand snatches the 50p price card off a loaf, then in the dark it's £1, in the light £5; 10.4-12 s a security mirror rocks; 12-13.6 s the burnt hand whips up off the freezer lid; 13.6-16.6 s lightning, and the prices are £50 and £12.
- The scares (each a fraction of a second) are at about 3.0, 4.8, 6.0, 7.8, 13.2 and 14.0 s. Exact hits get placed in the edit; the track should carry rising dread with sudden stabs and silences that can be cut to them.

## This story (stay inside its look and sound; another part's look does not apply)

# The Malevolent Force


## What it is
A BadCode horror short (9:16, 20.8 s): one trip to the corner shop for bread, shot like a haunting, the price climbing
50p → £1 → £5 → £50. The point: inflation is not weather; someone decides who gets the new money first (whoever stands
nearest the printer), and you meet it last, at the till. The force is never seen and never one person. No voice; an
end card, then the logo. State: rough cut 3 built (not in Premiere yet; rough cut 2 is in Premiere as
`short-malevolent-force-1-malevolent-force-r2` and on Drive). Owed: export from Premiere, delivery QC, gatekeeper.

**Next: more horror, the force more visible** (Jack and Kai, 17 Nov morning call,
[notes](../../misc/2026-11-17-morning-meeting.md)): a **ghostly hand** rapidly snatches the price tags, or waves over the
money, and the price changes. Kai: it makes it scarier and funnier. In progress (2026-11-18): **the hand is picked**: burnt, soot-black, cracked like old tarmac with a dull ember glow in the
cracks, long hooked fingers, nails like split slate, a thread of smoke; only hand and wrist, coming down from the dark
above, lit by the shop's teal. Picked: shot 4 `HS4-a`, shot 6 `HS6-b`.
**Jumpscare figure (Jack, 2026-11-18):** a matte black, thin figure with a smooth, round, featureless head, almost a
silhouette (as in `JS3-top-b`, the reference for every new shot of it; never grey or lit like a face). On screen
for a few frames with a strings stab. Picked: crouched on top of the shelving `JS3-top-b`, half behind the door `JS2-door-b`,
only in the mirror `JS5-mirror-b`; the aisle peek (out of the back door, scuttling backwards, never turning) is in round 7. Unclear: whether Jack keeps the figure as a rule change (the force was "never a person"). The finish is the **subtle VHS**
(`scripts/shorts/vhs_finish.sh`). All six horror pieces are animated and picked (round 8, `scenes/malevolent-force/picks.md`). Rough cut 3 (`cut/r3/`, 21.8 s) has
them cut in, with the subtle VHS finish; its timeline page is the one linked below.

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

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 17
}
```

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**lone-violin-near-the-bridge** — A single solo violin, alone in a small dead room, is the whole performer: thin, glassy tremolo played near the bridge, a two-note semitone figure that keeps creeping up a step, and sudden scratching high shrieks with heavy bow pressure. No section, no bass, no reverb wash: it should feel like one person playing in the shop after closing, close-miked and dry, so the silences between notes are truly empty. Describe the sound rather than relying on Italian terms (glassy, whispering, scraping, then a scream of the bow). Keep it under 17 seconds of gesture, ending on a high note that just stops.

Other writers are doing the other experiments (slasher-stab-section, quartet-cluster-ostinato, basses-from-below, aleatoric-swarm-strings, worn-tape-string-cue). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r3-strings/writers/lone-violin-near-the-bridge.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r3-strings/writers/lone-violin-near-the-bridge.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "lone-violin-near-the-bridge". Reply with just the two paths.