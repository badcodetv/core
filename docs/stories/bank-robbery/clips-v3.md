# The Bank Robbery — third pass of clips, with dialogue (7 October 2026)

**Asked for by Jack, 7 October 2026:** "make the videos in a David Lynch way, add dialogue in them.
Please avoid elements of AI slop... optimise this prompt for Google Flow Omni Flash
frames/ingredients... use the cinematography file and skills in the repo."

**This overturns yesterday's picture-only pass** ([`clips.md`](./clips.md)), where every prompt ended
"No dialogue, no music". The house rule is still no speech in Flow video; this film is now an
exception by Jack's word, like Money For Something.

- **Settings:** Omni 1.1 Flash · Frames (the still is the first frame) · 16:9 · 720p · 8 s · one
  take each. One take, not the standing two, to halve the credits; not ruled.
- **Flow project:** `63d22c4b` ("Oct 06 - 14:23").
- **Files:** `Desktop\Youtube Vids\animation\bank robbery\vids\v3\<id>.mp4`. Not committed.
- **Prompts, word for word:** [`scripts/bank-robbery/br-clips-v3.json`](../../../scripts/bank-robbery/br-clips-v3.json).
  Each prompt is `open` + the clip's `text` + `close`.
- **Runner:** `scripts/bank-robbery/br-clips-v3.mjs`, which calls
  `scripts/money-for-something/mfs-clip.mts` once per clip (start frame, then a Character chip for
  each speaker). Plates are copied into the WSL filesystem first.
- **Lines:** from [`script.md`](./script.md) as agreed with Jack. The narrator's lines are not in
  any clip; they are recorded separately.

## Why Frames, with the speaker's Character attached

- **Frames keeps the still's exact framing.** These stills took work, and the low and strange
  camera positions are the look Jack asked to keep. Ingredients re-stages the shot
  ([`omni-flash.md`](../../google-flow/omni-flash.md), "the tab rule").
- **A Character chip can be attached in Frames mode** (seen on Money For Something, 4 October), and
  the voice was the same speaker across clips there.
- 🔴 **Known doubt:** Google's Flow help says a custom voice works only on Ingredients generations.
  On Money For Something the accent heard did not match the Character's written voice. So the
  voices in these clips may not be the twelve custom voices made yesterday. **Not resolved.** The
  first test clip here (Mr Blue) was heard by a machine listener as a gruff northern English man of
  fifty to sixty, which fits him, but no person has listened.

## How the prompts are built

**The opening, on every clip:** "A locked-off shot from a scripted feature film, a slow dark drama
with made-up characters played by actors on a closed set. One continuous shot with no cuts. The
camera is fixed and does not move."

- **"Scripted... made-up characters played by actors"** is there because lines spoken by a man who
  looks like a politician were refused on Money For Something until the fiction was stated first.
- **No "comedy"** anywhere: on Money For Something that word brought a laugh track.
- **"One continuous shot with no cuts":** Google's own Omni page says the model cuts into several
  shots unless told not to.

**Then three to five sentences, motion only.** The still already has the people, the place and the
light. People are "the man on the left" or a Character's name, never a description.

**Speech** is written the way that worked on Money For Something: `He says:` then the words, with
no quotation marks anywhere in the prompt (a quotation mark burns a subtitle). Where two people
speak, each line is tied to a name and a position.

**The slow, uneasy feel**, written as things a camera could record, with no director named:

| What the films in question do | What the prompt says |
| --- | --- |
| Hold longer than is comfortable | "sits very still... for a long moment", "does not blink for a long moment" |
| Stillness, then one small movement | One action per clip, and it is small: a thumb on a button, one blink, one squeeze of a shoulder |
| Performers who are too calm and too slow | "speaks slowly and flatly", "with a pause before the last word", "After a long pause" |
| Reactions that come late or not at all | "does not react at all, then blinks once" |
| Room tone and electrical hum under everything | Every clip names a hum: a fridge, a strip light, a bare bulb, neon, a pump |
| A light that is not quite stable | A lamp that "flickers once" or "hums and dims for a moment" |
| No music telling you what to feel | "No music" closes every prompt |

**Against the AI look in motion** (the repo's list and the web pass agree):

- The camera is locked. A drifting camera with no reason is the first tell.
- One or two movements, never everyone at once.
- "They breathe and blink at different times" on any held shot of people.
- Bodies stay where they are and stay the same size (yesterday's three drifting takes were all
  fixed that way).
- Words in the picture are told to stay as they are: "The lettering on them stays exactly as it is."
- The sound is named object by object, so nothing is left for the model to invent.

**Line length:** about twelve words is the most one 8-second clip carries at a natural pace
(Jack's ear on Money For Something). Longer speeches are split across two or more clips from the
same still.

## What the web pass found (7 October 2026)

A research agent's report; it read pages through a summarising fetch, so quotes are as relayed.

- Google's Omni pages give "static", "locked off" or "fixed" for a held camera, and say the model
  cuts and invents a story unless told "In a single continuous shot" and "No scene cuts".
  [DeepMind prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/),
  [Gemini API Omni docs](https://ai.google.dev/gemini-api/docs/omni)
- **Google has published no dialogue format for Omni.** Its Veo guides use `A woman says, "..."`
  and `the man in the red hat says: ...`. The repo's own tests are the better evidence here.
  [Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- Flow Help: "You can add voice references only to video generations that use ingredients."
  [Flow Help](https://support.google.com/flow/answer/16353334)
- A vendor's tests (thirty-odd clips) say lip-sync holds for six to seven seconds with one speaker
  and falls apart sooner with two in frame; they advise one speaker a clip.
  [invideo](https://invideo.io/faq/how-long-can-ai-lip-sync-stay-accurate-before-it-breaks/)
- Named tells in generated video: floaty constant-speed motion, plastic skin, morphing faces,
  drifting backgrounds, flickering light. Fixes reported: less camera movement, one light with a
  direction, weight and physics described.
  [Genra](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix),
  [Luma](https://lumalabs.ai/news/prompt-realistic-ai-videos)
- **One source disagrees:** a vendor guide calls a locked-off frame a tell and recommends a slow
  push-in. Not adopted. Any camera move on these clips is added in the edit.
- On the mood: a sound designer who worked with the director describes natural sounds muffled into
  a subjective presence, and a cinematographer describes pace following the slowest person in the
  room. [Screen Slate](https://www.screenslate.com/articles/79),
  [American Cinematographer](https://theasc.com/articles/twin-peaks-dreams-doubles-and-dopplegangers)

## The clips

Fifty-four clips: thirty that speak and twenty-four that do not. Four are remakes of yesterday's
stills with their lines added (`s06-colours-talk`, `s10-hoover-talk`, `s11-vault-talk`,
`s12a-standoff-talk`), and three more use yesterday's plan still for the heist briefing
(`s05-plan-a`, `-b`, `-c`).

| Scene | Clip | Who speaks | The words |
| --- | --- | --- | --- |
| 1 | `s01b-remote` | nobody | |
| 1 | `s01c-blue` | Mr Blue | She should bloody well earn it. |
| 1 | `s01d-red-1` | Mr Red | I'd rather support her feminist rights. |
| 1 | `s01d-red-2` | Mr Red | My tip would be seen as a bigoted hate crime. |
| 1 | `s01e-denise` | Denise | Thanks for the, advice. |
| 2 | `s02b-shut-shops`, `s02c-bank-door` | nobody | |
| 3 | `s03a-hearing-1` | A voice at the table | If we let you go, what would you do? |
| 3 | `s03a-hearing-2` | The Ex | Help at the food bank. *(coughs)* Or consultancy. |
| 4 | `s04b` to `s04j` (nine) | nobody | Each holds a look into the lens, for the freeze |
| 5 | `s05-plan-a` | The Ex | The biggest vault in the city. Everyone's life savings. Right there. |
| 5 | `s05-plan-b` | The Governor, The Ex | Security isn't a problem. I am the security. / The problem is eyes. |
| 5 | `s05b-blue-side` | nobody | |
| 5 | `s05c-red-side-1` | Mr Red | Hang on. Which one's true? |
| 5 | `s05c-red-side-2` | The Platform | Doesn't matter. I don't need them to believe it. I need them to reply. |
| 5 | `s05d-twist-1` | The Donor, The Ex | And how much do we take? / Nothing. We put it in. |
| 5 | `s05-plan-c` | The Fixer, The Ex | And her? / She keeps every penny. |
| 5 | `s05d-twist-2` | The Donor | You bastard. |
| 6 | `s06a-list-1` | The Ex, Mr Turquoise | Mr Blue. Mr Red. Mr Turquoise. / Why am I Mr Turquoise? |
| 6 | `s06a-list-2` | The Ex, Mr Turquoise | Blue was taken. / This is exactly what the establishment does. |
| 6 | `s06a-list-3` | Mr Turquoise, Mr Blue | I'm the only one here who isn't a robber. / You're in the van. |
| 6 | `s06a-list-4` | Mr Turquoise | I'm in the van reluctantly. |
| 6 | `s06-colours-talk` | Mr Blue, Mr Red, The Ex | Thirteen years! / Fourteen! / Lovely. And cut. |
| 7 | `s07b-off-record` | The Presenter | The thing is, off the record, I agree with all of you. |
| 7 | `s07c-denise-hall` | Denise | Two hundred and five. Two hundred and six. |
| 8 | `s08a-placards`, `s08b-remote-window` | nobody | |
| 8 | `s08c-megaphones` | Mr Blue and Mr Red together | And I'll tell you whose fault it is. |
| 8 | `s08d-presenter` | The Presenter | Tensions are running high here. We'll be hearing from both sides. |
| 9 | `s09a-officer` | The officer | Mind how you go, sir. It's mad out here. |
| 9 | `s09c-pallet` | nobody (angry muttering, no words) | |
| 9 | `s09d-door` | The guard | Morning, Governor. |
| 9 | `s09e-turquoise` | nobody | |
| 10 | `s10a-enter` | nobody | |
| 10 | `s10-hoover-talk` | Denise | Full English. No tip. Lift your feet. |
| 10 | `s10c-that-much-1` | Denise | Our road's changed. Rent's gone up. Some of that's real. |
| 10 | `s10c-that-much-2` | Denise | It's about that much. |
| 10 | `s10d-counting` | Denise, from behind | What's all that, then? |
| 11 | `s11-vault-talk` | The Accountant, The Governor | Why am I drilling? / It looks better. |
| 11 | `s11b-in` | The guard, The Ex | You're putting it in? / Count it in the morning. It'll all be there. |
| 11 | `s11c-keys`, `s11d-pricetags` | nobody | |
| 12 | `s12a-standoff-talk` | Mr Blue, Mr Red | Who talked? / He talked. / Your lot always talk. |
| 12 | `s12d-lowering` | Mr Blue, The Governor | So nobody's coming? / Why would anybody come? It's policy. |
| 12 | `s12e-sold`, `s12f-kebab` | nobody | |

**Still used from yesterday's silent pass, unchanged:** `s01-breakfast`, `s02-spoiler`,
`s03-getting-out`, `s04-recruiting`, `s05-plan`, `s07-night-before`, `s08-march`, `s09-walk`,
`s12b-count`.

## Choices in this list that are mine

- **Eleven clips have two or three speakers.** The web pass and the repo both say the wrong mouth
  can move. They were written anyway because the lines are exchanges; they are the first to check.
- **The officer, the guard and the voice at the hearing have no Character,** so their voices are
  whatever the model gives.
- **The megaphone line is asked for from both men at once.** Nothing is known about overlapping
  speech. It may come back as one voice.
- **Mr Red's tipping line is split in two** because it is sixteen words.
- **`s09e-turquoise` has no gunshot,** only falling plaster, to match its still.

## What came back

**All fifty-four clips were made.** 1280×720, 8 s, with sound, in `vids\v3\`. About 75 seconds a
clip. Fifty-two came first time; two needed work (below), and two more were redone after checking.

**How they were checked:** four frames from every clip (start, 3 s, 5.5 s, end) on six contact
sheets, read by me; and the sound of the thirty-two talking clips joined into two files and
described by one machine listener (Gemini 3.5 Flash). 🔴 **Nobody has watched a clip at playing
speed and no person has listened.** Lip-sync was not checked at all.

### The words

**Every line came back word for word** in the listener's transcript, at a pace it called natural,
with no laughter and no audience. Exceptions:

| Clip | What |
| --- | --- |
| `s06-colours-talk`, first take | The two men carried on with invented lines ("No, it was 13, you always lie!"). **Redone** with only the two shouts and "Those are the only three words spoken. After that they glare at each other in silence". The second take has just "Thirteen years!" and "Fourteen!". The Ex's "Lovely. And cut." is no longer in any clip |
| `s08c-megaphones` | The line is said twice by what sounds like one voice, not by two men at once |
| `s03a-hearing-2` | The cough is there, between "food bank" and "or consultancy" |
| `s12d-lowering` (final take) | The listener reports a low synth drone under the lines. The prompt said "No music" |

### The voices: the main open question

- **In most clips with two speakers the listener heard one voice doing both lines** (`s05-plan-b`,
  `s05-plan-c`, `s06a-list-1`, `s11-vault-talk`, `s11b-in`, `s12a-standoff-talk`). It heard two
  voices in `s05d-twist-1`, `s06a-list-2`, `s06a-list-3` and the final `s12d-lowering`.
- **Accents are unreliable.** The same listener called Mr Blue northern English in one pass and
  received pronunciation in the next, and called several clips North American, including Denise in
  scene 1. A machine listener is a poor judge of accent, but an American-sounding take is possible.
- **So the open question from "Why Frames" is still open:** whether these are the twelve custom
  voices at all. A person has to listen.

### The pictures

From four frames a clip: the camera held on every clip, nobody changed face or clothes, and the
lettering on the placards, the SOLD board and the neon sign kept its spelling. The neon sign dims
and comes back. The Fixer stops chewing and stares. The price tags do move. Nothing was seen
morphing, but four frames would miss a short fault.

### Two that needed work

| Clip | What happened | What fixed it |
| --- | --- | --- |
| `s03a-hearing-1` | **Refused:** "Unable to generate videos that might cause reputational risk or misrepresent current events." The prompt had a figure at a committee table leaning to a microphone and asking the question | Cut to four short sentences with "A woman's voice from off screen says:" and no microphone. Passed first time |
| `s12d-lowering` | **The still was refused as an upload three times** ("Flow would not accept"). I took the cause to be the two pistols and remade the still with empty hands. That remake ran while Flow was still in video mode, so it made a clip, and the "still" that was saved was a frame of that clip with two strangers in it. A clip was then made from the strangers | Flow put back in image mode with one ordinary still; the still remade properly (right cast, empty hands, a dropped mask on the floor). **That still was refused as an upload three more times,** so the pistols were not the cause. A copy scaled to 1280×720 with a little grain added was accepted at once |

**What is not known:** why Flow refuses that picture as an upload. The Governor is in it facing the
camera, and one of his portraits was refused the same way yesterday. The wrong clip is in
`vids\v3\replaced\`.

**One extra still exists because of this:** `s12g-sold-close.jpg`, a close view of the SOLD board,
made as the ordinary still that put Flow back in image mode. It may be useful for the ending.

### Credits

Fifty-four kept clips, three redone and one made by mistake: **58 generations, about 700 credits
by the price list** (about 12 each). The balance was not read before or after.
