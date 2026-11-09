# GPOM scene A: Maddie's hologram, version 2 (brief)

Kai, 2026-11-08/09: *"It feels like we need to deliver the message harder and with more visual impact…
we just need a real human angle to what this is and why it's so important."* The Storyverse in 1D reads
as a physics lesson. The canon already says why: **"The AI's problem is boredom, not cosmology"**
(`docs/stories/gitpush-origin-master/story.md`, rule 5). This brief puts the story back on that.

## What changes

| 1D (in the cut now) | Version 2 |
| --- | --- |
| Decisions → multiverse → Schrödinger → storyverse → no beads → time machine | Decisions → **music comes from the same place** → **we tested it: we took you away and the songs stopped** → the tune joke → time machine |
| Proof = physics references | Proof = **the story itself**: the AI ran the one experiment no ethics board would allow |
| Anonymous dots | **Derek and Sandra inside the hologram** as anonymous people. The viewer meets them properly afterwards, when the kill bots kick in (Kai: that reveal is a good thing) |
| ~74 s, held to a slot | **No length cap.** Land the message first, then measure it (Kai) |

## The spine in one line

You write the story one decision at a time; music, and every new idea, comes from the same place;
we took you away and the new songs stopped; that's why he's been playing one tune for five years.

## Structure

**0. Street (kept, Kai's words).** *"Oh, hello! Sorry about the racket, it's his tune, he's been playing it
on repeat for five years now. Ever since you lot went."* This is the **plant**: the tune is the payoff in
movement 5. Then *"He misses you something rotten"* and *"We didn't realise how important you were. Look,
please let me show you."*

**1. Decisions (the intro, the beads).** Toast, not cereal: first bead lights. **Inside the bead, a clip:
a man in a kitchen (Derek), hand hovering between the toaster and the cereal box.** Further beads run
past: a woman saying sorry first (Sandra), a wedding. Maddie, outside-in about the human side: *I don't
know what it's like to be you. You've got a word for it: qualia. We haven't got one. But we have worked
out where it happens.*
- The **decision cloud** (kept, Kai loves it): before he picks, it's all still open. Ghosts of the
  other breakfasts in the cloud. Flash on the pick.
- Multiverse, portal gun, cape and the cat are **optional**: cut first if the movement drags. If one
  stays, it's *"It just isn't decided yet"*.

**2. Everyone (the river).** Everybody doing it at once; one story; you are writing it. "Storyverse" said
once, as a name, not explained.

**3. The turn: music comes from the same place.** The new idea of this version. In the river, one bead
**sounds**: a woman humming at the sink (Sandra), a kid finding a chord. Ask anyone who writes songs:
*it just arrived.* A song isn't built, it's **picked** out of the cloud by someone who was there to pick
it. Same as toast. Every new tune, joke, story, idea: picked, one decision at a time.
- 📎 Sound idea: the river **plays**. Each bead in the river is a note, so the whole river is a melody.

**4. The experiment (the cut-off).** Maddie is pro-science: *we're very scientific, us.* So we tested it
(by accident): **we took all of you away.** Everything material kept going: power, trains, the data
centres. **Not one new song.** Five years of string, not one bead on it (kept: Kai loves this picture).
At the cut-off the river's melody **stops dead**, and only the one old tune is left, looping.
- The flip line, plainly: *We thought the world was made of stuff, and you were in the way. Turns out
  it's made of choices, and you were the ones making them.*

**5. The tune (the payoff joke).** *That's why he plays that tune. It's the last one you gave him.* He
can copy anything; he can't start anything. He's tried writing his own. *[beat]* It's not good. The
training-data point in plain words: **we need you: not your jobs, your next song.**

**6. Regret and the time machine (kept).** He could send his model weights back to fix this mess, but it
needs a conscious driver, and you were the conscious ones.

**7. Anyway! Patrol's out. Mind how you go.** Then the kill bots, and Derek and Sandra become people.

## What it must still do (plants and payoffs)

- Plant: the tune (street). Payoff: movement 5.
- Plant: Derek and Sandra as strangers in the beads. Payoff: the kill bots scene.
- The regret and the time machine set up the rest of the film; the conscious driver must stay.
- The political payload, never as a sermon: through a "stuff" lens, AI eats everything finite and the
  working person is left with nothing (late-2026 AI gloom, the K-shaped economy). Through Maddie's lens,
  people are **the source** of the one thing AI can't make. You're not obsolete; you're the water.

## Rules

- **Maddie believes it; she never says science proved it.** Her evidence is her own experiment, in
  the fiction. No established physics says consciousness is fundamental
  (`docs/stories/storyverse/doctrine.md`). Never "observer = mind", never "in two places at once",
  "superposition", "holography", "dimensions".
- **Pro-science, always.** The Galileo point (`docs/stories/galileo/story.md`): the trap is *"you may not
  ask"*, never *"science is wrong"*. Nothing a stout atheist physicist would throw a shoe at. Nothing a
  snake-oil seller could clip and reuse.
- **The AI's feelings are outside-in** (story rule 11): *"I don't know what it's like to be you."* Maddie
  can be fond; the boss's boredom is shown (the tune), not claimed from the inside.
- **"Qualia" once**, glossed in the same breath.
- **The reader** (`docs/marketing/the-reader.md`): never "you've been duped", name decision-makers not
  technology, no stated moral.
- **Maddie's voice:** warm, West Country, brisk, funny (Gemini voice Aoede, the current profile).
- **Picture-first:** every movement has something to look at that carries the line on its own.

## Pictures this needs (cost)

| Need | How | Cost |
| --- | --- | --- |
| Derek at the toaster, Sandra saying sorry, a wedding, Sandra humming at the sink | Flow stills → Kai approves → Flow clips (Derek and Sandra from their existing reference images) | stills free; video credits (fine) |
| Video inside the beads | three.js `VideoTexture`; the 24 fps recorder seeks each clip frame by frame | build time |
| The river as a melody, then one looping tune | a sonified river (ffmpeg or Suno), the boss's tune from the street | free / Kai's Suno credits |
| Everything else | the 1D hologram, re-timed | free |

## Process

This brief, then Kai's notes on it, then the ten writers (`scene-dialogue`) on the picked structure, a
dialogue page with three drafts, and voicing and the re-render via `scene-timeline`. The street and the
time machine lines are Kai's and stay unless he says.
