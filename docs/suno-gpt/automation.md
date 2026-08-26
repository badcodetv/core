---
title: Suno automation — the DOM, the traps, and the operating protocol
status: recon complete and live-validated 2026-08-24 · no MCP server built yet
scope: MECHANICS only — driving the Suno web app over CDP. What to WRITE in the boxes is `suno-prompt`.
validated: Chrome for Testing 148, suno.com/create, Advanced Mode, v5.5, account `binocarlos`
---

# Suno automation

**The machine half of Suno.** How to drive the app, and nothing about what to put in the boxes.

This is the Suno counterpart to
[`flow-automation`](../../.claude/skills/flow-automation/SKILL.md). The split is deliberate
and load-bearing:

| Job | Where it lives | Question it answers |
| --- | --- | --- |
| **Driving it** | **this doc** (and the `suno-automation` skill, once built) | Which selector? Why did it silently do the wrong thing? |
| **Writing for it** | [`suno-prompt`](../../.claude/skills/suno-prompt/) + [`README.md`](./README.md) | What words go in the Style box? |
| **How to work** | [`session-method.md`](./session-method.md) | One variable per round; diagnose before rewording |

Everything below was **proven live** on 2026-08-24 unless a row says otherwise. The
distinction matters: this whole file exists because eight plausible-looking approaches
silently produced the wrong result.

---

## 1. Connecting

Suno runs in **the same Chrome as Flow** — `scripts/flow-chrome.sh`, CDP on
`http://localhost:9222`. No second browser, no second login.

```ts
const browser = await chromium.connectOverCDP('http://localhost:9222')
const page = browser.contexts()[0].pages().find((p) => p.url().includes('suno.com'))
```

`close()` on a `connectOverCDP` browser only **detaches** — it never kills Kai's Chrome.
Same contract as `flow-client.ts`.

### 🔴 Scripts must be `.mts`, and page code must be a STRING

Two traps, both from `tsx`:

1. **Top-level `await` needs `.mts`.** A `.ts` file is transformed as CJS and every
   `await` at module scope is a build error.
2. **`page.evaluate(() => …)` throws `ReferenceError: __name is not defined`.** esbuild's
   `--keep-names` injects a `__name` helper that does not exist inside the page. This is
   exactly why [`flow-mcp/src/dom.ts`](../../packages/flow-mcp/src/dom.ts) stores its
   scrapers as **function strings** rather than functions.

The working form — note the wrapping parens and the trailing `()`:

```ts
const SCRAPE = `() => { /* page code */ }`
const out = await page.evaluate(`(${SCRAPE})()`)
```

Passing the bare string returns **the function object**, which is not serialisable, so the
call quietly resolves to `undefined`. It looks like an empty page, not a bug in the call.

---

## 2. 🔑 The golden rule: scope everything to the Advanced panel

**Suno mounts the Simple panel and the Advanced panel at the same time.** Both are in the
DOM, both carry the same `aria-label`s and placeholders. So:

- `button[aria-label="Add Voice"]` matches **two** elements
- `input[placeholder="Song Title (Optional)"]` matches **two** elements
- one copy is `display:none`, the other is often scrolled to a **negative `y`**

Playwright strict mode errors on the first; `.first()` picks the wrong one about half the
time; and `scrollIntoViewIfNeeded()` cannot rescue a genuinely hidden node.

**The fix is one helper.** Anchor on the styles wrapper — the only element unique to the
Advanced panel — and walk up to the container that also holds the lyrics editor:

```js
const panel = () => {
  const w = document.querySelector('[data-testid="create-form-styles-wrapper"]')
  if (!w) return null
  let n = w
  for (let i = 0; i < 12 && n; i++, n = n.parentElement) {
    if (n.querySelector('[aria-label="Lyrics editor"]') &&
        n.querySelector('input[placeholder="Exclude styles"]')) return n
  }
  return document.body
}
```

Then query inside `panel()` and keep only nodes with `offsetParent !== null`.

**Corollary — click natively, not through Playwright.** The live Advanced control is often
scrolled out of view inside its own scroll container, so Playwright's visibility gate times
out after 30s. The `flow-mcp` forceClick recipe applies unchanged: `el.scrollIntoView({block:
'center'}); el.click()` inside a page eval.

---

## 3. The selector table

Every row verified live.

| Control | Selector | Notes |
| --- | --- | --- |
| **Mode tabs** | `button[role="tab"][aria-label="Advanced"]` | also `Simple`, `Sounds` |
| **Style box** | `[data-testid="create-form-styles-wrapper"] textarea` | 🔑 the only stable anchor |
| **Style char counter** | text node matching `/^\d+\/1000$/` inside that wrapper | Suno counts for us |
| **Exclude styles** | `input[placeholder="Exclude styles"]` | plain input, `fill()` works |
| **Lyrics** | `[aria-label="Lyrics editor"]` | contenteditable — see trap 2 |
| **Weirdness** | `[role="slider"][aria-label="Weirdness"]` | `aria-valuenow`, step 1 |
| **Style Influence** | `[role="slider"][aria-label="Style Influence"]` | `aria-valuenow`, step 1 |
| **Audio Influence** | `[role="slider"][aria-label="Audio Influence"]` | **only exists after a Voice is attached** |
| **Voice** | `button[aria-label="Add Voice"]` | two of them — use `panel()` |
| **Voice card** | ancestor with class `cursor-pointer` | a `div`, **no** `role="button"` |
| **Model** | button whose text matches `/^v\d/` | reads `v5.5` |
| **Title** | `input[placeholder="Song Title (Optional)"]` | two of them — use `panel()` |
| **Workspace** | button in `panel()` reading `Save to...<name>` | opens a picker |
| **Workspace search** | `input[placeholder="Search or create..."]` | selects **or creates** |
| **Credits** | `[aria-label^="Credits remaining"]` | free budget reporting |
| **Create** | `button[aria-label="Create song"]` | 🔴 **not** `aria-label="Generate"` — that is the *Lyricist* button and is usually disabled |
| **Clip row** | `[aria-label="Select clip"]`, `Like clip`, `More options` | one set per take |

**Never anchor on the Style box's placeholder.** It is built from the rotating recommended-style
chips (`slide, battle rap, breathy voice…`) and there is a **Refresh recommended styles** button
next to it. It changes under you.

---

## 4. 🔴 The eight traps

Each of these produces a *plausible-looking* result. None of them errors.

### Trap 1 — "Overwrite Styles?" when attaching a Voice

Attaching a saved Voice pops a dialog:

> **Overwrite Styles?** This Persona has styles. Do you want to overwrite your current styles?
> · **Overwrite** · **Keep Current**

**The ruling is absolute: always Keep Current.** Ruled by Kai, 2026-08-24 — *"we decline to
overwrite the styles every time."*

Why it matters here specifically: the `badcode newsreader` persona's own styles are the
**orchestral cut's** — football-terrace crowd chant, drum and bass, 174 BPM. Clicking
Overwrite on a narration generation replaces a near-silent two-instrument bed with a
174 BPM D&B track, and the Style box will *look* populated afterwards.

Automation must click **Keep Current** unconditionally and log that it did.

### Trap 2 — the lyrics editor is Lexical

`fill()` on `[aria-label="Lyrics editor"]` puts all the text into **one `<p class="lyrics-paragraph">`
as a single text node with raw `\n` characters**. It renders convincingly. It is wrong: Lexical's
editor state has one paragraph, so the line structure Suno reads is gone — and this sheet's whole
architecture is bracket cues on their own lines.

**Pasting by hand is fine** — a real clipboard paste fires Lexical's paste handler, which splits
paragraphs correctly. This is purely a robot problem.

The fix: clear, then insert line by line.

```ts
await lyr.click()
await page.keyboard.press('ControlOrMeta+a')
await page.keyboard.press('Delete')
for (let i = 0; i < lines.length; i++) {
  await page.keyboard.insertText(lines[i])          // instant, not per-character
  if (i < lines.length - 1) await page.keyboard.press('Enter')
}
```

**Verify by counting `<p>` elements, never by counting characters.** The broken version has the
right character count and one paragraph.

### Trap 3 — there are three `[role="dialog"]` nodes

`document.querySelector('[role="dialog"]')` regularly returns an **empty** one. Filter by
`offsetParent !== null` and take the last, or search the whole document and walk up.

This cost a false "voice not found" during recon while the voice card was plainly on screen.

### Trap 4 — the create form does not survive navigation

Clicking **Library**, or any reload, **wipes the entire create form**: Style → 0 chars,
excludes → 0, lyrics → 1 empty paragraph, both sliders → 50, Voice detached.

There is no draft recovery. Before this doc that meant re-pasting four boxes by hand; now it
means re-running the loader.

**Never navigate away with a loaded form.** If you must, reload from the sheet afterwards.

### Trap 5 — the Style box truncates silently at 1,000

The textarea carries a browser-enforced **`maxLength="1000"`**. An over-cap paste is not
rejected — the **tail is dropped**, and the tail is where the arc lives (the impact, the dead
air, the climb that stops).

This confirms at the DOM level what
[`narration.md`](../stories/gitpush-origin-master/songs/narration.md) §3 already ruled. Automation
gets the check for free: compare the source length against `textarea.value.length` after filling,
and read Suno's own `n/1000` counter as a second opinion.


### Trap 6 — the right-hand pane is shared

The clip list and the **workspace browser** occupy the same pane. Opening the Save-to picker
leaves the pane on the browser, so `[aria-label="Select clip"]` matches **zero** elements and a
take listing comes back **empty even though the takes exist**.

Restore it by **clicking the current workspace's row**, not by navigating — navigation would wipe
the create form (trap 4). `listTakes()` in the script does this automatically.

### Trap 7 — "Save to…" and the workspace name are different elements

The label reads `Save to...`; the workspace name lives in a **sibling button**. Two consequences:

- Reading the name by taking the *last* matching element yields an **empty string**. Take the
  **longest** match, which is the container holding both.
- The button's own text is the **current workspace name** — arbitrary, and different on every
  visit. Matching the picker button by text picked the sidebar nav instead. **Anchor on the
  `Save to...` label container** and take its button.


### Trap 8 — there are TWO duration controls and only one is Advanced Mode's

| | Simple panel | **Advanced panel** |
| --- | --- | --- |
| Control | `input[placeholder="Auto"]`, `type=number` | **`[role="slider"][aria-label="Duration"]`** |
| Range | 1–300 | **10–360**, step **5** |
| Toggles | `Custom` / `Auto` buttons | none in-panel |

**They are not linked.** Setting the number input leaves the slider exactly where it was — so
writing to it does nothing at all in Advanced Mode, silently. Verified by nudging the slider
(180 → 175) while the input stayed on 32.

Two further facts about the slider:

- It lives inside **More Options**, which is **collapsed by default and unmounts its contents.**
  "The duration control has disappeared" almost always means that section is shut — not that a
  Voice hid it, which was a hypothesis worth testing and is **false** (verified on a clean page:
  the control is present with `badcode newsreader` attached).
- More Options' trigger is a React div that **ignores a native `el.click()`**. It needs a real
  mouse click at the element's coordinates.

⚠️ **A step of 5 means an exact target is often unreachable**, and a naive "press toward the
target" loop **oscillates around it forever**. `setSlider` now stops as soon as a press stops
getting closer. This bit Duration first but protects every slider.

🖐 **Kai's manual route for an exact value:** choose **Custom**, then **double-click the number**
— it becomes a text box you can type into. Not automated; the slider's 5-second granularity is
inside our ±10s tolerance, so automation drives the slider.

---

## 5. The operating protocol

Kai's working practice, ruled 2026-08-24. Automation must implement all three.

### 🔑 Every attempt is a PAIR, not a generation

Every time we try something, we run it at **both** weirdness settings:

| | Style Influence | Weirdness |
| --- | --- | --- |
| **Take A** | 75 | **30** |
| **Take B** | 75 | **60** |

*"Sometimes weirdness 60 works better, sometimes weirdness 30 works better. I've not yet worked
out which rule to apply."* — Kai, 2026-08-24

So the automation unit is **load once → set w30 → Create → set w60 → Create**. Style influence
stays at 75 across both. Never generate at only one setting; the comparison is the point, and
the rule is still being learned.

**This is also a research programme.** Each pair is a data point on when 30 beats 60. Log the
verdict with the pair so the rule can eventually be stated.

### 🔑 Timing — narration must land within ±10s of the picture

Narration is cut against built picture, so a take that misses the budget badly costs an edit.
**Ruled 2026-08-24: a narration take should land within 10 seconds of its cut's budget.**

| Cut | Budget | Set duration to |
| --- | --- | --- |
| 1 · awakening | 56s | ~60 |
| 2 · the push | ~27.8s | ~30 |
| 3 · plant room | 40s | ~45 |

🔴 **Aim slightly ABOVE the budget, never below.** Suno's duration is a **target, not a
contract**, and our own toolkit's §10 records that it **shortens reliably and repeatedly fails to
stretch**. Long is trimmable; short is a reshoot.

Set it in the spec as `durationSec`. Omit it for Auto.

### Naming

Every track gets a title before Create. The scheme:

```
<story>-<cut>-<revision>-w<weirdness>
gpom-cut1-A-w30
gpom-cut1-A-w60
gpom-cut1-B-w30      ← prompt changed, revision letter advances
```

The **revision letter advances every time the prompt changes** — that is Kai's existing habit
(A, B, C, D…), preserved.

**Cost per Create: 10 credits, 2 takes.** So one full pair is 20 credits and 4 takes. Budget is
readable at any time from `[aria-label^="Credits remaining"]`.

> 🔴 **Collision to resolve.** `narration.md` calls the three *scenes* "Gen A / Gen B / Gen C",
> while Kai's letters mean *prompt revision*. A bare `A` is now ambiguous. The scheme above
> dodges it by never using a bare letter — the cut is always named — but the sheet's "Gen A/B/C"
> labels should probably become "Cut 1/2/3" to kill the ambiguity at the source.
> **Owed a ruling.**

### Workspaces

📎 **The workspace lands in the URL** as `suno.com/create?wid=<uuid>` once selected, so a session
can be resumed straight into the right workspace.

Work is organised into workspaces, set via **Save to…** before Create. `gpom-story` already
exists (112 clips). The picker's `Search or create...` input both selects an existing workspace
and creates a new one, so automation can guarantee a scene's takes land together.

Set the workspace **before** generating — it routes the output, and moving clips afterwards is
manual.

### 🔴 Never automate downloading

**Ruled by Kai, 2026-08-24.** Suno is about to introduce a licensing constraint that **limits
downloads per month**. A script that downloads takes would burn a metered, finite allowance
without anyone deciding to spend it.

- ❌ no automated WAV/MP3 download
- ❌ no automated stem splitting
- ✅ generate, name, file into a workspace, and **stop**

Downloading stays a deliberate human act. This is a hard rule, not a default.

---

## 6. What is verified, and what is not

Honesty about this is the point of the table — several recon assumptions failed on contact.

| Claim | Status |
| --- | --- |
| CDP attach to the Flow Chrome reaches Suno | ✅ proven |
| Style box fills to exactly 903 chars, counter agrees | ✅ proven |
| Exclude styles fills | 🟡 **proven but flaky** — see the truncation row |
| **Exclude box truncates on a multi-id run** | 🔴 **proven, four times** — 2026-08-25/26, EVERY time on the *second* variation of a run: 117/831, 169/871, 180/695. The kept prefix length varies, which rules out a `maxlength` and reads like stale React state winning a race against `.fill()`. Fix: clear → blur → refill → blur → read back, retry ×4 (`fillChecked` in `style-ab.mts`). A length assertion before Create is what makes a bad fill free |
| **`setTaste` writes My Taste** | ✅ **proven 2026-08-26** — read back at 1207/1207 chars. Previously listed nowhere because "it clicked Save" is not evidence; `getTaste` is the read-back half and is now in `suno.mts` |
| **My Taste is account-wide and outlives everything** | 🔴 **proven, expensively** — it belongs to no sheet, survives reloads, is invisible from the create form, and applies to every generation. On 2026-08-26 it was found still holding the *GPOM newsreader* profile ("**one** dark gravelly British male voice… **pure spoken narration**… **Music I love: almost nothing**") through fourteen Camping cover rounds. **Read it back at the start of every session, back it up before writing it, restore it after.** See [`camping-style.md`](../stories/camping/songs/camping-style.md) §1 |
| **Create mode is identifiable by its sliders** | ✅ proven — Weirdness + Style Influence only; no Audio Influence control exists with nothing attached. The cheapest proof a run is not secretly a cover |
| Lyrics land as 15 real paragraphs via per-line insert | ✅ proven |
| `fill()` collapses lyrics to one paragraph | ✅ proven (that's how we found it) |
| Sliders driven by keyboard, step 1, read back from `aria-valuenow` | ✅ proven for all three |
| Audio Influence appears only after Voice attach | ✅ proven (absent, then 25, set to 50) |
| Voice attaches; Overwrite dialog appears; Keep Current works | ✅ proven |
| Title sets via the native value setter + `input` event | ✅ proven |
| Workspace picker selects an existing workspace | ✅ proven (`gpom-story`) |
| Workspace picker **creates** a new workspace | ⬜ **not tested** — input says "Search or create…" |
| Form is wiped by navigation | ✅ proven (accidentally) |
| Whole Gen A set loads in one command | ✅ proven end-to-end |
| **Create click** | ✅ proven — 10 credits per click, 2 takes per click |
| **Form survives its own generation** | ✅ proven — style, excludes, lyrics, sliders, voice and title all intact afterwards |
| Takes land in the selected workspace, titled | ✅ proven |
| Reading clip rows back (title + duration) | ✅ proven |
| Advanced duration slider sets and reads back (`Duration=30`) | ✅ proven |
| The Simple number input is a different, unlinked control | ✅ proven |
| An attached Voice hides the duration control | ❌ **disproved** — it does not |
| **That a set duration actually changes the take's length** | 🟡 **partly** — 2026-08-25, a 200s target moved takes from 4:30–4:46 to 4:07–4:24. It shortens, it does not obey: treat it as a ceiling to aim under, never a floor |
| Take/clip harvesting from the workspace list | ⬜ not attempted |
| Model picker (changing v5.5 → other) | ⬜ not attempted; reads correctly |

🔑 **The form survives its own generation** — proven 2026-08-24. So the pair is cheap: load once,
Create, then **nudge the slider and retitle**, Create again. No reload between halves. This is what
makes `suno_pair` a single call rather than two full loads.

Two things still unproven: **creating a new workspace** through the picker (only selecting an
existing one has been exercised), and **harvesting** beyond reading titles and durations off the
clip rows.

---

## 7. Build order

1. ✅ **This doc** — the spec.
2. ✅ **[`scripts/suno/suno.mts`](../../scripts/suno/suno.mts)** — the working tool.
   `status` · `extract` · `load` · `pair` · `takes`. All verified live except `pair`, whose parts
   (`load` + Create + slider nudge + retitle) are each proven.
3. ✅ **[`.claude/skills/suno-automation/`](../../.claude/skills/suno-automation/SKILL.md)** — the
   mechanics skill, split from `suno-prompt` exactly as `flow-automation` is from `flow-prompt`.
   `suno-prompt`'s description now hands code-driving over.
4. ⬜ **`packages/suno-mcp`** — promote the script only if it outgrows a script. Mirror `flow-mcp`'s shape. Tools:
   `suno_status`, `suno_load` (style/excludes/lyrics/sliders/voice/title/workspace, with the
   Keep-Current guard and the paragraph assertion baked in), `suno_pair` (the w30/w60 protocol),
   `suno_generate`, `suno_list_takes`. **No download tool — by rule.**

The split line, now fixed: `suno-prompt` keeps **human** click-paths (stems, Studio, Voice
creation) and all prompt craft; `suno-automation` owns **programmatic** driving over CDP.

### Optional, later: the listening pre-filter

`narration.md` §5's fastest rejection test — *"what happens when he stops talking?"* — is
mechanically measurable: find the speech gaps, measure RMS energy inside them. A take where the
music steps forward has loud gaps. The same analysis flags percussion (transient onsets) and
checks the ending decays rather than resolving.

**It is a pre-filter, not a judge.** It would discard obvious fails so ears are only spent on
takes that already pass. Judging stays human. Note this needs local audio, which collides with
the no-download rule — so it applies only to files Kai has chosen to download anyway.

---

## 8. The working loader, in full

Proven end-to-end 2026-08-24. This is the prototype `suno_load` — keep it until the MCP
package replaces it. Run as `.mts`; see §1 for why.

```ts
// ── sliders: keyboard only. aria-valuenow is the source of truth; step is 1.
async function setSlider(page, label: string, target: number) {
  const s = page.locator(`[role="slider"][aria-label="${label}"]`)
  if (!(await s.count())) return `${label}: absent`
  await s.first().focus()
  const read = async () => Number(await s.first().getAttribute('aria-valuenow'))
  let cur = await read(), guard = 0
  while (cur !== target && guard++ < 300) {
    await page.keyboard.press(cur < target ? 'ArrowRight' : 'ArrowLeft')
    const next = await read()
    if (next === cur) break            // hit an end stop; do not spin
    cur = next
  }
  return `${label}=${cur}`
}

// ── title: React-controlled, so the native setter + a bubbling input event.
//    A plain `.value = x` is swallowed on the next render.
const setTitle = (val: string) => `(() => {
  const inp = [...panel().querySelectorAll('input[placeholder="Song Title (Optional)"]')]
    .filter(x => x.offsetParent !== null)[0]
  if (!inp) return 'no title input'
  Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value')
    .set.call(inp, ${JSON.stringify(val)})
  inp.dispatchEvent(new Event('input', { bubbles: true }))
  return 'set'
})()`

// ── workspace: open "Save to…", type into "Search or create...", click the row.
//    Set it BEFORE generating — it routes the output.

// ── voice: click the live Add Voice, click the card's cursor-pointer ancestor,
//    then ALWAYS Keep Current, then set Audio Influence (which only now exists).
const keepCurrent = `(() => {
  const b = [...document.querySelectorAll('button')]
    .find(x => /^keep current$/i.test((x.innerText||'').trim()))
  if (b) { b.click(); return 'kept' }
  return 'no-overwrite-dialog'
})()`
```

**Order matters.** Voice must be attached before Audio Influence exists, and the workspace must
be set before Create. Verify at the end by reading back — never assume a step took.

### The verification that actually catches things

```js
{
  styleLen: styleTextarea.value.length,          // must equal the source length
  lyricParas: lyricsEditor.querySelectorAll('p').length,  // 🔑 paragraphs, NOT characters
  sliders: [...document.querySelectorAll('[role="slider"]')]
    .map(s => s.getAttribute('aria-label') + '=' + s.getAttribute('aria-valuenow')),
}
```

Character count passes on a broken lyrics load. **Paragraph count is the only check that fails
when trap 2 fires.**

---

## Revision log

- **2026-08-24** — created. Full DOM recon of `suno.com/create` over CDP; five traps found and
  worked around; Gen A of the GPOM narration loaded end-to-end in one command (style 903,
  excludes 336, lyrics 15 paragraphs, voice attached, sliders 75/30/50, title `gpom-cut1-A-w30`,
  workspace `gpom-story`). Kai's rulings recorded: decline Overwrite every time, pair every
  attempt at weirdness 30 and 60, name every track, file into a workspace, never automate
  downloads.

- **2026-08-24 (Create proven)** — Kai authorised clicking Create. The full pair ran end to end for
  GPOM cut 1: `gpom-cut1-A-w30` then `gpom-cut1-A-w60`, both into the `gpom-story` workspace,
  20 credits, 4 takes. Three facts learned: the button is **`aria-label="Create song"`** (the
  `Generate` label belongs to the Lyricist and is usually disabled); **the form survives its own
  generation**, so the second half of a pair is a slider nudge plus a retitle rather than a reload;
  and the workspace id appears in the URL as `?wid=<uuid>`.

- **2026-08-24 (shipped as a skill)** — the recon became reachable capability:
  `scripts/suno/suno.mts` (status / extract / load / pair / takes) plus the
  **`suno-automation`** skill, with `suno-prompt`'s description narrowed to hand code-driving
  over. One more trap found while generalising: **the workspace picker's button text is the
  current workspace name**, which is arbitrary — matching it by text picked the sidebar nav
  instead. Anchor on the `Save to...` label container.


- **2026-08-24 (duration)** — Kai: narration must land within ±10s of the picture, so track length
  needs controlling. Added `durationSec` to the spec and `setDuration()` to the script. Trap 8
  found: **two duration controls exist and they are not linked** — the number input with
  Custom/Auto belongs to Simple; Advanced's is a 10–360 slider inside the collapsed More Options
  section. Writing to the wrong one does nothing, silently. `setSlider` hardened against a step
  that cannot land on the target exactly (it used to oscillate). **Whether a set duration actually
  binds is not yet proven** — it needs one generation.
