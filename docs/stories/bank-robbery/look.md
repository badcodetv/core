# The Bank Robbery — look

> The look for this story only. Read before any still or clip (new-image, scene-images,
> scene-animation, flow-prompt). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

**Status:** LOCKED for the film — **"The bank in the haze"**, chosen by Jack, 6 October 2026
([`look-tests.md`](./look-tests.md) round 3, frame R3-4, candidate b, Flow media `5a6fed78`). Kai had not
seen it when it was chosen. Refined the same day by the second still pass, which Jack approved (*"they
are great"*), and on 8 October by the riot look reference `br5-riot-look`. **Colour and light changed on 9 October 2026**
(cut 8, after Jack on cut 7: *"maybe it is a tad too grey as well, there should be more colour"*): the
grey colour lock and "one light, no fill" are **superseded** by named saturated colours per place and two
lights of different colours (*Rules*, below; the old lock is in *History*). Jack approved cut 10 on
12 October (*"That is great"*). The song's music video ("The Speakeasy Mint") has its own LOCKED look,
K3a (Jack, 2026-10-25) — see *Per part*.

## In one paragraph

A **heist film shot like the news at dusk**: cold ambient light, **one warm source** that is the brightest
thing in the picture, a dark out-of-focus shape cutting into the frame from one edge, and **red and blue
carried by things people brought** — flare smoke, flags, scarves, bin lids, ties — never issued like
cards. From cut 8 on, **each place has two or three named saturated colours and two lights of different
colours** (the banking hall: black and cream chequered floor, mahogany, oxblood columns, brass, green
banker's lamps against pink flare smoke; the strongroom: cream gloss brick, oxblood floor, a red fire
bucket, one tungsten lamp against a green glow — [`stills-v8.md`](./stills-v8.md)). A declining English
town is in every frame. From the second pass on the camera breaks height (floor, table top, ceiling
corner, inside an object): *"david lynch type of cinematography… interesting angles, cinematic, funny and
pretty to look at, whilst being gritty"* (Jack; never named in a prompt).

## Preamble(s)

There is no single pasted preamble; the lock is a **four-part prompt shape** with a fixed close
([`stills.md`](./stills.md) §"The style lock", distilled from the chosen still). The chosen still's own
prompt (R3-4) is verbatim in [`look-tests.md`](./look-tests.md).

**First pass (news-agency camera)** — superseded by the second pass; its camera sentence and grey close
are in *History*.

**Second pass onwards (the look Jack liked, kept in v3; colour and light changed at cut 8)** — [`stills.md`](./stills.md) §"Second pass",
[`stills-v3.md`](./stills-v3.md):

1. `A frame from a feature film, shot on 35mm with a [lens] lens [in a named physical place].`
2. Something large and out of focus against the lens.
3. The people: where each one is and what their face is doing (the Character carries how they look).
4. One sentence saying what is behind them "and nothing else".
5. ~~`One light source only, no fill:`~~ **From cut 8:** two named light sources of different colours,
   then where the shadow falls.
6. ~~The grey colour lock~~ **From cut 8:** two or three saturated colours named for the place. Never
   "muted", "cold", "grey", "no fill", "the only strong colour". (The old lock is verbatim in *History*.)

With Characters attached, the prompt opens: `The named people are the attached Characters, with their own
faces and clothes.` and closes `Visible 35mm film grain. Nobody looks at the camera. 16:9. Thanks.`
(s01-breakfast, verbatim in `stills.md`).

**The riot scenes** (from 8 October) attach `br5-riot-look` — a frame of our own `s08-march` clip (the
officer laying the barrier), uploaded to Flow project `63d22c4b` — as the look reference. Jack: *"realistic
and gritty, the flares, the camera being low to make it look scary, maybe add a dutch angle … really
disorientating and cinematic."*

## Rules for this story

- **No director, film or person named in any Flow field.** Every habit is written as a camera position, a
  lens and a light.
- **Every frame names where its light comes from: two lights of different colours** (from cut 8, 9 Oct
  2026; was "one light, no fill"). Vary the pair by place: the first pass's same warm lamp plus cool daylight
  in every frame read as AI. One part of every dark frame is clearly brighter than the rest, or it
  reads as a broken file.
- **Two or three saturated colours named for each place.** Never write "muted", "cold", "grey" or "no
  fill" (the old tail ordered grey in most stills — [`review-cut7.md`](./review-cut7.md)).
- **Short prompts, action first:** a still near 115 words, a clip near 60 (cut 7 averaged 244 and 120).
  One line for a reference. Never describe an attached Character.
- **Stage the hard move as already done** (mask on, cloth under the hand, gun raised, key in the lock):
  read the cannot-do list at the top of [`docs/google-flow/README.md`](../../google-flow/README.md) before
  designing a shot. Jack: *"flow clearly struggles with stuff like this"* (people lifting a leg while she
  hoovers).
- **A person with a line who is not a Flow Character is shown from behind**; the line is made outside Flow
  (`scripts/bank-robbery/br-tts-v8.py`).
- **Check clips at two frames a second or finer** before placing them.
- These six came from the cut-7 audit (Claude's rules, not Jack's words); he approved the cuts made with
  them (cut 10).
- **Pistols small and far off**; **a real-looking place over a model or a metaphor**; headlines are a
  spinning newspaper graphic, not someone holding a photo (Jack's notes on cuts 3 and 4, 8 Oct).
- **Eye-level, across-the-room, flat even light reads as AI to Jack** (*"some of the shots look very AI
  like… low or high angels, or from perspectives of objects in the room, mess around with lighting"*,
  6 Oct). Name every camera position as a physical place.
- **A shot Jack has seen and liked is not replaced by a re-make without asking** (he loved the old
  `s09-walk` eating-and-pushing clip).
- **Every wide shot of the crew shows a cost** (shut shops, Denise small in the back, an empty saucer).
  Someone is working in the frame where the scene allows.
- **Something in the foreground**; **something specific to this town in every frame**.
- **Red and blue arrive by accident**: smoke (best), flags on poles, plain knitted scarves with no badge,
  bedsheet banners in red or blue paint, bin lids, Mr Red's and Mr Blue's ties. Never two crowds holding
  red and blue cards (Jack: *"looks AI like"*).
- **Crowds are ordinary people**, same sort and same anger on both sides; nobody stupid, ugly or drunk
  ([`the-reader.md`](../../marketing/the-reader.md)). Hooded fire-starters are the risky frame.
- **No logos on clothing; no lettering** except placards that are spelt in the prompt. A word in the prompt
  can leak onto cloth ("BEDSHEET BENNER").
- **A written lock, not the chosen still as a reference** for scene stills: a reference drags its own
  building and crowd into every scene. The reference route is the fallback if scenes drift apart (and is
  used for the riot via `br5-riot-look`).
- **Tilt only where it means something**: a tilted horizon wears out fast and returned black wedges on wide
  shots. A high shot keeps its subject only if it is high **and close**.
- **Casting:** up to four Characters a still (the model's limit); anyone else is "men in black suits".
  With a Character attached, say only where they are and what their face does. Attach the portrait as well
  when the costume matters (Barry's hi-vis).
- **Talking:** full narration with several narrator voices, **no lip-sync** (15 Oct 2026 call). Mouths on
  screen are avoided.
- **Engines:** stills Nano Banana 2, 16:9; clips Omni 1.1 Flash, 720p, 8 s, camera locked.
- **Flow video is 16:9 or 9:16 only**; a 2.39 crop happens in Premiere.

## Anchors

- **The chosen still:** R3-4 *The bank in the haze*, candidate b, Flow media `5a6fed78` (candidate a
  `ca40d2ae`), Flow project `64a6c82d-2e1c-4ce8-9668-f67980bd7f5e` ("Oct 06 - 13:31"). Prompt verbatim in
  [`look-tests.md`](./look-tests.md).
- **The riot look reference:** `br5-riot-look` in Flow project `63d22c4b`, from `images\scenes-v2\s08-march.jpg`
  ([`stills-v5.md`](./stills-v5.md)). Also `br5-cafe` (the SOLD night still) and `br7-vault` as later scene
  references ([`stills-v6.md`](./stills-v6.md), [`stills-v7.md`](./stills-v7.md)).
- **Second-pass stills** Jack approved: `Desktop\Youtube Vids\animation\bank robbery\images\scenes-v2\`
  (contact sheet `00-contact-sheet.jpg`). Not committed.
- Per-pass prompts, word for word: `scripts/bank-robbery/br-stills-v3.json` … `br-stills-v10.json` and the
  matching `br-clips-*.json`.

## Cast

Twelve Flow Characters, each with a Portrait, a Body and a custom Voice, in Flow project
`63d22c4b-4bb8-46c6-81a1-ac598fc01030` ("Oct 06 - 14:23"). Ids, picked portraits and voice texts:
[`characters/cast-portraits.md`](./characters/cast-portraits.md). Portrait recipe: plain dark grey studio
backdrop, one large soft light, unretouched (pores, lines, slight asymmetry), expression written as
muscles. **They are types, not people** — none may resemble anyone real.

| Who | Flow Character id |
| --- | --- |
| Denise | `182650a9-67fe-4120-84b6-dfd1b8664c97` |
| The Ex | `fe8bbaf3-8bc1-4a40-bf6c-94772b4fba79` |
| The Fixer | `868e9f04-89f7-4c16-8b91-e814bda00206` |
| The Donor | `90eddd2d-75e2-470b-809e-92f6196737de` |
| The Governor | `3c37992a-ec0a-4c40-95af-824e6be1659a` |
| The Proprietor | `bf7a293e-9ec4-44e8-b065-6b969fa6af60` |
| The Presenter | `5f65f473-d436-4a95-b164-c912bd07ee69` |
| The Platform | `98bcb127-358b-46b1-9100-1b07090e3d7a` |
| The Accountant | `8332d003-7388-4db1-b0d8-cd9c287eef52` |
| Mr Blue | `e377138d-c795-401c-b556-5676afa09706` |
| Mr Red | `517dae07-ce42-4e19-93f8-4dc41d8e75d4` |
| Mr Turquoise | `0c3d04e7-016d-4d20-a289-1708b264052f` |
| Barry (the short) | `491aad1f-3e8f-4b07-b03c-b4b552edfda3` ([`short-shots.md`](./short-shots.md)) |

The crew: men in their fifties and sixties in black suits, white shirts and thin black ties; Mr Red and
Mr Blue in a red and a blue tie.

## Places

- **The greasy-spoon café** (scenes 1, 14; the short) — formica tables, tea urn, red and brown sauce
  bottles, a steamed-up front window, kitchen hatch heat lamps.
- **The high street and market square** — shuttered shops, a stained rendered wall, cobbles; the march,
  the gap held by police barriers.
- **The bank** — grey stone Victorian, tall columns, a wide flight of steps, warm lit windows; the vault in
  cold strip light on brushed steel.
- **The garage** (the plan) — one bare bulb over a bare table. **No model town** (Jack, 8 Oct: *"all of it
  out, or anything similar it just does not work"*).
- **The fountain** (the end) — switched off, blue dusk, one precinct lamp.
- **Denise in the rain** looking up as the café is sold (Jack, 8 Oct: the *Blade Runner* rain shot, never
  named in a prompt).

## Never

- Teal and orange, "cinematic" as a bare word, everything blurred behind the subject — the AI default.
- Two even lines of crowd holding coloured cards.
- Football club crests, brand logos.
- Stretched-lens flares (unsourced, but they put blue streaks on everything).
- Eleven sharp suits in a clean frame (an advert for them).
- A real person, film or director in any field.
- The cardboard model town, or anything like it (Jack, cuts 3 and 4).
- Guns pointed at the lens in close-up; a hand-with-remote at a window; grey-daylight eye-level crowds
  (all called *"AI slop"* by Jack, cut 3).
- "Muted", "cold", "grey", "no fill" in a prompt (from cut 8).

## Per part

- **The riot / march (scene 8)** — low, steeply up, tilted, a flare by the lens, attached `br5-riot-look`
  (from 8 October; `stills-v5.md` onwards). Cut 10 shows six one-second shots of the two sides shouting
  (`stills-v10.md`).
- **The short** (15 October, [`short-shots.md`](./short-shots.md)) — opens on real Second World War footage
  ([`footage-ww2.md`](./footage-ww2.md)) into a painting on the café wall.
- **Music video, "The Speakeasy Mint"** — LOCKED **K3a** (Jack, 2026-10-25; media `d81d7f7a`, Flow project
  `dedd295f` "Oct 25 - 09:43"): sitcom figures with real-skin faces, every colour in thick oil brushstrokes,
  wet cobbles, the small red moon. From scene 7 round 2 (2026-10-26) every prompt opens with the **"K3a
  lit"** lead, verbatim from [`songs/mv-speakeasy-mint/script.md`](./songs/mv-speakeasy-mint/script.md):

  ```
  Prime-time adult animated sitcom characters with simple rounded cartoon bodies, flat colour and black outlines, but every face is painted with startling real skin: pores, stubble, wrinkles, wet tired eyes, real eyelids, far more lifelike than anything around it, no feature exaggerated. Every colour is laid on in thick visible oil brushstrokes.
  ```

  Then a ~150-word light block per scene (*time + weather → one key light with direction → bounded
  practicals → value structure → warm/cold pair*). Jack: *"keep the real-skin faces"*. Name the crowd's
  mix person by person ("young and old, men and women, Black, white and South Asian"); never write
  "bakery" (it prints the word). 16:9, NB2, ×2. Picks per scene and the storyboard:
  [`songs/mv-speakeasy-mint/storyboard.md`](./songs/mv-speakeasy-mint/storyboard.md).
  Prompt rules learned on the K3a cut (2026-10-25/26):
  - Never name a show, game or artist; write traits only. **Check the caricatures in every frame.**
  - Real skin only holds when the face is large in frame; put the face-scope line on every prompt.
  - Real-skin faces plus a bare demographic summon a celebrity likeness: always give specific ordinary
    features.
  - Never write a shop word ("bakery" prints itself); print styles invent text, so ask for blank margins.
  - "Every face turned towards X" stops crowds staring at the camera.
  - Describe remains, not states (the candle: "a flat puddle of wax with a tiny drowning flame").
  - The mayor: always paste the full line (tall, skinny, bowler, gold chain); a bare "the mayor" gets a
    French sash, "top hat" summons the Monopoly man.
  - The band: gangsters in pinstripes ("mixed band" failed 12/12).
  - "1930s" wording on the press faces summoned a mascot lookalike: "simple faces painted on their sides".
- **Music video, "The Speakeasy Mint" — ALT cut** — **EXPLORING** (Jack, 2026-10-28; Flow project `706836d3`).
  A realistic prohibition-era world with exaggerated cinematic light and colour, and one psychedelic "layer" per
  scene laid over a real base. Settings change through transitions (e.g. fire into fire). Lynch-style odd vantages.
  Jack said on 2026-10-28 that most of the film "looks like ai slop", so scene 1 is being redone as a sealed round (internet research only), in
  `songs/mv-speakeasy-mint-alt/cleanroom/`. Nothing is locked yet.
  **2026-10-29:** Jack loved the clean-room stills (*"i love this new style"*). All 33 scenes now have clean-room stills
  and clips (Premiere sequence `Speakeasy Mint ALT cleanroom 1`). The look that worked:
  - Dry streets, not wet gloss.
  - One motivated light.
  - Odd vantages.
  - A different physical psychedelic layer per scene, coming from an object in the shot.
  - Each clip ending on something that cuts into the next scene.
  Engine notes: [`../../google-flow/2026-10-29-clean-room-sweep.md`](../../google-flow/2026-10-29-clean-room-sweep.md).
  What has held so far (record: [`songs/mv-speakeasy-mint-alt/picks.md`](./songs/mv-speakeasy-mint-alt/picks.md)):
  - Lead that killed the cream baked-in borders that "photograph" caused (0/44): `A frame from a feature film set in the 1920s, shot on grainy 35mm colour film, the picture filling the frame edge to edge.`
  - Name the physical cause of a layer, never "psychedelic / trippy / neon".
  - US cops wear peaked caps, not helmets. Keep "1920s" on every vehicle in a motion prompt.
  - Cast through the 10 Flow Characters plus their portrait as a reference: "dressed exactly as in his portrait reference" ([`cast.md`](./songs/mv-speakeasy-mint-alt/cast.md)).

## History

- **Round 1 and 2 look tests** (6 Oct): the four looks below tried on scene 9; two crowds holding red and
  blue cards *"looks AI like"* (Jack). Round 3, the protest made real from seven press photographs, gave
  the chosen still. All in [`look-tests.md`](./look-tests.md).
- **First still pass** (news-agency camera, warm lamp plus cool daylight in every frame) read as AI:
  everyone at standing height, two lights every time, nothing withheld. The second pass fixed it.
  Its camera sentence and close, verbatim (record only): `A news agency photograph, shot on a Canon EOS R3
  with a [lens] from [a place a person could stand] at [time].` … `The picture is slightly underexposed and
  muted: stone grey, black and navy, with small touches of red and blue the only strong colour. Nobody is
  aware of the camera. 16:9.`
- **The grey colour lock and "one light, no fill" (6–8 Oct 2026) — SUPERSEDED 9 Oct 2026** by the
  cut-8 colour rules (Jack on cut 7: *"a tad too grey… there should be more colour"*). Verbatim, for the
  record only — do not paste:
  `Muted colour: stone grey, black and navy, with small touches of red and blue the only strong colour.`
  · `One light source only, no fill:` + one named source, different in every scene. In those passes the
  eleven suits were "the only black in a grey street".
- **The model town** (cuts 1–3) — the garage plan on a cardboard model; Jack: *"the model house arent
  working… looks terrible"*. Out from cut 5.
- **The old grey look** — the standoff scene was cut whole at cut 9 partly because it was *"the old grey
  look"* ([`review-cut8.md`](./review-cut8.md)).
- **Music video style rounds** — 1930s rubber-hose cartoon brief → T sweep (red moon kept) → realism sweep
  (Jack picked R5a, real-skin faces) → K sweep (K3a) → "K3a lit".

### The suggestion board (6 October 2026, before the choice)

*Kept as written. Asked for by Jack, 6 October 2026: "suggest cinematic realistic artistic styles for
the images/video we make out of this… I'm thinking maybe like Heat or something." None of the four was
chosen.*

**Suggestions only.** When a look is picked, each shot still goes through `shot-craft` and then
`flow-prompt`, one at a time.

### Two things to know first

- **The generator follows a described camera, not a film's name.** We never put a film or a
  person in a prompt. So every look below is written as a recipe: the camera, the lens, the film
  stock, where the light comes from, and the colours.
- **Asking for "cinematic" gives the standard AI picture:** teal and orange, haze, everything
  blurred behind the subject. Each recipe exists to avoid that.

### Four looks

#### A. Cold money — the Heat look

- **Ancestors:** Heat (1995), Michael Clayton (2007).
- **Camera:** very wide 2.39 frame, the squeezed-lens kind that stretches lights sideways. A
  standard lens up close and a long lens from far away.
- **Light:** blue dusk and orange street lamps. Lamps and windows visible in the frame.
- **Colour:** steel blue-green, clean whites, pools of orange.
- **How Heat got its blue:** film made for indoor lamps was shot outdoors with no correcting
  filter, which turns daylight blue-green while whites stay clean.
- **What it gives us:** eleven suits that look dangerous and expensive. It makes the crew a
  proper heist crew, which is what makes them funny.
- **What it costs:** blue night with orange lamps sits right beside the AI default, so it needs
  the most care. It also fights a greasy spoon at nine in the morning.

#### B. Grey town — the observer look

- **Ancestors:** Ken Loach's recent films as shot by Robbie Ryan, Widows (2018), Dog Day
  Afternoon (1975).
- **Camera:** ordinary 35mm film, a longish lens on a tripod, watching from across the street.
  Pans only. Never hand-held.
- **Light:** grey overcast, lit from behind, never from the front. Indoors, the room's own strip
  lights plus one brighter window.
- **Colour:** wet slate, brick, nicotine cream. The only strong colours are police hi-vis yellow
  and the red and blue of the marches.
- **What it gives us:** the declining town, honestly, and a crowd that looks real. It is the
  picture language our reader already knows.
- **What it costs:** on its own it looks like a drama, not a heist.

#### C. Black suits, white walls — the Reservoir Dogs look

- **Ancestors:** Reservoir Dogs (1992), the vault in Ocean's Eleven (2001).
- **Camera:** very slow daylight film, a wide lens, everything sharp from front to back, almost
  no grain.
- **Light:** hard light through windows onto pale walls.
- **Colour:** black, white, and one red that is very red.
- **What it gives us:** the suits pop. The most recognisable heist picture there is.
- **What it costs:** it needs hard sun, which is not an English bank holiday.

#### D. Deadpan tableau — the locked-camera look

- **Ancestors:** Roy Andersson's films, with a little of Succession.
- **Camera:** a wide lens that never moves. Whole bodies in the frame. Everything sharp.
- **Light:** soft and flat from above, hardly any shadow.
- **Colour:** washed green-grey and beige.
- **What it gives us:** comedy from a camera that refuses to react. Eleven people lifting their
  feet for a hoover is funnier from across the room.
- **What it costs:** flat even light is exactly what looks like AI, or like a broken file,
  unless one part of the frame is clearly brighter.

### My recommendation: two looks, one for each side

**Look A for the crew. Look B for Denise and the street.**

- **Why two:** the story is about two groups of people living in the same town with different
  money. Giving each its own picture says that without a word. There is a precedent: Inside Man
  (2006) shot one strand of its story on different film on purpose.
- **Crew scenes in the cold look:** the garage, the recruiting, the night before, the vault,
  the fountain.
- **Denise's scenes in the grey look:** the café, the walk to work, the march, the staff room.
- **Where they meet:** the walk down the gap (scene 9) and the hoover (scene 10). The crew
  brings its blue into her grey. That is where the film should look strangest.
- **The camera barely moves,** borrowed from look D, for every shot of the eleven together.
  It suits the comedy and it suits how we make clips.
- **Heat without the night:** Heat's most famous sequence is a street shootout in hard
  daylight, shot from far away on long lenses. The walk down the gap can be that: a long lens
  that stacks the two crowds up behind the suits.

### How the look sits on each scene

| Scene | Look | The light comes from |
| --- | --- | --- |
| 1 and 14, the café | B | A steamed-up front window. Strip lights overhead |
| 2, the spoiler | B | Overcast sky, behind Denise |
| 3, getting out | A | One tall committee-room window |
| 4, the recruiting | A | A different single source each time: pool, print hall, make-up mirror |
| 5 and 6, the garage | A | One bare bulb over the model |
| 7, the night before | A, hand-held | Fairy lights and the marquee's own lamps |
| 8, the march | B | Overcast sky. Hi-vis yellow is the brightest thing in frame |
| 9, the walk down the gap | A and B together | Overcast, long lens, the suits the only black in a grey street |
| 10, the hoover | A and B together | The bank's strip lights. Denise's door is the bright part |
| 11, the vault | A | The vault's own cold strip lights on steel |
| 12, the standoff, and Denise's count | A, then B | The staff-room window with the SOLD sign across the road |
| 13, the fountain | A | Blue dusk, one orange precinct lamp |

### Rules from our own toolkit that apply to any look

From [`docs/cinematography/`](../../cinematography/README.md):

- **Every wide shot of the crew shows a cost:** shut shops, Denise small in the background, an
  empty saucer. Eleven sharp suits in a clean frame looks like an advert for them.
- **Every frame names where its light comes from.**
- **One part of every dark frame is clearly brighter than the rest,** or it reads as a broken
  file.
- **Something specific to this town in every frame.** Generic is what looks like AI.
- **Something in the foreground.** A barrier, a sauce bottle, the back of a head.

### Limits of the tools

- **Flow video is 16:9 or 9:16 only.** The very wide Heat frame is not available for clips.
  The route is to frame the action in the middle band of 16:9 and crop to 2.39 in Premiere.
- **Stills can be made at 21:9.**
- **Stretched-lens flares:** asking for them tends to put blue streaks on everything. From
  memory, not sourced. Suggestion: do not ask.
- **Snap zooms** (the Succession trick) are hard to get from a still turned into a clip.
  Premiere can do them afterwards.

### How to choose

A small test, not a debate:

1. Pick one scene that has both sides in it. **Scene 9, the walk down the gap,** is the obvious
   one.
2. Make that one frame in each of the four looks. One prompt at a time, Nano Banana 2, reviewed
   in Flow.
3. Pick by eye.

### The research behind it

One web pass by a research agent, 6 October 2026. **Read, not tested.** [S] the page was opened
(through a tool that summarises the page, so wording is not checked letter for letter);
[snippet] a search summary only; [memory] not sourced.

- **Heat:** 35mm with squeezed (anamorphic) lenses, 2.39 frame, one fast indoor-balanced film
  stock throughout, shot in daylight uncorrected for the blue-green. Night street lighting was
  coloured to match the orange street lamps. The diner scene used two cameras at once. [S]
  [American Cinematographer](https://theasc.com/article/hot-set-shooting-heat/)
- **Reservoir Dogs:** very slow daylight film (50 speed), hard light from overhead and through
  windows, a very wide lens indoors and a very long lens for the walk. Red "really, really red",
  black "black as hell". [S]
  [American Cinematographer](https://theasc.com/articles/flashback-reservoir-dogs)
- **Ocean's Eleven:** each place has its own colour: warm casino, electric-blue machine room,
  white and steel vault. Light bulbs in the ceilings were swapped for brighter ones so the
  rooms could light themselves. [S]
  [American Cinematographer](https://theasc.com/article/oceans-eleven-smooth-operators/)
- **Loach and Robbie Ryan:** 35mm, tripod and pans only, no light from the front, light through
  windows, modelled on documentary still photographs. [S]
  [Kodak](https://www.kodak.com/en/motion/blog-post/the-old-oak/)
- **Widows:** 35mm, one camera, rich but not saturated, frames shot through glass with
  reflections. [S] [Kodak](https://www.kodak.com/en/motion/blog-post/widows/)
- **Succession:** 35mm rated to give "slight milkiness to the blacks", long zooms, a
  photojournalist's distance. [S] [Kodak](https://www.kodak.com/en/motion/blog-post/succession/)
- **Dog Day Afternoon:** no added light; the bank's own strip lights. [snippet]
- **Inside Man:** a different film stock and processing for the interrogations. [snippet]
- **Roy Andersson:** locked camera, wide lens, flat shadowless light, washed colour. [snippet]
- **Killing Zoe's look, The Thick of It, Four Lions, and how British protest photographs look:**
  nothing sourced. [memory]
- **Long lenses make crowds look denser.** [snippet]
- **Google's own advice:** describe the shot in a paragraph, name the lens and the light source,
  say what is there and not what is absent. [S]
  [Google's Veo guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Aspect ratios:** already recorded in [`docs/google-flow/`](../../google-flow/README.md).
