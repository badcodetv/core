# Brief: three short video clips (image-to-video), portrait 9:16

You write motion prompts for an image-to-video model (Google Flow, "Omni Flash", Frames mode: each still below is the START FRAME, 8 seconds). Research on the open web how to prompt image-to-video models well (Google's Flow / Veo prompting guides, recent practitioner write-ups). Read ONLY this brief and the three images named here; open no other file on this machine.

The film: an 11-second UK satirical short, no dialogue. A terraced street at dusk with every political party's election sign in the front gardens; someone wheels their green wheelie bin to the kerb; the camera goes into the bin; inside, looking up at the lid, a logo lights up (the logo is added later in editing, never by you).

## Hard rules
- The camera does not move in any clip (an editor adds pushes later). Say so at the start and end of each prompt.
- One deliberate motion per clip plus at most one ambient motion. Few movers.
- No speech. No new text, signs or logos; the existing signs stay exactly as they are and unreadable changes are not wanted.
- Write constraints positively ("the lid stays closed"), not "no ...".
- Photographic realism: say it is shot at 24fps with a 180-degree shutter (natural motion blur).
- Ask for one continuous shot with no cuts. Each prompt ends with the word "Thanks."
- Under ~80 words each.

## The clips
1. **Start frame `ST1-a.jpg`** (street of signs; a person by a green bin in the middle distance). The person wheels the green bin the last few steps to the kerb, leaves it there and walks back toward the house. Ambient: one car's headlights pass, or nothing.
2. **Start frame `LD2-b-a.jpg`** (green bin lid close up at the kerb, signs behind). A faint, cool glow switches on from under the lid's front lip, as if something inside the bin just lit up, and holds steady. The lid stays closed; the bin stays still; the street stays as it is. Ambient: raindrops on the lid.
3. **Start frame `IN1-b.jpg`** (inside the bin looking up at the closed lid's underside). Thin seams of light at the lid's edges flicker gently like a passing streetlight; the bags shift very slightly. The lid stays closed; the flat square panel in the centre stays plain and evenly lit (a logo is added there later).

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "prompts": {"1": "...", "2": "...", "3": "..."}}
