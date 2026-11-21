# The Forecast

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, aim ~20 s). A TV weather presenter forecasts the economy as weather ("prices rising across the
south, wages staying cold in the north"); the camera pulls back to a man in a suit just off-set blowing the clouds
across the map with a desk fan. The way out: every cloud gets a name tag (who decided). From the BadCode government's
Chancellor policy `the-ledger`. State: script draft 1 ([script.md](./script.md)), nothing generated.

## Look
Status: EXPLORING (stills round 1). Jack, 2026-11-21: "Real TV studio": real-looking, built from Unsplash layouts:
`Krkr1WhLV-4` (news studio floor, the weather set), `Av7fp7AqJr0` (studio with light stands: off-set), `fnjxpnaivnE`
(past a camera operator's shoulder: the pull-back). Bright even light on set, darker and messier off-set. An invented
channel: no real broadcaster's look. Only words: RENT, PRICES, WAGES on the clouds; the name tags THE TREASURY,
BANK RATE, LANDLORDS' LOBBY, ENERGY FIRMS.
- Cast (portraits first): the presenter (BadCode in the navy balaclava, navy suit, pale blue shirt buttoned to the mask,
  plain tie, gloves, a clicker); the man with the fan (invented, ~55, slicked grey hair, navy pinstripe, red-and-gold tie).
Flow project: `44f7c34b-9f55-48c4-a688-3f1207971ee9` (shown in Flow as "Nov 21 - 16:51"). Stills Nano Banana 2.1, 9:16.

## Sound
Voice: the presenter is `presenter-b` (Jack's pick, 2026-11-21): a dry Yorkshire weatherman from Leeds in his fifties, AI Studio
voice `voice_ampe3xv1sq8t` (designs in `voices/casting/designed-voices.json`). Music: not decided. Any Suno track is music and sound only; every spoken line is an AI Studio voice. Voices must sound English:
design them with an English region, never just "British".

## Story-only rules
- **The presenter's mask is a sunshine-yellow chunky knit with a yellow pompom** (2026-11-21): Flow refused every clip of the
  navy-masked presenter on the lit news set (6 tries, any wording); an empty set and the masked man off-set both animated,
  so the guess is a masked man on a news set reads as a hostage or extremist video. The yellow bobble mask animated at
  once. Still refused in yellow: the pull-back past the camera crew (F02); it is a pull-back on the still instead.
  Keep "broadcast" and "footage" out of motion prompts.
- The presenter is BadCode in the balaclava (white ring, red triangle over his left eye, gloves, no skin, collar up to
  the mask); masked, so no lip-sync. Keep him facing the camera.
- The man with the fan is an invented man in a suit: no real politician's face or name. The name tags say roles and
  decisions ("THE TREASURY", "BANK RATE"), never a real person's name.
- No real broadcaster's look, logo, graphics or theme: an invented channel, no lettering beyond what the script names.
- Jack and Kai write the jokes; Claude's drafts are marked as Claude's.
- Run `scripts/variations/fresh.py --story short-the-forecast` over every new prompt and line, and say the result.

## Library pieces in use
- **Real photo as the look** (Jack, "Real TV studio"): an Unsplash photo is each still's layout; never an AI figure pasted into a real photo.
- **Clean room:** prompts written by a sealed writer from one brief (`scenes/the-forecast/cleanroom/`).
- **The BadCode balaclava:** the presenter. Attach `docs/brand/balaclava/mask-reference.jpg` with the line "The balaclava
  exactly as in the attached image: no holes, no skin, gloves." Collar up to the mask (no neck); check which EYE the
  triangle is over on a turned head.

## Where the detail is
- [README.md](./README.md), [script.md](./script.md), rulings [scenes/the-forecast/picks.md](./scenes/the-forecast/picks.md)
