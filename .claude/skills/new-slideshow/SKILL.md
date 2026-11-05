---
name: new-slideshow
description: Use to make a BadCode MEME SLIDESHOW: a talk that works as a website, a video and a live stage show ("ten minutes, a projector, one meme after another"). Runs brief → research → script (deck.md) → reading page → the deck's own look (picking page) → dress every slide in that look (slides.json + three.js diagrams) → a playable PREVIEW page with Keep/Change/Cut and a note on every slide → rounds on the notes → pictures → recording. Holds the deck folder layout, the meme rules and the tools in scripts/slideshow/. Triggers on "new slideshow", "meme deck", "make a talk / a presentation / slides for…", "slideshow for <story>", "preview the deck", "read my slide notes", "next round of the deck", "add a slide", "explain <idea> with memes".
---

# New slideshow: the meme talk (BadCode)

**One talk, three outputs:** a page people click through, a video (the narrator voices it), and
Kai on a stage with a projector. Kai, 2026-11-05: *"given ten minutes on a stage and a projector, I
could just show one meme after the other whilst making a point."* If an obvious diagram explains
the concept, use it, **then follow it with a meme**, because people love memes and they're funny.

First made for Future Proof's launch talk
(`docs/stories/future-proof/slideshows/launch-talk/`), which is the worked example for every stage
below. Like `new-scene`, it is gated: **talk → approve → produce**, and each stage has its own page.

```
1 brief       what the talk argues, for whom, how long, where it plays     → brief (in chat or brief.md)
2 research    canon readers + web researchers → synthesis → adversarial critic → fact-check
3 script      deck.md: every slide's On-screen / Visual / Say / Source        │ reading page, Kai notes
4 look        4 genuinely different looks, live samples, picking page         │ Kai (and Jack) pick
5 dress       slides.json in the look + three.js diagram scenes, self-shot
6 preview     preview.html: the real slideshow, Keep/Change/Cut + note per slide │ Kai notes
7 rounds      dump notes → answer each → rebuild → republish same link (repeat 6-7)
8 pictures    cast the recurring character (approval) → Flow stills per slot → assets
9 deliver     voice (sound.md) → record video → shorts → website route
```

## Read first

- `docs/marketing/the-reader.md` (who it is for) and `docs/voice.md` (how the narrator sounds).
- The story's canon, and its **`look.md` / `sound.md`** (no house look: a deck's look is the story's).
- `docs/using-ai.md` before any public copy that mentions AI.
- The worked example's `deck.md` (format), `theme/LAYOUTS.md` (a layout catalogue) and `slides.json`.

## The deck folder

`docs/stories/<story>/slideshows/<deck>/`:

| file | what | who writes it |
| --- | --- | --- |
| `deck.md` | the script, source of truth for WORDS: rules, the recurring character, every slide `### N · meme\|diagram (three.js)\|title · Ns` with `- **Visual:**` `- **On-screen:**` `- **Say:**` `- **Source:**`, appendix `### A1 · meme · "question"`, fact ledger, legal, timing, open flags | stage 3, then rounds |
| `slides.json` | how each slide is DRAWN in this deck's look: `{title, round, slides:[{id, layout, …fields}]}` | stage 5, then rounds |
| `theme/` | the deck's look: `head.html` (fonts), `theme.css`, `layouts.js`, `scenes/_common.js` + one file per three.js scene, `LAYOUTS.md` (field reference) | stage 4-5 |
| `images/` | `manifest.json` (`{"file.jpg": "<artifact asset url>"}`) + recipe cards; the media itself lives on D: (provenance) | stage 8 |
| `feedback/<date>-<what>/` | every db dump from every page, BEFORE it is acted on | every round |
| `preview.html`, `reading.html` | built pages (rebuild, never hand-edit) | `build.py` |

## Tools (`scripts/slideshow/`)

- `python3 scripts/slideshow/build.py <deck-folder>`: parses `deck.md`, merges `slides.json` and the theme into the generic engine (`engine.template.html`), writes `preview.html` and `reading.html`. Lists slides with no layout yet (drawn as a fallback box). Fails without a `theme/` on purpose.
- `node scripts/slideshow/shoot.mjs <preview.html> <outdir> <id>[:clicks] …`: headless screenshots, one fresh page per shot, prints page errors and empty stages. Needs `SHOOT_CHROME=$(ls ~/.cache/ms-playwright/chromium_headless_shell-1234/*/chrome-headless-shell)` and `TMPDIR=$HOME/.cache/pw-tmp` (Playwright's pinned browser may be missing; `/tmp` is sandboxed).
- The engine: 1600×900 stage scaled to fit; → / space / click advance (clicks inside a slide step through `reveal` and scene steps first); G grid of every slide with marks; N notes drawer (the Say line, the picture brief, Keep/Change/Cut, a note, other readers' notes); H hides the bar (for recording); F full screen; `#s-<id>` deep-links a slide. Notes live in the page's `db` collection `notes`, one doc per reader `{slides:{id:{v,n}}, round}`.
- Publish both pages with `capabilities: {db: {rules: [{path:"notes",read:"view",write:"owner"},{path:"notes/{self}",write:"interact"}]}, user: {scopes:["profile"]}}`. Republish the SAME file path each round (same link). Pages are private: tell Kai to share with Jack.

## The meme rules (load-bearing)

1. **Meme-laden.** At least four memes per diagram; every diagram is followed at once by a meme that lands its joke. A meme slide is 5-11 seconds; the punchline lands in the last two.
2. **Our own images in meme grammar.** Borrow layouts (two buttons, no/yes, receipt, label, error box); never a copied still, a known template character, a logo or a real person's face (UK s30A parody is narrow: research/19 of the Future Proof deck). Every picture is generated fresh, with a recipe card.
3. **The audience is never the butt.** The joke lands on the design or on a decision-maker named by their act. One recurring invented character (Future Proof: Mel) is the one who noticed, never the fool.
4. **Every fact has a source and a status** in the deck's fact ledger (OK / CHECK / CUT-IF / GATE). A fact-check agent opens the URLs before the preview; anything unverified is hedged, gated or cut. No invented numbers, ever.
5. **Spoken lines work from a human mouth** (Kai on stage) and from the narrator (the AI from the future, `docs/voice.md`). No "on the left you can see".
6. **Reader traps** (`the-reader.md`): no smugness, no "you've been duped", no party fight; name decision-makers, not technology.

## Stages

1. **Brief.** One or two questions at a time: the one sentence the talk argues, the reader, the length, where it plays, the opening line, who speaks. Don't start research without the opening and the length.
2. **Research** (only if Kai asks for agents, or it is plainly needed). A workflow: canon readers (the story's docs) + web researchers (precedents, existing memes and analogies, explainer-video craft, legal, the audience's humour), each writing one file in `design/<date>-<deck>/research/` with every claim marked by source and solidity; then a synthesis (a slide outline) and an adversarial critic against the reader and voice rules. Watch the session's web-search budget (~8 searches per agent). Synthesisers tend to work from summaries: the fact-check is not optional.
3. **Script.** Write `deck.md` in the format above (copy the worked example's sections). Rules section, recurring character, slides, appendix (one-slide answers to the questions a hall will ask), fact ledger, legal column, timing/cuts/shorts, open flags. Then a fact-check agent (opens sources, fixes the deck, writes `deck-<n>-factcheck.md`). Build and publish `reading.html`; Kai marks Keep/Change/Cut per slide.
4. **Look.** If the story's `look.md` has no slideshow look: a picking page of four genuinely different looks grounded in the talk's subject (frontend-design), each showing the SAME three slides (title, one meme, one live diagram), with what it serves and what it undermines, plus a vote and a note per look (db). Future Proof's options: Museum of Old Tech / **Update Available** (picked) / Bundle Deal / Building Site. Dump the votes to `feedback/`, then write the pick into the story's `look.md` and build `theme/` from it.
5. **Dress.** Write `theme/LAYOUTS.md` (the look's layouts and fields) and `layouts.js` first, prove two slides (one meme, one diagram) with `shoot.mjs`, then fan out: agents write `slides.json` parts by section and agents write the diagram scenes, each checking their own work with screenshots in a scratch copy of the deck. Merge the parts, build, shoot a sample of every layout yourself.
6. **Preview.** Publish `preview.html` (same link every round; Future Proof's: https://claude.ai/artifact/LNreQcESnsdmBZD1HVEaCB). Tell Kai: arrows to step, G for the grid, N for notes.
7. **Rounds.** *A big cut* ("far too long", "make it funnier"): don't trim, rewrite by options, like `scene-dialogue`. Six writers each push ONE comic shape to its extreme (Future Proof's: one running installer gag, a character's day, ruthless minimum, stand-up set, patch notes, the support call), a harsh judge scores them (funny / simple / structure / the look's gag paying off / reader rules) and names the spine and the best 15 lines, one writer combines them into the new `deck.md` (old one to `history/`), a dresser redraws `slides.json`. Round 1→2 of Future Proof went 8:41 → 3:17 this way. *Ordinary notes:* `ArtifactData list` on `notes` with `out_dir` = `<deck>/feedback/<date>-round-<N>/`, read the files, answer every note (change `deck.md` for words, `slides.json` for drawing, the theme for the look), bump `round`, rebuild, re-shoot what changed, republish. Log each ruling in `<deck>/trail.md` (date, round, note, decision).
8. **Pictures.** Cast the recurring character first (stills are free; Kai approves the casting before any slot is filled, and before anything is animated). Then one Flow still per image slot (`new-image`, the story's `look.md`, `flow-prompt`; the same-prompt check runs on every prompt), a recipe card each, upload to the preview artifact's asset store (declare `assets`), record the URL in `images/manifest.json`, rebuild.
9. **Deliver.** The narrator voice per the story's `sound.md` (AI Studio). Video: record the preview with the bar hidden (H), stepping on the voice's timings, or OBS. Shorts: the deck's "shorts" list, 9:16. Website: `build.py <deck> --public <out.html> --home <url>` writes the public copy (no notes, no picture briefs, main slides only, a "Back" link when opened on its own); Future Proof's plays inside the TV on GOVT 2 (`apps/site/README.md`, "The Future Proof talk"). Since 2026-11-05 a push to main that touches `apps/site/**` deploys itself (`.github/workflows/site-deploy.yml`), so regenerate the public copy, commit, push, and it is live in about a minute. *Not built yet (2026-11-05): automatic recording, a 9:16 stage mode. Build them when the deck is signed off, and update this list.*
