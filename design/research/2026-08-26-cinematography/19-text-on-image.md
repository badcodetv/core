---
brief: 19
title: Text on image - typography and captions as composition
swept: 2026-08-26
wave: 2
closes_gap: 5
searches_used: 8
---

# 19 - Text on image - typography and captions as composition

## 1. The short answer

- Text laid over an image is not decoration, it is a second compositional element with its own
  weight and its own claim on the eye — treat caption placement as a blocking decision, not an
  afterthought. **(p — craft consensus from comics lettering, no controlled study)**
- In English, the eye reads left-to-right, top-to-bottom, inside a balloon, inside a panel, and
  across a whole page — so a caption placed anywhere other than where that scan path already
  wants to go fights the reader instead of guiding them. Source: Todd Klein (below). **(p —
  single named practitioner, but the most decorated one in the craft, 18 Eisners)**
- Never let text cover a face; avoid covering hands (a comics-lettering rule that generalises —
  faces and hands are where a viewer's attention already lands, so covering them costs the most).
  **(p)**
- On a near-black frame with one thin light source — our exact house register — light text on
  dark ground is legible, but pure white on pure black is the worst version of it: it triggers a
  real optical bleeding effect (halation/irradiation) that softens edges and slows reading,
  worse for the roughly half the population with astigmatism. Use off-white, not pure white, and
  don't go for maximum contrast. **(A for the optical mechanism — see §2; the astigmatism
  prevalence figure is *(unverified in sweep)*)**
- WCAG's 4.5:1 minimum contrast ratio for body text is a real, citable floor — but treat it as a
  floor, not a target; comfortable reading at video pace wants more than the accessibility
  minimum, and thin/light-weight fonts read weaker than their measured contrast value implies.
  **(A — W3C standard grounded in vision-science testing)**
- 50–75 characters per line is the standard print/screen readability range; for a caption held
  for a few seconds under narration, go shorter, not longer — the reader has less time than a
  page does. **(P — repeated across typography practitioner sources, treated as trade wisdom not
  measured fact — see §2)**
- Most short-form video is watched with the sound off. This is BadCode's actual delivery
  condition for anything posted to feed-based platforms, and it means on-screen text sometimes
  has to carry the *entire* meaning, not reinforce audio. **(P — company-disclosed usage data,
  not independently replicated — see §2)**
- A caption is not a neutral label: changing the words under an unchanged image changes what the
  image means, because a viewer resolves ambiguity in an image by reading it in light of the
  words next to it (Barthes calls this "anchorage"). We are relying on this constantly — it's how
  narration + still functions as a form at all. **(A — canonical semiotics text, widely cited;
  see §2 for the counter-position, "relay")**
- The argument against on-screen text is real and worth holding in tension: a caption that
  explains what an image itself should be showing is often a confession the image didn't do its
  job. Treat every caption as a cost, paid only when the image genuinely can't carry the beat
  alone. **(p — a documented editorial position among photography theorists, not a measured
  claim — see §4)**
- Kinetic (moving) typography is doing real work only when the motion encodes something the
  static word can't — pace, hesitation, sudden emphasis, a line getting cut off; used as
  decoration (bouncing letters, generic sweep-ins) it competes with the image for no payoff.
  **(A mixed — single empirical HCI study plus one contested theory text, see §2)**
- Text placed over a moving or AI-generated background is placed over a surface you do not fully
  control — this argues structurally for a text-safe zone (a deliberately quieter part of the
  frame, or a scrim) decided *before* generation, because you cannot art-direct the pixels behind
  a caption after the fact the way a compositor can. This is our own inference from the
  constraint, not sourced.

## 2. The findings

**Reading order in a captioned frame follows the same left-to-right, top-to-bottom scan path
whether it's a comic page or a single frame with a caption box.** Grade: **p**. Todd Klein — the
most awarded letterer in comics history (18 Eisner Awards, lettered Neil Gaiman's *Sandman* for
its entire run) — states it directly in his own published placement guide: "In English we read
across from left to right, skip down, then left to right again. This happens inside a balloon,
inside a panel, and across a whole page." He adds the specific rule that within a panel "it's
always best if the character on the left speaks first," because the alternative forces the eye
to jump backward. Source: [Todd Klein, "How To Place Balloons"](https://kleinletters.com/BalloonPlacement.html).
This is one named, credentialed practitioner's stated method, not a study — graded p, not P,
honestly. It is corroborated in spirit by the general reading-order literature but that
literature is about prose, not comics captioning specifically.

**Balloons/captions shouldn't cover a speaking character's face; avoid covering hands where
possible; a balloon overlapping a figure should stay consistently in front or behind, never
switch mid-figure.** Grade: **p**. Same source, same page: "Balloons and captions shouldn't
cover figures. When they must, try not to cover hands and feet, and never cover faces of
important characters." And: "balloons usually shouldn't go behind one part of a figure and in
front of another." One named practitioner, no second corroborating source in this sweep —
flagged p, not P, per the grading discipline this corpus is enforcing.

**Anchorage: a caption resolves the ambiguity of a polysemic image by directing the viewer to
one meaning among several the image alone could support.** Grade: **A**. Roland Barthes,
"Rhétorique de l'image" (1964) / "Rhetoric of the Image": the linguistic message "directs the
reader through the signifiers of the image, causing him to avoid some and receive others," and
functions denotatively, answering "what is it?" This is the standard citation in photography
and film-semiotics scholarship, not a contested fringe reading. Barthes also names a second,
rarer function — **relay** — where "the words, in the same way as the images, are fragments of
a more general syntagm," used when text and image are equal partners advancing a single story
rather than one captioning the other; he specifically names cartoons/comic strips as the home
of relay. **This is the theoretical name for what BadCode's narration-over-still actually is
most of the time — closer to relay than to anchorage, because the VO carries plot the image
doesn't restate.** Source: [Rinnert & Lane's summary of Barthes, "Rhetoric of the Image"](http://utep1311.pbworks.com/f/Rinnert+and+Lane+-+On+Barthes+Rhetoric+of+the+Image.pdf)
*(secondary summary of the primary text; the primary essay itself, in *Image-Music-Text*, was
not independently re-read in this sweep — unverified in sweep for exact wording, but the
anchorage/relay distinction itself is uncontested textbook material)*.

**Pure white text on a pure black ground triggers halation — a real optical bleeding effect
where bright text edges appear to glow/blur into the dark ground — measurably reducing
legibility versus a slightly desaturated or off-white value on a dark-grey (not pure-black)
ground.** Grade: **A (mixed)**. The mechanism (irradiation: bright regions appear to expand into
adjacent dark regions on the retina) is established vision science, cited across accessibility
literature. The specific "13% slower reading on pure black vs tuned dark-grey" figure appearing
in current design-blog coverage of this effect could not be traced to a named study in this
sweep — **flag as unverified figure riding on a real mechanism**. What is solidly sourced: WCAG
itself warns that "thin or unusual fonts may appear weaker than the specified contrast would
imply" against a dark ground, which is the actionable version of the same fact. Source:
[Level Access, "Astigmatism and Web Accessibility"](https://www.levelaccess.com/blog/accessibility-for-people-with-astigmatism/)
and WCAG 2.x contrast-ratio guidance (§2.1) *(the ~50% astigmatism-prevalence figure quoted
across these sources is unverified in sweep — treat as directional, not precise)*.

**Short-form social video is overwhelmingly watched without sound; captions materially change
watch time.** Grade: **P (company-disclosed, not independently replicated)**. Facebook's own
data, reported by Digiday in 2016, put video-without-sound at roughly 85% on the platform; more
recent industry figures (Verizon Media/Publicis Media, 2019, via Forbes) put sound-off viewing
at 69% across a broader consumer survey, and cross-platform breakdowns commonly cited put
Instagram nearer 40% and LinkedIn nearer 80%. **These numbers disagree with each other by a wide
margin (40–85%) because they come from different platforms, years, and methodologies — the
honest summary is "a majority, often a large majority, not a fixed number."** None of this is
peer-reviewed; all of it is platform or vendor-disclosed usage telemetry reported through trade
press. Sources: [Digiday, "85 percent of Facebook video is watched without sound"](https://digiday.com/media/silent-world-facebook-video/);
[Forbes, "Verizon Media Says 69 Percent Of Consumers Watching Video With Sound Off"](https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/).
**For BadCode this is still the load-bearing fact of the whole brief**: on a sound-off feed
platform, on-screen text is not a redundant accessibility layer, it is very often the primary
channel.

**Kinetic typography carries emotional/paralinguistic information that static text cannot —
timing, rhythm and motion of type can shift how a line is read the way vocal prosody shifts a
spoken line — but the empirical base for *which* motion means *what* is thin.** Grade: **A
(mixed)**. Johnny C. Lee, Jodi Forlizzi and Scott Hudson (Carnegie Mellon, published in the HCI
literature as "The Kinetic Typography Engine," building on Ford/Bellantoni-style design study)
built and tested a system generating kinetic type from expressive rules; the design-theory side
traces to Yvonne Bellantoni & Matt Woolman's *Type in Motion: Innovations in Digital Graphics*
(1999), which catalogued techniques (blinking, scaling, timing) as an expressive vocabulary but
is a design-practice text, not an experimental one. A 2013 IASDR paper (Amic G. Ho, "Typography
Today: Emotion Recognition in Typography") explicitly calls for more research, stating the
field of "emotion in type/typography" is still under-explored. **Net: real effect, thin
evidence — treat specific claimed mappings (e.g. "letters that shake read as fear") as design
lore, not fact.** Sources: [Amic G. Ho, IASDR 2013 paper (PDF)](http://www.design-cu.jp/iasdr2013/papers/2213-1b.pdf);
[Wikipedia summary of Bellantoni & Woolman's taxonomy](https://en.wikipedia.org/wiki/Kinetic_typography)
*(the Bellantoni book itself not directly re-read in this sweep — unverified in sweep for exact
wording, secondary summary only)*.

**Title sequences can carry plot information the film's structure withholds, and the typographic
execution itself can encode the antagonist's psychology.** Grade: **p**. Kyle Cooper on *Se7en*
(1995), in his own account: "When I was a kid and I would watch horror movies, the monster
didn't come out until the third act... I wanted to somehow introduce the killer in the titles."
The lettering was scratched by hand into the film stock rather than set digitally, a choice
Cooper frames as characterization, not style: "I wanted it to be drawn by hand, because it was
from the mind of the killer... wanting it to be like the killer did the film opticals himself."
One named practitioner's account of one sequence — graded p, but it is the single most-cited
title sequence in the modern canon (IFC ranked it third greatest of all time, behind Bass's
*Vertigo* and Lester's *A Hard Day's Night*) so it is not a marginal case. Source:
[Art of the Title, "Se7en (1995)"](https://www.artofthetitle.com/title/se7en/).

## 3. What survives our constraints

Text is the one layer BadCode adds entirely in post — it is set, not generated, so everything in
this brief survives the no-crew/no-reshoot/one-8-second-clip reality better than almost anything
in the other eighteen briefs.

**Fully survives, no cost:**
- Klein's reading-order rule (place captions where the scan path already goes) — pure layout
  discipline, done in the comic engine / edit software, zero generation cost.
- Face/hands avoidance rule — same, a placement check against the still we already have.
- Off-white-not-pure-white on dark ground, WCAG contrast floor, shorter-than-print line length —
  all typesetting decisions made after the image exists; cost nothing, change nothing about the
  generation.
- Sound-off design (captions carry full meaning on feed platforms) — a scripting/editing
  discipline: write the caption to stand alone, independent of whether narration plays.
- Anchorage vs. relay as a diagnostic — before writing a caption, decide which job it's doing
  (pin down one meaning, or advance the story the image can't) — a free thinking tool, not a
  production step.

**Partial — needs a decision made *before* generation, not after:**
- A text-safe zone on a generated or moving background. We cannot art-direct pixels behind a
  caption after the fact the way a compositor keys and re-lights a plate. The mitigation that
  survives: prompt/compose for a deliberately quieter region (the near-black our register already
  favours helps here), or add a light scrim/gradient in post — a scrim is a compositing step we
  fully control and costs nothing per-generation.
- Kyle Cooper's "typography as characterization" (hand-scratched lettering = the killer's
  interiority) survives in spirit — a caption's *typeface and treatment*, not just its words, can
  characterize the narrator — but the bespoke hand-craft (scratching actual film stock) obviously
  doesn't; the portable version is choosing one deliberate type treatment for the narrator voice
  and holding it, not a one-off effect per shot.

**Dies outright:**
- Kinetic typography as a per-shot bespoke choreography (a title designer hand-animating one
  line's motion to match its exact meaning) — that is bespoke motion-graphics labor per line,
  which does not fit an 8-second-clip, no-crew pipeline. The survives-version is a small, reused
  library of motion presets (fade, hold, cut) applied consistently, not one-off invention per
  caption.
- Nothing else in this brief requires a set, an actor, or a reshoot — text is uniquely cheap for
  us, which is the whole point of writing this brief now.

## 4. Contested

**Berger vs. Sontag on whether a caption can make a photograph mean something true.** Susan
Sontag (*On Photography*) is the more skeptical position: a photograph is inherently ambiguous
and a caption is a kind of imposition that can never fully close that ambiguity — captions
manipulate more than they clarify. John Berger takes the opposite, more constructive position:
he holds that photographs *can* produce real understanding, but "only when placed within
narrative, explanation, and political analysis" — for Berger the caption/sequence is not a
compromise on the image's purity, it's the thing that activates it. **This is a live
disagreement, not a resolved one, and it matters directly for BadCode**: Sontag's position
implies every caption is a small dishonesty; Berger's implies the narration is doing legitimate,
necessary work the image alone cannot. BadCode's whole form (narration over still) is a bet on
Berger being right. *(Secondary summary of both positions —
[Heretakis, "Photography, Power, and the Burden of Seeing"](https://heretakis.medium.com/photography-power-and-the-burden-of-seeing-sontag-barthes-and-berger-in-critical-conversation-3329a593f949)
— primary texts of both *On Photography* and Berger's *Understanding a Photograph* not directly
re-read in this sweep, unverified in sweep for exact wording.)*

## 5. Myths — never cite

- "White text on black is the most readable combination because it's maximum contrast." **False
  as stated** — maximum contrast is not the same as maximum legibility; halation makes pure
  white-on-pure-black measurably worse to read than a slightly reduced-contrast pairing (off-white
  on dark grey). Never cite "more contrast is always better" without the halation caveat.
- "Adding captions is always good for engagement, full stop." The specific percentage lifts
  quoted around the internet (e.g. "80% more likely to watch to completion," "12% longer watch
  time") come from vendor/platform marketing pages (Verizon, Facebook's own case studies) with no
  visible methodology — treat every specific percentage in this space as a marketing claim, not a
  measured fact, unless traced to a named, published study.
- "Sound-off video watching is a fixed, known percentage (e.g. '85% of video')." The number
  varies by 40+ points depending on platform, year and source; citing one fixed figure as a
  universal truth is exactly the kind of laundering this corpus was warned about.
- Any specific claimed mapping between a kinetic-typography motion style and a specific emotion
  (e.g. "shaking text = fear," "slow fade = melancholy") stated as settled fact — the design
  literature offers these as a working vocabulary, not as tested findings.

## 6. Vocabulary worth having

| Term | Plain-English gloss | What it buys you |
| --- | --- | --- |
| Anchorage | A caption that pins an ambiguous image down to one specific meaning | The tool for "what am I looking at" captions — control, at the cost of narrowing the image |
| Relay | Text and image as equal partners advancing one story together, neither redundant | The tool for narration-over-still — the VO carries story beats the image can't show |
| Halation / irradiation | The optical bleeding of bright text into a dark ground | The reason to avoid pure-white-on-pure-black and use off-white on dark grey instead |
| Safe area / text-safe zone | A deliberately visually quiet region of the frame reserved for text | Lets you commit to caption placement before the background is finalized |
| Scrim / gradient plate | A darkened or gradated overlay placed behind text in compositing | Guarantees contrast on a background you don't fully control (moving, generated, busy) |
| Balloon tail | The pointer on a speech balloon indicating who's speaking | Establishes attribution without needing a name label |
| Kinetic typography | Type whose motion (timing, scale, shake) itself carries meaning | A tool for encoding tone/emphasis text alone can't — use sparingly, it's expensive craft |
| Legend / lower-third | A persistent identifying caption anchored to a fixed screen region | Documentary convention for naming a person/place without narration doing it |

## 7. Open questions

- No source in this sweep addresses text placement specifically *for a scroll-driven* format
  (BadCode's actual comic engine) as opposed to a fixed film frame or a static comic page —
  scroll position changes what's "above" and "below" continuously; nothing here was written with
  that reading mode in mind.
- The astigmatism-prevalence figure (~50% of population) and the "13% slower reading on pure
  black" figure both showed up repeatedly in design-blog coverage but could not be traced to a
  named primary study in an 8-search budget — worth a dedicated vision-science search if this
  brief needs to bear real weight in a decision.
- No practitioner source was reached specifically on newspaper/broadsheet column typography
  (relevant to the Imperial Gazette device) — this sweep covers comics lettering and film titles,
  not print-journalism layout craft, which is a distinct tradition (grid, masthead, column rules)
  BadCode is directly imitating and hasn't sourced.
- Kyle Cooper is one case; Saul Bass's own stated design philosophy (rather than secondary
  summaries of it) was not directly quoted in this sweep — worth going to a primary Bass
  interview if the title-sequence material needs to carry more weight.

## Sources

| URL | What it is | Grade of the source itself |
| --- | --- | --- |
| https://kleinletters.com/BalloonPlacement.html | Todd Klein's own published lettering-placement guide | Practitioner primary (named, credentialed) |
| https://www.artofthetitle.com/title/se7en/ | Art of the Title interview/feature on Kyle Cooper's *Se7en* titles, with Cooper's own quotes | Practitioner primary (interview-sourced trade site) |
| http://utep1311.pbworks.com/f/Rinnert+and+Lane+-+On+Barthes+Rhetoric+of+the+Image.pdf | Academic summary/close-reading of Barthes' "Rhetoric of the Image" | Secondary academic (summary of a primary theory text) |
| https://www.levelaccess.com/blog/accessibility-for-people-with-astigmatism/ | Accessibility-vendor explainer on halation and astigmatism | Practitioner/vendor (accessibility industry, not academic) |
| WCAG 2.x §1.4.3/1.4.6 contrast guidance (W3C) | The formal accessibility standard for text contrast | Primary standard, vision-science grounded |
| https://digiday.com/media/silent-world-facebook-video/ | Trade-press report of Facebook's internal sound-off viewing data | Trade press reporting company-disclosed data |
| https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/ | Trade press report of Verizon Media/Publicis Media survey data | Trade press reporting vendor survey data |
| http://www.design-cu.jp/iasdr2013/papers/2213-1b.pdf | Amic G. Ho, "Typography Today: Emotion Recognition in Typography," IASDR 2013 conference paper | Peer-reviewed conference paper (single study, explicitly calls itself preliminary) |
| https://en.wikipedia.org/wiki/Kinetic_typography | Overview/history including Bellantoni & Woolman's taxonomy | Secondary tertiary source (encyclopedia, used only for uncontested historical facts) |
| https://heretakis.medium.com/photography-power-and-the-burden-of-seeing-sontag-barthes-and-berger-in-critical-conversation-3329a593f949 | Essay comparing Sontag/Barthes/Berger positions on photography and text | Secondary commentary (content-mill-adjacent; primary Sontag/Berger texts not independently re-read) |
