# Prettier stills without slop: NB2 + Omni Flash (2026-10-26)

**Why:** Jack, Speakeasy Mint MV, scene 7: *"i kinda wanted more pretty shots, with more lights and reflections of the
ground … windows … more cinematic, interesting camera shots, also the lighting and gamma needs to pop more. i want
that for all images going forward. Please avoid elements of AI slop."* A subagent web pass on the same day confirmed the
repo's existing rules (`nano-banana-2.md` anti-slop toolkit, §10, the advert-vocabulary trap; `omni-flash.md`) and
added the items below. **The [official] lines came through a summarising fetch tool: re-check the exact wording before
quoting it publicly.**

## What the web added

- **Google's formula, image:** subject + action + location + composition + style, written as a narrative, never a
  keyword list; say what you want, not what you don't ("empty street", not "no cars"). Its lighting vocabulary
  includes "chiaroscuro lighting with harsh, high contrast". [official]
  https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- **Video:** "low-key lighting" and "film noir style with deep shadows and stark highlights" are Google's own words;
  avoid "no" and "don't"; state the style first. [official]
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide ·
  https://deepmind.google/models/veo/prompt-guide/
- **Omni Flash:** with no camera instruction it defaults to a static camera with slight breathing; write "Single
  continuous shot" or it may cut; [0-3s] ranges are budgets, not edit points. [practitioner]
  https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide
- **Slop tells and their counters:** poreless skin, golden glow everywhere, dead-centre symmetry, detail on every
  surface, blur with no physical reason, vague "cinematic lighting", too many light ideas. [practitioner]
  https://openart.ai/blog/visual-cliches-that-scream-made-by-ai/ · https://artlist.io/blog/ai-lighting-prompts/
- **Painted wet streets that work:** named practicals (a shopfront, a streetlamp), wet cobbles and puddles,
  dark ultramarine/indigo shadows, one warm accent, a medium word (impasto). [anecdote]

## 🔴 The conflict with the brief, and how we resolve it (inferred, untested until the scene 7 r2 results)

Naming a **reflection** makes NB2 overdo it (once it came back as a double exposure across a face, `nano-banana-2.md` §10), and NB2 already
runs "too sharp, too contrasty". So "pop" and "reflections" are asked for by their **causes**, never by name:

1. **Value structure, not adjectives:** "most of the frame in deep shadow; the brightest values are X and its streaks on the
   wet cobbles."
2. **One key light with a direction and an object**, plus one or two bounded practicals (lit windows, streetlamps).
3. **Warm against cold, named saturated colours** (amber against ultramarine).
4. **Shout the weather:** "cobbles soaked after a downpour, standing puddles, grit, a drain". Never name a reflection on
   glass near a face.
5. **Banned words:** cinematic, photorealistic, 8K, HDR, glowing, stunning, masterpiece, glossy, immaculate.
6. **Camera named:** height and angle, a foreground occluder, the subject off-centre.

## ✅ Settled 2026-10-26 (late): the Flow model is Nano Banana 2.1

Read off the compose bar over CDP in project `dedd295f`: **"🍌 Nano Banana 2.1 · crop_16_9 · x2"**. The flow MCP's
`model: "Nano Banana 2"` selects it: the name guard rejects a trailing word character (so it never picks "2 Lite"), and the "."
in "2.1" isn't one. **So every Speakeasy Mint still since the K sweep was made on 2.1.** This resolves the UNVERIFIED note in
`2026-10-09-crowd-vault-accent-sweep.md` §5. The credit cost per 2.1 image is still unread.

**Web pass, same evening** (Jack: "optimise for Nano Banana 2.1 / Omni Flash, avoid AI slop"): third-party 2.1 guides only
(Google has published no 2.1 prompting doc that I found). They agree with what we already do: a short brief in full sentences
(subject, setting, camera, light), plain precise words over stacked adjectives, and the claim that 2.1 follows long multi-
instruction prompts more completely than 2 did [practitioner]. Nothing new on slop for 2.1 specifically. Omni Flash
image-to-video guides say the same as `omni-flash.md`: the still carries the look, the prompt carries the motion,
the camera and the sound [practitioner]. Sources: morphic.com/resources/how-to/nano-banana-2-1-guide ·
openart.ai/de/blog/nano-banana-2-1-prompt-guide · fal.ai/learn/tools/how-to-use-gemini-omni-flash-1-1 ·
atlascloud.ai/models/google/gemini-omni-flash/image-to-video.

**What a day of 2.1 on the "K3a lit" lead taught (Speakeasy Mint scenes 7–23, ~130 stills; H-grade, ours):**
- The lit lead holds: one named key + bounded practicals + "most of the frame in deep shadow; the brightest values are X".
- **Any shop word prints itself:** "bakery" painted BAKERY twice. Describe the goods ("a shop window full of loaves under a plain
  blank sign"). Same family as "LOAN FORM" on a "loan form".
- **"Every face turned towards X"** stops crowds staring at the camera.
- **A before/after pair cuts cleanly** if the after-prompt is written to the before take's actual layout (object by object, left to right).
- **Exact state words can lose:** "a candle burnt low / a short stub" came out tall three times.
- Named recurring features hold across scenes (the mayor's "heavy gold mayoral chain round his neck"; the cops' walrus moustache /
  ginger sideburns), and a blouse can pull a face towards a real politician: dress recurring women in plain, specific clothes.
- **Fixed the same night:** describe the *remains*, not the state: "the last of a candle: only a flat puddle of wax with a
  tiny drowning flame in the middle, guttering" gave a burnt-out candle 2/2 (scene 28a), after "burnt low / a short stub" lost 0/6.
