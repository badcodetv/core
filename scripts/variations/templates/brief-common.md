# Brief: <story> <scene>, round <N> (common to every writer)

<!-- Template (Jack, 2026-11-17). Copy into the round's clean-room folder and fill the <...> parts from RAW inputs
     only: the human's words, the scene's geometry.md, the story's look.md. Never paste in earlier prompts or briefs.
     Writers run sealed: scripts/variations/sealed-writer.sh or the clean-room-writer agent. -->

You write prompts for <engine and model, e.g. Google Flow's Nano Banana 2 (stills)>. Read ONLY the files named in your
task. Research the web freely for how the real thing looks and behaves.

## The shot's facts first
- What happens in the scene, in plain facts: <two or three sentences>.
- Where everything is: read `geometry.md` (every vehicle's lane and direction, where the camera stands and which way it
  looks). Write those as plain physical facts in every prompt.
- People: <who is in shot; if a reference image is attached, call them "the person from the reference image" and do
  not describe their face or body unless the brief says so>.

## The look: one line
<ONE line copied from the story's look.md, e.g. its "In one sentence". Not a paragraph.>

## Rules for every prompt
- One paragraph, your own words, under ~200 words. <aspect ratio>.
- Describe only what should be in the picture; never name the thing to leave out.
- No real person's name. No readable text except <the slogan, if any>.
- End every prompt with "Thanks."

## Output
Write a JSON array of {"id","look","prompt"} to the file your shot brief names. Each prompt a genuinely different idea.
Reply with one line per prompt.
