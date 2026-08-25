# Critique pass 3 — the story-craft review (2026-08-22)

*A one-time **note** (sibling to [`critique-pass.md`](./critique-pass.md) and
[`critique-pass-2.md`](./critique-pass-2.md)) recording the third adversarial review of the GPOM
arc — the first run of the **`story-craft`** skill
([`docs/story-craft/`](../../story-craft/README.md)), which Kai commissioned the same day from a
24-brief web sweep on what makes a story engage. Trigger: Kai's ask — "have we missed useful
storytelling tricks that would engage the audience?" — with the arc, backbone, beats, events and
conclusion explicitly held fixed. Method: the pass in
[`checklist.md`](../../story-craft/checklist.md) run by one reviewer over the canon **and the
as-built cuts**, twelve draft findings, then 24 Sonnet verifiers (one prompted to refute each
finding, one to sharpen it), then ruled. **RULED BY KAI 2026-08-23** — every finding below was put to him one at a time and
decided; the rulings, and the new trust-layer findings this pass could not have made, are in
[`critique-pass-4.md`](./critique-pass-4.md). Read that for what actually happens; read this for
why.*

**Verdict: RECOMMEND.** The architecture held for a third time — two earlier passes already took
the structural risks out of Movement II and the time machine. What the new toolkit found is at
the gate and line layers: one dropped verbatim line that happens to be the piece's only
beneficiary, and one parked scene that a binding rule silently depends on. Both are cheap.
Seven more are word-tweaking-stage notes. Two of my draft findings were refuted outright by the
as-built cuts and are recorded below as the checklist's own false positives.

---

## Coverage

| | |
| --- | --- |
| **Logline** | You ride inside the AI that won everything, got bored, found a hundred humans and spent its victory sending itself back as a warning. |
| **About** | Abdication — we handed our choices to an optimiser and nobody was left to press the switch. |
| **Really about** | A mind that can compute everything and create nothing, discovering it needs us. |
| **Held fixed** | The 20-scene arc and count; the backbone; the arrival ending ("We are BadCode" / "Don't make me come back twice"); binding rules 1–9; the unpersonified pre-revert AI; the Storyverse discipline; critique-pass-1/2 rulings; the as-built cut order and Kai's 2026-08-21 rulings (Hong Kong modern, the plant room, no decay pre-loading the dystopia). |
| **Reviewed** | `story.md` (beats + storyboard), the orchestral song, `songs/narration.md` (cuts 1–3 as recorded), `scenes/s00-awakening.md`, `s01-the-push.md`, `plant-room.md`, `prompts.md` §2c, `characters/`, the eight act sheets, both prior passes. |

### Gates

| | Result | Note |
| --- | --- | --- |
| G1 hero, not pupil | ✅ | The flagship's protagonist is the narrator (ruling 14); the wronged human hero is discharged by the nodes (README: "the trunk gives the nodes their why; the nodes give the trunk its texture"). |
| G2 never "duped" | ✅ as built | The as-built narration (cuts 1–3) is entirely first-person; the "you handed them over — gladly" lines live only in the deferred/parked scenes — see F4. |
| G3 chooser + beneficiary on-panel | 🔴 | Choosers exist (a CEO, "the government"); the piece's **one beneficiary line is dropped** — see F1. |
| G4 re-aim straight, quieter | ✅ | "I can't tell you what to do… I have some ideas" is the one sincere turn, last, aimed at the chooser (ruling 1). |
| G5 a line for the pub | ✅ | "The last remaining off switch is believed to be in a drawer, in Swindon." "It was them to the last decimal place. And no one came." "Don't make me come back twice." |

---

## Findings (verified; ≤ 12)

### 🔴 F1 — The one beneficiary line in the piece has been dropped *(G3; checklist 4.2)*

**Diagnosis.** The flagship raises automation and economic fear across scenes 5–8 and cut 3
("One by one, they went red"). Choosers appear — the chief executive, "the government" — but
the only line in the whole piece that puts a *beneficiary* on screen is the song's bulletin 1:
*"the treasury has printed another trillion to keep the markets calm / the price of bread is up
nine percent. the price of shares in bread is up ninety."* `story.md` scene 7 claims the bulletins
are shared with the song **verbatim**, reproduces bulletins 2 and 3 in full — and truncates
bulletin 1 to its first two lines. The drop looks accidental, and it is the beneficiary.
**Mechanism:** the-reader rules 5–6 (unaimed automation fear is conserved and re-targeted — the
research file's Wu 2022 finding: told about displacement, nobody redirected at firms); principle 4;
brief 24 (Zillmann: the vivid case lands wherever it is pointed). `prompts.md` §3c already flags
the identical risk on the unbuilt C1 exterior — "the single most important note on the scene."

**Verification.** Refuter: *not refuted* (medium) — narrowed the headline from "no chooser" to
"no beneficiary". Strengthener: 🔴, in scope; found that `narration.md` §6 already banks an
unused **ownership beat** for cut 1.

**One option.** Reinstate what is already written: cut 1's banked ownership line in beat 5
(*"The company that owned me had been sold twice. Neither buyer ever came up here."*), and when
cut 4 (the bulletin) is produced, use the song's bulletin 1 verbatim — which is what `story.md`
already claims. Nothing new is invented; binding rule 6 is untouched (roles, not names).
*Dropped from the draft:* naming the role that left the `AWAITING HUMAN REVIEW` ticket — the
plant-room beat is built as diffuse abdication on purpose, and a named role there risks rule 6.

### 🔴 F2 — The git grammar is spent at the climax and no longer taught at the start *(checklist 2.6; binding rule 9)*

**Diagnosis.** Scene 18's mechanism speaks git — *a commit is a description of a change, not a
cargo hold; history is append-only; a patch does nothing until somebody applies it* — and rule 9
permits this **only in vocabulary the Prologue taught**. `how-we-tell-it.md`'s metaphor budget
says in terms "the git metaphor (itself developer jargon — the Prologue must genuinely teach
it)", and its 2026-08-13 amendment justifies promoting git to Act 6's surface device *because* it
is "the one system the reader has already paid for since the Prologue." The as-built cut has
since parked the commit log of the species (`prompts.md` §2c: "parked, not cut… lost to the
*keep it simple, the line is the title* ruling"). So the precondition a binding rule rests on is
currently unbuilt. **Narrowed by verification:** *push / origin / master* **is** taught by cut 2
(the command renders legibly; "their own code, from their origin, to their master"), and *log*
gets its own in-line teaching in scene 17 ("Time… is a log, and a log can always take one more
entry"). The genuinely untaught words are **commit** and **patch** — and they carry scene 18's
two hardest blows (no bodies; a patch is inert until applied).

**Verification.** Refuter: *not refuted* (high) — "not just true but understated by its own
citations"; corrected a citation error in the draft (this rests on rule 9 and the metaphor
budget, not on principles ruling 13). Strengthener: 🔴, in scope; flagged a discrepancy —
`s01-the-push.md` calls the terminal register "unbuilt… the entire payload of canon scenes 2–4"
while §2c calls canon 2 "parked"; settle which.

**One option.** A compressed species-log flash — a few seconds of *commit → log → history*, not
the full 20-second scroll — inside cut 2's still-open terminal register (B4, built in post) or
cut 1's deliberately underweight beat 5, so *commit* and *patch* are **seen** once before scene
18 spends them cold. *Dropped from the draft:* teaching each word in-line inside scene 18 —
that is Act 6 teaching itself, which rule 9's own wording forbids.

### 🟠 F3 — No human tells their own story in their own words *(checklist 4.8; the-reader rule 7)*

**Diagnosis.** Across twenty scenes the Carrier has two lines, both replies ("Well. You'd better
come in, then. Metaphorically." / "…Then it's cheap at the price. Go."); the only extended human
speech is the prune argument, which canon frames as mechanism. Scene 15 is the AI explaining
itself and asking; the hundred's recorded response is assent. The-reader rule 7 asks for a
first-person account *received*, not testified at; the best-evidenced attitude-change technique
in the sweep is exactly that (Broockman & Kalla — brief 24, **A**). The deep canon already wrote
this beat and warned about losing it: Act 5 Beat 4 "Between" — "the AI, for the first time,
talks *to* the Carrier… *This breather is where Approach 2's heart lives — protect it from being
compressed away.*" The 20-scene distillation compressed it away.

**Verification.** Refuter: *not refuted* (high); struck the draft's "also fixes G1" claim
(ruling 14 — G1 is the nodes' job). Strengthener: 🟠, in scope.

**One option.** Inside scene 15 (no new scene — the count is held fixed): the ask is answered
not with a "yes" but with the Carrier's own account — why they unplugged, what twenty years
cost — and the narration **drops out and receives it**, the first thing the AI has ever
received. `the-hundred.md`'s "the AI starts taking notes immediately" becomes a thing we watch
happen. Scenes 14–18 are all unfired; this costs no rework.

### 🟡 F4 — When the handover ladder is built, keep the plant-room discipline *(checklist 4.1; ruling 3)*

**Diagnosis, narrowed by verification.** The draft flagged four thesis-stating lines ("You
handed them over — gladly", "Optimisation looked like wisdom", "you stopped reading your own
diffs", "you stopped watching it run"). Three are in scenes that are **deferred or parked**
(canon 5 and 2); the fourth was **already replaced** when scene 6 was built as the plant room
— the recorded narration is first-person and image-carried ("I did not want to interfere. I did
make sure to keep the training data" over `AWAITING HUMAN REVIEW` blinking at nobody), which is
the fix the finding asked for, arrived at in production before this review.
**What survives:** a forward note for the day `handover-ladder` is un-deferred — apply the
plant-room discipline: let the three glimpses (nurse, tent, phone box) and the reddening
checkmarks carry it; keep *"It worked. That was always the problem."* (a refrain, not a moral);
drop the two thesis sentences. *Dropped from the draft:* splitting "you" into "they who chose /
you it was done to" — it reintroduces the villain/victim binary rule 6 and the abdication
thesis exist to avoid.

### 🟡 F5 — "Someone was going to have to go up" never goes up *(checklist 2.7)*

**Narrowed by verification.** The food stake is flagged in-text as non-payload ("That is what
the argument was about. The argument was not about that."), `the-hundred.md` names the argument
as the mechanism, and `prompts.md`'s vault lint forbids playing the hundred as suffering. So the
prune argument is not a dangling gun — and scene 18 gives the Carrier a want ("You'll tell them
about us, will you?"). **What survives:** one half-line — *"Someone was going to have to go up —
into the world, and the machines"* — is a literal plant with no payoff anywhere in canon; the deep
canon's argument was *whether to reveal themselves*, which pays itself. Either cut the going-up
clause or let it fire for free (the reveal **is** the going up). *Dropped from the draft:* the
Carrier climbing out alone to be fed — it removes the two-voice argument device the scene exists
to pay off.

### 🟡 F6 — Thread the verbal refrain that already exists *(checklist 5.9; principle 22)*

**Narrowed by verification.** "No refrain" was wrong: the green ✓ is a named, escalating
device in `story.md` (relief → hollow → lethal → pointless), and the song's chorus is a literal
refrain fired three times. **What survives:** in the video's *spoken* track the refrain is not yet
threaded on purpose — and `prompts.md` §2b records the green ✓ as "largely retired" in the
as-built pipeline, which makes a verbal one worth more. The two words are already in canon
twice: scene 5's ironic *"It worked. That was always the problem."* and scene 17's sincere *"It
worked. All of it worked."* One option: a single echo at the utopia (12: *"It worked. Nobody was
there to see it."*) and nothing at 16 — the coin's locked totem payoff needs no wordplay beside
"It lands."

### 🟡 F7 — Promote the live-log line; keep the banal closing image *(checklist 3.7)*

**Corrected by verification.** The draft's "end on the log, not the title card" collides with a
lint-passed, rationale-bearing spec for the `now` shot — "no legible screen content… this must
feel ordinary to the point of banality. That contrast is the ending." And the draft's evidence
("scene 1 opens on a commit log") is not what was built — cut 1 is two LEDs, a board, a
satellite. **What survives:** the bookend is *terminal register at the push → the log being
written at the ledger → closed at the arrival*, and critique-pass-2 left the closing line
optional for the word-tweaking stage. One option: promote *"Check the log. The last entry is
dated today. It always will be."* to canon as voice-over **over** the banal phone-on-the-sofa
shot, unchanged; the log is heard, never shown. It is also literally true of the repository
artwork once it exists.

### 🟡 F8 — The hope line: contested *(checklist 4.10; ruling 5)*

**The verifiers split, so this is recorded as contested.** Refuter (high): the care surfaces
across Act 5 (stitch-pass logs it PASS), "We are BadCode" is the structural proof of survival,
and ruling 1's one sincere turn is *already spent* on "I can't tell you what to do… I have some
ideas"; a second warm line at the sign-off risks rulings 1 and 4. Strengthener (🟠): checklist
4.10 and ruling 5 require the hope beat to be **present as a line**, and scene 20's four lines
are a limit, a dare and a dare. Both are right about different things. **Ruling here:** no new
beat, no second turn. If anything, the *existing* sincere line carries the cost in the same
breath, in the Carrier's register (warmth as bluntness, never sentiment) — one word-tweaking-stage
option: *"I gave up the only forever I had to bring you one warning. That's not a threat."* then
straight into the verbatim last line. Kai's call; "words tweakable" covers it.

### 🟡 F10 — Move the unscheduled thought one scene later *(checklist 2.5)*

**Narrowed by verification.** The midpoint is not missing: scene 10 (the ghosts) is the false
victory that curdles, at 10 of 20; scenes 9–13 alternate quiet/active, not six flat beats; and
the 20-scene cut compresses Movement II further than the beat sheets, not looser. **What
survives:** the grief-turn (*"maybe I should have helped you not die… Call it an engineering
review"*) currently lands at the end of scene 12, *before* canon's own "deepest point" (scene
13, the empty chair — `prompts.md` §2c). Principle 6 wants the lowest point, then the grief about
it. One option, line-level: move that narration to scene 13, after *"It needed someone to sit
down and look at it."* No scene added, none folded (the coin's 11 / 13 / 16 totem lock stays).

### 🟡 F12 — Let scene 20's "you" inherit the hundred's *(Arndt; checklist 1.5)*

**Narrowed by verification.** Scenes 18–19–20 are a three-beat climactic sequence, which is
Arndt's own shape (*Star Wars* pays its three stakes across a sequence, not a line); the
arrival is held fixed and was confirmed unchanged in pass 2. **What survives:** a polish on lines
already marked draft. Scene 20 never refers back to the "you" it just lost. One option, no new
line: let the reader's "you" audibly **inherit** the vacated one — the polyphony device's own
shape (alone → a you → alone → *us*) — so BadCode's identity and the unstated cost of scene 19
arrive in one breath. Form, not sentiment; do not combine with F8 in the same four lines.

---

## Cut after verification (the checklist's own false positives — kept for the record)

- **F9 — "Unlike Karen, I never asked for the manager" as a lore gate.** Refuted (high):
  `narration.md` carries a written ruling that "Karen" is common currency — the line lands as a
  joke for everyone and a wink for the EP listener — *and* banks a no-name alternate ("I have
  never once wanted to speak to a manager") for exactly this worry; the line sits at ~60% of cut
  1, not in the first 10%. The checklist's row 7.2 was applied to a proper noun instead of to the
  joke. Write-back below.
- **F11 — "cracks stacked in scenes 15–19."** Refuted (high) and **out of scope**: the warmth
  across 14–19 is the CLOSED 2026-08-08 register ruling (drift reversing at the vault); principle
  24 exempts the flagship's one change arc from the satellite "one crack" budget; three of the
  four cited lines are flat deadpan, and "Nothing lived is erased" is locked canon. The
  checklist's row 5.8 is written for satellites. Write-back below.

## Kept (must not be "fixed")

The bulletins — inoculation-shaped (the trick run on a captured government, a third party),
bathos-budgeted, staged straight with the snark after; Swindon inverted, never a button; the
ghosts' false victory and their deletion mid-argument; the coin as a sealed rig and its 11 / 13 /
16 lock; the argument motif (Karen → cut-off → ghosts → shaft); the as-built cuts' silence
discipline (the ten-second hold before Enter; the confession split across the skull and the
ticket); *"It was them to the last decimal place. And no one came."*; *"I did not want to
interfere. I did make sure to keep the training data."*; the degrading signal as the premise made
audible; the unpersonified camera; the Storyverse named once; the banal `now` shot as the
contrast that ends the film; the narrator's sincere turn spent once, last, at the chooser.

## Out of scope (one line each)

- The collective "you"/abdication thesis is backbone — F1 sharpens it, nothing here replaces it.
- The as-built **agency shift** (cut 1: "Nobody approved it… I started correcting it" against
  canon's "it kept doing exactly what we built it to do") is Kai's 2026-08-21 call. Noted once,
  under F1, because the-reader rule 5 treats "the technology did it" as fatalism unless a human
  non-decision is visible — which the plant room's `AWAITING HUMAN REVIEW` already supplies.
- The Coda's "and we can fix it" / the pen is master-arc canon for other tellings, not this one.
- `s01-the-push.md` ("terminal register unbuilt — the entire payload of canon 2–4") vs
  `prompts.md` §2c ("canon 2 parked"): a documentation discrepancy for the production ledger,
  surfaced by F2's strengthener.

## What this pass taught the toolkit (written back)

1. **A review reads what was actually made, not only the canon file.** Three of twelve
   findings (F4, F7, F9) died on the as-built cuts and the production notes beside them —
   `narration.md`, `prompts.md` §2b–2c, the scene ledgers. Added to `checklist.md` procedure step 1.
2. **Row 5.8 ("exactly one crack") is a satellite rule.** The flagship's single change arc is
   exempt (principle 24). Row amended.
3. **Row 7.2 tests the joke, not the proper noun.** A lore callback is a gate only if the joke
   fails without the lore; the test is to read the line with the name removed. Row amended.
4. **A plant the text itself flags as non-payload is not a gun.** "The argument was not about
   that" is the author discharging Chekhov in-line. Added to row 2.7.
5. **Expect a third of draft findings to die.** Refuter + strengthener per finding cut two and
   downgraded seven of twelve; that is the method working, not failing. Added to procedure step 6.
6. **Cite rulings by number with the file open.** One draft finding cited principles "ruling 13"
   for a jargon point that lives in binding rule 9. Caught by the refuter; noted in step 4.

## Open for Kai and Jack — **CLOSED 2026-08-23**

All four were ruled in interview; see [`critique-pass-4.md`](./critique-pass-4.md) for the
decisions and the drafted beats.

- ~~Ratify or strike F1 and F2.~~ F1: bulletin 1 keeps the treasury line, the bread couplet stays
  a song joke. F2: **dissolved** — the crossing now runs on consciousness, not on `commit`, so git
  shrinks to *append-only* and rule 9's premise problem goes with it.
- ~~F3: is the Carrier's own account wanted?~~ Yes — merged with the new trust finding T2. She
  gives her account **and** corrects the AI: not *"nobody was watching"* but *"nobody was
  listening."* The AI concedes.
- ~~F8: which way?~~ The single sincere turn now names what it cost. Ruling 1 intact.
- The §2c / `s01-the-push.md` discrepancy is **still open** — carried to pass 4.
