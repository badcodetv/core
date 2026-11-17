---
slug: german-expressionism
name: German Expressionism
kind: look
family: Film movements and national cinemas
checked: 2026-10-28, references and engine notes (see Web check)
---

# German Expressionism

> Painted, distorted sets and knife-edge shadows that put a character's mental state on the walls.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Weimar-era German silent cinema (c.1920-1927) in which sets, light and performance were bent to express fear, authority and paranoia rather than reality. Caligari's slanted painted streets, Murnau's long shadows, and Lang's mass-geometric Metropolis share a rule that architecture is psychology. It came out of postwar defeat, hyperinflation and mistrust of authority, which is why tyrants, sleepwalkers and crowds in uniform recur. Its tools (chiaroscuro, forced perspective, stylised acting) fed directly into film noir and horror.

## Signature traits

- Hard top and side light with deep black shadow, shapes cut by shadow rather than lit by fill
- Forced perspective: leaning buildings, trapezoid doors, stairs that do not meet the wall, painted shadows on the floor
- Black and white (sometimes tinted amber, blue or green in the original prints) at about 1.33:1 or 1.37:1
- Stylised, angular poses and wide-eyed performances; silhouetted figures on stairs
- Giant shadows of a figure cast ahead of the body on a wall
- Iris-in and iris-out vignettes and intertitle cards with hand-lettered text
- Crowds as geometric blocks, workers in lines and tiers
- Miniature and matte-painted cities, vertical architecture dwarfing people

## References

- *The Cabinet of Dr. Caligari* — Robert Wiene, 1920. The painted-set manifesto: streets and rooms drawn at impossible angles to put a madman's view on screen.
- *Metropolis* — Fritz Lang, 1927. A tiered city with workers underground and owners above; the clearest visual statement of class as architecture.
- *Nosferatu* — F. W. Murnau, 1922. Shadow as the monster; a landlord-like predator whose silhouette arrives before he does.
- *M* — Fritz Lang, 1931. Sound-era Expressionism with city-wide mob logic and shadow-cut interiors.

## What it carries

Dread, grotesque comedy, paranoia, tyranny and the sublime. It carries villains, bureaucracy as nightmare and the sense of a trap. It fights against warmth, intimacy and naturalism: a kind face in this world is a surprise, which can be used.

## What it suits, and what it would undermine

Satire of power: a landlord, a banker or a government department drawn as architecture and shadow. Excellent for a cynical future-narrator who is looking back on a tyranny, and for dream or nightmare sequences inside an otherwise plainer story. It fits dark humour because it is theatrical and a little ridiculous. It would undermine gentle slice-of-life sympathy, and it risks turning every opponent into a cartoon monster, which cuts against the idea of naming decision-makers rather than demons.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana handles 'German Expressionist silent film still' well because the look is heavily documented: ask for 'painted set with distorted perspective, leaning walls, trapezoid doorways, painted shadows on the floor, hard single light source, deep black shadows, black and white, 1920s film grain, 4:3'. Name the architecture feature you want (stair, archway, factory gate) and the shadow shape. Veo does better with slow, stagey motion: a figure creeping along a wall, shadow lengthening, an iris closing. For exclude: 'colour, modern CGI, realistic perspective, soft fill light, smiling, photorealistic skin pores, lens flare'. Use 'tinted blue-green monochrome' if you want the old tinted-print feel. Describe intertitles as separate text elements rather than asking the image model to render long text.

## How generators get it wrong

Models drift into generic gothic or modern 'film noir' with realistic perspective and pretty chiaroscuro, losing the warped geometry; fix by asking for specific distortions (walls leaning at 15 degrees, doors that taper) and painted shadows. Veo tends to straighten and stabilise sets and to animate with naturalistic physics, so a distorted set can wobble or 'correct' itself between frames; keep the camera locked and let the figure move. Performances come out naturalistic or glossy; ask for stylised, theatrical gesture. Text on intertitles gets garbled when long. Strong black crush can swallow facial detail and break character consistency, so lock a face with a reference image and a strong silhouette feature (hat, hair, coat).

## Production cost

Setting consistency is the main cost: a distorted set has to be re-created identically across shots, and models normalise it. Mitigate by using one or two hero environments, reusing the same image as a reference, and writing the distortion into the prompt every time. Silhouette-driven shots are forgiving of faces, which helps. Heavily stylised motion is limited and works well in 8-second clips.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Nano Banana supports 4:3. Flow has no dedicated exclude box for Veo; put exclusions in the main prompt as positive descriptions. Veo is 16:9 or 9:16 only.

## Web check (2026-10-28)

Engine notes: contradicted by what the checker found.

**Correction:** Flow's UI has no separate negative-prompt box for Veo or Nano Banana (the Veo API has a negativePrompt parameter, Flow does not expose it). Google and community guides advise positive framing (describe what you want), with 'no X' phrasing used sparingly for recurring defects. So put 'smooth photoreal 3D, modern CGI, colour grading, lens flare' into the main prompt as exclusions in prose, or describe the opposite positively (flat painted sets, hand-made, monochrome). The rest (explicit geometry words, small motion, locked camera) is plausible but undocumented.
