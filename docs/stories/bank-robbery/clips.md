# The Bank Robbery — scene clips, first pass (6 October 2026)

**Asked for by Jack, 6 October 2026:** "they are great... then do the videos." One clip from each
second-pass still in [`stills.md`](./stills.md).

**A picture pass. Nobody speaks.** Every prompt ends "No dialogue, no music", which is the
standing rule for Flow video. 🔴 **This is a call I made, and it is Jack's to overturn:** the
twelve Characters now have voices, but the storyboard says every line is a placeholder and no
script exists. Talking shots also want their own stills (one speaker, closer to eye level), so
these fifteen clips are not wasted either way.

- **Settings:** Omni 1.1 Flash · Frames (the still is the start frame) · 16:9 · 720p · 8 s · one
  take each. The standing default is two takes; one was used here to halve the credits (about 12
  a clip, 180 for the set) on a first pass. Not ruled.
- **Flow project:** `63d22c4b` ("Oct 06 - 14:23").
- **Files:** `Desktop\Youtube Vids\animation\bank robbery\vids\<scene>.mp4`. Not committed.
- **Runner:** `scripts/bank-robbery/br-videos.mts`, reading `scripts/bank-robbery/br-videos.json`
  (the prompts below, word for word).

## How the prompts are built

From the repo ([`omni-flash.md`](../../google-flow/omni-flash.md),
[`hybrid-method.md`](../../video-fx/hybrid-method.md), `shot-craft`):

- **Motion only.** The still already carries the people, the place and the light. Describing them
  again makes the model redraw instead of animate. People are "the man on the left", never a
  description.
- **The camera is locked off** in thirteen of fifteen. A moving camera is what makes the model
  rebuild the world. Any camera move gets added in the edit. The two exceptions are scene 7
  (hand-held, the only hand-held scene in the storyboard) and scene 9 (the camera is fixed to the
  moving pallet).
- **Two beats in eight seconds:** the action the shot is for, in its own sentence, then one small
  later one (a blink, a look, a breath). One action stretched over eight seconds comes back as
  drift.
- **Small movements.** Over-animation is the tell.
- **Sound is named, object by object,** from things in the frame.
- **Where the still shows open mouths** (scenes 4, 7, 12a), the prompt gives them something to do
  that is not words: stop at a buzzer, laugh, or be drowned by an alarm.

From the web (6 October 2026, search summaries only):

- Google's own five-part frame for this model: goal, the role of each input, scene, motion,
  constraints. It makes sound in the same pass, so the prompt has to say what the sound is.
  [Pillitteri](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide),
  [Google](https://ai.google.dev/gemini-api/docs/omni)
- What makes an image-to-video clip read as real: geometry that stays put, one light, a background
  that does not drift, one motion intent per prompt, and quiet words ("slowly") over loud ones.
  [Pixelbin](https://www.pixelbin.io/blog/how-to-make-realistic-ai-videos),
  [Promptessor](https://promptessor.com/blog/image-to-video-prompts-how-to-animate-photos-products-characters-and-art-in-2026)
- Nothing here disagrees with the repo.

**Frames, not Ingredients:** each still is an exact framing that took work to get, and Frames
keeps frame 0 as given. Ingredients holds a face better but re-stages the shot. The Characters are
not attached to these clips.

## The prompts

### s01-breakfast

```text
The camera is locked off and does not move. The man on the left chews and jabs his fork toward the man on the right, who leans in and jabs his own fork back, neither of them speaking. The woman standing above them looks from one plate to the next, her lips moving slightly as she counts, then lifts one more plate onto the stack on her arm. The man at the back takes a slow sip from his mug. Audio: cutlery on plates, a fridge humming, a chair creaking, rain on a window. No dialogue, no music. Thanks.
```

### s02-spoiler

```text
The camera is locked off and does not move. The woman turns the key, tries the door handle once, then puts the keys in her apron pocket and looks away down the street. Water beads run slowly down the glass. Behind her the white van's tail lights come on. Audio: a key turning in a lock, a door handle rattling, light rain on glass, an engine starting in the distance. No dialogue, no music. Thanks.
```

### s03-getting-out

```text
The camera is locked off and does not move. The man comes slowly down two more steps toward the camera and stops, the plastic bag swinging gently in his hand. He looks out over the camera, breathes in, and the corner of his mouth lifts a little more. Audio: leather shoes on stone steps, plastic crackling, wind between columns, a car door opening below. No dialogue, no music. Thanks.
```

### s04-recruiting

```text
The camera is locked off and does not move. Both men stop shouting at the same instant, close their mouths and slowly draw their faces apart, breathing hard through their noses. The man on the left wipes his lip with the back of his hand. Behind them, out of focus, the raised hand goes from three fingers to two. Audio: a studio buzzer, then two men breathing and the hum of hot lights. No dialogue, no music. Thanks.
```

### s05-plan

```text
The camera is locked off and does not move. The man in the middle lowers his finger until it touches the road beside the tiny figure, then slides it slowly along the model street toward the lens. The other three follow the finger with their eyes, and the man at the back keeps chewing. The paper price tags tremble slightly. Audio: a bare bulb buzzing, a fingertip dragging across card, rain on a metal roof. No dialogue, no music. Thanks.
```

### s06-colours

```text
The camera is locked off and does not move. The two men under the bulb keep counting on their fingers at each other, taking turns, neither giving way. The men by the door walk out into the blue dusk. The man at the light switch lowers his eyes from the ceiling and lets out a long breath, and the bulb swings very slightly on its flex. Audio: a bulb humming, shoes on concrete, a roller door rattling in the wind. No dialogue, no music. Thanks.
```

### s07-night-before

```text
The camera is hand-held and shakes slightly. The two men in front sway together with their heads back, laughing breathlessly with their mouths wide, and one slaps the other on the chest. Behind them the man with the glass drinks from it. The old man in the chair does not move and does not blink. Audio: wordless laughter, glasses clinking, canvas flapping in the wind, a generator humming. No dialogue, no music. Thanks.
```

### s08-march

```text
The camera is locked off and does not move. The flare burns steadily and pours thick red smoke that rolls left across the wet cobbles. The gloved hands set the steel foot of the barrier flat on the stones and let go. The flags above sway and blue smoke drifts in from the right. Audio: a flare hissing, steel scraping on stone, boots on cobbles, a far-off crowd roar with no words in it. No dialogue, no music. Thanks.
```

### s09-walk

```text
The camera is fixed to the pallet truck, so the men stay the same size in the frame while the street slides away behind them. The heavy man leans into the handle and takes a bite of the roll, chewing as he pushes. The man with the phone tilts it and grins at it, and the tall man walks on looking straight ahead. Red and blue smoke drifts across behind them. Audio: small steel wheels rattling on tarmac, flares hissing, a crowd roar with no words in it. No dialogue, no music. Thanks.
```

### s10-hoover

```text
The camera is locked off and does not move. The vacuum cleaner head slides slowly forward toward the lens and back, once. The woman pushes it without looking up. The two men on either side wobble on one leg, and the man on the left puts his raised foot down and then lifts it again as she comes nearer. Audio: an old vacuum cleaner motor droning, its wheels on marble, a leather shoe squeaking. No dialogue, no music. Thanks.
```

### s11-vault

```text
The camera is locked off and does not move. The man in front turns the small key between his finger and thumb so that it catches the light, then holds it still. The man in the goggles looks down at the drill in his hand, then back at the key, and his small smile fades. Dust drifts through the shaft of light on the floor. Audio: strip lights humming, a heavy steel door settling on its hinge, a cable dragging on concrete. No dialogue, no music. Thanks.
```

### s12a-standoff

```text
The camera is locked off and does not move. The man in the centre holds perfectly still, looking into the lens, and blinks once, slowly. The red light sweeps across his face and away, again and again. The two men at the edges breathe hard and the pistols tremble slightly. Audio: a loud alarm bell ringing close by, over everything. No dialogue, no music. Thanks.
```

### s12b-count

```text
The camera is locked off and does not move. The woman's eyes move down the page line by line and her lips move very slightly as she counts. She turns one page with her thumb. Her eyes lift from the book toward the window for a moment, then go back down. Audio: near silence, one page turning, a clock ticking. No dialogue, no music. Thanks.
```

### s13-fountain

```text
The camera is locked off and does not move. The four men look down into the fountain without moving. The pigeon takes two steps along the rim and turns its head. The carrier bag turns slowly on its handles and the lamp flickers once. Audio: a pigeon's claws on concrete, keys clinking inside a plastic bag, wind in an empty shopping precinct. No dialogue, no music. Thanks.
```

### s14-one-bill

```text
The camera is locked off and does not move. The woman's hand comes up to the lens and presses, then she lowers her arm and keeps looking up for a moment, calm. Below her the man on the left jabs his finger across the table and the man on the right spreads his empty hands, neither speaking. The man between them picks up the long receipt and reads down it. Audio: a switch clicking and a television's hum dying away, plates rattling, chairs scraping on lino. No dialogue, no music. Thanks.
```

## What came back

**Fifteen clips, all 1280×720, 8 s, with sound, in `vids\`.** Checked by me from the first,
middle and last frame of each. 🔴 **Not checked: the motion in between, and the sound.** Nobody
has listened for stray speech, and nobody has watched one end to end.

| Scene | From the three frames | Watch for |
| --- | --- | --- |
| 1 Breakfast | Forks move, Denise shifts the plates, The Ex drinks | |
| 2 The spoiler | She locks up and looks down the street; the van's lights come on | 🔴 Her face and top change by the last frame. The men by the van vanish |
| 3 Getting out | He comes down the steps with the bag | 🔴 In the middle frame he is further away, then near again. Likely a jump |
| 4 The recruiting | They stop shouting, pull apart, one wipes his lip, the fingers change | The best of the set |
| 5 The plan | The finger comes down and slides along the street | |
| 6 The colours | The two keep counting; the others leave | |
| 7 The night before | Laughing, swaying; the old man does not move | |
| 8 The march | Flare burns, smoke rolls, the officer steps away | A red flag gains a mark in the last frame |
| 9 The walk | The Fixer eats, Mr Turquoise films himself | The smoke colours swap sides |
| 10 The hoover | Hoover slides, men wobble on one leg | Made from a new still with no pistols (below) |
| 11 The vault | The key turns in the light | |
| 12a The standoff | He holds still; the red lamp turns | Very little moves |
| 12b Denise's count | Eyes down the page; a page lifts into frame | |
| 13 The fountain | The pigeon walks the rim | |
| 14 One bill | Her hand comes up, then down; the table argues | 🔴 Lettering appears on her apron in the last frame |

### Three blocks, and what got past them

Three of fifteen were refused on the first run (no clip, no charge): scenes 10, 12a and 13.

- **12a and 13 passed on a shorter prompt.** 12a lost "the pistols tremble" and "alarm"; 13 lost
  the sentence about the four men and the keys. Which words mattered is not known.
- **10 was refused twice, on two different prompts with no weapon word in either,** so the still
  was the likely cause: three pistols and a cleaner. The still was remade with empty hands and
  carnival masks pushed up on the men's heads, and its clip passed first time. The old still is
  in `images\scenes-v2\replaced\s10-hoover-r1.jpg`.

The prompts above are as first written. The three that changed, as run:

```text
The camera is locked off and does not move. The vacuum cleaner slides slowly forward toward the lens and back, once. The woman pushes it without looking up. The men on either side wobble slightly on one leg. Audio: an old vacuum cleaner motor droning, its wheels on marble, a leather shoe squeaking. No dialogue, no music. Thanks.
```

```text
The camera is locked off and does not move. The man in the centre holds perfectly still, looking into the lens, and blinks once, slowly. The red light sweeps across his face and away, again and again. Nothing else moves. Audio: a loud bell ringing close by, over everything. No dialogue, no music. Thanks.
```

```text
The camera is locked off and does not move. The pigeon takes two steps along the concrete rim and turns its head. The plastic bag turns slowly on its handles. The street lamp flickers once. The men stay still. Audio: a pigeon's claws on concrete, wind in an empty shopping precinct. No dialogue, no music. Thanks.
```

### One mistake, and what it cost

While remaking the scene 10 still, the by-hand casting script ran with Flow still in video mode,
so it made **an unplanned clip** from the still's prompt and the four Characters (about 12
credits) instead of a still. It is in the Flow project, not downloaded and not reviewed. The
mode-switch script reported `null` for both clicks and I did not stop on that.

### Credits

Fifteen kept clips and one unplanned one, at about 12 each: **about 190.** The balance was not
read before or after, so this is the price list, not a measurement.

## Three clips redone (6 October 2026, later)

**Jack:** "Redo the three flagged." Scenes 2, 3 and 14, each from the same still, with less
movement asked for. All three ran first time. The first takes are in `vids\replaced\`; the new
ones have the plain scene names in `vids\`.

Checked from **five** frames each this time (start, 2 s, 4 s, 6 s, end). Still not watched end to
end, and the sound is still not checked.

| Scene | What was wrong | What the new prompt changed | Result in five frames |
| --- | --- | --- | --- |
| 2 The spoiler | Her face and top changed; the men by the van vanished | She "stays where she is... eyes down on the lock"; no look down the street, no van lights; "everything behind her stays still" | Same face and apron in all five. The men and the van stay put. Her breath fogs the glass |
| 3 Getting out | He jumped further away, then back | He "stands still on the step, staying the same size in the frame"; no walking | Same size in all five. The bag swings, his head lifts |
| 14 One bill | Lettering appeared on her apron | Her hand "holds still"; "her apron is plain dark blue cloth and stays plain" | No lettering. Hand stays up; the table moves below |

**What the three have in common:** the first takes each asked for a body to travel or turn (walk
down two steps, turn to look away, lower an arm). The second takes ask for the body to stay and
something small to move. That fits the repo's rule that less motion is safer motion.

As run:

```text
The camera is locked off and does not move. The woman stays where she is, close to the glass, with her eyes down on the lock, and turns the key slowly. She breathes out once and her breath fogs a small patch of the glass. Water beads run slowly down the glass, and everything behind her stays still. Audio: a key turning in a lock, light rain on glass, a street lamp buzzing. No dialogue, no music. Thanks.
```

```text
The camera is locked off and does not move. The man stands still on the step, staying the same size in the frame, with the plastic bag swinging gently in his hand. He breathes in, looks out over the camera, and the corner of his mouth lifts a little more. The edge of his jacket moves slightly in the wind. Audio: plastic crackling, wind between stone columns, a car engine idling below. No dialogue, no music. Thanks.
```

```text
The camera is locked off and does not move. The woman keeps her arm raised with her hand near the lens and holds still, looking up, calm, and blinks once. Her apron is plain dark blue cloth and stays plain. Below her the man on the left jabs his finger across the table once, and the man in the middle picks up the long receipt and reads down it. Audio: a switch clicking and a television's hum dying away, plates rattling, a chair scraping on lino. No dialogue, no music. Thanks.
```

**Credits:** three more clips at about 12 each, so about 225 for the day by the price list. The
balance was not read.
