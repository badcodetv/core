---
name: suno-automation
description: Use when DRIVING Suno from code rather than by hand — loading a sheet's prompt boxes into suno.com/create, clicking Create, running the weirdness pair, filing takes into a workspace, listing what came back, or fixing a Suno automation call that silently did the wrong thing. Triggers on "automate Suno", "load this into Suno", "generate this in Suno", "run the pair", "click create", "put this in the gpom-story workspace", "paste the boxes for me", "what takes are in there", "the lyrics went in wrong", "it overwrote my styles", or any request to avoid pasting four boxes by hand. Mechanics only — what to WRITE in the boxes belongs to `suno-prompt`.
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
before changing any selector.** It carries the DOM map, the seven silent traps, the operating
protocol and the verified/unverified table. Every workaround in the script exists because the
obvious approach produced a plausible-looking wrong result.

🛠 **The tool is [`scripts/suno/suno.mts`](../../../scripts/suno/suno.mts).**

## Preflight

Suno runs in **the same Chrome as Flow** — one browser, one login.

```bash
scripts/flow-chrome.sh                       # if not already up
npx tsx scripts/suno/suno.mts status         # reads the create form back
```

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

### 🔑 Naming

`<story>-<cut>-<revision>-w<weirdness>` — e.g. `gpom-cut1-A-w30`. The **letter is the prompt
revision** and advances every time the prompt changes. Never a bare letter: the sheets also use
A/B/C for scenes.

### 🔑 Workspaces

Set the workspace **before** Create — it routes the output, and moving clips afterwards is
manual. The workspace id lands in the URL as `?wid=<uuid>`.

## The six traps that will bite you

Full detail in the knowledge base; this is the short list.

| Trap | What it looks like | The rule |
| --- | --- | --- |
| **Overwrite Styles?** | Attaching a Voice offers to replace your Style box with the persona's own — for `badcode newsreader` that's the orchestral 174 BPM chant. Box looks populated afterwards. | **Always Keep Current.** The script does this and logs it. |
| **Lexical lyrics** | `fill()` puts all lines in ONE paragraph with raw `\n`. Renders convincingly, structurally destroyed. | Insert line by line. **Verify by counting `<p>`, never characters.** |
| **Two panels mounted** | Selectors match twice; one copy hidden, one at negative `y`. | Scope to the Advanced panel via the styles wrapper; keep `offsetParent !== null`. |
| **Navigation wipes the form** | Clicking Library or reloading clears everything. No draft recovery. | Never browse mid-load. Re-run `load`. |
| **Shared right pane** | Opening the workspace picker replaces the clip list with the workspace browser, so a take listing comes back **empty though the takes exist**. | Click back into the workspace. **Never navigate** — that wipes the form. |
| **Save-to naming** | The picker button's text is the *current workspace name*, and the label is a separate element. | Anchor on the `Save to...` container; take the **longest** match to read the name. |

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
