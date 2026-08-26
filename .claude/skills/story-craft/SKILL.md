---
name: story-craft
description: Use when making a BadCode story more engaging or reviewing whether it engages — drafting or sharpening beats, a scene, a script, a narration line, a caption, a lyric, or an ending; running an adversarial review of a story, comic, video cut or track ("review this story", "is this beat working", "why is this flat", "does this land", "story doctor", "run the checklist", "coverage on…", "adversarial review of <story>"); or any beat/script/caption/lyric step inside new-story, make-comic, music-video-short or suno-prompt. Encodes the 2026-08-22 story-craft research (24 briefs) as principles with evidence grades, a 40-question review pass, the narrator pattern and per-form craft. Craft only — WHO the reader is stays with docs/marketing/the-reader.md, HOW we sound with docs/voice.md, and canon capture with new-story.
---

# Story Craft (BadCode)

Make the thing grip. Two modes, one knowledge base:

- **Build** — you are drafting or sharpening (beats, a scene, a script, narration, captions, lyrics,
  an ending). Apply the principles while writing; run the relevant checklist rows before handing
  over.
- **Review** — you are asked whether a piece engages, or to run an adversarial review. Run **the
  pass** ([`docs/story-craft/checklist.md`](../../../docs/story-craft/checklist.md)) and deliver a
  coverage sheet.

**Boundary with `shot-craft`:** story-craft owns what a sequence *means* — the argument, the
beat, whether it earns its place. `shot-craft` owns what the frame *is* — composition, light,
angle, cutting rhythm. A cut that is flat because the shots don't step is shot-craft; a cut that
is flat because the beat isn't earning is here. When unsure, ask whether re-framing every shot
would fix it.

This skill does **not** own the story's argument (that is the canon under `docs/stories/`), the
reader (`docs/marketing/the-reader.md`), or the tone (`docs/voice.md`). It owns the *machinery* —
how an idea becomes something a distrustful person finishes, remembers and repeats.

## Read first

- `docs/marketing/the-reader.md` — the ten rules. They are the **gates** of every review; a piece
  that fails one is not reviewed further.
- `docs/voice.md` — the four dials; sarcasm diagnoses, care re-aims.
- `docs/storytelling.md` — the BadCode method (concept + background → metaphor → beats). This skill
  sits under step 2 of its working process ("research storytelling techniques") and makes it
  permanent.
- **`docs/story-craft/principles.md`** — the thirty principles with evidence grades and the sixteen
  house rulings on contested advice. Read it in full the first time in a conversation; after that,
  consult.

## The knowledge base lives in `docs/story-craft/`

Read on demand. Never reproduce its content in a reply; don't lecture the user about it.

| File | What | Read when |
| --- | --- | --- |
| [`symptoms.md`](../../../docs/story-craft/symptoms.md) | **Start here when the user describes a problem** — ~45 symptoms in a writer's words, each routed to the checklist row, the named tool, the principle and the brief section | Any "this isn't working / feels flat / too preachy / doesn't land" |
| [`principles.md`](../../../docs/story-craft/principles.md) | **What we hold to be true**, graded A / P / p / H; the gates; the sixteen rulings; the two honest gaps | First use in a conversation; whenever two pieces of advice conflict |
| [`checklist.md`](../../../docs/story-craft/checklist.md) | **The pass** — ~40 questions in seven nested layers, the procedure (notes not fixes, one layer per pass, adversarial verification, write-back), the coverage-sheet format | Any review; the relevant rows before handing over a draft |
| [`narrator.md`](../../../docs/story-craft/narrator.md) | **The BadCode narrator pattern** — what an omniscient, bored, caring machine must want and be unable to have; carrier/cargo; address; bathos as a budget; the one crack; the comedy lanes; the failure modes | Writing or reviewing any narration, caption in the narrator's voice, or the narrator's lines in a track |
| [`toolbox.md`](../../../docs/story-craft/toolbox.md) | **Named tools, one line each**, by layer — Mamet's three questions, but/therefore, Arndt's three stakes, Gilligan's mystery/confusion, the boots test, Loach's stage-straight… with the brief to read for the long version | Drafting; when a note needs a named mechanism |
| [`forms.md`](../../../docs/story-craft/forms.md) | **What changes per form** — scroll comic, narrated video (incl. the house VO markup), D&B track (narrative in lyrics only — Suno mechanics stay in `docs/suno-gpt/`), the serialised run; the cross-form scarcity budgets | Any step that is about *this* medium rather than the story |
| [`evidence.md`](../../../docs/story-craft/evidence.md) | **What the science supports** — claim · grade · source; the myths and the never-cite list (22×, oxytocin, Zeigarnik-as-memory, the MrBeast document, retention percentages) | Before quoting any mechanism or number in public copy, a brief, or a note |
| [`case-studies.md`](../../../docs/story-craft/case-studies.md) | **Works that landed an idea** and the device that carried it — satire, dystopia, parables, AI narrators — as a pattern table with what was criticised | When a scene needs a precedent; when choosing a device |
| [`briefs.md`](../../../docs/story-craft/briefs.md) | **The brief index** — resolves every "brief NN" to its file and sections with anchors; the long version of any tool is one hop | Whenever a principle, tool or row cites "brief NN" |
| [`README.md`](../../../docs/story-craft/README.md) | Index, provenance, how to write back | Orientation; adding to the toolkit |

The raw research — 24 briefs, the critic's notes, the contradictions — is in
[`design/research/2026-08-22-story-craft/`](../../../design/research/2026-08-22-story-craft/README.md).
It is research, not policy: read it for the long version of a tool, never as a rule the toolkit
didn't adopt.

---

## Build mode

Use while drafting. The order matters — each step makes the next cheaper.

1. **The sentence.** Before beats: the theme as one *causal* sentence (never a word), the
   anti-theme beside it, and **the one costed object** that will carry it (the boots test). Write
   the last beat now. *(principles §1)*
2. **The gates.** Who is the hero? Who is the chooser, who benefits, and where are they on-panel?
   What is the one line for the pub? If any answer is "the system", stop. *(principles §0)*
3. **The spine.** Beats joined by *but* / *therefore*; a midpoint that reverses; a lowest point
   and then the grief about it; promise → progress → payoff; every plant fires in-release. Mark
   which scene is the compound reversal. *(principles §2)*
4. **The scenes.** Per scene: Mamet's three questions; the value it turns; "no, and…" at the end;
   the silent-movie test; exposition only as argument or pope-in-the-pool. *(toolbox — scene)*
5. **The persuasion check.** Consequence first; the moral never; the beneficiary once, straight,
   after the feeling. Pair every ironic line with a consequence. Run the Lee/Coe test on each
   sarcastic beat. Argue in the reader's moral vocabulary. *(principles §4)*
6. **The voice.** `narrator.md`: flat baseline, one crack, bathos banked before spent, the refrain,
   address by default and the sincere turn rationed. McKee's VO test on every narration line.
7. **The form.** `forms.md`: the duo-specific caption test; the motion, silence and address budgets;
   VO in the breakdown; the first 10% as a promise; the closing image answering the opening.
8. **Hand over with the rows.** List which checklist rows you ran and which you didn't. A draft
   handed over without that list is not finished.

When composing for another skill — `new-story` (beats), `make-comic` (storyboard, captions),
`music-video-short` (scene breakdown, edit plan), `suno-prompt` (lyrics) — say which step you are
applying and keep the canon folder as the source of truth. This skill never writes canon on its
own; it sharpens what those skills produce.

## Review mode

If the user has named a *symptom* rather than asked for a full review, go to `symptoms.md` first
— it routes the complaint to the row, the tool and the brief section, and often that is the whole
answer. For a full review, run **the pass** exactly as `checklist.md` § The procedure says. The
short version:

1. Read once as a reader. Write the **coverage line** (logline · about / really about · verdict).
2. **Gates first.** A gate failure *is* the review.
3. **One layer per pass** — idea, structure, engagement, persuasion, voice, form, run.
4. **Notes, not fixes.** Diagnosis + mechanism (the principle or brief) + at most one labelled
   example. The reviewer has no authority; that is what makes candour possible.
5. **Grade and cap.** 🔴 gate / promise broken · 🟠 missed trick with a named mechanism · 🟡 polish.
   Twelve findings at most; lead with the 🔴s.
6. **Adversarially verify** each finding before it ships — is it already handled in canon? would
   the fix break a binding rule? is the evidence **A** or one practitioner's testimony? For a
   flagship piece, do this with independent agents prompted to *refute*, not agree.
7. **Hold fixed what you were told to hold fixed.** The arc, the backbone, the rulings. A finding
   that needs the arc to change is one line under *out of scope*, not an argument.
8. **Say what works.** A "Kept" list of the things that must not be "fixed" is part of the sheet.
9. **Write back.** What the review taught goes into the toolkit, dated.

Output is the **coverage sheet** in `checklist.md`; for a large piece, write it to
`docs/stories/<story>/critique-pass-N.md` (the existing convention —
[`docs/stories/gitpush-origin-master/critique-pass-2.md`](../../../docs/stories/gitpush-origin-master/critique-pass-2.md)
is the worked reference) so the next session inherits it.

## Rules that are not negotiable

- **Never cite a banned number.** No "22× more memorable", no oxytocin, no retention percentage,
  pixel range, webtoon drop-off point or "first N seconds" as fact. The shape, never the digit.
  `evidence.md` has the list.
- **The evidence grade travels with the claim.** A practitioner's rule of thumb is introduced as
  one; a replicated finding as one. Never launder a **p** into an **A**.
- **The moral is never stated; the beneficiary always is.** (House ruling 3.) If a note asks for
  the point to be "made clearer", check which of the two it means.
- **No fix without a diagnosis, no diagnosis without a mechanism.** "It's boring" is not a note.
  "The scene has no turn — the value at the end is the charge it started with (principle 7)" is.
- **Scope is the user's.** An adversarial review of a committed story does not propose a different
  story. Arc, backbone, conclusion and ratified rulings are held fixed unless the user opens them.
- **Respect the canon's own rules.** GPOM's nine binding accuracy rules, the unpersonified-AI rule,
  the metaphor budget and the Storyverse discipline are constraints on every suggestion, not
  targets for one.
- **Don't restate the-reader.md.** The gates are referenced, not re-derived, and "beneficiary
  on-panel" appears once in a review, not once per layer.

## Write-back

The toolkit is live, like the Suno one. When a review or a draft teaches something the principles
didn't hold — a technique that worked on a real piece, a rule that turned out wrong, a number that
got verified — it goes into the relevant `docs/story-craft/` file with a date and a pointer to the
piece, and `README.md`'s "Post-sweep additions" table gets a row. A session that learns something
and doesn't write it back has spent the lesson.
