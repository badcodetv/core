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
