---
name: suno-automation
description: Use when DRIVING Suno from code rather than by hand — loading a sheet's prompt boxes into suno.com/create, clicking Create, running the weirdness pair, constraining a track to a target length, filing takes into a workspace, listing what came back, or fixing a Suno automation call that silently did the wrong thing. Triggers on "automate Suno", "load this into Suno", "generate this in Suno", "run the pair", "click create", "make it 30 seconds", "constrain the length", "set the duration", "put this in the gpom-story workspace", "paste the boxes for me", "what takes are in there", "the lyrics went in wrong", "it overwrote my styles", or any request to avoid pasting four boxes by hand. Mechanics only — what to WRITE in the boxes belongs to `suno-prompt`.
---

# Suno Automation

**The machine half of Suno.** Everything about making the app do what the sheet says, and
nothing about what the sheet should say.

## What this is not

Three jobs touch Suno and they are deliberately separate. Reaching for the wrong one is how
guidance drifts.

| Job | Skill | Question it answers |
| --- | --- | --- |
| **Driving it from code** | **this skill** | Which selector? Why did it silently do the wrong thing? How do I not spend credits twice? |
| **Writing for it** | `suno-prompt` | What words go in the Style box? What lyrics? Which slider? |
| **How to run a session** | [`session-method.md`](../../../docs/suno-gpt/session-method.md) | One variable per round; diagnose before rewording |

`suno-prompt` also owns **human click-paths** — "what do I click to split stems", Studio, Voice
creation. This skill owns **programmatic driving over CDP**.

## Knowledge base

📖 **[`docs/suno-gpt/automation.md`](../../../docs/suno-gpt/automation.md) is mandatory reading
before changing any selector.** It carries the DOM map, the eight silent traps, the operating
protocol and the verified/unverified table. Every workaround in the script exists because the
obvious approach produced a plausible-looking wrong result.

🛠 **The tool is [`scripts/suno/suno.mts`](../../../scripts/suno/suno.mts).**

## Preflight

Suno runs in **this session's channel — the same browser as Flow**, one login per profile.

```bash
./scripts/browser-channel.sh claim suno       # picks + launches a channel, prints which
npx tsx scripts/suno/suno.mts status          # reads the create form back
```

### 🔑 Channels — ask for one, never pick a port (2026-08-26)

A **channel** is one CDP port plus one Chrome profile, merged into one number. `suno.mts`
resolves it as: `SUNO_CDP_ENDPOINT` → `FLOW_CDP_PORT` → **the channel this session's flow MCP
server has locked** → 9222. So Suno and Flow in one session share a browser (correct), and two
sessions never collide.

Nothing to configure: run `claim`, read the channel it prints, get on with it.

🔴 **`LOGGED_IN=no` means STOP and ask the user to sign in to Suno** in that window, naming the
channel. A fresh profile is always logged out — relaunching only makes a second logged-out
browser.
### 🔴 ONE Suno session at a time — the channel system does NOT make Suno concurrent (2026-08-27)

Browser channels give Flow safe concurrency because each channel is its own tab and profile.
**Suno defeats that, twice over, and both are account-level:**

1. **There is ONE create form.** It is a single shared surface. A second session running `load`
   **wipes whatever the first was holding, with no draft recovery.**
2. **My Taste is ONE account-wide box.** It cannot be turned off, is invisible from the create
   page, and applies to every generation on the account regardless of channel.

**So before touching Suno: check no other session is mid-run.** `status` is the tell — if the
form holds a title and workspace belonging to another sheet, **stop and ask** rather than
loading over it. Note the title, workspace, `styleLen`, `excludeLen` and sliders first, so the
other session can reload.

📎 **Proven the hard way 2026-08-27:** a GPOM narration session and a Camping session ran
simultaneously. The GPOM session read `status`, found a Camping cover loaded (`camping-duet`,
take c3), and loaded over it. Separately, the credit balance **dropped by 30 mid-session** —
the other session generating — which is the other reliable tell.

🔴 **We still never automate downloading.** Suno caps downloads per month and that allowance is
only ever spent by a human. Two channels do not double it.

Model: [`docs/flow/concurrent-sessions.md`](../../../docs/flow/concurrent-sessions.md).

`status` failing with `NO_CONTEXT` means Chrome isn't up. `status` returning nulls means the
create page isn't open — the script will navigate there itself on the next command.

## The loop

```bash
# 1 ── pull the four boxes straight out of the sheet (no transcription risk)
npx tsx scripts/suno/suno.mts extract \
  docs/stories/gitpush-origin-master/songs/narration.md "GEN A · CUT 1" > /tmp/spec.json

# 2 ── add how to file and grade it
#      { ...boxes, voice, title, workspace, styleInfluence, audioInfluence, weirdness }

# 3 ── load everything. Spends NO credits.
npx tsx scripts/suno/suno.mts load /tmp/spec.json

# 4 ── or load AND generate both halves of the pair
npx tsx scripts/suno/suno.mts pair /tmp/spec.json

# 5 ── read the takes back
npx tsx scripts/suno/suno.mts takes gpom-cut1
```

`load` is always safe. `pair` costs **20 credits** (10 per Create, 2 takes each).

## The rules that are not negotiable

### 🔑 THE ATOM — four boxes, one unit (Kai, 2026-08-27)

**A "style" is not the Style box. A style is FOUR boxes**, and they describe one sound:

| | |
|---|---|
| **My Taste** | account-wide, invisible from the create page, and the one that persists between runs |
| **Style** | the arrangement |
| **Exclude styles** | what it must not become |
| **Lyrics** | the words and their bracket cues |

🔴 **They change together or not at all.** Kai: *"if we're changing any of the prompts, we should
change all of the prompts… it's an atomic action."* Changing three of four leaves a **hybrid nobody
designed** — and because My Taste is the invisible one, it is always the one left behind.

📎 **This is not theoretical.** The GPOM newsreader profile sat in My Taste under **fourteen**
Camping cover rounds and a scouting set, demanding *one voice* for a two-man duet and *almost no
music* for a drum-and-bass track. Every "genre X didn't work" finding from those rounds is unsafe.

### 🔑 The two levels of change — and only two

Every round is one of these. Naming which one you are doing is the discipline.

| Level | What moves | What must NOT move |
| --- | --- | --- |
| **1 · Prompt round** | **all four boxes**, together | — |
| **2 · Slider round** | audio influence · style influence · weirdness | **every prompt box.** Not one word |

**A round that changes a prompt *and* a slider tells you nothing**, because two variables moved.
Within one atom you may run as many slider rounds as you like — that is the cheap axis, and it is
where the pair at weirdness 30/60 lives.

### 🔑 How sheets must be written

**Each experiment is a self-contained block holding all four boxes**, separate from every other
experiment — so a variation can be heard as fully itself.

Put the taste **inside the block** as a ```taste fence:

````markdown
#### variation-name

My Taste:

```taste
Vocals I love: …
Music I love: …
```

Style:

```
…
```

Exclude styles:

```
…
```

Lyrics:

```lyrics
…
```
````

`extract` reads the atom's own ```taste fence **first**, and only falls back to a shared section
for sheets written before this ruling. 🔴 **A shared taste section is the old, wrong model** — it
is precisely how a profile gets left behind when the style changes.

⚠️ **An INSTRUMENTAL atom has no lyrics** — taste + style + excludes is the whole of it, and that
is valid, not short.

### 🔑 What the tooling now enforces

- **`load` writes My Taste every time** and **reads it back**, aborting on a mismatch rather than
  generating against the wrong global box.
- **`load` REFUSES a spec with no `taste`.** Pass `applyTaste: false` only for a deliberate
  slider-only round — and then no prompt box may change either.
- **`npx tsx scripts/suno/suno.mts taste [block.txt]`** reads it; with a file it backs up, writes
  and verifies.

⚠️ **This costs a few seconds per generation** (the profile menu, the save, the read-back). Kai
ruled that latency worth paying: *"it might add an extra bit of latency… I think that's a thing we
absolutely need to do."*

### 🔴 Never automate downloading

Suno is introducing a licensing constraint that **caps downloads per month**. A script must
never spend that metered allowance. Automation generates, names, files into a workspace, and
**stops**. Downloading and stem-splitting stay deliberate human acts.

There is no download tool and there must not be one.

### 🔴 Credits are Kai's to spend

`load` freely. **Do not run `pair`, or click Create, unless the user asked for that round.**
Report the credit balance (`status` returns it) rather than assuming.

### 🔑 Every attempt is a PAIR

Style influence **75**, run once at **weirdness 30** and once at **weirdness 60**, titled
`…-w30` and `…-w60`. Sometimes 30 reads better, sometimes 60 does, and the rule that predicts
which is **not yet known** — so both always run, and each pair is a data point toward stating it.

Never generate at only one setting. **Record which won and why.**

### 🔑 Timing — narration lands within ±10s of the picture

Narration is cut against **built picture**, so a take that misses its budget costs an edit.
**Ruled 2026-08-24: within 10 seconds of the cut's budget.** Set `durationSec` in the spec.

| Cut | Budget | `durationSec` |
| --- | --- | --- |
| 1 · awakening | 56s | 60 |
| 2 · the push | ~27.8s | 30 |
| 3 · plant room | 40s | 45 |

🔴 **Always aim slightly ABOVE the budget.** Suno's duration is a **target, not a contract**, and
it **shortens reliably but repeatedly fails to stretch**. Long trims; short is a reshoot.

🔴 **Two duration controls exist and only one is Advanced Mode's.** The number input with
Custom/Auto is the **Simple** panel's, and it is **not linked** — writing to it does nothing,
silently. Advanced's is the slider `[role="slider"][aria-label="Duration"]`, 10–360, step 5,
inside **More Options** (collapsed by default; its trigger needs a **real mouse click**).

🖐 For an exact value by hand: hit **Custom**, then **double-click the number** — it becomes a
typeable text box. Automation uses the slider, whose 5s granularity is inside the ±10s tolerance.

⬜ **Not yet proven:** that a set duration actually changes the take's length. One generation
settles it — say so and it gets run.

### 🔑 Naming

`<story>-<cut>-<revision>-w<weirdness>` — e.g. `gpom-cut1-A-w30`. The **letter is the prompt
revision** and advances every time the prompt changes. Never a bare letter: the sheets also use
A/B/C for scenes.

### 🔑 Workspaces

Set the workspace **before** Create — it routes the output, and moving clips afterwards is
manual. The workspace id lands in the URL as `?wid=<uuid>`.

---

## 🔴 INHERITANCE IS A BUG. Declare the whole form, assert it, then Create.

**Ruled 2026-08-27, after four separate versions of the same failure in one day.** The create form
is **persistent, account-level and shared** — with a human, and with any other session. Every field
you do not set this run is a field someone else set, and **none of them error**:

| What leaked | How it looked | What it cost |
| --- | --- | --- |
| **My Taste** | invisible from the create page | fourteen Camping rounds under another song's profile |
| **A saved Voice** | 🔴 the worst one — **overrides the casting outright**, silently | a two-man duet generated as one newsreader |
| **Workspace** | takes simply appear somewhere else | twelve takes filed into another story, moved back by hand |
| **Duration** | a number left behind by another sheet | every take clipped, or padded, with nothing saying so |

**So a run must state its COMPLETE intended form state and verify the live form against it before
clicking Create.** Not just the boxes it is changing this round. Concretely, assert **all** of:
style length · exclude length · lyric paragraphs · My Taste (read back) · **attached Voice** ·
workspace · Weirdness · Style Influence · Audio Influence · Duration · title · (covers) the
attached audio.

🔴 **Voices specifically: assert NO voice unless the sheet names one.** With none attached the
control reads exactly `Voice`; attached, it reads the persona's **name**. A sheet that casts its
voices in the Style box — which is all the Camping sheets — must abort when anything is attached,
because a Voice beats the Style box and the take will sound *plausible*, just not cast.
`cover-genre.mts` carries the reference implementation (`EXPECT_VOICE` / `NO_VOICE`).

### 🔴 CHECK THE MODE BEFORE THE BOXES — the most expensive miss so far (2026-08-27)

**The create form has FOUR mode tabs — Simple · Audio · Custom · Cover — and an
`Audio / Voice / Inspo` attachment row. Filling the four boxes clears NONE of it.**

So a form inherited in **Cover** mode with a source attached **silently generates covers of
somebody else's track**, carrying that track's arrangement — while `status` reports style,
excludes, lyrics, sliders, title and workspace all perfectly correct.

📎 **What it cost:** two GPOM narration pairs (revisions A and B, **40 credits**) were generated as
covers of a Camping source left attached by another session. Both void. And it produced a
convincing false diagnosis — "there is music under my dry read" was blamed on the taste box and on
audio-influence bleed from the cloned Voice. **Those were real bugs and worth fixing, but the cover
attachment was the dominant cause and nobody had looked at it.**

🔑 **The lesson generalises: `status` reads the boxes, not the KIND of thing being made.** A
green-looking form is not a safe form.

`load` now calls `formMode(page)` **before it fills anything** and aborts when the mode is not
`custom` or when anything is attached. Pass `mode: 'cover'` in the spec when a cover is genuinely
wanted. ⬜ **The check reports; it does not clear.** Removing an attachment is still a human act —
the selectors have had exactly one live read and are otherwise unverified.

### 🔴 ONE SUNO TAB, EVER — Kai's ruling, 2026-08-27

*"I'm going to say that we're never going to run more than one Suno tab at a time, because I think
we're getting in a real mess here."*

**Not one session per channel. One tab, full stop.** Everything that matters is account-level — the
create form, its mode and attachments, My Taste, the Voice list, the credit pool — so two tabs are
two hands on one instrument. The freedom token below manages the handover **between** sessions; it
does not make them concurrent.

**If another session is working, WAIT.** Do not open a second tab to be helpful.

### 🔑 THE FREEDOM TOKEN — `MUST_REPLACE_HERE`

**Kai's ruling, 2026-08-27. A lock file in reverse.** My Taste **cannot be saved empty** — a
profile can only be *replaced* — so there is no neutral state to return to and every session
inherits whatever the last one left. This makes the free state explicit and loud:

| When | Rule |
| --- | --- |
| **Before any generation** | My Taste MUST read exactly `MUST_REPLACE_HERE`. **Anything else means someone owns the box — PAUSE AND ASK THE HUMAN.** Never load over it. |
| **After any generation** | Write `MUST_REPLACE_HERE` back. That is what hands the box to the next session. Do it on the failure path too — a half-finished round still leaves a profile installed account-wide. |

The token is deliberately nonsense: a human who hand-generates while it is in force sees gibberish
in the box and knows to fill it, instead of silently inheriting the wrong song's profile.

**Do NOT restore "the previous profile" afterwards.** That was the old behaviour and it was the
bug: `taste-backup` captured whatever was ambient and `taste-restore` faithfully reinstalled it,
so a leaked profile was preserved forever and looked like the house default.

Helpers in `suno.mts`: `TASTE_FREE`, `tasteOwner(page)` (null when free, else the live text),
`releaseTaste(page)`. Reference use: `cover-genre.mts` — gate 1 claims, gate 2 releases.
Taking the box off someone is one explicit command that backs up first: `… taste-release`.

🔴 **And Suno is not concurrent.** Browser channels make *Flow* parallel; they do nothing here,
because the create form, My Taste, the Voice list and the credit pool are all **account-level**.
**One Suno session at a time.** Run `status` first, and if the form holds another sheet's title or
workspace, stop and ask rather than loading over it.

## The seven traps that will bite you

Full detail in the knowledge base; this is the short list.

| Trap | What it looks like | The rule |
| --- | --- | --- |
| **Overwrite Styles?** | Attaching a Voice offers to replace your Style box with the persona's own — for `badcode newsreader` that's the orchestral 174 BPM chant. Box looks populated afterwards. | **Always Keep Current.** The script does this and logs it. |
| **Lexical lyrics** | `fill()` puts all lines in ONE paragraph with raw `\n`. Renders convincingly, structurally destroyed. | Insert line by line. **Verify by counting `<p>`, never characters.** |
| **Two panels mounted** | Selectors match twice; one copy hidden, one at negative `y`. | Scope to the Advanced panel via the styles wrapper; keep `offsetParent !== null`. |
| **Navigation wipes the form** | Clicking Library or reloading clears everything. No draft recovery. | Never browse mid-load. Re-run `load`. |
| **Shared right pane** | Opening the workspace picker replaces the clip list with the workspace browser, so a take listing comes back **empty though the takes exist**. | Click back into the workspace. **Never navigate** — that wipes the form. |
| **Save-to naming** | The picker button's text is the *current workspace name*, and the label is a separate element. | Anchor on the `Save to...` container; take the **longest** match to read the name. |
| **Two duration controls** | The Simple panel's number input is unlinked; writing to it changes nothing in Advanced. | Drive `[role="slider"][aria-label="Duration"]`. Expand More Options with a **real mouse click** first. |

Two smaller ones: the Style box **truncates** at its 1,000 cap rather than refusing (the script
asserts the length back), and `aria-label="Generate"` is the **Lyricist**, not Create — Create is
`aria-label="Create song"`.

## Verifying, not assuming

Every command ends by reading the form back. Two checks earn their keep:

- **`styleLen` must equal the source length** — otherwise the cap truncated it and the tail, where
  the arc lives, is gone.
- **`lyricParas` must equal the line count** — character count passes on a broken lyrics load, so
  paragraphs are the only check that fails when the Lexical trap fires.

`load` refuses to continue into `pair` if either assertion fails, so a bad load never spends
credits.

## When something goes wrong

| Symptom | Likely cause |
| --- | --- |
| `NO_CONTEXT` | Chrome isn't up — run `scripts/flow-chrome.sh` |
| `workspace:no-picker` / picked the wrong thing | The picker button's text is the *current workspace name*, so never match it by text — anchor on the `Save to...` label |
| `voice:not-found` | There are three `[role="dialog"]` nodes, most empty — search the document, not the dialog |
| Takes sound like the wrong song entirely | Overwrite Styles was accepted somewhere — check the Style box length |
| Bracket cues ignored in the read | Lyrics went in as one paragraph — check `lyricParas` |
| Everything blank after a command | Something navigated; re-run `load` |
| Timeout clicking a control | It's the hidden twin or it's in a scroll container — use the native `el.click()` recipe |

## Extending it

The script is deliberately a script, not yet an MCP server. If it grows past this, promote it to
`packages/suno-mcp` mirroring `packages/flow-mcp`'s shape — see the build order in the knowledge
base §7. **Do not add a download tool.**

Anything learned about the DOM goes **into the knowledge base**, with a note saying whether it was
proven live or only read. The verified/unverified table there is the point of the whole document.
