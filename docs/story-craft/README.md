# Story-craft toolkit

The knowledge base behind the **`story-craft`** skill (`.claude/skills/story-craft/`). The skill
is the entry point — this is what it reads. It is the counterpart of [`../suno-gpt/`](../suno-gpt/README.md)
(how Suno hears words) and [`../flow/`](../flow/README.md) (how Flow sees prompts): **how a reader
is held.** The method that assumes this craft is [`../storytelling.md`](../storytelling.md); the
reader it serves is [`../marketing/the-reader.md`](../marketing/the-reader.md); the voice is
[`../voice.md`](../voice.md).

## Files

| File | What | Read when |
| --- | --- | --- |
| [`symptoms.md`](./symptoms.md) | **Start here when something is wrong and you don't know what** — ~45 symptoms in the writer's words ("it reads like an essay", "the middle sags", "will they get that it's sarcasm?"), each routed to a checklist row, a named tool, a principle and the *section* of the brief | The first stop for any "this isn't working" |
| [`principles.md`](./principles.md) | **What we hold to be true** — thirty principles in seven layers, each graded **A** (academic/replicated) / **P** (practitioner consensus) / **p** (one practitioner) / **H** (house ruling); the five gates from the-reader.md stated once; the **sixteen house rulings** where the sources disagreed; the two honest gaps | First use; whenever two pieces of advice conflict |
| [`checklist.md`](./checklist.md) | **The pass** — ~40 questions in seven nested layers (gates → idea → structure → engagement → persuasion → voice → form → run), each traced to its brief; the procedure (read once as a reader, gates first, one layer per pass, notes not fixes, grade and cap, adversarial verification, hold fixed, write back); the coverage-sheet format | Any review; the relevant rows before handing over a draft |
| [`narrator.md`](./narrator.md) | **The BadCode narrator as a design pattern** — a want its power cannot buy, the absence itemised not philosophised, relational vulnerability; flat in satellites / one change arc in the trunk (carrier fixed, cargo variable); the mechanics (bathos as a budget, pre-announcement, the refrain, address by default and the sincere turn rationed, flat baseline and one crack, two comedy lanes, the three-beat, stage straight / snark after); the irony risk and its two tests; eleven failure modes | Writing or reviewing any narration, caption or lyric in the narrator's voice |
| [`toolbox.md`](./toolbox.md) | **Named tools, one line each**, by layer — the move, the test, the example, the failure, the brief | Drafting; when a note needs a named mechanism |
| [`forms.md`](./forms.md) | **What changes per form** — the scroll comic (closure, gutter distance, word and picture, the generated-still redundancy test, constraint-and-break), the narrated video (rhythm, motion budget, words-to-picture, sound, **the house VO markup**, the opening, short-form), the D&B track (narrative in lyrics only), the serialised run (trunk/satellites, the recurring narrator, what may stay open); the cross-form scarcity budgets | Any step that is about the medium rather than the story |
| [`evidence.md`](./evidence.md) | **What the science supports** — claim · grade · source; the myths; the never-cite list | Before quoting a mechanism or a number anywhere |
| [`case-studies.md`](./case-studies.md) | **Works that landed an idea** and the device that carried it — satire, dystopia and warnings, parables, the made mind — with what was criticised | When a scene needs a precedent or a device |
| [`briefs.md`](./briefs.md) | **The brief index** — every "brief NN" cited anywhere in this folder resolved to its file *and its sections*, with anchors, so the long version of a tool is one hop away | Whenever a principle, tool or row says "brief NN" |

## How the skill uses it

**A symptom first** — if the user describes a problem ("it's flat", "too preachy", "the ending doesn't land"),
[`symptoms.md`](./symptoms.md) routes it to the row, the tool and the brief section in one lookup.

**Build mode** (drafting) walks principles §1 → §7 in order — the sentence and the costed object
first, the ending fixed, the spine, the scenes, the persuasion check, the voice, the form — and hands
over with the checklist rows it ran. **Review mode** runs the pass: gates first, one layer per pass,
notes not fixes, findings graded 🔴/🟠/🟡 and capped at twelve, each adversarially verified before
it ships, the arc held fixed, a *Kept* list beside the findings, and a write-back to this folder.

Three facts from the whole sweep that save the most time:

1. **The moral is never stated; the beneficiary always is** — once, plainly, after the feeling has
   landed (ruling 3).
2. **Tell the audience about the bomb.** A narrator who speaks from after the events hands us
   Hitchcock's suspense for free; the only thing worth withholding is the reveal that
   recontextualises (principles 10–12).
3. **Irony is decoded through prior belief.** A real share of any audience takes deadpan as sincere
   — so every sarcastic line is paired with an undeniable on-screen consequence, and every beat is
   run through the Lee/Coe test: whose contempt does it confirm? (principle 18)

## Provenance

Distilled 2026-08-22 from the 24-brief sweep in
[`../../design/research/2026-08-22-story-craft/`](../../design/research/2026-08-22-story-craft/README.md)
(20 commissioned briefs + 4 the critic found missing; three re-run with fresh search), its
[`critic-notes.md`](../../design/research/2026-08-22-story-craft/critic-notes.md), and the house
findings already in [`../stories/gitpush-origin-master/critique-pass.md`](../stories/gitpush-origin-master/critique-pass.md),
[`critique-pass-2.md`](../stories/gitpush-origin-master/critique-pass-2.md),
[`how-we-tell-it.md`](../stories/gitpush-origin-master/how-we-tell-it.md) and the-reader.md's
evidence file. The briefs are research input; this folder is the artifact. Where a brief's claim
was listicle-grade or marked *(unverified)*, it either carries that mark here or was left out.

The first live use was the third adversarial review of *GitPush Origin Master*
([`../stories/gitpush-origin-master/critique-pass-3.md`](../stories/gitpush-origin-master/critique-pass-3.md),
2026-08-22) — the checklist was run on the canon and the as-built cuts, and what it missed was
written back below.

## Post-sweep additions

The toolkit is live. A session that learns something and doesn't write it back has spent the lesson.

| Added | Source | Landed in |
| --- | --- | --- |
| 2026-08-22 | The GPOM critique-pass-3 review (12 draft findings → 24 verifiers → 2 🔴, 1 🟠, 7 🟡, 2 cut) | `checklist.md`: step 1 — read what was actually made, not only the canon file; step 4 — cite rulings by number with the file open; step 6 — refuter + strengthener per finding, expect a third to die; row 2.7 — a plant the text discharges is not a gun; row 5.8 — satellites only, the flagship's change arc is exempt; row 7.2 — test the joke with the name removed |
| 2026-08-22 | Re-run briefs 15, 17, 19 (no search budget; WebFetch of primary sources) | `narrator.md` §1b — the tic is the ache; the flat arc tested to nearly breaking; **the Ava trap** (one admitted uncertainty per run); cosmic scope, human-sized last image |
