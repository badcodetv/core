# How to run an iteration session

The rest of this toolkit is **what is true about Suno**. This file is **how to work** — the
process for taking a song from "not right yet" to a take you'd release, without paying
twice for the same lesson.

Written 2026-08-21 out of the Camping duet re-cut: seventeen rounds, roughly six of them
spent on a mistake the process below would have caught in one.

---

## The three layers, and why they must stay separate

Every session produces three different kinds of writing. Mixing them is how a toolkit rots.

| Layer | Lives in | Holds | Lifespan |
|---|---|---|---|
| **The sheet** | `docs/stories/<story>/songs/<song>.md` | the boxes you paste, plus the reasoning for each clause | until the song ships |
| **The log** | `docs/stories/<story>/songs/<song>-prompt-history.md` | what failed each round and why; superseded prompt versions as revert targets | forever, read rarely |
| **The rules** | `docs/suno-gpt/files/*` | what is true of **Suno**, not of this song | forever, read every session |

The test for which layer something belongs in: **would this sentence still be useful on a
completely different song?** If yes it is a rule and it goes in `files/`, even if you only
saw it once. If no it is a log entry.

**Promote the same round you learn it.** A lesson left in a song sheet is a lesson the next
song pays for again. Camping's history file exists because the promotion habit was there
from round 1; the rules that came out of it are now doing work on tracks that do not exist yet.

---

## The loop

**1. Baseline.** Generate once before changing anything. You cannot attribute an improvement
without a before.

**2. One variable per round.** The strongest discipline in the list and the easiest to break.
Two changes in a round means a round you cannot learn from — and the fix is not "be careful",
it is to *write down what the single variable was* before you paste.

**3. Listen, then diagnose — do not reword.** The reflex when something is wrong is to
re-word the clause that asks for it. In Camping that reflex was wrong more often than it was
right. Real causes found upstream of the wording:

| Symptom | The wording was fine. The cause was |
|---|---|
| guitar never appeared | a **stale ban** three rounds old, in a box nobody re-read |
| amen fills inaudible | the **drum bed was already amen** — the fill had nothing to contrast with |
| instrumental gap mid-verse | `[Build]`'s **genre connotation**, which beat three explicit denials |
| two ranting men started **singing** | a **melodic accompaniment** underneath them, no vocal clause touched |
| orchestra arriving in bar one | `My Taste` has **no section scope** |

So: before rewriting a clause, check what the *other* boxes already say. Most of that table
is a box contradicting itself.

**4. Change the category when the wordings fail differently.** The single most expensive
lesson of the Camping session, at roughly six rounds. Five ways of asking for an orchestral
layer each failed, each in a *new* way. Failing the *same* way means keep rewording. Failing
**differently every time** means the idea is wrong, not the sentence.

**5. Accept, then freeze.** Mark the sheet ACCEPTED with a date, and say plainly: *change
this only against a fault you can name in a take.* A sheet still labelled "draft" invites
the next unmotivated edit.

**6. Promote the lessons, then commit.** See the layers table.

---

## Boxes grow. That is the main regression source.

Every round adds words; nothing removes them unless you make it. Camping's verse cue reached
**1,010 characters and ten clauses** without any single round doing anything unreasonable.

- **Keep a trim ledger** — a written order of what gets cut first when a box hits its cap,
  and what may never be cut. Deciding that under pressure produces bad cuts.
- **Know each box's scope**, which is what makes trimming decidable rather than aesthetic.
  The scoping rule and the derivability test are in
  [`files/suno-tag-mechanics.md`](./files/suno-tag-mechanics.md).
- **Archive the previous version before a big cut**, into the log file, as a named revert
  target. Then a regression costs one paste instead of a re-derivation.
- **To add something back, change a global clause's scope — do not add clauses.**
  `running under every vocal section` is four words and covered three sections at once.

---

## Verification, when the words are fixed

If a song rebuilds something already released, **diff it mechanically every round.** Camping's
sheet lost three words — one deleted, two altered — and **nobody heard it across nine rounds
of close listening.** It surfaced only because Kai asked "are you confident?" and the answer
had to be computed.

Two rules that keep the check worth having:

- **Encode deliberate departures.** A check that always fails is a check nobody reads. When
  a word change is intentional, add it to the normaliser and record why in the sheet, so the
  script keeps flagging only *accidents*.
- **Measure the artifact, never the note about the artifact.** Camping's sheet documented
  five line-splits; two had never been applied, and the note recording an *intended* edit read
  exactly like one recording a *made* edit. It went unnoticed for weeks. Any claim a doc makes
  about a file is checkable — check it.

---

## Two things about evidence

**One take proves nothing.** Phrasing, casting and arrangement all vary between generations on
an *identical* sheet. A lever that looks like it worked may be a lucky roll. Any real
experiment needs **two or three takes per condition**, one variable at a time — and re-rolling
is cheaper than any fix, so try it before changing the sheet at all.

**The listener is the oracle; the model is the diagnostician.** The division that worked: the
human says *what is wrong with what they hear*, the model says *which clause in which box
causes it*. It breaks when the model starts having opinions about taste — and it is rescued,
repeatedly, by the human pushing back on a confident diagnosis. In Camping, "I'm just checking
you're happy the guitar would hold" found a third blocker after two had been reported as the
complete set. **Treat a challenge as data, not as doubt to be reassured away.**

---

## Opening a new song session — the checklist

1. Read the song sheet **in full**. Never work from memory of it; the human edits between turns.
2. Read the song's `-prompt-history.md` summary table — five lines, not the whole log.
3. Skim [`files/suno-tag-mechanics.md`](./files/suno-tag-mechanics.md) and the
   [known-unreliable list](./README.md#known-unreliable-claims) so you don't re-run a
   documented dead end.
4. Grep the Exclude box **and** `My Taste` for anything you plan to add — the instrument, its
   *category*, and any whole-palette adjective (`machine-made`, `acoustic`, `electronic`).
5. Baseline generation before any change.

---

## The per-song summary table

Every `<song>-prompt-history.md` opens with a **"What this song taught"** table so a future
session can absorb it in a minute without reading the log. Worked example:
[`docs/stories/camping/songs/camping-prompt-history.md`](../stories/camping/songs/camping-prompt-history.md).

Columns: **what broke · why · the fix · where the general rule now lives.** The last column is
the important one — an entry with nothing in it is a lesson that has not been promoted yet.
