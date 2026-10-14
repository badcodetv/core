# Money For Something 2026, round 2: the new shots and their prompts

**Status: written 14 October 2026. Jack: "do all of it ... avoid AI slop ... use the cinematography file and skills".**
The lines are in [`money-for-something-2026-joke-pass.md`](./money-for-something-2026-joke-pass.md) and the shooting
script. Every prompt below is the exact text sent; every revision is logged under it.

**Rules applied** (from `docs/google-flow/README.md`, `2026-10-08-anti-slop-sweep.md`, `nano-banana-2.md` §anti-slop,
`docs/cinematography/`): a brief in sentences near 115 words; the capture named once and carried through; one
positioned key light plus one light of a different colour; saturated colours named per place; an imperfection on a
surface; a soft foreground occluder; off-centre; no "photorealistic", "cinematic", "8K"; no golden hour; signage said
exactly or kept out; the engine's left/right placed by landmarks. Model: **Nano Banana 2** (the standing rule; the
request said "Pro 2", the free model was used). Every prompt ends "Thanks."

A fresh web pass on 14 October found nothing newer than the 8 October sweep.

## The shot specs (shot-craft, Design mode)

| | S1 Podcast host | S2 Water boss | S3 HS2 reporter |
| --- | --- | --- | --- |
| The job | The genre in one look: a smug wellness podcast | The guest who owns it all, comfortable | A live news shot of nothing happening |
| Register | Parody of the genre's own glossy look, dirtied | Same room, the reverse chair | Parody of a local-news live shot |
| Depth | Front: the mic's foam cover, soft. Middle: him. Back: neon, supplement tubs | Front: a jug of cloudy brown tap water, soft. Middle: him. Back: foam, a lamp | Front: rain on the lens edge, orange barrier. Middle: him. Back: an empty platform into the dark |
| The eye rests on | His face, lit warm | His face, then the gold watch | His face under the umbrella |
| The light | An amber desk lamp beside him; a hot-pink neon rim from behind | The same amber lamp from the other side; the pink neon behind | A sodium-orange floodlight high on one side; grey-blue dusk sky |
| Camera | Chest-up, three-quarter, slightly below his eye line across the desk, off-centre | Chest-up, three-quarter the other way, the same height | Waist-up, at his chest height, off-centre, a little tilted |
| The cost in frame | The shelf of his own supplements; a dried shaker | The undrinkable water in front of him | He is soaked; the platform is unfinished |
| Withheld | The guest (S1) / the host (S2): one speaker a shot | | Any train |
| What moves | Mouth, a nod; the wrist is already up in S2b | | Mouth; rain |

Flow cannot do: lifting a prop (S2b starts with the wrist already raised); small text (the neon and the book are large;
if garbled they go on in ffmpeg); two speakers in one clip (singles only).

## Prompts

### S1: the podcast host (still)

> A frame from a YouTube podcast video, full-frame mirrorless camera, 35mm lens, shallow focus, fine grain. A pale man of about thirty with swept-back blond hair and a thin moustache sits at a scuffed dark wooden desk in a small dark studio, chest up, a little off-centre, leaning on his forearms toward a big black microphone on a boom arm, mid-sentence, earnest. Plain black T-shirt, a silver ring. The microphone's grey foam cover is close to the lens at the lower corner, soft. Behind him, out of focus: black acoustic foam, a shelf of identical lime-green supplement tubs, and a large hot-pink neon sign in joined handwriting reading "The Toxin Cleanse Diary". A warm amber desk lamp beside him lights his face; the neon puts a pink edge on his shoulder. On the desk: a protein shaker with a dried film inside, tangled cable, a stack of square cards. Natural skin texture. 16:9. Thanks.

### S2: the water boss (still)

> Same studio as the reference image, the other chair, the camera turned the other way. A frame from a YouTube podcast video, full-frame mirrorless camera, 35mm lens, shallow focus, fine grain. A tanned man of about sixty with swept-back silver hair sits chest up, a little off-centre, relaxed, one arm on the scuffed desk, a thick gold watch on that wrist, a slight satisfied smile. Pale blue open-necked shirt, navy blazer. Close to the lens and soft: a glass jug of cloudy brown tap water with a lemon slice floating in it. On the desk by his hand: a hardback book standing up, its cover bright yellow with large black capitals reading "THE HIDDEN BENEFITS OF SEWAGE". A warm amber desk lamp lights his face from the side; a hot-pink neon glow behind him. Natural skin texture. 16:9. Thanks.

### S2b: the water boss showing the watch (still, from S2)

> Same man, same studio, same camera and light as the reference image. He holds his left forearm up toward the lens, wrist turned to show the thick gold watch, looking at the lens, pleased. Everything else unchanged. 16:9. Thanks.

### S3: the HS2 reporter (still)

> A frame from a local television news live report, broadcast video camera, rain on the lens at one edge. A soaked man of about forty-five in a cheap navy anorak stands waist up on an empty, unfinished concrete railway platform at dusk, a little off-centre, holding a black hand microphone with a plain grey foam cover at his chin and a dented black umbrella that is not helping. Hair plastered, face resigned. Behind him: a long bare platform running into the dark, a yellow edge line, orange plastic barrier fencing, a large blue sign with white letters reading "HS2". A sodium-orange floodlight high on one side lights his face and the rain; a grey-blue sky. Puddles, a soggy coffee cup on the ground. 16:9. Thanks.

## Characters and voices (Flow project cb27208c)

Made from the accepted stills. Names are descriptions, never a real person's name.

| Character | From | Voice preset (unused by MFS and Bank Robbery) | Performance text |
| --- | --- | --- | --- |
| Podcast Host | S1 | Fenrir | A British man of about thirty from the London suburbs. Earnest, breathy and intense, leaning into every word as if it is profound, a soft upward lift. A wellness podcaster. Speaking to one guest across a desk, not performing. |
| Water Boss | S2 | Schedar | An English company owner of about sixty, privately educated, Home Counties. Relaxed, smug and unbothered, slow and pleased with himself. Speaking to one interviewer across a desk, not performing. |
| HS2 Reporter | S3 | Zubenelgenubi | A tired English local news reporter of about forty-five from the Midlands. Flat, resigned, quick, standing in the rain. Speaking to a studio down the line, not performing. |

## Clip prompts (Omni 1.1 Flash, Ingredients: the still as the scene, the speaker's Character attached)

Template (short, the action first, the accent inside the speech clause, the audio named, no description of the
Character):

> Same shot as the reference image, locked off. [Who] speaks to [whom] in a [accent] voice, [manner]: "[line]" [one
> small action]. Audio: only his voice [room], no music. Thanks.

Lines, durations and outcomes are logged in the production file.
