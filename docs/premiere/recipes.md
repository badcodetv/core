# Premiere recipes — how to actually do the thing

Concrete tool-call sequences for the jobs that come up. **This is the file to open when someone
says "put these clips in Premiere and…".**

- What tools exist and what they take: [`packages/premiere-mcp/README.md`](../../packages/premiere-mcp/README.md)
- Which effect to reach for: [`effects-catalogue.md`](./effects-catalogue.md)
- Why the API behaves oddly: [`api-notes.md`](./api-notes.md)
- Getting the bridge running at all: [`setup.md`](./setup.md) and the `premiere-automation` skill

Every snippet below is a real tool call. Arguments are shown as JSON.

---

## The five rules that make everything else work

1. **`premiere_status` first, every session.** It is the only tool that runs without config.
2. **🔴 Every edit tool acts on the ACTIVE sequence, and it takes no sequence argument.**
   `premiere_set_active` before a run of edits, and **read `sequence.name` on every response** to
   confirm the work went where you meant. A human clicking a different tab in Premiere silently
   redirects your next call.
3. **Refs go stale.** `v0:2` means "third clip on video track 0 **in the state that produced it**".
   Use the newest state; never a cached ref.
4. **Look before you claim.** `premiere_export_frame` then read the PNG. A timeline whose numbers
   are right can still look wrong, and you cannot see the program monitor.
5. **Never guess a match name.** `premiere_list_effects` / `premiere_list_transitions` first.

And one for working alongside a person: **do not drive Premiere while a human is using it.** The
bridge serialises the panel, not the person at the keyboard.

---

## Reading a timeline without drowning

A real cut is far too big to return whole — Jack's camping project is 573 KB of state. So
`premiere_get_sequence` **summarises by default** and you ask for detail.

```jsonc
// The digest: every track, one line each. ~1.8 KB however big the edit.
premiere_get_sequence({})

// One track's clips in full, with every effect parameter.
premiere_get_sequence({ tracks: ["V1"] })     // UI label
premiere_get_sequence({ tracks: ["v0"] })     // API index — same track

// Just what plays in a window, across all tracks.
premiere_get_sequence({ range: [10, 30] })

// Named clips, expanded.
premiere_get_sequence({ clips: ["v0:2", "a0:0"] })

// Arrangement only, skip reading parameters from Premiere at all (faster on a graded cut).
premiere_get_sequence({ params: false })
```

🟢 **The complete state is always written to disk** at the returned `statePath`
(`<project dir>/.bridge/state-<sequence>.json`). **`jq` over that file for anything bulk** —
counting, searching, auditing a whole cut. It costs zero context and it is untrimmed.

```sh
# every clip on V3, as a table
jq -r '.videoTracks[2].items[] | "\(.ref)\t\(.start)\t\(.name)"' "<statePath>"

# which source files does this cut use, and how often
jq -r '[.videoTracks[].items[]] | group_by(.mediaPath) | map({f:.[0].mediaPath, n:length}) | sort_by(-.n)[] | "\(.n)\t\(.f)"' "<statePath>"

# anything offline: paths the project claims that are not on disk
jq -r '[.videoTracks[].items[],.audioTracks[].items[]] | map(.mediaPath) | unique[]' "<statePath>" \
  | while read -r p; do [ -e "$p" ] || echo "MISSING: $p"; done
```

If a response would still be too large it degrades a rung at a time — parameters, then effect
chains, then markers, then clip lists — and `notes` says exactly what went and which narrower call
would have kept it.

---

## Recipe: build a cut from a folder of clips

The bread and butter. Import, make a sequence that matches the footage, lay the shots.

```jsonc
// 1. Open the project (any path, no media root needed)
premiere_open_project({ path: "/mnt/d/badcode-videos/gitpush-origin-master/gpom-story.prproj" })

// 2. Import into a named bin
premiere_import({
  paths: ["/mnt/d/.../s01-earth.mp4", "/mnt/d/.../s02-hong-kong.mp4"],
  bin: "s01"
})

// 3. Make the sequence — pick ONE of these
premiere_create_sequence({ name: "s01", fromItems: ["s01-earth.mp4"] })   // match the footage
premiere_create_sequence({ name: "s01", preset: "/mnt/c/Program Files/Adobe/Adobe Premiere Pro 2026/Settings/SequencePresets/HD 1080p/HD 1080p 25 fps.sqpreset" })

// 4. Lay the shots at known positions
premiere_insert_clip({ item: "s01-earth.mp4",     time: 0,    mode: "overwrite", videoTrack: 0 })
premiere_insert_clip({ item: "s02-hong-kong.mp4", time: 56,   mode: "overwrite", videoTrack: 0 })

// 5. Narration on A1
premiere_insert_clip({ item: "narration.wav", time: 0, mode: "overwrite", audioTrack: 0 })
```

🔴 **`create_sequence({name})` with neither `fromItems` nor `preset` uses the PROJECT DEFAULT**,
which on this machine is 1920×1080 @ 23.976 — almost never what you want. Proven with pixels: the
first frame exported through the bridge showed the picture inset in black because a 1280×720 @ 25
source sat in a 1080p/23.976 sequence.

**`overwrite` vs `insert`:** `overwrite` drops the clip in place, replacing what is under it — use
it when laying shots at known positions. `insert` splices and **pushes everything after it later on
that track** — use it when adding a shot into an existing cut.

🟢 **`changed.added` tells you the ref of the clip you just made.** The panel returns a timeline,
never a receipt, so the server diffs against the previous state. Read the ref from there rather
than re-scanning the track.

### Placing the next shot at the end of the last one

**Do not compute it from `ffprobe`.** Premiere conforms a clip to the sequence's frame grid on
insert — 27.834s of 24fps footage became exactly **27.8s** (695 frames) in a 25fps sequence. Read
the real `end` from the returned state and use that as the next `time`.

---

## Recipe: fill the frame when the source is smaller

A 1280×720 clip in a 1920×1080 sequence renders **inset in black on all sides**. Scale it with the
Motion intrinsic — no `apply_effect` needed, Motion is already on every clip as component 1.

```jsonc
premiere_set_param({ clip: "v0:0", component: 1, param: 1, value: 150 })
```

`150` because 1920/1280 and 1080/720 are both exactly 1.5. Motion's param 3 is Uniform Scale
(display name is a single space) and defaults to `true`, so setting Scale alone drives both axes.

**Then look at it** — `premiere_export_frame({ time: 10 })` and read the PNG. This recipe was
verified that way, twice.

---

## Recipe: a push-in, a pan, a fade

All keyframing goes through `premiere_set_param` with a `time`. Call it twice at two times to get a
move.

```jsonc
// Slow push in: Scale 100 → 115 over two seconds, eased
premiere_set_param({ clip: "v0:0", component: 1, param: 1, value: 100, time: 0 })
premiere_set_param({ clip: "v0:0", component: 1, param: 1, value: 115, time: 2, interpolation: "bezier" })

// Drift left to right: Position is a 0–1 FRACTION of the frame, not pixels
premiere_set_param({ clip: "v0:0", component: 1, param: 0, value: {x: 0.45, y: 0.5}, time: 0 })
premiere_set_param({ clip: "v0:0", component: 1, param: 0, value: {x: 0.55, y: 0.5}, time: 4, interpolation: "linear" })

// Fade up from black: Opacity is component 0, param 0
premiere_set_param({ clip: "v0:0", component: 0, param: 0, value: 0,   time: 0 })
premiere_set_param({ clip: "v0:0", component: 0, param: 0, value: 100, time: 1, interpolation: "bezier" })
```

`interpolation` is `"linear"` (constant rate), `"bezier"` (ease) or `"hold"` (snap). Every Motion
and Opacity param reports `areKeyframesSupported() === true`.

⚠️ **A `set_param` returns an empty `changed`** — the diff compares clip *times*, and the clip did
not move. That is correct, not a failure. To confirm a value landed, read it back with
`premiere_get_sequence({ clips: ["v0:0"] })` or export a frame.

---

## Recipe: dissolves and cuts that land

```jsonc
// Always list first — match names mix prefixes with no pattern
premiere_list_transitions({ query: "dissolve" })

// A transition belongs to a CLIP EDGE, not to a cut. Add it once, from either side.
premiere_add_transition({ clip: "v0:0", matchName: "AE.ADBE Cross Dissolve New", at: "end", duration: 1 })
```

The ones worth knowing: `AE.ADBE Cross Dissolve New` · `AE.ADBE Dip To Black` ·
`AE.AE_Impact_Luma_Fade` (dissolves into the black — the BadCode register) · `AE.AE_Impact_Flash`
(cheapest way to land a cut on a beat).

🔴 **No handles is NOT a refusal.** A clip used to its full source length has nothing to dissolve
into, and Premiere takes the transition anyway — writing a **single-sided frame-hold**. It will
also happily put one across a *gap*. If a dissolve must be genuinely two-sided, trim both clips
shorter than their source first, then add it.

🔴 **You cannot read a transition back.** `getTrackItems()` returns `null` for every non-CLIP item,
so `SequenceState` reports a per-track `transitionCount` and nothing else — no match name, no
position, no duration. `add_transition` verifies itself by comparing that count before and after.
If you genuinely need to know what transitions a hand-cut project contains, the `.prproj` is
gzipped XML and carries them in full (`zcat`), at the cost of forcing a save.

🔴 **There is no audio transition API at all.** Audio crossfades are manual.

---

## Recipe: grade it

```jsonc
premiere_apply_effect({ clip: "v0:0", matchName: "AE.ADBE Lumetri", params: { "19": -0.5, "20": 15 } })
```

Lumetri's readable indices — **the index is the address**, because `Saturation`, `Intensity`,
`Look` and `Input LUT` each appear **twice** at different indices:

| Index | Param | | Index | Param |
| --- | --- | --- | --- | --- |
| 11 | Intensity (Basic) | | 23 | Whites |
| 14 | Temperature | | 24 | Blacks |
| 15 | Tint | | 38 | Intensity (Creative) |
| 16 | Saturation (Basic) | | 40 | Faded Film |
| 19 | **Exposure** | | 41 | Sharpen |
| 20 | **Contrast** | | 42 | Vibrance |
| 21 | Highlights | | 43 | Saturation (Creative) |
| 22 | Shadows | | 45 | Tint Balance |

🔴 **33 of Lumetri's 130 params cannot be READ by any route** — `getValueAtTime` throws,
`getKeyframePtr` returns null or throws, `getStartValue` returns null. They come back with
`unreadable: true` and `value: null`. **They can still be written.** Do not treat an unreadable
param as a failure.

⚠️ **`apply_effect` is TWO undo entries, not one.** Premiere cannot address an effect's parameters
until the effect itself has committed, so the append and the parameter sets are separate
transactions. This is a hard API constraint, not a choice.

---

## Recipe: the BadCode near-black look

Vignette plus grain over a Lumetri base is the house grade.

```jsonc
premiere_list_effects({ query: "vignette" })   // → AE.Impact_Vignette_FX
premiere_apply_effect({ clip: "v0:0", matchName: "AE.Impact_Vignette_FX" })
premiere_describe_effect({ clip: "v0:0", component: "Vignette" })   // learn its indices, then set them

premiere_list_effects({ query: "noise" })      // → AE.ADBE_Noise_FX
premiere_apply_effect({ clip: "v0:0", matchName: "AE.ADBE_Noise_FX" })
```

🔴 **`premiere_describe_effect` REQUIRES a clip.** An un-inserted effect object has **no methods at
all** — its prototype is a bare `constructor`. There is no way to ask "what settings does this
effect have" without applying it to something first.

Then, always: `premiere_export_frame` and look.

---

## Recipe: fire, smoke, sparks — the free route

**We own no VFX plugins and are not buying any.** The house answer:

1. Generate the element in **Flow**, prompted on a **pure black background** (see the `flow-prompt`
   skill and `docs/flow/`).
2. `premiere_import` it and `premiere_insert_clip` it on a track **above** the plate
   (`videoTrack: 1` is V2).
3. Key the black out with **Luma Key** (`AE.ADBE Legacy Key Luma`) or **Extract**
   (`PR.ADBE Extract`).
4. Soften the edge with **Edge Feather** (`AE.ADBE Edge Feather`) if it reads as cut out.

⚠️ **Blend modes are not currently reachable by number.** They live on the Opacity intrinsic as two
params both named `Blend Mode` (indices 1 and 2), and the API exposes **no way to enumerate the
options** — a live probe found no `getOptions`, `getEnumValues` or range accessor of any kind. The
integer for Screen has not been measured. **Key instead of blending** until someone runs the sweep
(see the Open questions in `effects-catalogue.md`), and run that sweep **in a scratch project**.

Stock-element libraries (Mixkit, Pexels, Videvo — free tiers) are the fallback if Flow will not
produce it.

---

## Recipe: text on screen without a template

🟢 `AE.ADBE PPro SimpleText` is an ordinary effect, so it applies and sets like any other — no
MOGRT, no Essential Graphics, no unresolved API question.

```jsonc
premiere_apply_effect({ clip: "v0:0", matchName: "AE.ADBE PPro SimpleText" })
premiere_describe_effect({ clip: "v0:0", component: "Simple Text" })   // dump its params, then set them
```

Its parameter list has not been recorded yet — **describe it once and write the indices into
[`effects-catalogue.md`](./effects-catalogue.md)** so the next session does not pay again.

For animated/templated type, the `AE.AE_Impact_Typewriter` and `AE.AE_Impact_Text_Animator`
*transitions* are free and installed. Full MOGRT parameter automation is still an open question
(T11).

---

## Recipe: leave a note for the human inside Premiere

Markers are the way to say something at a timecode rather than only in chat.

```jsonc
premiere_add_marker({ name: "beat", time: 12.5, comments: "cut lands a frame late here" })
premiere_set_playhead({ time: 12.5 })   // moves the program monitor so they see it
```

Markers read back in full (name, start, duration, comments) in every state — one of the few parts
of the API with no marshalling trouble. `set_playhead` is not an Action and is not undoable.

---

## Recipe: see it, then ship it

```jsonc
// One frame, to look at
premiere_export_frame({ time: 12 })
// → { path: "/mnt/d/.../frames/<seq>-12s.png" }   then READ the PNG

// The whole thing
premiere_export_sequence({})
// → { path, durationSeconds, bytes }   duration measured with ffprobe on the finished file
```

Then contact-sheet it and look across the whole render:

```sh
scripts/video-contact-sheet.sh "<the returned path>"
```

Facts worth knowing about export:

- **`exportSequence` resolves on COMPLETION**, not on queueing — a 6s sequence rendered in 1.3s. It
  renders inside Premiere, so it blocks; allow up to 10 minutes and roughly real time for a graded
  cut.
- 🔴 **Both exports resolve BEFORE the file is finished being written.** Measured: the frame promise
  resolved at 8394 ms, the file appeared at 8498 ms holding 672 KB, and settled at 8704 ms at 831 KB.
  The server waits for a stable size before returning, so the path you get is safe — **but any new
  tool that writes a file through Premiere must do the same.**
- Premiere **adds a silent AAC track** to a render even when the source is video-only.
- Neither export is an Action, so neither appears in Edit ▸ Undo. Correct — they write files, they
  do not change the project.

---

## Recipe: audit a project someone else cut

Read-only, and the right first move on any unfamiliar `.prproj`.

```jsonc
premiere_open_project({ path: "…/theirs.prproj" })
premiere_list_sequences({})                    // cheap; does not walk any timeline
premiere_get_sequence({ name: "their-seq" })   // the digest
```

Then `jq` the `statePath` for everything else (see the snippets at the top). What the digest tells
you at a glance: which tracks carry the work, which are muted, where the transitions are, and the
total span.

⚠️ **Opening a project makes it Premiere's active project.** If a human is at the keyboard, you have
just changed what they are looking at — say so. This cost a real hand cut once: a session activated
Jack's camping project for measurement, and the user then built a different edit into it by mistake.

⚠️ **`mediaPath` is what the project CLAIMS, not what is on disk.** Offline media reports a path
happily. Stat it before assuming a frame can be rendered — see the offline check in the `jq`
snippets above.

---

## Recipe: when a plain edit will not do it

`premiere_eval` runs JavaScript inside the panel with `ppro`, `helpers` and `log()` in scope. It is
a **diagnostic tool, not the product**: use it to find out what an unfamiliar API actually does,
then promote anything you reach for twice into a typed tool.

```jsonc
premiere_eval({ code: `
  const project = await helpers.activeProject()
  const seq = await helpers.activeSequence(project, 'gpom-s01')
  const clip = await helpers.resolveClip(seq, 'v0:0')
  const chain = await clip.getComponentChain()
  return { count: await chain.getComponentCount() }
` })
```

`helpers` carries `activeProject()`, `activeSequence(project, name?)`, `resolveClip(seq, ref)`,
`resolveProjectItem`, `resolveComponent`, `dumpSequence`, `withTransaction`, `secondsToTick`,
`tickToSeconds`, `plainValue`, `require`. Values that will not serialise come back as
`{ __opaque, members }` listing what the object offers — which is what makes it useful for probing.

**When eval teaches you something, write it into [`api-notes.md`](./api-notes.md) in the same
session.** That file is why the next person does not pay for the same lesson.

---

## Things that do not work, so you stop looking

| You want to | Reality |
| --- | --- |
| Read which transitions a cut uses | **Impossible via the API.** Count only. Parse the gzipped `.prproj` if you must |
| Add an audio crossfade | **No audio transition API exists at all** |
| Ask an effect what params it has, before applying it | **No.** An un-inserted component has no methods |
| Read all of Lumetri's params | 33 of 130 are unreadable by every route. Writable though |
| Trim and move in one call | Actions in a transaction all compute against the pre-transaction state, so they fight. **Trim, then move** |
| Apply an effect and set its params in one undo step | Two transactions, unavoidably |
| Enumerate what projects are open | `getActiveProject()` is the only handle Premiere offers |
| Remove the Motion or Opacity intrinsics | Refused, deliberately. Reset their params instead |
| Read blend mode options | No enumeration accessor exists |
| Get an exact time back from an edit | **Everything snaps to a frame.** Compare within half a frame (`0.5 / frameRate`, which is in every state) |

---

## When it breaks

| Code | What it really means | Do |
| --- | --- | --- |
| `PANEL_NOT_CONNECTED` | Panel closed, or **rebuilt and not reloaded** | ⋯ → Load in UXP Developer Tool |
| `PANEL_ERROR: listen EADDRINUSE` | Something holds port 7890 — **either your own orphaned server, or another live Claude session that used Premiere first** | Trace the holder up to its `claude` process before killing anything. Yours → kill it. Someone else's → leave it and tell the user. Full recipe: the skill's §1d |
| `TIMEOUT` | **Almost always a modal dialog waiting in Premiere** | Ask the user to look and dismiss it |
| `CLIP_NOT_FOUND` | A stale ref | Re-read the state |
| `EFFECT_NOT_FOUND` / `TRANSITION_NOT_FOUND` | Guessed a match name | List first |
| `INVALID_ARGS` | Bad arguments — **or a stale panel** | Check the call, then reload the panel |
| `MCP error -32602` | A zod schema violation, rejected before the tool ran | Not our error shape; read the message |

🔴 **An MCP reconnect does not kill the old server** — it orphans it holding the bridge port. This
is now the most likely reason a working bridge suddenly stops working, and the error names a port
rather than the cause.
