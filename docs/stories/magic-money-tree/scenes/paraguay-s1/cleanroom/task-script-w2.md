# Your task (script writer 2)

Read ONLY these three files in /home/jackt/projects/badcode/badcode/docs/stories/magic-money-tree/scenes/paraguay-s1/cleanroom/ :
brief-facts.md, research-comedy.md, research-engine.md. Do not read, list or search any other file on this computer.
You may search the web.

Write ONE complete version of the short described in brief-facts.md, with the jokes written (Jack will punch them up
later, so be bold and specific, not safe). The humour is the satirical-cartoon kind in research-comedy.md (blunt,
absurd escalation, everyone a fool, a point without a sermon) delivered in the deadpan street-reporter register.
Comic engine for YOUR version: He plays the earnest straight man: deadly polite, serious interview questions to people who are busy doing something absurd; the awkward pause is the joke.

Write with the Write tool to script-w2.json in that folder, exactly this shape:
{"title":"<3-6 words>","engine":"<one line>","voice_direction":"<how the presenter's voice-over should sound: accent, pace, attitude, 1-2 lines>",
 "beats":[{"t":"0.0-6.0","part":"REAL|REMADE|END","picture":"<what we see, incl. the streamer box when present>",
   "vo":"<presenter voice-over words, or empty>","on_screen":"<big overlay text / lower-third / caption, or empty>",
   "meme_flash":"<0.5-1 s meme cutaway: describe the image + its text, or empty>","sound":"<ambience / sting / music cue>"}],
 "flow_shots":[{"id":"<short id>","for":"streamer box|remade|end|meme","describe":"<what the generated shot must show, plain words>"}]}
Keep the whole short 15-20 s; VO must fit (about 2.5 words per second). Reply "done".
