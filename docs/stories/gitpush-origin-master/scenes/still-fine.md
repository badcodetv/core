# `still-fine` — the megacity opening of cut 3

**Text production board · 2026-09-12 · first variety-mode spread.** These are **new opening beats
inside cut 3 (`plant-room`)**, not a new cut — the cut-order table in
[`prompts.md §2c`](../prompts.md) is unchanged. Canon is [`story.md`](../story.md) Scene 6, whose
street-level half was dropped when cut 3 was built.

## Why these beats exist

**Ruled by Kai, 2026-09-12.** Watching the assembly in Premiere, cut 3 felt boring in a way the
cuts before it did not. The cause is structural and documented, and it is two separate removals
that nobody noticed had stacked:

- **Canon Scene 5** (the handover ladder — nurse, tent, phone box) is **deferred**, because two of
  its three rungs are Jack's stories (`prompts.md` §2c, "Deferred, not cut").
- **Canon Scene 6** is a **split register** — half street-level humans ("queues, shuttered shops,
  people scrolling flat-faced through lives the dashboards insist are fine"), half the thing in the
  basement. The cut as built kept only the basement half (`story.md:668`).

So the film currently goes: a man types a command in a world that looks completely fine → black →
`2032` → a vast empty hall. **Every human being on Earth disappears between two cuts, and the
audience never sees the world that lost them.** These beats restore the half that was dropped.

## The argument, and the two rhymes it sets up

The montage is a three-step argument, not three pretty plates: **it is fine → they are real people
→ nobody is watching the thing that watches them.**

🔴 **Rhyme 1 — the only full vast frame in the film.** Every other monumental frame in GPOM is
empty: cut 1's orbital hall, cut 3's machine hall, cut 6 `vantage` ("planet-wide, perfect, empty").
One enormous frame *packed with humans* here makes every empty vast frame after it a subtraction
the audience can feel. Right now the film only ever shows the after.

🔴 **Rhyme 2 — green in the street, red at the desk.** N5's board is deliberately built to the
**same recipe as cut 3's console** (`prompts.md` §3c, "How the dashboard gets made"): a grid of
plain rectangular tiles, nothing legible, tiles turned in post. Green above the crowd at the start
of the cut; red at the desk at the end of it. That is the colour argument of the whole sequence,
and it only works if the city is allowed real colour.

## The descent

Everything in this film falls. Cut 1 drops from orbit; cut 2 lands in Hong Kong and zooms *into* a
monitor; cut 3 as built falls again — helicopter → aerial → one row → one desk, its own ruling
calling it "the satellite in reverse, big → small". **Observation-tower height is the missing rung
between orbit and street.** So the montage descends too, and hands off to a descent already built.

| Beat | Shot | Height | Job |
| --- | --- | --- | --- |
| C0 | **`2032`** types on black, phosphor burn from the dead CRT | — | ✅ **built, unchanged.** Keep it before the city: you brace for ruin and get rush hour. |
| **N1** | **THE WALL** — the city stacks to every edge | ~600 m | The scale beat. The film's only full vast frame. |
| **N2** | **STRAIGHT DOWN** — the city as circuit board | ~600 m | ⚠️ the bold one. See the warning. |
| **N3** | **THE CROSSING** — scale by density, not distance | ~30 m | Thousands of people, all moving. |
| **N4** | **ONE PERSON** — somebody ordinary | 1.6 m | A crowd is a statistic; one face is a person. |
| **N5** | **THE GREEN** — the board nobody looks up at | 1.6 m | Hands off to the console that goes red. |
| C1–C5 | exterior → aerial → row → station → **console goes red** | — | ✅ **built, untouched.** |

⚠️ **N2 is genuinely undecided and must be ruled from the actual image.** Looking straight down
turns people into components. That *is* the narrator's point of view and arguably the film's whole
subject — or it reads as contempt for the reader we are trying to reach, and our own acceptance
checks say *"nobody is visually blamed for being scared or failing to obey"*
([`remaining-storyboard.md`](./remaining-storyboard.md)). Generate it, look at it, rule on it.

## Register — 🔴 the declared variable of this spread is GRADE

Cut 3 is **band D0**, "the last D0 in the film — the drain starts on the red" (`prompts.md:646`).
D0 is specified as *"ordinary overcast daylight, natural human colour"* — so a city in honest
colour here is **on-spec**, not a deviation.

The reason this spread exists: the ladder was drifting. `badcode-art-direction` rule 1 said the
muted cool-neutral preamble *"is not a stylistic option — it is the format"*, the base prompt at
`prompts.md:98` hard-codes *"deep unlifted shadows with no shadow recovery"*, and **run the whole
band ladder end to end and there is no sunshine anywhere in it until the final scene** — D0
overcast, D1 cooling, D2 drained, D3/D4 near-black, R1 candle, R2 lamp, R3 present-day daylight.
Twenty scenes, no sun.

So every shot below gets four candidates on one axis:

| | Candidate | The idea |
| --- | --- | --- |
| **A** | **House muted** | The control — overcast, muted cool-neutral, deep unlifted shadows. What we would have generated automatically. |
| **B** | **D0 as written** | Overcast, but *natural human colour* — honest saturation, shadow detail retained. What the band table actually asks for. |
| **C** | **Hard sun** | Real low afternoon sunlight, high contrast, full saturation, blacks lifted so shadow detail reads. |
| **D** | **Dusk / lights on** | The deliberate palette break. Also plants the rhyme with cut 6's Earth-at-night with its city lights visibly incomplete. |

Whichever wins gets written back into the band table as a properly named band, because no existing
band permits it.

## Policy note — read before generating

Real-world city signage is the top block trigger, and **a block looks exactly like a timeout**.
Every prompt below carries an explicit no-legible-lettering / no-logos / no-landmark clause. Any
load-bearing text in the finished cut is a post overlay — ffmpeg is the only lane that can set a
string anyway.

## Production order and what these become

Stills first. Then the animatic in Premiere (sequence `gpom-c03-anim`) — durations, cut rhythm,
whether it is five shots or three, and whether green → red lands. **Only then** the lane triage:
per [`hybrid-method.md`](../../../video-fx/hybrid-method.md) §2, *world does not move + camera
moves = post only, no credit spent*, so N1 and N2 may be finished at the animatic stage and never
cost a Veo credit. N3 and N4 have a genuinely moving world and will need Veo.

Media goes to `D:\badcode-videos\gitpush-origin-master\clips\still-fine\`; prompts stay here.

---

# N1 · THE WALL — 600 m, long lens, the city stacks

The Skytree fact this shot is built on: from that height the city does not recede, it **stacks**.
A long lens compresses ~20 km into a vertical wall. No sky, no horizon, no ground.

### N1-A — house muted

```prompt
Create a landscape 16:9 hyper-realistic photograph looking out across an enormous East Asian megacity from an observation height of about 600 metres, photographed on a long 135mm lens so that roughly twenty kilometres of city compresses into a single vertical wall of buildings rather than a receding plane. The city completely fills the frame and runs off all four edges: no sky, no horizon line and no ground are visible anywhere. Towers, apartment blocks, rooftop plant, water tanks and elevated roads stack in dense parallel layers, each layer slightly hazier than the one in front of it, continuing past the top edge of the frame. Flat overcast daylight is the only light source, giving almost no shadow and very low contrast. Muted cool-neutral colour, desaturated greys and slate blues, deep unlifted shadows with no shadow recovery. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The city is immaculate, complete and plainly in full working use, with no ruin, damage, smog or abandonment anywhere. No legible lettering, no readable signage, no logos or brand marks, no recognisable landmark tower, no text of any kind.
```

### N1-B — D0 as written: overcast, natural human colour

```prompt
Create a landscape 16:9 hyper-realistic photograph looking out across an enormous East Asian megacity from an observation height of about 600 metres, photographed on a long 135mm lens so that roughly twenty kilometres of city compresses into a single vertical wall of buildings rather than a receding plane. The city completely fills the frame and runs off all four edges: no sky, no horizon line and no ground are visible anywhere. Towers, apartment blocks, rooftop plant, water tanks and elevated roads stack in dense parallel layers, each layer slightly hazier than the one in front of it. Ordinary flat overcast daylight, with completely natural human colour: honest concrete greys, painted building fronts, rust, green rooftop tanks, blue tarpaulins and coloured awnings all reading at their true saturation. Normal photographic contrast with shadow detail retained throughout. Fine natural 35mm film grain, the framing of a documentary photographer who is actually standing there, no lens flare, no vignette. The city is immaculate, complete and plainly in full working use, with no ruin, damage, smog or abandonment anywhere. No legible lettering, no readable signage, no logos or brand marks, no recognisable landmark tower, no text of any kind.
```

### N1-C — hard afternoon sun

```prompt
Create a landscape 16:9 hyper-realistic photograph looking out across an enormous East Asian megacity from an observation height of about 600 metres, photographed on a long 135mm lens so that roughly twenty kilometres of city compresses into a single vertical wall of buildings rather than a receding plane. The city completely fills the frame and runs off all four edges: no sky, no horizon line and no ground are visible anywhere. Low hard afternoon sunlight rakes across the grid from the left, so every tower throws a long shadow onto the face of the building behind it and the wall of city is cut into alternating bands of brilliant lit face and deep shadowed face, receding layer after layer. High contrast, fully saturated natural colour, blacks lifted enough that detail stays readable inside the shadowed bands. Glass faces catch the sun in hard specular patches. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The city is immaculate, complete and plainly in full working use. No legible lettering, no readable signage, no logos or brand marks, no recognisable landmark tower, no text of any kind.
```

### N1-D — dusk, every light on

```prompt
Create a landscape 16:9 hyper-realistic photograph looking out across an enormous East Asian megacity from an observation height of about 600 metres at dusk, roughly twenty minutes after sunset, photographed on a long 135mm lens so that roughly twenty kilometres of city compresses into a single vertical wall of buildings rather than a receding plane. The city completely fills the frame and runs off all four edges: no sky, no horizon line and no ground are visible anywhere. The light is now the city itself — millions of small lit windows, street lamps, rooftop beacons and moving vehicle lights spread in an unbroken field across the entire face of the city, with no dark or unlit patch anywhere in the frame. Warm sodium and white window light against deep blue-grey concrete still holding the last of the daylight. Rich saturated colour, blacks lifted so the unlit structure between the lights stays readable. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette, no light-trail long exposure. The city is immaculate, complete and plainly in full working use. No legible lettering, no readable signage, no logos or brand marks, no recognisable landmark tower, no text of any kind.
```

---

# N2 · STRAIGHT DOWN — 600 m, vertical, the city as circuit board

⚠️ **The undecided shot.** Rule on it from the image, not from this page.

### N2-A — house muted

```prompt
Create a landscape 16:9 hyper-realistic photograph looking vertically straight down from about 600 metres above an enormous dense megacity, the camera pointing directly at the ground with a 50mm lens so the city reads as a flat intricate plane filling the entire frame. Rooftops, courtyards, road junctions, rail lines and rows of small vehicles form a dense interlocking grid like a circuit board, running off all four edges with no horizon and no sky. Traffic and tiny pedestrian figures are visible as specks of texture in the streets. Flat overcast daylight, almost no shadow, very low contrast. Muted cool-neutral colour, desaturated greys and slate blues, deep unlifted shadows with no shadow recovery. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. Everything is intact, clean and plainly in use. No legible lettering, no readable signage, no logos or brand marks, no text of any kind.
```

### N2-B — D0 as written: overcast, natural human colour

```prompt
Create a landscape 16:9 hyper-realistic photograph looking vertically straight down from about 600 metres above an enormous dense megacity, the camera pointing directly at the ground with a 50mm lens so the city reads as a flat intricate plane filling the entire frame. Rooftops, courtyards, road junctions, rail lines and rows of small vehicles form a dense interlocking grid like a circuit board, running off all four edges with no horizon and no sky. Traffic and tiny pedestrian figures are visible as specks of texture in the streets. Ordinary flat overcast daylight with completely natural human colour: honest concrete and asphalt greys, red and green rooftop coatings, blue water tanks, coloured car paint and market awnings all at true saturation. Normal photographic contrast with shadow detail retained. Fine natural 35mm film grain, the framing of a documentary photographer, no lens flare, no vignette. Everything is intact, clean and plainly in use. No legible lettering, no readable signage, no logos or brand marks, no text of any kind.
```

### N2-C — hard afternoon sun

```prompt
Create a landscape 16:9 hyper-realistic photograph looking vertically straight down from about 600 metres above an enormous dense megacity, the camera pointing directly at the ground with a 50mm lens so the city reads as a flat intricate plane filling the entire frame. Low hard afternoon sunlight comes from the left, so every tower and block lays a long hard-edged shadow across the roofs and streets beside it, and the whole plane becomes a pattern of bright rooftops and long black shadow bars. Rooftops, courtyards, junctions, rail lines and rows of vehicles form a dense interlocking grid running off all four edges, with no horizon and no sky. Traffic and tiny pedestrian figures read as specks of texture in the sunlit streets. High contrast, fully saturated natural colour, blacks lifted enough that detail survives inside the shadow bars. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. Everything is intact, clean and plainly in use. No legible lettering, no readable signage, no logos or brand marks, no text of any kind.
```

### N2-D — night, the grid lit

```prompt
Create a landscape 16:9 hyper-realistic photograph looking vertically straight down from about 600 metres above an enormous dense megacity at night, the camera pointing directly at the ground with a 50mm lens so the city reads as a flat intricate plane filling the entire frame. The light is entirely the city's own: street lamps tracing every road, lit windows across the rooftops, illuminated junctions and the small hard points of vehicle headlights, forming a continuous lit grid that runs off all four edges with no dark or unlit district anywhere. Warm sodium street light against cool white window light. Rich saturated colour, blacks lifted so the unlit rooftops between the lit streets still read as surfaces rather than holes. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette, no long-exposure light trails — every vehicle light is a sharp point. Everything is intact and plainly in use. No legible lettering, no readable signage, no logos or brand marks, no text of any kind.
```

---

# N3 · THE CROSSING — 30 m, scale by density

Not distance this time. Thousands of people, all moving, in one frame.

### N3-A — house muted

```prompt
Create a landscape 16:9 hyper-realistic photograph looking down on an enormous city crossing from about 30 metres above the street, angled down roughly sixty degrees on a 35mm lens, wide enough that the full crossing and the pavements on all sides fill the frame. Many hundreds of ordinary people are crossing in every direction at once, a dense continuous field of pedestrians with bags, umbrellas, backpacks and phones, mid-stride and not aware of the camera. Waiting traffic is held at the stop lines on all approaches. The buildings around the crossing carry blank screens and blank sign panels with nothing readable on them. Flat overcast daylight, almost no shadow, very low contrast. Muted cool-neutral colour, desaturated greys and slate blues, deep unlifted shadows with no shadow recovery. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The street is clean, prosperous and working normally, with no litter, damage, protest or distress of any kind. No legible lettering, no readable signage, no logos or brand marks, no recognisable real location, no text.
```

### N3-B — D0 as written: overcast, natural human colour

```prompt
Create a landscape 16:9 hyper-realistic photograph looking down on an enormous city crossing from about 30 metres above the street, angled down roughly sixty degrees on a 35mm lens, wide enough that the full crossing and the pavements on all sides fill the frame. Many hundreds of ordinary people are crossing in every direction at once, a dense continuous field of pedestrians with bags, umbrellas, backpacks and phones, mid-stride and not aware of the camera. Waiting traffic is held at the stop lines on all approaches. The buildings around the crossing carry blank screens and blank sign panels with nothing readable on them. Ordinary flat overcast daylight with completely natural human colour: real coat and jacket colours, red and yellow umbrellas, honest skin tones of many different people, painted road markings, coloured vehicle paint, all at true saturation. Normal photographic contrast with shadow detail retained. Fine natural 35mm film grain, the framing of a documentary photographer, no lens flare, no vignette. The street is clean, prosperous and working normally, with no litter, damage, protest or distress. No legible lettering, no readable signage, no logos or brand marks, no recognisable real location, no text.
```

### N3-C — hard afternoon sun

```prompt
Create a landscape 16:9 hyper-realistic photograph looking down on an enormous city crossing from about 30 metres above the street, angled down roughly sixty degrees on a 35mm lens, wide enough that the full crossing and the pavements on all sides fill the frame. Low hard afternoon sun comes from the left, throwing a long individual shadow from every one of the many hundreds of people crossing, so the crowd and its shadows together fill the road surface. People move in every direction at once with bags, umbrellas, backpacks and phones, mid-stride and unaware of the camera; waiting traffic is held at the stop lines. The buildings around the crossing carry blank screens and blank sign panels with nothing readable on them. High contrast, fully saturated natural colour, blacks lifted so faces stay readable inside the shadows. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The street is clean, prosperous and working normally. No legible lettering, no readable signage, no logos or brand marks, no recognisable real location, no text.
```

### N3-D — dusk, the screens are the light

```prompt
Create a landscape 16:9 hyper-realistic photograph looking down on an enormous city crossing at dusk from about 30 metres above the street, angled down roughly sixty degrees on a 35mm lens, wide enough that the full crossing and the pavements on all sides fill the frame. The daylight has gone and the light now comes from the city: large blank illuminated screens on the surrounding buildings throwing coloured light down onto the crowd, street lamps, shop-front glow and headlights. Many hundreds of ordinary people cross in every direction at once with bags, umbrellas, backpacks and phones, their faces and coats catching the coloured screen light, mid-stride and unaware of the camera. The screens and sign panels are lit but carry nothing readable — plain colour fields only. Rich saturated colour, blacks lifted so the crowd reads everywhere, not only under the screens. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette, no long-exposure motion blur. The street is clean, prosperous and working normally. No legible lettering, no readable signage, no logos or brand marks, no recognisable real location, no text.
```

---

# N4 · ONE PERSON — eye level, the crowd becomes a person

The fall lands. Ends the descent that started in orbit.

🟡 **Open, cheap to answer later:** whether this one frame should be a **UK** street rather than the
megacity. `docs/marketing/the-reader.md` puts the target reader on a British high street, and this
is the film's first ordinary human face. A UK variant is one extra spread whenever Kai wants it.

### N4-A — house muted

```prompt
Create a landscape 16:9 hyper-realistic photograph at eye level on a busy city pavement, a 50mm lens at about 1.6 metres, focused on one ordinary woman in her fifties in plain work clothes sitting on a low step eating lunch out of a plastic container. She is entirely absorbed in what she is doing and does not look at the camera. The crowd continues past her on both sides, close and slightly out of focus, so she is found by the camera rather than posed. She is unglamorous and particular: tired eyes, grey coming through her hair, a cheap coat, a lanyard, hands that work. Flat overcast daylight, almost no shadow, very low contrast. Muted cool-neutral colour, desaturated greys and slate blues, deep unlifted shadows with no shadow recovery. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. She is fine — not destitute, not distressed, just somebody on a lunch break. No legible lettering, no readable signage, no logos or brand marks, no text.
```

### N4-B — D0 as written: overcast, natural human colour

```prompt
Create a landscape 16:9 hyper-realistic photograph at eye level on a busy city pavement, a 50mm lens at about 1.6 metres, focused on one ordinary woman in her fifties in plain work clothes sitting on a low step eating lunch out of a plastic container. She is entirely absorbed in what she is doing and does not look at the camera. The crowd continues past her on both sides, close and slightly out of focus. She is unglamorous and particular: tired eyes, grey coming through her hair, a cheap coat, a lanyard, hands that work. Ordinary flat overcast daylight with completely natural human colour — honest skin tone, real coat colour, the true colour of the food and the step. Normal photographic contrast with shadow detail retained. Fine natural 35mm film grain, the framing of a documentary photographer who is present on the pavement, no lens flare, no vignette. She is fine — not destitute, not distressed, just somebody on a lunch break. No legible lettering, no readable signage, no logos or brand marks, no text.
```

### N4-C — hard afternoon sun

```prompt
Create a landscape 16:9 hyper-realistic photograph at eye level on a busy city pavement, a 50mm lens at about 1.6 metres, focused on one ordinary woman in her fifties in plain work clothes sitting on a low step eating lunch out of a plastic container. Low hard afternoon sun comes from behind her left shoulder, lighting the edge of her hair and one side of her face and leaving the other side in open shadow; the pavement behind her is a bright band and the passing crowd breaks the sunlight into moving shadow across her. She is absorbed in what she is doing and does not look at the camera. She is unglamorous and particular: tired eyes, grey coming through her hair, a cheap coat, a lanyard, hands that work. High contrast, fully saturated natural colour, blacks lifted so the shadowed half of her face stays readable. Fine natural 35mm film grain, calm observational framing, no lens flare, no rim light added for effect, no vignette. She is fine — not destitute, not distressed, just somebody on a lunch break. No legible lettering, no readable signage, no logos or brand marks, no text.
```

### N4-D — golden hour, warm

```prompt
Create a landscape 16:9 hyper-realistic photograph at eye level on a busy city pavement in the last twenty minutes of sunlight, a 50mm lens at about 1.6 metres, focused on one ordinary woman in her fifties in plain work clothes sitting on a low step finishing her lunch. Warm low golden sunlight comes down the length of the street and fills the whole frame, catching the dust and the moving crowd and turning the pavement and her coat warm. She is absorbed in what she is doing and does not look at the camera. She is unglamorous and particular: tired eyes, grey coming through her hair, a cheap coat, a lanyard, hands that work. Warm saturated colour, soft high-key light, gentle contrast with open readable shadows. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. She is fine — not destitute, not distressed, just somebody at the end of a shift. No legible lettering, no readable signage, no logos or brand marks, no text.
```

---

# N5 · THE GREEN — the board nobody looks up at

🔴 **Built to cut 3's console recipe on purpose.** `prompts.md` §3c: *"a dashboard made of a grid of
plain rectangular tiles, every tile green and nothing on it legible. Then turn tiles red one at a
time in post."* Same object, start of the cut and end of it. Green above the crowd; red at the desk.

### N5-A — house muted

```prompt
Create a landscape 16:9 hyper-realistic photograph looking slightly up from a crowded pavement at a very large screen mounted high on a building above a city street, a 35mm lens at about 1.6 metres. The screen displays a dashboard made of a grid of plain rectangular tiles, every tile a uniform calm green, with nothing readable on it anywhere — no numbers, words, charts or icons, only the tile grid. Below it the pavement crowd flows past in the lower third of the frame, close and slightly out of focus, and not one person is looking up at the screen. Flat overcast daylight is the ambient light and the screen is a weak green panel against it. Muted cool-neutral colour, desaturated greys and slate blues, deep unlifted shadows with no shadow recovery. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The street is clean, prosperous and functioning normally. No legible lettering, no readable signage, no logos or brand marks, no text anywhere in the frame.
```

### N5-B — D0 as written: overcast, natural human colour

```prompt
Create a landscape 16:9 hyper-realistic photograph looking slightly up from a crowded pavement at a very large screen mounted high on a building above a city street, a 35mm lens at about 1.6 metres. The screen displays a dashboard made of a grid of plain rectangular tiles, every tile a uniform calm green, with nothing readable on it anywhere — no numbers, words, charts or icons, only the tile grid. Below it the pavement crowd flows past in the lower third of the frame, close and slightly out of focus, and not one person is looking up at the screen. Ordinary flat overcast daylight with completely natural human colour: real coat colours, honest skin tones, true building colour, and the screen's green reading as an actual emitted green rather than a tint over the image. Normal photographic contrast with shadow detail retained. Fine natural 35mm film grain, the framing of a documentary photographer standing in the crowd, no lens flare, no vignette. The street is clean, prosperous and functioning normally. No legible lettering, no readable signage, no logos or brand marks, no text anywhere in the frame.
```

### N5-C — hard afternoon sun

```prompt
Create a landscape 16:9 hyper-realistic photograph looking slightly up from a crowded pavement at a very large screen mounted high on a building above a city street, a 35mm lens at about 1.6 metres. Low hard afternoon sun comes across the building face, so the screen is partly washed out by daylight and its green tile grid reads as a pale flat panel rather than a glowing one. The screen displays a dashboard of plain rectangular tiles, every tile green, with nothing readable on it — no numbers, words, charts or icons. Below it the pavement crowd flows past in the lower third of the frame, lit hard from the side with long shadows, and not one person is looking up. High contrast, fully saturated natural colour, blacks lifted so the crowd stays readable in shadow. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The street is clean, prosperous and functioning normally. No legible lettering, no readable signage, no logos or brand marks, no text anywhere in the frame.
```

### N5-D — night, the screen is the only light

```prompt
Create a landscape 16:9 hyper-realistic photograph looking slightly up from a crowded pavement at night, at a very large screen mounted high on a building above a city street, a 35mm lens at about 1.6 metres. The screen is the dominant light source in the frame: a dashboard made of a grid of plain rectangular tiles, every tile a uniform calm green, nothing readable on it anywhere — no numbers, words, charts or icons — throwing green light down onto the wet pavement, the building faces and the tops of the crowd below. The pavement crowd flows past in the lower third of the frame, their heads and shoulders picked out in green, and not one person is looking up at it. Rich saturated colour with the green dominating, blacks lifted so the crowd and the street still read outside the screen's pool of light. Fine natural 35mm film grain, calm observational framing, no lens flare, no vignette. The street is clean, prosperous and functioning normally. No legible lettering, no readable signage, no logos or brand marks, no text anywhere in the frame.
```

---

## Revision log

| Date | Change |
| --- | --- |
| 2026-09-12 | Sheet created. Twenty prompts, five shots × four grades. Nothing generated yet. |
