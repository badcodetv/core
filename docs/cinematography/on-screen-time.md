# Putting the year on screen — and keeping it in one place

> **What this is:** how films state *when* we are, researched 2026-08-30 for the camping film's
> 2008 / 2026 / 2031 clock. Tool-agnostic craft. Graded per
> [`evidence.md`](./evidence.md) — **A** hard fact · **P** practitioner consensus ·
> **p** one practitioner or one case · **obs** observed by us in a released film but not
> sourced in this sweep.
>
> Phrasing a prompt is `flow-prompt`. Which tool renders it is
> [`../video-fx/`](../video-fx/README.md). Whether the beat needs a caption *at all* is
> [`principles.md`](./principles.md) **R8**.

## The rule that outranks the rest

🔴 **R8 already governs this.** On-screen text is *a cost, paid deliberately*. A caption
explaining what the image should have shown means the image failed. So before designing a year
device, answer: **is the year doing a job the picture cannot?**

For a film that jumps eighteen years and then five more, the answer is yes — a jump the audience
gets wrong is a jump that costs you the whole reveal. **But the corollary bites:** if the picture
*can* say it, the number should confirm, not announce.

🔑 **Text fixes an image's meaning** — Barthes on anchorage, **A**. That is exactly what a year
does: it takes an ambiguous skyline and makes it a date. It is also why a badly placed number
takes over a frame it was only meant to annotate.

---

## The six families

Ordered by how much they cost the picture.

### 1. The full-frame card

Black frame, the year, cut. The oldest device in cinema — inter-titles were how silent film
carried anything the picture could not, and white-on-black became standard because it projected
cleanest. **P**

- **Costs a beat of screen time and gives it back as rhythm.** A held black frame is on the
  short list of upgrades that need no footage
  ([`motion-and-cutting.md`](./motion-and-cutting.md) §4).
- **Strongest when the film is already chaptered.** *Kill Bill*'s chapter cards,
  *Requiem for a Dream*'s season cards. **obs**
- 🔴 **Weakest when used to paper a jump the cut should have made.** It stops the film to
  explain the film.

### 2. The superimposed card in a fixed screen slot

The year burns in over the live frame, always the same corner, always the same type. The
**lower third** is the broadcast default and exists because it sits clear of faces and clear of
the frame edge. **P**

- **Consistency of placement is the whole technique.** The trade guidance is unanimous and
  boring: same position, same type, same duration, every time — that is what makes it read as
  *the film's clock* rather than as a note. **P**
- **Title-safe is the inner ~80% of the frame** — Netflix's partner spec and every broadcast
  standard agree. Anything closer to the edge gets cropped by somebody's player. **A**
- 🔑 **The one that models what we want:** *(500) Days of Summer*'s day-counter cards, designed
  by Imaginary Forces. The card **recurs in a fixed role** and its *treatment* carries story
  state — greyer and flatter in the bad stretches, brighter in the good. **The position is the
  constant; the colour is the variable.** **p**
- **HBO's *Chernobyl*** cut its place-and-time cards in a bespoke rendering of a Soviet
  typeface — the typography itself is a claim about where you are, not just when. **p**

### 3. The number lives in the world (diegetic)

The date is *in* the scene: a newspaper masthead, a calendar, a dated screen, a scoreboard, a
sign. The clock/calendar is the classic device for time passing. **P**

- **Cheapest to justify, hardest to keep in one place** — the world puts the number where the
  world wants it.
- **Strongest when one prop does two jobs** — a newspaper that dates the scene *and* carries the
  news is worth more than a card that only dates it.
- ⚠️ **Legibility is the failure mode.** A diegetic date the audience cannot read has done
  nothing, and generated footage is unreliable at lettering.

### 4. The same frame, twice — the graphic match

No number moves at all. **The same composition returns and something in it has changed**: a
building, a skyline, a room, a face. The cut itself is the timestamp.

- 🔑 **The most expensive to set up and the only one that is free at the moment of use.** It
  needs the first frame planted early enough that the return lands.
- **A number can ride on top of it** and then the two devices reinforce rather than compete —
  the picture says *time passed*, the number says *how much*.
- **This is the family camping's canon already chose.** See below.

### 5. The counter that never leaves

A permanent HUD element — a countdown, a day tally, a running total — present continuously
rather than at jumps. *The Hurt Locker*'s days-remaining counter is the reference. **obs**

- **Only works when the number is the tension.** Ours is not; ours is orientation. **Not our
  family.**

### 6. Text as the film's argument

Curtis-style: on-screen words as an authorial voice with its own register. Curtis has said the
style came out of necessity — raiding the archive to deadline — rather than design. **p**

- **Tempting for us and dangerous.** Our narrator already has a voice. A second authorial text
  layer competes with it, and R8's failure mode is exactly this.

---

## If you pick a fixed slot, these are the decisions

| Decision | The default that works |
| --- | --- |
| **Position** | One slot, title-safe (inner 80%), chosen to sit in negative space that recurs across the plates. **Never moved.** **A** for the safe area, **P** for the consistency |
| **Anchor** | 🔑 **Screen-fixed beats subject-fixed.** If the number tracks a building, it moves when the building moves and the device stops reading as a device. Fix the pixel coordinates; let the world move behind it |
| **Type** | One face, one weight, one size, all instances. Give it a reason to belong to the world (a period face, a masthead face, a terminal face) rather than a default sans |
| **Duration** | Appear ~0.5s after the cut so the shot lands first, hold ~1.5–2s, out. Same every time |
| **Animation** | Pick none or pick one, and never mix. A number that fades in once and slams in once reads as an error |
| **Contrast** | White-on-black halation slows reading — **A**. On our near-black register, prefer a soft off-white or a knocked-back grey over pure white at large sizes |
| **The one break** | A device that never varies can afford to break **once**, at the beat that matters most, and the break must mean something. Twice and there is no device |

## 🔴 What we can actually build

**Premiere's API cannot write a string at all.** `SimpleText` and MOGRT text both throw
`Illegal Parameter type`; an exported frame still read *"Default Text"* after the write appeared
to succeed. Measured 2026-08-22 — [`../premiere/api-notes.md`](../premiere/api-notes.md). **A,
house-measured.**

**So any automated on-screen year is an ffmpeg `drawtext` job**
([`../video-fx/ffmpeg-catalogue.md`](../video-fx/ffmpeg-catalogue.md)) — which is *good news for
this problem specifically*: `drawtext` takes exact x/y, so "the same place every time" is a
constant in a script rather than a thing a human eyeballs three times.

⚠️ **Do not ask Flow to render the number into the plate.** Generated lettering is unreliable,
and we have already ruled the same way twice on this film — the `W-AI-trose` gag and the `10b`
fascia are both **post jobs**. The year is the same call.

## Sources

- [Film title design through cinema history](https://www.smashingmagazine.com/2010/10/the-art-of-the-film-title-throughout-cinema-history/) · [The graphic art of film titles](https://www.canva.com/learn/film-titles/) · [A brief history of film title design](https://www.linearity.io/blog/movie-title-design/)
- [Title card — study guide](https://www.studyguides.com/study-methods/study-guide/cmmkfg1o487jw01aa1qrl2rkg)
- [Lower third](https://en.wikipedia.org/wiki/Lower_third)
- [Netflix — titles & graphics requirements](https://partnerhelp.netflixstudios.com/hc/en-us/articles/360034536253-Titles-Graphics-Requirements-Best-Practices) · [Netflix — title safe and safe action](https://partnerhelp.netflixstudios.com/hc/en-us/articles/4406208331923-Title-Safe-and-Safe-Action-Best-Practices) · [What title safe is and why it matters](https://www.veneratech.com/what-is-title-safe-and-why-it-still-matters-in-modern-video-production)
- [Imaginary Forces — (500) Days of Summer](https://imaginaryforces.com/project/500-days-of-summer)
- [HBO *Chernobyl* typography](https://standarddesigns.co.uk/blogs/standard-designs-blog/hbos-chernobyl-typography)
- [Time-passes montage](https://tvtropes.org/pmwiki/pmwiki.php/Main/TimePassesMontage) · [Exploding calendar](https://tvtropes.org/pmwiki/pmwiki.php/Main/ExplodingCalendar) · [Writing the passage of time](https://www.studiobinder.com/blog/passage-of-time/)
- [Adam Curtis on his method](https://www.dazeddigital.com/artsandculture/article/33496/1/adam-curtis-hypernormalization-bbc-film-power)

⚠️ **What the sweep could not find:** any comparative analysis of fixed-corner date cards across
named films. The placement guidance above is broadcast-graphics practice, not film scholarship.
Everything marked **obs** is our own viewing, not a source.
