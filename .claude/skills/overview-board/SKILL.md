---
name: overview-board
description: Use to run a BadCode film at the level of the WHOLE STORY — set up its skeleton (every scene or sequence in film order, with the beat each must land), keep the overview board that shows the film start to end with each part's state and timeline page, say where the film stands and what to open next, and hand any one part to new-scene to make or re-cut. The story-level layer above new-scene's scene timelines. Triggers on "overview board", "set up the film", "skeleton for <story>", "lay out the whole story", "what's the running order", "where are we on the film", "which timeline do I open", "add a scene to the film", "move/split/merge/cut a scene", "let's work on <scene>", "the whole film start to end".
---

# Overview board (BadCode)

The overview board is **the whole film on one page**: every part in film order, the beat each part must
land, its state, the timeline page to open, and every earlier page under it. It is the top level of
the scene editor we have built out of skills:

```
overview-board   the film       timelines.json → overview page        (this skill)
   └─ new-scene  one part       brief → mood board → storyboard → clips → TIMELINE PAGE
        └─ provenance           recipe cards, trail.json, final.json  (docs/provenance/README.md)
```

Kai, 2026-10-23: *"initialise the skeleton shape of a whole story and then go into each scene and edit the
scene's timeline."* Worked example: GPOM, https://claude.ai/artifact/AXJqmgAWTRhxK7fzMkKukp

## Read first

- `docs/provenance/README.md`, the overview board section: the file and the builder.
- The story's canon: `docs/stories/<story>/README.md` and `story.md`. A restructure note, if there is one, wins.
- **`story-craft`** when laying out the skeleton: every part is a step in the argument (but/therefore). Write the ending first.

## The file and the page

| What | Where |
| --- | --- |
| The running order | `docs/stories/<story>/timelines.json` |
| The page | `docs/stories/<story>/timelines/index.html`, built by `python3 scripts/provenance/build-timelines.py docs/stories/<story>` |
| The link | `timelines.json` `url`, **and at the top of the story's `README.md`** |

`timelines.json`:

```json
{
 "story": "<story>", "title": "<Story Title>", "url": "<artifact url once published>",
 "updated": "YYYY-MM-DD", "open_now": "<section or part id>",
 "intro": "One line saying what the page is for.",
 "sections": [
  {"id": "door", "group": "Part 2 · The humans", "name": "B · At the door",
   "beat": "What this part must land, in one sentence (from the canon).",
   "at": "4:10", "length": "about 2:00",
   "state": "not made", "tone": "gap",
   "scene": "scenes/<scene>",
   "timeline": "<current timeline page url>",
   "premiere": "<project> · sequence <name>",
   "what": "Where it stands right now, in plain words.",
   "history": [{"name": "Cut 2 timeline", "url": "...", "kind": "timeline", "date": "YYYY-MM-DD"}],
   "parts": [ /* same shape, one level deep: a reel and the scenes in it, or a track and its sections */ ]}
 ]
}
```

- `tone` colours the state chip: `gap` (red, not made), `wip` (amber, being worked on), `ok` (green), `premiere` (green, cut by hand in Premiere).
- `group` makes the page's headings. Consecutive sections with the same group sit together.
- The builder fills in a section from its `scene` folder **by itself**: the timeline link from `scene.json` `boards`, every published round from `trail.json` (as earlier pages), and a "recipe frozen" badge when `final.json` exists. So for a new-scene part, you mostly keep `state` and `what` current.
- A part that exists only in Premiere, or doesn't exist yet, **still gets a row**. The gaps are the point.

### The Premiere map (Kai, 2026-10-26)

*"For a given story, we need to always have a coherent map of what timeline artifacts are currently managing
our script and what Premiere sequences each timeline maps onto."* The board opens with it, built by itself:

- **One row per timeline page:** the page, the **current sequence** it drives, whether they still match
  (`in sync` / `page ahead` / `edited in Pr`, from `scripts/scene/premiere-check.py --write`), and the older
  sequences it replaced. All of it comes from each scene's `scene.json` `premiere` record (`current` plus one
  record per build; the shape is in `scene-timeline`, "Premiere sync"). A reel page lists its parts' sequences.
- **Every other sequence in the project**, in `timelines.json` → `"premiere": {"project": "…", "other":
  [{"sequence": "…", "what": "Kai's hand cut | replaced by … | a test, safe to delete | unknown to Claude"}]}`.
  Every sequence in the project is either on a row or in `other`. When `premiere_list_sequences` shows one
  that's in neither, add it, and say "unknown to Claude" rather than guess.
- **The open tabs follow the map:** Kai's own cuts and each page's current sequence, in film order, and
  nothing else (`scene-timeline`, "Tabs show the film").
- The section's own `"premiere": "<project> · sequence <name>"` string is only for parts with no timeline page
  (Kai's own cuts).

## Modes

### 1. Skeleton: lay out a new film

1. **Read the canon** and propose the running order: parts in film order, each with a one-sentence `beat`, a rough length, and the part of the film it sits in (`group`). Fixed music sets the timecodes.
2. **Talk it through** one or two questions at a time. Kai's best structure notes come from cutting, not adding. Push for every part to change something; name the ending first.
3. **On Kai's yes:** write `timelines.json` with every part `"state": "not made", "tone": "gap"`, plus a planned `scene` folder name for each part that will be made the new-scene way. Don't create the scene folders; new-scene does that.
4. **Build and publish** the page (below). Put the link in `timelines.json` and at the top of the story README.

### 2. Status: where are we, what do I open

Read `timelines.json`, then each part's `trail.json` and `cut-notes.json`, and answer in the board's usual format:
what is on a timeline, what is in Premiere, what is not made, and **which one to open now** (`open_now`).
Read the live page first if another session may have changed it (`Artifact read`); merge any newer state into the file.

### 3. Go into a part

"Let's work on <part>": hand over to **`new-scene`** with the part's `scene` folder and its `beat` as the
starting sentence for stage 1. When new-scene publishes that part's first timeline page, set the part's
`state`/`tone`, make it `open_now` if Kai is noting it, rebuild, republish.

### 4. Reshape the film

Add, cut, split, merge or move parts in `timelines.json`. Never delete history: a cut part keeps its row,
with state `cut` and its pages under `history`, until Kai says to drop it. A merged part takes both parts'
history. Rebuild and republish.

### 5. Keep it current (every time a part changes)

Whenever a timeline page is made, changes state, or is replaced:
1. Edit `timelines.json`: `state`, `tone`, `what`, `open_now`, `updated`. When a page is replaced, move the old link into `history`. When a Premiere sequence is built, read every current one and run `premiere-check.py --write` so the map is fresh.
2. `python3 scripts/provenance/build-timelines.py docs/stories/<story>`
3. Publish `timelines/index.html` with `url` set to the `url` in `timelines.json`. **Same link, every time.**

## Publishing

First publish: run `Artifact quickstart` (intent `other`), then publish `timelines/index.html` with an icon
like `map` and a one-line description, and record the URL. After that, always republish to that URL.
The page is read-only: Kai and Jack never type into it, they tell Claude. Notes belong on the scene timeline pages.
The board is also **the decision log**: each earlier page shows the decisions logged against it (`prov.py trail --decided`).
Like every page, it is only a window; `timelines.json` and the scene trails are the record (docs/provenance, "Artifacts are the UI").

## Replies

House output style. Lead with the state of the whole film in one line (the page's count line: parts, on a
timeline, in Premiere, not made), then the one part to open now, and the link.
