# docs/ — the BadCode knowledge base

Four content sections, a few toolkit folders, and three core context files. If you're
about to add a file here, it goes in exactly one of these places.

## Content sections

| Section | What lives here | Goes in when… |
| --- | --- | --- |
| [`stories/`](./stories/) | Per-story canon (`stories/<story>/` — concept, characters, beats, songs). Source of truth for everything a story produces. | …we've committed to making it. Promoted from `ideas/` via the `new-story` skill. |
| [`ideas/`](./ideas/README.md) | The idea inbox — raw, minimal-prose seeds with an index table. | …it just popped and we want it out of our heads. Captured via the `new-idea` skill. |
| [`marketing/`](./marketing/README.md) | Marketing & release plans — channels, campaigns, positioning, launch sequencing. | …it's about *reaching people*, not making the thing. |
| [`misc/`](./misc/) | Anything that fits none of the above. | …in doubt. Better parked here than lost. |

The promotion path is **`ideas/` → `stories/`**: an idea graduates when we commit to it
and `new-story` scaffolds its canon folder.

## Toolkit & production (skill-owned — don't file content here)

- [`shorts/`](./shorts/README.md) — short-form music-video packages (`music-video-short` skill)
- [`images/`](./images/README.md) — standalone brand imagery catalogue (`new-image` skill)
- [`suno-gpt/`](./suno-gpt/README.md) — Suno toolkit (`suno-prompt` skill): prompt language, the control sliders, the recurring-narrator stack, and what Suno reliably gets wrong
- [`flow/`](./flow/README.md) — Google Flow toolkit, two halves: **craft** (Nano Banana and Veo prompt craft, camera vocabulary, consistency, policy blocks) and **automation** (how `@badcode/flow-mcp` drives the browser — selectors, DOM roles, harvest)
- [`premiere/`](./premiere/README.md) — Premiere Pro bridge (`premiere-automation` skill): the UXP panel + WebSocket setup that lets a session build and adjust timelines. **[`setup.md`](./premiere/setup.md) is the one-time, per-machine install — start there**
- [`video-fx/`](./video-fx/README.md) — choosing the tool for a video job: the lane table (Flow invents / ffmpeg is exact / Premiere is the edit), the **no-paid-plugins** ruling and the free route instead, and the 20 research briefs. No `video-fx` skill yet — reach for `premiere-automation` and `flow-prompt`
- [`story-craft/`](./story-craft/README.md) — the story-craft toolkit (`story-craft` skill): thirty graded principles and sixteen house rulings, the adversarial review pass, the narrator pattern, per-form craft, the evidence table and case studies — distilled from the 24-brief sweep in [`../design/research/2026-08-22-story-craft/`](../design/research/2026-08-22-story-craft/README.md)
- [`superpowers/`](./superpowers/) — **archive only**: dated implementation plans & design specs. Nothing live lives here; the name is a fossil of a plugin we no longer run. Flow automation notes moved to [`flow/`](./flow/) on 2026-08-20

## Core context (read these first)

- [`vision.md`](./vision.md) — origin story, mission, themes
- [`voice.md`](./voice.md) — the load-bearing tone guide
- [`storytelling.md`](./storytelling.md) — how we craft a story (the method); the craft itself is [`story-craft/`](./story-craft/README.md)
- [`marketing/the-reader.md`](./marketing/the-reader.md) — **who the work is for** (ruled
  2026-08-15): the working-class reader drifting right, the ten rules for writing to them, and the
  traps. Evidence: [`misc/2026-08-15-target-reader-research.md`](./misc/2026-08-15-target-reader-research.md)
- [`using-ai.md`](./using-ai.md) — our position on making the work with AI: what we concede, what we
  don't, what we owe, and the sentences we never use. **Armour, not the campaign.** Evidence:
  [`misc/2026-08-15-anti-ai-research.md`](./misc/2026-08-15-anti-ai-research.md)
