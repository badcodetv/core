---
name: story-style
description: Use to FIND a story's own look and sound and write them into its docs/stories/<story>/look.md and sound.md — an interview that starts from the story (what it argues, who it is for, how the end should feel), then proposes genuinely different looks and sounds from a wide style library plus at least one invented for this story, shows them on a picking page (a test still per look, references per sound), runs rounds on Kai's and Jack's votes, and locks the pick. Runs inside new-story, or alone. Triggers on "find the look for <story>", "what should <story> look / sound like", "style interview", "bootstrap look.md / sound.md", "this story has no look yet", "the look isn't working, start again", "story style".
---

# Story style: find this story's look and sound

**Why this exists** (Kai, 2026-10-28). What every session loads ends up in every prompt: one story's
dark register and drum & bass became every story's, and 400+ Bank Robbery takes came out in one
voice. So BadCode has **no house style** (`docs/stories/STYLE.md`). But each story *does* need a
strong identity, obvious in every still, clip and track it makes. That identity is decided once,
here, deliberately, and written into the story's own `look.md` and `sound.md`, which only that
story's work reads.

**The library.** `docs/style-library/` is a wide menu (looks and sounds, one file each, saying
what each serves *and* what it would undermine). **Only this skill reads it.** It is a menu, never a
default: the story comes first, and the library is opened only after the interview.

**You don't pick.** You ask, research, propose spread-out options and run the page. Kai or Jack
picks. Your own taste is a default in disguise: when two options feel like "the obvious one",
that is the signal to swap one out.

## The round folder

`docs/stories/<story>/style/` (a mini scene folder, so the provenance tools work):

| File | What |
| --- | --- |
| `scene.json` | `{"scene": "style", "title": "<Story> style", "media": "/mnt/d/badcode-videos/<story>/style"}` |
| `interview.md` | the questions and the answers, **verbatim**, newest round at the top |
| `round-<n>/options.json` | the options shown (format in `scripts/story-style/build-page.py`) |
| `round-<n>/variations/` | the `variations` round that wrote the test-still prompts |
| `trail.json`, `feedback/` | written by `scripts/provenance/prov.py`, as for any page |

Test stills go to `<media>/round-<n>/<id>.jpg`.

## 1. The interview: story first

One or two questions at a time, in plain words; write each answer into `interview.md` as it
comes. Read the story's `README.md` / `story.md` first and don't ask what they already answer.

1. **The argument.** The one sentence the story argues, and the costed object that carries it.
2. **The reader and the end.** Who it's for, and what they should *feel* walking away (not think).
3. **The world.** Where and when it happens: real, period, invented? Whose eyes is it seen through?
4. **The form.** Film with narration, music video, comic, song only? A sung song, a score, a
   narration bed, character voices? Roughly how long? (This decides what the sound must do.)
5. **Taste, by example.** Three things in *any* medium that feel like this story, and one thing it
   must never look or sound like. Ask Jack's view too, if he isn't the one in the session.
6. **The constraints.** Recurring characters who must stay the same, talking heads or lip-sync,
   real footage to cut with, anything that rules a style out on cost.

Then say back the story in five lines (these become the page's "The story" section) and get a yes.

## 2. Research: from the story, then the library

1. **The story's own world first.** If it has a period, place or subculture, run 2 to 4
   `general-purpose` research subagents in one message (≤ 6 web searches each; the session budget
   is shared): what did that world look and sound like, and what did the art *about* it look and
   sound like? This is where the off-library option usually comes from.
2. **Then the library.** Read `docs/style-library/README.md` (one line per style and its *Used by*
   column), then open the 10–15 most promising entries.
3. **The shortlist: 6 to 8 looks and 6 to 8 sounds.** Rules, all of them:
   - **at least three different families** in each list;
   - **at least one off the library**, invented for this story (often a hybrid from step 1);
   - **at least one against the grain**: the option a reader wouldn't expect for this subject;
   - **no style another story already uses** (the *Used by* column) unless Kai or Jack asks for it;
   - each option names what it **risks** for this story, honestly (the library entry's
     "would undermine" line is the place to start).

## 3. Show it

1. **Looks: one test still each, of the same moment.** Pick one beat from the story (the key
   image) and write it as `subject.md`. Make a `variations` round of kind `flow` in
   `round-<n>/variations/` with `ask.md` = the shortlist's look list verbatim, `subject.md`, and
   **write `writers/ideas.json` yourself from the shortlist** (one idea per look: its name and its
   pitch, with the library entry's traits pasted in) instead of spawning the ideas writer. Then
   follow the `variations` loop from `round.py asks`: separate writers, the gate, then one
   `flow_generate_image` per prompt, verbatim, count 1. Stills are free.
2. **Sounds: words and references, no Suno.** For each, two or three real reference tracks (with
   links) and a rough Suno Style-box sketch. Suno takes cost credits and pull the ear toward the
   first decent take: test only after a pick, or if Kai or Jack asks.
3. **The page.** Write `round-<n>/options.json`, then
   `python3 scripts/story-style/build-page.py docs/stories/<story>/style/round-<n> <scratchpad>/<story>-style.html`
   and publish it with `capabilities: {db:{}, user:{}}`, republishing to the same file path every
   round. Log it: `python3 scripts/provenance/prov.py trail docs/stories/<story>/style --stage other --round <n> --url <url> --what "style round <n>: <k> looks, <k> sounds" --rebuild "<the build command>"`.

## 4. Rounds

Dump the page's `votes` and `notes` into the repo before reading them (`ArtifactData list`, with
`out_dir` = `python3 scripts/provenance/prov.py feedback-dir docs/stories/<story>/style --stage other --round <n>`),
and log the decisions with `prov.py trail … --feedback --decided "<their words>"`. Round 2 narrows:
the "This" and "Maybe" picks, the combinations the notes ask for, and one new wildcard each side so
the round doesn't collapse onto a single idea. Usually two or three rounds.

## 5. Write it back

When a look and a sound are picked, fill the story's `look.md` and `sound.md` from the templates
in `docs/stories/STYLE.md`:

- **Copy, don't link.** Put the traits, palette, light, lens, preamble, instruments, voice and
  rules this story needs into its own file, adapted to it. A later edit to the library must never
  change a story that has already picked.
- Under *In one paragraph*, add a line `**Library:** \`<slug>\`, \`<slug>\`` (or `off the library`).
  Then `python3 scripts/story-style/library.py index` updates the *Used by* column.
- **Status:**
  - **LOCKED** once there's a still Kai or Jack calls "that's it" and a preamble that reproduces it.
  - **EXPLORING** while it's a direction without a proven prompt. The next `new-image` /
    `suno-prompt` work then runs a `variations` round inside it and locks it.
- **Anchors:** the picked test still (path + Flow media id). **History:** every option shown and why
  it lost, with a link to the page.

## Never

- Never open the library before the interview, and never show options before the five-line story
  is agreed.
- Never seed a story from another story's `look.md` / `sound.md`, and never call a style
  "BadCode's".
- Never point any other skill, CLAUDE.md or memory at `docs/style-library/` (`scripts/style-lint.py`
  fails). A story's style reaches other work only through that story's own files.
- Never write the test-still prompts yourself; the `variations` writers do.
