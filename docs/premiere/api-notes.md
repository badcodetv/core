# Premiere UXP API — hard-won notes

Facts about Premiere's UXP API that cost us time, or that the documentation gets wrong.
**Append to this file whenever a call surprises you.** Every entry should say what we expected,
what actually happened, and what to do instead.

Ground truth for signatures is the type declarations that ship with the npm package:
`node_modules/@adobe/premierepro/src/premierepro.d.ts` (4,675 lines, v26.3.0). Read them
rather than guessing — Adobe's web docs lag the package.

---

## Verified live, 2026-08-21 (T1 spike, Premiere 26.3.2)

The panel connected and ran real code inside Premiere. These are measured, not assumed.

| Fact | Value |
| --- | --- |
| Host reported by UXP | `premierepro` **26.3.2** |
| `require('premierepro')` exports | **70** |
| `VideoFilterFactory.getMatchNames()` | **106 video effects** on this install |
| `new Function(...)` | **Works.** `premiere_eval` (T11) is viable |
| `async` via `new Function` | Works — `new Function('return (async () => 42)')()()` resolves |
| `WebSocket` in the panel | Present and functional |
| `VideoFilterFactory` · `SequenceEditor` · `EncoderManager` · `Exporter` · `TickTime` | All present |

### 🔴 `ppro.Application.version` returns `null`

The type declarations show `Application: Application` with `readonly version: string`, and the
plan's tool table specified `ppro.Application.version` for `premiere_status`. **It returns
`null` at runtime.** Do not use it.

**Use the UXP host object instead** — verified returning `26.3.2` in the same probe:

```js
const { host } = require('uxp')
host.version   // "26.3.2"
host.name      // "premierepro"
```

`require('uxp').versions` came back as `{}` — also not useful.

### The panel connects over plain `ws://localhost`

No mirrored networking, no direct-IP fallback, no firewall rule needed. Default WSL2 NAT
forwarding was enough on Windows 11 25H2. The manifest declared:

```json
"network": { "domains": ["ws://localhost:7890", "ws://127.0.0.1:7890"] }
```

Both forms were accepted by the manifest validator. (`ws://*:7890` was never tested — it was
dropped before the spike rather than risk a validator rejection.)

---

## Projects, 2026-08-21 (T6)

### 🔴 `Project.isProject(path)` is NOT an existence check

It answers *"could a Premiere project live at this path"*, essentially a filename question — **it
returns `true` for files that do not exist.** Measured live on two different non-existent paths,
both `true`.

This cost us the whole first T6 run. The panel used it to choose between `open` and
`createProject`; it chose `open` for a file that was not there, and Premiere threw
**`Failed to open the project`** — a native error with **no stack and no detail**, which tells you
nothing about which call failed or why.

**Do not use it to decide create-vs-open.** The server checks the real filesystem through
`/mnt` and passes an explicit `create: boolean` to the panel, which obeys. The panel cannot make
this call correctly, because it has no filesystem worth the name.

### 🔴 `project.path` comes back as an extended-length path

Premiere reports `\\?\D:\badcode-videos\x.prproj`, **not** `D:\badcode-videos\x.prproj`. That
`\\?\` prefix defeats every drive-letter match, so an untreated path silently passes through
translation unchanged and the session ends up with a raw Windows string where it expected
`/mnt/d/…`. `paths.ts` now strips it (`stripExtendedPrefix`, with the `\\?\UNC\` variant handled
too) before anything else looks at the string.

### 🔴 `Project.open()` rejects with a bare STRING — even when it succeeds

The worst one so far, because the failure is a lie.

```
Project.open(path, options)   →   rejects with the string "Failed to open the project"
                                  …and the project is now open and active.
```

Measured live 2026-08-21, three times: after the rejection, `getActiveProject()` was the project
we had just asked for — whether it was already open beforehand or not. What is thrown is a
**plain string, not an `Error`**, which is why it arrives with no stack, no `.name` and no
`.message`, and why `String(e)` is the only way to read it.

**Never trust the return value or the rejection on its own. Attempt, swallow, then verify:**

```js
let project = null
try { project = await ppro.Project.open(path, options) } catch { /* the throw means nothing */ }
if (!project) {
  const active = await ppro.Project.getActiveProject()
  if (samePath(active?.path, path)) project = active   // samePath() normalises the \\?\ prefix
}
```

`panel/src/commands/project.ts` applies this to `createProject` too — uniformly, rather than
betting that only one of the two lies.

### There is no way to enumerate open projects

`getActiveProject()` is the only handle Premiere offers — the declarations have no `getProjects`,
no `setActiveProject`, no way to list what is open. So a project that is open but **not active**
is unreachable: opening it again is the only way to bring it forward (which works, per the
above), and there is no way to ask what else is currently open.

### What does work

| Call | Behaviour |
| --- | --- |
| `Project.createProject(winPath)` | Works, returns the `Project`. The parent directory must already exist — create it server-side first |
| `Project.open(winPath, options)` | Works on a file that actually exists. Suppress all three dialogs (`setShowConvertProjectDialog`, `setShowLocateFileDialog`, `setShowWarningDialog`) — a modal reaches the caller as an unexplained `TIMEOUT`, not an error |
| `project.close(new CloseProjectOptions().setPromptIfDirty(false).setShowCancelButton(false))` | Works, returns `true` |
| `new ppro.OpenProjectOptions()` / `new ppro.CloseProjectOptions()` | Constructible with `new`; the setters chain |

### `Object.keys(ppro.Project)` returns Array.prototype members

Probing a ppro *static* with `Object.keys` gives you `["at","concat","copyWithin",…]` — array
methods, not the API surface. The statics are native handles, so enumerate their prototype chain
instead (`premiere_eval` does this automatically and returns
`{ __opaque, members }` for anything that will not serialise).

---

## Sequences and component params, 2026-08-21 (T7)

### 🔴 `ComponentParam.getValueAtTime()` returns a WRAPPER, not the value

The declarations promise `Promise<number | string | boolean | PointF | Color>`. What actually
comes back is a plain object with a single `value` key:

```
Scale     →  { value: 100 }          NOT  100
Position  →  { value: [0.5, 0.5] }   NOT  a PointF
```

Unwrap it or every parameter in the timeline reads as `{"value":…}` noise. `plainValue()` in
`panel/src/ppro.ts` unwraps any object whose only own property is `value`, recursively.

### `PointF` params are ARRAYS, and they are NORMALISED 0–1

`Position` and `Anchor Point` come back as `[0.5, 0.5]` — a two-element array, not `{x, y}` — and
**0.5, 0.5 is the centre of frame, not half a pixel**. Do not reach for pixel coordinates on
these; they are fractions of the frame. Confirm the same convention before *writing* a point
value (T10).

### The intrinsic components, measured

Every video clip arrives with two, in this order. Match names and **param indices** matter,
because display names do not identify a param reliably (see below).

| # | matchName | displayName |
| --- | --- | --- |
| 0 | `AE.ADBE Opacity` | Opacity |
| 1 | `AE.ADBE Motion` | Motion |

**`AE.ADBE Opacity`** — 3 params: `0 Opacity` (100) · `1 Blend Mode` (18) · `2 Blend Mode` (0)

**`AE.ADBE Motion`** — 11 params: `0 Position` ([0.5,0.5]) · `1 Scale` (100) · `2 Scale Width`
(100) · `3 " "` (true) · `4 Rotation` (0) · `5 Anchor Point` ([0.5,0.5]) · `6 Anti-flicker Filter`
(0) · `7 Crop Left` · `8 Crop Top` · `9 Crop Right` · `10 Crop Bottom`

All eleven report `areKeyframesSupported() === true`.

### 🔴 Display names are not unique, and are sometimes blank

Two traps in that table, both live:

- **`AE.ADBE Opacity` has TWO params called "Blend Mode"** (indices 1 and 2). Resolving a param
  by display name is therefore ambiguous on the intrinsics themselves.
- **`AE.ADBE Motion` param 3 has a display name of `" "`** — a single space. It is Uniform Scale
  in the UI, and it is unaddressable by name.

**The index is the authoritative address.** Name lookup is a convenience for the common case and
must never be the only route — `premiere_describe_effect` (T10) has to report indices.

### Miscellany

- A default-preset sequence is **3 video and 3 audio tracks**, 1920x1080.
- **`createSequenceFromMedia` lays down no audio when the source has none** — obvious in
  hindsight, but it briefly read as a bug. Flow renders are frequently video-only
  (`ffprobe` the source before believing an empty `A1`).
- The full param walk is **cheap**: 15 ms with params versus 9 ms without, on a one-clip
  sequence. `premiere_get_sequence({ params: false })` is kept for colour-graded timelines, but
  it is not needed for ordinary use. **Re-measured in T10 on a Lumetri-graded clip: 181 params
  cost 49ms against 3ms without. Still cheap.**

---

## Editing the timeline, 2026-08-21 (T8)

### 🔴 `TrackItemSelection.createEmptySelection()` is unusable — use `sequence.getSelection()`

It is the API Adobe's declarations point you at for `createRemoveItemsAction`, and it does not
work. The callback hands you an object with every method present —
`["addItem","removeItem","getItems","getTrackItems"]` — and **every native call against it throws
`"The script object is no longer valid."`**, including synchronously inside the callback itself.

Isolated properly before concluding: the *clip* handle resolved alongside it was fine
(`getName()`, `getStartTime()` both answered), so it is the selection that is dead, not the items.

**The route that works** — verified removing a real clip inside a transaction:

```js
await sequence.clearSelection()
const selection = await sequence.getSelection()   // the sequence's OWN selection
selection.addItem(clip, true)
// …then createRemoveItemsAction(selection, ripple, MediaType.ANY, false) inside executeTransaction
```

Side effect: this replaces whatever the user had selected in the timeline. Worth it, since the
alternative is being unable to remove a clip at all.

### 🔴 Every edit snaps to a frame boundary

Ask for a clip at `4.0`s in a 23.976 fps sequence and it lands at **4.004**. Nothing warns you,
and no caller can predict it without knowing the sequence's rate.

So `SequenceState.sequence` now carries **`frameRate`**, derived from `timebase`:

```
frameRate = 254_016_000_000 / Number(timebase)      // ticks per second / ticks per frame
```

Measured: `timebase 10594584000` → 23.976 fps; `10160640000` → 25 fps. A missing or nonsense
timebase yields `0`, never `Infinity`.

**Never assert exact equality on a time you asked Premiere for.** Compare within half a frame
(`0.5 / frameRate`).

### Schema violations arrive as MCP protocol errors, not as our error shape

A `premiere_*` argument that fails its zod schema is rejected by the MCP layer **before the tool
handler runs**, so it comes back as `MCP error -32602: Input validation error: …` rather than the
usual `{ error: true, code, message, hint }`. Both mean "rejected"; anything parsing tool results
has to recognise both forms.

### `createSequence(name)` uses the project default, which was 23.976 fps 1920x1080

Not the frame rate of any media in the project — `createSequenceFromMedia` is what matches the
footage (it produced a 25 fps 1280x720 sequence from the same clip). Worth knowing before
wondering why a 25 fps source is landing on 23.976 frame boundaries.

---

## Transitions, markers, playhead, 2026-08-21 (T9)

### 🔴 `getTrackItems()` returns `null` for every item that is not a CLIP

The headline finding, and it is a hard wall.

```
track.getTrackItems(TRANSITION, false)   →   [null, null]     (with two real transitions on the track)
track.getTrackItems(CLIP, true)          →   [clip, null, clip, null]   (the nulls are the gaps)
track.getTrackItems(EMPTY|PREVIEW|FEEDBACK, false) → all null
```

**The length is exact and meaningful** — measured live going 0 → 1 → 2 as transitions were added
to a fresh sequence — but **not one element can be marshalled into JavaScript.** So a transition
can be counted and never read: no match name, no position, no duration, no side.

Two consequences, both load-bearing:

- **Filter every `getTrackItems()` result.** A single unfiltered null took down `dumpSequence`
  with `Cannot read properties of null (reading 'getMatchName')` — which then broke *every* tool
  that returns a state, `move_clip` included. This was latent from T8 and only surfaced the
  moment a transition existed. `liveItems()` in `panel/src/ppro.ts` does it.
- **`SequenceState` reports `transitionCount` per track and nothing else.** The per-clip
  `transitions: { start?, end? }` field is kept in the schema and is always empty; the day Adobe
  marshals a transition track item it fills itself in with no other change.

### The transitions ARE there — the project file proves it

Worth knowing that the write half works, and worth knowing *how* it was proved, because the same
trick settles the next argument of this kind.

**A `.prproj` is gzipped XML.** `premiere_save`, then `zcat`:

```xml
<VideoTransitionTrackItem ObjectID="82" …>
  <TransitionTrackItem Version="3">
    <TrackItem Version="4"><Start>900539643327</Start><End>1144215075327</End></TrackItem>
    <Alignment>115524356673</Alignment>
    <DisplayName>Cross Dissolve (Legacy)</DisplayName>
    <MatchName>AE.ADBE Cross Dissolve New</MatchName>
    <HasOutgoingClip>true</HasOutgoingClip>
    <HasIncomingClip>true</HasIncomingClip>
  </TransitionTrackItem>
```

Ticks ÷ 254,016,000,000 gives seconds: 3.545 → 4.505 on a cut at 4.004, i.e. a 0.959s (23-frame)
dissolve centred on the cut, exactly as asked for.

**This is the escape hatch if reading existing transitions ever becomes load-bearing** — for
instance when opening an edit a human cut by hand, where we did not place the transitions and
therefore do not know them. The cost is forcing a save on read, which is why it is not built in.
Ruled 2026-08-21 (Kai): not now; revisit if a real project needs it.

### Because the read is gone, `add_transition` verifies by count

`executeTransaction` returning `true` is not proof — Premiere has been caught reporting success
on calls that did nothing (`Project.open`, above). With no read-back, comparing
`getTrackItems(TRANSITION, …).length` before and after is the only verification available, and
`panel/src/commands/transitions.ts` does exactly that.

### No handles is NOT a refusal — you get a single-sided transition

Expected: a clip with no unused source media beyond the cut refuses the transition. Measured:
Premiere takes it and writes `HasOutgoingClip=true, HasIncomingClip=false` — a frame-hold on the
empty side. It will also add one across a **gap** between clips.

So there is no "Premiere will stop you" safety net here. If a dissolve must be genuinely
two-sided, leave handles deliberately: trim both clips shorter than their source first.

### 🔴 `inPoint` and `start` must not go in the same `trim_clip` call

Every Action in a `CompoundAction` is computed against the state at the **start** of the
transaction, not against the result of the Action before it. So a head-trim of +1s and a
"start at 4" do not compose — they fight, and the clip lands at 5.

**Trim, then move — two calls.** This applies to any pair of edits where one's correct argument
depends on the other having already happened.

### There is no audio transition API at all

No `AudioTransition` type, no `createAddAudioTransitionAction`, nothing anywhere in the 4,675
lines of declarations. `createAddVideoTransitionAction` exists only on `VideoClipTrackItem`.
`premiere_add_transition` therefore takes a video-only ref (`v0:2`), enforced at the schema.
**Audio crossfades have to be done by hand in the timeline.**

### `alignment` is a fraction, not an enum

`AddTransitionOptions.setTransitionAlignment(n)` reads back a default of **0.5** — the fraction
of the transition sitting before the cut, so 0.5 is centred. It reads like an enum of
start/centre/end constants and is not one. (The `<Alignment>` integer in the saved XML is a
different, tick-based encoding — do not cross the two.)

### Match names, measured on this install

118 video transitions. Both prefixed and unprefixed forms exist in the same catalogue, so
**always resolve through `premiere_list_transitions`** rather than typing one from memory.

| Wanted | Match name |
| --- | --- |
| Cross Dissolve | `AE.ADBE Cross Dissolve New` |
| Dip to Black | `AE.ADBE Dip To Black` (saved as `ADBE Dip To Black`) |
| Additive Dissolve | `ADBE Additive Dissolve` |

`getVideoTransitionMatchNames()` returns match names **only** — there are no display names on
the transition API, unlike `VideoFilterFactory`. The friendly name (`Cross Dissolve (Legacy)`)
exists in the project file and nowhere the API will show you.

### Markers and the playhead behave

The dull, welcome half of T9. `Markers.getMarkers(seq)` → `createAddMarkerAction(name,
ppro.Marker.MARKER_TYPE_COMMENT, tick, tickDuration, comments)` inside a transaction works, and
markers read back in full (name, start, duration, comments) — no marshalling trouble.
`sequence.setPlayerPosition(tick)` is a plain async call, **not an Action**, so it runs outside
any transaction and is not undoable. Read the playhead back rather than echoing the request: it
snaps to a frame like everything else.

---

## Effects and params, 2026-08-21 (T10)

### 🔴 An un-inserted `VideoFilterComponent` has NO METHODS — the T10 open question, answered

```js
const comp = await ppro.VideoFilterFactory.createComponent('AE.ADBE Gaussian Blur 2')
Object.getOwnPropertyNames(Object.getPrototypeOf(comp))   // ["constructor"]  — that is all
comp.getParamCount()   // TypeError: comp.getParamCount is not a function
comp.getMatchName()    // TypeError: …is not a function
comp.getParam(0)       // TypeError: …is not a function
```

It is an **opaque token**, good for exactly one thing: handing to `createAppendComponentAction`
or `createInsertComponentAction`. Params exist only on the **applied** instance, fetched back out
of the chain afterwards.

**Ruling: `premiere_describe_effect` requires a `clip`.** There is no way to ask "what settings
does this effect have" without putting it on something first. The plan anticipated this and the
tool signature changed from `{ matchName, clip? }` to `{ clip, component }`.

### 🔴 Applying an effect and setting its params cannot be one transaction

A direct consequence of the CompoundAction rule (T9, issue #7): every Action is computed against
the state at the **start** of the transaction. Until the append has committed there is no applied
component, and the token you hold has no `getParam` to address. So:

```
transaction 1:  chain.createAppendComponentAction(component)
   …re-resolve the clip and its chain…
transaction 2:  param.createSetValueAction(param.createKeyframe(value), true)   × n
```

`premiere_apply_effect` therefore leaves **two** `BadCode:` entries in Edit ▸ Undo, not one. The
plan asked for one; it is not possible, and the tool description says so.

The same applies to keyframing: `createSetTimeVaryingAction(true)` must commit **before**
`createAddKeyframeAction` has a keyframe track to add to.

### 🔴 33 of Lumetri Color's 130 params cannot be read by ANY route

`getValueAtTime()` throws:

> *getValueAtTime is not supported for these value types. Use GetKeyframeAtTime to get a keyframe
> object at time. The value can be extracted from the keyframe object.*

**That advice does not work.** Measured on the same params:

| Route | Result |
| --- | --- |
| `getValueAtTime(t)` | throws (the message above) |
| `getKeyframePtr(t)` | returns `null`, or throws *"Illegal Parameter type"* |
| `getStartValue()` | returns `null` |

Stable and reproducible: exactly 33 every time, unchanged by re-reading, by stacking another
effect on top, or by writing to a different param. They are the structural ones — `Blob`
(index 0), `White Balance` (13), the colour wheels and curve controls, and the blank-named group
headers.

**They can still be WRITTEN.** Only reading is lost.

`SequenceState`'s `Param` therefore carries **`unreadable: true`** with `value: null`, and keeps
the param's real display name rather than replacing it with a placeholder. `value: null` alone
would be ambiguous — a readable param may legitimately be null — so the flag is carried
explicitly from the panel and never inferred.

### The param walk is cheap even on Lumetri

Answering the caution left in the T7 notes. On a clip carrying Opacity + Motion + two blurs +
Lumetri — **181 params** — the full walk cost **49ms**, against 3ms with `params: false`.

So `premiere_get_sequence({ params: false })` is a real optimisation on a heavily graded
50-clip timeline (~2.5s → ~0.2s) and unnecessary for anything smaller. Nothing here needs
avoiding.

### The "Gaussian Blur" trap: display names collide across generations

| Display name | Match name | Params |
| --- | --- | --- |
| **Gaussian Blur** | `AE.Impact_Blur_FX` | 20, mostly internal |
| **Gaussian Blur (Legacy)** | `AE.ADBE Gaussian Blur 2` | 3, all meaningful |

The modern Impact effect exposes `Error occurred`, `_ Applied Version`, `_ Sequence Width`,
two params called `Controls` and three with empty names. Its real control is **index 5,
"Amount"**. The legacy one is `0 Blurriness` (defaults to **25**, not 0), `1 Blur Dimensions`,
`2 " "` (Repeat Edge Pixels).

**Prefer the legacy effect for automation** unless the modern look is specifically wanted.
Premiere ships several such pairs — always confirm the match name, never the display name.

### Lumetri Color param indices, measured

The useful, readable ones (of 130). Recorded so nobody walks the component again:

| Index | Param | Default |
| --- | --- | --- |
| 6, 7 | Input LUT *(name appears twice)* | 0 |
| 8 | HDR White | 100 |
| 11 | Intensity *(Basic)* | 50 |
| 14 | Temperature | 0 |
| 15 | Tint | 0 |
| 16 | Saturation *(Basic)* | 100 |
| 19 | Exposure | 0 |
| 20 | Contrast | 0 |
| 21 | Highlights | 0 |
| 22 | Shadows | 0 |
| 23 | Whites | 0 |
| 24 | Blacks | 0 |
| 25 | HDR Specular | 0 |
| 34, 35 | Look *(twice)* | 0 |
| 37 | Color Space | 26 |
| 38 | Intensity *(Creative)* | 100 |
| 40 | Faded Film | 0 |
| 41 | Sharpen | 0 |
| 42 | Vibrance | 0 |
| 43 | Saturation *(Creative)* | 100 |
| 45 | Tint Balance | 0 |
| 52 | HDR Range | 100 |

Note `Saturation`, `Intensity`, `Look` and `Input LUT` each appear **twice** at different
indices, in different sections of the effect. **This is why the index is the address.**
`resolveParam()` refuses an ambiguous name rather than guessing which one was meant.

### Point values are written the way they are read

`{x: 0.25, y: 0.75}` on Motion's Position reads back as `[0.25, 0.75]` — the write convention
matches the read convention confirmed in T7, and both are **0–1 fractions of the frame**, not
pixels. `toPproValue()` accepts `{x,y}` or a two-element array and builds a `ppro.PointF`;
colours are `{r,g,b,a?}` → `new ppro.Color(...)`.

### Keyframes work exactly as the declarations describe

The one genuinely uneventful part of T10. `Keyframe.position` is settable, so:

```js
const kf = param.createKeyframe(120)
kf.position = ppro.TickTime.createWithSeconds(2)
param.createAddKeyframeAction(kf)
param.createSetInterpolationAtKeyframeAction(tick, ppro.Constants.InterpolationMode.BEZIER, true)
```

Scale 100 at 0s and 120 at 2s produced two keyframes reading back at the right times with the
right values. `areKeyframesSupported()` is honest — every intrinsic param returns true.

### The intrinsics cannot be removed

`AE.ADBE Opacity` and `AE.ADBE Motion` are on every clip and Premiere's own UI will not delete
them. `premiere_remove_effect` refuses them with an explanation rather than issuing a
`createRemoveComponentAction` that would fail obscurely. Reset their params instead.

---

## Export, 2026-08-21 (T12)

### `exportSequence(IMMEDIATELY)` resolves on COMPLETION — the T12 open question, answered

Not on queueing. A 6s sequence resolved in 1348ms with a complete 5.4MB MP4 behind it, and the
file did not change over the following 8 seconds. So there is no job to poll and no queue to
watch: `await` is the whole story.

`ExportType.IMMEDIATELY` renders **inside Premiere**, which is why it blocks. The alternatives
(`QUEUE_TO_AME`, `QUEUE_TO_APP`) hand off to Media Encoder and would need a different, much more
awkward completion story — we do not use them.

### 🔴 …but BOTH exports resolve before the file is finished being written

The subtlety the plan did not anticipate, and it bites silently. Measured live on a frame export:

| Moment | Elapsed | File |
| --- | --- | --- |
| `exportSequenceFrame` promise resolves | 8394ms | **does not exist** |
| file first appears | 8498ms | 672,839 bytes |
| size settles | 8704ms | 831,695 bytes — final |

Read it the instant the promise resolves and you get `ENOENT`; read it 150ms later and you get a
**truncated PNG that still opens**, which is worse. The same applies to the video render.

**Never treat the promise as "the file is ready."** `waitForStableFile()` in `src/server.ts`
waits for the file to exist and for its size to hold steady (1.5s for a frame, 2s for a render)
before either tool returns. Both tools report `bytes`, so a caller can tell.

### Neither export is an Action

Neither runs in a transaction and neither appears in Edit ▸ Undo — correctly, since they write
files rather than changing the project. They are the only two mutating-looking tools with no
`BadCode:` undo entry.

### `exportSequenceFrame` takes the directory and filename SEPARATELY

`exportSequenceFrame(sequence, time, filename, filepath, width, height)` — `filename` is the
bare name with extension, `filepath` is the containing directory. Passing a full path as
`filename` does not work. Formats: **bmp, dpx, gif, jpg, exr, png, tga, tif**.

The directory must already exist; Premiere will not create it, and the failure is a bare `false`
return. The server creates it first, as it does for everything else.

### A default sequence does not match your footage, and the exported frame proves it

Visible in the very first frame exported through the bridge: the picture sat **inset in black**
on all sides. Not a bug — the source is 1280x720 @ 25fps and `createSequence(name)` had made a
1920x1080 @ 23.976 sequence from the project default, so the clip sat unscaled in a larger frame.

This is the T8 note about `createSequence` versus `createSequenceFromMedia`, now confirmed with
pixels. **Use `premiere_create_sequence({ fromItems: [...] })` when the sequence should match the
footage** — which for a cut assembled out of Flow renders is nearly always.

### Premiere adds a silent audio track on export

The test media is video-only (`ffprobe` shows a single h264 stream), and the rendered MP4 came
back with **h264 + aac**. The Match Source preset supplies a silent track rather than omitting
audio. Worth knowing before wondering where an audio stream came from.

### Exported duration is trustworthy

A 6s timeline rendered to `duration=6.037333` — 6s plus one frame at 23.976fps, which is exactly
right for an inclusive out point. `premiere_export_sequence` reports `durationSeconds` from
**ffprobe on the finished file**, never from what was asked for.

---

## A real hand-cut project, 2026-08-21 (camping)

The first project the bridge opened that a human actually edited, rather than a scratch project it
built itself: `D:\badcode-videos\camping\camping vid Copy-test_1.prproj` — Jack's camping cut.
149 video clips and 135 audio clips across 12 tracks, 3m35s at 25fps 1920x1080. Everything below
is measured on it.

### 🔴 `SequenceState` does not fit through MCP on a real timeline — in EITHER mode

The finding that matters. Measured on camping:

| Mode | Bytes | Time |
| --- | --- | --- |
| `params: true` (the default) | **573,065** | 769 ms |
| `params: false` | **60,371** | 117 ms |

The MCP result cap is roughly 25,000 tokens. **Both modes blow it.** `premiere_get_sequence`
returned 63,543 characters and was refused; `premiere_set_active` returned **576,237** and was
refused. The refusal happens at the transport, *after* the panel has done the work — so
`set_active` genuinely switched the sequence in Premiere and the caller still got an error. **A
failed state-returning call is not proof the mutation failed.**

This is not a `get_sequence` problem. **Thirteen tools return `SequenceState`** through the single
`sendAndNormalise()` door in `src/server.ts` — `create_sequence`, `set_active`, `get_sequence`,
`insert_clip`, `move_clip`, `trim_clip`, `remove_clip`, `clone_clip`, `add_transition`,
`remove_transition`, `add_marker`, `apply_effect`, `set_param`, `remove_effect`. On a project this
size **every one of them is unusable from a conversation**, which retires Decision 3's promise
that a mutating tool hands back a state the session can act on.

The scratch projects never showed it because they had one to three clips.

### Where the bytes actually go

| Portion | Bytes | Share |
| --- | --- | --- |
| Effect params | 466,797 | 81% |
| Clip scaffolding (times, refs, names, media paths) | 57,614 | 10% |
| Component headers | 41,064 | 7% |

And within the params, one component dominates:

| Component | Params across the timeline |
| --- | --- |
| **Channel Volume** | **4,455** |
| Motion | 1,639 |
| Opacity | 447 |
| Volume | 270 |
| Hard Limiter | 8 |

**`Internal Channel Volume Stereo` reports 33 params per audio clip**, and indices 3–32 are all
**blank-named and carry an identical value** — Premiere exposing 32 channel slots on a clip that
has two. 65% of every param in the dump is that padding. Any future size work should start here:
it is pure noise, it is trivially identifiable (blank name + duplicate of index 1/2), and dropping
it costs nothing.

### The audio intrinsics, measured

`api-notes` had the video intrinsics from T7 and nothing for audio. Every audio clip carries two:

| # | matchName | displayName | Params |
| --- | --- | --- | --- |
| 0 | `Internal Volume Stereo` | Volume | 2 — `0 Mute` (bool), `1 Level` (linear gain, **not dB**) |
| 1 | `Internal Channel Volume Stereo` | Channel Volume | 33 — `0 Bypass`, `1 Left`, `2 Right`, `3…32` blank |

`Level` reads as a **linear multiplier** (0.1778 on this cut ≈ −15 dB), not the decibel figure the
UI shows. Convert before quoting a number at a human.

### 🔴 Audio effect match names are bare GUIDs — the prefix rule does not hold

The note further down this file says native effects are `PR.ADBE.*` and AE-ported ones `AE.ADBE.*`.
Jack's Hard Limiter on A6 reports its match name as:

```
e0b23f05-f1a7-4ef7-9b50-7ec3e3002058     displayName: "Hard Limiter"
```

A bare GUID with no prefix at all. **Never pattern-match a match name to decide what an effect
is** — resolve through `premiere_list_effects` and compare display names.

### `mediaPath` is reported for OFFLINE media too

All 284 track items came back with a `mediaPath`, and 57 distinct source files behind them — but
one of those files **does not exist on this machine**:

```
/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/badcode logo designs/draft 1/4.mp4
```

That is Jack's OneDrive, on Jack's PC, referenced by 8 clips. Premiere reported the path happily.
**`mediaPath` is what the project *claims*, not what is on disk** — stat it before assuming a
session can read the frame, and expect any export covering those 8 clips to render Media Offline.

### The transitions wall did NOT bite here

Worth recording, because it was the predicted trouble. Every video track reported
`transitionCount: 0`, and `zcat`-ing the project file agreed: **no `VideoTransitionTrackItem`
nodes at all.** Jack cut the whole thing with hard cuts. (The older `camping vid.prproj` from
30 June has 3.) So issue #6 — transitions being write-only — costs this project nothing, and the
`.prproj`-XML workaround stays unbuilt, as Kai ruled.

### `getSequences()` disagrees with the project file, and `getSequences()` is right

The XML has **three** `<Sequence` nodes; `premiere_list_sequences` reports **one** (`camping`).
Not a marshalling failure — the other two are structural (nested/master-clip sequence records),
not timelines a human would open. **Do not count XML nodes to predict what the API will list.**

### A freshly opened project has NO active sequence

`premiere_open_project` succeeded and `premiere_list_sequences` reported `active: false` for the
only sequence in it. Opening a project does not open a timeline. Pass `name` explicitly to
`premiere_get_sequence`, or call `premiere_set_active` first — but see the size problem above
before calling `set_active` on anything large.

### How this was fixed — read this before adding a tool that returns a timeline

T21, same day. **No tool returns a raw `SequenceState` any more.** `src/view.ts` turns it into a
`SequenceView` and `sendAndView()` in `server.ts` is the single door every one of the thirteen goes
through. Three things happen there:

1. **The complete state is written to disk**, untrimmed, at
   `<project dir>/.bridge/state-<sequence>.json`, and the path comes back as `statePath`. **`jq`
   over that file is the right tool for anything bulk** — counting, searching, auditing a whole
   timeline — and it costs the session no context at all. This is how the findings above were
   produced.
2. **The caller gets a summary**: the project, the sequence settings, and one line per track
   (clip count, transition count, time span, mute state). On camping that is **1,772 bytes against
   573,065**. It is bounded by the number of *tracks*, so it does not grow with the edit.
3. **Detail is asked for, not dumped.** `premiere_get_sequence` takes `tracks: ["v2"]`,
   `clips: ["v2:3"]` and `range: [10, 30]`. Uppercase names are read as UI labels (`V3` → index 2),
   lowercase as API indices (`v2`) — whichever form you copied from a previous result works.

If a response would still be too large it degrades one rung at a time — parameter values, then
effect chains, then markers, then change detail, then clip lists — and `notes` names both what went
and the narrower call that would have kept it. **The bottom rung always fits**, so a state-returning
tool can no longer fail on size.

Two details worth knowing before extending it:

- **The blank channel-volume slots are folded in the VIEW, never in `normalise.ts`.** The file on
  disk stays lossless on purpose; a caller can still write to those param indices even though the
  summary does not list them. Only params with a genuinely **empty** name that duplicate a named
  param's value are folded — a single-space name (`AE.ADBE Motion` index 3, Uniform Scale) is a
  real control and survives.
- **Mutating tools report `changed`** — added, removed and modified clips, found by diffing
  against the previous state for that sequence. This is the only way to learn the ref of a clip
  `insert_clip` just created: the panel returns a timeline, never a receipt.

### What a hand cut actually looks like, for calibration

Useful when guessing whether a tool will cope. 149 video clips, mean duration **1.81s**, minimum
**0.12s** (three frames at 25fps — rapid-fire cutting on the beat), maximum 10s. One source file
(`clips/2.mp4`) is used **56 times**. Tracks are used unevenly: V1 empty, V3 carries 84 clips, V6
carries 3; A2–A5 are all **muted**. Gaps between clips are common and normalise handles them (the
item counts matched the XML exactly, so no nulls leaked through `liveItems()`).

Effects are almost absent: 569 components on 284 items is **the intrinsics and nothing else**,
bar one Hard Limiter. Only **4 clips** carry keyframes, and **0 params** came back `unreadable`
(the Lumetri problem from T10 needs Lumetri to show up).

---

## Running the bridge, 2026-08-21 (T21 live validation)

### 🔴 Reconnecting the MCP server does NOT kill the old one — it orphans it holding the port

Reconnecting `premiere` from `/mcp` spawns a **new** server process and leaves the previous one
running. The old process keeps its `ws` listener on 7890, so the new server's `listen()` fails and
**every tool returns `PANEL_ERROR: listen EADDRINUSE: address already in use 127.0.0.1:7890`**.

Three generations were found alive at once on this box.

### 🔴 …but "kill all but the newest" is only safe for ONE of the two causes

There are two ways to arrive at `EADDRINUSE`, they look identical, and the fix for one is
destructive to the other. **Establish which before killing anything.**

| Cause | Holder belongs to | Safe to kill? |
| --- | --- | --- |
| An `/mcp` reconnect orphaned an older generation | **your own** `claude` process | **Yes** — it is your own litter |
| Another Claude session used Premiere first | **a different** live `claude` process | 🔴 **NO.** It may be mid-edit |

Claude Code starts every server in `.mcp.json` at launch, so several sessions open at once is
ordinary, not a fault — and the first one to make a `premiere_*` call takes the port for its
lifetime. **That is the one-Premiere-one-panel law working**, not a bug to clear.

Tell them apart by walking the holder up to its `claude` process and comparing with your own:

```sh
ss -lptn 'sport = :7890'                       # the holding pid
up() { P=$1; while [ -n "$P" ] && [ "$P" != 1 ]; do ps -o pid=,args= -p "$P" --no-headers | cut -c1-90
        P=$(ps -o ppid= -p "$P" 2>/dev/null | tr -d ' '); done; }
up <holding pid>                               # whose server is it
up $$                                          # …and whose are you
```

Same `claude` pid in both chains → your own orphan, `kill -TERM` it. **Different `claude` pid →
another live session. Do not kill it.** Say what you found and let the user choose: work in that
session, or close it themselves. Only they know what is unfinished in it.

Measured live 2026-08-22: four sessions open, three holding `premiere-mcp` processes, and the one
holding the port was seven minutes into an unrelated task with an agent attached. "Kill all but
the newest" would have destroyed it.

The next tool call after a genuine release binds cleanly, and the panel reconnects on its own
backoff (capped at 10s) — no Premiere-side action needed. **`getBridge()` only caches the `Bridge`
after `listen()` resolves**, so a failed bind does not poison the process; retrying really works.

### The bridge binds on first USE, which keeps idle sessions out of the fight

For one day (2026-08-21) the server opened its listener at startup, so the panel's light stayed
green through an idle session. That was the wrong trade: it made every *launched* session grab the
port, so three collided before anyone had touched Premiere. Reverted 2026-08-22.

**Nothing binds until the first `premiere_*` call** — the same discipline as Flow, where the
browser comes up when you start working on Flow. The panel reads `waiting for Claude…` until then,
which is honest and costs nobody a port. `premiere_status` is what opens it.

### 🔴 Every edit tool acts on the ACTIVE sequence — and a human clicking in Premiere changes which

The worst footgun found so far, because nothing reports it and the call succeeds.

`premiere_insert_clip`, `move_clip`, `trim_clip`, `apply_effect` and the rest take **no sequence
argument**. They act on whatever Premiere considers active *at the moment the panel runs them*.
`premiere_create_sequence` and `premiere_set_active` make a sequence active — but so does **a human
clicking a different timeline tab**, and the session is never told.

Measured live 2026-08-21: a `create_sequence('_probe-blend')` was followed seconds later by an
`insert_clip`, which landed in **`gpom-s01`** — because the user had clicked back into that tab in
between. The tool returned success and a valid state; only the `sequence.name` in the response
revealed where the work had actually gone.

**Defences, in order of strength:**

1. **Read `sequence.name` on every response.** It is in every state a tool returns. If it is not
   the sequence you meant, stop and re-assert with `premiere_set_active` before doing anything else.
2. **Re-assert `set_active` immediately before a run of edits**, not once at the top of a session.
3. **Never assume a `create_sequence` is still active** by the time the next call runs.
4. **Do not drive Premiere while a human is using it.** The bridge is serial with respect to the
   panel, not with respect to the person at the keyboard. If the user says they are going to work
   in Premiere, stop making calls until they say they have stopped.

This also poisons `changed`: the diff compares against the last state *this session* read, so a
human's edits in between are reported as if the tool had made them. On the same run, `s03-plant-room`
showed as `modified` from 83.8s to 185.32s — a move the user had made by hand.

### `changed` reports clip TIMES, not parameter edits

`premiere_set_param` returns `changed: { added: [], removed: [], modified: [] }` — empty, because
`diffStates` compares `start`/`end`/`inPoint`/`outPoint` and the clip did not move. That is
literally correct and worth knowing before reading an empty `changed` as "nothing happened".
**To confirm a param landed, read it back** (`premiere_get_sequence({ clips: ["v0:0"] })`) or, for
anything visual, export a frame and look at it.

### A 720p clip in a 1080p sequence is inset in black, and Scale 150 fixes it exactly

Confirmed with pixels twice over on `gpom-s01`: `s01-earth.mp4` is 1280x720 in a 1920x1080 25fps
sequence and rendered pillarboxed *and* letterboxed. `set_param(v0:0, component 1, param 1, 150)`
— Motion → Scale — filled the frame precisely, because 1920/1280 and 1080/720 are both exactly
1.5. Motion param 3 (the one named `" "`) is Uniform Scale and defaults to `true`, so setting
Scale alone drives both axes.

### Premiere trims a clip to the sequence's frame grid on insert

`s02-hong-kong.mp4` is 27.834s of 24fps footage. Dropped into a 25fps sequence it became
**27.8s** — 695 frames exactly. Expect a conformed clip's duration to differ from `ffprobe`'s by
up to a frame, and take the length from the returned state rather than from the source file.

---

## Building the panel, 2026-08-21 (T5)

### The esbuild CJS bundle is safe in UXP — but only because the entry exports nothing

The plan specified `format: 'cjs'`, `platform: 'neutral'`, externals `premierepro`/`uxp`/`os`/`fs`.
That works, and the emitted bundle was **checked rather than assumed**:

- **No `module.exports` / `exports.` reference anywhere in the output.** esbuild only emits those
  when the entry point has exports. `panel/src/main.ts` is a pure side-effect entry with no
  `export` statements, so nothing at top level touches `module` — which a UXP `<script src>`
  context does not reliably provide. **Keep `main.ts` export-free**, or the bundle will start
  referencing a `module` that may not exist.
- `require` survives as a free identifier for UXP to supply.

### Reach `require` through a helper, not a bare call

`panel/src/ppro.ts` exports `uxpRequire<T>(id)`, which reads `require` as an *identifier*
(`typeof require === 'function' ? require : globalThis.require`) rather than calling
`require('…')` directly. esbuild only rewrites `require(...)` **call expressions**, so writing it
this way keeps the bundler out of it entirely and covers both ways UXP might expose `require`
(true global vs. script-wrapper scope-local).

### 🔴 A rebuilt panel does not reload itself

Premiere keeps executing the previously loaded bundle until someone presses **⋯ → Load** in UXP
Developer Tool. Confirmed live: after T5's rebuild, the panel still in Premiere was the T1 spike.

**The symptom is not an error you would connect to this.** The stale panel opens the socket
normally, so the port is up and the light may look fine — but its `hello` fails validation
against the current protocol, so the bridge never marks itself connected and the caller gets
`PANEL_NOT_CONNECTED`. A stale panel that *does* handshake answers `INVALID_ARGS` to commands it
ought to know. `bridge.ts` now detects "socket attached, handshake never completed" and says
*"it is almost certainly an older build"* rather than *"No panel connected"*.

---

## Known from the type declarations, not yet exercised

Recorded during planning review so nobody re-derives them. **Unverified against a live host** —
promote to the section above once proven, correct it if wrong.

- **`SequenceEditor.insertMogrtFromPath` is NOT an Action.** It returns
  `Array<VideoClipTrackItem | AudioClipTrackItem>` synchronously, so it cannot go inside a
  `CompoundAction`. It is the one mutation that runs outside `executeTransaction`, and therefore
  the one with no single `BadCode:` undo entry.
- **`Project.importFiles` returns only `Promise<boolean>`** — not the imported items. To learn
  what arrived, snapshot the target bin's item ids, import, re-list, and diff.
- **`VideoFilterFactory.createComponent()` returns `VideoFilterComponent`, which is typed `{}`.**
  Cast it to `Component` before calling `getParamCount()` / `getParam(i)`. Whether an
  *un-inserted* component can report its params at all is still an open question — resolve it in
  T10 and record the answer here.
- **`VideoClipTrackItem` has no "get transition" accessor.** Transitions come back as separate
  items from `getTrackItems(TRANSITION, false)`; associating one with a clip means matching by
  time adjacency on the same track.
- **`TrackItemSelection.createEmptySelection(callback)`** really does take a callback rather than
  returning the selection.
- **`TickTime` has a `readonly seconds`** property — verified present in the declarations.
- Native effect match names are prefixed `PR.ADBE.*`; effects ported from After Effects are
  `AE.ADBE.*`. **No third-party vendor publishes their match names** — always discover with
  `premiere_list_effects` and confirm, never assume.

---

## `premiere_eval` in anger, 2026-08-22 (the blend-mode sweep)

Everything below came out of one job: sweeping `AE.ADBE Opacity`'s Blend Mode through every
integer. Four separate traps, and three of them silently produce a wrong answer rather than an
error.

### 🔴 `helpers.withTransaction`'s builder is SYNCHRONOUS and takes a CompoundAction

The signature is `withTransaction(project, label, build: (ca: CompoundAction) => void)`. The
builder must call **`ca.addAction(...)`**; it is not an async function and its return value is
discarded.

```js
// WRONG — does nothing, and reports success
helpers.withTransaction(project, 'x', async () => [param.createSetValueAction(kf, true)])

// RIGHT
const kf = param.createKeyframe(value)                       // resolve everything first
helpers.withTransaction(project, 'x', (ca) => { ca.addAction(param.createSetValueAction(kf, true)) })
```

**An empty transaction commits successfully.** `executeTransaction` returned `true` for a callback
that added no actions, so `withTransaction` did not throw and the caller had every reason to
believe the write landed. It had not: Opacity read back 100 after being "set" to 42. **Read the
value back after any write you care about** — the transaction returning is not evidence.

`withActions(project, label, thunks)` is the nicer helper the command modules use, but **it is not
exposed to `premiere_eval`** — eval gets `withTransaction` only.

### 🔴 A committed transaction invalidates every handle resolved before it

Reuse a `Clip`, `ComponentChain`, `Component` or `ComponentParam` across a commit and the next
native call throws **"The script object is no longer valid."** — the same error T8 hit on
`TrackItemSelection`.

So a loop that writes must re-resolve from the project down on **every** iteration:
sequence → clip → chain → component → param. This is the T10 note about applying an effect and
setting its params generalised: it is not about effects, it is about transactions.

### 🔴 Long transaction loops inside one eval exhaust Premiere and it does not recover mid-call

A single eval running **55 write-then-export cycles** worked for about 54 of them and then began
throwing "The script object is no longer valid." from `withTransaction` itself — with freshly
resolved handles. The typed `premiere_set_param` failed the same way immediately afterwards, so it
is a host-wide state, not an eval bug.

**It clears on its own.** A minute later the same call succeeded, and reads never stopped working
throughout. **Keep a loop inside one eval to roughly a dozen commits and split the rest across
calls.** A batch of 7 and a batch of 6 both ran clean.

### 🔴 `exportSequenceFrame` returns `true` for frames it never writes

T12 recorded that the promise resolves before the file is finished. It is worse than that under
load: of 55 exports that all returned `true`, **44 files existed** afterwards, and a later batch of
6 produced 4. The missing ones never appeared — this is not the settle delay, they are simply
absent minutes later.

The typed `premiere_export_frame` is safe (`waitForStableFile` in `src/server.ts` waits for the
file to exist and its size to hold). **Raw `ppro.Exporter.exportSequenceFrame` inside an eval is
not.** Check the file exists yourself and retry, or accept a lossy sweep and measure what landed.

### 🔴 A string parameter cannot be written — `Illegal Parameter type`

`AE.ADBE PPro SimpleText` param 5 is the text itself. It reads back `unreadable`, and writing it
throws `Illegal Parameter type`. Its *styling* params write fine — Size 120 and Opacity 100 both
landed and were confirmed in an exported frame that still read **"Default Text"**.

T10 recorded that unreadable params "can still be WRITTEN". **That is true of Lumetri's structural
params and false of this one** — unreadable does not imply writable. Expect the same of a MOGRT's
text fields when T11's write half is finally tested.


## MOGRTs, answered live 2026-08-22 (T11)

The question the research sweep raised three times, settled with pixels.

### ✅ `insertMogrtFromPath` works, and it is not an Action

```js
const editor = await ppro.SequenceEditor.getEditor(seq)
let inserted = null
project.lockedAccess(() => {
  inserted = editor.insertMogrtFromPath(winPath, tick, videoTrackIndex, audioTrackIndex)
})
// inserted: Array<VideoClipTrackItem | AudioClipTrackItem>, length 1 for a title
```

It runs **inside `lockedAccess` and outside `executeTransaction`**, exactly as the declarations
implied, and returns the created track items synchronously. The clip arrives named `Graphic`.

### The inserted MOGRT exposes MORE than expected — four components

| # | matchName | displayName | Params |
| --- | --- | --- | --- |
| 0 | `AE.ADBE Opacity` | Opacity | 3 |
| 1 | `AE.ADBE Motion` | Motion | 11 |
| 2 | `AE.ADBE Graphic Group` | **Vector Motion** | 6 — Position, Scale, Rotation, Anchor Point |
| 3 | `AE.ADBE Text` | **Text** | 22 — **param 0 is `Source Text`** |

So a MOGRT is not opaque. Its transform, scale, rotation and opacity are ordinary readable,
writable params, and `premiere_set_param` drives them.

### 🔴 …but `Source Text` cannot be written. `Illegal Parameter type`

| Route | Result |
| --- | --- |
| `getValueAtTime()` | throws — reports `unreadable` |
| `getStartValue()` | `null` |
| `getKeyframePtr()` | throws `Illegal Parameter type` |
| `areKeyframesSupported()` | **`false`** — the only param seen to return this |
| `createSetValueAction(createKeyframe('BADCODE'), true)` | throws **`Illegal Parameter type`** |

Verified with an exported frame: after writing Text ▸ Opacity 55 and Text ▸ Scale 140 (both
landed and both visible), the rendered title still read **"Your Title Here"**.

**The same is true of `AE.ADBE PPro SimpleText` param 5.** Two independent text params, same
refusal — this is how Premiere treats string params through UXP, not a MOGRT quirk.

### 🔴 It will NOT create a track, and says only "Invalid parameter"

`premiere_insert_clip` creates a video track when you address one past the last. **`insertMogrtFromPath`
does not.** Asking for `videoTrack: 3` on a three-track sequence throws a bare
`Error: Invalid parameter` with nothing to say which parameter was wrong — the path is fine, the
time is fine, the track is the problem. Insert onto an existing track, or make one with a clip first.

### Component count varies by template

`Basic Title` inserts with **four** components including `AE.ADBE Text`. `Bold Lower Third Left`
inserts with **three** — Opacity, Motion, Vector Motion, and **no Text component at all**. Do not
assume component index 3 is the text on an arbitrary template; read the chain back from the
`changed.added` entry the tool returns.

### The ruling

**T11's write half is answered: no. Do not build a workaround.** *(Kai, 2026-08-21: full
automation was never the goal.)* The working division is:

- **Automatable:** choosing the template, placing it at a timecode, its position, scale, rotation
  and opacity.
- **Handwork:** the words. `premiere-automation` skill §8.

What each installed template asks for is catalogued offline in
[`mogrt-catalogue.md`](mogrt-catalogue.md), so a hand-over can name the fields before anything is
placed.

---

## Markers hold exact time — they do NOT snap to the frame grid

Every clip edit snaps to a frame boundary (T8). **Markers do not.** 23 markers were written from a
beat grid at 175.78 BPM and read back at exactly the requested times:

```
asked  0.7147   11.6373   22.56   …   241.0133
got    0.7147   11.6373   22.56   …   241.0133
```

0.7147s at 25fps is frame 17.87 — not a boundary — and Premiere stored the tick unrounded
(`66.2507` came back as `66.25069999999606`, a float round-trip, not a snap).

**So a beat grid survives into Premiere at full precision**, which is what makes markers the right
carrier for one: the cut you place against the marker snaps, the reference itself does not.

### 23 markers, one transaction, one undo entry

`createAddMarkerAction` is an ordinary Action, so the whole grid goes in a single
`executeTransaction` — which is also how to avoid the script-object exhaustion above. It took
**1ms**.

```js
const markers = await ppro.Markers.getMarkers(seq)
helpers.withTransaction(project, 'beat grid', (ca) => {
  TIMES.forEach((t, i) => ca.addAction(markers.createAddMarkerAction(
    `phrase ${i + 1}`, ppro.Marker.MARKER_TYPE_COMMENT,
    helpers.secondsToTick(t), ppro.TickTime.createWithSeconds(0), 'note')))
})
```

🔴 **The constant is `ppro.Marker.MARKER_TYPE_COMMENT`.** `ppro.Constants.MarkerType` does not
exist and fails with `Cannot read properties of undefined (reading 'COMMENT')`.

🔴 **Reading markers back: use `premiere_get_sequence`, not your own probe.** `await m.start` on a
`Marker` handle returned 0 for all 23 while the typed tool reported every time correctly. The
panel's `dumpSequence` knows the right accessors; a hand-rolled read does not.


## Open questions

Things we will only learn by asking a running Premiere. Each is assigned to a ticket in
[`the plan`](../../design/2026-08-21-premiere-bridge-and-video-fx.md).

| Question | Why it matters | Ticket |
| --- | --- | --- |
| Can the bridge **SET** a MOGRT's exposed Essential Graphics parameters? | Blocks template-driven maps, charts and kinetic type. *Reading what a template exposes no longer needs Premiere at all — see below.* | T11 |
| Which integer is Screen on `AE.ADBE Opacity`'s Blend Mode, and which of its two Blend Mode params is live? | The one-call route for compositing Flow fire and smoke | — |
| `AE.ADBE PPro SimpleText` parameter list; `AE.Impact_Vignette_FX` and `AE.ADBE_Noise_FX` param indices | Titles without a template, and the two most BadCode effects there are | — |

---

## MOGRT definitions are readable without Premiere, 2026-08-22

A `.mogrt` is a **zip**, and the `definition.json` inside it carries `clientControls` — the exact
list of fields Premiere will show in the Essential Graphics panel, each with a stable GUID, a
type and a default value. Nothing has to be running to read it.

```bash
unzip -p "Basic Title.mogrt" definition.json | jq '.clientControls'
scripts/mogrt-catalogue.py --find "lower third" --controls   # does it for all 77
```

Control types, inferred from their shape across all 77 shipped templates (type `1` always carries
a boolean `value`; type `2` always carries `min`/`max`/`value`; `6` and `8` never carry a value,
and `8` is used for the unnamed and section-named separators):

| `type` | Control |
| --- | --- |
| 1 | checkbox |
| 2 | slider (with `min`/`max`) |
| 4 | colour |
| 6 | text |
| 8 | group header |

**77 templates, 317 editable controls** — 144 text, 93 colour, 51 checkbox, 29 slider. Full
inventory: [`mogrt-catalogue.md`](mogrt-catalogue.md).

### 🔴 Adobe's own templates name every text field `TextLayer`

A two-line lower third exposes `TextLayer` and `TextLayer`, and the definition cannot tell you
which is the name and which is the role. Only the two `[AE]` packages use meaningful names
(`Title`, `Subtitle`, `Team #1 Score`).

So this file answers *what boxes exist*, never *which box is which*. **Describe a hand-over by
position and purpose** — "the top field is the name" — never by the name the file gives it.

This does **not** imply the params are writable through UXP. That is still T11's open half.
