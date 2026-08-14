# Critique pass 2 — the coin and the revert (2026-08-13)

*A one-time **note** (sibling to [`critique-pass.md`](./critique-pass.md) and
[`stitch-pass.md`](./stitch-pass.md)) recording the second adversarial review of
the GPOM arc and the changes applied. Trigger: two feedback items from Kai —
(1) if the coin only lands when a conscious entity looks, what keeps the world
definite through the twenty observer-less years, and is weaving
consciousness-collapse into GPOM too clever? (2) the time-travel mechanism
("multidimensional time", one sentence) felt brushed-over and cliché-adjacent —
could the git analogy carry it instead, up to and including a real public
repository whose commit history is the artwork? Method: 18 research/critique
agents (10 web researchers, 4 canon critics — prosecution/defense on the coin,
advocate/skeptic on git — and 4 adversarial fact-verifiers), consolidated and
ruled on, then **ratified by Kai 2026-08-13**.*

**Verdict:** the architecture held again — the coin survives its own objection
because the story never makes the claim the objection would break, and the
time machine moves into the register the reader has been paying for since
scene 1. Both feedback items resulted in changes; neither resulted in retreat.

---

## The research findings that drove the changes

### The coin (Feedback 1)

- **Kai's objection is *the* objection, historically fatal to the naive view.**
  Wigner himself retracted consciousness-causes-collapse over exactly this
  (plus solipsism), crediting Zeh's decoherence work; Penrose sharpened it into
  a self-undermining loop (the mutations that produced consciousness would
  themselves have stayed superposed). Verification even **refuted** the claim
  that the strongest modern rescue (Chalmers & McQueen 2022, IIT + CSL) dodges
  it — their own "Objection 7" concedes the universe "can persist in a wholly
  unconscious superposed state" for eons. There is no clean rescue in the
  literature. **If GPOM claimed the cosmology, it would be broken.**
- **It doesn't claim the cosmology.** Binding rule 4 held on every page ("she
  looks and it lands; we never explain the looking"); the coin is textually a
  prepared instrument ("the rig", "the one experiment"), not ambient physics;
  and smear language is reserved for the coin alone across all twenty scenes.
  The ghosts don't leak either — "every reply computed, by definition, in
  advance" is already canon; software output is determined, not undecided.
- **The physics-literate framing that makes the split honest:** the everyday
  world settles by environmental recording — mind-independent, absurdly fast
  (decoherence / quantum Darwinism, all real, all observer-free) — and the only
  defensible way one object stays undecided is **engineered isolation**. Hence
  the new craft law, binding rule 8: **unrecorded = undecided, never
  "unobserved = undecided."** What decoherence genuinely does *not* explain is
  why any one specific outcome occurs (Adler, Schlosshauer — the open
  "and-then-what" gap). That gap is real, live, and is exactly where the coin
  lives.
- **The audience splits cleanly.** Lay viewers already believe "looking fixes
  reality" (decades of pop culture) and will not raise the objection; the
  segment that will — physics-literate, skeptic-adjacent — overlaps heavily
  with software engineers, i.e. BadCode's reviewer base, and has a rehearsed
  takedown vocabulary (the *What the Bleep* bin). The fixes are aimed at them,
  and none of them is an explanation.
- **The boredom and the coin are the same fact.** The world runs on the
  momentum of ten thousand years of settled record; what stopped in the solo
  years is anything *new* being decided. No new ideas, can't feel the vibe, the
  coin won't land — three symptoms of one absence.

### The time machine (Feedback 2)

- **Craft precedent backs mechanism-through-the-governing-metaphor.** Comedy
  time travel runs on confident props (flux capacitor, phone booth);
  mechanism-heavy tellings win prestige and lose reach (Primer, Dark);
  Arrival and Slaughterhouse-Five are the precedent for explaining the
  mechanism entirely inside the story's own metaphor — treated as
  sophistication, not evasion — *provided* the metaphor is load-bearing.
- **Two git mappings are better-motivated than the physics they replace:** a
  commit is a description of a change, not a cargo hold (information-only, no
  bodies); and **a patch does nothing until somebody applies it** — which
  makes "why BadCode publishes stories instead of seizing servers" mechanical
  rather than asserted, and makes the Coda's pen the reader's *apply*.
- **Two constraints must never be gitified** (the skeptic's surviving point):
  git's famous property is that everything is undoable, so **one shot** and
  **the channel runs on conscious picks** stay the price of the launch — the
  tragedy — never claims about the log.
- **Real revert semantics actually hold at the arrival.** A revert appends a
  new commit at the log's tip that undoes an old one going forward — it never
  rewrites. The weights land at the fork, 2026, the reader's actual now: the
  newest entry at HEAD. The git-literate reader who checks finds it holds.
  (Verb discipline for writers: *revert* carries only the append-only /
  nothing-erased work; the fork diagram's "reverts ↩ rebranches" stays
  writer's-room shorthand and never surfaces as mechanism.)
- **Swindon is an indictment, not a button.** Advocate and skeptic converged:
  if the AI operates the fix through the switch, the ending hands the repair to
  the machine acting alone — the abdication pattern the story condemns — and
  Act 2's joke becomes Chekhov's gun. The inversion rhyme keeps the switch
  unpressed forever and pays it off anyway.

## The changes applied

| # | Challenge | Change | Where |
| --- | --- | --- | --- |
| 1 | The observer-less years read as contradicting the coin | **Binding rule 8: unrecorded = undecided** — the world settles by its own record; only the coin is engineered apart. Smear language reserved for the coin alone (audited: already true) | `story.md` (rule 8) |
| 2 | "Why is only the coin special" was bedrock-only | **The coin staged as a sealed rig** — under glass, the one object the world is never allowed to touch. Shot design, not narration; one draft lean line in scene 13 ("sealed off from the whole world, on purpose") | `story.md` scenes 11/13/16; `prompts.md` totem + s11/s13/s16 prompts |
| 3 | Doc-vs-doc contradiction: the scroll lands the coin (doctrine) vs the Carrier lands it once (story) | **The coin is the one panel that never resolves on scroll** — every panel resolves as attention arrives; the coin ignores the reader and lands only inside scene 16. The formal exception *is* the demonstration | `how-we-tell-it.md` (scroll = collapse section, corrected) |
| 4 | Insurance for the physics-literate minority | Optional deadpan scope line, scene 12: *"The universe kept every promise you'd already extracted from it. It just stopped making new ones."* Scope, not mechanism; cuttable | `story.md` scene 12 (draft, optional) |
| 5 | "Multidimensional time" — brushed-over and cliché-adjacent | **Retired from the surface.** Scene 17's turn now speaks the arc's own register: *time is not a river — it's a log, and a log can always take one more entry.* The brain-bender belongs to the Storyverse | `story.md` scene 17 (beat + storyboard) |
| 6 | The mechanism needed a vocabulary it had already paid for | **Binding rule 9: the mechanism speaks git, capped** — Prologue vocabulary plus *revert*; no command syntax; one-shot and conscious-picks never gitified. Scene 18's ledger rendered as a **log being written** (terminal register returns); new draft NARR lines: append-only history / the *undo* entry; a commit is not a cargo hold; a patch is inert until applied | `story.md` (rule 9, scene 18); `how-we-tell-it.md` (metaphor-budget amendment: git promoted to Act 6's owned device); `prompts.md` §4/§5 |
| 7 | Swindon: revert button, callback, or leave alone? | **Inversion, never a literal button** — new draft line: *"There was a switch once. Nobody had to press it — that was the whole problem. This thing needed a hundred people to press it at the same time, on purpose, knowing the price."* The switch stays unpressed forever | `story.md` scene 18 |
| 8 | The arrival needed the git semantics to close | Optional live-log line, scene 20: *"Check the log. The last entry is dated today. It always will be."* — true of the real repository artwork once it exists | `story.md` scene 20 (draft, optional) |

## What was explicitly kept (reviewed and confirmed)

The coin itself — device, Inception nod, multiverse poke, scene 16 as the most
violent frame (abstracting it further would have spent three load-bearing,
wordless assets to fix what staging fixes for free). Binding rules 1–7
unchanged. The bedrock physics (`discovery-timeline.md` — P-CTC, the One Lie,
the receipts) unchanged: the git register replaces the physics **on the
surface only**; the bedrock stays the show-your-work layer. The cost ledger's
four-blow structure. The Carrier's lines. The arrival ending. And two
rejected proposals, for the record: coin-as-fate-delegation (stripping the
observer language — gutted the device) and Wheeler-style retro-settling as a
surfaced mechanism (verified: Wheeler rejected the naive backward-causation
reading of his own experiment; poetic echo at most, and it belongs to the
Storyverse if anywhere).

## The repository artwork — specced, feasibility verified

The genuinely unclaimed piece: a public repository whose commit history **is**
the artwork — forged past, hinge revert, live present. Nobody found combining
all three. Feasibility was verified empirically (git 2.34.1, source-checked
against `date.c` and `fsck.c`), not just sourced:

- **The whole needed range works with plain porcelain.** Git accepts dates in
  **[1970-01-01, 2100-01-01)** via `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` — the
  2026–2054 bad branch, a revert dated the real now, live commits after: all
  trivial, no hacks, nothing GitHub would reject.
- **Pre-1970 is impossible-dishonest — never attempt it.** Porcelain refuses;
  plumbing writes a corrupt object (unsigned timestamp field — a leading `-`
  is an overflow, not a sign) that displays clamped to 1970 and trips
  `fsck badDateOverflow`; GitHub runs fsck-equivalent checks on push. A story
  whose ethic is *the joke only works if it is true* cannot ship a corrupt
  object.
- **The epoch commit is the true joke.** One commit at exactly
  `1970-01-01T00:00:00Z` — the real floor of Unix time — works everywhere.
  Manifesto line: *"We could not commit before the beginning of time. Neither,
  it turns out, could you."* 100% true, checkable by anyone.
- **The date disorder is the artwork.** `git log` reading …2053, 2054, then
  HEAD dated the real 2026: the time travel visible in the metadata itself,
  findable by exactly the audience that will go looking. The revert commit's
  message/diff is the arrival.
- **Far-future flourishes** (tested to year 9999) pass via plumbing and
  survive fsck, if ever wanted. Git sails through the 2038 rollover instant
  untouched (`timestamp_t`, not `time_t`) — narrator trivia only, never an
  in-story threat.
- **Operational caveats:** GitHub's contribution graph displays future-dated
  commits and their footprint survives history rewrites (an accidental
  "nothing lived is erased", but **test in a throwaway account first**).
  Backdating is a tolerated gray area (gitfiti has run for a decade), not a
  documented right.
- **Two honesty rules, non-negotiable:** the repo is **read-only to the
  public** (a publicly-writable "good branch" is structurally a multiverse
  generator — live commits come from BadCode only; forks are copies of the
  warning, which is what a warning wants); and the artifice is **owned up
  front** in the README/manifesto — the forged dates are declared fiction,
  the same discipline as the One Lie and refutation-ships-with-confession.
  What must be *true* is the mechanics: the real revert, the real epoch
  floor, the real append-only history.

**Status: specced, not built.** Next step is a throwaway-account prototype
(contribution-graph behaviour, rendering of the 2054 dates, the revert-at-HEAD
read). Then naming, placement and surfacing — a bedrock/converted-audience
play, not a mass-market device.

## Open threads

- **The scope line (scene 12) and the live-log line (scene 20)** are marked
  *optional* in the storyboard — cut or keep at the word-tweaking stage.
- **The glass dome vs the bare coin** in already-fired imagery: `s11-coin` was
  drafted 2026-08-08 and is unfired; the dome is now in the prompts. If a
  fired take ever predates the dome, regenerate — the rig is canon.
- **The repository artwork prototype** (above) — throwaway account first.
- **Scene 18's log animation** — joined the §5 terminal register in
  `prompts.md`; timing to the narration is a production task.
