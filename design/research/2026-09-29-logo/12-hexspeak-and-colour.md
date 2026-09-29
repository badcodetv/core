# 12 — The name is a number and a colour

*Research brief, 2026-09-29. One Sonnet agent, 6 web searches (cap 8). Raw research, not house policy — the ruled layer is [`direction.md`](./direction.md) once Kai rules on it.*

**Evidence grades:** *verified* = the agent fetched a page that says it · *secondary* = a search snippet or secondary source said it · *(unverified)* = recalled from the model's own memory, not checked. The agent could not see images: every description of a logo comes from text.

## Headline

BADC0DE is real hexspeak (a Linux kernel constant contains it), and its first six digits make #BADC0D, a genuine acid yellow-green sitting between hi-vis and Android's old green. It is a free, provable, non-cliche colour for the mark. Nothing I verified says the colour alone reads as BadCode to a non-coder, so it needs one strong shape and strict use on near-black.

## Findings

- **[verified]** 0xBADC0DEDDEADBABE appears as BUFPAGE_MAGIC in a Linux kernel magic-numbers list in the Linux-Kernel Archive (lkml.iu.edu, hypermail 9901, i.e. January 1999). So BADC0DED is a real in-kernel hexspeak constant, glued to DEADBABE, used as a 'bad buffer page' sentinel. — <https://lkml.iu.edu/hypermail/linux/kernel/9901.0/0606.html>
- **[verified]** 0xbadc0de is used as a throwaway placeholder in pwntools ROP-chain example code (rop += p64(0xbadc0de), commented 'arbitrary string with no null bytes'). It is an exploit-writer's filler value, not a formal OS or debugger constant. A C++ forum thread also lists it as a magic number someone thought of, and a GitHub user is named 0xbadc0de. — <https://github.com/RylanOC/BLACK-MAGIC/blob/master/pwn/libc_csu_init.md>
- **[verified]** 0xBADC0DE is NOT in Wikipedia's Hexspeak table or its Magic number page, and I found no OS, debugger or crash-code owner for it. The verified debug/crash family is different: 0x8BADF00D (Apple iOS crash report: app took too long to launch or respond), 0xBAADF00D (Microsoft debug heap, uninitialised memory), 0xBADDCAFE (libumem, uninitialised memory), 0xDEADC0DE (OpenWrt firmware marker), 0xC00010FF (iOS thermal kill). Safe claim: 'hexspeak that reads bad code, and it turns up in the Linux kernel'. Do not call it an official error code. — <https://en.wikipedia.org/wiki/Hexspeak>
- **[verified]** 0xC0DEBAD: I found no real-world use in any page I fetched or searched (Wikipedia, kernel list, forum). Treat it as invented by analogy. — <https://en.wikipedia.org/wiki/Magic_number_(programming)>
- **[*(unverified)*]** Computed arithmetic: BADC0DE is 7 hex digits (195,936,478 decimal) so it is not a valid CSS colour, but BADC0DED (8 digits) IS a valid 8-digit RGBA CSS colour: #BADC0D at alpha 0xED = about 93% opacity. So 'BADC0DED' can be typed into CSS as the bad-code green, slightly see-through.
- **[secondary]** #BADC0D = RGB(186, 220, 13); HSL about 70 deg, 89%, 46%; HSV about 70 deg, 94%, 86%; relative luminance 0.617; WCAG contrast about 13.3:1 on pure black and 12.6:1 on #0a0a0a (all computed by me). Nearest CSS named colours by RGB distance: greenyellow #ADFF2F, then yellowgreen #9ACD32. Pantone: I could NOT verify a nearest match (Pantone's site withholds values; colorhexa and encycolorpedia returned 403). Search snippets put the neon yellow-green family at PMS 389 (about #CEE007, secondary source), 809 C and 803 C; a match to #BADC0D is my guess only. — <https://www.pantone.com/color-finder/809-C>
- **[secondary]** Comparators: web chartreuse is #80FF00 (named for the 1737 liqueur). Tennis 'optic yellow': one secondary source lists #ccff00, another quotes dfff4f, hue about 77 deg; approved by the ITF in 1972 after five years of visibility tests on colour and black-and-white TV; Wimbledon stayed white until 1986. My computed Lab distance from #BADC0D: about 17 to #ccff00, about 17 to #dfff00, about 21 to greenyellow, about 23 to pure yellow, about 36 to web chartreuse (a just-noticeable difference is about 2). So #BADC0D is the tennis-ball family, one notch dimmer, greener and more mustard, not a different species. — <https://edition.cnn.com/style/article/artsy-tennis-ball-design-artsy/index.html>
- **[verified]** Hi-vis standards: EN ISO 20471 (2013) says colours other than yellow or orange may not give adequate conspicuity; ANSI/ISEA 107 (US, first 1999, revised to 2020) requires fluorescent yellow-green ('chartreuse yellow' on traffic vests). British Rail trialled fluorescent orange 'fire-flies' in 1964 (Glasgow) and 1965 (London Midland); UK rail standard RIS-3279-TOM is orange. I did not verify the ISO 20471 chromaticity box, so I cannot say whether #BADC0D falls inside it; it is probably too dark in luminance to count, so it is the same neighbourhood, not a compliance colour. — <https://en.wikipedia.org/wiki/High-visibility_clothing>
- **[verified]** Yellow-green on dark, screen and print: since about 1973 some US fire engines went fluorescent chartreuse because Stephen Solomon found it more visible at night than red (Purkinje effect, eye sensitivity shifts to yellow-green in low light). On screen this hue is nearly the brightest saturated colour, so it pops hardest on near-black (12-13:1), but a screen cannot exceed white so it reads as a glowing green rather than day-glo. In print, neon hues are outside CMYK gamut: you need a fluorescent spot ink (PMS 803 etc.), over a white underbase on dark stock; fluorescent inks soften after months of direct sun and glow under blacklight. Practical: the mark needs an sRGB value, a CMYK fallback that will look dull, and a spot-ink version for stickers and sleeves. — <https://publicide.com/techniques/fluorescent-ink/>
- **[secondary]** UK class meaning: a Conversation article on hi-vis (Australian and British examples) says it signals 'safety, authority, working class masculinity, being employed', spreads off-job to security guards and cleaners, gets staged by politicians for photo-ops, and builds group solidarity in protest. The French gilets jaunes used the vest because French law has required one in every car since 2008 (cheap, everywhere) and it read as working and lower-middle class outside city centres. I found no verified source on UK rave-and-hi-vis or a UK far-right vest link, so I make no claim there. Acid house's smiley (yellow; Shoom, Danny Rampling, Nov 1987; press panic Oct 1988) is the British 'yellow means the party' precedent but is pure yellow. Read for BadCode: yellow-green says 'the person on site', which is the audience. It also says 'warning', which is the message. — <https://theconversation.com/the-deep-political-power-of-fluoro-how-hi-vis-became-a-symbol-of-working-class-masculinity-238584>
- **[verified]** Brand precedent: I found no brand known for #BADC0D and none that names its colour by a hex pun (absence of hits, not proof of absence). The closest big-brand ancestor is the original Android green #A4C639 (2007, Irina Blok), chosen because it 'reminded us of a nostalgic code colour and would stand out against a dark background'; replaced in 2019 by #3DDC84 for colour-blind accessibility. So lime-on-dark as 'code colour' has a very large incumbent. #BADC0D is yellower and more acid, and its origin would be a hex pun, not phosphor nostalgia. — <https://en.wikipedia.org/wiki/Android_green>
- **[verified]** CSS shorthand doubles each digit. #BAD = #BBAADD = RGB(187, 170, 221), a pale violet, about HSL(260, 43%, 77%). #C0DE = #CC00DDEE = RGBA(204, 0, 221, 0.93), a hard electric magenta. Both are legal colours that literally spell the words, but they are purples and nothing like #BADC0D. So the pun works only at six digits. — <https://en.wikipedia.org/wiki/Web_colors>

## Precedents

- **Android robot, original green #A4C639** — Small yellow-green robot in profile, chosen as a code colour that would stand out on dark backgrounds; replaced in 2019 by #3DDC84. **Lesson:** Lime-on-dark as 'code colour' is already owned by a giant, so BadCode must not use a friendly robot or plain green, and should lean acid and warning-yellow instead. — <https://en.wikipedia.org/wiki/Android_green>
- **ITF optic yellow tennis ball** — Fluorescent yellow-green felt, about #ccff00 to #dfff00 by secondary sources, approved 1972 for TV visibility. **Lesson:** A colour that was engineered for being seen on any screen is culturally read as 'ball', so keep the mark dark-dominant and use the colour as one small event. — <https://edition.cnn.com/style/article/artsy-tennis-ball-design-artsy/index.html>
- **High-visibility clothing (EN ISO 20471, ANSI 107)** — Fluorescent yellow-green or orange garments with reflective bands. **Lesson:** The colour already means 'someone is working here' to the target reader, and 'danger, look out' to everyone. Use hi-vis grammar (bands, stencils, hazard) rather than a generic neon. — <https://en.wikipedia.org/wiki/High-visibility_clothing>
- **Gilets jaunes yellow vest** — Ordinary hi-vis vest worn as a protest uniform in France from 2018, tied to a 2008 in-car law. **Lesson:** Proof a hi-vis garment can become a working-class political mark overnight. Also a warning: do not make a vest the logo, since it hands BadCode a political tribe it does not want. — <https://en.wikipedia.org/wiki/Yellow_vests_movement>
- **Acid house smiley (Shoom, 1987-88)** — A yellow smiley face, adopted as the symbol of British acid house, then of the drug panic. **Lesson:** A pared-down face in a single yellow became Britain's best-known subcultural mark. BadCode could invert it: the same 'face' with the smile removed, in a duller, sicker yellow-green. — <https://en.wikipedia.org/wiki/Acid_house>
- **Hexspeak crash codes (0x8BADF00D, 0xBAADF00D, 0xDEADC0DE)** — Hex words used as debug markers: bad food, dead code, and so on. **Lesson:** Programmers already treat 'a hex number that reads as a word' as a sign of something broken, which is the exact meaning BadCode wants, and needs no explanation for coders. — <https://en.wikipedia.org/wiki/Hexspeak>
- **Linux kernel BUFPAGE_MAGIC 0xBADC0DEDDEADBABE** — A 64-bit sentinel that starts with BADC0DED. **Lesson:** A verified, quotable origin for the hex claim, so the pun is a fact, not a stretch, and a caption can say 'this number is in the Linux kernel'. — <https://lkml.iu.edu/hypermail/linux/kernel/9901.0/0606.html>

## Clichés to avoid

- Matrix-style green code rain, or any glowing green terminal text, and plain phosphor green on black.
- A friendly lime robot or mascot (the Android territory).
- Curly braces, angle brackets, </>, slashes, semicolons or cursor blocks as the C or as decoration (the founders' own rejection).
- Circuit-board traces, binary or hex digits streaming down a screen, and a printed hex dump as wallpaper.
- A skull, or the caution-triangle used as a plain warning icon.
- Neon-gradient 'cyber' glow and glitch RGB-split effects.
- A vest or gilet silhouette: it gives away a political tribe.
- Slapping a hex string on as decoration ('#BADC0D' as a tag) without it being the logic of the mark.

## Risks

- **(high)** The hex pun is invisible to the audience. The working-class UK reader is not a coder and will read 'BADC0DE' as letters and a zero, at best 'bad code'. The colour will not decode as a joke; it will just be a colour. — The pun is a reward for coders and a bonus for the founders, not the mechanism. The mark must work on shape and colour alone, and the hex fact belongs in a caption or Easter egg.
- **(medium)** Red-green colour blindness and the Android incumbent. Yellow-green next to a red dot (the founders' Terminator idea) is a red/green pair that fails for about 1 in 12 men. Android already dropped its green for accessibility. — Use luminance contrast, not hue contrast, for the essential shape (lime on near-black is fine at 12-13:1). Do not put the lime and a red dot in the same small mark, or if you do, do not rely on hue to tell them apart.
- **(medium)** Print reproduction: the acid colour is out of CMYK gamut and will print as a dull olive-mustard unless a fluorescent spot ink over white is paid for. Stickers, sleeves and stencils are where this bites. — Decide the CMYK fallback up front, keep a one-colour black-only version that carries the whole mark, and treat the neon spot ink as a bonus for the record sleeve.
- **(medium)** Screen colour is not fluorescence. On a phone, #BADC0D reads as a glowing green, not day-glo, and on OLED in dark mode it can look sickly, or vanish into a JPEG-compressed avatar with a lime-on-black border. — Test at 16px favicon and 98px avatar sizes, and in avatar circle crops. Keep the coloured area big enough to survive compression.
- **(medium)** Hi-vis carries political freight in UK culture (politician photo-ops, protest vests, 'the working man'). It can read as 'Reform-adjacent workwear' or as patronising if overplayed. — The verified sources say hi-vis is a staged political symbol. Use the colour as a warning light on a dark field, not as a garment or worker figure.
- **(low)** Evidence for the founders' actual audience is thin. I found no verified data on how UK working-class viewers respond to acid yellow-green as a brand colour; the culture claims are secondary and mostly Australian/French. — Consistent with the repo's own rule not to assert unmeasured audience claims. Treat the class-meaning of yellow-green as a hypothesis to test with real people.

## Logo ideas this agent proposed

### The Zero Eye

**Sketch in words:** Near-black square (#0a0a0a). Centre-left, the word BADC0DE in a heavy, monospaced, slab-cut stencil in off-white, seven glyphs in one line. The zero is NOT a letter: it is a solid #BADC0D circle the exact height of the capitals, with no slash and no inner counter. Everything else stays white and static. For the avatar and favicon, crop to the circle alone, filling about 40% of the square, sitting slightly above centre on black.

**Why it fits:** The zero is the hex joke and the Terminator dot in one shape, and the dot is a status LED that is 'on' in the wrong colour: acid instead of red or green, which is unsettling and un-cliched. It uses the founders' existing 'tiny LED points of light on near-black' register, and it draws in one marker stroke.

**Weakness:** A lone glowing dot is the most common brand device there is (Recording, Uber-ish, every 'AI' startup). The mark only becomes BadCode's if the lettering is odd enough; the wordmark carries the weight, and the avatar alone may look generic.

### Colour Is The Logo

**Sketch in words:** A full-bleed field of flat #BADC0D. On it, in black, the text #BADC0D set in a plain monospaced typeface, small, lower left, like a colour-picker label. Nothing else. As a video ident: the frame flashes black to #BADC0D, holds two seconds, the text types itself, then cuts to black. On a record sleeve it is a plain lime cover with the black hex label.

**Why it fits:** It is the simplest possible mark, unmistakably ours because the number is the name, and it reads on Spotify as a solid, loud square in a grid of dark album art. It also smuggles the pun as text a non-coder can still read as a code.

**Weakness:** It depends on brand discipline and on the number being recognised; without the label it is just a lime square, and in CMYK it goes olive. It also reads as 'a colour', not a character, and it has no menace on its own.

### The Warning Blade

**Sketch in words:** Near-black square. One thin vertical bar of #BADC0D, about 6% of the width and about 60% of the height, sitting centred slightly left, with a single circular dot of the same lime below it, separated by a gap equal to the bar's width, dot diameter equal to bar width times 1.6. It is an exclamation mark drawn with the studio's own 'thin vertical blade of cold light', and the dot is the eye.

**Why it fits:** It links the existing register (vertical blade, tiny LED) to hi-vis warning yellow-green, and it reads as 'something has gone wrong' to anyone, coder or not. It is drawable in two marker strokes and survives at 16px.

**Weakness:** An exclamation mark is a highly generic warning icon and can look like an error dialog or a Kickstarter badge; it needs a distinctive proportion (very thin bar, oversized gap) to feel authored rather than stock.

### Bad Sticker

**Sketch in words:** A rounded-rectangle hazard-tape label, #BADC0D with a black border, containing the black stencil text 0xBADC0DE with a slashed zero, over a diagonal black hazard-stripe band along the bottom edge. It is meant to be printed as a real sticker on laptops, cabinets and bin lorries, and appears on video as a label slapped onto a shot (a 'defect' tag on a machine).

**Why it fits:** Turns the logo into an object the audience meets in the world, like a hi-vis warning tag, and it takes on the story: BadCode as the 'do not use' sticker a technician puts on a broken machine. It suits the stencil, the sticker and the ident in the founders' list and needs no character drawing.

**Weakness:** Hazard stripes plus a hex string is close to a dozen hacker and industrial-goth brands, and the hex prefix means nothing to non-coders. It reads more 'workshop' than 'threatening AI from the future'.

### The Sick Smiley

**Sketch in words:** A circle of #BADC0D on near-black, with two small black square eyes on the upper third and NO mouth: only a very thin horizontal black slit, straight, halfway between eyes and chin. It is the acid-house smiley with the smile removed, in a sour, sickly yellow-green instead of happy yellow. Ident: the flat face holds for two seconds, and one eye goes out.

**Why it fits:** Uses the only verified British subcultural yellow mark (acid house) and flips it into the contempt-with-care voice: the face that used to say 'party' now says 'deadpan'. It gives BadCode an actual face with menace and is drawable in five strokes.

**Weakness:** It is a face, and the founders want a threat rather than a friendly mascot. A blank smiley is also an established meme trope (Smile, Bad Smile, Trollface reversal), and an acid-house smiley without the smile risks looking like a copy of an existing drug-culture joke.

## Gaps — what this brief could not verify

I issued 6 WebSearch calls (the brand-colour query internally ran two or three follow-up queries, so the true count may be a few higher, but I stayed within the budget as I counted it). Not verified: any official OS, debugger or crash-code use of 0xBADC0DE itself (only the kernel BADC0DED-prefixed constant and exploit filler code); a nearest Pantone (values paywalled, colorhexa and encycolorpedia gave 403); the EN ISO 20471 chromaticity box and luminance minimum; any UK-specific source on hi-vis and rave or far-right associations; whether any brand uses #BADC0D or a hex pun colour (no hits, not proof); the ITF's own official optic yellow value (two secondary sources disagree, #ccff00 vs dfff4f). All colour maths (contrast ratios, Lab distances, decimal values) is my own computation and unsourced. I could not see any logo images; all mark descriptions are from text."
