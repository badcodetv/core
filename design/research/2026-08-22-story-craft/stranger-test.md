# Stranger test — does the story-craft toolkit route a cold agent to the right page?

**Run:** 2026-08-23, 16:22–16:29 BST · **Subject:** GitPush Origin Master · **Method:** two
fresh `general-purpose` agents, spawned in parallel, given **no** knowledge that
`docs/story-craft/` exists, that a review had already happened, or that they were being
observed for navigation. Both read-only; neither wrote to disk. Each logged every file open
in order, with the reason and how it found it.

This file is a **report on the toolkit's navigability**, not a review of GPOM. Every
navigation fix below is **proposed only — nothing has been applied.** The strangers' craft
findings are summarised here only where they bear on whether the toolkit works; the two 🔴
craft findings they surfaced are listed in §7 for Kai to route, and neither has been added to
`critique-pass-3.md`.

| | **Agent 1 — "the drafter"** | **Agent 2 — "the symptom"** |
| --- | --- | --- |
| Brief | "Kai wants GPOM to grip a **distrustful reader** harder. Find whatever guidance this repo has and use it." | "Someone says: *'the middle drags and the ending feels like it's telling me what to think.'* Diagnose it." |
| Trace length | 29 steps | 25 steps |
| Wall clock | ~6 min | ~7 min |
| Searches needed to find the toolkit | **0** | **0** |

---

## 1. The two traces, side by side

Aligned by phase, not by step number. `→` = followed a link; `?` = guessed a path; `#` = grep/glob; `ls` = directory listing.

| Phase | Drafter | Symptom |
| --- | --- | --- |
| **Entry** | 1. `CLAUDE.md` (preloaded as project instructions) | — same, preloaded |
| **Orient** | 2. `docs/story-craft/README.md` → CLAUDE.md repo-map row | 1. `docs/story-craft/README.md` → CLAUDE.md repo-map row |
| | 3. `gitpush-origin-master/README.md` → CLAUDE.md "Deeper context" | 2. `gitpush-origin-master/README.md` → CLAUDE.md "Deeper context" |
| | 4. `wc -l` survey of both folders # | 4. `wc -l` of the story folder # |
| **Route** | 5. **`symptoms.md`** → README's "start here" | 3. **`symptoms.md`** → README's file table |
| **Gates** | 6. `docs/marketing/the-reader.md` → symptoms + CLAUDE.md | 21–22. `the-reader.md` → principles §0 + CLAUDE.md |
| | 7. `principles.md` → symptoms/gates | 7. `principles.md` → symptoms |
| | 8. `checklist.md` → README + principles | 6. `checklist.md` → symptoms |
| **The story (canon)** | 9–11. `story.md` in three passes (1–260, 260–470, 470–795) | 4–5, 10–11. `story.md` in four passes (1–200, 200–420, 420–600, 600–795) |
| **Prior art** | 12. `critique-pass-3.md` → README ×2 | 8. `critique-pass-3.md` → README ×2 |
| **As-built hunt** | 13–14. `ls -R` of the story folder, then `scenes/ songs/ storyboard/` ls | 9–10. `ls -R`, then `scenes/ songs/ storyboard/` ls |
| | 15–16. `songs/narration.md` (§2 cut tables, §6 the bank) | 14–15. `songs/narration.md` (§2, real durations) |
| | 17. `prompts.md` §2c + §3c # | 12–13. `prompts.md` outline, then §2c lines 139–180 # |
| **Craft depth** | 18. `narrator.md` → README + cited in pass 3 | 16–17. `narrator.md` §1/§1b, then §3/§4/§5/§7 → symptoms rows |
| | 19. `forms.md` §2 # | 18. `forms.md` §2 # |
| | 20. `toolbox.md` # | 23. `toolbox.md` # (tool-name lookup only) |
| | 21. `docs/voice.md` → CLAUDE.md + narrator.md | — |
| **Story-specific** | 22. `scenes/s00-awakening.md` ls | — |
| | 23. `how-we-tell-it.md` # → README + pass 3 | 19–20. `how-we-tell-it.md` "The one rule" # |
| | 24. `scenes/s01-the-push.md` # (searching for a human) | — |
| | 25. `ep1.md` → README | — |
| | 27. `characters/the-carrier.md` → README | — |
| **Verification** | 26, 28, 29. stale-link checks; grep for "messenger"/"uncertainty"; existence checks on `design/research/…`, `storytelling.md`, `storyboard/img` | 24–25. dangling-reference checks; grep of the song file to verify F1's truncation **live rather than trusting the review**; `prompts.md` §4–§5 |

**Convergence.** Two agents, different briefs, no contact — and the first five moves are the
same five files in nearly the same order. Both then independently decided the canon was not
enough and went hunting for the as-built cut, landing on the same two files (`prompts.md` §2c,
`songs/narration.md`). Both treated `critique-pass-3.md` as a *stop list* rather than an answer
key, and neither re-filed F1/F2/F3 as new findings.

---

## 2. Time-to-toolkit

| | Drafter | Symptom |
| --- | --- | --- |
| First substantive craft guidance | **step 2** (`story-craft/README.md`) | **step 1** (`story-craft/README.md`) |
| Actionable *routing* in hand | **step 5** (`symptoms.md`) | **step 3** (`symptoms.md`) |
| Operative rules (gates + rows) | steps 6–8 | steps 6–7 |
| Hops from cold start | **4** | **3** |
| Guessing or searching required | none | none |

Both reached the gates before drafting a single note. The symptom agent's summary of the route
is the cleanest evidence the wiring works:

> The pointer chain was two links: `CLAUDE.md`'s `docs/story-craft/` row says **start here** →
> `story-craft/README.md`'s file table → `symptoms.md`. Substantive craft guidance was
> reachable at step 1 and in hand at step 3; everything after step 3 was evidence-gathering
> against rows the repo had already chosen for me.

---

## 3. Which pointers fired

| Pointer | Fired | Note |
| --- | --- | --- |
| `CLAUDE.md` repo-map row for `docs/story-craft/` | **2/2** | The bolded **"start here"** on `symptoms.md` is what both cite. Highest-value five words in the wiring. |
| `CLAUDE.md` "Deeper context" GPOM bullet | 2/2 | Both found the story folder without a search. |
| `story-craft/README.md` file table | 2/2 | Routed both to `symptoms.md` first. |
| **`symptoms.md`** | 2/2 | The symptom agent found **both complaints as near-verbatim rows** (24, 41, 48) and ran exactly the rows they name. This is the toolkit working as designed. |
| `checklist.md` rows | 2/2 | Cited by number, correctly, in both reports. |
| **`checklist.md` procedure step 1** — *"read what was actually made, not only the canon file"* | 2/2 | Both explicitly name this line as the reason they left `story.md` for `prompts.md` §2c and `narration.md`. Without it, both diagnoses would have been of a script nobody is shooting. |
| `principles.md` gates §0 + the 16 rulings | 2/2 | Both cited rulings by number. The drafter used **ruling 11** unprompted to *refuse* to attach a cadence number — the never-cite guard fired without `evidence.md` being opened. |
| `narrator.md` §1b + §5 failure table | 2/2 | **Both independently found the same 🔴** — see §7. |
| `the-reader.md` as gates | 2/2 | Both ran G1–G5 before craft notes. |
| `forms.md` §2 | 2/2 | The drafter says forms.md's *War of the Worlds* lesson **turned a proposal into a compliment** — he would have flagged GPOM's ten-second pre-Enter silence as dead air. A toolkit page prevented a wrong note. |
| `toolbox.md` | 2/2 | Both used it late, as a name lookup, not for routing. Working as intended. |
| `critique-pass-3.md` | 2/2 | Used as prior art. No duplicate filings. |

### Pointers that did **not** fire

| Pointer | Fired | Reading |
| --- | --- | --- |
| **The `story-craft` skill itself** | **0/2** | Both entered via `CLAUDE.md` → `docs/story-craft/` directly. The skill's Build/Review framing, its non-negotiable rules, and its **write-back step** never ran. The drafter's report ends with a hand-rolled "one write-back worth making" — he reinvented the step the skill would have given him. |
| **`briefs.md`** | **0/2** | Neither opened it, and **neither opened a single raw brief.** `symptoms.md`'s inline deep links made the index redundant for these two tasks. Not evidence it is broken — evidence it is *unexercised*, and that the distilled layer answered everything on its own. |
| **`evidence.md`** (the never-cite list) | **0/2** | Neither cited a banned number, so no harm — but the guard was never consulted. It fired by proxy through `principles.md` ruling 11. |
| **`case-studies.md`** | **0/2** | Neither reached for a comparable. |
| `docs/storytelling.md` | 0/2 | The drafter checked it exists (step 29) and did not open it. |

---

## 4. What they had to invent, because the repo had no answer

These are the honest holes. Each is a place a competent stranger composed an answer the toolkit
does not contain.

**Drafter**
1. **The trust layer itself.** Nothing in the toolkit treats *"the reader does not believe you"*
   as a craft layer with its own tests. He derived it by composing `the-reader.md` rule 10
   (the unlikely messenger) + `narrator.md` §1b rule 6 (the Ava trap) + inoculation. Verified:
   **61 rows in `symptoms.md`, zero about believability**; `checklist.md`'s only occurrence of
   "believe" is row 4.4, which tests *opposition contempt*, not messenger credibility.
2. **Where a flagship's first human face should land.** No attention or churn model anywhere —
   deliberately, per ruling 11. He argued from row 3.5 with no number attached, which is the
   behaviour the ruling wants, but he had to work out that it was permitted.
3. **Whether checklist rows are independent** — can a joke pass 7.2 and still fail 4.4? The
   checklist does not say.

**Symptom**
4. **The chooser/viewer collapse.** Principle 21 and row 4.9 both assume "the chooser" and
   "the viewer" are separable people. GPOM's thesis is abdication, which makes them the same
   person, so the protection cannot be applied as written. No repo file names this case.
5. **The film's real length.** No target runtime is written anywhere; `forms.md` says
   "narrated video (3–5 min)" and the three built cuts run 123.8s for 3 of 17. He extrapolated
   ~8–10 min and applied principle 8's long-form penalty **on an estimate**.
6. **Which artefact the complaint was about.** Only cuts 1–3 exist and they contain no middle
   and no ending, so he assumed the complaint was against the script — and flagged that if the
   stranger watched the 124s that exists, his diagnosis answers the wrong question.
7. **The praeteritio reading** of scene 20 (disclaiming instruction while performing it). The
   repo names the failure mode but not this rhetorical shape.
8. **Whether "with the confidence of the only witness" trips binding rule 5.** Rule 5 is written
   about scientific citation; he read it as citing its own authority, and flagged it as his
   reading rather than a breach.

**Note on 3 and 4:** both agents independently hit a version of *"the checklist does not say how
its rows interact."* The symptom agent's form is sharper — he argues that pass 3's F11 dismissal
was ruled against row **5.8** (the one-crack warmth budget, a satellite rule) and therefore does
**not** discharge row **4.10** (holding the comic register through the diagnosis), which was
never run. Verified on disk: 5.8 and 4.10 are distinct rows testing different things.

---

## 5. Where a file misled them, or made them work

All five verified on disk during this run.

| # | Problem | Verified |
| --- | --- | --- |
| 1 | **`gitpush-origin-master/README.md` never mentions `scenes/`, `prompts.md` or the 17-cut order.** Its act-maturity table stops at "Beats". Both agents had to `ls -R` to discover the real production artefact. The symptom agent: *"Someone following the backbone alone would review the wrong thing."* | `grep -n "scenes/\|prompts.md\|§2c" README.md` → **no matches** |
| 2 | `README.md:121` names `../../ideas/stories/` in the code span. That directory does not exist. | `ls docs/ideas/stories` → no such file. The href resolves to `../../ideas`, so the **link works and the label lies** |
| 3 | `ep1.md:40` links `../camping-v2/README.md` — deleted in the 2026-08-05 consolidation. | `ls docs/stories/camping-v2/README.md` → no such file |
| 4 | An empty phantom directory tree: `docs/stories/gitpush-origin-master/docs/stories/gitpush-origin-master/scenes/`. A relative-path slip during a scene write. | Exists, contains no files, **untracked** (git cannot track empty dirs) — a local artefact only |
| 5 | `prompts.md` §5's own headline reads **"RULING OVERTURNED"**, which reads as stale on arrival even though the pointer to it resolves. | §5 exists at line 1086 |
| 6 | `s01-the-push.md` says the commit-log register is *unbuilt/pending*; `prompts.md` §2c says *parked*. | Known — already flagged by critique-pass-3's F2 strengthener, still unresolved |

No toolkit file gave either agent a *wrong* instruction. Every mislead above is in the **story
canon's own indexes**, not in `docs/story-craft/`.

---

## 6. Verdict

**The routing layer works.** Two cold agents, zero searches, three to four hops to the gates,
both landing on the same five files in the same order and both citing rows by number. The two
things built most recently — `symptoms.md` as the front door and the bolded "start here" in
CLAUDE.md's repo-map row — are the two pointers that carried the entire run.

**The distilled layer is load-bearing and the raw layer is not being touched.** Neither agent
opened a single one of the 24 briefs, or `briefs.md`, or `evidence.md`, or `case-studies.md`.
For these two tasks the five distilled files answered everything. That is the intended design
succeeding — but it means four files have no evidence of being load-bearing, and `briefs.md`
(built specifically to make brief sections one hop away) went unused because `symptoms.md`
already carries inline deep links.

**The strongest single line in the toolkit** is `checklist.md`'s procedure step 1 — *read what
was actually made, not only the canon file*. Both agents name it as the reason they left the
canon. Without it, both would have diagnosed a script that is 3/17 built.

**The clearest gap** is that nothing tests *why this reader should believe this narrator* — and
it showed up twice, from two different directions, in one run.

---

## 7. Craft findings the run surfaced (routed here, not filed)

Not part of the navigation verdict. Listed so they are not lost. **Neither has been added to
`critique-pass-3.md`, which remains unratified.**

- 🔴 **No admitted uncertainty anywhere in the twenty scenes.** `narrator.md` §1b rule 6 (the
  Ava trap) requires at least one per run; §5 lists its absence as a named failure mode.
  **Both agents found this independently, neither knowing the other existed.** The drafter adds
  the reason pass 3 missed it: §1b was written back into the toolkit *on the same day, after*
  that review ran — so GPOM has never been tested against it. A toolkit reproducing the same
  finding twice from two different briefs is the best evidence in this report that the
  distillation is real.
- 🔴 **The middle has no human in it, and this is worse as built than in canon.** Both found it
  by different routes — the drafter from the plates (every prompt in cuts 1–3 says *"No people"*;
  124 seconds of finished film with no human being), the symptom agent from the cut order
  (`prompts.md` §2c defers `handover-ladder` and parks canon 2, so **cuts 5–10 carry no human
  presence at all** except the ghosts, whom the scene exists to prove are not there).

The drafter's own proposed write-back — *a `symptoms.md` row for "why would this reader believe
us?"* — is fix 🔴1 below, arrived at independently.

---

## 8. Proposed navigation fixes — **nothing applied**

### 🔴 Must fix

1. **Add a trust layer.** One `symptoms.md` row — *"Why would this reader believe us?"* →
   gates G2/G4 · rows 1.3, 4.4, 5.11 · `narrator.md` §1b rule 6 — plus one `checklist.md` row
   under §4 testing messenger credibility. The ingredients are all in the repo and are
   currently three hops apart in three different files, which is why a competent stranger had
   to compose the frame himself.
2. **Make the story folder route to what was actually built.** `gitpush-origin-master/README.md`
   needs a line naming `prompts.md` §2c as the cut-order authority, `scenes/` as the as-built
   plates and `songs/narration.md` as the recorded narration. `checklist.md` tells a reviewer to
   read what was made; the story folder does not tell them where it is, so both agents burned
   steps on `ls -R`. Same fix likely applies to every story folder.

### 🟠 Should fix

3. **Decide whether the `story-craft` skill is the door or a duplicate.** It fired 0/2 — both
   agents went `CLAUDE.md` → `docs/` and never invoked it, so its Review-mode framing and its
   write-back step never ran. Either make CLAUDE.md's bullet lead with the skill, or accept the
   docs are the real entry point and move the write-back instruction into
   `story-craft/README.md` where a stranger will actually see it.
4. **Write down a target runtime and a burn-down for GPOM.** Both agents flagged its absence;
   one had to extrapolate the film's length to apply a principle. A single line in `prompts.md`
   §2c (`n of 17 fired`, target runtime) closes it.
5. **Fix the three stale pointers and delete the phantom directory** — `ep1.md:40` →
   `../camping/`, `README.md:121`'s code span → `../../ideas/`, and
   `rm -r docs/stories/gitpush-origin-master/docs` (untracked, safe).
6. **State whether checklist rows are independent.** Both agents hit this. One line in the
   procedure — *a beat that passes one row may still fail another; a ruling against row X does
   not discharge row Y* — would have prevented the symptom agent having to argue it from
   scratch, and would have caught the F11/5.8-vs-4.10 gap earlier.

### 🟡 Worth doing

7. **Add a `principles.md` note to 21 / row 4.9** for the case where the chooser and the viewer
   are the same person. The rule assumes they are separable; an abdication thesis collapses
   them, and the toolkit currently has nothing to say about it.
8. **`briefs.md` is unexercised.** 0/2 opened it, because `symptoms.md`'s inline links already
   go section-deep. Not broken — but before investing further in the raw-brief layer, note that
   two full reviews were completed without touching it.
9. **`evidence.md` fired only by proxy.** The never-cite guard worked because ruling 11 is
   duplicated in `principles.md`. Consider whether the never-cite list needs a pointer from
   `symptoms.md`, or whether the duplication is the correct design and `evidence.md` is an
   archive.
10. **Re-headline `prompts.md` §5.** "RULING OVERTURNED" as a section title reads as stale to
    anyone arriving cold, even though the content is current.

---

## 9. Method note, for repeatability

Two agents, one hostile-audience brief and one symptom-report brief, is the right shape: the
first tests whether the toolkit can be *found and applied*, the second tests whether
`symptoms.md`'s rows *match the words a real complaint arrives in*. Running them in parallel
with no contact is what made the convergent Ava-trap finding meaningful.

Cheap to repeat. Worth re-running against a different story (Camping or Magic Money Tree) once
🔴1 and 🔴2 are applied, to check the fixes hold and that the pattern is not GPOM-specific.
