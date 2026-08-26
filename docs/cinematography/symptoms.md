# Symptoms — start here when something looks wrong and you can't say why

The complaint in ordinary words, what is actually causing it, and what to change. Written for
the moment someone looks at a frame or a cut and says *"I don't know, it's just boring."*

Brief 12 was commissioned to produce this table and returned prose instead; this is our
synthesis across the whole corpus. Rows marked 🔴 are the ones that fire most often on
BadCode work.

---

## A. The single frame

| You say | It's probably | Change this |
| --- | --- | --- |
| 🔴 "It's flat" | Only one depth plane is populated — a subject against a backdrop, nothing near, nothing far | Put something in the foreground. Anything: a doorway edge, a cable, a rail, haze. Depth is layers, never resolution *(principle 1)* |
| 🔴 "It looks like AI" | The named bundle: too symmetrical, too evenly lit, too much in focus, generic setting, no gaze pulling anywhere, light with no traceable source | Break one axis hard — kill the fill, put the light behind something, obstruct a third of the frame, make the setting specific to *this* story |
| "It looks like a stock photo" | Same bundle from the other direction: a scene built to mean nothing in particular so it could be reused anywhere | Give it one detail that could only be here. Generic is the disease; specificity is the whole cure |
| 🔴 "I don't know where to look" | No single focal point — everything at the same visual weight | Pick the one thing. Give it the light, the space, or the depth position; take those away from everything else *(principle 2)* |
| "It's busy / cluttered" | Midground clutter, the most common flatness bug in generated stills | One clean subject beats three ambiguous ones. Delete, don't rearrange |
| 🔴 "It's just dark / muddy" | Near-black with no bright anchor — the eye has nothing to normalise against, so it reads as a broken file rather than as chosen darkness | Add one small deliberately brighter region. A rim, a practical, a screen. This is the highest-value fix in the file *(principle 11)* |
| "The dark bits look grey, not black" | Diffusion models pull toward mid-grey; near-black is structurally uphill for them | Name the single source AND state where the falloff goes. "Deep falloff into shadow" is an instruction; "dark" is not |
| "It feels staged / posed" | Unmotivated light — no traceable source in the world | Name the source and put it somewhere specific *(principle 10)* |
| "It's fine but boring" | Eye-level, dead-on, evenly lit, nothing hidden — the exact recipe for furniture | Break at least one of: height, light, or information withheld |
| "It's pretty but it doesn't do anything" | Composed for resolution rather than tension — balanced, centred, closed | Off-centre the subject, converge the lines onto it, violate the headroom *(principle 5)* |
| "It feels like a diorama" | No implied off-screen world; the frame contains itself | Cut something off at the edge. Aim a gaze out of frame. Let a shape run past the border *(principle 7)* |
| "Nothing's at stake in it" | Everything is shown, so there is nothing to discover | Withhold. A partial view, a shadow, an obstruction |
| "The building's big but not scary" | Scale is unmeasurable — nothing of known size in frame | Add a doorway, a stair, a vehicle, a figure. Size without a reference is abstraction *(principle 26)* |
| "The empty room isn't creepy, it's just empty" | Shot too wide or too high — from a distance human proportions stop being legible and it reads as geometry | Get close and low enough that a doorway, a desk, a seat-back still reads as human-sized. **This is exactly what we found the hard way on the GPOM `vantage` cut** |
| "The person doesn't look small enough" | Scale contrast is stated rather than composed | The figure must be *in* the frame with the thing, on a legible depth plane — not cut to separately |

## B. Light and colour

| You say | It's probably | Change this |
| --- | --- | --- |
| "Everything's the same colour" | No colour plan for the piece — each frame graded on its own | Decide the palette across the whole cut first. We can't fix drift in the edit the way a DP can *(principle 15)* |
| "It looks like a movie poster" | Teal-and-orange, or complementary contrast used everywhere instead of once | Complementary contrast is a pop. Spend it once. It reads as an effect the second time it's noticed |
| "It doesn't feel lit by anything" | No warm/cool contrast in frame | One warm source against a cold ambient — most of what "production value" actually means *(principle 17)* |
| "The shadows have gone to mush after upload" | Compression allocates fewest bits to dark, low-detail regions — our whole frame | Add grain or dither before encode; check range tagging. See [`../video-fx/delivery.md`](../video-fx/delivery.md) |
| "It looked fine here and terrible on YouTube" | Full/limited colour-range mismatch, untagged file — everything below a threshold clipped to black | This shipped once already in `camping.mp4`. Run the QC script, never eyeball it |

## C. Motion and the clip

| You say | It's probably | Change this |
| --- | --- | --- |
| 🔴 "The move doesn't add anything" | The camera moved without a reason | Ask what the movement means that stillness would not. No answer, no move *(principle 27 → `motion-and-cutting.md`)* |
| "It looks like a photo, not a shot" | First and last frame identical | Even a still needs one thing to change — light drift, haze, a slow breath of camera |
| "It's trying too hard" | Movement on every shot, so no shot's movement lands | A single move in a still body of work hits hard. The economy only works if the surrounding stillness is real |
| "The push-in feels cheap" | Pushing on nothing — a push-in means narrowing attention toward a realisation, so there has to be one | Put something at the end of the push worth arriving at |
| "The camera feels shaky for no reason" | Handheld reached for as a shorthand for realism | Handheld is a style, not truth. Locked-off with the right content beats wobble every time *(ruling R7)* |

## D. The cut and the sequence

| You say | It's probably | Change this |
| --- | --- | --- |
| 🔴 "It's a pile of nice shots, not a scene" | No argument — the shots don't step | A scene is a small argument. Every shot is a step in it, or it's decoration *(→ `motion-and-cutting.md` §2)* |
| 🔴 "It feels random / chaotic" | Shot size jumping with no direction, so the viewer can't tell what the change means | Pick a direction (wide→close is the default "moving toward the truth") and hold it |
| "I'm lost, I don't know where we are" | Geography never established, or established late | One wide, once, early. Then every closer shot spends its whole budget on feeling instead of re-explaining |
| "It drags" | Shots held past the point they finished delivering | There is no correct length. Cut the instant the frame stops earning. A wide with nothing left to read dies at 2s |
| "It's fast but it isn't exciting" | Speed mistaken for tension — fast cutting produces a different *kind* of tension, not more of it | Contrast is what lands. A held shot next to fast cutting beats uniformly fast |
| "The ending just stops" | No button — no shot closing the transaction the scene opened | End on one shot, often small, that closes it. Punctuation, not the last frame you happened to have |
| "The two shots don't go together" | They do — the viewer's brain invents a relationship whether you meant one or not | Use it deliberately. Juxtaposition is editorial opinion, and it's the entire toolkit of satire *(ruling R4)* |
| "The transition is clunky" | Hard cut between unrelated images with nothing carrying across | Let sound arrive early or linger late (a J-cut or L-cut) — two unrelated images become one thought |
| "The reveal didn't land" | It was a surprise, not a reveal | A reveal is a withheld shot. Decide what the audience may not see yet, and for how long |

## E. Register and meaning

| You say | It's probably | Change this |
| --- | --- | --- |
| 🔴 "It looks impressive but I feel weird about it" | **The aspirational-reading risk.** Monumental grammar with no visible cost reads as celebration of the power it means to indict | Gate 2: put a cost in frame — wreckage, exhaustion, a body that failed, someone the system is failing *(principle 23)*. **This is the check to run before anything monumental ships** |
| "It feels like it's showing off" | Awe reached for without accommodation — the frame explains itself instantly | Withhold. Slow the reveal. Let the viewer's understanding lag the image *(principle 25)* |
| "It feels cold / I don't care about anyone" | The register is doing scale when the beat needed a person | Ruling R2 — spend a tight human-scale frame here, deliberately, as the exception |
| "It's preachy" | The image is being explained — by a caption, a line, or a narrator naming what the object represents | An objective correlative dies the moment anyone says what it means. The moral is never stated; the beneficiary always is |
| "The motif isn't landing" | One or two occurrences, or three too faint to recognise at a glance | Three occurrences, composed to rhyme hard enough to be clocked instantly. Two is a coincidence |
| "The ending doesn't tie back" | No bookend | Repeat or invert the opening composition as the closing one, and let the difference carry the theme. Highest value, lowest cost structure we have |

## F. Text on the picture

| You say | It's probably | Change this |
| --- | --- | --- |
| "The caption fights the image" | Text placed without treating it as a compositional element | Caption placement is a blocking decision. Put it where the scan path already goes, never over a face |
| "The white text is hard to read on black" | Pure white on pure black causes real optical bleeding (halation), worst for readers with astigmatism | Off-white on near-black. Maximum contrast is not maximum readability |
| "The caption is just saying what I can see" | Redundant narration — the fastest way to kill a still's tension | A caption carries only what the eye cannot get: motive, causality, irony, the named beneficiary |

---

## When the answer isn't here

- The frame is fine but the *story* isn't → [`story-craft/symptoms.md`](../story-craft/symptoms.md)
- You know what you want but not how to ask the tool for it → the `flow-prompt` skill
- You know what you want but not which tool → the `video-fx` skill
- It's a delivery or upload problem → [`../video-fx/delivery.md`](../video-fx/delivery.md)
