# Tricks: methods that work for any story

> Part of the [library](../README.md). Like the looks and sounds, a trick applies to a story only once that
> story lists it under **Library pieces in use** in its `badcode.md`. These are methods, not styles: none of
> them says what a picture should look like or a song should sound like.

| Trick | What it does | Use it when | How |
| --- | --- | --- | --- |
| **Real photo as the look** | Find a real photo on Unsplash and give it to Flow as the reference. Flow follows the reference image more than the prompt, so the photo sets the look and the prompt only says what happens. | Starting a scene's stills, or when every still is coming back looking like AI | `python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>"` → picks page → the picked photo goes in the story's `badcode.md` (Jack, 2026-11-13) |
| **Clean room** | Fresh web research plus sealed writers who read one brief file and nothing else from the repo. Breaks the "every prompt sounds the same" habit. | New looks, new sounds, or when results keep coming back samey. Jack's word for it is "clean room". | `variations` skill, `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent. Never `general-purpose` writers. Rules: `docs/rules/flow.md` §clean room |
| **Music before picture** | Make the track first, then cast and shoot to the voice. You can't know what the singer looks like until you hear them. | Any music video, or any short scored in Suno | Script → Suno track → pictures built around it (Kai and Jack, 2026-11-13 and 2026-11-17) |
| **The BadCode balaclava** | Anyone in the BadCode balaclava is BadCode in person. It also gets round lip-sync. | A story that wants BadCode on screen | The fixed rules (ring and triangle, gloves, no skin) are a brand rule: [`docs/brand/README.md`](../../brand/README.md) §"The BadCode balaclava" |
| **Same-prompt check** | Flags a prompt that copies an earlier one or carries habit phrases. Runs by itself before every Flow and Suno call. | Always on; run it by hand for prompts typed elsewhere | `python3 scripts/variations/fresh.py` |

Add a trick by adding a row here, written as a method with no look or sound in it.
