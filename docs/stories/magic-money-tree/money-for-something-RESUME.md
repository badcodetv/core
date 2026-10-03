# RESUME HERE — Money For Something (the game-show telling of Magic Money Tree)

**Last worked 3 October 2026 (evening), by Jack.** Everything is in
[`money-for-something.md`](./money-for-something.md); this page says where it stands and what is next.
**Kai has not seen any of it, and it is not ruled as the film.** It sits beside the 1 October
direction ([`direction-2026-10-01.md`](./direction-2026-10-01.md)), not over it.

## Where it stands

| Piece | State | Where |
| --- | --- | --- |
| The idea | A rigged quiz show from the future, with a First World War panel | "The idea in one breath" |
| The look | ✅ Jack picked the comedy-club roundtable, with a clear stage and no audience | Rounds 7 to 9 |
| The room reference | ✅ Round 9's 9c: [`characters/roundtable-clear-stage-reference.jpg`](./characters/roundtable-clear-stage-reference.jpg), in Flow as `mfsclearstageref.jpg` | "The room reference and the voice plan" |
| The cast | ✅ Four Flow Characters, each with a Portrait, a Body and a custom Voice | "The cast and their voices in Flow", "Character sheets, second pass" |
| The voices | ✅ Jack: "I like the voices" | Same |
| Who speaks where | ✅ Jack ruled "split the roles": the narrator (Google AI Studio) over real clips, the host and guests on camera only (Flow) | Same |
| The storyboard | 🟡 v2 written: ten scenes, about three minutes, the tree as the game. Not marked up by Jack | "Storyboard v2" |
| The narrator's voice | ✅ Jack picked Zubenelgenubi with the British (Brixton) accent setting, AI Studio, nothing else in the boxes | "The narrator's voice" |
| The room reference v2 | 🟡 One candidate with the four updated Characters, in Flow only. Jack has not ruled | "Room reference v2" |
| The narrator's lines | 🟡 Draft 2 with Jack's edits; all eleven lines rendered and in the narrator folder. Jack accepted scene 5 take 3; the rest are not ruled | "The narrator's lines", "First takes" |
| The narrator's facts | 🟡 Checked: scene 10 holds; scene 8 and scene 6 each have one loose phrase | "The fact check" |
| The Premiere project | 🟡 Open, no sequence yet. Three bins: `narrator` (13 line takes), `s07-quick-fire` (12 stills), `s08-plant` (3 films) | "Premiere and the real footage" below |
| The real footage | 🟡 Scenes 7 and 8 part pulled; scenes 4 and 5 found, not yet on disk; scene 6 not found; scenes 1, 9, 10 stills queued | Same |
| Script for the room, video clips | ⬜ Not started | |

**Flow:** project `cb27208c-4b16-426d-9144-c394f2735c15` ("mmt jack"), Jack's account.
Stills on Nano Banana 2, 4:3 for the room, 3:4 for character sheets.

| Character | Flow id | Voice (preset) |
| --- | --- | --- |
| The Host | `65e090db-11a1-4dce-bc6c-c182f4213f4a` | The Host voice (Sadachbia) |
| The British Soldier | `5895147c-5392-4ac0-ace9-34742b8ec24e` | The British Soldier voice (Algenib) |
| The German Soldier | `5e09ee82-7f79-4c2e-9aee-b5ebcca1d2d0` | The German Soldier voice (Alnilam) |
| The Politician | `6baccdfb-7353-4559-829d-8fe253eb7b1f` | The Politician voice (Umbriel) |

## Premiere and the real footage (3 October, evening)

**Project:** `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\money for something\money for something.prproj`
(the Desktop is under OneDrive on Jack's machine). No sequence exists. Saved after the imports.

**Where the media lives:** `...\money for something\clips\<scene>\`. Films are
`<id>.picture-only.mov`: ProRes 422 LT, no audio, md5 checked against archive.org. LT, not the HQ
the 29 September pass used, because this folder syncs to OneDrive. `clips\_masters\` holds the
originals with their soundtracks: **never import those** (the picture is free, the sound is not).

**The rebuild kit:** [`research/footage-pass-2026-10-03-mfs/scripts/`](./research/footage-pass-2026-10-03-mfs/scripts/).
Both scripts skip what is already done, so re-running them is the way to resume.

- `bash pull.sh` reads `videos.list`, downloads, checks md5, conforms. Status in `pull-status.tsv`.
- `python3 stills.py` fetches the Commons stills already cleared in [`footage.md`](./footage.md);
  `python3 stills.py ww1.json` fetches the First World War set. Status in `stills-status.tsv` and
  `ww1.json.status.tsv`, written only when a run finishes.

| Scene | What | State at the time of writing |
| --- | --- | --- |
| 7 Quick-fire | 12 Germany 1923 stills (bank, Essen, banknotes, the bread van) | ✅ On disk and in Premiere |
| 7 Quick-fire | 2 London unemployed stills (1931); `what_a_life_TNA` (a street queue, but 1949); `gov.fdr.25.2` (Dunkirk, for the next war) | 🟡 Queued |
| 8 Plant | `new_town_TNA`, `your_very_good_health_TNA`, `pop_goes_the_weasel_TNA` | ✅ On disk and in Premiere |
| 8 Plant | `DiaryForTimothy` (ward, nurse, bricklayer); 6 post-war housing stills | 🟡 Film was conforming; stills queued |
| 4 How did it start | `111-m-59-r3`, *The Battle of the Somme*, reel 3, 1920x1080, 674 s | 🟡 Queued. See the licence note |
| 4 How did it start | Kitchener poster, three recruiting posters, three trench photographs | 🟡 Listed in `ww1.json`, not fetched |
| 5 Can we afford it | Two war loan posters, three Chilwell shell-factory photographs | 🟡 Listed in `ww1.json`, not fetched |
| 5 Can we afford it | Ships | ⬜ Not found yet |
| 6 What happened next | Men coming home, the homes promise on a poster, a 1920s dole queue | ⬜ Not found. One Commons search round returned nothing usable; a second was rate-limited |
| 1, 9, 10 | Commons stills: Theresa May 2017, Northern Rock queue, Lehman, Bank of England, Osborne, the 2020 press conference | 🟡 Queued. The moving BBC and news clips are still not ruled |

**Two things that went wrong, so nobody repeats them.**

- **Wikimedia rate-limits hard** (`HTTP 429` on `upload.wikimedia.org`). Running a search loop
  while the downloader ran is what tripped it. One Commons job at a time, and expect retries.
- **`pkill -f stills.py` kills the shell that launched it**, because the pattern matches the
  launching command line too. It took the film queue down with it.

**Licence notes, not ruled.**

- `111-m-59-r3` is the British 1916 film in a US National Archives copy (FedFlix, uploader
  `skip@avgeeks.com`, no `licenseurl`). Custody is not authorship, so it does not rest on US federal
  status. My reasoning: a 1916 film is free on age and on the pre-1957 Crown chain in `footage.md`
  11d. **Kai has not ruled on a First World War film.**
- The First World War posters and photographs are tagged "Public domain" on Commons. Read from the
  search result only; the per-file receipts land in `docs/footage/` when they are fetched.
- Real, identifiable people in scenes 1, 9 and 10 (May, Osborne) are Kai's call whatever the licence.

**Next on this, in order:** check `pull-status.tsv` and the two stills status files; re-run both
scripts if anything is missing; import the rest into bins named for their scene; find scene 6 and
the ships; then write the footage rows into `footage.md`.

## Waiting on Jack

1. **Mark up storyboard v2:** which scenes, lines and gags stay.
2. **Two costume calls made without a ruling:** the Politician is now a 1916 minister (the
   clergyman's collar is gone), and the British Soldier is now a private (he was dressed as an
   officer).
3. **Scene 9 (Sound Off):** the host dubs the clips on camera and his sound carries over the cut.
4. **The new room picture:** is room reference v2 the reference now? It is the newest 4:3 still in
   the Flow project.
5. **Two narrator lines the fact check loosened:** scene 8 "owed more than it ever had" (the peak
   was 1946/47) and scene 6 "a committee of businessmen" (the Cabinet capped the houses first, in
   July 1921). Keep them, or change the words and re-render.
6. **Jack's seed line** ("...the next my arm flew off. Morphine is hard to kick") is out of v2
   because the soldier has both arms.

## Next moves, in order

1. **Room reference v2 is made and waits on Jack.** If he takes it, save it to `characters/`,
   upload it to Flow under a new name and use it from then on. Every still from rounds 8 and 9
   shows the old collar and the officer's tunic.
2. **The first talking test clip (start here):** the host, one short line, Omni Flash, his Character and Voice
   attached. Then two more with the same voice, to hear whether it holds from clip to clip. Nobody
   has tested that, here or in anything found online.
3. **The missing stills**, scene by scene: the table is under "What already exists, and what has to
   be made" in storyboard v2.
4. **The narrator:** voice picked, lines written, all eleven rendered, facts checked. Left: Jack's
   ear on the other ten takes, and his call on the two loose lines. Takes are in Jack's narrator
   folder (`Desktop\Youtube Vids\animation\money for something\narrator`), named `line-s01-…` to
   `line-s10-…`. Videos go to `...\videos`. To render more: `scripts/ai-studio/.tmp/render.mjs`.

## Not checked

- How many houses were built in 1948 (scene 8), and the 1948 debt in pounds.
- Whether BBC and news clips can be used (scenes 1, 9 and 10).
- Whether a Flow voice name sounds the same as its AI Studio namesake.
- The updated Characters in a video clip. (In a still: done once, all four held.)

## How Flow was driven

By hand over the browser, because the Flow tools for Characters are not rebuilt. The steps and the
traps are in [`docs/flow/automation-2026-09-rebuild.md`](../../flow/automation-2026-09-rebuild.md),
items 25 to 48; the scratch scripts are in `scripts/flow/.tmp/`. **The one to remember:** the
Character page's top-bar Delete removes the whole Character (item 44).
