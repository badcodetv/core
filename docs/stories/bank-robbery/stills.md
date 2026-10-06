# The Bank Robbery — scene stills, first pass (6 October 2026)

**Asked for by Jack, 6 October 2026:** one still for each scene of the
[storyboard](./storyboard.md), in the style of the chosen look, "The bank in the haze"
([`look-tests.md`](./look-tests.md), round 3, frame 4, candidate b, Flow media `5a6fed78`).

**First pass. Not reviewed.** Jack's ruling the same day: known faults get fixed "when we get to
that part in the storyboard", so this pass does not stop to fix them.

- **Flow project:** `64a6c82d` (shown in Flow as "Oct 06 - 13:31").
- **Settings:** Nano Banana 2, 16:9, two candidates, no reference image, no Flow Character.
- **Files:** `Desktop\Youtube Vids\animation\bank robbery\images\`, named `sNN-<scene>-a.jpg` and
  `-b.jpg`. Not committed.
- **Fifteen stills for fourteen scenes:** scene 12 has two (the standoff, and Denise's count).

## The style lock (distilled from the chosen still)

Every prompt has the same four parts, in this order.

1. **The subject, in one sentence.**
2. **One camera:** "A news agency photograph, shot on a Canon EOS R3 with a [lens] from [a place a
   person could stand] at [time]."
3. **The scene,** starting with a dark, out-of-focus shape that cuts into the frame from one edge,
   then the people, small or middle-sized, each doing something.
4. **The light and the close,** word for word:
   cold ambient light, one named warm source as "the brightest thing in the picture", then
   *"The picture is slightly underexposed and muted: stone grey, black and navy, with small
   touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9."*

**Why a written lock and not the still as a reference image:** a reference drags its own building
and crowd into every scene ([`nano-banana-2.md`](../../google-flow/nano-banana-2.md)). The web says
both routes are used: a style tag on every prompt, or a reference frame
([Flowith](https://flowith.io/blog/nano-banana-consistent-characters-storyboard/), search summary
only). The reference route is the fallback if the scenes drift apart.

## Placeholder cast (prose only, until there are Flow Characters)

These looks are **invented for this pass** so the same people turn up in each still. They are not
canon and nobody has ruled on them.

| Who | Written as |
| --- | --- |
| Denise | a woman in her late fifties, grey-blonde hair clipped up, a tired lined face; a faded navy apron by day, a pale blue tabard at night |
| The Ex | a tall man of about sixty with swept-back silver hair |
| The crew | men in their fifties and sixties in black suits, white shirts and thin black ties |
| Mr Red, Mr Blue | the same, one in a red tie, one in a blue tie |

## The shot specs (from `shot-craft`)

| # | Scene | The job of the still | In front | Warm source |
| --- | --- | --- | --- | --- |
| 1 | Breakfast | Eleven suits take up the whole café; one woman works round them; a saucer is empty | Tea urn | Kitchen hatch lamps |
| 2 | The spoiler | She walks to job two; they leave in one van, small, behind her | Bus shelter | The café window |
| 3 | Getting out | Leaving office looks like leaving prison | Railings, a photographer | The open doorway |
| 4 | The recruiting | The row is a show, seen from behind the cameras | Studio camera | The set lights |
| 5 | The plan | The target is the whole town, not the bank | Roller shutter | One bare bulb |
| 6 | The colours | Two men cannot stop a fake argument | The model | The bulb |
| 7 | The night before | Off camera they get on; someone else is working | A caterer's back | The marquee |
| 8 | The march | Two angry crowds, one sentence, and a gap being built to the bank | Window frame | The bank's windows |
| 9 | The walk down the gap | The police open the way; the money goes in | The officer's back | The bank's doorway |
| 10 | The hoover | Eleven guns on a cleaner who is not impressed | A masked shoulder | The staff door |
| 11 | The vault | A drill for show, a key for real | Pallets | A work lamp |
| 12a | The standoff | Everyone aims at who they already hated | A tipped pallet | The alarm light |
| 12b | Denise's count | The flat is sold while she counts what she has | Door frame, hoover | The café across the road |
| 13 | The fountain | The win is a switched-off fountain | A bench and a bin | One precinct lamp |
| 14 | One bill | The saucer has a bill on it; the row is now about paying | The saucer itself | Kitchen hatch lamps |

**Cost in frame (gate 2):** shut shops in 2, 8, 9 and 13; someone working in 1, 7, 10, 12b and 14.

## The prompts

### 1. Breakfast

```text
Eleven men in black suits eat fried breakfasts at pushed-together tables in a small English greasy-spoon café while a waitress clears their plates. A news agency photograph, shot on a Canon EOS R3 with a 35mm lens from behind the counter on a grey morning.

The dark back of a steel tea urn and a rack of mugs fill the left edge of the frame, out of focus. Beyond the counter the men, in their fifties and sixties, in white shirts and thin black ties, are crammed elbow to elbow round formica tables covered in plates of egg, bacon and beans, mugs, a red sauce bottle and a brown one. Two of them point forks at each other mid-argument, one is on his phone, one is still eating. Standing among them, the only person on her feet, is a woman in her late fifties with grey-blonde hair clipped up and a tired lined face, in a faded navy apron, stacking plates up one arm, her lips moving as she counts. On the corner of the table nearest us sits an empty white saucer. A small television high on the wall shows a small boat on a grey sea.

Cold grey daylight comes through the steamed-up front window behind the men, so they are dark shapes with pale edges. The warm heat lamps over the kitchen hatch on the right are the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 2. The spoiler

```text
A waitress in her late fifties walks toward us down a half-shut English high street at dusk, on her way from one job to the next. A news agency photograph, shot on a Canon EOS R3 with an 85mm lens from the far pavement.

The scratched perspex and steel post of a bus shelter cut across the right edge of the frame, out of focus. She is in the middle distance: grey-blonde hair clipped up, a tired lined face, an anorak open over a faded navy apron, a carrier bag in one hand, looking at the pavement. She passes steel shutters, whitewashed windows and a boarded doorway. Far behind her, small, the café she has just locked still has its light on, and outside it eleven men in black suits are climbing one after another into a single white van.

Cold blue-grey dusk light from the sky on a wet pavement. The café's lit window in the distance is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 3. Getting out

```text
A tall man of about sixty in a black suit walks down the steps of a grand stone government building carrying his belongings in a clear plastic bag. A news agency photograph, shot on a Canon EOS R3 with a 135mm lens from across the road at dusk.

Black iron railings cross the foreground, out of focus, with a press photographer's shoulder and camera at the left edge. The man has swept-back silver hair, no tie and his top button undone. The clear bag holds a phone, a rolled tie and a small red leather despatch box. He is halfway down a wide flight of pale stone steps between tall columns, alone, with a slight smile. At the kerb a long black car waits with its rear door held open by a driver. Behind him the building's tall doors stand open onto a lit hallway.

Cold blue-grey dusk. The warm open doorway behind him is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 4. The recruiting (the drivers)

```text
Two politicians in dark suits, one in a red tie and one in a blue tie, shout at each other across a desk in a television studio. A news agency photograph, shot on a Canon EOS R3 with a 50mm lens from behind the studio cameras.

The dark bulk of a studio camera and its operator in headphones fill the left third of the frame, out of focus, with cables across the floor. Beyond them, on a small lit set, the two men in their fifties lean over a curved desk jabbing fingers at each other, mouths open. Between them a presenter sits back with both hands raised. Around the set the studio is dark: a lighting rig, a floor manager holding up three fingers, a wall clock, crew looking at their phones. In the shadows at the far right a tall man with swept-back silver hair, in a black suit, watches with his arms folded.

Everything off the set is cold blue-black. The set's warm studio lights are the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 5. The plan

```text
Eleven men in black suits stand round a trestle table in a lock-up garage looking down at a scale model of an English town. A news agency photograph, shot on a Canon EOS R3 with a 28mm lens from just outside the half-raised roller door at dusk.

The dark underside of the roller shutter crosses the top of the frame and an oil drum the right edge. Inside, under one bare bulb on a flex, the model covers the whole table: a high street of little cardboard houses and shops, each with a paper price tag on a cocktail stick, a stone bank at one end, and one tiny figure with a vacuum cleaner. A tall man with swept-back silver hair leans over it with one finger on the high street. The others, in their fifties and sixties, stand round it in white shirts and thin black ties, half in shadow. One eats from a foil tray, an open laptop glows on a stool, and two at the back are arguing with each other. On the breeze-block wall behind them is a corkboard of photographs joined with red string.

Cold blue dusk outside on wet concrete. The bare bulb is the brightest thing in the picture and lights only the model and the faces nearest it. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 6. The colours

```text
Two men in black suits, one in a red tie and one in a blue tie, argue nose to nose in a lock-up garage while nine others walk out past them. A news agency photograph, shot on a Canon EOS R3 with a 50mm lens from the back of the garage, looking toward the open roller door at dusk.

The edge of a trestle table carrying a cardboard model town crosses the bottom of the frame, out of focus. The two men, in their fifties, stand under a bare bulb, each counting on his fingers at the other. Around them the other men in black suits are leaving with their backs to us, pulling on coats, walking out through the open door as dark shapes. A tall man with swept-back silver hair waits by the door with a sheet of paper in one hand and the other hand on the light switch, looking at the ceiling.

The open door is a rectangle of cold blue dusk. The bare bulb over the two men is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 7. The night before

```text
A white marquee glows on a dark lawn behind a large English country house during a summer party, seen from beside the catering van. A news agency photograph, shot hand-held on a Canon EOS R3 with a 35mm lens at night, with slight motion blur.

In the foreground a caterer in a black apron sits on the van's rear step with her back to us, smoking, beside crates of empty champagne bottles. Across the wet grass the marquee's open side shows the party: men in black suits with their ties loosened, a string quartet, a chocolate fountain, waiters with trays. At the entrance two men in their fifties, one in a red tie and one in a blue tie, stand with their arms round each other's shoulders, heads back, singing. Strings of bulbs sag between poles.

The house and the trees are blue-black. The marquee's warm light, spilling across the grass, is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 8. The march

```text
Two protest marches meet in an English market square below a grey stone Victorian bank while police carry steel barriers in between them. A news agency photograph, shot on a Canon EOS R3 with a 35mm lens from a first-floor window across the square at dusk.

A window frame and a hand holding back a net curtain cut into the left edge of the frame. Below, a crowd with red flags, red scarves and red flare smoke pours in from a street on the left, and a crowd with blue flags and blue smoke from a street on the right. Each crowd carries a hand-painted bedsheet at its front that reads "WE CAN'T AFFORD TO LIVE HERE". Between them officers in hi-vis jackets carry steel barriers in pairs and set them down in two lines, leaving an empty strip of cobbles that runs straight to the bank's steps. Near the steps, with his back to the bank, a television presenter in a suit talks to a camera under a crew's small light. The bank's columns and tall windows rise above it all.

The last grey daylight is behind the bank. Its warm lit windows are the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 9. The walk down the gap

```text
Men in black suits push pallets of banknotes down an empty strip of road between two shouting crowds toward a grey stone bank, as a police officer holds a steel barrier open for them. A news agency photograph, shot on a Canon EOS R3 with an 85mm lens from behind the officer at dusk.

The officer's hi-vis back and the lifted barrier fill the right foreground, out of focus. Past him eleven men in their fifties and sixties in black suits walk away from us in ones and twos, four of them leaning on the handles of two pallet trucks stacked with shrink-wrapped banknotes. On either side, behind steel barriers, the crowds are dark shapes in hoodies and scarves under drifting flare smoke, red on the left and blue on the right, every face and raised arm turned across the strip at the other crowd. Nobody looks at the pallets. At the end of the strip, stone steps climb between columns to the bank's open doors, where a doorman waits.

Cold blue-grey dusk. The bank's warm doorway and windows are the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 10. The hoover

```text
A cleaner in a pale blue tabard pulls a vacuum cleaner through a door at the back of a grand banking hall and finds eleven men in black suits and carnival masks pointing pistols at her. A news agency photograph, shot on a Canon EOS R3 with a 35mm lens from behind the men, at night.

The dark shoulder of one masked man and the corner of a pallet of shrink-wrapped banknotes fill the left foreground, out of focus. Across a marble floor, small in a doorway between tall columns, stands a woman in her late fifties with grey-blonde hair clipped up and a tired lined face, one hand on the hose of an old upright vacuum cleaner. She is looking at their shoes, brows level, her face doing almost nothing. The men, in black suits and cheap plastic carnival masks, have all turned toward her with handguns raised. One of them is also holding a sausage roll. Brass desk lamps with green shades stand along a long wooden counter. Through the tall windows red and blue smoke drifts in the street.

The hall is cold blue-grey with small pools from the lamps. The staff door behind her stands open onto a lit corridor and is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 11. The vault

```text
A man in a black suit and safety goggles drills at an enormous round steel vault door while a second man leans past him holding a small key. A news agency photograph, shot on a Canon EOS R3 with a 28mm lens from the corridor, behind a row of pallets.

Two pallets of shrink-wrapped banknotes on pallet trucks fill the bottom and right of the foreground, dark and out of focus. The vault door is three times the height of the men, brushed steel with a spoked wheel. The driller is thin, in his fifties, sweating, jacket off, bracing a heavy drill against the steel with sparks falling. Beside him a calm grey-haired man in a black suit reaches past with the key toward a keyhole, not looking at him. Other men in black suits wait along the corridor wall, one eating, one checking his watch. At the far end a security guard watches with his hands in his pockets.

Cold greenish strip lights overhead on steel and concrete. A warm work lamp on a stand beside the drill is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 12a. The standoff

```text
Eleven men in black suits stand in a bank corridor all pointing pistols at one another while a red alarm light turns on the wall. A news agency photograph, shot on a Canon EOS R3 with a 35mm lens from the far end of the corridor, at night.

A pallet of shrink-wrapped banknotes, tipped half over, crosses the foreground, out of focus. The men, in their fifties and sixties, are frozen mid-shout. A man in a red tie and a man in a blue tie aim at each other at arm's length. A third aims one pistol at each of them while holding up a phone to film himself. A man in the middle points two pistols in opposite directions, his face neutral. Cheap plastic carnival masks are pushed up on their foreheads. Behind them an enormous round steel vault door stands open.

Cold greenish strip lights on concrete. The revolving red alarm light is the brightest thing in the picture and puts red on one side of every face. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 12b. Denise's count

```text
A cleaner in her late fifties sits alone at a table in a bank's small staff room, counting the pages of a building-society passbook. A news agency photograph, shot on a Canon EOS R3 with a 50mm lens from the doorway at dusk.

The door frame and the handle of an upright vacuum cleaner cut into the left edge of the frame, out of focus. She sits side-on at a formica table with a kettle, a mug and a folded pale blue tabard. She has grey-blonde hair clipped up and a tired lined face, reading glasses on, one finger on the open passbook, lips slightly parted. Beside her a window looks across the road to a café with a flat above it. On the wall of the flat a man on a ladder is fixing up an estate agent's board that reads "SOLD".

Cold blue dusk through the window lights half her face. The café's lit window across the road is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 13. The fountain

```text
Eleven men in black suits stand in a line with their backs to us, looking at a small municipal fountain that is switched off, in an English shopping precinct at dusk. A news agency photograph, shot on a Canon EOS R3 with a 35mm lens from behind a bench.

The slatted back of a bench and an overflowing litter bin cross the foreground, out of focus. The fountain is a dry concrete bowl with a green stain, a traffic cone lying in it and a pigeon on the rim. The men stand along its edge with their hands in their pockets, silent. The heavy man at the left end holds a supermarket carrier bag sagging with keys. At the right end a man in a red tie and a man in a blue tie stand side by side. Round the precinct are shuttered shops, a boarded unit and a charity shop. A thin drift of red and blue smoke still hangs over the roofs.

Blue dusk on wet paving. One orange precinct lamp on a pole is the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

### 14. One bill

```text
A long till receipt lies folded on a white saucer on a café table, and behind it eleven men in black suits argue about who is going to pay. A news agency photograph, shot on a Canon EOS R3 with an 85mm lens at table height on a grey morning.

The saucer and the bill are sharp in the near foreground, beside a red sauce bottle, a plate smeared with egg and a balled paper napkin. Behind them, out of focus, the men lean across pushed-together formica tables pointing at one another, mouths open, one holding up empty hands, one patting his pockets. At the back a woman in her late fifties with grey-blonde hair clipped up, in a faded navy apron, reaches up with her back to them to switch off a small television on the wall. Behind the counter a chalkboard menu has fresh smears where the prices were rubbed out.

Cold grey daylight through the steamed-up front window lights the men from behind. The warm heat lamps over the kitchen hatch are the brightest thing in the picture. The picture is slightly underexposed and muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is aware of the camera. 16:9.

Thanks.
```

## What came back

All fifteen ran first time, two candidates each (thirty stills), 1376×768. **No blocks,** including
the pistols in scenes 10 and 12a. My reading from contact sheets (`00-contact-sheet-1..3.jpg` in
the images folder); Jack has not reviewed them.

**The style held across all fifteen:** cold dusk or grey morning, one warm source, a dark shape in
front, people seen from a distance.

| # | Media ids (a, b) | Notes |
| --- | --- | --- |
| 1 | `292247a7`, `67f4cdec` | Urn in front, steamed window, Denise with plates, the empty saucer on the counter, the boat on the television. Candidate a shows a real brown-sauce brand on the bottle |
| 2 | `080af229`, `9a519819` | Denise walking, shut shops, the suits and one white van small behind her, the café lit. Both work; b has more street |
| 3 | `1af0b974`, `7ad95888` | Railings, a photographer, the steps, the clear bag with a red box in it, the car door held. The lit doorway rhymes with the bank |
| 4 | `e8750ed4`, `5483ff13` | From behind the camera. The two men over the desk, the presenter with his hands up, the floor manager's fingers, The Ex in the shadows on the right |
| 5 | `b69facb4`, `76a7b8c0` | Seen from outside the half-raised door. One bulb, the model town, the corkboard with red string, The Ex pointing |
| 6 | `02dc971f`, `d48ea669` | Red tie and blue tie arguing under the bulb, the rest leaving into blue dusk, The Ex at the switch looking at the ceiling |
| 7 | `fc25aa7f`, `534aa749` | The caterer smoking by the van, the marquee glowing, red tie and blue tie arm in arm. Candidate b has them in shirtsleeves |
| 8 | `45e42b58`, `934cc5c5` | From a window with a net curtain. Red smoke and blue smoke, both bedsheets reading "WE CAN'T AFFORD TO LIVE HERE", police building the gap, the presenter under a light |
| 9 | `6c6b3b50`, `05868dda` | Over the officer's shoulder as he holds the barrier. Suits and two pallets walking away to the lit bank door, crowds in red and blue smoke |
| 10 | `92fd448d`, `ccf8ee23` | Denise small in a lit doorway with the hoover, pistols on her from all sides, green lamps, coloured smoke in the windows. Candidate b is the cleaner frame |
| 11 | `ab20475e`, `eaffb134` | Drill and sparks, the work lamp, the other man reaching past with a key, pallets in front, men waiting, a guard at the end |
| 12a | `9027ebff`, `c35417d9` | Everyone aiming at everyone under a red alarm light, the tipped pallet in front, the open vault behind. The masks came back as small party masks on foreheads, which looks silly rather than sinister |
| 12b | `556e8e74`, `9459ec1b` | Denise with the passbook and glasses, the hoover handle in the door, and across the road a man on a ladder fixing a SOLD board above the lit café. The quietest and best of the set |
| 13 | `9960b4fb`, `e97a2f51` | Backs of the suits round a dry fountain with a cone in it, one precinct lamp, a bag of keys at the left end. Candidate a has thirteen men in a row; candidate b has water in the fountain |
| 14 | `fdcca89c`, `ce6c863b` | The long receipt on the saucer in front, the table erupting behind, Denise reaching up to the television |

**Known faults, left for when each scene is worked on (Jack's ruling):**

- **Denise is a different woman in each still,** and so is every crew member. Needs Flow
  Characters, or reference stills, before any of these becomes a plate for a clip.
- **Head counts:** rarely exactly eleven.
- **Small lettering** on shop signs and a branded sauce bottle (scene 1 a).
- **Scene 12a's masks** need describing properly, or removing.
- **Scene 13 b** has water in a fountain that is meant to be off.
- **The scene 8 rule "nothing burns"** is still unruled. These stills use smoke and flares, no fire.


---

# Second pass — the cast, and stranger cameras (6 October 2026)

**Asked for by Jack:** remake the scenes with the cast. "Some of the shots look very AI like." Try
low and high angles, the point of view of objects in the room, and different lighting. He pasted
a short note on one American director's habits: off-kilter angles, tight close-ups with a stare
into the lens, still wide shots, faces layered over backgrounds, and a cheap hand-held camcorder.

**No director or person is named in any Flow field.** Each habit is written as a camera position,
a lens and a light.

- **Flow project:** `63d22c4b` ("Oct 06 - 14:23"), where the twelve Characters live.
- **Settings:** Nano Banana 2, 16:9, one candidate each.
- **Casting:** by hand through the "@" picker (`scripts/flow/.tmp/cast-many-v3.mjs`), up to four
  Characters a still, which is the model's stated limit. Anyone else in frame is "men in black
  suits". With a Character attached the prompt gives only where they are and what their face does.
- **Files:** `images\scenes-v2\`.

## What changed from the first pass, and why

| First pass | Why it read as AI ([`symptoms.md`](../../cinematography/symptoms.md)) | Second pass |
| --- | --- | --- |
| Every camera at standing height, across the room | "Eye-level, dead-on, nothing hidden: the exact recipe for furniture" | Every still breaks height: the floor, the table top, a ceiling corner, inside an object |
| A warm lamp plus cool daylight in every frame | Two lights, and the same two every time | **One light, no fill,** different in each scene: a bulb, a flare, an alarm lamp, a street lamp, a camcorder's own light |
| Everyone visible, small, evenly spread | Nothing withheld | Faces in half shadow, heads cut by the frame, something huge and out of focus against the lens |
| "A news agency photograph" | A neutral record | "A frame from a feature film", with a named lens for each angle |

## What the research said (web, 6 October 2026; search summaries only)

- The director's cinematographers describe **"dark has to be darker"**, soft light from **one
  source with no fill and no backlight**, lamps in the room that have to be dimmed, and the camera
  put **in the top corner of a room, under a table, or looking through an object**.
  [Variety](https://variety.com/2025/artisans/global/frederick-elmes-peter-deming-david-lynch-1236438889/),
  [StudioBinder](https://www.studiobinder.com/blog/what-does-lynchian-mean/),
  [Filmmaker](https://filmmakermagazine.com/131058-you-build-a-movie-like-you-build-a-fire-lost-highway-dp-peter-deming-on-restorations-lighting-and-working-with-david-lynch/)
- Extreme up and down angles belong to exceptional points of view: someone on their back, an
  animal, a watcher above. [Britannica](https://www.britannica.com/art/film/Shooting-angle-and-point-of-view)
- **From the repo, kept:** a tilted horizon wears out fastest and returned black wedges on wide
  shots, so only the camcorder frame is tilted; a high shot keeps its subject only if it is high
  **and close**; near-black needs one brighter place in it.

## The fourteen shots

| Scene | Where the camera is | Characters attached |
| --- | --- | --- |
| 1 | Low, from the table top | Denise, Mr Blue, Mr Red, The Ex |
| 2 | Through glass, with a reflection laid over her face | Denise |
| 3 | Very low, from the bottom step | The Ex |
| 4 | Extreme close-up, two profiles | Mr Blue, Mr Red |
| 5 | From inside the model, at the height of a toy figure | The Ex, The Donor, The Governor, The Fixer |
| 6 | From the top corner of the room, looking down past the bulb | Mr Blue, Mr Red, The Ex |
| 7 | A cheap camcorder, too close, its own light on | Mr Red, Mr Blue, The Presenter, The Proprietor |
| 8 | From the cobbles, at boot height | none |
| 9 | From on top of the money, looking back at the men pushing it | The Ex, The Fixer, Mr Turquoise, The Donor |
| 10 | From the floor | Denise, Mr Blue, Mr Red, The Governor |
| 11 | From inside the vault as the door opens | The Governor, The Accountant |
| 12a | Extreme close-up, a stare into the lens | The Presenter, Mr Blue, Mr Red |
| 12b | Extreme close-up, with the street laid over her in the glass | Denise |
| 13 | From the bottom of the dry fountain, looking up | The Ex, The Donor, Mr Blue, Mr Red |
| 14 | From the television on the wall, as her hand comes up to switch it off | Denise, Mr Blue, Mr Red, The Governor |

Scene 12 is two stills again (12a and 12b), and scene 8 has no Character in it.

## The prompts

### s01-breakfast

- **Characters attached:** Denise, Mr Blue, Mr Red, The Ex

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with an 18mm lens resting on a café table top among the breakfast things, looking up. A red sauce bottle and a brown one tower in the near foreground, out of focus, beside a plate of egg and beans and an empty white saucer. Across the table Mr Blue on the left and Mr Red on the right lean in over their plates pointing forks at each other, mouths open mid-argument. Between them, standing over the table and seen from below, Denise looks down with her lips slightly parted, counting, a stack of dirty plates up one arm. Behind her shoulder The Ex sits back with a slight smile, stirring a mug. A greasy-spoon café ceiling with a strip light that is switched off. One light source only, no fill: grey morning daylight through a steamed-up window on the left. The right side of every face falls into deep shadow. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s02-spoiler

- **Characters attached:** Denise

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with an 85mm lens from inside a dark café, through the steamed glass of its front door. Denise is outside, very close to the glass, her face filling the right half of the frame as she turns a key in the lock, eyes down, face doing almost nothing. Water beads and a wiped streak on the glass cross her face. Laid over the left half of the frame, as a reflection in the same glass, a line of men in black suits climbs into one white van across the street, small and ghostly. A CLOSED sign hangs at the top edge, seen from behind. One light source only, no fill: a single orange street lamp behind her, rimming her hair. The café interior around the door is black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s03-getting-out

- **Characters attached:** The Ex

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 21mm lens from the bottom step of a grand stone government building, almost at ground level, looking steeply up. The Ex comes down the steps toward the lens, seen from below, towering, no tie and his top button undone, with a small one-cornered smile, looking over the camera at something beyond it. In his nearer hand, large and close to the lens, swings a clear plastic bag holding a phone, a rolled black tie and a small red leather despatch box. Above and behind him tall stone columns lean together toward a dusk sky, and the building's doors stand open. One light source only, no fill: warm light from the open doorway behind him, so he is nearly a silhouette with a bright edge, and the red box glows through the plastic. The steps in front fall into deep blue shadow. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s04-recruiting

- **Characters attached:** Mr Blue, Mr Red

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 100mm macro lens in a television studio. An extreme close-up of two faces in profile, nose to nose, filling the whole frame: Mr Blue on the left and Mr Red on the right, both mid-shout, mouths wide, a fleck of spit caught in the light between them, sweat on their foreheads, veins in their necks. The frame cuts off the tops of their heads and their chins. In the narrow gap between the two faces, far behind and out of focus, a floor manager holds up three fingers beside a red tally light. One light source only, no fill: a single hot studio lamp directly above them, bright on brows, noses and lips, with the eye sockets and everything behind them black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s05-plan

- **Characters attached:** The Ex, The Donor, The Governor, The Fixer

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 24mm probe lens placed inside a cardboard scale model of an English town, at the height of the model's street. Little cardboard houses and shops rise on both sides of the near foreground like real buildings, each with a paper price tag on a cocktail stick, and a tiny plastic figure with a vacuum cleaner stands in the road close to the lens. Looming over the rooftops like giants, seen from below, are four huge faces looking down into the model: The Ex in the middle with one enormous finger coming down toward the street, The Donor on the left with one eyebrow raised, The Governor on the right with his face blank, and The Fixer behind them chewing. Above them the rafters of a lock-up garage. One light source only, no fill: a bare bulb hanging just above their heads, bright on the tops of the model roofs and their foreheads, with their eyes in shadow and the garage behind them black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s06-colours

- **Characters attached:** Mr Blue, Mr Red, The Ex

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 16mm lens from the top corner of a lock-up garage, pressed against the ceiling and looking steeply down, like a security camera. A bare light bulb on a flex hangs large and burnt-out white in the near foreground. Directly beneath it Mr Blue and Mr Red stand nose to nose, each counting on his fingers at the other, their shadows thrown out across the concrete floor like clock hands. Around them the floor is empty except for a trestle table with a cardboard model town on it. At the edge of the pool of light, backs of men in black suits walk away into the dark toward an open roller door showing blue dusk. By the door The Ex stands with one hand on the light switch, looking up at the ceiling, straight toward the lens. One light source only, no fill: the bare bulb. Beyond its pool the garage is black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. 16:9. Thanks.
```

### s07-night-before

- **Characters attached:** Mr Red, Mr Blue, The Presenter, The Proprietor

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a home video shot at night on a cheap standard-definition digital camcorder held at arm's length, with its small built-in light switched on. Mr Red and Mr Blue fill the frame, too close to the lens, arms round each other's necks, ties loosened, heads back, singing with their mouths wide open, faces shiny and slightly blown out by the camera's light, their eyes catching it. The frame is tilted and cuts off the top of one head. Behind them in the dark, lit only by spill, The Presenter laughs with a champagne glass raised and The Proprietor sits alone in a chair staring into the lens, not smiling. Further back, the pale wall of a marquee, a string of bulbs and a chocolate fountain, soft and noisy. One light source only: the camcorder's own harsh white light, falling off within two metres into grainy black. Low resolution, video noise in the shadows, smeared highlights, washed colour. 16:9. Thanks.
```

### s08-march

- **Characters attached:** none (ordinary tool call)

```text
A frame from a feature film, shot on 35mm with a 16mm lens lying on the wet cobbles of an English market square at dusk, at boot height, looking up. In the near foreground a dropped hand flare burns on the cobbles, pouring thick red smoke across the left of the frame, and the steel foot of a crowd barrier is being set down beside it by a pair of hands in a hi-vis sleeve. Beyond, seen from below, a forest of legs, boots and trainers, the bottom edge of a hand-painted bedsheet banner, and raised arms holding red flags on the left and blue flags on the right, with blue smoke drifting in from the right edge. Between the two crowds an empty strip of cobbles runs away to the steps of a grey stone Victorian bank that towers over everything, its columns leaning together toward the sky. One light source only, no fill: the red flare in the foreground, lighting the wet cobbles and the undersides of everything near it. The bank's tall windows are small warm rectangles far above. The rest falls into deep blue-black. Muted colour: stone grey, black and navy, with red and blue the only strong colour. Visible 35mm film grain. 16:9. Thanks.
```

### s09-walk

- **Characters attached:** The Ex, The Fixer, Mr Turquoise, The Donor

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 21mm lens strapped to the front of a pallet truck, low, looking back over a stack of shrink-wrapped banknotes at the men pushing it. The plastic-wrapped corner of the money fills the bottom of the frame, out of focus, with the truck's handle rising behind it. Gripping the handle and leaning into it, seen from below, is The Fixer, chewing, a sausage roll in his free hand. Beside him The Ex walks upright and calm, looking straight ahead over the camera. On the other side Mr Turquoise holds a phone up at arm's length, filming himself and grinning at it. Behind them The Donor follows with his hands in his pockets. Over their shoulders, out of focus, crowd barriers, raised arms and thick drifting flare smoke, red on one side of the frame and blue on the other. One light source only, no fill: low dusk daylight from behind the men through the smoke, so their faces are in shade with bright edges, and the smoke glows. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s10-hoover

- **Characters attached:** Denise, Mr Blue, Mr Red, The Governor

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with an 18mm lens lying on the marble floor of a grand banking hall, looking up. The head of an old upright vacuum cleaner fills the near foreground, coming straight at the lens. Behind it, seen from below and towering, Denise pushes it in a pale blue cleaner's tabard, looking down past the camera at the floor, brows level, face doing almost nothing. On either side of her path men in black suits stand on one leg with the other polished shoe lifted off the floor to let her through: Mr Blue on the left and Mr Red on the right, each holding a pistol pointed at the floor and looking down at their own raised feet, and behind them The Governor with one foot lifted and his hands clasped. Tall columns and a dark coffered ceiling rise above them. One light source only, no fill: a row of brass desk lamps with green glass shades on a counter at the left, throwing long low light across the floor. The ceiling and the far end of the hall are black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s11-vault

- **Characters attached:** The Governor, The Accountant

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 24mm lens from deep inside a dark bank vault, looking out through its round doorway as the door swings open. The inside of the vault is black; the thick circular steel door frame makes a ring round the picture, and the edge of a shelf of old banknotes catches a little light in the near foreground. In the bright circle of the doorway stands The Governor, holding a small key up between finger and thumb, his face blank. Just behind him The Accountant, in safety goggles pushed up on his forehead and with a heavy drill hanging from one hand, looks at the key with a small smile. Behind them a pallet of shrink-wrapped banknotes waits in a concrete corridor. One light source only, no fill: cold strip light in the corridor behind them, pouring through the doorway in a hard-edged shaft across the vault floor. They are lit from behind and above, with their eyes in shadow. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s12a-standoff

- **Characters attached:** The Presenter, Mr Blue, Mr Red

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with an 85mm lens in a concrete bank corridor. A tight close-up of The Presenter's face in the centre of the frame, looking directly into the lens with a calm practised half-smile, perfectly still. His arms are stretched out to either side so that each hand, holding a pistol, leaves the frame at the left and right edges, pointing in opposite directions. Out of focus at the left edge is the angry face of Mr Blue with a pistol barrel pointed across the frame, and out of focus at the right edge the angry face of Mr Red with another, both shouting past him at each other. One light source only, no fill: a revolving red alarm lamp on the wall to the left, washing the left half of his face deep red while the right half falls into black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. 16:9. Thanks.
```

### s12b-count

- **Characters attached:** Denise

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 100mm lens from outside a small staff-room window at dusk, through the glass. An extreme close-up of Denise inside, her face filling the frame from forehead to chin, reading glasses on, eyes down, lips slightly parted as she counts. In the lenses of her glasses are two small reflections of the open pages of a building-society passbook. Laid over her cheek and forehead, as a reflection in the window glass, is the street behind the camera: a café with a flat above it, and a man on a ladder fixing an estate agent's board that reads "SOLD", seen back to front and ghostly. One light source only, no fill: the last blue dusk through the window on the near side of her face. The far side of her face and the room behind her are black. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s13-fountain

- **Characters attached:** The Ex, The Donor, Mr Blue, Mr Red

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 14mm lens lying at the bottom of a dry concrete municipal fountain, looking straight up. The stained concrete rim makes a ring round the picture. In the near foreground a fallen traffic cone lies across one corner of the frame and a pigeon stands on the rim, looking down. Leaning over the rim and looking down into the fountain, seen from below against a blue dusk sky, are four faces: The Ex with a slight smile, The Donor holding a supermarket carrier bag that sags with keys over the edge, and Mr Blue and Mr Red side by side, both frowning down at the same dry drain. Other men in black suits are dark shapes round the rest of the rim. One light source only, no fill: one orange precinct lamp on a pole behind The Donor's shoulder, flaring slightly, lighting one side of each face and leaving the other side dark against the sky. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.
```

### s14-one-bill

- **Characters attached:** Denise, Mr Blue, Mr Red, The Governor

```text
The named people are the attached Characters, with their own faces and clothes. A frame from a feature film, shot on 35mm with a 16mm lens from the position of a small television mounted high on a café wall, looking steeply down into the room. Denise stands directly below, seen from above, reaching up toward the lens, her hand large and out of focus in the near foreground about to press a button, her face tilted up and calm, in a faded navy apron. Below and behind her, round pushed-together formica tables covered in dirty breakfast plates, men in black suits are on their feet arguing: Mr Blue jabbing a finger at Mr Red, who holds up both empty hands, while The Governor sits still between them looking at a long till receipt on a white saucer in the middle of the table. One light source only, no fill: grey morning daylight through the steamed-up front window on the right, lighting the table and one side of Denise's face, with the corners of the café in shadow. Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour. Visible 35mm film grain. 16:9. Thanks.
```

## What came back (second pass)

Fifteen stills, one candidate each, 1376×768, all first time, no blocks. Thirteen were cast by hand
(13 of 13 attached and saved); scene 8 was an ordinary tool call. All fifteen are on
`00-contact-sheet.jpg` in `images\scenes-v2\`. My reading; **Jack has not reviewed them.**

**The cast held.** Denise, The Ex, Mr Blue, Mr Red, The Donor, The Governor, The Fixer, The
Presenter, The Proprietor, The Accountant and Mr Turquoise are each recognisably the same person
in every still they are in, including from below, from above and in extreme close-up. The Platform
is not in any of these stills.

| Scene | Camera | Notes |
| --- | --- | --- |
| 1 Breakfast | Table top | Sauce bottles huge at the edges, Mr Blue and Mr Red arguing over the plates, Denise above them counting, The Ex behind. The empty saucer is centre front |
| 2 The spoiler | Through the café door | Denise close at the glass locking up, the CLOSED sign back to front, the suits climbing into a white van behind her under one orange lamp. They are seen through the glass, not as a reflection |
| 3 Getting out | Bottom step | The Ex towering, columns leaning in, the bag with the red box close to the lens |
| 4 The recruiting | Extreme close-up | Two shouting profiles filling the frame, a tally light and three fingers in the gap between them |
| 5 The plan | Inside the model | Giant faces over cardboard rooftops, price tags, The Fixer's finger coming down, the tiny figure with the hoover in the street. The best of the set. It is The Fixer's finger, not The Ex's |
| 6 The colours | Ceiling corner | The bulb huge in front, the two arguing under it with long shadows, the rest leaving into blue dusk, The Ex at the switch |
| 7 The night before | Camcorder | Mr Red and Mr Blue singing into the lens, The Presenter laughing, The Proprietor alone in a chair staring. Sharper than a real camcorder; the low-resolution ask was mostly ignored |
| 8 The march | Cobbles | A flare burning in front, hands setting a barrier down, the bank leaning above. The banner lettering is garbled and the sleeve reads as a firefighter's |
| 9 The walk | On the money | The Fixer pushing with a sausage roll, Mr Turquoise filming himself, The Ex and The Donor, red and blue smoke behind |
| 10 The hoover | The floor | The hoover head coming at the lens, Denise above it, Mr Blue and Mr Red each with one foot lifted, The Governor behind. Green lamps down the left |
| 11 The vault | Inside the vault | A black ring round The Governor holding up the key, The Accountant with the drill. No goggles on him |
| 12a The standoff | Close-up, eyes to lens | The Presenter calm and smiling into the camera with his arms out, Mr Blue and Mr Red shouting at each edge, a red alarm lamp |
| 12b Denise's count | Through the window | Her face filling the frame, glasses on, eyes down, the SOLD board in the glass beside her. The passbook reflections in her lenses are faint |
| 13 The fountain | Bottom of the fountain | The rim as a ring, four faces looking down, the cone, the pigeon, the bag of keys hanging over the edge |
| 14 One bill | The television | Denise's hand coming up at the lens, her face tilted up, the three men and the receipt on the table below |

**To fix when each scene is worked on:**

- **Scene 8:** banner words and the hi-vis sleeve.
- **Scene 7:** make it look like cheap video, or do that in post.
- **Scene 5:** the pointing finger should be The Ex's.
- **Scene 2:** the van as a reflection laid over her face was the idea; it came back as a view
  through the glass. Works anyway.
- **Scene 11:** goggles.
- **Every scene shows at most four named faces,** so "eleven" is never on screen at once here.

### Three stills redone (6 October 2026, later)

Jack: "they are great. Fix the listed faults." Scenes 5, 8 and 11 were remade, one candidate each,
all first time. The first versions are in `images\scenes-v2\replaced\`.

| Scene | Changed in the prompt | Result |
| --- | --- | --- |
| 5 | "The Ex is nearest and largest, in the middle... it is his arm and his enormous pointing finger"; The Fixer "furthest back... with both hands out of sight" | The finger is now The Ex's. The Fixer is behind, hand at his mouth |
| 8 | The banner removed; "plain red cloth flags"; "plain yellow police hi-vis with two silver reflective bands" | No lettering. The officer reads as police. More of the bank's front is visible |
| 11 | "wearing large clear plastic safety goggles over his own glasses, with concrete dust on his shoulders" | Goggles on, dust on his suit |

**Jack approved this pass in words ("they are great") without naming scenes.** The clips made from
these stills are in [`clips.md`](./clips.md).
