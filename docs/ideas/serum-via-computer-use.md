# Sound Design in Serum, by Computer Use

Point a desktop agent at Serum's actual interface — the wavetable window, the filter, the LFOs,
the macros — and let it *turn the knobs* to chase a described sound. Not a prompt to a music
model. A machine using a synthesiser the way a person does.

Kai saw a video of **GPT Astra 6's computer use** doing exactly this, and the two candidate
drivers on our side are **desktop Claude (Fable)** and **Codex desktop** — the desktop apps, not
the CLI, because this needs a real screen and a real mouse.

**Kai, 2026-09-12: not now.** Music comes out of Suno this season.

## What it would buy

- **The sound we already reference, actually made.** Serum *is* the camping track's reference
  synth — and the sheet has to work around not having it:
  `docs/stories/camping/songs/camping.md:453` records that Serum's name is deliberately kept out
  of the Suno prompt (brand names are unreliable and risk alias collisions), so we ask for
  `screaming detuned wavetable lead, hard-synced, bending, formant-morphing, gnarly mid-range`
  and hope. With Serum in the loop we stop describing the sound and start owning it.
- **A patch is a file.** A prompt is not. A `.fxp` is reusable, versionable, and identical every
  time — a house sound instead of a lucky roll.
- **It generalises past Serum.** Whatever can drive one plugin GUI can drive any of them.

## What it costs

- **Slow and expensive per attempt.** Computer use is screenshot-look-click-look. Sound design is
  hundreds of small moves. This is the opposite of cheap iteration.
- **A judgement problem we have only half solved.** The agent must *hear* the patch to know
  whether the knob helped. `design/2026-09-11-claude-can-hear.md` is our listening work and it is
  **paused at ticket T3** — AI Studio returns 403 to Chrome for Testing, and the fix is a branded
  Chrome. Without ears this is a blind agent twiddling.
- **It runs where the DAW runs.** Serum lives on the Windows host, so this is a desktop-app
  session on Windows, not a WSL session — a different operating posture from everything else here.
- **Unverified, entirely.** One video. We have measured none of it. Treat every claim above the
  line as "Kai saw a demo".

## What already exists to build on

- **`docs/stories/camping/songs/camping.md` §"How the synths are worded"** — the sound we want,
  already described in transferable terms, plus the reason we cannot name the plugin to Suno.
  That section is the brief for the first patch.
- **The listening tooling** (`design/2026-09-11-claude-can-hear.md`), which is the missing half.
- **The Flow browser-driving discipline** — `./scripts/browser-channel.sh claim`, PID locks, the
  rule that an agent never picks a port. Different surface, same "an agent is driving a UI a human
  also uses" hazards.
- **The Premiere bridge as the alternative** to compare against: an *API* bridge is precise and
  brittle; computer use is general and slow. See [Ableton Automation](ableton-automation.md) —
  the two are complements, not rivals.

## What un-parks it

- The listening tools come off pause (T3), so an agent can judge its own patch.
- Or: a Suno track fails specifically on the synth, twice, and rewording does not fix it.
- Or: desktop Claude / Codex desktop computer use gets demonstrably good enough that a
  half-day spike is a fair bet. **Cheapest first test:** one session, one described sound, one
  patch, timed — then decide.
