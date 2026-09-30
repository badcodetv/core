# RESUME HERE — Magic Money Tree documentary ("The Future He Never Saw")

## 🟢 30 September 2026: phase 1 of the rough cut is DONE (branch `mmt-rough-cut`, worktree `.claude/worktrees/mmt-rough-cut`)

Kai ruled a two-phase build: **phase 1 = the full plan and every asset** (done), **phase 2 = execute
with full autonomy**: Suno generation, recording Suno previews, and the Premiere timeline, all without
asking per step. Everything is in [`rough-cut/`](./rough-cut/README.md); start there.

| Piece | Where | State |
| --- | --- | --- |
| The edit, as data | `rough-cut/cutlist/*.json` | ✅ all 19 scenes, 267 clips, **0 errors, no holes**, 15:13 at planned pace |
| Every shot in every film | `rough-cut/shotlogs/` + `clips/_shotlogs/` on D: | ✅ 29 films indexed |
| Facts + exact quotes | `rough-cut/facts.md` | ✅ 7 narration lines reworded for accuracy (logged in `songs/narration.md` §8) |
| Documents | `rough-cut/documents.md` | ✅ judgment, contract notices, Red Book, White Paper, 1948 leaflet |
| Cards, chart, diagram | `clips/cards/`, `clips/charts/` on D: | ✅ 61 cards, debt chart (3 animations), QE diagram |
| Illustrations | `rough-cut/illustrations.md` | ⬜ prompts only; grey placeholders on the timeline. Kai approves plates |
| Open checks for a human | `rough-cut/checks.md` | 60, by scene and time |
| Preview (no voice yet) | `D:\badcode-videos\magic-money-tree\previews\rough-cut-preview.mp4` | narration as subtitles |
| **Phase 2 runbook** | `rough-cut/README.md` § Phase-2 run | ready |

**Resume prompt (phase 2):** *Resume the Magic Money Tree rough cut, phase 2, in worktree
.claude/worktrees/mmt-rough-cut: read docs/stories/magic-money-tree/rough-cut/README.md and run the
Phase-2 runbook — Suno round 1 and the rest of the parts, record previews, align, retime, then build
mmt-rough-cut-v1 in Premiere. Full autonomy granted for Suno, recording and Premiere; P8 waits for the
legal read; no Flow video credit without my yes.*

---

**Paused 2026-09-29 by Kai** (the state before phase 1, kept for the record):
Read this, then the four files it points to. Everything below is in git
except the media, which is on `D:\badcode-videos\magic-money-tree\`.

## Where we are

| Piece | File | State |
| --- | --- | --- |
| The story | [`storyboard.md`](./storyboard.md) | ✅ rebuilt 2026-09-28: 19 scenes, five movements (Pride, Craftsman, Build, Misuse, Statement), ≈15 min, statement ending + 20 s AI coda |
| The footage | [`footage.md`](./footage.md) §11–12 | ✅ every scene has a free source; 39 films + 36 stills + 18 headline screenshots on disk; conforms 32/41 when paused (re-runnable) |
| The paper edit | [`edit-plan.md`](./edit-plan.md) | ✅ every narration line → clip, in-point, treatment, clock. Not executed; no Premiere project yet |
| The narration | [`songs/narration.md`](./songs/narration.md) | 🟡 first draft: ten Suno parts, style template, three palettes. Words not locked, **nothing generated** |

**The point (agreed):** "We can't afford it" is a choice. The real limit is the work, not the money.

## Kai's rulings to remember (all recorded in the files above)

- 28 Sept: statement ending; shake / starve / plant as verb cards; "we outgrew the debt", never "paid
  it down"; Covid is not the inflation villain; who paid told three times (1940s the wealthy, 2010s
  the nurse, 2020 some of the wealthy got paid); priority lane + yacht IN; AI coda with no ownership
  line; never "short-sighted".
- 29 Sept: pre-1957 Crown films usable, picture only; no £170 spend; no photo of Baroness Mone,
  newspaper headlines instead; agents may read paid sites in a browser; narration is **scored in
  Suno**, minimal and documentary, **English narrator**; the film should get shorter; several Suno
  takes are fine.

## Next moves, in the order recommended

1. **Suno round 1** (`songs/narration.md` §4): part 1 six ways — palettes A felt piano / B English
   pastoral / C colliery brass, each with and without the `badcode newsreader` Voice. Kai picks by ear.
   Record or listen only when Kai asks.
2. **Kai edits the words**, using §6's trims (≈1.5 min saved). Mirror changes into `storyboard.md`.
3. **Premiere**: create `magic-money-tree.prproj`, then `edit-plan.md` §9, after its §6 prerequisites
   (cards rendered by ffmpeg, debt chart, bank diagram, Flow plates approved by Kai, three screenshots,
   the 1948 pamphlet).

## Still owed

- 🔴 **Legal read + fact re-check of scene 11a** before narrating (part P8) or cutting it. Say £122m,
  never "fraud", never "Tory peer" as current.
- Kai rulings: Question Time as clip or cards · "People have tried" vs "Nobody ever has" · "I would know."
- Verify at source: both 1942 Keynes quotations, post-war debt/unemployment figures, the 1944 tax rates.
- Not pushed to the remote; commit only.
