# YouTube words: The bank robbery, the story film (draft, 2026-11-13)

**Status:** drafted by marketing-producer; gatekeeper REVISE (2026-11-13), all six fixes applied below; option B struck.
Applied to the private video 2026-11-13 on Kai's word ("fill in all of the description").
**Video:** https://youtu.be/TMIMX1V3iGg · title **"The bank robbery"** (fixed, not touched here) · private · AI label on
(log.jsonl) · Premiere `bank robbery short - cut 7g`, 2:28, 16:9, so **a long-form film, not a Short**.
**Canon:** `docs/stories/bank-robbery/` (`short.md` for the script, `short-shots.md` for cut 7 to 7g, `story.md` for the
twist and the may-say list). No new research (chief-of-staff plan §9 rule 1).

**What is said in this cut, in order** (from `scripts/bank-robbery/brs-narration*.json`), so the description can use the
same words (shorts-growth.md §3, "Search words"):

| Line | Words | Setup or spoiler? |
| --- | --- | --- |
| na1-grandparents | Your grandparents fought the Nazis for this country. | setup |
| ns03-one-bed | Their grandkids can't get a one-bed. | setup |
| ns11-both-right | Both of them are right. Neither of them is looking at the bank. | setup |
| ns12-masks | This lot don't wear masks. Nobody's ever looked at them. | setup |
| nr6-print-pay | Most people rob a bank to get money out. This lot print the money... then pay it in. | 🔴 **the twist** |
| np1-shout | Then give both sides something to shout about. | after the twist |
| ns19-first-line | They agree on the first line; only the blame was bought and paid for. | after the twist |
| ns1-side-door | Everyone's watching the front door. Nobody's watching the side one. | after the twist |
| ns23-just-early | The new money gets to him first. He buys before the prices catch up. He's not a thief. He's just early. | 🔴 the ending |
| ns26-no-law | Take a pound off someone and they call the police. Make every pound they've got worth less, and there's no law for that one, mate. | 🔴 the ending |

Plus the café voices from cut 7 (`build-short7.py`, `short.md` cut 2 table): Barry's "Nine hundred quid. For a box room.",
Denise's "Mine's gone up again. The café *and* the flat." / "It's the landlord. Put mine up twice this year. And the
council's put my rates up for the privilege.", the 10p Freddo ("Least something's still cheap."), The Ex's distraction
line and Mr Red's toast. **The description uses only the four setup lines and the café, and stops at about 0:55.**

## Before any of this goes on

- 🔴 **The music credit is owed** (CC BY 4.0, `short-shots.md` cut 7d, "🔴 Credit owed before upload"): Darkfluxx,
  "Reloaded", under the vault. It is in the credits block below. Don't trim it out.
- 🟡 **The credits block is built from `build-short7.py` and the cut 7d notes**, not from a `final.json` (none exists for
  this cut). Cuts 7e to 7g were Premiere edits on top. Kai or Jack: confirm nothing third-party was added after 7d, and
  that the Beth's Cafe real-plate test (`short-shots.md`, CC BY 3.0, real identifiable people) is **not** in 7g. I found
  no Beth's file in `build-short7.py`. If it is in, it needs its own credit line and the real-people question answered
  first.
- 🟡 **The site page `/stories/4` is the film's page** (`apps/site/build.mjs`, films are `/stories/1`–`4` in
  `content.json` order), but its blurb still describes the long film ("Eleven politicians and pundits in black suits…")
  and `film` is `null`, so it says "Coming to YouTube". Before this goes public: set `film` to `TMIMX1V3iGg`, and
  consider swapping the blurb for opening A's two lines so site and video say the same thing.
- 🔴 **Before going public: Mr Red's face** (`short-shots.md` cut 7g: Flow read his close-up as a "prominent person").
  Someone checks no frame reads as a real politician. The thumbnail never shows Mr Red's face.
- ✅ **Beth's Cafe is not in 7g** (checked against the Premiere sequence 2026-11-13: the café wide is the generated
  `c01b-cafe-wide`). The ECB and archive clips are in it, and credited.
- 🟡 **Cross-links** (`youtu.be/XinO1Kze_5A`) only click through once the music video is public or unlisted.
- ⬜ **No mailing list yet** (plan §3 item 2), so no signup line. Add it the day "Transmissions" exists.

---

## Opening (the two lines that show before "more")

- **A (PICK):** Your grandparents fought the Nazis for this country. Their grandkids can't get a one-bed. Nobody's looking at the bank.
  A British heist comedy about rent, a greasy spoon and the bank across the road.
  *Gatekeeper: a target inside the first 120 characters, so a cut-off preview can't read as a nativist post (the-reader.md rules 6, 10).*
  *Why: the narrator's own first two lines, word for word, then the search words ("heist comedy", "rent", "bank"); it
  starts on the reader's wound in the reader's own story about the country, not their wage maths (the-reader.md rule 3),
  and it's the line someone repeats in the pub (rule 8).*
- ~~**B:**~~ struck by the gatekeeper (FAIL): it put the boats claim first on the page with no film to answer it.
- **C:** A bank robbery in two and a half minutes. One café, one bank across the road, and a crew that never needed
  masks.
  *Plainest for search ("bank robbery"), least voice.*

## Body (shaped as a heist film's crew sheet, unlike the music video's prose; rule 12)

```
THE REGULARS

Barry. Hi-vis, full English, nine hundred quid for a box room.
Denise. Owns the café. The landlord's put her rent up twice this year, and the council's put her rates up for the privilege.

ACROSS THE ROAD

A back room, a bottle, and people who run things. A man just "out" of a very big job. One politician from each side, who get on fine when nobody's filming. No masks. Nobody's ever looked at them.

THE JOB

Barry and Denise have the same problem and a different culprit each. Both of them are right. Neither of them is looking at the bank.

Somebody planned this, and it wasn't Barry or Denise. I've seen how this job ends. They haven't, yet.

Two and a half minutes. Watch the bank.
```

## AI line, links, credits, hashtags

```
Made by machines trained on work nobody was paid for. So was the future I come from.
The full account: https://www.badcode.tv/how-we-made-it

The story: https://www.badcode.tv/stories/4?src=yt
Next: The bank robbery (music video) https://youtu.be/XinO1Kze_5A

Credits
Music under the vault: "Reloaded" by Darkfluxx (freemusicarchive.org/music/darkfluxx), licensed under CC BY 4.0 (creativecommons.org/licenses/by/4.0/)
Score: HoliznaCC0 (CC0)
Printing press footage: "New 20 Euro Banknotes Printing Production", European Central Bank, CC BY 3.0 (creativecommons.org/licenses/by/3.0/), via Wikimedia Commons, modified
Wartime archive: Battle of North Africa, Part 1 (The Big Picture), U.S. Army; Divide and Conquer, U.S. War Department, FDR Presidential Library; War Pictorial News No. 91 (1943), U.S. National Archives. All via archive.org

#ShortFilm #CostOfLiving #HousingCrisis
```

**Hashtag options:** **PICK** `#ShortFilm #CostOfLiving #HousingCrisis` (*the format plus the reader's two words; differs
from the music video's `#QuantitativeEasing #MusicVideo`*) · alt `#BankRobbery #Rent #BritishComedy` (*more title, less
topic*) · alt `#ShortFilm #Rent` (*two is enough*).

## Tags (358 characters, counting the quotes YouTube adds round multi-word tags; limit 500)

`The bank robbery, bank robbery short film, heist short film, heist comedy, British short film, UK short film, comedy short film, short film, cost of living, rent, rent rise, can't afford rent, housing crisis, one bed flat, box room, landlord, greasy spoon, cafe, grandparents, WW2, political satire, satire, AI short film, BadCode, badcode tv`

*No "boats", "immigration" or "small boats" tag on purpose (the-reader.md rule 10: don't put the claim in front of
people who never watch the answer). No "quantitative easing" or "money printing": both point at the twist.*

## Pinned comment (optional)

- **A (PICK):** `What does a one-bed cost where you are? — Kai / Jack`
  *Why: a question any viewer can answer from their own life, so the first comments are about rent, not about AI or
  each other (plan §7 "answer the first comments"; the-reader.md rule 8). No claim, so no source owed (rule 11).*
- **B:** `Who's in your café arguing about rent, and who are they blaming? — Kai / Jack`
  *Invites the argument, but invites people to name culprits, which is where a comment section turns on itself.*
- **C:** None. *The film has no checkable statistic on screen to source (the £200bn slip is a story prop, `short.md`
  cut 2), so a pinned comment is optional.*

## Studio-only steps

1. **Altered or synthetic content: Yes.** Already set by us (log.jsonl); YouTube won't read it back, don't "fix" it.
2. **End screen → The bank robbery (music video)** (platform-playbooks.md §3, "end screens to the next core"). 🟡 The
   last 20 s are the ending beat (the café wide under the last line, Denise at the sink, the neon). Keep the end screen to
   the **last 5 s** (the neon and black) so it doesn't sit on Denise.
3. **Category:** keep **Film & Animation** (`categoryId 1`, as uploaded). The other four use 22; for this one 1 is right.
4. **Language:** en-GB title and audio, as uploaded. Leave it.
5. **Thumbnail** (youtube-channel skill step 8): a setup frame only, e.g. Barry and Denise under the painting, or the
   bank seen through the café window. **Never** Mr Red's face, the press, the vault, the keys, the estate agent's window or the sink.
6. **Playlist (suggestion):** "The bank robbery": this film, then the music video.
7. **Suggestion for the music video's description:** its "Next:" line points at The Rules; once this film is public,
   consider pointing it here instead, so the two point at each other. Not drafted as a change here.
8. **Pinned comment** is a Studio click (the API can't pin).

## The doc behind each choice

- **First two lines = narrator's lines + search words:** youtube-channel rule 1 (plan.md §3.10 evergreen search;
  platform-playbooks.md §3 Provisional, "long-form: title/describe for search"); rule 2, same words as spoken
  (shorts-growth.md §3): "grandparents", "one-bed", "box room", "landlord", "masks", "bank" are all said on screen.
- **Setup only, stops at 0:55:** Kai's ruling 2026-10-22 (apps/site/README.md); story.md "The twist: nothing is taken".
  Nothing about printing, paying in, the side door, the vault, the keys, "just early", the Freddo going to 20p, "no law",
  or the sink. "I've seen how this job ends. They haven't, yet." promises an ending without giving one.
- **The protest is left out** even though The Ex sets it up before the twist: it is the first thing after "This lot",
  and "the protest is their plan" (Jack, 2026-10-21) is half the reveal.
- **Crew sheet shape:** youtube-channel rule 12 (vary the shape; the music video's description is a hook and prose);
  the story borrows Ocean's Eleven's recruiting roll call (bank-robbery/README.md).
- **Barry and Denise are the heroes, both right:** the-reader.md rule 1 (hero, not pupil); voice.md "don't punch down";
  short.md "Rules the opening keeps" (Barry's worry is his own and not mocked).
- **"Somebody planned this, and it wasn't Barry or Denise":** the-reader.md rule 5 (name the chooser); rule 6 relaxed
  2026-10-23, so the beneficiary stays implied (the landlord is named, the planners are seen; who gains is the film's job).
- **"One politician from each side, who get on fine":** story canon (left and right mocked equally, the toast);
  the-reader.md rule 2 (the trick is shown run on Barry and Denise, never on the viewer). Types, no real names
  (story.md open call 2). 🟡 Note for the gatekeeper: Flow read Mr Red's close-up as a "prominent person"
  (`short-shots.md` cut 7g); the description names nobody and he is seen only in wides in this cut.
- **"Former Chancellor":** The Ex's canon (characters/the-crew.md, "A former Chancellor, just 'out'"). A type, no name.
- **No swear word in the opening or body:** the film has the chant; the preview lines sit next to the title (lane rule,
  first-four draft).
- **AI line and link:** using-ai.md §0 (one line, in voice, linked to the account); same wording and URL as the other
  four on the channel (`channel.json`).
- **Credits:** CC BY music and footage must be attributed (`short-shots.md` cut 7d; `footage-print.md`); archive and CC0
  credits are courtesy (`footage-ww2-action.md` "Credit strings"); footage-sources.md "credits fine".
- **Next watch = the music video:** youtube-channel rule 5 (on a long film: website with `?src=yt`, the next video, end
  screens; shorts-growth.md §4); plan.md §6 (second audience reached through the music).
- **Tags in the viewer's words, as insurance:** youtube-channel rule 4; the-reader.md portrait ("rent", "can't afford").
- **Hashtags, three at most:** youtube-channel rule 3 (shorts-growth.md §2–3).
- **Pinned comment as a question:** plan §7; the-reader.md rule 8.
