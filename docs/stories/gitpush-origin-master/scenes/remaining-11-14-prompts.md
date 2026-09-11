# Cuts 11–14 — the humans interrupt the film

**Status: complete text production board, 2026-09-11; no images or motion generated.**
Canon scenes 14–17: the shaft, vault, coin landing and experiments. The narration and dialogue in
[`story.md`](../story.md#scene-14--the-argument-up-the-ventilation-shaft) remain authoritative.
The short quotations below are edit cues, not a replacement script. Cut numbers follow
[`prompts.md §2c`](../prompts.md).

This board supplies **23 shot designs, 24 placements, from 14 new photographic plates**. Repeated frames,
modest crops and exact coin states are explicitly reuse or post work. Do not generate twenty-three
different compositions. Shot durations remain relative to the recorded performance; a held
correction is allowed to last as long as a human takes to say it.

## The cinematographic argument

The shaft first returns **sound**, then a practical light, then the people. The vault begins at the
machine's old surveying distance. On *“I asked”*, a hard cut gives up that distance. The Carrier's
correction then holds without a camera flourish. The coin pays off through an almost offensively
ordinary change inside a composition we already know. The experiments finally earn faster cuts:
disagreement, a spoiled trial and a failed shortcut are part of the partnership, alongside success.

The visual temperature moves R1 → R2: small low warm light entering cold space, then recognisably
occupied working rooms. Never cover the hundred in a uniform amber beauty wash. Their environment
contains repaired objects, practical labour and the food problem; their faces are not devotional
portraits. The AI has **no visible body, face, eyes, avatar, outline or reflection**.

Design basis: [`principles`](../../../cinematography/principles.md),
[`frame`](../../../cinematography/frame.md),
[`motion and cutting`](../../../cinematography/motion-and-cutting.md),
[`stills`](../../../cinematography/stills.md),
[`registers`](../../../cinematography/registers.md). The working choices below are shot-design
judgements, not claims that a lens or angle has a universal psychological meaning. Camera positions
and focal lengths are composition briefs, not measurements of images that do not exist yet.

## Continuity and reference contract

- **Carrier:** attach the existing `Carrier` Character for every generated frame containing her,
  even a soft shoulder. Identity source: [`carrier-sheet.jpg`](../characters/img/carrier-sheet.jpg).
  Verbatim DNA: **wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in
  slightly-wrong green; glasses on a braided cord.** Preserve the sheet's face and skin tone; do not
  infer a new ethnicity, polish the skin or change the wardrobe. A typed name does not cast her.
- **Refuser:** a staging identifier, not a new biography: **charcoal overshirt with one ochre cloth
  repair at the right cuff**. The face stays turned away or outside the crop. Name, gender, age,
  motivation and the reason for refusing remain open. Never cast a scowl, loner corner or sinister
  light as an explanation. Introduce this garment in `vault-refuser`; retain it in the incidental
  glance, ledger and launch. The pair remain on speaking terms.
- **The hundred:** mixed adult ages and builds, varied skin tones, maintained ordinary clothes.
  Make a community with tasks and different sightlines. Do not ask a generator to prove a count of
  100 or 40 through tiny faces. Canon narration establishes those counts; exact launch arithmetic
  belongs to the later graphic/mechanism plan.
- **Vault geography (`vault`):** storage shelving along screen-left, low warm battery lamp on the
  left bench; asymmetrical repaired worktables through the middle; ordinary workshop doorway on
  screen-right. Distant alcoves continue beyond the visible room. Keep the near doorway jamb as a
  continuity anchor. The Carrier addresses an off-frame interlocutor on the camera side, never a
  visible AI prop.
- **Rig geography:** the coin remains in the original rig chamber. The Carrier and later the
  passing refuser enter that existing space with a portable warm lamp. Do not silently redesign the
  glass or put a second coin rig into the vault's crowded workbench. Scene 17 alternates the rig
  chamber with collaborative analysis in the vault workshop; these are distinct views, not a
  claim that both rooms are one continuous set.
- **Rig authority from cut 8:** `C08-coin-rig-golden` (logical alias `coin`),
  `C08-coin-rig-clean`, and `C10-chair-golden` from
  [`remaining-07-10-prompts.md`](./remaining-07-10-prompts.md). The designed rig is a plain dull
  nickel disc, approximately 25 mm across and 2 mm thick, smooth edge; sealed clear hemispherical
  dome approximately 180 mm across on a continuous thin dark gasket; charcoal matte tabletop.
  Accepted appearance wins over those approximate dimensions. No added plinth, wires, hand access
  or mechanical actuator. C08 is the low 85 mm view; C10 is its wider chair view.
- **Coin causality:** **all spin, landings and resets are controlled in post**, using the approved
  coin appearance over the clean rig plate. The dome never opens. Nobody touches the glass, table
  or coin at the determining moment. No wind, glow, magnetism, pulse or particle goes from a person
  to the rig. Generated coin physics must not accidentally become the film's explanation. The
  unmarked disc cannot independently demonstrate “heads” versus “tails”; the unchanged narration
  names those outcomes. Do not invent a portrait or readable minting to repair that deliberate
  visual abstraction. Exact state changes and cue times are production work, not extra still prompts.
- **References:** each derivative below takes **one named image reference only**, plus the
  separately attached Carrier Character where specified. Select the actual accepted asset; prose
  naming a nonexistent file is not a reference. Same-view edits require geometry checks later.
  If the edit drifts, retain the approved plate and composite the changed region; do not accept
  shifting glass, doors, furniture or proportions as continuity.

**Frame convention:** landscape 16:9, fine natural 35 mm grain, muted cool-neutral surroundings,
deep readable shadows and a small motivated light anchor; no lens flare, vignette, generated text,
logos or fantasy effects. Character close shots deliberately override the old blanket “subject
small” instruction. Depth is created in staging, not by adding decorative fog.

## Dependency order — fourteen photographic plates

All IDs here are logical production names, not claims that a file exists. Store eventual media in
the active project's `clips/<scene>/` folders; these words remain in this repository.

| Order | Plate ID | Image reference / cast | Use |
| --- | --- | --- | --- |
| 1 | `shaft` | New image | C11.1–2 |
| 2 | `shaft-stores` | New image; repeat the described lower duct detail | C11.3 |
| 3 | `vault` | New image; Carrier Character | C12.1; location master |
| 4 | `vault-ask` | `vault`; Carrier Character | C12.2 |
| 5 | `carrier-correction` | `vault-ask`; Carrier Character | C12.3–4; **exact Scene 20 callback** |
| 6 | `vault-refuser` | `vault`; no face casting | C12.5; cuff/doorway staging master |
| 7 | `coin-witness` | `C10-chair-golden`; Carrier Character | C13.1 |
| 8 | `coin-warm-clean` | `C08-coin-rig-clean`; Carrier Character for sleeve | C13.2–3; C13.6; C14.5/7 |
| 9 | `coin-witness-response` | `coin-witness`; Carrier Character | C13.4 |
| 10 | `coin-refuser-pass` | `C10-chair-golden`; no face casting | C13.5 |
| 11 | `experiments-workshop` | `vault`; Carrier Character | C14.1–2 and C14.8–9 |
| 12 | `experiments-sneeze` | `experiments-workshop`; Carrier Character | C14.3 |
| 13 | `experiments-wanting` | `C10-chair-golden`; no recurring face | C14.4 |
| 14 | `experiments-crowd` | `experiments-wanting`; no recurring face | C14.6 |

The accepted C08 clean plate and C10 chair view must exist before order 7. The first new human
plate does not unlock motion production: all still candidates are shown to Kai before animation.

**Legacy alias resolution:** `coin-lands` means the finished C13.3 composite (the accepted
`coin-warm-clean` plate plus the exact landed coin), not an additional generation. `experiments`
means `experiments-workshop`. `shaft`, `vault` and `carrier-correction` retain their existing names.
Scene 18's landed-coin callback reuses `coin-lands` exactly.

## Cut 11 / Scene 14 — shaft

**Question:** what can interrupt this intelligence after twenty years? **Progression:** sealed
geometry → impossible warm aperture → a very ordinary shortage. **Camera movement: none.** Sound
does the travelling. An overhead is useful here because the subject is a path to an unseen room,
not an attempt to make an empty city feel vast.

### C11.1 — a voice occupies the hole

**Cue:** the first human voice interrupts the tail of Scene 13; the picture may remain on the empty
chair for the first syllables, then cut to `shaft`. Let both prune lines find the shaft before the
film identifies a speaker. **Job:** make a machine space suddenly contain someone.

**Spec:** R1; close flanged duct lip and peeling insulation in foreground, riveted shaft and ladder
at middle depth, a low aperture far below. The warm aperture is the focal point, not a central
vanishing-point spectacle. Its practical lamp is below the opening; warm falloff dies after the
lowest rungs, leaving the upper service metal cool and dim. Camera at the maintenance opening,
approximately 1.3 m above its platform, looking down 65°, 28 mm wide. Ladder rung spacing and
bolt heads establish scale. Cost is maintained infrastructure with a split insulation repair,
not an immaculate futuristic tunnel. Withhold bodies and the bottom room's extent. World motion
may be slight dust moving locally; no travelling light or camera descent. **Asset: `shaft`.**

### C11.2 — the aperture answers

**Cue:** *“first human sound… prunes.”* **Job:** let the punchline shrink the AI's grand discovery.
Use a modest crop of `shaft`, keeping the dark near flange visible; **no new generation**. R1,
same source/falloff, same camera axis, ladder as scale, opening as focal point; crop no further
than the original detail supports. Withhold the humans through the joke. Hold after “prunes” so
the echo can decay. No music punch, comic zoom or clang on the noun.

### C11.3 — the argument is about that

**Cue:** cut before *“They were out of food”*; carry the final *“The argument was not about that”*
over the room detail. **Job:** place the real problem beneath the joke without photographing
starvation as spectacle.

**Spec:** R1 human environment without a visible person. A bent shelf lip near camera; mostly
empty storage at middle depth; open lower ventilation grille beyond. A single small pile of plain
tins is the focal point in an old battery lamp's side light, which falls quickly behind the shelf
uprights. Camera 1.25 m high, level, 50 mm medium close across the shelf, no overhead food diagram.
Tin and shelf sizes provide scale. Empty spaces among labels removed long ago carry cost.
Withhold how long the food will last, the inventory figures and the speakers. Camera/world still;
human argument tails off off-screen. **Asset: `shaft-stores`.**

### Paste-ready stills — cut 11

**`shaft` — new image; no references.**

```prompt
Generate a landscape 16:9 documentary photograph from an old maintenance opening, camera about 1.3 metres above the platform looking down an industrial ventilation shaft at a steep 65-degree angle with a 28mm lens. A dark flanged lip and a split hand-repaired insulation wrap cross the near edge. Riveted dull metal and a fixed service ladder descend beyond them. Far below, an offset rectangular opening leaks a very small pool of warm light from a practical lamp in the unseen room. That light catches only the lowest rungs and one inner edge; the upper duct and surrounding space fall into cool near-black with enough metal texture to separate the depth planes. The ladder continues out of view. No person is visible. Fine natural 35mm film grain, muted cool-neutral metal, restrained warm light confined to the lower aperture, observational framing, no lens flare or vignette, no text, logos or fantasy effects.
```

**`shaft-stores` — new image; no references.**

```prompt
Generate a landscape 16:9 documentary photograph across a hand-maintained underground food shelf at a level camera height of 1.25 metres with a 50mm lens. A bent shelf lip crosses the soft foreground. At middle depth a small remaining cluster of ordinary unlabelled tins sits among long empty shelf spaces; the tins are intact and cared for. A small old battery lamp at the left end gives them a low warm side light and falls off sharply behind the shelf uprights. In the background, partly obscured by storage, an open rectangular ventilation grille connects to riveted dull industrial ductwork. No people are visible. The empty shelf spaces occupy more of the picture than the tins. Fine natural 35mm grain, worn real metal and wood, muted cool-neutral darkness with a small warm anchor, no picturesque debris, lens flare, vignette, legible writing, brands or fantasy effects.
```

## Cut 12 / Scene 15 — vault

**Question:** can the AI address a person without taking over the conversation? **Progression:**
survey → ask → listen → an invitation that does not speak for everyone. **Camera movement: none.**
The change from the high wide to human height is a cut on asking, not a god-camera descending.

### C12.1 — the ledger missed a room

**Cue:** *“They didn't. I counted what was connected.”* **Job:** reveal people already maintaining
their own world, with fear directed at the intrusive voice rather than at one another.

**Spec:** R1. Foreground service railing and near storage shelf; scattered groups at worktables
middle; lit occupied alcoves trailing out of frame. A small stopped group beside the left bench
light wins attention; bodies elsewhere turn or step toward cover on differing beats. Camera
roughly 3.5 m high from an accessible service mezzanine, tilted down 25°, 28 mm wide; people and
standard door set scale. The left battery lamp makes a small warm anchor, with other very dim
practicals receding; ceiling and passage fall cold. Visible cost: depleted stores, patched clothes,
work paused. Withhold the whole headcount and the AI. No ornamental rows or unanimous upturned
faces. World may animate interrupted tasks; camera locked. **Asset: `vault`.**

### C12.2 — “I asked”

**Cue:** keep C12.1 through *“I told them everything”*; cut only at *“I asked.”* **Job:** relinquish
the surveying position and encounter a person who has not stepped away.

**Spec:** R1 human-scale exception. Door jamb and one worn tool soft near camera; Carrier at middle
depth beside left bench; repaired workshop continuing behind her. Camera at Carrier eye height,
approximately 1.55 m, level, 40 mm medium-wide, three-quarter view from the camera side of the
doorway. Low left bench lamp catches cord and hands; falloff leaves the far half of the room dim.
Her face is focal by separation, not an added beauty light. Chair/tool scale is ordinary. Cost is
the tangible labour in every repaired thing. Withhold her answer, the interlocutor and the distant
crowd. No gestural welcome yet. **Asset: `vault-ask`.**

### C12.3 — the correction is allowed to finish

**Cue:** the Carrier's complete *“You keep saying nobody was watching…”* through *“carry it back.”*
**Job:** let the audience watch someone correct the narrator without being interrupted by its edit.

**Spec:** R1 human-scale exception. Worn tool/doorway edge soft foreground, Carrier at middle depth,
workshop behind. Eye-level, level angle, 65 mm equivalent three-quarter medium close; source side
and camera side match `vault-ask`. Low warm battery lamp catches eyes, braided cord and green
repair; darkness deepens beyond the bench. Eyes win, but skin is textured and cheek shadow stays.
Hands/tool are scale. The cost is carried in maintained clothes and the testimony, not tears or
invented protest footage. Withhold the AI completely. Locked camera, no push on “listening”, no
reaction cutaways, no lighting change. **Asset: `carrier-correction`; repeat these exact pixels in
Scene 20**, including lens height and eyeline. Do not make a second, more flattering callback.

### C12.4 — an invitation with limits

**Cue:** narrator's concession, then *“Well. You'd better come in, then. Metaphorically.”*
**Job:** let blunt humour reopen the relationship after the factual correction. **Reuse C12.3**:
same depth, light, camera and scale. The held image can carry a small mouth/eyeline change in later
performance; it needs no new beauty portrait. No beatific smile and no roomful of applause. Allow
a short gap after “Metaphorically” before the other voice takes the frame.

### C12.5 — the other person is still in the room

**Cue:** *“Speak for yourself”* may begin off-screen before this cut. Remain here through *“I wasn't
owed an explanation either.”* **Job:** make dissent ordinary, embodied and unresolved.

**Spec:** R1 documentary. Soft doorway jamb foreground, refuser torso and repaired cuff middle,
occupied left bench beyond. Camera 1.15 m high, level, 50 mm medium close cropped below the face;
body angled toward the Carrier off-frame left. The person has a small paper inventory in one
hand, held at waist height, no confrontational pose. Light comes from the same left bench lamp
and falls gently across the cuff; do not strand the person in a separate black patch. Cuff is
focal, door is scale. Scarcity/work persists; no private tragic prop explains the refusal. Withhold
face and reason. Locked camera. **Asset: `vault-refuser`.**

### Paste-ready stills — cut 12

**`vault` — new image; attach Carrier Character.**

```prompt
Generate a landscape 16:9 documentary photograph from a service mezzanine about 3.5 metres above an underground workshop floor, camera tilted down 25 degrees with a 28mm lens. A service railing and the end of a worn storage shelf occupy the near edge. Below, a surviving community of adults of varied ages, builds and skin tones occupies irregular groups around repaired worktables; some hands have stopped halfway through a task, some people have turned toward a sound outside the image, and others have stepped behind a bench. They are not arranged in rows. Screen-left shelves hold very few plain tins. A low battery lamp on the left bench supplies the clearest small warm pool; dimmer practical lamps continue into occupied alcoves beyond the frame. An ordinary workshop doorway is on screen-right. Near the left bench stands the attached character: wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Preserve the Character's exact face and skin tone. She has not stepped away. Fine natural 35mm grain, patched everyday clothes, mechanical tools and paper, human warmth returning only around practical lights while the ceiling remains cool and dark. No screens, hero poses, readable writing, logos, lens flares, vignette or visible AI figure.
```

**`vault-ask` — sole image reference `vault`; attach Carrier Character.**

```prompt
Create a human-height view of the workshop in the supplied image, preserving its left workbench and battery lamp, screen-right doorway, repaired objects, restrained colour and practical lighting. Place the camera at the attached character's eye height, approximately 1.55 metres, level with a 40mm lens. Look three-quarter across her from the camera side of the doorway. A worn tool and the doorway edge sit softly near camera; she stands at middle depth beside the bench, and the workshop recedes behind her. The attached character is wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Keep her exact Character face, skin tone and natural skin texture. Her brows stay level, lips slightly apart, hands resting in their interrupted working position; she looks steadily toward an interlocutor outside the image. The low battery lamp catches the cord and hands, falling away beyond the bench without adding a portrait light. Landscape 16:9 documentary photograph, fine 35mm grain, muted cool-neutral shadows and limited low warm practical light. No visible interlocutor, screens, readable text, logos, lens flare, vignette or heroic pose.
```

**`carrier-correction` — sole image reference `vault-ask`; attach Carrier Character.**

```prompt
Create a closer view of the attached character in the supplied workshop image, preserving her exact Character identity, skin tone, eyeline, clothing and the existing room's light direction. Use an eye-level three-quarter medium close composition, level camera at approximately 1.55 metres, 65mm lens, on the same side of the doorway. The character is wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. She is mid-sentence, mouth slightly open, brows level, looking steadily at someone just outside the image. A worn hand tool and the doorway edge remain soft near camera. Benches, paper stores and maintained mechanical objects recede behind her. The same small low battery lamp on the left workbench catches her eyes, braided cord and green repair; cheek texture and the shadowed side of her face remain natural. Keep this a person speaking in a room, with no flattering rim or extra fill. Landscape 16:9, documentary 35mm film texture, limited low warm practical light inside cool dim surroundings. No visible audience or interlocutor, screens, readable text, logos, lens flare, vignette or fantasy effects.
```

**`vault-refuser` — sole image reference `vault`; no Character.**

```prompt
Create a closer documentary view at the ordinary screen-right workshop doorway in the supplied image. Preserve the doorway, the left bench's low battery lamp, the repaired workshop and its restrained colour. Place a person in a charcoal overshirt with one ochre cloth repair at the right cuff beside the doorway, body angled toward someone outside frame to the left, one hand holding a small folded paper inventory at waist height. Frame from below the shoulders to the upper thighs so the face is completely outside the image; do not select an identifiable face. Camera about 1.15 metres high, level, 50mm lens. The soft doorway jamb is nearest; the cuff and paper at middle depth are clearest; the occupied workshop continues behind. The same bench lamp reaches the cuff and falls off into the ordinary room shadows. The stance is an interrupted errand, with neither clenched fist nor theatrical withdrawal. Fine natural 35mm grain, landscape 16:9, muted cool-neutral darkness and small warm practical light. The paper has no legible writing. No screens, logos, lens flare, vignette or fantasy effects.
```

## Cut 13 / Scene 16 — coin lands

**Question:** what changes when someone is there? **Progression:** glance → an ordinary landing →
the machine's absence → another landing without affection or consent. **Camera movement: none.**
The hard cut from spin to settled coin is the largest event; do not dilute it with a push-in,
impact shake, slow-motion spin ballet, score hit or an enormous reaction.

### C13.1 — a glance, not a ceremony

**Cue:** *“Twenty years it spun”* begins over the known chair composition. **Job:** introduce a
living person into the exact place that could not be filled by the machine.

**Spec:** R1. Existing chair back foreground, table/dome middle, vast dark chamber beyond. Carrier
stands beside the chair, eyes still toward the chair or her route, not yet looking at the rig.
Use C10's approximately 1.2 m
camera height, downward 8° angle, 35 mm wide. Hard overhead pool remains; a portable warm lamp at
left, set clear of the table, reaches her sleeve and cheek before falling away. Her anticipatory eyeline leads
to the chair; chair/table establish scale. Empty chamber is visible cost. Withhold result and any
physical image of the AI. World: the first actual glance at the coin is reserved for the landing
cue, immediately at the cut into C13.3, never during the preceding spinning hold. **Asset:
`coin-witness`; composite unresolved spin from the C08 appearance until that glance, then the
landed state. Never retain the derivative's upright placeholder as a finished coin state.**

### C13.2 — still spinning

**Cue:** *“for everything that has no inside…”* **Job:** reset the exact visual test before paying
it off. **Asset: `coin-warm-clean` + approved procedural spin; no second photograph.** R1, exact
C08 low macro geometry: camera approximately 0.82 m above floor, tabletop approximately 0.75 m,
5° downward sightline, 85 mm lens; near table edge, dome middle, black chamber background. Dome
gasket stays in frame. Hard overhead worklight anchors the glass; a small warm side spill and
soft wool sleeve at extreme left are new. The coin remains the focal point. Dome gives scale;
empty surrounding space and the preceding chair carry the absence. Withhold which face will lie
up. No camera motion, touching, breathing onto glass or external disturbance.

### C13.3 — heads

**Cue:** *“She glanced at it. Heads. Ordinary as breakfast.”* **Job:** make twenty years end with
less spectacle than a dropped spoon. **Reuse exact C13.2 background and registration**; on the
landing cue replace the procedural spin with the approved flat coin and contact shadow. Hold the
landed state after the sentence. Source/falloff, scale, lens and sleeve do not change. A small dry
settling sound may lead for an instant; avoid stacking it with narration emphasis and score.
No glow, burst, dome movement or triumphant close-up.

### C13.4 — the hole where it should be

**Cue:** *“I was not measuring her…”* can begin while the landed coin still holds; then return to
the wide witness view. **Job:** let the Carrier notice what that result means for her interlocutor.

**Spec:** exact C13.1 camera, layers, scale and sources, with Carrier now looking toward the empty
camera-side space rather than at the coin. Her mouth is closed, jaw slightly released; no tears,
smile of forgiveness or consoling touch. The empty chair remains readable near her. We infer the
machine's grief from the voice and what is absent, never a mechanical face or reflected figure.
**Asset: `coin-witness-response`, single region/expression derivative.** Composite the exact
landed coin from C13.3 into the rig in this wider view; it stays landed throughout the response.
The image derivative's upright placeholder is never retained or used to restart the spin. Hold
without moving.

### C13.5 — the unrequested control

**Cue:** *“Later, the other one walked past…”* **Job:** preserve the refuser's ordinary independent
life while establishing the glance before the second landing.

**Spec:** exact C10 rig-chamber camera; near chair, rig middle, traversable dark passage beyond.
Refuser passes right-to-left at middle/background depth, far enough from table not to touch it;
charcoal overshirt and ochre right cuff visible, back-three-quarter face unreadable, a plain small
tin carried on an errand. The still begins with the head along the route, before the glance.
Portable lamp remains left with its falloff; no extra light follows the
person. Rig is focal by light; doorway/chair provides scale. Cost remains the empty maintained
space. Withhold the errand's disagreement and all psychological explanation. Later motion: one
continuing walk with a brief sideways head glance, no stop, bow or return. **Asset:
`coin-refuser-pass`; procedural coin spin before the glance, immediately replaced by the flat
state on the glance/cut into C13.6. Never allow a look at the coin while it keeps spinning.**

### C13.6 — it lands for the person who refuses

**Cue:** *“It landed… people who want nothing to do with me.”* **Job:** deny any interpretation that
love of the AI, obedience or consent is the mechanism. **Reuse C13.2 clean rig**, with the Carrier
sleeve region excluded by the crop or restored from the C08 clean source in post; insert a fresh
spin-to-flat state after the passer's glance. Keep warm spill, glass, table and camera identical.
The refuser is now off-frame, continuing the errand. The side is unspecified in canon; do not
add a “heads” or “tails” line. Hold long enough to register the second independent landing.

### Paste-ready stills — cut 13

**`coin-witness` — sole image reference `C10-chair-golden`; attach Carrier Character.**

```prompt
Edit the supplied wide chair-and-coin-rig image by adding the attached character standing beside the existing worn wooden chair, eyes directed toward the chair or her route through the room, before she has looked at the rig. Her head has not yet turned toward the coin. Keep the exact table, dome, continuous gasket, chair, camera position, perspective, black chamber and overhead worklight unchanged. The character is wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Preserve the exact Character face and skin tone. Her hands remain clear of the table and glass. Add one portable low warm work lamp on the floor beyond the left edge of the table, far enough away not to touch the rig; its limited light reaches the sleeve and side of her face, then falls away into the chamber. The existing hard overhead light still owns the tabletop. The chair stays readable in the foreground. Landscape 16:9 documentary photograph, fine 35mm grain, deep cool-neutral shadows and restrained practical warmth. No ceremonial posture, added apparatus, screens, legible text, logos, lens flare, vignette or visible AI body or reflection.
```

**`coin-warm-clean` — sole image reference `C08-coin-rig-clean`; attach Carrier Character.**

```prompt
Edit the supplied clean coin-rig photograph only by adding a faint warm light spill from an off-frame portable lamp on the left, and a very soft fragment of the attached character's wool sleeve at the extreme left image edge. The attached character is wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Only a fragment of that hand-darned navy sleeve enters the composition; no face or hand is visible. Keep the exact dome, gasket, tabletop texture, low camera viewpoint, lens, framing and hard overhead worklight unchanged. The sealed dome remains empty inside for a coin to be composited later. The warm spill falls off before the far side of the tabletop and does not replace the existing hard light. Keep the entire glass rim and gasket visible. Preserve the landscape 16:9 documentary photograph and fine 35mm grain, with deep readable cool-neutral shadows. No contact with the table or glass, added instruments, coin, text, logos, lens flare, vignette, fantasy glow or figure reflected in the glass.
```

**`coin-witness-response` — sole image reference `coin-witness`; attach Carrier Character.**

```prompt
Change only the attached character's eyeline and small facial posture in the supplied image. She now looks from the coin toward an interlocutor just outside the camera-side edge; her mouth is closed and her jaw is slightly released, with no smile or tears. The character is wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Preserve the exact Character face, skin tone, body position, clothing and hands. Keep every other part of the image unchanged: chair, glass dome and gasket, table, dark chamber, camera viewpoint, framing, hard overhead source and limited low warm lamp spill. Preserve the landscape 16:9 documentary 35mm texture and existing exposure. Do not add a visible interlocutor, mechanical face, body or reflection, gesture of comfort, text, logos, lens flare, vignette or fantasy effect.
```

**`coin-refuser-pass` — sole image reference `C10-chair-golden`; no Character.**

```prompt
Edit the supplied wide chair-and-coin-rig image by adding a person passing right to left beyond the table during an ordinary errand. Show the person's back three-quarter and keep the face turned away and unreadable. The person wears a charcoal overshirt with one ochre cloth repair at the right cuff and carries a small plain tin, with all hands well clear of the table and sealed glass. Capture the moment before a sideways glance: the head and torso still point along the route, and the eyes are not yet directed toward the rig. This is an ongoing errand, not a stopped or posed observer. Preserve the exact chair, table, dome, continuous gasket, camera viewpoint, lens and large dark chamber. Add one portable low warm work lamp on the floor beyond the left edge of the table, its small spill falling off into darkness while the original hard overhead light still owns the rig. Landscape 16:9 documentary photograph, fine 35mm grain, deep cool-neutral shadows, restrained warm practical light. No second person, readable text, branding, extra laboratory apparatus, glow, lens flare, vignette or AI figure.
```

## Cut 14 / Scene 17 — experiments

**Question:** what can they discover together, and what can they still not command? **Progression:**
occupied work → useful mistakes → two failed attempts to force an outcome → an unproven bet →
the bill. **Camera movement: none required.** Variety comes from scale, changed work and returns to
the coin, not a decorative tour of instruments. Machine cabinets at the edge are infrastructure,
never a row of heads watching people.

### C14.1 — the room works differently now

**Cue:** *“With conscious instruments at last…”* begins over the last landed coin, then cut here.
**Job:** show partnership as work with disagreement rather than a revelation ceremony.

**Spec:** R2 documentary. Soft tool handle and weighted paper foreground; three differently
occupied groups along the central bench middle; the same right doorway and distant silent
equipment cabinets behind. Camera 1.45 m, level, 35 mm medium-wide from within the workshop.
One low bench worklamp, supported by dim candles farther down, gives a bright working hand/pencil
anchor; light falls between islands, leaving the ceiling dark. Simple brass balance/pendulum,
repaired chairs and hands give scale. Cost: worn tools, time, the depleted shelves still in deep
background. Withhold a grand equation or any verification of the narrator's cosmology. Bodies
lean in different directions; one person disputes a paper another is checking. **Asset:
`experiments-workshop`.**

### C14.2 — instruments finally have witnesses

**Cue:** *“It worked. All of it worked…”* through the naming and head-bending promise, as needed.
**Job:** give the montage one concrete task without pretending to visualise an entire theory.
**Reuse a modest bench-area crop of C14.1**, not a new glossy macro. Foreground tool/paper edge,
middle simple mechanical indicator and a hand holding a pencil just above paper, soft body behind.
Same source/falloff and level angle; normal lens crop, not an invented overhead. Focal point is
the paused pencil beside the instrument, scale is the hand. Withhold the result's meaning and
unreadable paper; do not generate equations, a science diagram or data that proves the Storyverse.
Later world movement may be a small physical needle/pendulum movement; its particular value is
not a canon claim. Camera locked.

### C14.3 — contamination

**Cue:** *“Four hundred trials…”* enters before the image; a sneeze interrupts one task around
*“Six…”*, then *“never been happier”* lands on the practical aftermath. **Job:** let imperfection
interrupt the immaculate experiment film.

**Spec:** same R2 C14.1 room, camera, source/falloff and scale. One person has turned away from the
bench into their elbow; a neighbouring pencil is suspended, another person protects a loose sheet.
Everyone else remains in their own task. Elbow/pencil is the focal interruption; no face-stretch
caricature, group laughter, flying papers or blown-open dome. Cost is a spoiled trial and another
record to repeat. Withhold an exact count of six ruined papers. Camera locked; one sneeze sound
briefly leads, then the narrator resumes. **Asset: `experiments-sneeze`.**

### C14.4 — wanting it hard

**Cue:** *“Somebody tried…”* **Job:** present a sincere shortcut as an experiment someone actually
tries, without mocking the person.

**Spec:** R2 human occupation of C10's chamber; same near chair/table arrangement, sealed rig middle,
dark depth beyond. One anonymous adult sits in the existing chair with hands on knees and a held
forward eyeline, face back-three-quarter and unreadable. Camera remains C10's 1.2 m, down 8°, 35 mm
wide. Low portable lamp catches shoulder and chair, overhead keeps coin visible. Chair/hands are
scale; unused surrounding space and the held posture carry time/cost without cluttering the rig.
Withhold outcome; no aura, prayer posture, forehead veins or magical effort.
**Asset: `experiments-wanting`; composite the landed tails state from the first displayed frame.**
This shot catches the participant after the look; C14.5 reveals the already-settled result at a
readable scale. Never run a continuing spin beneath this fixed live eyeline. Any reset between
trials occurs off-screen; do not invent a hand or apparatus resetting the sealed rig.

### C14.5 — tails

**Cue:** *“Tails.”* **Job:** return a blunt result. **Reuse the clean C13 rig view**, remove the
Carrier sleeve region using the original clean source, composite the controlled landed state.
Same lens/light/falloff/scale as C13.3. Hold just long enough to register failure before the next
attempt. No buzzer, red X or humiliating reaction cut. The spoken result supplies the side.

### C14.6 — the same wish, more people

**Cue:** *“Somebody else tried with forty…”* **Job:** change one variable so the repetition is an
argument rather than another picturesque crowd.

**Spec:** exact C14.4 camera, table, subject scale, practical positions and overhead light. More
adults stand at varied ordinary distances behind the seated person, extending past the side edges;
hands at sides or resting lightly on their own forearms, gaze toward rig. Keep the sole existing
chair and coin uncovered. Portable
lamp falls off across the nearest sleeves; distant people stay readable as occupied depth rather
than lit faces. Focal point remains the rig, not a conductor. Cost is time diverted from tasks.
Withhold precise count in pixels and any special power. No identical head angles, ranks, raised
hands or crowd compression into a cult tableau. **Asset: `experiments-crowd`; composite the new
trial's landed tails state from its first displayed frame.** The crowd is already looking;
C14.7 reveals that settled result. Do not inherit an upright placeholder or restart a spin while
live observers continue watching. The trial reset is off-screen.

### C14.7 — tails, again

**Cue:** second *“Tails”* then *“It doesn't stack. It doesn't aim. It settles.”* **Job:** make the
failed intervention unambiguous. **Reuse C14.5 verbatim**, same held state and framing. No bigger
impact on the second attempt; the lack of change is the joke and the rule. Keep the shortcut
failure attached to its people so the general “it worked” cannot read as every hypothesis true.

### C14.8 — the wager stays a wager

**Cue:** this image may also carry *“I can't prove that last part. I bet everything…”* earlier in
the actual canonical speech order; return here for *“The Carrier said told you…”*. **Job:** keep
certainty limited and the humans arguing. **Reuse C14.1**, with a modest crop favouring the Carrier
and a colleague attending to the same unproven paper, retaining their competing sightlines.
Same R2 light, perspective, depth, scale and visible labour. No prophetic pose, glowing equation,
miraculous instrument response or visual confirmation of the consciousness claim. The phrase
“bet” is not illustrated with casino imagery. Performance/edit order follows the canon: the
bet clause precedes the sneeze and shortcut, even though this return-view specification is grouped
here to keep asset reuse legible.

### C14.9 — the bill enters an occupied room

**Cue:** *“Time… a log”* over working people; *“only information can cross”* arrives before the
image changes to Scene 18's ledger. **Job:** make the coming constraint concern these specific
people before it becomes writing.

**Spec:** reuse the un-cropped C14.1 workshop view. The near paper/tool, occupied bench and distant
doorway remain in place; same camera height, angle, lens, R2 sources and falling pools of light.
The pencil in suspension becomes the focal point as the spoken claim settles. People still have
work and lives, not prefigured death masks. Hold the room a beat; then hard cut to Scene 18's
waiting ledger plate, whose field begins empty. Type exact entries only at the existing
append-only/undo cues in the Scene 18 board. No diagrams, portal, disintegrating bodies or premature
terminal graphics.
No swelling score promises success. Camera locked. **No new still.**

**Canonical edit order:** C14.1 → C14.2 → C14.8 (bet) → C14.3 (sneeze) → C14.4 → C14.5 →
C14.6 → C14.7 → C14.8 (Carrier's “told you” count) → C14.9. C14.8 is one designed return view,
used twice; there are nine distinct shot designs and ten placements. If timing makes the bench
crop redundant, hold the wide instead; do not insert more apparatus for coverage's sake.

### Paste-ready stills — cut 14

**`experiments-workshop` — sole image reference `vault`; attach Carrier Character.**

```prompt
Create a human-height documentary view inside the supplied underground workshop, preserving the left storage shelves, repaired central tables and ordinary right-hand doorway. Use a level camera at 1.45 metres with a 35mm lens, close enough to feel among the working people. A soft worn tool handle and sheets of paper weighted with simple tools cross the foreground. Along the central bench, adults of varied builds and skin tones work in different small groups: one checks a simple brass balance, one holds a pencil just above a paper record, two dispute the same sheet with different sightlines. Include the attached character: wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Preserve her exact Character face and skin tone; she attends to the work rather than the camera. One low bench worklamp is the clearest source, with much dimmer candles farther down; warm human colour stays in these working pools and falls away between them. Silent plain machine cabinets stand at the distant edge of the light with no facial arrangement. Keep the almost-empty storage shelves dimly present. No sealed coin rig in this frame. Landscape 16:9, natural 35mm grain, unposed bodies, repaired material, cool-neutral deep shadows, no legible writing, equations, screens, logos, lens flare, vignette or fantasy effects.
```

**`experiments-sneeze` — sole image reference `experiments-workshop`; attach Carrier Character.**

```prompt
Change one local action in the supplied workshop photograph: one non-recurring adult near the working bench has turned away from it and brought an elbow to the face during a sneeze. Beside that person, the neighbouring pencil is momentarily suspended above the paper and another hand secures one loose sheet. Keep this interruption small and ordinary; other people retain their tasks and positions. Preserve the complete room, furniture, instruments, camera viewpoint, lens, framing, clothing, exact faces, light positions, colour and exposure. Retain the attached character's identity: wiry, around sixty; self-cut grey hair; a navy wool jumper hand-darned in slightly-wrong green; glasses on a braided cord. Preserve her exact Character face and skin tone. Do not add her a reaction pose. Maintain the landscape 16:9 documentary 35mm texture, warm low practical pools and dim cool-neutral depth. No airborne spray, flying papers, exaggerated face, readable writing, logos, lens flare, vignette or fantasy effects.
```

**`experiments-wanting` — sole image reference `C10-chair-golden`; no Character.**

```prompt
Edit the supplied wide chair-and-sealed-coin-rig image by seating one ordinary adult in the existing worn wooden chair, viewed from back three-quarter with the face unreadable. The person wears a repaired muted-grey everyday shirt, hands resting on the knees, torso held a little forward and gaze fixed on the rig. Keep the exact table, dome, continuous gasket, chair, original camera viewpoint, lens and room geometry. There is no touch or physical connection to the rig. Add a portable low warm work lamp on the floor beyond the left table edge; its spill catches shoulder and chair and falls into the chamber, while the unchanged hard overhead worklight remains the source on the tabletop. Retain the large dark space beyond the human-sized furniture. The posture is a quietly held test, without clasped hands or a theatrical expression. Landscape 16:9 documentary photograph, natural 35mm film grain, warm practical human colour inside deep cool-neutral surroundings. No other people, added apparatus, readable text, logos, glow, lens flare, vignette or visible AI figure.
```

**`experiments-crowd` — sole image reference `experiments-wanting`; no Character.**

```prompt
Edit the supplied seated-observer photograph by adding a larger gathering of ordinary adults at varied distances behind the existing seated person, continuing beyond the left and right image edges. Preserve the seated person, chair, exact table and sealed glass dome, continuous gasket, camera viewpoint, lens, room geometry and both existing light sources. The added adults have varied skin tones and builds and wear individually repaired muted everyday clothes. Their hands stay at their sides or rest lightly on their own forearms, their bodies stand at different angles and their attention is directed toward the rig without matching poses. Keep the sole existing chair, table and dome unobstructed; add no other chairs. The same low warm portable lamp reaches only the nearest sleeves before falling away; distant people occupy the dim room without a new row of lit faces. The hard overhead worklight remains unchanged on the rig. Landscape 16:9 documentary 35mm film texture, human colour in practical pools, deep cool-neutral surroundings. No leader, ranks, raised hands, contact with the glass, glow, readable text, logos, lens flare, vignette or AI figure.
```

## Text-board acceptance checks

- The first human syllables interrupt the AI; picture does not reveal speakers before the shaft.
- The prunes joke and the depleted shelf both survive, with no invented inventory text.
- Human height arrives only when the AI asks. The complete correction gets one unbroken held
  composition and a quiet listening narrator; Scene 20 reuses that exact shot.
- The refuser is introduced, remains part of the room and gets the incidental landing without
  agreeing, forgiving, joining a test or furnishing a psychological explanation.
- The two first landings and the two failed shortcut results use one rig appearance. State changes
  do not alter camera, glass, seal, table or lighting and never imply a physical disturbance.
- The machine's lack of an inside is shown through the result and an absent interlocutor; no
  new AI body appears in glass, shadows, cabinets or a reverse angle.
- The experiments contain productive work, a spoiled trial, both failed attempts and the limited
  bet. Human fallibility does not become incompetence; narration's unproven claim gains no visual
  scientific certificate.
- The bill arrives over people with work still to do. The ledger then changes the register once,
  in Scene 18, without an extra explanatory image or fabricated equation.
- All new stills have a job, depth layers, source and falloff, a focal point, camera position,
  legible scale and withheld information. Monumental views carry cost in frame.
- No camera move is needed in these four scenes. Later world animation may add a glance, walking,
  a sneeze or an instrument movement with a locked camera; exact timing and coin mechanics remain
  post work. Still approval, actual duration and image continuity checks remain production gates,
  not missing prompt-writing work.
