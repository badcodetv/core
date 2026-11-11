# Brief: four short video clips (image-to-video), portrait 9:16

You write motion prompts for an image-to-video model (Google Flow, "Omni Flash", Frames mode: the still below is the START FRAME, 8 seconds, no audio used). Research on the open web how to prompt image-to-video models well (Google's own Flow / Veo / Gemini video prompting guides, recent practitioner write-ups). Do NOT read any file other than this brief and the four images named here.

The film: a 20-second satirical UK short. A black-and-white TV charity appeal asks viewers to sponsor a wealthy politician ("Crispin only earns £100,000 a year"). Pull back: it is playing on the old TV of a freezing pensioner in a cold council flat. Junk mail drops: a "Sponsor a Chancellor" flyer. She reads it and says, with real pity, "Poor bastard...". Played straight; the joke is in the words, not in mugging.

## Hard rules
- The camera does not move in any clip (an editor adds pushes later). Say so at the start and end of each prompt.
- The people are already in the start frame. Never describe their appearance, clothes, age or face: only position, action, expression.
- No speech, no singing, no on-screen text requested. (Exception: clip 4, see below.)
- One deliberate motion per clip plus at most one ambient motion. Few movers.
- Write constraints positively ("his hand stays on the glass"), not "no …".
- For anything photographic and moving, say it is shot at 24fps with a 180-degree shutter (natural motion blur).
- Ask for one continuous shot with no cuts.
- Each prompt ends with the word "Thanks."

## The clips
1. **Start frame `AP1-b.jpg`** (black-and-white man behind a rainy conservatory window). TWO prompts, chained: **1A** from this still; **1B** starts from 1A's last frame. Idea: 1A, he looks out, rain running down the glass, one slow sad blink. 1B, his hand slides slowly down the pane, a single raindrop tracks down the glass beside his face. Slow, solemn, charity-appeal sincerity. Black and white must stay black and white.
2. **Start frame `RM2-b-a.jpg`** (pensioner in her armchair watching an old TV, seen from the hallway). Idea: she sits still with her mug; the TV light flickers on her; her breath shows faintly in the cold; steam from the mug. Stillness is the point.
3. **Start frame `PO2-b-b.jpg`** (looking down at junk mail on a doormat; a flyer among it). Idea: nothing moves but a cold draught under the door lifts one leaflet corner and lets it fall. The flyer itself stays still and flat.
4. **Start frame `NA1-a.jpg`** (close-up, the pensioner reading a flyer). Idea: she reads, a small sad shake of the head, then says the words "Poor bastard" quietly, with pity. Write it as `She says: Poor bastard` (no quotation marks). Her mouth must form those two words clearly and slowly; the audio is replaced afterwards. Then she holds, still, lips closed.

## Output
Write ONE JSON file at the path you are given: `{"research": ["source url — one-line takeaway", ...], "prompts": {"1A": "...", "1B": "...", "2": "...", "3": "...", "4": "..."}}`. Each prompt under ~90 words.
