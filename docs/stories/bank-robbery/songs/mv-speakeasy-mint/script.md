# The Speakeasy Mint — script (draft 1, 2026-10-25)

Jack, 2026-10-25: *"lets do this style [K3a] but change the scenes, as in the setting, dont worry we will do this
later once we have the still ready for each scene, so lets write the script."*

**The style is locked: K3a** (`d81d7f7a`, Flow project `dedd295f`). Sitcom figures with real-skin faces, every flat
colour laid on in thick oil brushstrokes, wet cobbles, the small red moon. Record: `storyboard.md` → "K sweep".
**The settings now change scene by scene.** The cross-section building is one setting among many, not the whole film.
The stills for each scene come next, one scene at a time.

**Words:** Kai's lyrics, word for word (standing rule: always Kai's). Source: `../bank-robbery-jack.md`, Round VB
lyrics block. The song take is not picked yet, so there are no timings; scenes are cut to the lyric lines, and get
re-timed to Suno's word alignment once a take is chosen.

## The spine (story-craft, build mode)

- **The sentence:** printing money makes whoever holds it first richer and everyone paid in it poorer, and the fight
  on the street is what stops anyone looking down.
- **Anti-theme (what the mayor says):** the money's for everyone; your problem is the other lot.
- **The costed object: the loaf.** It costs more every time we see it: a coin, two coins, a pay packet, a wheelbarrow.
  It ends as a cake. Grandma's candle is the second object: it burns lower each time we visit her.
- **Hero:** the street (the worker, grandma, the two crowds). **Chooser and beneficiary, on screen every time we go
  down:** the mayor and the gangsters who own the press.
- **The pub line:** *own the printer and you don't fear winter* (Kai's own line; it lands on the warm basement and the
  frozen attic in one cut).
- **Shape:** verse 1 sets up the street and where the money goes (but nobody knows); choruses 1–2 are the first drop
  into the Mint (therefore: that's where); verse 2 is the distraction (but they fight each other); the money shot is
  the reversal (the leaders dance together downstairs); choruses 3–4 are the raid (but the police leave with bread);
  verse 3 is the cost (the furnace, the wealth gap); the ending is the turn (therefore they look down together).
- **The closing image answers the opening:** we open on the red moon over a city at war with itself; we close on the
  red moon over an empty street, because everyone has gone downstairs.

## Locked from the storyboard (Jack, 2026-10-25)

The bakery front · the password "quantitative easing" in a speech bubble · the raid (presses flip into bread ovens,
cops leave with a loaf) · the left and right leaders dancing with the mayor downstairs · the furnace heats the basement
only, grandma freezes in the attic · the band = gangsters in pinstripes · the mayor = tall, skinny, bowler hat, gold
chain · 🔴 the caricature check on every frame (`storyboard.md`).

## Scenes

One thing moves per clip; camera moves are done in Premiere over the still (`docs/video-fx/hybrid-method.md`). All
text (bubbles, chalkboards, stamps, the end card) goes on in ffmpeg, never asked of the model. **Gags marked ✏️ are my
proposals; Jack writes the jokes and can swap any of them.**

| # | Lyric | Setting | What we see | What moves |
| --- | --- | --- | --- | --- |
| 1 | *(Intro) Robbery!* | **The city skyline at night** | Rooftops and chimneys under the small red moon; far below, a siren's light sweeps the brick. Nobody in frame yet | The siren light |
| 2 | *They say, ya can't make money from a tree / let's see, each day, make hay, not free* | **The bakery kitchen, 4 a.m.** | Bakers in vests knead dough by oven light, flour in the air, sweat on real-skinned faces. "Earning that dough", literally | Arms kneading |
| 3 | *work and get paid though, earning that dough / but where does it go? nobody knows!* | **The bakery back door, dawn** | The foreman hands one baker a thin brown pay packet. ✏️ He tips it out: three coins and a moth | The coins dropping |
| 4 | *means of production means a reduction / standards bleeding, land-lords needing* | **A tenement stairwell** | A landlord in a fur collar holds out his palm at the top of the stairs; the baker climbs towards him, packet in hand. Peeling paint, one bare bulb | The baker climbing |
| 5 | *quantative easing,* | **The back stairs: a plain door with a slot** | A gangster in pinstripes knocks. The slot opens: two eyes. Speech bubble **"QUANTITATIVE EASING"** (ffmpeg) | The slot sliding open |
| 6 | *grandma FREEEEEEEZING!* | **Grandma's attic** | Frost on everything, icicles on the beams, breath steaming, one candle. The held note lands on her face | Her breath; the candle flame |
| 7 | *stimulus checks are next. Get wrecked!* | **The mayor's balcony over the square** | The mayor tosses a handful of envelopes to the crowd below; the wind blows them straight into a storm drain | Envelopes falling |
| 8 | *rent seeking?... I'm just about eating / sorry, did I interrupt your meeting?* | **A smoky back room with a long table** | Gangsters and the mayor mid-feast (whole hams, champagne). The door bursts open: the baker, holding one small loaf. Everyone freezes, forks in the air | Nothing: a freeze-frame gag, the camera pushes in on the baker |
| 9 | *remember kids, the Fed is not your friend! / it prints all the dollars that the government spends* | **A 1930s schoolroom** | A teacher at the blackboard; on it, a chalk drawing of a printing press with a smiling face (chalk lines added in ffmpeg). Adults at the desks, squeezed into children's chairs ✏️ | The teacher's pointer tapping |
| 10 | *this fiat system is insistent / on debts existence, sooooo* | **A marble bank lobby** | A worker in his only suit sits at a loan desk; the clerk's pen hovers. Behind them, gangsters walk straight past the guard into the vault with sacks | The gangsters walking (in the background, small) |
| 11 | *don't be hating on the credit rating / or have resistance to the facts I'm stating* | **Same lobby, close** | The clerk brings down a rubber stamp: **DENIED** (ffmpeg) on the worker's form | The stamp coming down |
| 12 | **Chorus 1** *Robbery, robbery! / Call the police, it's a robbery! / Debasement!… in da basement! / Printer is burrrrning…* | **The building in cross-section: the first drop** | Down through the bakery floor into the Mint: rows of presses, sheets of banknotes, the band, notes like confetti, the mayor dancing | The drop (Premiere move over a tall still); the presses throwing notes |
| 13 | **Chorus 2** (same words) | **The Mint, close on the biggest press** | The press glowing red hot, spitting notes; the mayor feeds it with a coal shovel | The shovel |
| 14 | *Stacks and stacks of elastic cash / distracted by a dispraxic flash* | **The town square, a stage** | The mayor does a magician's flash (smoke, a bright pop) on a bandstand; behind the smoke, gangsters carry sacks out of the bank | The smoke puff |
| 15 | *mob, angry at their shitty little job / the right and the left both witness the theft* | **The street outside the bakery** | Red crowd and blue crowd, banners and scarves, shoving under the street lamp; police cars nose to nose | The shove |
| 16 | *blaming each other is a sick little cover / institutional, dilutional, the usual* | **Close in the crowd** | A red-scarf man and a blue-scarf man nose to nose, shouting; both have the same thin pay packet in their back pockets ✏️ | The two mouths shouting (no speech, music only) |
| 17 | *distraction IS the attraction / the intention is tension between the factions* | **The cross-section: the money shot 🔑** | Upstairs the crowds fight; directly beneath, the red leader and the blue leader dance arm in arm with the mayor | The dancers (camera locked; the cut-away does the work) |
| 18 | *divide and conquer, just look at the hand / It's not ya standard, propaganda, worth a couple grand-ahh* | **A radio studio** | The mayor at a big chrome microphone, an ON AIR lamp lit, reading from a script with a grin | The ON AIR lamp flicking on |
| 19 | *it is, state, level, manipulation / it is the devil, with a radio station* | **Kitchens across the city** | Three windows in a row, a radio in each: the red family, the blue family, grandma. All leaning in to the same voice | The radios' dial lights |
| 20 | *stack up the vaults like a wheelbarrow / risk of default is really rather narrow* | **The vault** | Gangsters wheel barrows of rubber-banded stacks up a plank onto a mountain of money | The wheelbarrow |
| 21 | *Biggie said waaaay back in ninety seven / don't get high off your own supply* | **The vault, top of the pile** | The mayor lies back on the money mountain, gold chain on his chest, eyes glazed, a banknote over his face like a newspaper on a beach | The note lifting on his breath |
| 22 | **Chorus 3** *Robbery, robbery! / Call the police…* | **The bakery front → the Mint: the raid** | Two cops knock at the bakery; downstairs a gangster yanks a huge lever; every press flips round into a bread oven; the band are bakers in white hats | The presses flipping (Omni can't do a state change cleanly: two stills, before and after, cut on the lever) |
| 23 | **Chorus 4** (same words) | **The bakery doorway** | The cops leave, each with a free loaf under his arm, tipping their hats. Behind them, the "oven" door glows green ✏️ | The cops walking off |
| 24 | *(Break: riff and stomps)* | **The bottom: the furnace** | The last drop, through the Mint's floor: a man in a vest shovels banknotes into a roaring furnace. Its heating pipe climbs the wall and stops dead at the Mint's ceiling | The fire |
| 25 | *You know the real star is Pablo Escobar, / who has elastic bands not plastic hands,* | **The counting room** | Rubber-banded stacks to the ceiling; rats nibbling the bundles (the rats eat money; they never stand for people) | A rat |
| 26 | *stacking up the cash by the grands / standard plans are for the working man* | **The bakery counter** | The baker, back at work, buys a loaf with his whole pay packet; the price chalked on the board above (ffmpeg) is rubbed out and written higher as he watches | The chalk hand |
| 27 | *and this right here is a next level scam / ill gotten gains, no need to explain* | **A rowing boat on a black river** | ✏️ "Bail and out": the mayor sits in a sinking rowing boat, bailing it out with a bucket of banknotes | The bucket |
| 28 | *"bail" and "out", will never mean the same / own the printer and you don't fear winter* | **Split: the warm Mint / the frozen attic** | One cut: the gangsters in shirt-sleeves, sweating in furnace heat; grandma, candle burnt down to a stub, frost on her eyelashes | The candle guttering |
| 29 | *crime is asset inflation, passive creation; / of a wealth gap that drives the situation* | **The whole cross-section** | One long ride up the building, gold at the bottom to ice at the top: the wealth gap as height | The ride (Premiere over the tall still) |
| 30 | *working people get paid in money, so it's not very funny / when you print more and expect them not to worry* | **The bakery queue** | A long queue in the snow; each person holds the price of one loaf: a coin, a fistful, a bag, a wheelbarrow at the back | The queue shuffling forward one step |
| 31 | *hungry people, feed a revolution, / then it's retribution, perhaps some execution* | **The street** | The two crowds stop shoving. Both turn, slowly, and look down at the trapdoor behind the bakery counter. Then they pour down the back stairs together | The turn (heads only) |
| 32 | *it's time to give, not just to take / but for heaven's sake, don't just eat cake* | **The Mint, the end of the line** | The mayor backed against the furnace, the crowd filling the room, holds out a tiered cake on a silver tray. Iris out | The tray trembling |
| 33 | *(Outro) Robbery!* | **The city skyline at night (bookend)** | Scene 1's frame again: the red moon over the rooftops, but the street below is empty. Everyone's downstairs. End card (ffmpeg): *"She never said it, by the way."* Then the BadCode logo | The siren light, now still |

## Notes for the stills round

- **Faces:** the K3a real-skin faces need size, so most scenes are mid shots or closer (scenes 3, 6, 8, 16, 21, 28).
  The cross-section scenes (12, 17, 29) are wide on purpose.
- **Recurring people** (the baker, grandma, the mayor, the landlord, the teacher) should become Flow Characters
  once each has a still Jack likes, so the face holds across scenes (`new-image` → casting).
- **Crowds:** name the mix every time ("young and old, men and women, Black, white and South Asian"); "mixed" alone
  gave all white men. Team colour on scarves and banners, never on people.
- **Press faces:** "simple faces painted on their sides". The "cheerful 1930s cartoon faces" wording summoned a
  game-mascot lookalike twice.
- **Omni can't reach a state** (open, flip, arrive): scenes 5, 11 and 22 are two stills cut on the action, or the
  move is already under way in frame one (`docs/google-flow/README.md`).
- **The end-card fact:** "let them eat cake" is not something Marie Antoinette is recorded saying; it traces back to
  Rousseau's *Confessions*, written when she was a child. Check the wording before it ships.

## Rows run (story-craft, build mode)

Ran: the sentence + anti-theme + costed object (§1); the gates (hero, chooser, beneficiary on screen, pub line);
the spine (but/therefore, midpoint reversal = scene 17, lowest point = scene 28, closing image answers the opening);
one-thing-moves per scene. **Not run:** the full adversarial pass (`checklist.md`), the reader rules line by line
(`the-reader.md`), and timing against a song take (none picked).

## Scene 1 stills — round 1 (2026-10-25)

**Shot spec (`shot-craft`, design mode):**
- **For:** the film's first promise. This city is about to go off, and something is watching (the red moon, BadCode's
  mark). It opens the bookend; scene 33 repeats the frame with the street empty.
- **Cost in frame:** a sign of the cold and the poor (frozen washing, a lit attic, money in a drain), so the skyline
  isn't a postcard.
- **Light, all in the world:** the red moon, a police light sweeping red and blue, one warm window. Saturated colour
  named per place (`docs/google-flow/` rule 2).
- **Moves later (Omni, camera locked):** the siren light only.
- **Withheld:** who is in trouble.

**Anti-slop for this shot (web pass 2026-10-25 + repo):** the generic AI night city is rain-slick streets, neon signs,
magenta-and-cyan, fog and a lone figure against a dense backdrop ([Luma](https://lumalabs.ai/news/cyberpunk-ai-prompts),
[zsky](https://zsky.ai/blog/ai-cyberpunk-art-prompts.html)) `[vendor]`; the fix is specificity: a named vantage, named
materials, one named source. So: **no neon** (it also prints sign text), a 1930s city of brick, chimneys and water towers,
a vantage that isn't eye level, a foreground object, and the K3a brushwork carrying the texture.

**Variety mode, declared variable: where the camera stands.** Four ideas:

| # | Idea | Why |
| --- | --- | --- |
| 1a | **On the roofs:** frozen washing in the foreground, the red moon between chimneys, the siren far below | Cost in the foreground; the moon as the only warm-red thing in the sky |
| 1b | **Straight down into the street canyon:** the moon seen only as a reflection in a puddle | The moon withheld and found; the siren paints the walls |
| 1c | **From the gutter:** banknotes caught in a storm drain, looking up at a slit of sky | Plants scene 7 (checks down the drain) and the money in the first frame |
| 1d | **From across the river:** the skyline small, one tall chimney smoking, the bakery's basement glowing green | Plants the Mint: the only green in the city, before we know why |

**Style lead (K3a, identical in all four):** `A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes.`

**1a:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. A 1930s American city at night, seen from among its rooftops, low behind a washing line of grey shirts frozen stiff in the near foreground. Brick chimney stacks and wooden water towers lean against a deep navy sky; a small, perfectly round, solid red moon sits between two chimneys. Far below, down a gap between the buildings, a police car's light throws red and blue across wet brick. One attic window glows candle yellow. Plain margins with no writing. Thanks.

**1b:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. Looking straight down from a rooftop into a narrow 1930s American street at night: soot-black brick walls fall away to wet cobbles at the bottom, where a police car's light throws red and blue up the walls. In a puddle on the cobbles, the only sign of the sky: the reflection of a small, perfectly round, solid red moon. One window halfway down glows candle yellow. Plain margins with no writing. Thanks.

**1c:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. Seen from the gutter of a 1930s American street at night: in the near foreground a rusty iron storm drain with a few green banknotes caught in its bars. Behind it, tenement walls of soot-black brick rise steeply to a thin slit of deep navy sky holding a small, perfectly round, solid red moon. A police car's light, out of sight, throws red and blue across the brick. Plain margins with no writing. Thanks.

**1d:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. A 1930s American city at night seen from across a black river, the skyline small and long: brick tenements, water towers, one tall factory chimney trailing grey smoke, a small, perfectly round, solid red moon low over the roofs. In the middle of the skyline one plain bakery building, its basement windows glowing emerald green, the only green in the city. A police car's light flickers red and blue on the far embankment. Plain margins with no writing. Thanks.

### Scene 1 round 1 results (2026-10-25)

NB2, 9:16, 2 each, project `dedd295f`. All four ran first time; no invented text; the red moon landed 8 of 8.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 1a | On the roofs | d91c9dc3 · bf28028f | ⭐ The frozen washing line across the foreground carries the cold; water towers, chimneys, the moon between them; the police car tiny below. 1a is the fuller frame, 1b has icicles on the shirts |
| 1b | Straight down, the moon in a puddle | 0221560c · 5f104507 | ⭐ **The idea landed in both:** the red moon exists only as a reflection on the cobbles; the siren paints the walls red and blue. The most graphic and the most "BadCode" (the mark found, not shown) |
| 1c | From the gutter | c28a1409 · 12fa996c | ⭐ Banknotes in a rusty drain in the foreground, tenements rising to a slit of sky with the moon; siren light on the brick. 1b has the clearer notes. Plants scene 7 |
| 1d | Across the river | c77c958d · a8d5d1dc | 🟡 The green basement is the only green, as asked, but the frame is mostly black water and the city is a thin strip: it reads as an empty file at phone size (`symptoms.md`: near-black needs a bigger bright region). 1a is the better of the two |

**Style:** the brushwork held in all eight; with no people in frame it reads as a painted cartoon background rather
than the sitcom look, which is right for an establishing shot (the people bring the sitcom look back).
**For Omni (inferred):** 1b and 1c have the siren light on big brick surfaces, so the one moving thing has room to move.

### Scene 1 round 2: 1b in 16:9 (Jack, 2026-10-25)

Jack picked **1b-b (`5f104507`)**, the moon in the puddle, and asked for it again in **16:9**.

**Engine:** the Flow picker reads **Nano Banana 2.1** when the tool asks for "Nano Banana 2" (seen on screen this
session), so these run on 2.1. Google: 2.1 is an update to NB2 with better quality and prompt adherence
([ai.google.dev](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1)) `[official]`. Rendering on a
different canvas changes the composition, so the prompt is rephrased for the shape, not just re-run
([zilliz](https://zilliz.com/ai-faq/how-does-nano-banana-2-handle-aspect-ratios-like-169-or-916)) `[single source]`.

**The design problem (`shot-craft`):** a straight-down street canyon is a tall shape. In a wide frame it leaves dead
space on both sides unless the frame gains lateral things (pavements, cross streets, repeated fire escapes); a slight
tilt off true overhead adds depth to a wide frame ([Videomaker](https://www.videomaker.com/article/c10/12985-composition-tips-for-169),
[Morphic](https://morphic.com/es/ai-glossary/Birds-Eye-View)) `[practitioner]`. Everything else stays as 1b-b: the
moon only in the puddle, one candle window, the siren painting the walls, the K3a brushwork.

**Variable: how the wide frame is filled.**

| # | Idea |
| --- | --- |
| W1 | **Control:** 1b's prompt unchanged, 16:9 |
| W2 | **The street runs across the frame:** true overhead, roof edges along the top and bottom, fire escapes repeating left to right |
| W3 | **Near overhead, a slight tilt:** from a roof edge, the street running away diagonally into the distance |
| W4 | **A crossroads from above:** two narrow streets cross; the police car at the corner, the puddle in one arm |

**W1** = 1b's prompt verbatim.

**W2:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. Looking straight down from high above onto a narrow 1930s American street at night that runs from the left edge of the frame to the right: the flat rooftops and gutters of the buildings line the top and bottom edges, iron fire escapes repeat along the soot-black brick walls, and wet cobbles run along the middle. A police car parked on the cobbles throws red and blue up the walls. In a puddle on the cobbles, the only sign of the sky: the reflection of a small, perfectly round, solid red moon. One window glows candle yellow. Plain margins with no writing. Thanks.

**W3:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. Looking steeply down from the edge of a rooftop into a narrow 1930s American street at night, the street running away diagonally into the distance: soot-black brick walls and iron fire escapes on both sides, wet cobbles below, where a police car's light throws red and blue up the walls. In a puddle on the cobbles, the only sign of the sky: the reflection of a small, perfectly round, solid red moon. One window glows candle yellow. Plain margins with no writing. Thanks.

**W4:**

> A prime-time adult animated sitcom background: flat colours and slightly wobbly black outlines, every colour laid on with thick visible oil brushstrokes. Looking straight down from high above onto a crossroads of two narrow 1930s American streets at night: four blocks of flat rooftops and soot-black brick fill the corners, wet cobbles form the cross between them. A police car stopped at the junction throws red and blue up the walls. In a puddle in one of the streets, the only sign of the sky: the reflection of a small, perfectly round, solid red moon. One window glows candle yellow. Plain margins with no writing. Thanks.

#### Round 2 results (2026-10-25)

16:9, 2 each, project `dedd295f` (W3 failed once with "Failed · You have not been charged", refresh-and-retry worked).
The moon-in-the-puddle idea held in 8 of 8; no invented text.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| W1 | Control | 2a01d47e · de40af85 | ⭐ **1a is 1b-b in 16:9:** the walls converge into the canyon, the candle window, the car, the moon in the puddle. The engine filled the width with the walls themselves. 1b tilts so the street runs along the bottom |
| W2 | Street across the frame | 2cb33584 · 704a99af | 🟡 Clean and graphic, but flat and symmetrical, like a game map (the symmetry tell). Least depth |
| W3 | Near overhead, a slight tilt | b0ebb799 · 5cbcf7a8 | ⭐ **3b: the most depth:** a rusty roof parapet and pipes in the foreground, the street running away with the police car, the moon in the puddle. Room for a slow push in Premiere |
| W4 | Crossroads | b6785061 · a2bc25eb | 🟡 A neat map of four blocks; loses the canyon's mood |

**Shortlist:** W1a (the faithful 16:9 of Jack's pick), W3b (the deeper, more cinematic version).

**✅ Scene 1 PICKED (Jack, 2026-10-25): W3b (`5cbcf7a8`)**, "this one is cool". The rooftop parapet, the street
running away, the police car, the red moon in the puddle. 16:9.

## Scene 2 stills — round 1 (2026-10-25)

*They say, ya can't make money from a tree / let's see, each day, make hay, not free* — **the bakery kitchen, 4 a.m.**

**Shot spec (`shot-craft`):**
- **For:** the first people. Work before dawn: "earning that dough", literally. The film's hero is labour, so we
  meet it tired.
- **Cost in frame:** sweat, flour in the stubble, a burn on a forearm, the dark outside the window.
- **Light:** two sources, two colours: the **orange mouth of the bread oven** and **one bare cold bulb**.
- **Faces:** K3a's real skin needs size, so three of four candidates are mid shot or closer.
- **Moves later (Omni):** the kneading. The hands start already on the dough (Omni can use a prop already in
  contact, not pick one up).
- **Strange angles, one light** (Jack's Bank Robbery rule, 2026-10-06: eye level looks like AI).
- **Cast:** name the mix (the crowd lesson): an older Black man, a young white woman, a middle-aged South Asian man.

**Variety mode, declared variable: where the camera is.**

| # | Idea |
| --- | --- |
| 2a | **Low across the table:** mounds of dough huge in the foreground, floury forearms pressing, faces above lit by the oven |
| 2b | **From inside the oven:** the oven mouth frames the bakers, loaves in the foreground (object point of view) |
| 2c | **High in the ceiling corner:** the whole cramped kitchen, flour sacks, the bulb, a dark window |
| 2d | **Close on one face:** the young woman wiping her brow with a floury wrist, sweat and flour on real skin |

**Style lead (K3a, identical in all four):** `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, flat colour and black outlines everywhere except the faces, which are rendered with startling real skin: pores, stubble, sweat, tired wet eyes. Every flat colour is laid on with thick visible oil brushstrokes.`

**2a:**

> [Style lead] A cramped 1930s bakery kitchen at four in the morning, seen from low across a long wooden table: big pale mounds of bread dough fill the near foreground. Behind them three bakers in sweat-stained vests knead hard, floury forearms pressing into the dough: an older Black man, a young white woman, a middle-aged South Asian man. The open mouth of a brick bread oven behind them throws hot orange light across their faces; one bare cold bulb hangs above. Flour hangs in the air. Plain margins with no writing. Thanks.

**2b:**

> [Style lead] Seen from inside a brick bread oven at four in the morning, looking out through its arched mouth: a row of loaves on the oven floor in the near foreground, glowing orange. Framed in the opening, a cramped 1930s bakery kitchen where three bakers in sweat-stained vests knead dough at a wooden table, squinting into the heat: an older Black man, a young white woman, a middle-aged South Asian man. Behind them one bare cold bulb and a black window. Plain margins with no writing. Thanks.

**2c:**

> [Style lead] A cramped 1930s bakery kitchen at four in the morning, seen from high in a corner of the ceiling: three bakers in sweat-stained vests knead dough at a long wooden table below, an older Black man, a young white woman, a middle-aged South Asian man. Flour sacks stacked against peeling walls, trays of rising loaves, one bare cold bulb on a cord close to the camera, a black window. The open brick oven throws hot orange light across the floor. Plain margins with no writing. Thanks.

**2d:**

> [Style lead] Close on a young white woman baker at four in the morning in a cramped 1930s bakery kitchen, wiping her brow with the back of a floury wrist, her other hand still pressing a mound of dough. Flour in her eyebrows, sweat on her temple, a small burn on her forearm, eyes half shut with tiredness. Hot orange light from the open bread oven on one side of her face, the cold blue-white of one bare bulb on the other. Behind her, out of focus, two more bakers kneading. Plain margins with no writing. Thanks.

### Scene 2 round 1 results (2026-10-25)

16:9, 2 each, project `dedd295f` (2b harvested from the page after a slow timeout). 2c and 2d were sent with **specific
features** for the bakers (heavy-set, shaved head, broken nose / skinny, ginger bun / big moustache), after 2a.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 2a | Low across the table | ca815247 · e61b09d8 | 🔴 **"An older Black man" with real-skin rendering came back as a near-likeness of a famous film actor, in 2 of 2.** Unusable. Otherwise strong: dough mounds, sweat, the oven glow |
| 2b | From inside the oven | fbbbcacc · c9257e6c | ⭐ for the framing (the brick arch, glowing loaves in the foreground, the bulb behind) · 🔴 the same actor likeness in both. Re-run with the new cast wording |
| 2c | High in the ceiling corner | 06c543ca · 314a6480 | ⭐ **2c-a:** the bulb swinging close to the camera, the open oven, peeling walls, flour sacks, the three bakers looking up; the faces are now ordinary people. 🟡 2c-b's older man still drifts towards the likeness |
| 2d | Close on one face | 7745180e · 18f2f484 | ⭐ **2d-a: the strongest:** her tired real-skin face, flour in her eyebrows, sweat, the burn on her forearm, the orange oven on one side and the cold bulb on the other. 🟡 Background bakers in chef's hats (generic); 2d-b prints "FLOUR" on a sack |

**🔴 Lesson:** real-skin rendering + a bare demographic ("an older Black man") pulls towards a famous face. Give every
person **specific, ordinary features** (build, hair, nose, a scar), never just age + ethnicity. Check every face for a
celebrity likeness before Jack sees it (rule zero's cousin: we never want a real person's face).

**Shortlist:** 2d-a, 2c-a; 2b's framing is worth a re-run with the new cast.

### Scene 2 — 2b round 2 (2026-10-26)

Jack, on 2b round 1 (the oven-mouth still): *"this one is great"*. 🔴 Its older baker is a near-likeness of a famous
film actor, so it can't ship as it is. Re-run with the same 2b prompt and specific features for the cast (heavy-set Black man in his
fifties, shaved head, broken nose, double chin / skinny young white woman, ginger bun, gap teeth / middle-aged South
Asian man, big drooping moustache, thick eyebrows, bald patch). NB2, 16:9, ×2, project `dedd295f`.

| # | Media | Verdict |
| --- | --- | --- |
| 2b-r2-a | 2afc56ec | 🟡 No likeness. Two bakers lean into the camera and stop kneading, and the faces went goggle-eyed cartoon (real skin mostly lost) |
| 2b-r2-b | c98067ae | ⭐ No likeness, all three kneading, the arch and loaves kept. 🟡 The faces are flatter and more cartoon than round 1. The real skin Jack liked is weaker |

**Lesson (inferred, one round):** the specific features fixed the likeness but pulled the faces back towards the cartoon.
The round-1 realism may have come from the same famous-face pull.

**✅ Scene 2 PICKED (Jack, 2026-10-26):** the 2b round-2 oven-mouth still: three bakers kneading, the arch, glowing loaves,
flames at both sides of the oven. Jack shared it as an image in chat. It looks like 2b-r2-b plus side flames, but its media id is
**not confirmed** (check the newest tiles in `dedd295f`). Jack: *"try and keep the style with the real skin faces, some
of them drift to completely cartoon"*, so from scene 3 every prompt carries a face-scope line (below).

## Scene 3 stills — round 1 (2026-10-26)

*work and get paid though, earning that dough / but where does it go? nobody knows!*: **the bakery back door, dawn.**
The baker paid is the heavy-set one from the scene 2 pick. ✏️ The gag (proposal): he tips the packet out, and three coins and a moth fall out.

**Face-scope line (new, after Jack's scene 2 note):** added straight after the K3a style lead in every prompt: `Only the
bodies, clothes and places are cartoon: every face in the frame, however small, is painted as real human skin with
wrinkles, pores, bags under the eyes and real eyelids, far more lifelike than anything around it, and no feature is
exaggerated.` ("no feature is exaggerated" was added from 3b on, after the 3a-a caricature fail.)

Variety mode, declared variable: where the camera is. NB2, 16:9, ×2, project `dedd295f`. Full prompts in the provenance cards.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 3a | Worm's-eye from the cobbles | a6e74911 · f7fad7a2 | ⭐ The gag reads (coins and moth falling, red moon, foreman leaving). 🔴 3a-a: the baker's lips are exaggerated, so it fails the caricature check. 🟡 Both have cartoon goggle eyes: the face line was beaten at full-figure size |
| 3b | Over the foreman's shoulder | 7b38a06c · 76894e2b | ⭐ **3b-b: the most real skin** (real eyes, sweat, flour in the vest). No gag in frame (the packet is unopened). 🟡 3b-a has cartoon eyes and an apron |
| 3c | Down from the fire escape | 5b714de1 · 9f84faa1 | 🔴 3c-a: the baker is drawn twice. 🟡 3c-b: good geography and the gag, but his face is small and goes cartoon |
| 3d | Close on the palm | 080c97bc · aa6656c7 | ⭐ **Both strong:** real-skin face large in frame, floury palm, three coins and a moth, foreman walking away, oven glow. 3d-b is frontal, 3d-a is a three-quarter view with the alley deeper |

**Lesson (one round):** real skin holds when the face is **large in frame** (3b, 3d) and drifts to cartoon when the
figure is small or full-length (3a, 3c), even with the face-scope line. For wide shots, plan a close-up to cut to,
or accept the drift. 🟡 Continuity: the baker grew a grey goatee in 3d (clean-shaven in scene 2).

**Shortlist:** 3d-a, 3d-b, 3b-b. Pick owed (Jack).

**✅ Scene 3 PICKED (Jack, 2026-10-26): 3a-b** (`f7fad7a2`), "this is cool". Worm's-eye from the cobbles: coins and the moth
falling, the red moon, the foreman glancing back. (Jack is happy with this one's cartoon eyes.)

## Scene 4 stills — round 1 (2026-10-26)

*means of production means a reduction / standards bleeding, land-lords needing*: **a tenement stairwell.** The
landlord in a fur collar holds out his palm at the top of the stairs; the baker (the same one as scene 3) climbs towards him with the pay packet.
Peeling paint, one bare bulb. Moves later: the baker climbing. Face-scope line on every prompt. New cast: the landlord
is a plump white man in his forties with slicked-back black hair, a thin pencil moustache, rosy jowls, a fur-collared
overcoat and gold rings.

| # | Idea |
| --- | --- |
| 4a | **Over the landlord's shoulder:** his ringed open palm huge in the foreground, the baker climbing below |
| 4b | **Worm's-eye from the foot of the stairs:** the baker's back climbing, the landlord at the top under the bulb, hand out |
| 4c | **Straight down the stairwell:** the baker on the stairs looking up, the landlord's palm reaching in from the frame edge |
| 4d | **Close, side-on, mid-climb:** the baker's tired face large in frame, the landlord's palm hovering just above |

### Scene 4 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 4a | Over the landlord's shoulder | 1e19ed0c · a8cef796 | ⭐ **4a-a:** the ringed palm huge in front, the baker climbing up into it, his face in real skin. 🟡 A white strip at the top-left edge (crop in Premiere). 🔴 4a-b: the landlord came out bald and the baker goggle-eyed |
| 4b | Worm's-eye from the foot of the stairs | 4c88a041 · 1cc44717 | ⭐ **4b-a: the clearest story:** the baker turns back on the stairs, and at the top the smiling landlord in fur (slicked hair, pencil moustache) holds his hand out. 🟡 It isn't really from the foot of the stairs; the baker looks back at us. 4b-b goes cartoon in profile |
| 4c | Straight down the stairwell | 2e123d9e · 8d6f8fe3 | ⭐ **The strongest graphic:** the square well spiralling into the dark, the ringed palm reaching in, the baker looking up. 4c-b has the bulb on its cord. The faces are smallish but hold |
| 4d | Close, side-on, mid-climb | 56978031 · 14520747 | ⭐ The most real skin (4d-b especially), the palm hanging above. 🟡 Continuity: he is in a T-shirt and apron, not the vest |

**Caricature check:** ✅ no exaggerated lips or teeth this round; the landlord is a plain plump villain. Likeness: no clear famous face that I can see in the close-ups, but this is unverified; Jack's eye on 4d.

**Shortlist:** 4c-b, 4b-a, 4a-a, 4d-b. Pick owed (Jack).

**✅ Scene 4 PICKED (Jack, 2026-10-26): 4b-b** (`1cc44717`). The smiling landlord in fur at the top of the stairs, hand out; the
baker in the foreground, turned to look at him, pay packet down by his side.

## Scene 5 stills — round 1 (2026-10-26)

*quantative easing,*: **the back stairs, a plain door with a slot.** A gangster in pinstripes knocks; the slot opens on
two eyes; the speech bubble **"QUANTITATIVE EASING"** goes on in ffmpeg, so every frame keeps empty wall for it. Cast:
the gangster is a short, wide man in his forties with a flattened nose, a scar through one eyebrow, a pinstripe suit
and a grey fedora. Face-scope line on every prompt.

| # | Idea |
| --- | --- |
| 5a | **From inside, through the slot:** the gangster's face fills the open slot, leaning in to whisper |
| 5b | **Extreme close on the slot:** two eyes in the dark gap, the gangster's raised knuckles at the frame edge |
| 5c | **Low from the foot of the back stairs:** the gangster at the door under a bulb, knocking, long shadow, empty wall |
| 5d | **Side-on two-shot:** the gangster's profile leaning into the slot, the eyes inches away, empty space above |

### Scene 5 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`. 🔴 **Four calls sent at once collided:** 5c timed out at 99% and never landed, and the
"5d" call came back with images of the 5c prompt (the steps and the knock). 5c and 5d were then re-run one at a time. **Send Flow
generations one at a time** (it matches the standing one-prompt-at-a-time rule).

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 5a | Through the slot from inside | 487066de · 0f078704 | ⭐ The gangster's real-skin face fills the bright slot, and the dark door around it is perfect for the bubble. 🟡 Reads more "tired detective" than gangster (no pinstripes visible); likeness unverified |
| 5b | Extreme close on the slot | 575fa62c · 78dd1a7b | ⭐ **5b-b:** real wrinkled eyes in the rusty slot, the cartoon pinstripe fist knocking, chipped green door. 🟡 5b-a has white strips at the edges |
| 5c | Low from the foot of the stairs | 1471a1cd · 7ab0840a | ⭐ 5c-b: clean geography (stairs, the bulb, eyes in the slot, the gangster glancing back, empty wall above the door). 🟡 The gangster is small, so his face goes cartoon |
| (5c prompt, landed on the 5d call) | | 4d06a289 · 94982b16 | 🔴 a prints "BAKERY - BREAD" on the wall; b has the gangster twice. Out |
| 5d | Side-on, whispering into the slot | b4491fa2 · 698e9953 | ⭐ **5d-a: the shot:** he cups his hand to whisper into the slot, the eyes inside are real, and the whole upper half is empty wall for the "QUANTITATIVE EASING" bubble. 5d-b: a huge comic profile with one goggle eye; funny, but it drops the real skin |

**Shortlist:** 5d-a, 5b-b, 5a-a. Pick owed (Jack).

**✅ Scene 5 PICKED (Jack, 2026-10-26): 5d-a** (`b4491fa2`). The gangster whispers behind a cupped hand, real eyes in the slot,
empty wall above for the "QUANTITATIVE EASING" bubble.

## Scene 6 stills — round 1 (2026-10-26)

*grandma FREEEEEEZING!*: **grandma's attic.** Frost on everything, icicles on the beams, breath steaming, one candle;
the held note lands on her face. Moves later: her breath and the candle flame. **The candle is the second costed
object:** this is the first visit, so it is still tall. Cast: grandma is a tiny white woman in her eighties with thin
silver hair in a hairnet, a long pointed nose and a mole on one cheek, wrapped in three cardigans and a crocheted
blanket. Face-scope line on every prompt; sent one at a time.

| # | Idea |
| --- | --- |
| 6a | **Close on her face:** frost on her eyelashes, a breath cloud, candle glow under her chin, the held note |
| 6b | **High from the icicled roof beams:** tiny grandma in bed under every blanket, the candle, frost everywhere |
| 6c | **Through the frosted window from outside:** the red moon in the glass, her face behind the frost, the candle |
| 6d | **Low behind the candle:** the flame huge in the foreground, grandma huddled in an armchair beyond |

### Scene 6 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, sent one at a time. 6d's first call stuck at 99% and nothing landed; the retry worked.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 6a | Close on her face | 7bf83582 · 8d42e0f3 | ⭐ **6a-a: the held note:** her mouth open in the wail, frost on her lashes, blue lips, a breath cloud, the candle under her chin, the mole. The most real skin of the day. 6a-b is the same face, quieter |
| 6b | High from the icicled beams | 4ddb8a74 · 0cf76f6e | 🟡 A lovely room (bed, washstand, the candle on a chair, icicles framing), but she is tiny, so it is not the held note. Good as an establishing shot if the film wants one |
| 6c | Through the frosted window | d6f35b2e · 740a0f6e | ⭐ **6c-b:** a real-skinned face behind frost ferns, the red moon in the glass, the candle held up, snow on the slates. The quietest and saddest. 🟡 6c-a goes goggle-eyed cartoon |
| 6d | Low behind the candle | 9dfee2bf · 257e5259 | ⭐ **6d-a:** a huge dripping candle in front, her hands held out to it, frost on the armchair. It sets up the candle as the costed object (tall now, lower each visit). 🟡 6d-b is goggle-eyed |

**Caricature/likeness:** ✅ an ordinary old woman, no exaggeration; no famous face that I can see (unverified).

**Shortlist:** 6a-a (lands the note), 6d-a (sets up the candle), 6c-b. Pick owed (Jack).

**✅ Scene 6 PICKED (Jack, 2026-10-26): `5df38f52`.** Grandma in a wing armchair with a granny-square blanket, holding her
hands to a tall dripping candle, real-skin face. It came from the **first 6d call, which stalled at 99% and landed late**:
two extra stills (`6f9dd59e`, `5df38f52`) that I found on the page afterwards. 🔴 A 99% timeout can still land minutes
later, so check the newest tiles before re-running.

## Scene 7 stills — round 1 (2026-10-26)

*stimulus checks are next. Get wrecked!*: **the mayor's balcony over the square.** The mayor tosses a handful of
envelopes to the crowd; the wind blows them straight into a storm drain. Moves later: the envelopes falling. Cast: the
mayor (locked) is tall and skinny with a bowler and a gold chain. His face: a white man in his sixties with a long narrow face,
hollow cheeks and a pencil-thin grey moustache. The crowd is named outright: young and old, men and women, Black, white and South Asian.
Envelopes are blank (no writing).

| # | Idea |
| --- | --- |
| 7a | **From inside the storm drain looking up:** envelopes fluttering down into the grate towards us, the crowd's hands at the edges, the mayor tiny on the balcony |
| 7b | **Behind the mayor on the balcony:** his bowler and his throwing arm, envelopes in the wind, the crowd reaching below, the drain in the gutter |
| 7c | **Low in the crowd:** the baker's face large, looking up, hand out, the envelopes sailing over his head, the mayor beaming behind |
| 7d | **High from a rooftop opposite:** the whole square, the envelopes arcing on the wind straight into the drain, the red moon |

### Scene 7 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, sent one at a time; all landed first time.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 7a | From inside the storm drain | afee2365 · 5039be4e | ⭐ **7a-a: the gag in one frame.** The envelopes fall through the bars at us; the crowd peers down through the grate (a Black man, an old white woman, a South Asian man, a woman in a headscarf); the mayor is tiny on the balcony in his bowler and chain. 7a-b is as good, with fewer faces |
| 7b | Behind the mayor on the balcony | ce240a6e · 68392b63 | 🔴 Both add a **second official in a red-white-blue sash** (a French-mayor cue), so it reads as two mayors. 7b-a's thrower has no bowler and reads as an elder statesman (likeness unverified). Out |
| 7c | Low in the crowd, the baker | e98b6b6e · 31629996 | ⭐ **7c-a:** the baker's real-skin face large, his hand reaching as the envelopes sail over, the mayor beaming on the balcony. 7c-b: an envelope just past his fingertips. 🟡 A floury coat instead of the vest (fine for the street) |
| 7d | High from a rooftop opposite | 4e7f6f1c · 77c84d11 | ⭐ **7d-b:** one clean ribbon of envelopes from the mayor's hand straight down into the drain, the red moon, chimney pots. The faces are tiny and cartoon (expected at this size). 🟡 7d-a has a stray bowler-hatted man in the foreground |

**Caricature check:** ✅ no exaggeration; the mixed crowd held (named outright).

**Shortlist:** 7a-a (the gag), 7d-b (the arc), 7c-a (the baker). Pick owed (Jack).

**Scene 7 pick (Jack, 2026-10-26): 7b-a** (`ce240a6e`), *"this is good, but i kinda wanted more pretty shots, with
more lights and reflections of the ground … windows … more cinematic, interesting camera shots, also the lighting and
gamma needs to pop more. i want that for all images going forward."* Research: `docs/google-flow/2026-10-26-pretty-not-slop.md`.

## 🔴 NEW HOUSE LEAD from scene 7 r2 on (Jack, 2026-10-26): "K3a lit"

Two changes to the K3a lead: (1) "big round eyes, small dot pupils and overbites" is dropped, because it fought the real-skin
faces Jack asked to keep (the goggle-eye drift); (2) a **light block** is written per scene in this shape:
*time + weather → one key light with direction → bounded practicals → value structure → warm/cold pair*. ~150 words.

**Lead (identical every time):** `Prime-time adult animated sitcom characters with simple rounded cartoon bodies, flat colour and black outlines, but every face is painted with startling real skin: pores, stubble, wrinkles, wet tired eyes, real eyelids, far more lifelike than anything around it, no feature exaggerated. Every colour is laid on in thick visible oil brushstrokes.`

## Scene 7 round 2 (2026-10-26): cinematic

**Shot spec (`shot-craft`):**
- **For:** the hand-out is a show. The mayor throws, the wind takes it, and the drain gets it. The crowd's hands are the visible cost.
- **Time and light:** dusk just after rain. **Key:** warm amber light pouring out of the open French doors behind the
  mayor, rimming him. **Practicals:** iron streetlamps round the square and lit shop windows. **Cold:** an ultramarine dusk sky.
  Value: most of the frame in deep shadow, the brights being the doorway, the lamps and their streaks on the wet cobbles.
- **Ground:** cobbles soaked, standing puddles, grit, tram rails, the drain.
- **Cast:** the locked mayor (tall, skinny, bowler, gold chain; a long narrow face, hollow cheeks, a pencil-thin grey moustache).
  Jack's pick had a second official in a red-white-blue sash; he is replaced by **a squat gangster in pinstripes holding
  the rest of the envelopes**, which keeps the two-figure balcony Jack liked and puts the beneficiary beside the mayor.
- **Variety, declared variable: the camera.** 7e is Jack's composition upgraded; 7f, 7g and 7h are new.

### Scene 7 round 2 results (2026-10-26): the new "K3a lit" lead

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed. **Verdict on the new lead: it works.** Lit windows,
streetlamps, wet cobbles throwing streaks of light, warm amber against ultramarine, deep shadows; real skin held on
every face of any size; no reflection went wrong.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 7e | Jack's composition: balcony level, past a lamp bracket | 45f43c28 · 836c118c | ⭐ Jack's frame, now lit: the mayor in bowler and chain mid-throw, the pinstripe gangster holding the stack, the doorway glow, the crowd reaching, the drain on wet cobbles. 🔴 7e-b paints "SHOP" on a sign (fix: name the shop's goods in a picture, or crop) |
| 7f | Inches above the drain, wide, tilted up | 112f8862 · d76aaf95 | ⭐ **The prettiest of the day.** An envelope sinks into the grate in front of us, an old woman stoops for it too late, the balcony blazes in the background. 7f-a is wider, with the whole crowd; 7f-b is closer, with the kerb |
| 7g | Steep over the mayor's shoulder | 2972c23f · e330a2ea | 🟡 The square is beautiful (tram rails, streaks of light), but the mayor grew a beard (7g-a), 7g-b isn't throwing, and the crowd becomes a pattern of tiny cartoon heads |
| 7h | Long lens from behind the crowd | 1816adc9 · 5344bbce | ⭐ **7h-a:** silhouetted hats and hands in front, the South Asian woman's real face turned in lamplight, the balcony as a lit frame within the frame, envelopes sweeping to the drain. 🟡 7h-b has cream strips at the edges |

**Shortlist:** 7f-a, 7h-a, 7e-a. Pick owed (Jack).

**✅ Scene 7 PICKED (2026-10-26): 7f-a** (`112f8862`). Jack: "you pick". My pick: the prettiest frame of the round, and the gag reads in it (an envelope sinking into the grate, an old woman stooping too late, the balcony blazing behind). It fits Jack's "pretty, lit, cinematic" note.

## Scene 8 stills — round 1 (2026-10-26): "K3a lit"

*rent seeking?... I'm just about eating / sorry, did I interrupt your meeting?*: **a smoky back room with a long table.**
The gangsters and the mayor mid-feast; the door bursts open on the baker holding one small loaf; everyone freezes, forks
in the air. Moves later: nothing (a freeze-frame gag); the camera pushes in on the baker in Premiere.

**Shot spec (`shot-craft`):**
- **For:** the first time the street sees where the money goes. Up to now the baker has only lost things (pay, rent);
  here the beneficiary is caught with his mouth full. The laugh is the freeze.
- **Visible cost:** the one small loaf in the baker's hand against the whole hams and the champagne.
- **Light:** night. **Key:** one low brass lamp with a green glass shade hanging over the middle of the table, pooling
  amber on the food. **Practicals:** candle stubs in bottles, glowing cigar ends. **Cold:** the open doorway, a cold blue
  corridor behind the baker, so he arrives as a dark shape edged in blue. Cigar smoke hangs in flat layers under the
  lamp. Value: most of the room in deep brown shadow; the brightest values are the lamp pool on the food and the doorway.
- **Ground:** a long polished table, spilled champagne, ham bones, grease.
- **Cast:** the mayor (locked: tall, skinny, bowler, gold chain; a long narrow face, hollow cheeks, a pencil-thin grey
  moustache). Gangsters in pinstripes, each with ordinary specific features: a fat one with a scar through his top lip, a
  thin bald one with big ears, a young one with slicked red hair and freckles. The baker (scene 2–4): a heavy-set Black
  man in his fifties, shaved head, broken nose, double chin, sweat-stained vest, flour on his forearms.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 8a | **Down the table from the far end, long lens:** hams and bottles huge in front, the diners frozen mid-bite turning to the door, the baker small in the bright doorway at the end |
| 8b | **Over the baker's shoulder from the doorway:** his floury hand and the little loaf in front, the whole table frozen and staring back at him, the mayor at the head |
| 8c | **Low among the food:** a carved ham and a champagne glass in front, the mayor's real-skin face large, frozen mid-chew with his fork raised, eyes swivelled to the door; the baker a dark shape in the doorway behind |
| 8d | **Close on the baker in the doorway (the push-in's end):** his real-skin face large, the small loaf held in front of his chest, smoke rolling past him, the lamp's amber on his face, the blue corridor behind |

Every prompt: the K3a lit lead + face-scope, "Plain margins with no writing. Thanks." NB2, 16:9, ×2, project `dedd295f`,
one at a time. Full prompts in the provenance cards.

### Scene 8 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time. 8a timed out at 99% and landed a minute later (fetched from the page).

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 8a | Down the table from the far end | bc301616 · 7ffa80d9 | ⭐ **8a-b: the whole gag in one frame:** the feast lit by the green lamp, spilled champagne pooling on the table, the baker in the blue doorway holding up his loaf. 🟡 The camera ended up at the foot of the table, so the mayor sits dead centre and the diners stare at us, not at the door: it reads as a group portrait more than a freeze. 🔴 Likeness check (unverified): the fat scarred gangster in 8a-b may look like a well-known TV actor; check before it ships |
| 8b | Over the baker's shoulder | 93ea0c16 · 7fa3e9d8 | ⭐ **8b-a: the clearest story:** the loaf large in his floury hand, the table frozen, the mayor stopped with a drumstick at his lips, champagne overflowing the glass. Blue light across the floorboards. 🟡 Only four diners (a small table, not a long feast). 8b-b is the same with an apron and a flatter light |
| 8c | Low among the food, the mayor | 496e8342 · d0eb8353 | ⭐ **8c-a: the best real-skin face of the round:** the mayor mid-chew, grease on his chin, eyes swivelled to the door. 🔴 In both, the baker in the doorway wears a waistcoat and tie and reads as a butler, and the two gangsters are the same man twice. 🟡 8c-a: the chain is on his hat, and no pencil moustache |
| 8d | Close on the baker (push-in end) | e386359c · 8511d9b2 | ⭐ **8d-b:** real skin, sweat on his head, the floury loaf held to his chest, the cold corridor behind. 🟡 The room's warm light comes from the side, not from in front of him, so he reads as standing in a hallway rather than on a threshold. 8d-a is the same, flatter |

**Lesson:** the K3a lit lead held again (lamp, smoke layers, warm/cold split); real skin stayed on every face of any size.
A figure in a doorway with no wardrobe line goes formal (8c's butler): give the baker his vest every time he is small.

**Shortlist:** 8b-a (the story), 8a-b (the feast), 8d-b for the push-in end (pairs with either). Pick owed (Jack).

**✅ Scene 8 PICKED (Jack, 2026-10-26): 8b-b** (`7fa3e9d8`): over the baker's shoulder (vest and apron, the loaf in his floury
hand), the four diners frozen, champagne pouring, the mayor with a drumstick at his lips, blue door light on the floorboards.

## Scene 9 stills — round 1 (2026-10-26): "K3a lit"

*remember kids, the Fed is not your friend! / it prints all the dollars that the government spends*: **a 1930s
schoolroom.** A teacher at the blackboard; grown adults squeezed into children's desks ✏️. The chalk drawing (a printing
press with a smiling face) goes on in ffmpeg, so the board is asked for **wiped clean and empty**. Moves later: the
teacher's pointer tapping.

**Shot spec (`shot-craft`):**
- **For:** the film turns to camera and teaches. After the feast (where the money goes), this is the narrator's lesson
  for the street, and the joke is that the grown-ups are the class.
- **Visible cost:** the street's own people at the tiny desks, still in work clothes, wet coats, the baker's knees up
  round his chin. They're the ones who need the lesson.
- **Light:** a grey winter afternoon, snow outside. **Key:** tall windows down one side, cold blue-grey daylight raking
  across the desks. **Practical:** a pot-bellied iron stove glowing orange through its grille, one green-shaded lamp over
  the teacher's desk. **Warm/cold:** stove orange against window blue. Value: the room mostly in shadow; the brightest
  values are the windows, the stove grille and the wet floor in front of it.
- **Ground:** worn floorboards wet from boots, puddles of melted snow, coats steaming on the hooks.
- **Cast:** the teacher (recurring, new): a plump woman in her forties, round wire glasses, frizzy brown hair with a grey
  streak in a bun, a brown cardigan, a long wooden pointer. The class, named outright: the baker (vest, apron, shaved
  head, broken nose), a young South Asian mother in a headscarf, a skinny old white dock worker in a flat cap, a young
  Black man in overalls, a ginger woman in a factory smock.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 9a | **From behind the teacher at the board:** her shoulder and raised pointer in front, the rows of adults crammed into tiny desks facing us |
| 9b | **Low along a row of desks:** a tiny inkwell desk in front, the baker's knees up to his chin, his real-skin face large looking up; the teacher small at the board |
| 9c | **High from the back corner:** the whole room, the stove, the snowy windows, the teacher at the empty board, the squeezed rows from behind |
| 9d | **Close on the teacher:** pointer on the empty board, turned to the class mid-word, her real-skin face large |

### Scene 9 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. Every blackboard came back empty (ready for the
ffmpeg chalk press), and nothing invented writing.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 9a | Behind the teacher | 968984d6 · 240678df | 🟡 **9a-a has the teacher's best profile** (real skin, grey streak, the pointer up) and the whole class facing us. 🔴 The desks are adult-sized, so the gag is gone, and 9a-a has the old dock worker and the ginger woman twice. 9a-b is cleaner but hides her face |
| 9b | Low along the desks | 93f96d27 · 8e44823c | ⭐ **The gag lands:** the baker crammed into a tiny desk with his knees up to his chin and an inkwell in front, a worried real-skin face; the mother and the dock worker squeezed in down the row; the teacher at the empty board; the stove and the snowy windows. 9b-a: the most real skin. 9b-b: the baker's shaved head (continuity) and more room. 🟡 9b-b has a cartoon-faced figure cut off at the left edge |
| 9c | High from the back corner | 180f047e · 9fd02593 | 🟡 Lovely rooms (snowy windows, the stove, the coat hooks, wet floor), but everyone twists round to look up at the camera, and the desks are adult-sized. 9c-b is a full class: good as an establishing shot only |
| 9d | Close on the teacher | 08cb9961 · 73d0759d | ⭐ **9d-a:** a real-skin teacher mid-word, the pointer on the empty board, the green lamp, the stove, the cartoon caps and headscarf of the class in front. 9d-b: same, with a softer light. 🔴 Likeness check (unverified): she may look like a well-known British comedy actress; check before she becomes a Flow Character |

**Lesson:** "tiny children's desks" only showed when the camera was low and close to one sitter (9b). Wide and high, NB2
sized the desks to the adults.

**Shortlist:** 9b-a or 9b-b (the gag), 9d-a (the teacher, a cut to go with it). Pick owed (Jack).

**✅ Scene 9 PICKED (Jack, 2026-10-26): 9d-a** (`08cb9961`): close on the teacher mid-word, pointer on the empty board, the class's caps and headscarf in front. (Jack overrode my 9b-b; 9b-b stays in the bin as a cutaway.) 🔴 Likeness check still owed before she becomes a Flow Character.

## Scene 10 stills — round 1 (2026-10-26): "K3a lit"

*this fiat system is insistent / on debts existence, sooooo*: **a marble bank lobby.** A worker in his only suit at a
loan desk, the clerk's pen hovering; behind them, small, gangsters walk straight past the guard into the vault with
sacks. Moves later: the gangsters walking. Scene 11 is the same lobby, close, with the DENIED stamp (ffmpeg).

**Shot spec (`shot-craft`):**
- **For:** two doors to the same money. The worker has to ask for it and wait; the gangsters just walk in. One frame,
  two lanes.
- **Visible cost:** the baker (the worker is the baker: continuity, and his face carries it) in a suit two sizes too
  small, hat in his hands, waiting.
- **Light:** a rainy evening. **Key:** the open round vault door at the back, glowing warm gold from inside, the one big
  bright. **Practicals:** green banker's lamps on the desks. **Cold:** tall rain-streaked windows, blue. Value: the hall
  mostly in shadow; the brightest values are the vault mouth and its long streak across the wet marble floor.
- **Ground:** polished marble floor with rain tracked in by boots, puddles, a mop bucket.
- **Cast:** the baker (shaved head, broken nose, double chin) in a shabby brown suit too small for him. The clerk: a thin
  young white man, centre-parted oiled hair, sleeve garters, a pen hovering over a form. The guard: an old white guard in a
  peaked cap and brass buttons, tipping his cap. The gangsters from scene 8 in pinstripes, with sacks over their shoulders:
  the fat one with a scar through his lip, the thin bald one with big ears, the young ginger one with freckles.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 10a | **Over the clerk's shoulder:** the hovering pen and the form in front, the baker across the desk, hat in hands; deep behind him the gangsters stroll into the glowing vault past the guard |
| 10b | **Low on the wet marble from beside the vault door:** the gangsters' shoes and sacks passing close in front, the loan desk far back with the baker waiting |
| 10c | **High from the gallery:** the whole lobby, the loan desk on one side, the procession into the vault on the other |
| 10d | **Close on the baker, side-on at the desk:** his face large, the vault blazing soft behind him with the small gangsters walking in |

### Scene 10 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The lead held: the gold vault light streaks
across the wet marble, the green lamps glow and the windows are cold blue in every one.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 10a | Over the clerk's shoulder | dae424d0 · 9136b29a | ⭐ **10a-b: both lanes in one frame:** the baker in his tight suit, hat in hands, a real-skin face; the clerk's pen over a blank ruled form; across the hall, the gangsters with sacks at the blazing vault, the guard tipping his cap, gold bootprints on the marble. 🔴 10a-a prints "LOAN FORM" on the paper (out) |
| 10b | Low by the vault door | 6c72e22b · 21deb73b | ⭐ The gangsters large, in real skin, sacks over shoulders, two-tone shoes on gold-lit marble, the guard tipping his cap; the baker small and waiting at the desk behind. 🟡 The camera stayed at standing height, and the gangsters walk out of the vault rather than in (still reads as theft). 10b-b has the prettier floor |
| 10c | High from the gallery | a4871671 · ac693a22 | 🟡 Clean two-lane geography, but the camera came down to near eye level, so it's flat. 🔴 10c-b paints a signature scrawl in the bottom-right corner |
| 10d | Close on the baker | 3591d932 · 5a530acc | ⭐ **10d-a:** sweat running down his scalp, a real-skin face, the green lamp, the clerk's hand and pen at the edge, the gangsters small in the gold vault behind. 🔴 10d-b's pen floats with no hand. 🟡 The small background gangsters wear fedoras and lose their scene-8 faces (too small) |

**Shortlist:** 10a-b (the scene in one frame), 10d-a (his face; the push-in or the cut into scene 11), 10b-b.

**✅ Scene 10 PICKED (my pick, provisional, 2026-10-26): 10a-b** (`9136b29a`). Jack said "next" without picking; swap it any time.

## Scene 11 stills — round 1 (2026-10-26): "K3a lit"

*don't be hating on the credit rating / or have resistance to the facts I'm stating*: **the same lobby, close.** The
clerk brings down a rubber stamp; **DENIED** goes on in ffmpeg. Omni can't reach a state, so the still holds the stamp
**raised high, about to fall**, over a blank form; the clip moves it down, and the word lands in ffmpeg on the cut.

**Shot spec (`shot-craft`):** same light, cast and lobby as scene 10 (rain, green lamps, the gold vault).
- **For:** the punchline of scene 10. The worker asked; this is the answer, and it's instant.
- **Visible cost:** the blank form under his hands, the only thing he brought.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 11a | **Straight down on the desk:** the blank form, the baker's hands either side of it, the clerk's fist with a wooden stamp raised high above, the ink pad open |
| 11b | **Low at desk level:** the form in front, the stamp hanging above it at the top of frame, the baker's real-skin face beyond, wincing |
| 11c | **Close on the clerk:** a bored real-skin face, the stamp raised by his ear, the baker's shoulder dark in the near foreground |
| 11d | **Over the baker's shoulder:** the clerk swinging the stamp up, the vault blazing behind him with the gangsters strolling in |

### Scene 11 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 11a | Straight down on the desk | dd94c9c0 · 542705e0 | 🟡 A strong graphic frame (green lamp, red ink pad, blank page between them), but both men crane their heads up to look at the camera, and the stamp is held by the lamp, not above the page |
| 11b | Low at desk level | b0167d1f · 98a09790 | ⭐ **The scene in one frame:** the stamp dripping red ink hangs over the blank form, and the baker winces with his eyes squeezed shut, sweat on his scalp, a real-skin face. **11b-b** has the gold vault glowing over his shoulder; 11b-a's vault is duller, and the clerk's sleeve is brown |
| 11c | Close on the clerk | 89c73422 · ab70d09c | 🟡 **11c-b:** bored, sleepy-eyed, the stamp up by his ear, the gold vault behind, the baker's profile in front. The gum became a cigarette. 🔴 11c-a's shaving nick reads as blood running from his mouth |
| 11d | Over the baker's shoulder | eb1814cb · 1e34840a | ⭐ **11d-b:** the clerk swings the stamp up while the gangsters stroll out of the blazing vault behind him, with the guard tipping his cap: both lanes again. 🔴 11d-a scribbles letters on the stamp's face |

**Shortlist:** 11b-b (the wince), 11d-b (both lanes), 11c-b.

**✅ Scene 11 PICKED (Jack, 2026-10-26): 11d-a** (`eb1814cb`): over the baker's shoulder, the clerk swinging the stamp up, the gangsters at the blazing vault behind. (Jack overrode my 11b-b.) 🟡 Its stamp face has scribbled letters: the ffmpeg DENIED goes over them at the impact.

## Scene 12 stills — round 1 (2026-10-26): "K3a lit"

**Chorus 1** *Robbery, robbery! / Call the police, it's a robbery! / Debasement!… in da basement! / Printer is burrrrning…*:
**the building in cross-section, the first drop.** Down through the bakery floor into the Mint: rows of presses, sheets of
banknotes, the band, notes like confetti, the mayor dancing. Moves later: the drop (a Premiere move) and the presses
throwing notes.

**Shot spec (`shot-craft`):**
- **For:** the reveal the whole first verse has been asking for (*where does it go? nobody knows!*). Upstairs is the cold,
  floury, honest bakery; one floor down is a party lit like a casino.
- **Visible cost:** the bakery above, dark and empty at night, the baker's apron on a hook, directly over the party.
- **Light:** the Mint's own colours (`storyboard.md` → the building): **emerald** press lamps, **gold** stage spots, **scarlet**
  velvet. The bakery above is cold blue night with one dim bulb. Value: the Mint is the bright floor; everything above it is
  dark, so the eye falls down.
- **Rules carried:** the band = the gangsters themselves in pinstripes (the "mixed band" fix); the press faces = "simple faces
  painted on their sides"; the banknotes are blank green paper with no printing.
- **The tall-still problem (inferred, untested):** a 9:16 still from NB2 is 768 px wide, so a 16:9 window panned down it
  would be blown up about 2.5× for 1080p. So round 1 tries the tall still **and** 16:9 frames that can be cut as the drop
  (start, through, landing) if the tall one is too soft.
- **Variety, declared variable: the frame.**

| # | Idea |
| --- | --- |
| 12a | **9:16 tall cross-section:** the dark bakery on top, the floor slab cut open, the blazing Mint below |
| 12b | **16:9 the Mint in cross-section, side-on (the landing frame):** the whole speakeasy like a lit stage, presses, the band, the mayor dancing, the bakery's underside as a dark ceiling strip at the top |
| 12c | **16:9 low inside the Mint among the presses:** notes raining, the mayor dancing large in real skin, the band behind |
| 12d | **16:9 the drop's start:** straight down through a gap in the bakery floorboards into the emerald and gold glow below |

### Scene 12 round 1 results (2026-10-26)

NB2, project `dedd295f`, one at a time; all landed first time. (Prompts say "basement", never "Mint", so that the word
can't be painted on anything.)

| # | Frame | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 12a | 9:16 tall cross-section | 99e79a4d · 527e4a3b | ⭐ **The drop works as a picture:** the dark bakery (loaves on racks, the apron on its hook, moonlight), the floor cut through to joists, brick and earth, then the blazing basement (emerald lamps over the presses, notes flying, the pinstripe band on a red-curtained stage, the mayor dancing). **12a-a** is full of people; **12a-b** is simpler and reads faster (the mayor on a table) but sits inside a cream canvas border (crop). 🟡 Faces are small and go cartoon (expected). 🔴 At 768 px wide, a 16:9 pan down it is ~2.5× blown up for 1080p (inferred): it will look soft |
| 12b | 16:9 the basement, side-on | 642ccdf6 · d16a7a58 | ⭐ **12b-b: the landing frame:** flour sifting down through the cut ceiling joists into the emerald light, the presses with painted faces, notes in the air, the mayor dancing in his chain, the band under gold spots, spilled champagne on the tiles. 🔴 12b-a paints "FLOUR" on a sack. 🟡 The drinkers look glum for a party (it may suit the satire) |
| 12c | 16:9 low among the presses | 5da41d28 · 3babc5dc | ⭐ **12c-a:** the mayor mid-jig with his arms up and eyes shut in bliss, notes raining, a press with a smug painted face, the band behind, a tipped champagne bottle on the tiles. 🟡 His face is more cartoon than real skin. 12c-b is the same, but his moustache grew into a walrus (off-model) |
| 12d | 16:9 down through the floorboards | 5d7f8e14 · a48bc51c | 🔴 Both put people on the bakery floor peering down the gap (I asked for an empty room); 12d-b paints the same man twice in modern T-shirts. 🟡 **12d-a is a seed for scene 31** (the street looking down at the trapdoor): a worn man and an old woman on their knees at a glowing green hole |

**For the drop, two ways (inferred, untested in Premiere):** (1) the tall 12a-b as one move, accepting the softness; or
(2) a cut chain: the bakery at night → a whip-pan down → **12b-b** landing → **12c-a** for the chorus's second half.

**Shortlist:** 12b-b (the landing), 12c-a (the mayor dancing), 12a-b (the tall drop).

**✅ Scene 12 PICKED (my pick, provisional, 2026-10-26): 12b-b** (`d16a7a58`), as the landing of the cut chain (bakery at night → whip-pan down → 12b-b → 12c-a). Jack said "next" without picking; swap it any time.

## Scene 13 stills — round 1 (2026-10-26): "K3a lit"

**Chorus 2** (same words as chorus 1): **the basement, close on the biggest press.** The press glows red hot, spitting
notes; the mayor feeds it with a coal shovel. Moves later: the shovel.

**Shot spec (`shot-craft`):**
- **For:** chorus 1 showed the party; chorus 2 shows the engine. The mayor isn't a guest, he's the stoker. *Printer is
  burrrning* made literal.
- **Visible cost:** the bakery floor directly overhead, flour sifting down through the joists onto his shoulders.
- **Light:** the key is the open firebox of the press, red-orange, uplighting him; the emerald lamps are the cool fill;
  sweat and heat shimmer. Value: deep shadow everywhere except the firebox and the notes it spits.
- **Rhyme:** 13d is shot from inside the firebox, the same oven-mouth frame Jack picked for scene 2 (the bakers). Same
  frame, different oven.
- **Cast:** the locked mayor (tall, skinny, bowler, gold chain, long narrow face, hollow cheeks, pencil-thin grey moustache),
  shirt-sleeves rolled, waistcoat, sweating. The press has a simple face painted on its side.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 13a | **Low under the press's delivery tray:** notes spitting out towards us, the mayor behind shovelling, lit red |
| 13b | **Close profile:** the mayor's real-skin face large, sweating, lit red by the open firebox as he heaves a shovel of coal |
| 13c | **High from the band's stage, past the trumpet bell:** the big press glowing in the middle of the room, the mayor small at it, gangsters cheering |
| 13d | **From inside the firebox looking out:** flames framing the mayor's face lit orange, the shovelful of coal coming at us |

### Scene 13 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. No text anywhere.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 13a | Low under the delivery tray | 4c73facc · 1e818939 | 🟡 Notes sliding out at us with red-lit edges, the open firebox, flour sifting from the ceiling. But the mayor looks weary, not gleeful, and the fire doesn't light his face. 13b-b's moustache goes walrus again |
| 13b | Close profile | 09a7b2d8 · 43041d06 | ⭐ **13b-a: the stoker:** on-model mayor (narrow face, pencil moustache), a gritted, sweating grimace-grin, flour on his bowler, the press's painted face smiling beside the open fire. 🟡 13b-b has the strongest real skin, but the head is oversized and the face is off-model (not the narrow mayor). Likeness unverified |
| 13c | High from the stage, past the trumpet | 947d423e · 90711dbe | ⭐ **13c-a: chorus energy:** the trumpet in the foreground, the press spitting a fountain of notes, its red glow on the tiles, the mayor shovelling, gangsters cheering with fists up. **13c-b:** same, but the press's painted face looks worried (a good gag) and the crowd is packed. The camera came out at stage height, not high |
| 13d | From inside the firebox | 7514ee8b · 861fc7d7 | ⭐ **13d-a: the rhyme with scene 2:** coals and flames framing the door, the mayor leaning in with a heaped shovel, notes and emerald lamps behind. 🔴 13d-b sits inside a white canvas border |

**Shortlist:** 13c-a (the chorus), 13b-a (the mayor), 13d-a (the oven rhyme).

**✅ Scene 13 PICKED (Jack, 2026-10-26): two shots: 13a-b** (`1e818939`, the notes sliding off the press at us, the mayor shovelling, the painted face smiling) **and 13d-a** (`7514ee8b`, from inside the firebox).

## Scene 14 stills — round 1 (2026-10-26): "K3a lit"

*Stacks and stacks of elastic cash / distracted by a dispraxic flash*: **the town square, a bandstand.** The mayor does a
magician's flash (smoke, a bright pop); behind the smoke, gangsters carry sacks out of the bank. Moves later: the smoke puff.

**Shot spec (`shot-craft`):**
- **For:** the trick named. Verse 2 is the distraction, and this is the first time we watch the crowd look the wrong way.
- **Visible cost:** the crowd's faces, lit white by the flash, mouths open, looking at the wrong thing.
- **Light:** night after rain. **Key:** the flash itself, a burst of white magnesium light and a billowing smoke cloud on
  the bandstand, throwing hard shadows across the square. **Practicals:** a ring of bare bulbs round the bandstand roof,
  iron streetlamps; the bank door ajar, spilling gold. **Cold:** ultramarine sky, the small red moon. Value: the flash is the
  brightest thing; the bank's gold doorway is the second.
- **Ground:** wet cobbles throwing the flash back in streaks.
- **Cast:** the locked mayor, in a magician's cape over his suit, bowler on. Gangsters in pinstripes with sacks, tiptoeing.
  The crowd named outright: young and old, men and women, Black, white and South Asian.
- **Text:** the bank is "a columned stone building with a blank pediment and no lettering".
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 14a | **Long lens from behind the crowd:** silhouetted hats in front, the mayor mid-flash on the bandstand, and through the thinning smoke behind him, the gangsters carrying sacks down the bank steps |
| 14b | **Close on the crowd:** three real-skin faces lit white by the flash, open-mouthed (the cost) |
| 14c | **High from the bank's cornice:** sacks going down the steps right below us, the square beyond, everyone facing the smoke on the bandstand |
| 14d | **Wide at ground level, side-on:** the bandstand and its flash on the left, the bank on the right with the gangsters tiptoeing out, the crowd in between all facing left |

### Scene 14 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The blank-pediment wording held: no lettering on
any bank.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 14a | Long lens from behind the crowd | b9380ec1 · 366f58b6 | ⭐ **14a-a: the trick in one frame:** the mayor in his cape mid-flash on the bulb-ringed bandstand, the smoke rolling across to the bank, gangsters with sacks tiptoeing down the steps from the gold doorway, the red moon above the pediment, wet cobbles streaked with light, the mixed crowd in front. 🟡 Some of the crowd turn to face us instead of the stage. 14a-b: half the crowd faces us, and cartoon onlookers stand on the bandstand |
| 14b | Close on the crowd | 88e7038d · 9345c556 | ⭐ The strongest real skin of the scene: the baker, a young South Asian woman, an old dock worker, open-mouthed. 🟡 The light is even, not a hard flash from one side, and three faces in a row read as a poster line-up. Likeness unverified |
| 14c | High from the bank's cornice | f72867fd · 9bbab8fd | ⭐ **14c-a:** the flash a huge white bloom round the mayor, the whole crowd facing it, and right below us the gangsters hauling sacks out of the gold doorway; one turns his real-skin face up at us, caught. 🟡 14c-b: the flash is weak, the red moon is missing, and the two foreground gangsters are the same man twice |
| 14d | Wide, side-on | 6c6fa451 · 6d5f89ab | 🟡 Clear geography (bandstand left, bank right, crowd between), but flat and staged, with half the crowd facing us. 🔴 14d-b dresses children in modern T-shirts and shorts with goggle eyes |

**Shortlist:** 14a-a (the trick), 14c-a (caught from above), 14b-a (the cost, a cutaway).

**✅ Scene 14 PICKED (Jack, 2026-10-26): 14d-b** (`6d5f89ab`): wide and side-on, the mayor flashing on the bandstand (left), the gangsters slipping out of the gold doorway (right), the crowd between. 🟡 Two children in modern T-shirts and shorts: fix in a re-roll or the edit if they jar.

## Scene 15 stills — round 1 (2026-10-26): "K3a lit"

*mob, angry at their shitty little job / the right and the left both witness the theft*: **the street outside the bakery.**
A red crowd and a blue crowd, banners and scarves, shoving under the street lamp; police cars nose to nose. Moves later:
the shove.

**Shot spec (`shot-craft`):**
- **For:** the distraction working. Scene 14 was the trick; this is the audience turning on itself.
- **Visible cost:** both crowds in work clothes (overalls, aprons, flat caps, factory smocks): the same people, the same jobs,
  split by a scarf.
- **The irony (15d):** "both witness the theft": a gangster strolls past them with a sack, and nobody looks.
- **Light:** night after rain. **Key:** one iron street lamp over the clash. **Practicals:** the bakery's lit shop window,
  warm cream; two police cars' headlamps, hard white. **Cold:** ultramarine sky, the small red moon. Value: the lamp pool
  and the headlamp beams are the brights.
- **Rules carried:** team colour on scarves, armbands and banners, never on people; **each** crowd named outright (young and
  old, men and women, Black, white and South Asian), so neither colour reads as a race; banners and the shop sign plain, with
  no writing; after 14: "every face turned towards the other crowd".
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 15a | **Low between two police cars nose to nose:** bumpers and headlamps huge in front, the crowds clashing beyond under the lamp |
| 15b | **High from the bakery's upstairs window:** the two crowds meeting in a ragged line, red left, blue right, the shop's light on the cobbles |
| 15c | **In the crush:** a red-scarf man and a blue-scarf woman shoulder to shoulder, faces large, real skin, mid-shove |
| 15d | **Long lens down the street:** the lit bakery, the crowds fighting, and on the near pavement a gangster strolling past with a sack, unseen |

### Scene 15 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. Every banner and the shop sign came back blank.
"Every face turned towards the other crowd" worked: nobody stared at the camera this time. Both crowds held the named
mix in every still, so neither colour reads as a race.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 15a | Low between the police cars | f65b6764 · 70895704 | ⭐ **15a-b:** the two headlamp pairs pin the brawl like a stage, fists flying, red and blue banners, the bakery window glowing between them. 15a-a is the same, more posed, with a cartoon-heavy left crowd |
| 15b | High from the upstairs window | f84f3665 · af05303b | ⭐ **15b-a:** the window frame as a border, the ragged line where red meets blue under the lamp, the police cars nose to nose with crossed headlamp beams, the red moon in the top pane. **15b-b:** a wider street, peeling paint on the sill, the cars further off; more air, less crush |
| 15c | In the crush | f9424fe7 · 046d2a41 | ⭐ **15c-b: the best real skin of the scene:** the gap-toothed docker and the grey-haired woman forehead to forehead, both roaring, the crowds behind. 🔴 **Both 15c banners came out cream, not red and blue** (the colours went onto the scarves only). Fine as a close-up; banners can be crops |
| 15d | Long lens, gangster on the pavement | a730f61f · 35534262 | ⭐ **The line in one frame:** the brawl, the cars, the lit bakery, and in front a gangster strolling past with a sack while nobody looks. **15d-b** is the cleaner composition (the gangster's real face, the alley wall); 15d-a has a stray onlooker glancing at him |

**Shortlist:** 15d-b (the theft witnessed by no one), 15a-b (the stage), 15b-a (the line from above), 15c-b (the faces, for scene 16).

**✅ Scene 15 PICKED (Jack, 2026-10-26): 15d-a** (`a730f61f`): the brawl, the cars nose to nose, the lit bakery, and the gangster strolling past in front with a sack.
**Note for scene 16:** 15c-b already *is* scene 16's "red-scarf man and blue-scarf man nose to nose"; scene 16 just
needs the pay-packet gag added.

## Scene 16 stills — round 1 (2026-10-26): "K3a lit"

*blaming each other is a sick little cover / institutional, dilutional, the usual*: **close in the crowd.** A red scarf
and a blue scarf nose to nose, shouting; both have the same thin pay packet in their back pockets ✏️. Moves later: the
two mouths shouting (no speech).

**Shot spec (`shot-craft`):**
- **For:** the punchline of the brawl. They're fighting each other, and they're paid the same pittance by the same people.
- **Visible cost:** the two identical thin brown pay packets: the same object as scene 3's, so it pays off.
- **Cast (continuity with 15c-b):** the broad young white docker in overalls, red scarf, a broken front tooth; the tall
  middle-aged Black woman in a factory smock, blue scarf, grey in her hair.
- **Light:** as scene 15: the street lamp hard from above, the bakery's warm window behind, wet cobbles, the red moon.
- **The hard part:** a back pocket and a face can't both be large unless the camera is behind and low, so the variants
  trade the two off.
- **Pay packet wording:** "a thin brown paper pay envelope with no writing on it".
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 16a | **Low behind them at hip height:** both back pockets large in front, the identical packets poking out, their shouting heads above in the lamplight |
| 16b | **Side-on, waist up, profile to profile:** both shouting, the packets visible in their back pockets at the frame edges |
| 16c | **Insert, close on the two back pockets side by side:** the identical packets, a red scarf end and a blue one hanging beside them |

### Scene 16 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The docker and the grey-haired woman carried
over from 15c-b in every still. The envelopes came out identical and blank every time.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 16a | Low behind, at hip height | 94f85424 · ef689476 | ⭐ **16a-b: the painterly one:** two matching envelopes in two back pockets, huge in front; the two faces roaring nose to nose above; scarves streaming in the wind. 🔴 Both paint shop lettering ("BAKERY", "BAK"): **the word "bakery" in a prompt prints itself.** Fixed from 16b on ("a shop window full of loaves under a plain blank sign"). 16a-b could be fixed with a crop or a paint-out |
| 16b | Side-on, profile to profile | 3fed75a3 · 9b48d47c | ⭐ **16b-a: the gag and the faces in one frame:** the roaring docker (broken tooth) and the woman (grey hair), fists clenched, the matching envelopes at both frame edges, the shop of loaves glowing between them, the red moon. No lettering. 16b-b: closer and wetter, but the faces lean cartoon |
| 16c | Insert on the two pockets | 4c6cc443 · 2d727b63 | ⭐ The punchline as an insert: blue denim and grey smock, two identical envelopes, the red and blue scarf ends, the wet street and lamp between. **16c-b** is the richer paint, **16c-a** the cleaner composition. No lettering |

**Shortlist:** 16b-a (all in one), 16c-b (the insert to cut to).

**✅ Scene 16 PICKED (Jack, 2026-10-26): 16c-a** (`4c6cc443`): the two back pockets, identical envelopes, red and blue scarf ends, the lamp and the shop of loaves between.

## Scene 17 stills — round 1 (2026-10-26): "K3a lit" 🔑 the money shot

*distraction IS the attraction / the intention is tension between the factions*: **the cross-section, the midpoint
reversal.** Upstairs the crowds fight; directly beneath, the red leader and the blue leader dance arm in arm with the
mayor. Moves later: the dancers (camera locked; the cut-away does the work).

**Shot spec (`shot-craft`):**
- **For:** the reversal the whole film turns on. Everything so far said "they fight each other"; this says "their leaders
  don't". It must read in one look, with no words.
- **Visible cost:** the crowd above, the same working people from scene 15, hurting each other in the cold while the floor
  under their boots is a party.
- **Light:** the split is the image. Upstairs: cold ultramarine night, one street lamp, wet cobbles. Downstairs: the
  basement's emerald lamps, gold spotlights, scarlet velvet. The floor slab between them is a thin dark line.
- **Cast (new, recurring):** the red leader, a short stout white man in his sixties with ginger mutton-chop whiskers, a
  red tie and a red carnation; the blue leader, a broad-shouldered white woman in her fifties with a black bob, a long
  nose, a blue tie-neck blouse (a plain blue cardigan from 17b on) and a blue carnation. Both with ordinary, specific features (likeness rule). The locked
  mayor between them. Team colour only on ties and carnations; **no sashes** (a sash summoned a French mayor in scene 7).
- **Text:** "plain banners with no writing", and no shop word.
- **Variety, declared variable: the camera / the frame.**

| # | Idea |
| --- | --- |
| 17a | **Straight-on cross-section, two equal halves:** the street brawl on top, the floor slab cut through, the three dancers below |
| 17b | **Mostly basement, the street a thin strip at the top:** the dancers large with real-skin faces, the crowd's boots and banners just visible above the cut |
| 17c | **From the basement looking up through an iron pavement grating:** the crowd's boots stamping on the grate above, light from below; the three dancers in the foreground, lit gold |
| 17d | **Close on the three dancers:** arm in arm, mid-kick, laughing, dust shaking down from the ceiling with each stamp above |

### Scene 17 round 1 results (2026-10-26) 🔑

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. No lettering anywhere. **The reversal reads in
one look in every variant.** The two new leaders held their features across all eight (ginger mutton-chops + red
carnation; black bob + blue carnation).

| # | Frame | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 17a | Straight-on cross-section, two halves | 036e9b6e · 9d90d5ae | ⭐ **17a-b: the money shot as designed:** the red and blue crowds brawling on the cobbles under the lamp and the red moon, the street cut through, and right below, the three kicking in a gold spotlight, laughing, presses spitting notes, the pinstripe band. 🔴 17a-a: the blue leader lost the bob and gained wavy hair and a bow blouse, a drift towards a real former PM's look (unverified); so from 17b on she wears "a plain blue cardigan" |
| 17b | Mostly basement, a strip of street | 23c9b8d3 · e78285aa | ⭐ **17b-b:** the boots stamping across the top, the ceiling cracking and grit pouring into the spotlight, the trio kicking, gangsters drinking and catching notes. 17b-a: the trio larger and off-centre, cleaner, real skin strong |
| 17c | Up through the pavement grating | 063a663b · ef14153d | ⭐ **17c-a: the most striking frame of the film so far:** boots on a glass-and-iron grate overhead, red and blue scarves dangling through, rain dripping, the red moon in a pane; below, the three in a gold blaze, roaring with laughter. 🟡 The mayor's gold chain shrank to a watch chain in both (fixed in 17d with "a heavy gold mayoral chain round his neck") |
| 17d | Close on the trio | 139a0b9a · 95364943 | ⭐ Real skin at its best on all three; the mayoral chain is back; dust in the spotlight. **17d-a** has the kick, **17d-b** is a posed group, almost a portrait. 🟡 The red leader's hair went white and bald on top (mutton-chops kept) |

**Shortlist:** 17a-b (the money shot as written), 17c-a (the grate), 17d-a (the close-up to cut to).

**✅ Scene 17 PICKED (Jack, 2026-10-26): 17c-a** (`063a663b`): up through the pavement grate, boots and scarves above, the three kicking in a gold blaze below.

## Scene 18 stills — round 1 (2026-10-26): "K3a lit"

*divide and conquer, just look at the hand / It's not ya standard, propaganda, worth a couple grand-ahh*: **a radio
studio.** The mayor at a big chrome microphone, the ON AIR lamp lit, reading from a script with a grin. Moves later: the
lamp flicking on. **"ON AIR" is ffmpeg:** the lamp is asked for as "a blank glowing red lamp box", and the script as blank pages.

**Shot spec (`shot-craft`):**
- **For:** the machine that makes the fight. Scene 17 showed the leaders are friends; this is how the street is told
  they're enemies. It sets up scene 19 (the same voice in every kitchen).
- **Visible cost / beneficiary:** a gangster at the control desk behind the glass, counting a wad of notes while the needles
  swing: the broadcast is paid for.
- **Light:** night. **Key:** the red ON AIR box glowing above the door, washing the padded walls red. **Practicals:** a
  brass desk lamp on the script; the control room's valve dials glowing green through the glass. **Cold:** a tall window
  onto the snowy city, the small red moon. The chrome microphone catches all three.
- **Cast:** the locked mayor (with "a heavy gold mayoral chain round his neck", the 17d fix). A gangster engineer in
  pinstripes and headphones: a thin bald one with big ears (the scene 8 gangster).
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 18a | **Close on the mayor at the chrome mic:** real skin, a grin, the script in his hand, red light on one side of his face, the desk lamp on the other |
| 18b | **From the control room, past the gangster engineer:** his bald head, headphones and the wad of notes in front, the green dials, the mayor beyond the glass under the red lamp |
| 18c | **Low from the desk:** the chrome microphone huge in the foreground, the mayor leaning into it, the red lamp above the door behind |
| 18d | **Wide, the tall window behind:** the mayor small at the mic in the red-lit studio, the snowy city outside full of little lit kitchen windows, the red moon |

### Scene 18 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The "blank glowing red lamp box with no writing"
came back blank in all eight (ready for the ffmpeg ON AIR). The script pages stayed blank. The mayoral chain held in all
eight (the 17d wording works).

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 18a | Close at the mic | 42ea67ad · acf39cce | ⭐ **18a-b:** the most real skin on the mayor so far: a sly, knowing grin, red light on one cheek and the brass lamp on the other, the green control window behind, the chrome mic. 18a-a is the same, more rumpled. 🟡 18a-b's red lamp box has faint marks (ffmpeg covers it) |
| 18b | Through the control-room glass | 6effb4be · 69e43176 | ⭐ **The beneficiary in frame:** the bald gangster in headphones counting a fat wad of notes in the green glow of the dials, while the mayor broadcasts in a red booth beyond the glass. **18b-a** is the cleaner composition; **18b-b** has the gangster's real-skin face in profile and green valve tubes |
| 18c | Low from the desk, the mic huge | aa9e898c · a95209e0 | ⭐ **18c-b: the showman:** both hands up, mouth wide, the chrome mic towering in front, the red padded door. 18c-a: the wave, with the mayoral chain at its best |
| 18d | Wide, the city through the window | 80c03da3 · 7730cf83 | ⭐ **18d-a:** the snowy city full of little lit kitchen windows and chimney smoke, a radio mast with a red light, the red moon, the mayor grinning at the mic: it hands over straight into scene 19. 18d-b: the same through a split window, a bigger city |

**Shortlist:** 18b-a (the beneficiary paying for it), 18c-b (the showman), 18d-a (the handover to 19).

**✅ Scene 18 PICKED (Jack, 2026-10-26): 18d-b** (`7730cf83`): the mayor at the mic, the split window behind him onto the snowy city of lit kitchens, the radio mast, the red moon.

## Scene 19 stills — round 1 (2026-10-26): "K3a lit"

*it is, state, level, manipulation / it is the devil, with a radio station*: **kitchens across the city.** Three windows in
a row, a radio in each: the red family, the blue family, grandma, all leaning in to the same voice. Moves later: the
radios' dial lights.

**Shot spec (`shot-craft`):**
- **For:** the reach. Scene 18 was the voice; this is where it lands: both sides of the brawl and the one person with no
  side, all fed the same broadcast.
- **Visible cost:** bare tables (bread and dripping, one pan), grandma's breath steaming, **her candle burnt lower than in
  scene 6** (second visit: the costed object).
- **Light:** night, snow. Outside: cold blue brick, snow on every sill, the red moon. Inside each window: one warm bulb and
  the radio's glowing amber dial, the one light all three share. Grandma's window: only the candle and the dial, frost
  ferns on the glass.
- **Cast:** red kitchen: a white man in a vest and a Black woman with her hair tied up, a red scarf hung on a chair.
  Blue kitchen: a South Asian man in braces and a white woman in a pinny, a blue scarf on a hook. (Mixed couples on both
  sides, so neither colour reads as a race.) Grandma (scene 6): a tiny white woman in her eighties, thin silver hair in a
  hairnet, a long pointed nose, a mole on one cheek, three cardigans and a crocheted blanket.
- **Radios:** the same 1930s cathedral-top wooden radio in all three windows, glowing dials.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 19a | **Straight-on from across the street:** three windows side by side in one snowy tenement wall, the three households leaning into identical radios |
| 19b | **High from a rooftop opposite:** a whole tenement wall of lit windows, everyone leaning into a radio, the three in the middle row, the radio mast and red moon behind |
| 19c | **Inside the red kitchen, low behind the radio:** its glowing dial huge in front, the couple's real-skin faces leaning in, rapt |
| 19d | **Grandma's window from outside, close:** frost ferns, the candle lower, her ear pressed to the radio, the red moon in the glass |

### Scene 19 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The three households held in every wide (the
red-scarf couple, the blue-scarf couple, grandma), and the radios came out identical, as asked. No lettering.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 19a | Straight-on, three windows | 351d94a0 · ec5512f2 | ⭐ **The scene as written, like a comic strip:** three windows in a snowy blue brick wall, the same radio in each, two warm kitchens and grandma's frosted blue one with her candle. **19a-b** has more real skin and the snow falling. 🟡 Flat and symmetrical by design |
| 19b | High from a rooftop | 590708e6 · 6de31e62 | ⭐ **19b-b: the reach:** a whole tenement wall of windows, every one leaning in to the same glowing radio, the three households in the middle row, the radio mast and red moon behind, snow falling. 19b-a went to one row of three, with a chimney and the mast |
| 19c | Inside the red kitchen | cc07481e · 7b5d164a | ⭐ **The best real skin of the scene:** the couple leaning in, lit amber by the huge carved radio; the red scarf on the chair; the red moon in the snowy window. **19c-b**: the man close to tears, the woman grim. 19c-a: both rapt and anxious |
| 19d | Grandma through the frost | cdb3dc98 · 85f14120 | ⭐ **19d-a:** frost ferns, her ear to the radio, breath steaming, the mole, the hairnet, the red moon in a frosted pane. 🟡 The candle came out tall in both (the "burnt low" stub didn't land). 19d-b: an even taller candle, the hairnet lost |

**Shortlist:** 19b-b (the reach), 19a-b (three windows), 19c-b (the faces), 19d-a (grandma).

**✅ Scene 19 PICKED (Jack, 2026-10-26): 19c-a** (`cc07481e`): inside the red kitchen, the couple leaning in rapt and anxious, lit amber by the radio.
**Note:** the candle-burning-lower beat is not landing in the stills; fix it in Premiere/ffmpeg or by a dedicated re-roll before scene 28.

## Scene 20 stills — round 1 (2026-10-26): "K3a lit"

*stack up the vaults like a wheelbarrow / risk of default is really rather narrow*: **the vault.** Gangsters wheel barrows
of rubber-banded stacks up a plank onto a mountain of money. Moves later: the wheelbarrow.

**Shot spec (`shot-craft`):**
- **For:** the scale. Until now the money has been sheets in the air; here it's a landscape. It also sets up scene 21
  (the mayor on top of the pile) and the wheelbarrow, which comes back as the price of one loaf in scene 30.
- **Visible cost:** a narrow barred window high in the vault wall onto the snowy street: the feet of the bread queue
  going past outside (it pays off in scene 30).
- **Light:** the bottom floor (storyboard: furnace orange, black). **Key:** a row of caged bulbs along the vault ceiling, plus
  the furnace glow through an open iron door in the back wall, orange. **Cold:** the barred window, blue. The stacks' paper
  edges catch the light; deep black between.
- **Money:** "bundles of blank green paper money with no printing, each tied with a rubber band".
- **Cast:** the scene-8 gangsters in pinstripes and shirt-sleeves, sweating: the fat one with a scar through his lip, the
  thin bald one with big ears, the young ginger one with freckles.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 20a | **Low at the foot of the plank:** a barrow wheel huge in front, the plank rising to a mountain of bundles, gangsters toiling up it |
| 20b | **High from the top of the pile looking down:** bundles in the foreground, the plank dropping away, barrows queueing below, the vault door |
| 20c | **Side-on, wide:** the whole vault, the money mountain filling it to the ceiling, the barred window high up with the queue's feet passing |
| 20d | **Close on a gangster pushing:** sweaty real-skin face, barrow heaped with bundles, the mountain behind him |

### Scene 20 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The three scene-8 gangsters came back recognisable
in every wide (fat and scarred, bald with big ears, young ginger). The barred window with the queue's boots in the snow
landed in six of eight. The bundles are blank with rubber bands, and there's no text anywhere.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 20a | Low at the foot of the plank | ed9b8086 · 9b884a32 | ⭐ **20a-a:** a heaped barrow in front, the plank rising past the money mountain, the three toiling up it, the furnace blazing under a brick arch, the queue's boots behind bars. 20a-b: the young ginger one leads; the window is at floor level |
| 20b | High from the top of the pile | fa734e77 · dcd54fe0 | 🟡 The camera stayed low rather than on the pile. **20b-b**: the open round vault door, the furnace, the barred window, the queue of barrows; good geography. 20b-a has a fourth gangster with a different face going up the plank |
| 20c | Wide, side-on | 74226771 · 36296ca8 | ⭐ **20c-a: the line:** three gangsters in step up the plank, the slope of money filling the right half, the barred window of boots on the left, the furnace between. 20c-b: a bigger, paler mountain (the money goes grey-white) |
| 20d | Close on the fat gangster | ba9b6248 · 4130543e | ⭐ **Real skin at its strongest:** sweat, stubble, the scar through his lip, a cigar. **20d-b** has the mountain and the furnace behind him. 🟡 Likeness check owed (heavy-set, slicked hair, cigar: unverified) |

**Shortlist:** 20c-a (the line), 20a-a (the climb), 20d-b (the face).

**✅ Scene 20 PICKED (Jack, 2026-10-26): 20d-b** (`4130543e`): the fat scarred gangster close, sweating, cigar, barrow of bundles, the money mountain and the furnace behind. 🟡 Likeness check still owed.

## Scene 21 stills — round 1 (2026-10-26): "K3a lit"

*Biggie said waaaay back in ninety seven / don't get high off your own supply*: **the vault, top of the pile.** The mayor
lies back on the money mountain, gold chain on his chest, eyes glazed, a banknote over his face like a newspaper on a
beach. Moves later: the note lifting on his breath.

**Shot spec (`shot-craft`):**
- **For:** the high. Getting high off your own supply, played as a sunbather: the money has stopped being a tool and become a
  bed. Quiet after the hustle of scene 20.
- **Visible cost:** the barred window at pavement level just above him: the bread queue's boots in the snow, a foot away
  from his head, and he can't see them.
- **Light:** a single caged bulb hangs low over him like a sun, warm, and the furnace glows orange below. **Cold:** the barred
  window. Mostly black around the pool of light.
- **Gag:** the whole beach kit: shoes off, socks on, trousers rolled, a champagne glass balanced on his belly, bowler tipped.
- **Cast:** the locked mayor with "a heavy gold mayoral chain" lying on his chest.
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 21a | **High overhead, straight down:** the mayor spread-eagled on the bundles like a sunbather, a note over his face, the bulb's pool of light around him |
| 21b | **Low across the pile, side-on:** bundles in front, the mayor reclining, socks on, a glass on his belly; the barred window of boots right above his head |
| 21c | **Close on his face:** the note half-lifted by his breath, one glazed real-skin eye showing beneath, the chain on his chest |
| 21d | **From the foot of the mountain:** the pile rising like a dune, the mayor tiny at the top under the bulb like a sun |

### Scene 21 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The beach kit read every time (socks on, trousers
rolled, champagne glass, bowler tipped). The mayoral chain held in all eight. No text.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 21a | Straight down overhead | 4d6190d1 · 43b0d1f8 | ⭐ **21a-a: the sunbather:** spread-eagled on the bundles, a note over his eyes like a sleep mask, socks on, one shoe off, champagne on his belly, the bulb's pool of light, the barred window of boots in the corner. 🔴 21a-b took his shirt off (bare chest and chain): funny, but off-model and too far |
| 21b | Low across the pile | dd5cd612 · ced306c8 | ⭐ **21b-a: the cost and the high in one frame:** reclining with his hands behind his head, a blissful, smug real-skin smile, the glass balanced on him, and right above his head the barred window with the queue's boots in the snow. 21b-b: shoes kicked off in front, the furnace glowing down a tunnel; the window is further away |
| 21c | Close on his face | 67ff46f6 · 33ba7eec | ⭐ **21c-b:** the note over his face lifting on his breath, one glazed eye and a lazy smile beneath, the chain, the caged bulb: the move written into the frame. 🔴 21c-a sits inside a cream canvas border (crop) |
| 21d | From the foot of the mountain | 3a1f17c2 · e238190e | ⭐ **21d-b: king of the hill:** the dune of money, the abandoned barrow, the mayor on the summit raising his glass under the bulb like a sun, the furnace to one side, the barred window to the other. 21d-a: the same, flatter |

**Shortlist:** 21b-a (the window right above him), 21d-b (king of the hill), 21c-b (the note on his breath).

**✅ Scene 21 PICKED (Jack, 2026-10-26): 21c-a** (`67ff46f6`): close on his face, the note lifting off it, one glazed eye, the chain. 🟡 Cream canvas border: crop in Premiere.

## Scene 22 stills — round 1 (2026-10-26): "K3a lit"

**Chorus 3** *Robbery, robbery! / Call the police…*: **the shop front → the basement: the raid.** Two cops knock at the shop;
downstairs a gangster yanks a huge lever; every press flips round into a bread oven; the band are bakers in white hats.
Omni can't do a state change cleanly, so it's **two stills, before and after, cut on the lever.**

**Shot spec (`shot-craft`):**
- **For:** the punchline the chorus has been building to: "call the police" is answered, and the system hides itself in
  one second. The joke is how fast and how practised it is.
- **Visible cost:** the cops are the street's only hope, and they're about to be fobbed off with bread.
- **Before:** the basement as in scene 12 (emerald lamps, presses spitting notes, the pinstripe band), and one gangster lunging
  at a huge iron lever on the wall, a red bulb flashing above it. **After:** the same room, same camera, warm orange oven light
  instead of emerald: brick bread ovens where the presses stood, loaves on the racks, the band in white baker's hats and
  aprons over their pinstripes, flour on everything, innocent smiles, the mayor holding a baguette.
- **The pairs share a camera** (a+b of each idea = same frame before and after), so the cut lands on the lever.
- **Text:** never "bakery" (it prints itself); the shop is "a shop window full of loaves under a plain blank sign".
- **Variety, declared variable: the frame.**

| # | Idea |
| --- | --- |
| 22a | **BEFORE, side-on basement:** the presses spitting notes, the band playing, one gangster lunging at the lever under a flashing red bulb |
| 22b | **AFTER, the same frame:** ovens, loaves, the band in baker's hats, flour, innocent smiles |
| 22c | **Cross-section, both floors (before):** two cops knocking at the shop door above; directly below, the gangster yanking the lever |
| 22d | **Close on the lever:** a gangster's hand on the huge iron lever, mid-yank, sweating, the red bulb, the presses blurred behind |

### Scene 22 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. **The before/after pair works:** 22b was written to 22a-a's
layout (ovens where the presses were on the left, the stage centre, the mayor on the table, the lever and the ginger gangster
on the right wall), and both 22b stills matched it closely enough to cut on the lever. The shop sign came back blank (no "bakery").

| # | Frame | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 22a | BEFORE, side-on | 7fa5e38e · ba88b0da | ⭐ **22a-a: the before frame:** smiling presses spitting notes under emerald lamps, the pinstripe band on the red-curtained stage, the mayor dancing on a table, the ginger gangster lunging in panic at the lever under the red bulb. 22a-b adds a crowd of hatted drinkers on the left (busier) |
| 22b | AFTER, the same frame | 0a514730 · 197d0ce9 | ⭐ **22b-a: the after frame:** three brick ovens blazing where the presses were, racks of loaves, the band in white chef's hats and aprons with rolling pins, the mayor beaming with a baguette, flour on the floor, the ginger one leaning on the lever in an apron, smoking. **The pair 22a-a → 22b-a is the cut.** 22b-b: the mayor in an apron too, the band less smiley |
| 22c | Cross-section, both floors | ca00dd18 · 230f06c8 | ⭐ **22c-b:** two cops knocking at the loaf-window shop under the red moon, the police car; directly below, a row of pinstripes staring up at the ceiling between smiling presses, and the ginger one yanking the lever under the red bulb. A clean establishing shot for the knock. 22c-a: the lever in a separate red room (a comic-panel look) |
| 22d | Close on the lever | dc6f1f70 · 309173dd | ⭐ **22d-a:** sweating, terrified real skin, both fists on the lever, the red beacon, presses and green notes behind. 22d-b: shirt-sleeves and braces (off-wardrobe) |

**The cut (proposal):** 22c-b (the knock) → 22d-a (the yank) → 22a-a → hard cut → 22b-a (the reveal).
**Shortlist:** 22a-a + 22b-a (the pair), 22c-b, 22d-a.

**✅ Scene 22 PICKED (Jack, 2026-10-26): 22b-a** (`0a514730`): the after frame (ovens, chef's hats, the mayor with a baguette, the ginger one smoking on the lever). 22a-a / 22c-b / 22d-a stay in the bin for the lead-in if the edit wants them.

## Scene 23 stills — round 1 (2026-10-26): "K3a lit"

**Chorus 4** (same words): **the shop doorway.** The cops leave, each with a free loaf under his arm, tipping their hats.
Behind them, the "oven" door glows green ✏️. Moves later: the cops walking off.

**Shot spec (`shot-craft`):**
- **For:** the payoff of the raid. The law came, and left fed. The green glow is the tell that nothing has changed.
- **Visible cost:** the bread queue from scene 20's window, waiting in the snow beside the shop as the cops walk past them
  with free loaves.
- **Light:** night after rain, wet cobbles. **Key:** the shop's warm doorway behind the cops (rim light). **Practicals:**
  the street lamp; the police car's headlamps. **The tell:** a pavement grating in front of the shop glowing emerald from
  below, and a green edge of light under the inner door. Red moon.
- **Cast:** the two cops from 22c (1930s peaked caps, long blue coats; give ordinary features: one tall and thin with a
  grey walrus moustache, one short and round with ginger sideburns). The fat scarred gangster (scene 8/20) in a white
  apron in the doorway, waving them off.
- **Text:** never "bakery"; "a shop window full of loaves under a plain blank sign".
- **Variety, declared variable: the camera.**

| # | Idea |
| --- | --- |
| 23a | **Low on the cobbles, the green grating in front:** emerald light up through the bars, the cops walking away from the shop with loaves, tipping caps back at the waving gangster |
| 23b | **From the queue:** shabby shoulders in the foreground, the cops strolling past the line with their free loaves |
| 23c | **Close on one cop:** real-skin face, a contented bite of the loaf, tipping his cap |
| 23d | **From inside the shop past the counter:** the gangster in his apron waving, the cops in the doorway with loaves, the trapdoor behind the counter glowing green |

### Scene 23 round 1 results (2026-10-26)

NB2, 16:9, ×2, project `dedd295f`, one at a time; all landed first time. The two cops (tall with a grey walrus moustache; short
and round with ginger sideburns) held in all eight, and so did the scarred gangster in his apron. The shop sign stayed blank.

| # | Camera | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| 23a | Low, the green grating in front | 7af31382 · b120463f | ⭐ **23a-a: the tell:** green mist streaming up through the pavement grating in front, the cops strolling off with loaves, tipping their caps, the gangster waving from the warm doorway, the police car's headlamps. 23a-b: the same, the grating cleaner and the gangster further back |
| 23b | From the queue | d465a362 · c3d4849e | ⭐ **23b-a: the cost:** a hungry, mixed queue in flat caps and headscarves, real-skin faces watching the cops stroll past with free loaves, the gangster waving, snow, the red moon. 23b-b: the queue more lined up, the cops mid-frame |
| 23c | Close on the cop | 9d789cfd · e0da036f | ⭐ **23c-a:** eyes shut in bliss, a big bite of the loaf, crumbs in his walrus moustache, tipping his cap, the shop and the green grating behind. 23c-b: the same, a stubbled real-skin face |
| 23d | Inside, past the counter | 92b13bfd · 45c5702a | ⭐ **23d-b:** the trapdoor wide open behind the counter glowing emerald, the gangster waving them off, the cops in the doorway with their loaves under the red moon. 23d-a: the gangster's face large and real, the trapdoor smaller |

**Shortlist:** 23b-a (the queue watching), 23a-a (the green tell), 23d-b (the open trapdoor), 23c-a (the bite).

**✅ Scene 23 PICKED (Jack, 2026-10-26): 23d-a** (`92b13bfd`): inside the shop, the scarred gangster waving them off, his real face large, the trapdoor glowing green, the cops in the doorway with loaves.

## Scenes 24–33 — round 1 (2026-10-26): "K3a lit", my picks

Jack, 2026-10-26: *"please just make them and you pick which one to use, basically as long as it fits the style and they have
the cartoon-like realistic faces, it looks pretty and cinematic, then choose them. Please avoid elements of AI slop … optimise
for Nano Banana 2.1 / Omni Flash … use the cinematography file and skills."* So from scene 24 on, **I pick**; Jack can swap any.

**Method:** shot-craft gates on each scene (what it's for, the visible cost, a named light source); `docs/cinematography/symptoms.md`
"looks like AI" counters (break symmetry, one source, obstruct part of the frame, one specific detail); the K3a lit lead and the
rules from scenes 7–23 (`docs/google-flow/2026-10-26-pretty-not-slop.md`, now confirmed on **Nano Banana 2.1**). Three cameras a
scene (four on the ending), ×2 each, NB2.1, 16:9 (29a 9:16), project `dedd295f`, one at a time. Prompts in the provenance cards.

| # | For | Visible cost | Key light | Cameras |
| --- | --- | --- | --- | --- |
| 24 | The heat goes nowhere but down | The pipe capped at the basement ceiling; frost on the shop floor above | The furnace mouth | a cross-section · b low at the fire · c close on the stoker |
| 25 | Money that only rats eat | Rats fat on bundles while the queue starves upstairs | One green-shaded lamp | a rat at floor level · b overhead on the counting table · c towers like a city |
| 26 | The loaf costs the whole packet | The empty pay envelope | The shop lamp | a over the seller's shoulder · b close on the palm · c the chalkboard wiped |
| 27 | "Bail" and "out" | The city's lights he's sinking in front of | City lights on black water | a waterline · b from a bridge · c close on him |
| 28 | Own the printer, don't fear winter | The candle drowned in its own wax | The guttering flame / the red-hot pipe | a grandma · b the hot basement · c both floors in one frame |
| 29 | The wealth gap as height | The whole building | Gold at the bottom, ice at the top | a 9:16 tall · b 16:9 |
| 30 | The price of a loaf, in a line | Coin → fistful → bag → bucket → wheelbarrow | The shop window | a down the queue · b low side-on · c from above |
| 31 | They look down together | — (the turn) | The green trapdoor | a up from the trapdoor · b the crammed shop · c the street turning |
| 32 | Let them eat cake | The silent presses | The furnace behind him | a over the crowd · b close on him · c wide |
| 33 | The bookend: everyone's gone downstairs | Two scarves in a puddle | The red moon in a puddle | scene 1's W3 prompt, street emptied (pre-lit-lead style, to match W3b) |

### Results, scenes 24–33 (my picks, 2026-10-26)

| Scene | Media (a · b per camera) | Pick | Why / notes |
| --- | --- | --- | --- |
| 24 | a 45dc28ff · 4fce29af · b 54eab8cc · 92b87c5f · c 499afb10 · 3672a29c | ✅ **24a-b** (`4fce29af`) + cutaway 24b-b (`92b87c5f`) | 24a-b tells it: the stoker feeds notes to the furnace, the copper pipe climbs into the warm card-playing basement and ends there, under a shop floor hung with icicles. 24b-b is the prettiest fire (sparks, real skin). 🟡 24a-a has a cream strip at the left edge. 24c: good real skin, but no story |
| 25 | a 8e1625b5 · bb37adfe · c 77adb3d4 · 3e3e7c7f (b skipped) | ✅ **25a-b** (`bb37adfe`) | A painterly rat in front gnawing a bundle, towers of money, two more rats, the gangster counting under the green lamp without noticing. 25a-a's rat is too cute. 25c invented extra workers (an old labourer slumped among the stacks in c-b) and a tiny desk scribble in c-a |
| 26 | a 363c8ee7 · 417fd6c7 (b, c skipped: a landed) | ✅ **26a-b** (`417fd6c7`) | The baker tips his whole pay packet out (a thin trickle of coins) for one loaf; the scarred seller in the foreground; a big blank chalkboard behind for the ffmpeg price; loaves warm, the window cold blue. 🔴 26a-a's seller wears an apron over a bare back |
| 27 | a 334137a6 · d5e86478 (b, c skipped: a landed) | ✅ **27a-b** (`d5e86478`) | "Bail and out": the mayor pours a bucket of water and soggy notes over the side, notes floating all round, the city's lights and the red moon streaking on black water; real-skin, worried. 27a-a: the same, with the oar and more notes, the face flatter |
| 28 | a 9187fa87 · 8febbc4f · b 68beec54 · a23a9340 (c skipped: the pair landed) | ✅ **28a-b** (`8febbc4f`) **→ 28b-a** (`68beec54`) | The cut, as written. **28a-b:** grandma's real-skin face, frost in her eyebrows, blue lips, breath steaming, and **the candle finally burnt out: a puddle of wax with a tiny flame** (the costed object pays off). **28b-a:** gangsters in vests and braces sweating in armchairs, ice buckets, one flat on a pile of money with a damp cloth on his head, the copper pipe glowing orange. 🔴 28b-b repeats one face four times (clones) |
| 29 | a 9:16 a9b52c37 · 86528c08 · b 9:16 22291019 · ae848e6f (b landed after a 99% timeout) | ✅ **29b-b** (`ae848e6f`) | The whole building in one tall frame for the Premiere ride up: the frozen attic with grandma, the cold shop and its queue, the mustard stair, the emerald Mint with the on-model mayor dancing on a table, the furnace and the barred vault. 🔴 29a: an undescribed "the mayor" came back with a French sash (and a top hat in 29a-b): **always paste the full mayor line**. 🟡 29b-a sits on a canvas border. 🟡 Soft at 768 px wide if panned (see scene 12) |
| 30 | a 871a420b · c306b595 (b, c skipped: a landed) | ✅ **30a-a** (`871a420b`) | The price of a loaf in one line, read left to right: one coin, a fistful, a bag, a bucket of notes, a wheelbarrow, a mixed queue with real-skin faces in the snow beside the warm window. 🔴 30a-b paints "$" on the bag |
| 31 | a bda4d496 · a5126026 · c 3dad2b8e · b410fa2e (b skipped) | ✅ **31c-b** (`b410fa2e`) **→ 31a-a** (`bda4d496`) | 31c-b: the red-scarf crowd and the blue-scarf crowd squared off, fists up, the green glow rising from the grating at the shop door between them: the start frame for the Omni clip (the heads turn to the green). 31a-a: **the turn landed**: looking straight up out of the trapdoor at a ring of real-skin faces, red and blue scarves side by side, lit green. 🟡 31a-b's geometry is muddled (the trapdoor ends up in front of them) |
| 32 | a 54f5efa3 (1st call "failed, not charged", retry landed 1 of 2) · b 356afd26 · 238809b3 (c skipped) | ✅ **32a-a** (`54f5efa3`) **→ 32b-a** (`356afd26`) | 32a-a: the silent mixed crowd, red and blue scarves together, the on-model mayor against the glowing furnace door holding out a white tiered cake, the presses' painted faces looking away, notes on the floor. 32b-a: close, sweating, a desperate grin, the cake on its silver tray, the furnace bars glowing, crowd silhouettes at the edges (the iris-out frame). 🔴 32b-b sits on a white border with cartoon shake lines |
| 33 | a 47982df5 · 95e88e68 | ✅ **33a-a** (`47982df5`) | The bookend of scene 1's W3b: the same rusty parapet and steep look down the street, now empty and still; a red scarf and a blue scarf drowned together in one puddle, the red moon in the next, one candle-yellow window, the green glow rising from the grating. 33a-b: the same, darker, cleaner parapet |

**All 33 scenes now have a still (2026-10-26).** Skipped cameras (25b, 26b–c, 27b–c, 28c, 30b–c, 31b, 32c) were not needed once a camera
landed the scene; their prompts stay in the scratch prompts and can be run on request.

**What's still owed before the Omni pass:** (1) Jack's eye on my picks for 10, 12, 24–33; (2) likeness checks flagged on 8a-b,
9d-a, 20d-b (unverified); (3) crops: 21c-a, 29b and any canvas-border picks; (4) the song take (no timings yet); (5) recurring
cast as Flow Characters (baker, grandma, mayor, the scarred gangster, the two cops, the leaders).
