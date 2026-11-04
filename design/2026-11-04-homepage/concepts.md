# BadCode homepage: eight concepts

Researchers merged: 10. Starting ideas: 30. These are 8 different concepts that don't overlap, with the best moves from each research lens grafted in.

**Rules for all eight:**
- The logo is fixed. The wordmark "badcode" is the drawn SVG from `docs/brand/logo/` and is never set in a typeface. The typefaces below are for everything else.
- The logo red is the only red that belongs to BadCode.
- No cyan and no SaaS cards.
- Future Proof is the lit, daylight place in every concept.

---

## 1. THE WEDGE

**Pitch:** The logo is already a 1919 political poster. The homepage plays it out: the red triangle hits the ring and breaks it into the three strands.

**Hero moment:**
1. A black screen. A thin warm-white ring draws itself in.
2. The red triangle sits at 2 o'clock and swivels once toward the cursor.
3. One hard sound. The triangle drives through the ring and splits it into three arcs.
4. Each arc flies out and unrolls into a slab, labelled TELL, REPORT and RULE.

The whole sequence takes under 4 seconds.

**Layout:** Three slabs fill the viewport.
- Two slabs are tilted at 18 to 22 degrees and overlap like machine parts: Stories and News.
- The Government slab is perfectly flat and upright. That is the joke: it is the only one trying to look official.
- Scrolling slides the slabs so that one fills the screen.
- On a phone, the slabs stack into three angled bands, and the Government band stays flat.

```
 ┌──────────────────────────┐
 │╲ STORIES ╲  ▲            │
 │ ╲ film frames ╲          │
 │  ╲╲ NEWS ╲╲ NURSES £0 ╲  │
 │   ╲ ticker ticker ╲      │
 │┌────────────────────────┐│
 ││ GOVERNMENT  [Start now]││
 │└────────────────────────┘│
 └──────────────────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Litho Black | `#111010` |
| Postbox Red (the logo red; not Soviet crimson) | `#D7261E` |
| Newsprint | `#EDE6D6` |
| Press Grey | `#8A857C` |
| Future Proof Gold (the Government slab only) | `#F2B705` |

**Type:**
- Display: Big Shoulders Stencil
- Slab text: Archivo Black
- Small print: IBM Plex Mono

**Motion:**
- One violent opening move, then mechanical sliding.
- No easing curves softer than a press. Panels clunk into place.

**The three strands:**
- **Stories.** Rodchenko-style film-frame photomontage cut into the slab, with the four titles stamped across it.
- **News.** A ticker band, plus a departures-board flip counter for "NURSES: £0".
- **Government.** An official-looking parody: off-white with a black bar, a green "Start now" button and the line "Promises to enact Future Proof".

**Opening line:** "We tried subtle. You were busy."

**Steals from:**
- El Lissitzky, *Beat the Whites with the Red Wedge*: https://en.wikipedia.org/wiki/Beat_the_Whites_with_the_Red_Wedge
- Rodchenko: https://en.wikipedia.org/wiki/Alexander_Rodchenko
- GOV.UK Design System: https://en.wikipedia.org/wiki/Gov.uk
- Channel 4 ident, shapes that assemble into a mark: https://en.wikipedia.org/wiki/Channel_4_idents_and_presentation

**Risk:**
- A red wedge on black reads as "communist" to a reader drifting right.
- Mitigations: no Soviet text, postbox red rather than crimson, and let the very British Government slab set the tone.

---

## 2. CHANNEL BADCODE (the pirate signal)

**Pitch:** A dull, respectable page is hijacked. BadCode takes over the screen and turns out to run three channels.

**Hero moment:**
1. For 1.5 seconds the page is a believable, boring "consultation" page.
2. The picture tears sideways and a rolling bar passes through.
3. The balaclava host fills a corrugated backdrop for exactly one second. He is motionless and silent.
4. The logo becomes the standby light. A tuner clunks and three channel numbers snap in.

**Layout:**
- One CRT screen, with a channel strip of 1, 2 and 3 below it. These are big thumb targets, and number keys work too.
- Channel changes use a datamosh smear: the last channel's footage bleeds into the next.
- On a phone, the screen is full-bleed and the channel strip is a fixed bottom bar.

```
 ┌──────────────────────────┐
 │ ░▒▓  CH 2  ▓▒░      LIVE │
 │   [ host, never speaks ] │
 │ ▬ WE HAVE SEEN THIS... ▬ │
 │ NURSES £0 ◂ ticker ◂◂◂◂  │
 ├────────┬────────┬────────┤
 │ 1 FILM │ 2 NEWS │ 3 GOVT │
 └────────┴────────┴────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Tube Black | `#0B0B0C` |
| Phosphor Red | `#E0301E` |
| Static Grey | `#9C9A96` |
| Studio Sodium | `#E8A33D` |
| Daylight Concrete (Channel 3 only) | `#E9E7E1` |
| Hi-Vis | `#F5D300` |

**Type:**
- Channel bugs: Share Tech Mono
- Lower thirds: Oswald
- Tally: DSEG7 (OFL seven-segment font)
- Channel 3: Public Sans

**Motion:**
- Jitter quantised to 12 frames per second, so it feels like tape damage rather than digital shimmer.
- Static that briefly spells readable truths.
- Reception follows the real clock: deeper static late at night.
- The Government channel fades every CRT effect to zero. It is the only clean picture.

**The three strands:**
- **Channel 1, Stories.** A letterboxed trailer wall with a VHS-shelf strip of the eight videos.
- **Channel 2, News.** Bulletin, ticker, the seven-segment "Nurses: £0" and the "money found this week" bug.
- **Channel 3, Government.** Flat daylight, with a hoarding reading "FUTURE PROOF: BUILDING" that overwrites the static.

**Opening line:** "Sorry to interrupt your programme. It ends badly."

**Steals from:**
- Max Headroom signal intrusion: https://www.discoveryuk.com/mysteries/max-headroom-broadcast-signal-intrusion-tvs-strangest-hack/
- The Day Today titles: https://www.artofthetitle.com/title/the-day-today/
- Buck, datamoshing: https://buck.co/sandbox/moshing
- Radio Garden, static between stations: https://swling.com/blog/2016/12/radio-garden-an-addictive-way-to-scan-online-radio-stations

**Risk:**
- VHS and CRT nostalgia is crowded, and shaders are heavy on cheap Android phones.
- It needs a reduced-motion static fallback.
- It needs live data (today's date, this week's tally) so it doesn't feel like a tribute act.

---

## 3. P100

**Pitch:** BadCode is the last teletext service left running. Navigation is by page number.

**Hero moment:**
- The page redraws line by line from the top, the way teletext did, in about 2 seconds.
- The ring and the stepped red triangle assemble from mosaic blocks.
- The eye blinks using the old flash attribute.
- A cursor types "100" and the three index lines fill in.

**Layout:**
- A 40×24 grid with seven flat colours.
- Fastext buttons along the bottom: red for News, yellow for Government, white for Stories, and green for "the bit that works", which is Future Proof.
- Visitors type three digits or tap.
- It works on a phone almost unchanged, because it is just big text.

```
 ┌P100 BADCODE  04 Nov 21:14┐
 │ ▄█▀▀█▄  ◥                │
 │ █    █  STORIES ...... 200│
 │ ▀█▄▄█▀  NEWS .......... 300│
 │          GOVERNMENT ... 400│
 │ NURSES £0   ▓ FLASH ▓    │
 ├──red──┬green┬yellow┬white┤
 └───────┴─────┴──────┴─────┘
```

**Palette (true teletext):**

| Name | Hex |
| --- | --- |
| Black | `#000000` |
| Teletext Red | `#FF0000` (the logo red is used for the triangle only) |
| Yellow | `#FFFF00` |
| Green | `#00FF00` |
| Magenta | `#FF00FF` |
| White | `#FFFFFF` |

Teletext's cyan is dropped on purpose.

**Type:**
- Bedstead (Ben Harris's free teletext font), or MODE7GX
- Long reading: Atkinson Hyperlegible

**Motion:**
- The line-by-line redraw.
- Subpages cycle on their own (1/3, 2/3, 3/3).
- The flash attribute is reserved for the tally.

**The three strands:**
- **P200 Stories.** A TV-guide listing, with each film thumbnail drawn in mosaic. A page opens into a full-colour player.
- **P300 News.** Headlines only. "Nurses: £0" and "money found this week" are permanent fields.
- **P400 Government.** Numbered manifesto clauses, a two-column "Cabinet said / BadCode says" and "LAST AMENDED 07:12 TODAY".
- **Future Proof (P888).** The one page that breaks the grid into a white daylight building site.

**Opening line:** "P100. The only service still running. Ask yourself why."

**Steals from:**
- NMS Ceefax: https://www.raspberrypi.com/news/keeping-ceefax-alive-with-nms-ceefax-the-magpi-118/
- Tim Potter's Ceefax: https://timpotter.dev/projects/ceefax/
- Craig Oldham on teletext's legacy: https://wepresent.wetransfer.com/story/teletext-creative-legacy/
- CodeFronts mosaic recipe: https://codefronts.com/design-styles/css-retro-designs/teletext-and-ceefax-block-graphics/

**Risk:**
- It skews over-40 and can read as a joke about the past rather than a warning from the future.
- The films get no visual room until a page opens out, so the open-out has to be spectacular.

---

## 4. DEPARTURES

**Pitch:** A UK station departures board. Every service to the future is delayed, and BadCode knows why.

**Hero moment:**
- Pitch black except the station clock: the logo ring, with the triangle as the second hand.
- Hundreds of split-flaps clatter into life and settle left to right on STORIES, BULLETIN and GOVERNMENT.
- One red row flips last: "NEXT DEPARTURE 00:03:12", counting down to the next bulletin.

**Layout:**
- A full-viewport enamel board under the eye-clock.
- Three platforms, each a group of rows. Tapping a row expands it into a window onto that strand.
- On a phone, one platform shows at a time, swiped like a station's rotating screens.

```
 ┌───────── ( ◥ ) 21:14 ────┐
 │ PLAT DESTINATION  STATUS │
 │ 1   KAREN WILL LEAD  ON  │
 │ 1   THE BANK ROBBERY ON  │
 │ 2   NURSES ........ £0   │
 │ 2   MONEY FOUND  £4.2BN  │
 │ 3   MANIFESTO  14 CHANGES│
 │ ▌NEXT DEPARTURE 00:03:12 │
 └──────────────────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Enamel Black | `#121212` |
| Flap Amber | `#FFB000` |
| Off-White | `#EFEBE2` |
| Signal Red | `#D7261E` |
| Bezel Grey | `#3A3A3C` |
| Platform 3 Daylight (on expand) | `#F7F3E8` |

**Type:**
- Flaps: Doto (Google's dot-matrix font) or a hand-built flap face.
- Row labels: Barlow Condensed
- Expanded pages: Public Sans

**Motion:**
- Split-flap built with splitflap-js.
- Each strand has its own rhythm: Stories clacks slowly, News clacks non-stop, Government lands with one heavy thunk.
- Sound is off by default.

**The three strands:**
- **Platform 1.** The four stories and eight videos, marked "NOW SHOWING".
- **Platform 2.** Headlines and the running tallies.
- **Platform 3.** Manifesto lines, struck through when the real cabinet contradicts them: "1 CONTRADICTS THE CHANCELLOR, 0 APOLOGIES".

**Opening line:** "All services to the future are delayed. We've seen the cause. It's not the leaves."

**Steals from:**
- splitflap-js: https://github.com/c-hinck10/splitflap-js
- LAb[au], *Signal To Noise*: https://www.creativeapplications.net/project/signal-to-noise-by-labau-512-mechanical-split-flaps-and-the-noise-of-data
- Debt-clock "honest projection" footnotes: https://www.us-debt-clock.com/

**Risk:**
- Small text gives the films no room.
- Flipping text is hard to read for some people.
- It must expand into rich windows, or it becomes a novelty that is dead after one visit.

---

## 5. X MARKS THE SPOT (the ballot)

**Pitch:** A UK ballot paper with three candidates. They are all BadCode.

**Hero moment:**
- The cursor is the pencil on a string.
- After 2 seconds, Xs appear in all three boxes in quick succession, as if a very fast voter filled it in.
- A rubber stamp comes down: "COUNTED". The pencil is handed back to you.

**Layout:**
- One portrait ballot, which is naturally phone-shaped.
- Three rows, each with a number, a candidate name, a description and an emblem box.
- Marking a box draws a hand-pencilled X with a wet-ink sound, and the paper slides into that strand.

```
 ┌──────────────────────────┐
 │ BALLOT PAPER  No. 000100 │
 ├──────────────────────────┤
 │1 STORY, Teller of  [▶][ ]│
 │  Films and songs. Eight. │
 │2 MONEY, For Something    │
 │  News (weekly, regrettably)[£0][ ]│
 │3 GOVERNMENT, The BadCode │
 │  Promises: Future Proof [▲][X]│
 ├──────────────────────────┤
 │ Not a real election. Yet.│
 └──────────────────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Ballot Buff | `#E9E1C9` (pale and grey-green, not cream-terracotta) |
| Rule Black | `#1A1A1A` |
| Pencil Graphite | `#4B4B4D` |
| Logo Red (the only colour) | `#D7261E` |
| Booth Plywood | `#B89B6A` |

**Type:**
- Candidate names: Libre Caslon Text in small caps
- Descriptions: Courier Prime
- Pencil marks: Caveat (hand-drawn)

**Motion:**
- Pencil swing physics on the string.
- The X drawn with a stroke-dasharray animation.
- The stamp thud.
- After voting: "You voted BadCode. So did everyone."

**The three strands:** The layout of each row is identical, so the strands are told apart only by name, description and the object in the emblem box.
- **Stories:** an EP thumbnail.
- **News:** a miniature "£0" tally.
- **Government:** the triangle, plus "Promises to enact Future Proof".

Future Proof opens as a lit, daylight-yellow ballot box.

**Opening line:** "Choose carefully. You didn't last time."

**Steals from:**
- Official Monster Raving Loony Party: https://www.loonyparty.com/
- Best Party / Jón Gnarr: https://en.wikipedia.org/wiki/Gnarr
- The Juice Media, Honest Government Ads: https://www.thejuicemedia.com/

**Risks:**
- Electoral law: misleading voters is an offence. It needs an obviously fictional party name, no real constituency or party names, none of the Electoral Commission's wording, and a printed "not a real election" footer.
- The three strands are treated as equals, so one strand growing later will feel mismatched.

---

## 6. THE HOARDING

**Pitch:** A boarded-up high-street shop front. The real government's promises are pasted over, and BadCode's three posters go up on top.

**Hero moment:**
- A wheatpaste roller runs down the screen.
- Three posters unroll wet, one after another. The third lands crooked.
- The balaclava host is already on one of them, staring. Only his triangle eyepatch is dry.
- A stencil appears beneath: "BADCODE. ISSUED FROM THE FUTURE." The logo is applied as a circular franking stamp.

**Layout:**
- A brick wall seen head-on. The camera doesn't move; the wall does.
- Each poster is printed differently and on different paper, so the strands are legible from across the room.
- Hovering or scrolling peels a corner to show what's under it: a paraphrased, fictional "cabinet line" that the poster answers in the Die PARTEI over-literal style.
- On a phone, the posters stack vertically down a tall hoarding, and you swipe to peel.

```
 ┌──────────────────────────┐
 │▓▒ torn ▒▓ sticker ◥ ▒▓▒▓│
 │┌──────┐┌──────┐ ┌──────┐│
 ││CINEMA││TABLOID│ │ VOTE ││
 ││ONE-  ││ NURSES│ │FUTURE││
 ││SHEET ││  £0   │ │PROOF ││
 │└──────┘└──────┘  └──────┘│
 │ BADCODE. ISSUED FROM THE │
 │ FUTURE.  (◥)             │
 └──────────────────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Wet Brick | `#5A3A32` |
| Paste Grey | `#C9C5BC` |
| Newsprint Black | `#1C1C1C` |
| Logo Red | `#D7261E` |
| Campaign Yellow | `#F3C613` |
| Bottle Green | `#1F4D3A` |

**Type:**
- Tabloid headline: Anton
- Cinema one-sheet: Bodoni Moda in condensed italic
- Campaign leaflet: Rubik Mono One
- Small print: Special Elite

**Motion:**
- Paste roller.
- Peel with paper curl physics.
- Staple pops.
- The "cabinet line" underneath, set in a believable slogan template.

**The three strands:**
- **Stories.** A glossy black cinema one-sheet with grain and pull-quotes for the four films.
- **News.** A tabloid front page, with "MONEY FOUND THIS WEEK" pencilled in a box.
- **Government.** A flat yellow-and-red council leaflet with a rosette and numbered pledges, plus "Have you checked what your Cabinet said today?". The leaflet answers the line pasted beneath it.

**Opening line:** "Previously: someone else's promises."

**Steals from:**
- Die PARTEI: https://en.wikipedia.org/wiki/Die_PARTEI
- Ministry of Information 1939 poster trio: https://history.blog.gov.uk/2014/06/27/keep-calm-and-carry-on-the-compromise-behind-the-slogan
- Shepard Fairey / OBEY, repetition as authority: https://en.wikipedia.org/wiki/Shepard_Fairey
- Barnbrook's Dismaland: https://barnbrook.net/work/dismaland-cruel-designs/

**Risks:**
- Street-art grunge is common. It needs real photographed paste, staples and wet edges, not filters.
- Every under-poster must be a paraphrased fictional slogan. No real faces, no real party layouts.
- Avoid Keep Calm tea-towel cosiness: every poster needs one line that is slightly, menacingly wrong.

---

## 7. YEAR ZERO / YEAR NOW (the two-timeline wipe)

**Pitch:** The screen is split down the middle into the future that went wrong and the building site where you fix it. You drag the seam.

**Hero moment:**
- The page loads entirely in ruin: sodium orange, smoke, chromatic tearing.
- A thin vertical line of daylight rips down from the top, and the right half snaps clean, with scaffolding, plans and hi-vis.
- Caption: "THIS IS WHAT YOU DO NEXT."
- The seam is draggable from the first frame.

**Layout:**
- Three objects run across both halves, so they appear in both timelines:
  - a cinema screen (burnt out / showing a film)
  - a TV (static / the live bulletin)
  - a podium (toppled / a manifesto board)
- On a phone, the seam is horizontal and you drag it up and down, so ruin sits above and repair below.
- A "revert" button snaps the whole page to the clean side. This is the GPOM git-revert as a gesture.

```
 ┌────────────┃─────────────┐
 │ RUIN 2054  ┃  NOW (site) │
 │ [screen ▒] ┃ [screen ▶]  │
 │ [tv  ▓▓▓ ] ┃ [tv NEWS ]  │
 │ [podium ⟋ ] ┃ [FUTURE    │
 │  smoke     ┃  PROOF ▦ ]  │
 │      ◂ drag ┃ ▸           │
 └────────────┃─────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Sodium Ruin | `#C8551B` |
| Smoke Black | `#17130F` |
| Daylight Concrete | `#ECEAE4` |
| Hi-Vis Yellow | `#F5D300` |
| Blueprint Line | `#2B3A55` (ink navy, not cyan) |
| Logo Red | `#D7261E` |

**Type:**
- Ruin side: Saira Stencil One
- Clean side: Barlow
- Notes on the clean side: Permanent Marker, for marker-on-tape annotations
- Receipts: JetBrains Mono

**Motion:**
- The seam's daylight rip.
- The ruin side glitches with scanline decay and crossed-out text.
- The clean side has none of it: it is still, apart from a crane that slowly swings.
- Gource-style, the strand objects visibly fork from one shared trunk when you drag past the halfway point.

**The three strands:** Told apart by the object, which keeps its shape in both timelines:
- Screen = Stories
- TV = News
- Podium = Government

The Future Proof side is where most of the page lives: tenets pinned like site notices, for example "CONTINUOUS INTEGRATION: we test the law before you live in it".

**Opening line:** "Left is what happened. Right is what you do instead. Drag."

**Steals from:**
- Nine Inch Nails, Year Zero ARG: https://en.wikipedia.org/wiki/Year_Zero_(game)
- Gource: https://github.com/acaudwell/Gource
- Sator Square, reads both ways: https://en.wikipedia.org/wiki/Sator_Square

**Risks:**
- The clean side can tip into startup optimism. It has to stay grubby and handmade: tape, tea rings, marker.
- Ruin-orange edges toward GPOM's monumental dark register, which is already overused, so keep the ruin small and the daylight large.

---

## 8. THE PLUG

**Pitch:** A scuffed four-way extension lead on a prepayment meter. Plug in a strand and the room powers up as it.

**Hero moment:**
- Dark. One tired red LED blinks: the triangle as the pilot light.
- Caption: "The future is on a meter. Plug something in."
- Three fat plugs sway in on their flexes. The Government plug is sparking slightly.
- Dragging (or tapping) any plug in gives a mains thunk, a hum and a bulb-warming flicker, and the whole page lights as that strand.

**Layout:**
- A cream plastic block with a burn mark sits low on the screen. Three flexes loop up and form the logo ring.
- Each plug powers a different appliance behind it.
- On a phone, tapping plugs in, the sockets are big, and the meter readout sits at the top.

```
 ┌──────────────────────────┐
 │ METER: £0.43  ◥ ●        │
 │   ╭─────╮ ← flexes form  │
 │   │  ◥  │   the ring     │
 │   ╰┬─┬─┬╯                │
 │    │ │ │                 │
 │  [BLK][RED][HI-VIS]      │
 │ ┌─▣───▣───▣───▢─┐ scorch │
 └──────────────────────────┘
```

**Palette:**

| Name | Hex |
| --- | --- |
| Socket Cream | `#E6DFCF` |
| Unlit Room | `#0E0D0C` |
| Pilot Red | `#D7261E` |
| Flex Black | `#232323` |
| Studio Glow | `#B9C2C9` |
| Floodlight Yellow | `#FFD94A` |
| Burn Brown | `#5B3B24` |

**Type:**
- Moulded labels: Overpass in a heavy weight
- Meter: DSEG7
- Captions: Instrument Serif in italic, for deadpan subtitles

**Motion:**
- Cable physics, kept tight and small rather than a physics demo.
- Power-on flicker.
- Pulling a plug drops the page back to dark.
- The meter ticks down while you browse. It is a joke, and it never blocks anything.

**The three strands:**
- **Black flex → projector.** The Stories glow, a film wall in the beam.
- **Red flex → studio monitor.** News, flickering, with the tally.
- **Hi-vis flex → building-site floodlight.** The Government and Future Proof: the only warm daylight on the site.

**Opening line:** "The future is on a meter. Plug something in."

**Steals from:**
- Retro workshop desk portfolio, insert a thing to change the screen: https://discourse.threejs.org/t/my-portfolio-is-a-retro-workshop-desk-you-can-actually-use/95359
- Bruno Simon, one verb for a whole site: https://www.creativebloq.com/news/3d-car-portfolio
- Low-poly room where you fly into the CRT: https://discourse.threejs.org/t/a-low-poly-room-where-you-fly-into-the-crt/92694

**Risk:**
- Dragging is fiddly on phones, so tap-to-plug must be first-class.
- Skeuomorphic rendering lives or dies on art direction; a stock 3D asset kills it.
- The prepayment-meter joke has to aim at whoever set the tariff, never at the person on the meter.

---

## Ranking

1. **Channel BadCode.** The strongest on all three strands. The News strand is literally TV, the Government channel being the only clean picture makes the argument with no words, and the hijack is a five-second hero.
2. **Year Zero / Year Now.** It answers Kai's brief directly: it pads out Future Proof as the destination, and the drag *is* the GPOM story.
3. **The Wedge.** The most striking and the most "ours", because the logo performs the hero. Its politics-of-form risk is real but manageable.
4. **X Marks the Spot.** Instantly British, flatters the reader's agency and is phone-shaped by nature. The legal care costs effort but is bounded.
5. **The Plug.** The craziest and most class-literate (the prepayment meter). It is held back by build cost and mobile interaction.
6. **The Hoarding.** The best at "same news cycle, opposite conclusions" via the peel, but grunge is the most-copied look here.
7. **Departures.** A beautiful object and a great receipts engine, but it starves the films of picture.
8. **P100.** The cheapest to build, fast on phones and lovable. It is also the most likely to read as nostalgia rather than a warning. Better as one page inside another concept (see grafts).

## Grafts any concept can borrow

- **The eye tracks you.** The logo's triangle rotates toward the cursor or finger, and the ring narrows like an eyelid when you get close (Framer cursor-eye components). No webcam, ever.
- **Honest projection footnotes.** Every live counter ticks from the latest real figure, and small print gives the source, the date and "projected", following the debt-clock model. A wrong number on a page about receipts is fatal.
- **Hansard permalinks as receipts.** Each Government line links to the passage in TheyWorkForYou it answers: https://www.theyworkforyou.com/about/
- **A red figure and a lifeline figure.** Climate Clock style, one per strand: for example "days since promise" against "lines filed today": https://www.smithsonianmag.com/smart-news/clock-new-york-counts-down-time-remaining-avert-climate-disaster-180975881/
- **The one ugly page.** The Best Party move: the Government's "join" form is deliberately council-leaflet cheap, against two slick strands.
- **Page numbers as an easter egg.** Typing 100, 200 or 300 anywhere jumps strands, borrowed from P100.
- **A 404 from the future.** "We saw you'd try this URL." It works the way RCA Records made its 404 page a toy.
- **"Promoted by BadCode, on behalf of the future."** A UK-legal-imprint-style footer on every page.
- **The triangle as a sticker everywhere.** Fairey-style, slapped on photos and corners with deadpan captions. Cheaper and funnier than a hero image.
- **The light changes with the strand.** As in Trivision: night cinema, studio fluorescent, then daylight for Future Proof. Daylight is always the last thing you reach.
- **Catalogue numbers.** BC-01, BC-02 and BC-03 as pressing codes, so the strands feel like sub-labels of one parent mark.
- **A clue in the end-cards.** A code on each YouTube end-card that unlocks something on the homepage (Year Zero's trail).
- **Idle choice.** After 4 seconds idle, the page picks a strand for you: "You were going to click that."