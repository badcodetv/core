# Sound effects brief (clean room)

You write prompts for **Suno's "Sounds" tab** (Create → Sounds): a text box "Describe the sound you want", a Type
switch (One-Shot or Loop), an optional BPM and Key. Each Create returns two takes. **Research the internet first**:
Suno's own notes on Sounds, practitioner write-ups and tests of it (2026), and how sound designers describe these
particular sounds so a generator gets them right (mic position, distance, room, duration). Base your prompts on what
you find. Do not read any file on this machine except this brief.

## The film
A 14-second vertical UK short. Night, rain, a British city. Inside an NHS ambulance two paramedics fight to save a
dying old man while the driver forces through traffic. At a red light a police motorcycle outrider holds them so a
government minister's black saloon can glide across. The patient flatlines; silence; black. It must sound like a real
British emergency on film: close, physical, unshowy. Voices and music are made separately; your sounds sit under
shouted dialogue.

## The sounds needed (one prompt each)
1. `siren`: a UK ambulance siren heard from INSIDE the vehicle (muffled by the body of the van, close and loud), running at speed (0-5.5 s), then it cuts off as they stop.
2. `monitor`: a patient heart monitor's beeping, fast and getting faster (a dying patient), dry, inside the ambulance (0-7 s).
3. `cabin`: the bed under it all: heavy rain on the roof of a vehicle, the diesel engine, road noise, a little rattle of equipment (a loop).
4. `stop`: the ambulance braking hard to a stop on a wet road (one hit, about 2 s).
5. `passby`: a big quiet luxury saloon gliding slowly past in the rain, tyres hissing on wet tarmac (3-4 s).
6. `flatline`: a patient monitor's continuous flatline tone, one steady pitch, dry (4+ s).

## Output
Write JSON to the path you are given:
{"research": ["url: takeaway", ...],
 "sounds": [{"key": "siren", "type": "One-Shot"|"Loop", "bpm": null, "prompt": "...", "why": "one line"}, ... six]}
Each prompt is plain English, in your own words. Keep each under 300 characters unless your research says longer works better.
