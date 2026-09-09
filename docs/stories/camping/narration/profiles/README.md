# Voice profiles — the paste-and-render files

**What this is:** one file per built voice, holding the **exact prompt AI Studio composes** from
the four Composer fields, with the `## Transcript:` header left open at the end.

**Why they exist separately from [`../ai-studio-cast.md`](../ai-studio-cast.md):** that file is the
store and the argument — why each voice sounds the way it does. **These are the artefacts**, in the
shape `scripts/aistudio-tts.py` and the API want them, so a render is one command and never a
retype.

```bash
export GEMINI_API_KEY=...
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Kore --profile docs/stories/camping/narration/profiles/nell-kore.md
```

| Profile | Voice | Who | Status |
| --- | --- | --- | --- |
| [`nell-kore.md`](./nell-kore.md) | `Kore` | **The narrator.** Nell, 38 | ✅ **Ruled 2026-09-09** — Jack: *"the Kore one works."* First take |
| [`tarquin-zubenelgenubi.md`](./tarquin-zubenelgenubi.md) | `Zubenelgenubi` | **Tarquin, speaking** | ⬜ Built 2026-09-08, exported 2026-09-09. Lines and the five-group render plan: [`../tarquin-lines.md`](../tarquin-lines.md) |
| [`bob-algenib.md`](./bob-algenib.md) | `Algenib` | **Bob, speaking** | ⬜ Built 2026-09-08, exported 2026-09-09 with the Scene and Sample Context rewritten from narrator to character. Lines: [`../bob-lines.md`](../bob-lines.md). ⬜ Open: the build is southern English, `bob.md` says Scouse |

## ⚠️ Four faults in every AI Studio "Get code" export

[`scripts/aistudio-tts.py`](../../../../../scripts/aistudio-tts.py) is that export with all four
fixed. **They recur in every fresh copy**, so use the script rather than the paste:

1. **One file written per streamed chunk** instead of one file per render.
2. **A literal `ENTER_FILE_NAME_0`** as the output name.
3. **`num_channels = 1`** — 🔴 mono, and Premiere shows a mono clip red. **Rewrite to stereo.**
4. **The Transcript field holding the profile** rather than the spoken words.

## 🔑 Whitespace matters — save these clean

An export pasted out of a terminal carries **leading spaces on wrapped lines**. The profile above is
saved de-indented. ⬜ Untested whether the model cares, but a prompt is the one place to not find
out by accident.
