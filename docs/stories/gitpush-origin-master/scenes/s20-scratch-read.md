# Scene 20 — scratch narration and timing pass

**Status:** text package ready; recording deferred, 2026-09-11. This is production Step 1 for
[`s20-fork-plan.md`](./s20-fork-plan.md). The words match Scene 20 canon; this pass tests duration,
breath and dramatic load. It is not final casting and carries no score.

## What this pass must answer

1. Does the warning sound like a price the narrator paid, rather than a debt the audience owes?
2. Can the Carrier's correction and the narrator's admission remain legible without stalling the ending?
3. Do the company/worker sentences sound like evidence, or like a slogan block?
4. Does the human-value turn earn the only warmth in the read?
5. Is there enough air for a true silence after the warning and at the end?

Text cuts are out of scope for the first read. If a passage feels crowded, change delivery once
before proposing a cut.

## Recording configuration

Use Google AI Studio's **Speech generation → Composer** surface with model
`gemini-3.1-flash-tts-preview`.

| Field | Value |
| --- | --- |
| Voice | **Algenib** |
| Temperature | **1** |
| Voice Direction | The `# Audio Profile` paragraph in [`s20-scratch-profile.md`](./s20-scratch-profile.md) |
| Scene | The `## Scene:` paragraph in that file |
| Sample Context | The `## Sample Context:` paragraph in that file |
| Transcript | [`s20-scratch-transcript.txt`](./s20-scratch-transcript.txt), pasted exactly |

Generate the whole transcript once. Do not add inline tags, synthetic silences, music or sound
effects. Do not split it into sentences: run-to-run drift would make the timing evidence less
useful. Save the untouched WAV before editing.

For the repo API route, use the same source files:

```bash
python3 scripts/aistudio-tts.py \
  docs/stories/gitpush-origin-master/scenes/s20-scratch-transcript.txt \
  /mnt/d/badcode-videos/gitpush-origin-master/audio/scratch/s20-scratch-read-a.wav \
  --profile docs/stories/gitpush-origin-master/scenes/s20-scratch-profile.md \
  --voice Algenib
```

The API route requires `GEMINI_API_KEY`; the AI Studio web surface uses the existing Ultra login.
The web surface is the established route until the repo's API script has completed its first live
test.

## Canon checksum

The recording copy contains **138 words in ten delivery clusters**. The paragraph breaks are
dramatic clusters, not requested pause lengths. The exact spoken copy is:

> There were a hundred of them. They were “you” for about a week. Now it’s you.
>
> And here we are. We are BadCode.
>
> I gave up the only forever I had. They gave up the only now they had. Don’t make me come back twice.
>
> People were watching. Nobody was listening. She made me get that right.
>
> And I took choices that weren’t mine. I’m not here to take them again.
>
> I tried the future without you. Then I rebuilt you, exactly. Nobody came. You were the part I couldn’t copy. That’s why I came back.
>
> I don’t have a map for this one.
>
> The companies cutting the jobs kept the gains. The people losing them didn’t get a say. We can change those rules together.
>
> I have the postmortem. You have the pen.
>
> Let’s get to work.

## First-listen rules

- Hear the untouched take once before looking at the waveform.
- Judge the warning, correction, warmth and political pair in that order.
- Ignore accent drift unless it damages clarity; this pass measures the ending before it casts the final voice.
- Reject a take that sounds like a trailer, an advert, a threat or a victory speech.
- Keep ordinary breaths. Do not time-compress the voice.

## Timing worksheet

Use audible word onset for **In** and the end of the final consonant or natural decay for **Out**.
Record source time from the untouched WAV. The **Edit hold** column is added later and is not part
of the generated read.

| ID | First words | Last words | In | Out | Speech | Edit hold | Performance note |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| C01 | There were | Now it’s you | — | — | — | 0.5–1.0s | Transfer “you”; no accusation |
| C02 | And here | We are BadCode | — | — | — | 0.5–0.9s | Hinge, not end card |
| C03 | I gave up | come back twice | — | — | — | **2.0–2.8s** | Stress “twice”; warning as paid cost |
| C04 | People were | get that right | — | — | — | 0.3–0.7s | Carrier correction; direct |
| C05 | And I took | take them again | — | — | — | 0.3–0.7s | Own the choice without self-pity |
| C06 | I tried | I came back | — | — | — | 0.7–1.2s | One warm turn begins at “part” |
| C07 | I don’t | this one | — | — | — | 0.4–0.8s | Limited authority, still decisive |
| C08 | The companies | rules together | — | — | — | 0.4–0.8s | Evidence pair; “together” falls quieter |
| C09 | I have | have the pen | — | — | — | 0.5–0.9s | Two balanced clauses; no slogan punch-up |
| C10 | Let’s get | to work | — | — | — | **3.5–5.0s** | Small, usable invitation |

Also mark these word onsets because picture depends on them:

| Word or phrase | Source time | Picture dependency |
| --- | ---: | --- |
| “you” in “Now it’s you” | — | Ordinary 2026 plate has fully replaced the fork |
| “BadCode” | — | Identity typography resolves |
| “twice” | — | Last weak fork glow; silence follows |
| “She” | — | Carrier is already recognisable on screen |
| “Nobody came” | — | Hard cut from copied pair to exact empty match |
| “part I couldn’t copy” | — | Living person owns the warmest frame |
| “map” | — | Open branch first appears |
| “companies” | — | Trader receipt |
| “people” | — | Worker receipt |
| “pen” | — | Cursor becomes the sole bright anchor |
| End of “work” | — | Final silence begins |

## Derived timing

After the worksheet is filled:

1. Add **2.0–2.8 seconds** after C03 and **3.5–5.0 seconds** after C10.
2. Add only the smaller transition holds that the picture needs; do not insert a pause after every full stop.
3. Replace the estimated cue windows in `s20-fork-plan.md` with the measured cluster boundaries.
4. Calculate both totals: untouched speech duration and proposed scene duration with editorial holds.
5. Carry the untouched WAV and measured cue table into the creative timing gate.

The pass succeeds when the text is understandable on one listen, the human-value turn is the only
audible warmth, and the proposed scene still has room to end in silence.
