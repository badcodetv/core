# The Speakeasy Mint — storyboard

The Bank Robbery song's music video. Chosen by Jack 2026-10-25 (idea 8 in
[`../music-video-ideas.md`](../music-video-ideas.md)). Lyrics: Kai's (`../sealed-r5/lyrics.txt`). The
song take is not picked yet, so this is timed by lyric section, not by seconds.

## ▶️ Resume here (end of 2026-10-25)

**Where we are:** the style is locked, the script is written, and we're making **one still per scene, in order**.

- **Style LOCKED = K3a** (`d81d7f7a`, Flow project `dedd295f` "Oct 25 - 09:43"): sitcom figures with real-skin faces,
  every colour in thick oil brushstrokes, the small red moon. Its exact prompt is under "K sweep" below; the
  style lead used for each scene is in `script.md`.
- **Format: 16:9** (Jack, scene 1 round 2).
- **Script draft 1: [`script.md`](./script.md)**: 33 scenes on Kai's lyrics, each in its own setting. Gags marked ✏️
  are proposals; Jack writes the jokes. Not yet timed (no song take picked).
- ✅ **Scene 1 picked: W3b** (`5cbcf7a8`): roof parapet, the street running away, police car, red moon in a puddle.
- 🟡 **Scene 2 (bakery kitchen, 4 a.m.): round 1 done, Jack's pick owed.** Shortlist **2d-a** (`7745180e`, close on
  the tired ginger baker) and **2c-a** (`06c543ca`, from the ceiling corner). 2b's oven-mouth framing is worth a re-run.
- ⬜ **Next:** Jack picks scene 2 → scene 3 (the pay packet at the back door, dawn) → on through the script. Then one
  Omni Flash test clip of a picked still before any batch of clips.

**Rules learned today (all in `script.md` / `docs/google-flow/nano-banana-2.md`):**
- 🔴 Real-skin faces + a bare demographic ("an older Black man") = a famous actor's likeness. Give every person
  specific ordinary features (build, hair, nose, a scar) and check every face for a celebrity likeness.
- Name crowd mixes outright ("young and old, men and women, Black, white and South Asian"); "mixed" is ignored.
- Press faces = "simple faces painted on their sides" ("cheerful 1930s cartoon faces" gave a game-mascot lookalike).
- No neon (it prints sign text); "plain margins with no writing" on every prompt; all real text goes on in ffmpeg.
- Flow: when a call times out at 99–100% the stills still land: list the newest tiles over CDP and fetch them
  (`flow-content.google/image/<id>`). "Unusual activity" = refresh the project and retry. Don't script the page
  between generations.

**How we got here (all on 2026-10-25, sections further down):** ten-style sweep → video-game sweep (V1–V8) →
pixel-world mix (M1–M4) → own-look sweep (C1–C4, the wrong question) → Jack: keep round 3a's sitcom style → twist
sweep (T3 red moon kept) → realism sweep (R1–R6; Jack picked R5a, real-skin faces) → K sweep (R5a + R6's painting;
**Jack picked K3a**) → script → scene stills.

## What Jack locked (2026-10-25)

*(The "1930s rubber-hose cartoon" style below was the starting brief; the style is now K3a, see Resume.)*

- A 1930s Prohibition speakeasy, as a **1930s rubber-hose cartoon** (the old Fleischer-era look; we
  never write "Cuphead" in a prompt). Gangsters print money; the mayor is there.
- **The building is a cross-section**, side wall off like a doll's house. Police cars and protest on
  the street; **each chorus drops the camera one floor; verses ride back up; the last chorus
  reaches the bottom.**
- **The front is a bakery.** Bread upstairs, cake downstairs, the cake ending.
- **The password "quantitative easing"** at the door slot, in a cartoon speech bubble.
- **The raid:** a cop knocks, a lever, the presses flip into bread ovens, the cops leave with a free loaf.
- **The left leader and the right leader dance with the mayor downstairs** while their crowds fight
  on the street.
- **The furnace burns notes and heats the basement only.** Grandma freezes in the attic.
- 🔴 **Check the caricatures in every frame** (below).

## The building, top to bottom

| Floor | What's there | Light | Colour |
| --- | --- | --- | --- |
| **Attic** | Grandma's room: frost, a candle, a radio | one candle | ice blue, candle yellow |
| **Street + shop** | The bakery "Honest Bread": a queue, the counter, the crowds outside, police cars | street lamp + shop window | brick red, cream |
| **Back stairs** | A plain door with a slot | one bare bulb | mustard |
| **The Mint** (basement) | The speakeasy: presses, a jazz band, the mayor, the two leaders, notes like confetti | press lamps + stage spots | emerald, gold, scarlet |
| **The bottom** (sub-basement) | The furnace burning notes; the vault, rubber-banded stacks, rats | furnace fire | furnace orange, black |

**Why the floors work:** the height of the building is the wealth gap. Warm and gold at the bottom,
frozen at the top. The beneficiary (whoever owns the press) is in frame every time we go down.

## Shot list against the lyrics

Camera moves are done in Premiere over tall stills (`docs/video-fx/hybrid-method.md`); each window
gets its own short Omni loop with the camera locked. One thing moves per clip.

| # | Lyric section | Floor | What we see |
| --- | --- | --- | --- |
| 1 | *They say, ya can't make money from a tree … nobody knows!* | street | Night. Police cars nose to nose, sirens spinning. A left crowd (red banners) and a right crowd (blue banners) shove each other outside the bakery. Wide, the whole frontage. |
| 2 | *means of production … Get wrecked!* | attic | Ride up the wall to the attic window. Grandma in her coat and hat, breath steaming, a single candle (**"grandma FREEEEZING!"** lands on her). A brown envelope slides under her door on *stimulus checks*. |
| 3 | *rent seeking?… I'm just about eating … interrupt your meeting?* | shop | Down to the bakery counter: a queue for one loaf each, prices chalked high on a board. The baker's smile is too wide. |
| 4 | *remember kids, the Fed is not your friend … the government spends* | shop | A delivery of flour sacks goes in the front; sacks of money come up out of a trapdoor behind the counter. |
| 5 | *this fiat system … the facts I'm stating* | back stairs | A gangster in a pinstripe suit knocks on the plain door. The slot opens: two eyes. A speech bubble: **"QUANTITATIVE EASING"**. The door swings. |
| 6 | **Chorus 1** *Robbery, robbery!* | ↓ back stairs → Mint | **First drop.** Down the stairs and through the floor into the Mint: rows of presses, sheets of banknotes, a jazz band, notes like confetti. |
| 7 | **Chorus 2** *Printer is burrrrning* | Mint | Push in on the biggest press, glowing red hot, throwing notes. The mayor (sash, top hat) feeds it with a shovel. |
| 8 | *Stacks and stacks of elastic cash … witness the theft* | ↑ street | Back up to the street: the two crowds fighting, the shop window between them. |
| 9 | *blaming each other … between the factions* | cross-section | 🔑 **The money shot.** The cut-away in one frame: upstairs the crowds fight; directly beneath them, the red leader and the blue leader dance arm in arm with the mayor. |
| 10 | *divide and conquer … the devil, with a radio station* | attic + Mint | Grandma's radio crackles; follow its wire down the wall to a microphone in the Mint, where the mayor is reading the news. |
| 11 | *stack up the vaults like a wheelbarrow … your own supply* | street | A police car pulls up at the bakery. Two cops get out. |
| 12 | **Chorus 3** *Call the police, it's a robbery!* | shop → Mint | **The raid.** A cop knocks; downstairs a gangster yanks a big lever; every press flips round on its floor into a bread oven; the band are now bakers in white hats. |
| 13 | **Chorus 4** *Debasement!… in da basement!* | ↓ the bottom | The cops leave with a free loaf each. **Last drop**, through the Mint's floor to the bottom: the furnace, a man shovelling banknotes into the fire. |
| 14 | *You know the real star is Pablo … not plastic hands* | the bottom | The vault: rubber-banded stacks to the ceiling, rats nibbling the bundles (the rats eat money; they never stand for people). |
| 15 | *and this right here is a next level scam … don't fear winter* | bottom + attic | The furnace's heating pipe climbs the wall and stops dead at the Mint's ceiling. Cut to grandma, frost on her candle. |
| 16 | *crime is asset inflation … not to worry* | the whole building | Ride all the way up the cross-section in one move, gold at the bottom to ice at the top. |
| 17 | *hungry people, feed a revolution … perhaps some execution* | street → stairs | The crowds stop fighting each other. Both turn and look down at the trapdoor. They pour down the back stairs together. |
| 18 | *it's time to give … don't just eat cake* | Mint | The mayor, cornered, holds out a tiered cake on a silver tray. Iris out. |
| 19 | (end card) | — | A narrator card: "She never said it, by the way." (Marie Antoinette never said "let them eat cake"; it traces back to Rousseau.) Then the BadCode logo. |

Lines 17 and 18: *"perhaps some execution"* stays a word in the song; we show nobody hurt. The crowd
arriving is enough.

## 🔴 The caricature check (every frame, before Jack sees it)

1930s cartoons carry racist design habits and the engine may reach for them on a "1930s cartoon" prompt.
Every still and every clip is checked for:

- **Minstrel faces:** big pale lips, black-face, white "minstrel" gloves on dark faces. We never ask for
  white gloves.
- **Antisemitic banker:** hooked nose, fat cigar banker drawn as a racial type, money-grabbing hands.
  Our gangsters and the mayor are drawn as **ordinary** cartoon men; fat, thin, short, tall, any
  ordinary nose.
- **No other ethnic stereotype** in the crowds or the band (a jazz band is the riskiest spot).
- **Rats eat the money and never stand for people.**
- **Left and right drawn to the same scale and dignity.** The crowds are angry for real reasons; the
  joke is on the mayor and the press, not on them.

A frame that fails is regenerated, never shipped with a note.

## Text on screen

The password bubble and the end card are **added afterwards in ffmpeg**, not asked of the video model
(Omni cannot hold small readable text, `docs/google-flow/README.md`). A still can try its own bubble;
the clip gets the overlay. The shop sign "Honest Bread" the same.

## Stills (style first)

Stills before any video (house rule). The first job is the **style**: one still that settles what
the cartoon looks like, before any shot list is made.

### Style test 1 — the cross-section (2026-10-25)

Shot spec (shot-craft): **For** setting the whole idea in one picture, the building as the wealth gap.
**Cost in frame:** grandma freezing at the top, the fighting crowds. **Light:** a street lamp outside,
press lamps in the Mint, the furnace at the bottom, one candle in the attic; warm gets stronger the
lower you go. **Depth:** the street and the crowds in front, the building cut open behind. **Camera:**
straight on, eye level with the shop, flat like a cartoon background. **Withheld:** the faces of the
leaders (backs to us).

Settings: Nano Banana 2, 9:16, 4 outputs. Flow project: see the revision log.

```prompt
A 1930s rubber hose cartoon, hand inked with bouncy limbs, painted watercolour backgrounds and the warm grain of old Technicolor film. A tall city building shown in cross-section with its side wall cut away like a doll's house. At street level a bakery with a cream and brick red front; a red crowd and a blue crowd shove each other on the pavement under a street lamp, a police car beside them. In the attic, an old woman in a coat shivers by one candle in an ice blue room. Below the bakery, a secret emerald and gold basement full of printing presses throwing banknotes into the air, a jazz band, a mayor in a top hat dancing. At the very bottom a furnace burns orange. Ordinary faces, no white gloves. Thanks.
```

Flow project: `dedd295f-a519-46bb-aeb8-0e422a58e757` (shows as "Oct 25 - 09:43"; renaming a project
can't be automated). Nano Banana 2, 9:16, 4 outputs per round.

**Round 1** (the prompt above). Layout right first time in all four: attic → floors → bakery + street →
green Mint → furnace. **Style wrong:** a modern storybook watercolour, not 1930s. Only 1a gave the
press a face. 1a has a TV (wrong decade) and a "brrrr" caption. Media 8646b7d6, e6a7129b, e09bd0c5,
2686d0ab.

**Round 2**, one change: only the style clause rewritten.

```prompt
A frame from a 1930s black-ink cel cartoon: bendy rubber hose arms and legs with no elbows, pie-cut eyes, everything bouncing in time, flat bright Technicolor colours, thick ink outlines, painted backgrounds, scratchy old film grain. The objects have faces and dance too. A tall city building shown in cross-section with its side wall cut away like a doll's house. At street level a bakery with a cream and brick red front; a red crowd and a blue crowd shove each other on the pavement under a street lamp, a police car beside them. In the attic, an old woman in a coat shivers by one candle in an ice blue room. Below the bakery, a secret emerald and gold basement full of printing presses throwing banknotes into the air, a jazz band, a mayor in a top hat dancing. At the very bottom a furnace burns orange. Ordinary faces, no white gloves. Thanks.
```

Much closer: presses, furnace, lamps, bread and furniture all have faces and bounce. The people
are still drawn like modern comics (no pie-cut eyes on humans). Media fb74afca (2a), 26a53f2d (2b),
ef5f0c51 (2c), 47edaf77 (2d).
- **2d** best: the grain, the colour, the cakes in the bakery window, the angry furnace.
- **2a** second: the grinning furnace, the bouncing furniture.
- 2c printed junk labels ("SUB-LEVEL 1 (Basement)"); 2b's police car says "TAXI".

**Caricature check, round 2 (zoomed on the bands and the mayor):**
- ✅ No minstrel faces: the Black musicians have ordinary features in all four.
- 🟡 In every take the only Black people in the building are the band, playing for a white mayor.
  It's a 1930s role pattern even without a caricature. Fix in the next round: a mixed band, and mixed
  crowds on the street.
- 🔴 **The mayor drifts into the Monopoly man** (top hat, white moustache, gloves: 1a, 2c, 2d). That's
  Hasbro's mascot. "A mayor in a top hat" is summoning him. Redesign the mayor.
- 🟡 "No white gloves" was ignored on the mayor and the presses in 2d.

### The style, re-ruled (Jack, 2026-10-25)

Jack: *"i think we should make it look more modern, like a simpsons style, mixed with rick and morty, and
the cuphead style elements subtly added. Please avoid elements of 'AI slop'."*

**How it goes into a prompt.** No show is named, for the same reason "Cuphead" never is (an AI copy
of a named studio's look is the 2025 Ghibli backlash; practitioner guides also say to use broader
visual language rather than a franchise name). The traits are named instead:
- **The sitcom (Simpsons) half:** flat colour, one shadow tone, simple rounded people, big round eyes
  with small dot pupils, overbites. **Not** yellow skin; that is the one trait that would make it a
  copy, and the crowds must be mixed anyway.
- **The sci-fi cartoon (Rick and Morty) half:** slightly wobbly hand-drawn outlines, lanky
  limbs, tired eyes, a toxic green glow (the Mint's light).
- **The 1930s half, subtly:** only the *objects* are rubber-hose (presses, furnace, bread with faces),
  plus faint film grain. Old cartoon things living in a newer cartoon world.

**Anti-slop rules for this cartoon** (repo: `docs/google-flow/nano-banana-2.md` anti-slop toolkit,
`2026-10-08-anti-slop-sweep.md`; web pass 2026-10-25):
- Slop is **polish**: smooth gradient shading, glossy sheen, airbrushed 3D-ish volume, perfect
  symmetry, a generic blend of styles. → Flat colour, one shadow tone, a line that wobbles.
- **Kill-list words:** "modern", "clean", "professional", "high quality", "cinematic", "8K". ("Modern"
  is out, so the prompt says *prime-time adult animated sitcom*.)
- **Gibberish text** is the commonest art tell → no text asked for; the one sign is short block capitals,
  and real text goes on in ffmpeg.
- **Give decisions, not adjectives** (practitioner): a named colour per floor, named light sources.
- **One cartoon look locked and reused word for word** in every prompt of the video. Without a fixed
  style phrase the model drifts back to its average.
- **Too busy reads as AI:** a floor holds one idea.

**Cinematography (shot-craft gates):** *For:* the whole argument in one picture, the height of the
building as the wealth gap. *Cost in frame:* grandma at the top, the fighting crowds. *Light:* a yellow
street lamp and the Mint's green lamps (two lights, two colours, both in the world), the candle, the
furnace. *Depth:* crowd and police car on the pavement in front of the cut-away. *Camera:* straight
on and level with the shop, the flat elevation a cartoon background uses. Two fixes ride with the
style change because they're caricature/trademark fixes, not taste: **the mayor redesigned** (tall,
skinny, bowler, gold chain) and **a mixed band and mixed crowds**.

### Round 3 (2026-10-25)

Nano Banana 2, 9:16, 4 outputs, same project.

```prompt
A still from a prime-time adult animated sitcom: flat colours with one shadow tone, slightly wobbly hand-drawn black outlines, simple rounded people with big round eyes, small dot pupils and overbites, faint old film grain. A tall city building cut open in cross-section like a doll's house, seen straight on. In the attic an old woman in a coat shivers by one candle in an ice blue room. At street level a cream and brick red bakery; a red crowd and a blue crowd of mixed ages and skin tones shove each other under a yellow street lamp, a police car beside them. Below, a secret emerald basement in toxic green lamplight: printing presses with cheerful 1930s cartoon faces throw banknotes into the air, a mixed jazz band plays, and a tall skinny mayor in a bowler hat and gold chain dances. At the very bottom an orange furnace. Thanks.
```

Media 567940d3 (3a), e0dd52c8 (3b), 40d7d780 (3c), 6f08b43e (3d).

**What came back:** the style landed. Flat colour, a slightly wobbly line, round eyes with dot pupils,
overbites, and the presses kept their 1930s faces in all four (the subtle old-cartoon element). The
crowds are mixed on both sides. The mayor is no longer the Monopoly man (bowler, gold chain, lanky)
in all four.
- **3a** best: the clearest sitcom read, every floor legible, the bakery, the police car.
- **3d** second: the biggest, liveliest crowd.
- 3b and 3c are emptier.

**Slop check:**
- 🟡 The lamp cones are soft airbrushed gradients (3b, 3c), the one polished-looking thing left.
  A flat lamp shape would be more cartoon.
- 🔴 3a has a gibberish "signature" in the bottom-right corner (a named AI tell). Crop or regenerate.
- 🟡 3b prints "Bakery" twice; 3d has a second cut-off "BA" sign.
- The middle floors filled up with TV-watchers nobody asked for. They're neutral; they could be the
  neighbours, or the floor could be cut.

**Caricature check (zoomed):**
- ✅ No minstrel features; the musicians are drawn like everyone else.
- 🔴 **"A mixed jazz band" was ignored in 4 of 4.** It's an all-Black band playing for a white mayor
  again (12 of 12 band takes so far). The 1930s-jazz prior is stronger than the word "mixed". The next
  round names each player differently, or replaces the band (the gangsters play, or a gramophone).

**Open question for Jack:** the pictures drifted to the present day (CRT tellies, a modern police car).
Is it a 1920s Prohibition setting drawn in a newer cartoon style, or today's city with a speakeasy
under it?

## Style sweep (Jack, 2026-10-25)

Jack: *"please try a bunch of different styles that would fit badcode and the theme."*

**Method:** one fixed scene paragraph, eight style clauses, so the only variable is the style. The style
clause goes first (front-loaded, per `docs/flow/` rule 3). Nano Banana 2, 9:16, 2 outputs each, run one at a
time. No artist or show is named in any prompt (rule zero; living-studio copying); each style is named by
its traits and its period.

**Fixes carried into the shared scene:**
- **The band is the gangsters themselves**, in pinstripes. "A mixed jazz band" was ignored 12 of 12 times
  (`docs/google-flow/nano-banana-2.md`, cartoon pass).
- **"Four floors only"**, so no filler flats of TV-watchers.
- The mayor as in round 3, which fixed the Monopoly drift.

**Shared scene paragraph (identical in all eight):**

> A tall city building cut open in cross-section like a doll's house, seen straight on at night, four floors
> only. Attic: an old woman in a coat shivers by one candle. Street level: a bakery; a red crowd and a blue
> crowd of mixed ages and skin tones shove each other under a street lamp, a police car beside them.
> Basement: printing presses throw banknotes into the air while gangsters in pinstripe suits play jazz and a
> tall skinny mayor in a bowler hat and gold chain dances. Bottom: a furnace burns. Thanks.

**The eight styles, and why each fits:**

| # | Style | Why it fits BadCode and the song |
| --- | --- | --- |
| S1 | **Georgian satirical etching**, hand-coloured, 1790s | Britain invented the money-printing cartoon: in March 1797, after the Bank stopped paying out gold, Gillray drew Pitt as Midas, eating gold and spewing banknotes (*Midas, Transmuting all into Paper*, Bank of England Museum). Ours is its great-grandchild, and it's British |
| S2 | **Banknote engraving**: fine intaglio lines, guilloche patterns, two inks | The video is drawn in the material it's about: the money draws the robbery |
| S3 | **Cut-out paper collage** of Victorian engravings | The 1970s British TV-comedy animation tradition; the political collage videos (Sleaford Mods' *UK GRIM*) live here. We use engravings, never photos of real people |
| S4 | **Constructivist propaganda poster** | Political poster grammar: bold diagonals, red and black. Plays the mayor's own propaganda back at him |
| S5 | **1960s limited-animation heist titles** | Flat cut-paper shapes, no outlines. The look of 1960s heist and spy film titles, which suits the funk |
| S6 | **Linocut protest print**, two colours | The leaflet and protest-poster tradition (an Austrian film animated the 1934 February Uprising in linocut for exactly this reason) |
| S7 | **Risograph punk zine**, misregistered | DIY print, fluorescent ink, grain; the anti-polish style, and the furthest from slop |
| S8 | **BadCode noir**: near-black ink, one thin light per floor | The house register (`new-image`): darkness as the canvas, one light, the presses as monumental machines, gold as the only bright colour |

**The style clauses** (each prompt = clause + the shared paragraph):

- **S1:** `A hand-coloured satirical etching from 1790s London: fine crosshatched ink lines on cream laid paper, loose watercolour washes in vermilion, Prussian blue and yellow ochre, exaggerated but ordinary human faces, plate marks at the edges.`
- **S2:** `Drawn as a banknote engraving: every shape built from fine parallel intaglio lines and crosshatching, guilloche swirls for the smoke and the light, printed in two inks, deep banknote green and sepia brown, on off-white security paper.`
- **S3:** `Cut-out paper collage animation: figures and buildings cut from Victorian black and white engravings, glued flat with visible paper edges and small drop shadows, tinted with flat washes of tomato red, mustard and sky blue.`
- **S4:** `A 1920s constructivist propaganda poster: bold flat shapes on strong diagonals, only red, black and cream, coarse halftone dots, blocky geometric figures, the building tilted dramatically.`
- **S5:** `1960s limited-animation film titles: flat cut-paper shapes with no outlines, slightly misaligned colour blocks, a palette of mustard yellow, tomato red, olive green and black, simple angular figures, a texture of printed card.`
- **S6:** `A two-colour linocut protest print: black and scarlet ink on cream paper, bold carved gouge marks, uneven ink coverage with small white specks, chunky simplified figures.`
- **S7:** `A risograph-printed punk zine: fluorescent pink and bright blue inks slightly misregistered, heavy grain, rough hand-drawn figures, photocopier smudges.`
- **S8:** `A near-black ink graphic novel: most of the frame solid black, each floor lit by its one thin light, deep unlit shadows, hard ink edges, the printing presses huge machines towering over the people, gold banknotes the only bright colour.`

Results per style below.

**Added mid-sweep (Jack, 2026-10-25): "or maybe like mafia game cartoon style".** Two readings, both tried. No game
is named in the prompt; *MOUSE: P.I. For Hire* (a noir 1930s-cartoon gangster game) is the closest existing
reference found, and period gangster art leans on Art Deco as the look of the underworld's excess.

- **S9 — gangster game cartoon:** `Stylised gangster video game key art: chunky cel-shaded characters with huge square jaws, broad shoulders and tiny legs, matte flat colours with one hard shadow, an Art Deco city in deep burgundy, brass gold and bottle green, thick black outlines.`
- **S10 — 1930s gangster comic strip:** `A 1930s newspaper gangster comic strip: heavy black brush outlines, angular square-jawed faces, flat primary red, yellow and blue printed with visible coarse dots on yellowed newsprint, Art Deco buildings.`

### Style sweep results (2026-10-25)

All ten ran on the first try (NB2, 9:16, 2 each, project `dedd295f…`). Contact sheets were checked whole, then
zoomed where faces or text were small. The pinstripe-gangster band fixed the all-Black-band problem in every
style (the players are gangsters now, of mixed looks); the bowler mayor held in all twenty.

| # | Style | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| S1 | Georgian etching | f9ce3307 · dd516601 | Beautiful and the most British. 🔴 **1a forged a "James Gillray" signature and gibberish verse under the plate** (nobody was named in the prompt); 1b's caption "The London Doll-House; or, The Way of the World" is legible, but there's small signature text again. Any use crops or covers the margin. Drags the clothes to the 1790s. 1a has a raised knife in the crowd |
| S2 | Banknote engraving | cee46924 · 75b1e530 | Clever and clean, but nearly grey: fails the "more colour" rule. 2a added RED/BLUE placards |
| S3 | Paper collage | 39eb2207 · 10dffbe9 | Did **not** come out as collage: a detailed coloured engraving instead. Busy |
| S4 | Constructivist poster | 9bc1a37e · e6f00874 | Strongest graphics. 4b invented slogans ("THE CITY", "ONLY") and Cyrillic. 🔴 A Soviet poster reads as "communist" to the reader we're trying to reach (`the-reader.md`) |
| S5 | 1960s heist titles | b9f8125b · 4b0e24b6 | The cleanest and most readable; suits the funk. Flat shapes should be the easiest for Omni to move (inferred, untested) |
| S6 | Linocut protest print | de1b7078 · 19b80a82 | Bold, readable, angry. 🟡 The red crowd got the colour and the blue crowd stayed black, so the sides aren't equal; give each side an ink |
| S7 | Risograph zine | 4f7a4b58 · 5b0266c0 | 7a good, punk and colourful. 7b wrote labels ("DIY PUNK ZINE", "TOP ATTIC"): the prompt read literally |
| S8 | BadCode noir | 288fc960 · dc1732e7 | The house register, but the small figures vanish in the black; only the gold basement reads (`symptoms.md`: near-black needs one bright region, and this has one per floor at best). Weakest for a cross-section |
| S9 | Gangster game cartoon | a1cf80ad · 3be1345a | The "mafia game" look: square-jawed, matte cel shading, Art Deco. Faces fine at zoom. 9b adds a trenchcoat heavy at the door |
| S10 | 1930s comic strip | e4a7d7bc · 36e5a4f8 | 10b lovely: Art Deco frame, newsprint colour. 10a invented a masthead and floor labels |

**Slop and text, across the sweep:** every style that suggests *print* (etching, zine, comic strip, poster)
invents text: captions, labels, signatures, mastheads. **Next round, every print style says where the paper ends
and that the margins are blank**, or the frame is cropped. Real text goes on in ffmpeg.

**For Omni (inferred, untested):** fine hatching (S1, S2, S3) is likely to shimmer and "boil" when animated;
flat shapes (S4, S5, S6, S9) should hold. One test clip of the chosen style answers it.

## Video-game sweep (Jack, 2026-10-25)

Jack: *"how about we try a bunch of video game styles, like gta, red dead redemption 2, mafia. Please avoid
elements of 'AI slop' … optimise this prompt for Nano Banana 2/Omni Flash … use the cinematography file."*

**Rule zero holds:** no game, studio or show is named in any prompt. Each style is described by its traits
and its period. *(Web pass 2026-10-25: Google has blocked Disney requests since its cease-and-desist; whether
game names are blocked is unknown. We don't name them either way.)*

**Each style brings its own era.** That answers the open era question from the pictures: the crime-satire
style is today, the western is 1899, the mob game is the 1930s.

**Shot spec (shot-craft), changed from the sweep:**
- **For:** the whole argument in one picture. The height of the building is the wealth gap.
- **Cost in frame:** grandma freezing in the attic, the crowds fighting.
- **Light (all in the world, a colour each):** the candle (yellow on ice blue), the street lamp (yellow),
  the Mint's emerald press lamps, the orange furnace. Warmer the lower you go.
- 🔴 **Camera, the one design change:** the straight-on elevation was a symmetry magnet (`nano-banana-2.md`
  §37; "looks like AI" in `symptoms.md` is too symmetrical and too evenly lit). Now the camera **stands across
  the street to the left, low, looking up**. The building sits off-centre and the street runs out of frame.
  The camera position is named rather than described with a composition word (§3c).
- **Foreground:** the police vehicle's roof cuts across the bottom-left corner, a foreground occluder (free depth).
- **Withheld:** the leaders' faces (backs to us).

**Anti-slop, applied (repo toolkit + web pass 2026-10-25):**
- **Decay and wear in the world:** soot, peeling paint, puddles. Mafia's own art director named "decay" against
  a "travel brochure" look (Game Informer, 2025) `[official, via press]`.
- **Hard light with real shadows.** The video-slop tell is one soft "cloudy afternoon" key with no hard shadows
  (opus.pro) `[practitioner]`.
- **People mid-action, not posed:** shoving, playing, dancing, shivering.
- **A colour named for each place**, two lights of different colours (`docs/google-flow/` rule 2).
- **No kill-list words** ("cinematic", "high quality", "8K", "photorealistic", "masterpiece", "epic").
- 🟡 **Game styles invite on-screen interface** (score, map, logo). "Photo-mode capture" is used on the in-engine
  styles to ask for a frame with nothing on screen. That this word works is **unverified** (my inference; the web
  pass found no source for it).
- **Omni later (inferred, untested):** flat colour and hard shapes hold better in motion than fine texture or
  hatching. One test clip of the pick settles it.

**Engine:** Nano Banana 2, 9:16, 2 outputs each, run one at a time, project `dedd295f…`.
⬜ The Gemini API docs now name **Nano Banana 2.1** as the current model and NB2 as the previous generation
(ai.google.dev, 2026-10-25) `[official]`. Not seen in Flow's picker; we stay on NB2 (house rule) until checked.

**Shared scene paragraph (identical in all eight):**

> A tall narrow city building cut open in cross-section like a doll's house after dark, four floors only, seen
> from across the street, low and to the left, so the building stands off-centre and the street runs out of
> frame. Attic: an old woman in a coat shivers by one candle in an ice blue room. Street level: a brick red
> bakery; a red crowd and a blue crowd of mixed ages and skin tones shove each other under a yellow street lamp,
> the roof of a police vehicle in the near left corner. Basement: in emerald lamplight, printing presses throw
> banknotes into the air while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat
> and gold chain dances. Bottom: an orange furnace. Soot, peeling paint and puddles. Thanks.

**The eight style clauses** (each prompt = clause + the shared paragraph):

| # | Jack's reference | Style clause |
| --- | --- | --- |
| V1 | GTA (loading-screen art) | `Open-world crime satire video game loading-screen art, present day: a painted illustration with thick black ink outlines, flat cel colour with hard-edged shadow shapes, semi-realistic people full of attitude, the last coral and mango light of the sky laid in flat bands, hot pink neon.` |
| V2 | Red Dead Redemption 2 | `A photo-mode capture from a western open-world video game, 1899: painterly realism, a frontier town of weathered timber and brick, oil lamps throwing hard amber pools, cold blue moonlight, dust and woodsmoke hanging in the air, mud churned in the street.` |
| V3 | Mafia | `A photo-mode capture from a 1930s gangster video game: an American city in decay, soot-black brick, rain-wet cobbles, hard directional light from each lamp with deep dark shadows like an old master painting, warm amber, bottle green and oxblood.` |
| V4 | Cutaway colony game | `A side-on cutaway from a colony-management video game: every room a lit box like an ant farm, chunky stylised 3D figures with big heads and stubby limbs, bright toy colours on matte surfaces.` |
| V5 | 1990s point-and-click adventure | `A hand-painted background from a 1990s point-and-click adventure game: gouache with visible brush strokes, slightly crooked cartoon architecture, chunky figures with big hands, low screen resolution, warm lamplight against deep violet night.` |
| V6 | Late-1990s console game | `A screenshot from a late-1990s console video game: blocky low-polygon figures with flat painted faces, blurry low-resolution textures stretched across the walls, distance fog at the far end of the street, a saturated primary palette.` |
| V7 | 16-bit side-scroller | `16-bit side-scrolling video game pixel art: one even pixel grid, a limited palette of thirty-two colours, crisp pixel edges with dithered shading, small sprite characters.` |
| V8 | Cel-shaded comic-book game | `A cel-shaded comic-book video game render: 3D figures and buildings covered in thick hand-inked black contours and rough crosshatching, textures painted by hand with visible brush marks, flat bold colour.` |

V7 is side-on by nature, so its camera line will be ignored or will fight the style; that's expected.

### Video-game sweep results (2026-10-25)

All eight ran first time (NB2, 9:16, 2 each). 🔴 **They landed in Flow project "mmt jack" (`cb27208c-4b16-426d-9144-c394f2735c15`), not `dedd295f`**: `flow_open_project` reported `dedd295f` open, but the tab was on "mmt jack" by the time the stills were generated (cause unknown; checked over CDP 2026-10-25). Contact sheets were checked whole; the crowd
and Mint floors were checked zoomed on 1a, 2a, 3b, 5b, 7b and 8a.

| # | Style | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| V1 | Crime-satire loading-screen art (GTA) | b29f5d9e · 0319c4d2 | ⭐ The strongest and most readable. Bold ink, coral sky, the off-centre camera worked, the police car sits in the foreground. 🔴 1a printed **"LOADING..."** and a neon sign **"HOT PINN"** ("hot pink neon" was written onto a sign). 1b has gibberish neon signs, and the crowd stands on a ledge floating in mid-air |
| V2 | Western photo mode (RDR2) | 211722d1 · 8cb4254b | Atmospheric: mud, haze, a barred police wagon, a fiddle and banjo band (1899 got the era right). 🟡 It reads as a **miniature diorama render**, dark, with small figures. The red/blue crowds are mostly lost. 2b has five floors |
| V3 | 1930s mob photo mode (Mafia) | 2b0d3f8a · 63202310 | ⭐ The best mood: rain, amber lamps, steam, a 1930s car in the foreground, an accordion band. 3b is the pick. 🟡 The same diorama read as V2, and dark. Faces are tiny, which will be hard for Omni |
| V4 | Cutaway colony game | 3b557d35 · f2d07dc2 | ❌ Shiny toy figures, exactly the plastic sheen the slop guides name. 4b's crowd reads as children (`no kids` was a Camping rule, but it's still wrong here) |
| V5 | 1990s point-and-click painting | 019bd9f0 · 9b436ed1 | ⭐ The furthest from slop: gouache, crooked buildings, angry expressive crowd faces, a grinning mayor. 5b is the pick. 5a has five floors and a tiny "Bakery" note |
| V6 | Late-1990s console screenshot | 32a9f5e2 · 4948d11a | 🔴 **"Screenshot" brought in a game interface in 2 of 2**: "CAMERA UI", "MISSION 04", "LIFE", "HP", "SCORE: 00420", "LEVEL 1". The low-poly look only half landed. Fun as a joke, unusable as-is |
| V7 | 16-bit pixel art | ac27234d · 080bf869 | Charming and clean, with a consistent pixel grid at zoom. 🔴 7b drew the crowds with **solid red and solid blue skin** (the team colour became the skin colour, so mixed skin tones were lost). 7a has five floors |
| V8 | Cel-shaded comic-book game | 9dd8eee7 · bf23d8ff | Good: inked contours, gritty, a mixed crowd, the press spitting notes. Close to V1 but darker and less distinct |

**Caricature check (zoomed):** ✅ no minstrel or antisemitic features in any checked frame. ✅ The bowler mayor
held in 16 of 16; no Monopoly man. ✅ The pinstripe-gangster band held in 16 of 16. 🟡 V7b's red and blue
people (above).

**Across the sweep:**
- ✅ **The camera position worked.** "Seen from across the street, low and to the left" put the building
  off-centre in nearly every take, with the police vehicle as a foreground occluder. The straight-on symmetry is gone.
- 🔴 **"Four floors only" was ignored in 4 of 16** (2b, 5a, 6a, 7a added a bedroom floor).
- 🔴 **Game words summon game text:** "loading-screen" → LOADING; "screenshot" → a HUD. **"Photo-mode capture"
  gave a clean frame in 4 of 4** (V2, V3), so that word earns its place.
- 🟡 **The two realistic styles (V2, V3) come back as a dark miniature diorama** with tiny faces. Good mood,
  but the weakest for the caricature satire and the hardest for Omni.

**My shortlist:** **V1** (GTA: the punchiest, needs its text cleaned), **V3b** (Mafia: the best mood),
**V5b** (point-and-click: the least AI-looking). V7 if Jack wants a retro joke.

**Fixes for the next round of whichever wins:** drop "loading-screen" (keep the traits only); never put a colour
word where it can become a sign (say "hot pink light from a neon tube", or drop the neon); give each crowd
its colour on **banners and scarves**, never on the people; repeat "four floors" by naming them in order.

### Re-run in the right project (2026-10-25)

The first run (verdicts above, media ids in the table) is in Flow project **"mmt jack"** (`cb27208c…`). Jack asked
for them in **"Oct 25 - 09:43"** (`dedd295f…`), so the same eight prompts were re-run there, word for word. The
tab's project was checked over CDP before and after; all 16 are in `dedd295f`. **These are new takes, not copies**
(Flow has no move between projects), so they differ from the ones judged above. A glance at the contact sheet shows
the same patterns: V1b printed "LOADING..." again; V6 got a HUD again in 2 of 2 ("STAGE 4", "TIME 01:14",
"DOWNTOWN"). The re-run takes haven't had a zoomed caricature check yet: do it on whichever Jack picks, before
anything is built on it.

| # | Style | Media in `dedd295f` (a · b) |
| --- | --- | --- |
| V1 | Crime-satire key art (GTA) | fc2c6614 · 49c7588d |
| V2 | Western photo mode (RDR2) | 9e9fce14 · a21de852 |
| V3 | 1930s mob photo mode (Mafia) | 9268a358 · fc0d5fbb |
| V4 | Cutaway colony game | a2547b23 · cfd17f64 |
| V5 | 1990s point-and-click painting | 9688d22b · 0de323f9 |
| V6 | Late-1990s console screenshot | f9031fd3 · 63f285bb |
| V7 | 16-bit pixel art | 4a384654 · b90b38e0 |
| V8 | Cel-shaded comic-book game | ba276c8d · a8ba87b7 |

🔴 **Automation lesson:** `flow_open_project` said `dedd295f` was open, yet the first run's stills went to another
project (probably a parallel session moved the shared tab). Before and after a batch, check the tab URL
(`curl -s 127.0.0.1:9222/json/list`), and look for the new media ids in the page.

## Mixed sweep: pixel world, painted people (Jack, 2026-10-25)

Jack: *"try an art style where the world is a pixelated art style and the people are a red dead redemption 2 art
style … avoid AI slop … optimise for Nano Banana 2/Omni Flash … use the cinematography file and skills."*

**Web pass (2026-10-25), what changed the prompt:**
- Nobody has published a tested "pixel world + realistic people" prompt for NB2 (searched) `[checked]`. Stable
  Diffusion does it with regional prompts; Flow has none. Morphic warns that blending far-apart styles is
  unpredictable ([morphic](https://morphic.com/docs/how-tos/blending-images)) `[vendor]`. Expected failure (inferred): the model
  picks one style for the whole frame, most likely painted.
- Google's NB guide: the model obeys **hard scope words** (its "photo visible ONLY inside the letterforms" example);
  narrative prose, positive framing ([Google Cloud, 2026-03-06](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)) `[official]`.
  So each style is scoped: *every* building is pixel art, *only* the people are painted.
- NB pixel art sits on no true grid (mixed pixel sizes, colour bleed); a counted palette and "hard pixel edges" help
  ([spritecook](https://www.spritecook.ai/blog/nanobanana-pixel-art-for-games)) `[vendor]`. Our own V7 grid held at zoom.
- RDR2 described as traits: muted earthy palette, low warm sun through dusty haze, weathered faces with real skin
  texture, wool and leather ([itechguides](https://www.itechguides.com/what-makes-red-dead-redemption-2s-visuals-look-so-realistic/),
  [Polygon essay via gamescenes](https://www.gamescenes.org/video-essay-red-dead-redemption-2-and-the-hudson-river-school-of-painting/)) `[practitioner]`.
  "Oil-painted" is fan language, not documented. The game is never named.
- Slop tells to keep out: plastic skin, symmetric faces, light with no source, gibberish text, too clean
  ([magicshot, 2026-08-06](https://magicshot.ai/blog/why-your-ai-images-still-look-fake-12-tells-and-how-to-kill-them)) `[vendor]`.

**Carried from the video-game sweep:** "photo-mode capture" (clean frame 4 of 4, no HUD); the camera across the
street, low and left; team colour on **scarves and banners**, never on people (V7b's red and blue skin); four floors
**named in order**; no neon, no colour word that can become a sign; the pinstripe-gangster band; the bowler mayor.

**Shot spec (shot-craft):** for = the whole argument in one picture, height = wealth gap. Cost in frame = grandma
freezing, the crowds fighting. Light, all in the world: candle, street lamp, emerald press lamps, orange furnace.
Foreground = the police car roof. Withheld = nothing yet (style test).

**Variety mode, declared variable = how the two styles are joined.** Four ideas:

| # | Idea | Why |
| --- | --- | --- |
| M1 | **Plain scoped split** | The cleanest test: every world thing pixel, only people painted |
| M2 | **Stage set**: pixel-art flats, painted actors, the blocky lamp light falls on them | Gives the model a reason for two media in one frame (a theatre) |
| M3 | **Closer**: street and basement only, protesters' backs big in the foreground | Painted faces need size; V2/V3 came back as tiny diorama faces |
| M4 | **Dusk and coarse pixels**: low amber sun through dust, sixteen colours | The signature western light, and the biggest contrast between the two media; breaks the night palette on purpose |

NB2, 9:16, 2 each, project `dedd295f` ("Oct 25 - 09:43"), tab URL checked before and after.

**M1:**

> A photo-mode capture from a video game that draws its world and its people in two different ways. Every building, street, lamp and sky is crisp 16-bit pixel art: one even pixel grid, a limited palette of thirty-two colours, hard pixel edges. Only the people are painted in muted realism: weathered faces with real skin texture, stubble and tired eyes, 1930s wool coats, flat caps and worn leather, soft brushwork. A tall narrow building cut open like a doll's house at night, seen from across the street, low and to the left, four floors from the top down: an ice blue attic where an old woman in a coat shivers by one candle; a brick red bakery where a crowd in red scarves and a crowd in blue scarves, mixed ages and skin tones, shove each other under a yellow street lamp; an emerald-lit basement where printing presses throw banknotes while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat and gold chain dances; an orange furnace at the bottom. A police car roof in the near left corner. Thanks.

**M2:**

> A photo-mode capture from a mixed-media video game: the whole set is built from flat pixel-art backdrops, like theatre scenery made of chunky square pixels, and the actors standing in it are painted realistic people with weathered faces, real skin texture, 1930s wool coats and worn leather. The blocky coloured light of the pixel lamps falls across the painted actors. The set is a tall narrow building cut open like a doll's house at night, seen from across the street, low and to the left, four floors from the top down: an ice blue attic where an old woman in a coat shivers by one candle; a brick red bakery where a crowd in red scarves and a crowd in blue scarves, mixed ages and skin tones, shove each other under a yellow street lamp; an emerald-lit basement where printing presses throw banknotes while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat and gold chain dances; an orange furnace at the bottom. A police car roof in the near left corner. Thanks.

**M3:**

> A photo-mode capture from a video game that draws its world and its people in two different ways. Every wall, pavement, lamp and machine is crisp 16-bit pixel art: one even pixel grid, a limited palette of thirty-two colours, hard pixel edges. Only the people are painted in muted realism: weathered faces with real skin texture, stubble and tired eyes, 1930s wool coats, flat caps and worn leather. At night, close to a city building cut open like a doll's house, two floors fill the frame. Street level: a brick red bakery, and in the near foreground the shoulders and backs of protesters in red scarves shoving protesters in blue scarves, mixed ages and skin tones, under a yellow street lamp. Below, through the cut-away floor, an emerald-lit basement where printing presses throw banknotes while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat and gold chain dances. Seen low and from the left. Thanks.

**M4:**

> A photo-mode capture from a video game that draws its world and its people in two different ways. Every building, street, lamp and sky is coarse chunky pixel art: big square pixels, sixteen colours, hard pixel edges. Only the people are painted in muted realism: weathered faces with real skin texture, stubble and tired eyes, 1930s wool coats, flat caps and worn leather. Evening: a low amber sun from the right through drifting dust and chimney smoke, long hard shadows. A tall narrow building cut open like a doll's house, seen from across the street, low and to the left, four floors from the top down: a cold blue attic where an old woman in a coat shivers by one candle; a brick red bakery where a crowd in red scarves and a crowd in blue scarves, mixed ages and skin tones, shove each other; an emerald-lit basement where printing presses throw banknotes while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat and gold chain dances; an orange furnace at the bottom. A police car roof in the near left corner. Thanks.

### Mixed sweep results (2026-10-25)

All four ran first time (NB2, 9:16, 2 each). Tab checked: all eight in `dedd295f`. Contact sheet checked whole,
people zoomed on 1a, 1b, 2a, 3b, 4b.

| # | Idea | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| M1 | Plain scoped split | 468eb490 · 56b68708 | ✅ **The split works in both takes:** pixel walls and presses, painted people. People lean painted-illustration rather than full realism. 🔴 1a has a **camera viewfinder overlay** ("CAM", zoom numbers); 1b wrote room labels ("Bakery", "Secret Basement", "Furnace Room"). 1b's crowd sides are muddled (a man in both scarves) |
| M2 | Stage set | 2f15f92f · 67e040f2 | 🟡 The people come back as realistic 3D game figures and the pixels are weaker; it reads as a lit diorama. Clean of text. The least distinct of the four |
| M3 | Closer, two floors | c2fea7a9 · 4715bdba | ⭐ **3b is the pick:** big painted faces with weathered skin, stubble and wool; the closest to the western-game look, against a crisp pixel bakery and pixel basement. 🔴 3a wrote **"brick red bakery" on the shop sign** (the colour word went onto the sign) plus "PHOTO MODE" and a viewfinder. 3b has "BAKERY" and "OPEN" signs (fine, or cover them in post). 🟡 3b's crowd is all white men; the "mixed ages and skin tones" ask was lost |
| M4 | Dusk, coarse pixels | f7f4c3fc · 40608517 | 🟡 Lovely dusk light and chimney smoke, but "coarse chunky pixel art" turned 3D: **voxel blocks** with tiny figurines, a miniature model look. Faces too small |

**Caricature check (zoomed):** ✅ no minstrel, antisemitic or other stereotyped faces; ✅ bowler mayor 8 of 8, no
Monopoly man; ✅ pinstripe-gangster band held. 🟡 3b's crowd lost its mix (above).

**What the sweep says:**
- ✅ **NB2 keeps two media apart when each is scoped** ("every … is pixel art; only the people are painted") in 8 of 8.
  The web expected the model to pick one style (inferred there); it didn't.
- ✅ **Size decides how "realistic" the painted people read.** Small figures drift to illustration or toy figurines;
  chest-up figures (M3) get the real skin, stubble and wool.
- 🔴 **"Photo-mode capture" summoned a camera viewfinder in 2 of 8** this time (1a, 3a); clean 4 of 4 last sweep.
  Next round: drop it and say "a frame of a game world with nothing on screen but the world" (untested).
- 🔴 **A colour word in front of "bakery" became sign text** ("brick red bakery"). Put the colour on the bricks.

**Next round from 3b (if Jack picks it):** keep the M3 camera, fix the crowd mix by naming two or three people ("a
young Black woman in a red scarf, a grey-haired white man in a blue scarf…"), "the bakery's brick walls are brick
red", drop "photo-mode capture". Then one Omni test clip: does the pixel grid hold still while the painted people move?

## Own-look sweep: Jack likes 3a but "it's too similar to other cartoon styles" (2026-10-25)

**Why 3a reads as generic:** we *asked* for the stock adult-sitcom kit: "big round eyes, small dot pupils and
overbites, wobbly black outlines, simple rounded people". Critics name that cluster (round heads, dot eyes, even
outline) as the industry's herd look ([Cartoon Brew](https://www.cartoonbrew.com/ideas-commentary/yes-virginia-there-is-a-calarts-sensibility-74428.html)) `[practitioner]`.
A model with no unusual reference points falls to its averaged style ([arXiv 2505.09166](https://arxiv.org/abs/2505.09166)) `[research]`.

**Levers that make a look recognisable in one frame (web pass 2026-10-25):**
- **Two media for two worlds:** Wolfwalkers draws the town as woodblock print (hard edges, ink gaps, blocky) and the forest
  as loose pencil; colour fills are offset from the line ([mande.net](https://mande.net/btl/crafts/visual-fx/wolfwalkers-animation)) `[official, via press]`.
- **Off-register print:** fills slipped out of line, halftone shadows (Spider-Verse, Wolfwalkers) `[practitioner]`.
- **Modernist flat icons, rooms barely drawn:** UPA, flat graphic shapes, backgrounds more abstract than the
  characters, colour by mood ([Animation Obsessive](https://animationobsessive.substack.com/p/what-the-upa-style-actually-is)) `[practitioner]`.
- **Distortion as the opinion:** the British satire line (Gillray, Scarfe, Spitting Image): faces stretched and
  swollen to say what the artist thinks of them ([BFI](https://www.bfi.org.uk/features/spitting-image-still-biting-after-all-these-years)) `[practitioner]`.

**What stays from 3a:** the doll's-house cross-section seen straight on, flat cartoon colour, the floors and their colours, the jokes.
**What goes:** the round-eye / dot-pupil / overbite kit. Every candidate replaces it with its own face rule.
**Declared variable:** the signature lever. Scene paragraph identical in all four; the band is the pinstripe gangsters
(fixes the all-Black-band problem); the margins are said to be plain.

**Shared scene paragraph:**

> A tall city building cut open in cross-section like a doll's house, seen straight on, four floors from the top down. Attic: an old woman in a coat shivers by one candle in an ice blue room. Street level: a bakery with cream and brick red walls; a crowd in red scarves and a crowd in blue scarves, mixed ages and skin tones, shove each other under a street lamp, a police car beside them. Basement: in emerald lamplight, printing presses with cheerful faces throw banknotes while gangsters in pinstripe suits play music and a tall skinny mayor in a bowler hat and gold chain dances. Bottom: an orange furnace. Plain margins with no writing. Thanks.

| # | Lever | Style clause |
| --- | --- | --- |
| C1 | **Two media, the wealth gap in the drawing** | `A cartoon still drawn in two different media that split the building. The attic, the street and the people up there are a rough black woodblock print: chunky carved lines, white gaps where the ink did not take, flat grey-blue and brick colours on coarse paper. The basement and the furnace are smooth Art Deco lacquer painting, crisp gold lines on emerald and black, every edge perfect. Everyone is drawn as flat angular shapes with small dash eyes and heavy brows.` |
| C2 | **Cheap off-register screenprint** | `A cartoon still printed as a cheap four-colour screenprint: flat inks of brick red, mustard, teal and black on cream paper, each colour layer slipped slightly out of line with the black outline, coarse halftone dots for every shadow. People are tall stiff blocky figures with long faces, square jaws, small dash eyes and heavy brows.` |
| C3 | **Mid-century modernist icons** | `A 1950s modernist cartoon still: the people are flat graphic icons built from triangles, rectangles and long thin limbs, small dash eyes, colour shapes with no outlines and a few loose black lines for detail. The rooms are barely drawn: each floor is one flat block of mood colour with a few sketchy lines for the furniture.` |
| C4 | **Distortion is the opinion** | `A satirical cartoon still in sharp scratchy pen and flat watercolour, where the closer people are to the money, the more distorted they are drawn. The old woman and the crowds are drawn plainly with tired human faces. The gangsters are swollen round bodies with tiny heads; the mayor is stretched impossibly tall and thin with a huge grin full of teeth. Everyone has an ordinary nose.` |

🔴 C4 is the caricature risk (grotesque bankers have an antisemitic history): zoom every face; ordinary noses are written in.

### Own-look sweep results (2026-10-25)

All four ran first time (NB2, 9:16, 2 each). Tab checked: all eight in `dedd295f`. The C4 Mint was zoomed for the caricature check.

| # | Lever | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| C1 | Two media | 6e052de8 · 122fe13e | ⭐ **1b: the wealth gap is in the drawing.** Grey carved woodblock upstairs (icicles, ink gaps), and below the street line it turns into gold-on-emerald Art Deco lacquer, furnace included. Nobody else's cartoon looks like this. 1a splits less cleanly (the bakery is half Deco). "BAKERY" signs in both |
| C2 | Off-register screenprint | d737c016 · 89a846bf | 🟡 Handsome, warm, mixed crowds and a mixed band. But it reads as **modern editorial illustration**, which is itself a common look now. The off-register slip is faint |
| C3 | Mid-century modernist | cde7670d · 6d42b230 | ⭐ **The furthest from any sitcom:** flat colour blocks, rooms barely drawn, dash eyes, long limbs. 3b's yellow lamp cone over the crowd is a strong graphic beat. Fewest details, so likely the easiest for Omni to hold (inferred, untested). Mixed crowd and band |
| C4 | Distortion is the opinion | 96556d99 · 5dad38f5 | ⭐ **The most British and the most brutal:** scratchy pen and watercolour, the tired crowd drawn plainly, the gangsters swollen and the mayor a grinning stick. Matches the film's "brutal and silly" register. Busy, so hard for Omni |

**Caricature check:** ✅ no minstrel or other ethnic stereotype in any frame; mixed crowds in all eight; the band
was mixed in C2 and C3. ✅ C4 zoomed: the swollen gangsters have ordinary noses and nothing that reads as a racial type.
🟡 C4a's mayor has a long pointed nose (pointed, not hooked); watch it in any refinement. ✅ Bowler mayor 8 of 8.

**What the sweep says:** dropping the round-eye / dot-pupil / overbite kit and naming **a medium plus a face
rule** got eight frames that don't read as adult sitcom. "Plain margins with no writing" held (no signatures, no
labels); only the diegetic BAKERY signs remain.

**My shortlist:** C1b (the idea is in the drawing), C3 (the most original and the simplest to animate), C4 (the
satire register). Next: Jack picks, then one Omni test clip of the pick before any shot list.

## Twist sweep: 3a's style kept, a subtle BadCode touch (Jack, 2026-10-25)

Jack: *"no as in i liked the style i shared before (3a), i just want a subtle badcode twist, like a subtle overlay or
something … keep the style, just do small artistic iterations that vary from each other."* The own-look sweep above
answered the wrong question; **3a's style is locked.**

**Method:** one base prompt (3a word for word, with two fixes that are caricature/slop fixes, not taste: the band is the
pinstripe gangsters, which ends the all-Black-band-for-a-white-mayor problem; "plain margins with no writing" stops the
corner signature). Each twist adds **one sentence** to the base, so the only variable is the twist (one change at a
time, `shot-craft`; vary one element, keep the rest of the prompt fixed: [Picsart](https://picsart.com/tutorials/how-to-create-visuals-with-nano-banana-2-ai-model) `[vendor]`).
Overlays that must be exact and identical in every shot (a channel bug, a transmission texture) are **not asked of the
model**: they go on in ffmpeg, so Omni can't boil them (`docs/video-fx/hybrid-method.md`).

**Why a hidden mark:** studios sign their films with one recurring hidden object (Pixar's delivery truck and A113;
*Inside No. 9* hides the same hare statue on every set; [Den of Geek](https://www.denofgeek.com/tv/is-one-really-hidden-in-the-background-of-every-episode/)) `[press]`.
Ours is the logo's idea: **a ring with a small red triangle off-centre** (`docs/brand/README.md`: red only ever the
triangle, one small red thing, never centred). Never the word "BadCode" in a prompt (it would print it).

**Base B0:**

> A still from a prime-time adult animated sitcom: flat colours with one shadow tone, slightly wobbly hand-drawn black outlines, simple rounded people with big round eyes, small dot pupils and overbites, faint old film grain. A tall city building cut open in cross-section like a doll's house, seen straight on. In the attic an old woman in a coat shivers by one candle in an ice blue room. At street level a cream and brick red bakery; a red crowd and a blue crowd of mixed ages and skin tones shove each other under a yellow street lamp, a police car beside them. Below, a secret emerald basement in toxic green lamplight: printing presses with cheerful 1930s cartoon faces throw banknotes into the air, gangsters in pinstripe suits play jazz, and a tall skinny mayor in a bowler hat and gold chain dances. At the very bottom an orange furnace. Plain margins with no writing. Thanks.

**Twists (one sentence inserted before "Plain margins"):**

| # | Twist | Sentence |
| --- | --- | --- |
| T1 | **The mayor's medal is the mark** | `The medallion on the mayor's gold chain is a plain gold ring with one small red triangle inside it, set off to one side.` |
| T2 | **The machines are watching** | `Each printing press has one normal cartoon eye and one eye that is a small red triangle.` |
| T3 | **A red moon** | `Above the roof hangs a small, perfectly round, solid red moon in a dark sky.` |
| T4 | **The furnace peephole** | `The round peephole in the furnace door glows as a thin ring with a small red triangle of fire inside it, set off-centre.` |

**Post overlays on B0 (ffmpeg, not the model):**
- **P1 Transmission:** fine horizontal scanlines, a one-pixel red/cyan edge split, a little extra grain: a signal received
  from the future. Subtle, and identical on every shot.
- **P2 Channel bug:** the BadCode mark (`docs/brand/logo/badcode-mark-reversed.svg`) small in a corner at low opacity, like a TV channel's.

### Twist sweep results (2026-10-25)

NB2 (picker label "Nano Banana 2.1"), 9:16, 2 each, all in `dedd295f`. **3a's style held in 10 of 10.** The pinstripe-gangster
band came back mixed in most takes, so the all-Black-band-for-a-white-mayor problem is gone.

| # | Twist | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| B0 | Base (3a + fixes) | 54dd04d7 · 0bed6930 | ✅ Style matches 3a. 🔴 **B0-a: one press became a cup-headed character with a straw, close to a famous 1930s-style game mascot.** Unusable (trademark); "cheerful 1930s cartoon faces" summoned it |
| T1 | Mayor's medal | 59e93c4e · cfd55823 | ⭐ 1b: a red triangle on the gold medal; readable when you look, invisible when you don't. Centred, not off to one side. 1a barely shows |
| T2 | Red-triangle eye on the presses | 357ff563 · ee85fc88 | ❌ 0 of 2: the presses kept two normal eyes |
| T3 | Red moon | a6cc944f · 1f2716e1 | ⭐ **2 of 2.** A small solid red circle over the roof: the "o" of the wordmark, an omen, and it reads as a sign without any logo. The most striking twist |
| T4 | Furnace peephole | 068922fe · af4d4bf1 | ⭐ 4a: ring with a red triangle of fire, centred. 4b: a ring with a flame in it off-centre, subtle enough to miss |
| P1 | Transmission overlay (ffmpeg on B0-b) | — | Fine scanlines, a one-pixel red/cyan split, grain: "received from the future". Barely visible at phone size, clear at full size |
| P2 | Channel bug (ffmpeg on B0-b) | — | The BadCode mark top right at 70%, like a TV channel's |

**Caricature check:** ✅ no stereotyped faces; bowler mayor 10 of 10; crowds mixed both sides. 🔴 B0-a's mascot-like press (above).

**The twists stack:** the red moon, the medal and the peephole are in-picture and each is one sentence; the transmission
and the bug are post. My suggestion is **T3 (red moon) + P1 (transmission)** for the film, with the medal as the hidden
sign in close shots. The overlays are applied in ffmpeg on every shot, so they never boil in Omni.

## Realism sweep: 3a with a hint of realism, six wildly different ways (Jack, 2026-10-25)

Jack: *"what if it's this style with a hint of realism. please try a bunch of styles based on this one, that are wildly
different from each other."* Base = 3a's design (round people, dot pupils, overbites, the cross-section). **Declared
variable: what kind of "real" is added.** Each candidate is a different idea (variety mode, `new-image`).

**Web pass (2026-10-25):**
- **Klaus** kept 2D drawings and added up to eight hand-drawn light layers (ambient occlusion, subsurface, rim, bounce)
  plus brush texture on the characters, "not trying to fake a 3D render"
  ([befores & afters](https://beforesandafters.com/2019/11/14/heres-what-made-the-2d-animation-in-klaus-look-3d/),
  [Cartoon Brew](https://www.cartoonbrew.com/feature-film/how-klaus-draws-on-centuries-old-artistic-principles-to-push-2d-animation-forward-182325.html)) `[press]`. → R1.
- Handmade looks: ask for **material properties and scale** so the model treats it as a physical world; fingerprints,
  tiny asymmetries, loosely sewn cloth, matte surfaces; "not a polished toy"
  ([Luma](https://lumalabs.ai/news/3d-claymation-ai-prompts), [carat.im](https://carat.im/en/prompt-gallery/stop-motion-puppet)) `[vendor]`. → R2, R3.
  Our own warning: "chunky stylised 3D figures" gave glossy toys (V4), so every physical lever says **matte**.
- The British satire precedent for R3 is *Spitting Image*'s latex (BFI, own-look sweep above).

**Fixes carried:** the presses' faces are **"simple faces painted on their sides"** (the "cheerful 1930s cartoon faces"
wording produced a mascot lookalike twice); the band is the pinstripe gangsters; the red moon twist (T3) rides along in
every candidate since it's the best twist so far; "plain margins with no writing".

**Shared scene paragraph:**

> A tall city building cut open in cross-section like a doll's house, seen straight on at night, a small solid red moon above the roof. In the attic an old woman in a coat shivers by one candle in an ice blue room. At street level a cream and brick red bakery; a red crowd and a blue crowd of mixed ages and skin tones shove each other under a yellow street lamp, a police car beside them. Below, a secret basement in emerald lamplight: printing presses with simple faces painted on their sides throw banknotes into the air, gangsters in pinstripe suits play jazz, and a tall skinny mayor in a bowler hat and gold chain dances. At the very bottom an orange furnace. Plain margins with no writing. Thanks.

**Style clauses** (clause + shared paragraph). Every one opens with 3a's design so the base stays the same:

| # | Kind of real | Clause |
| --- | --- | --- |
| R1 | **Light** (feature-film 2D) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, still drawn in 2D with wobbly black outlines, but lit like a feature film: soft painted shading wrapping round every form, warm bounce light from the floor, a thin rim of light from each lamp, visible brush texture on coats and walls.` |
| R2 | **Clay** (stop-motion) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, rebuilt as a stop-motion miniature: matte plasticine people with fingerprints and tiny asymmetries, felt coats loosely stitched, a real wooden doll's-house set lit by tiny practical bulbs, dust in the air.` |
| R3 | **Latex** (satire puppets) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, made as foam-latex satirical puppets: matte painted latex skin with blotchy colour washes, glassy eyes, real cloth suits and wigs, in a real miniature set photographed under hard studio lamps.` |
| R4 | **Film** (photographed cels) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, painted on clear celluloid sheets and photographed on an old animation camera: dust and hairline scratches on the cels, soft shadows where the cel layers sit above the painted background, colours slightly faded.` |
| R5 | **Skin** (the gross-up) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, flat colour and black outlines everywhere except the faces, which are rendered with startling real skin: pores, stubble, broken veins, wet eyes.` |
| R6 | **World** (realist painted set) | `Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, drawn flat with black outlines, standing in a building and street painted with thick-oil night realism: wet cobbles reflecting the lamps, soot on old brick, steam rising from a grate.` |

🔴 R3 and R5 carry the caricature risk (realistic grotesque faces): zoom every face.

### Realism sweep results (2026-10-25)

NB2, 9:16, 2 each, all in `dedd295f` (R1 and R5 were harvested from the page after slow 99–100% timeouts; R3 needed one
"unusual activity" refresh). **The red moon landed in 12 of 12.** The press-face rewording ended the mascot lookalike (0 of 12).

| # | Kind of real | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| R1 | Light | b7e3fa96 · f84a24a2 | ⭐ 1b: the subtlest version, still 3a but with painted shading, a real lamp cone and rim light. 1a came back with a white poster border |
| R2 | Clay stop-motion | ffd77609 · 7049c27f | ⭐ Wildly different and charming: matte plasticine, tiny practical bulbs, a real miniature set; googly eyes keep 3a's design. No plastic sheen. Mixed crowds |
| R3 | Latex puppets | 92f9ed3d · 32bc6dcb | ⭐ 3a: satirical-puppet look on a real miniature set, matte, mixed crowd, the mayor a grimacing stick. 3b grew extra floors. Close to R2 in feel |
| R4 | Photographed cels | dea1adf9 · f336e6c0 | 🟡 Barely different from flat 3a; the cel dust, scratches and layer shadows didn't really show |
| R5 | Real skin on the faces | 3f22ec7d · 98046eb7 | 🔴 5a pasted photographic heads onto cartoon bodies: uncanny, the crowd went to all white men, and real-looking faces risk reading as real people. 5b ignored it |
| R6 | Realist oil-painted world | 1ed80cd3 · 4a95d774 | ⭐ **The strongest "hint of realism":** 3a's flat outlined people standing in a thick-oil night street, wet cobbles mirroring the lamps, soot, steam from a grate. Still unmistakably the 3a cartoon |

**Caricature check (zoomed R2, R3, R5, R6):** ✅ no stereotyped faces; mixed crowds except R5a; bowler mayor 12 of 12.

**Shortlist:** **R6** (closest to "this style with a hint of realism"), **R1b** (the gentlest hint), **R2 / R3a** (the
wild physical options). For Omni (inferred, untested): R1 and R6 keep flat people, so they should hold best; clay and
latex may smear in motion.

## The pick: R5a + elements of R6 (Jack, 2026-10-25)

Jack picked **R5a (`3f22ec7d`)**: *"this is the style i like it, also add some elements of the painting one."* So the
look is 3a's sitcom figures with real skin on the faces, in R5a's panelled cross-section, plus R6's oil-painted night
realism. (I had marked R5a down as uncanny; Jack's call.)

**Fixes carried:** R5a's crowd came back all white men, so the mix is named person by person (a word like "mixed" is
ignored; naming works: the band precedent). Red moon, press faces "painted on their sides", plain margins.

**Declared variable: how much of R6's painting comes in.** Four steps, from a little to a lot:

| # | How much painting | Clause added after the R5 style sentence |
| --- | --- | --- |
| K1 | **Only the street** | `Outside the building the street is painted in thick-oil night realism: wet cobbles mirroring the lamps, steam rising from a grate. Inside, the rooms stay flat cartoon colour.` |
| K2 | **The whole city** | `The building, the street and the night sky are painted in thick-oil night realism: soot on old brick, wet cobbles mirroring the lamps, steam rising from a grate.` |
| K3 | **Brushwork everywhere** | `Every flat colour is laid on with thick visible oil brushstrokes, and the street is wet cobbles mirroring the lamps.` |
| K4 | **Light only** | `The lamps cast real painted light: the street lamp's cone pools on wet cobbles, the candle glows warm on the attic frost, the furnace throws orange up the basement walls.` |

**Base (R5a's prompt, crowd fixed), clause inserted after the first sentence:**

> Prime-time adult animated sitcom characters, simple rounded people with big round eyes, small dot pupils and overbites, flat colour and black outlines everywhere except the faces, which are rendered with startling real skin: pores, stubble, broken veins, wet eyes. [CLAUSE] A tall city building cut open in cross-section like a doll's house, seen straight on at night, a small solid red moon above the roof. In the attic an old woman in a coat shivers by one candle in an ice blue room. At street level a cream and brick red bakery; a red crowd and a blue crowd shove each other under a yellow street lamp, each side young and old, men and women, Black, white and South Asian, a police car beside them. Below, a secret basement in emerald lamplight: printing presses with simple faces painted on their sides throw banknotes into the air, gangsters in pinstripe suits play jazz, and a tall skinny mayor in a bowler hat and gold chain dances. At the very bottom an orange furnace. Plain margins with no writing. Thanks.

### K sweep results (2026-10-25)

NB2, 9:16, 2 each, all in `dedd295f` (K1 and K4 harvested from the page after slow 99% timeouts).

| # | How much painting | Media (a · b) | Verdict |
| --- | --- | --- | --- |
| K1 | Only the street | 18fec2a3 · f10288ea | 🟡 Painted wet cobbles and steam outside, flat rooms inside; 1b is the cleaner split. The building grew extra flats of TV-watchers again. The faces lost most of R5a's real skin |
| K2 | The whole city | 5df5d12e · f0239d06 | ⭐ **2a: closest to "R5a + the painting":** R5a's panelled cross-section and cream border, a real-skinned grandma, a stormy painted sky, painted brick, steam, wet cobbles, a roaring painted furnace. 2b is moodier, with less face realism |
| K3 | Brushwork everywhere | d81d7f7a · 864f5d62 | 🟡 Thick strokes over everything: it turns into an oil-painted naive picture, and the cartoon line softens. Lovely but further from R5a |
| K4 | Light only | 3b88d11d · f0f47a65 | ⭐ **4a: the closest to R5a itself,** with the most real skin (the grandma, the gangsters) and a real lamp cone; the painting is only in the light. 4b is flatter |

**Crowd fix worked:** naming "young and old, men and women, Black, white and South Asian" gave mixed crowds on both
sides in 8 of 8 (R5a was all white men). **Caricature check (zoomed K2a, K2b, K4a):** ✅ ordinary faces, no stereotypes;
bowler mayor 8 of 8; red moon 8 of 8; no mascot lookalike.

**Shortlist:** **K2a** (the most painting), **K4a** (the most real skin). **Jack picked K3a** (`d81d7f7a`, brushwork everywhere), 2026-10-25.
