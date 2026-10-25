# Money For Something, 26 Oct: the format with the host off screen

**Status: proposal, 25 October 2026, for Jack. Not ruled. Kai has not seen it.**
Jack, 25 Oct: "the host should only be in the screen sparingly, like only the intro and outro… our badcode money for
something guy is emotionless therefore boring to look at, also, its for short form content anyway."

## The verdict: he's right, so the voice and the picture carry the jokes

A panel show sells a joke with a face. Ours has no face, so the punchline has to land on **the cut**: the voice
sets it up dead straight and the picture delivers it. That's the Charlie Brooker *Screenwipe / Newswipe / Weekly
Wipe* shape: narration over news footage, the host seen in a room only round the edges (read: Wikipedia, British
Comedy Guide). Cunk works the same way: the deadpan never moves, and the cutaway gets the laugh.

The host's blankness is still useful, but as a **stillness gag**: put him on screen only when doing nothing *is*
the joke (the Buster Keaton "Great Stone Face" rule: the world reacts, he doesn't). *(My reading, p-grade.)*

## The shape: one story = one short

The 30-row script becomes **about 8–10 shorts**, one topic each, 20–45 s. The long version, if we make one, is just
those shorts in a row with the host's bookends.

| Slot | What's on screen | Length |
| --- | --- | --- |
| **Hook** | The strongest fact as a card or the footage, with the voice already talking. **No host here**: in a short, the first frame has to be the story | 1–3 s |
| **Facts** | Footage / photos / loud cards (cut 4's style), one text overlay per beat, burnt-in captions | most of it |
| **Turn** | The voice's last word, then a **hard cut to the punch picture** (a meme image, a card, a contrast photo) | 1–2 s |
| **Host tail** | Plate H1: he does one silent thing (pushes the pint away, turns his head to camera, one gloved finger). Then the logo | 1–2 s |

**The host's budget in a short is one appearance: the tail.** In the long version: the cold open, the ending, and
at most one silent insert in the middle (the pint). He never talks on camera, so no lip-sync work.

## What changes in the work

- **The script gets a fourth column: the punch picture.** Every row now needs "what we cut to on the turn" as well
  as the line. That's where the jokes live now, so Jack writes it or picks from options.
- **The voice is the performer now.** The TTS voice carries the timing the face used to. Worth a short voice round
  in AI Studio (deadpan, unhurried, British) before the lines are recorded.
- **Fewer Flow clips:** four stock host clips from plate H1 (sit, pint, head turn, finger), made once, reused every
  week. The rest is real footage, photos and cards, like the 2026 cut 4.
- **Sound-off first:** every short must work muted: hook card, captions, punch picture (shorts-factory rules).
- **The intro hook isn't the host.** If Jack wants the host at the start of the long cut, keep it there. In the
  shorts, the host goes at the end only.

## Three shapes, one recommended

1. **Recommended: Newswipe vertical.** As above: voice and footage, a 1–2 s host tail on every short. Cheapest,
   the most joke per second, and the host becomes the series' signature.
2. **The bug.** Ray William Johnson's set from the 20 Oct meeting: the host stays small in a corner over the
   footage the whole time, like a TV station's logo. It brands every frame, but it's a motionless figure eating
   screen space in a vertical frame. 🔴 **And it breaks Jack's 18 Oct rule: never put AI people into real footage**
   (join real and AI by the cut only). So it only works over cards and generated pictures, never over news clips.
3. **Text-only.** No host at all, just the voice and cards. Loses the brand.

## Sources

- Charlie Brooker's Weekly Wipe / Newswipe / Screenwipe: https://en.wikipedia.org/wiki/Charlie_Brooker%27s_Weekly_Wipe ,
  https://en.wikipedia.org/wiki/Newswipe_with_Charlie_Brooker , https://en.wikipedia.org/wiki/Charlie_Brooker%27s_Screenwipe
- Ray William Johnson (Equals Three: fast jump cuts; now story-time shorts on TikTok, Facebook and Instagram):
  https://en.wikipedia.org/wiki/Ray_William_Johnson , https://tubefilter.com/2015/02/13/top-6-kelly-landry-ray-william-johnson-equals-three/
- Repo: `docs/marketing/shorts-factory.md` (hook bar, captions, safe areas), `docs/story-craft/forms.md` §2
  (short-form cutdowns: script the opening as its own artefact; one overlay per beat), `docs/marketing/money-for-something-series.md`.
- No source found on how well faceless satire news does in numbers. Unmeasured, not claimed.

## The overlay: BadCode's own news furniture over the footage (Jack, 25 Oct, later)

Jack: "i worried just footage of stuff/news would be boring, can we have like a badcode overlay over it like a bbc
news banner or a badcode version".

**What the research says:** the parody news shows made the **graphics themselves a joke layer**. *The Day Today*
stayed faithful to real news "with spinning graphics and portentous tone"; *Brass Eye*'s send-up of "self-important
and melodramatic TV graphics" was one of its strengths (read: Wikipedia, chortle.co.uk). Onion News Network's head
writer said the aim was to "mirror the look and feel" of cable news and its touch-screen graphics, and its chyrons carry
lines a real one never would (read: CJR, NPR). So the overlay is a second joke track, not decoration. A lower third gets
about two seconds of reading (trade explainer, generic, p-grade).

**Mock-ups (stills, not motion):** `money for something\2026-10-26\overlay\` · kit
`scripts/money-for-something/oct26/build-overlay-mock.py`. The words on them are **placeholders: Jack writes the jokes**.

| | **A: BROADCAST** | **B: TRANSMISSION** |
| --- | --- | --- |
| Idea | A real news channel's furniture, but ours: BADCODE NEWS, "LIVE · 2054" | A signal received from the future: ring bug, "RECEIVED 25.10.2026 / SENT 2054 · SIGNAL 71%", viewfinder brackets, scanlines, cold grade |
| Chyron | BREAKING (AGAIN) tag, a straight headline, then a yellow strap for the joke | ARCHIVE · ITEM 0412, the quote, then a yellow `›` line where the future corrects it |
| Extra joke layer | **The ticker, "LATER":** future headlines crawling under everything, one gag each | **Signal strength** that drops when the news gets worse; glitches on the turn |
| Read | Instantly "news"; most familiar; the ticker rewards a second watch | More BadCode, less BBC; colder; fits the "from the future" premise |

**My pick: A's furniture with B's premise**: the channel strip, chyron and LATER ticker from A, with B's "sent 2054"
clock in place of LIVE. The chyron's yellow strap is where the punchline lands, timed to the voice's turn.

**Rules it keeps:** graphics over real footage are fine (no AI people in real footage, the 18 Oct rule). Nothing in
the bottom 350 px or the right 150 px (platform buttons). Our own colours and logo, never the BBC's typeface or red
blocks copied. One text overlay changing per beat, so captions and chyron mustn't stack (forms.md §2): **the chyron
carries the joke, burnt-in captions carry the voice, so the captions sit above the chyron or the chyron replaces them.**

**To build after a pick:** motion (the strip slides in once, the chyron wipes on with each story, the ticker crawls,
a two-frame glitch on BREAKING), as a transparent overlay rendered once per short over the footage.

Sources: https://en.wikipedia.org/wiki/The_Day_Today · https://en.wikipedia.org/wiki/Brass_Eye ·
https://www.cjr.org/behind_the_news/allknowing_news_network_debuts.php ·
https://www.kunc.org/2011-01-21/onion-news-network-a-highly-successful-debut-for-the-fakest-of-fake-news ·
https://keepthescore.com/blog/posts/lower-thirds/ · https://www.newscaststudio.com/graphics/bbc-news/
