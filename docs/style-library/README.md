# The style library

> **Read only by the `story-style` interview** (Kai, 2026-10-28). Not a house style, not a
> default, not a shortlist. It is a wide menu so a new story can find a look and a sound of its
> own. No other skill, CLAUDE.md or memory may point here: `scripts/style-lint.py` fails if one does.

**How it is used.** The interview starts from the story (what it argues, who it is for, how the end
should feel), and only then opens this index. It proposes options from **at least three different
families**, **at least one off the library** (invented for this story), and avoids a style another
story already uses (the *Used by* column) unless asked. The picked style is **copied** into the
story's `look.md` / `sound.md` (the parts it needs, adapted) and named on its `**Library:**` line.
Editing an entry here never changes a story that has already picked it.

**Where it came from.** 20 research agents, 2026-10-28, one per family (10 visual, 10 music), each
told to say what a style undermines as well as what it serves. They wrote from model knowledge; a
second pass of 20 agents then checked every entry on the web (67 searches): 627 references
confirmed, 48 corrected, 23 unconfirmed (marked in place), none found to be invented outright. Engine
notes are mostly **untested first guesses** (136 of 159), 7 documented, 16 corrected; each entry's
*Web check* section says which. Recurring engine fact: **Flow has one prompt box and no exclude
field**, so what a style must avoid is written into the prompt as what it should be instead. Rebuild this index with
`python3 scripts/story-style/library.py index`. Add an entry by writing a file in `look/` or
`sound/` with the same sections, and its slug to `families.json`.


## Looks


### Film movements and national cinemas

These are looks that came out of particular economic and political conditions: postwar rubble, Weimar inflation, revolution, class resentment, Cold War censorship. That gives them a built-in argument about who gets seen and how. They differ mainly in how much they trust the real world (neorealism, kitchen-sink, Dogme) versus how much they distrust it (Expressionism, montage, Czech satire). Nothing was checked on the web for this entry, so engine notes are working knowledge of Flow, Nano Banana and Veo to be tested, not verified facts.

| Style | In one line | Used by |
| --- | --- | --- |
| [Italian neorealism](./look/italian-neorealism.md) `italian-neorealism` | Ordinary people in real streets in flat daylight, shot like a witness not a stylist. | — |
| [German Expressionism](./look/german-expressionism.md) `german-expressionism` | Painted, distorted sets and knife-edge shadows that put a character's mental state on the walls. | — |
| [Soviet montage](./look/soviet-montage.md) `soviet-montage` | Meaning made by collision between shots: low angles, hard cuts, masses of bodies and machinery. | — |
| [British kitchen-sink and social realism](./look/british-kitchen-sink-social-realism.md) `british-kitchen-sink-social-realism` | Northern and working-class Britain in grey daylight, shot at human height with real rooms and real money worries. | — |
| [French New Wave](./look/french-new-wave.md) `french-new-wave` | Jump cuts, street shooting and a playful, essayistic camera that talks back at the audience. | — |
| [Dogme 95](./look/dogme-95.md) `dogme-95` | Ugly-on-purpose handheld digital video: no lights, no props, no score, raw performance. | — |
| [Hong Kong 1990s (neon, step-printing and heroic bloodshed)](./look/hong-kong-1990s.md) `hong-kong-1990s` | Saturated neon night streets, smeared step-printed motion, and tiny rooms of lonely people. | — |
| [Czech New Wave](./look/czech-new-wave.md) `czech-new-wave` | Gently absurd, cruelly funny 1960s Czechoslovak satire of bureaucrats and ordinary people in muted colour. | — |

*Not yet written up:* Japanese golden age and Japanese New Wave (Ozu, Kurosawa, Oshima): strong but covered partly by other families; Indian parallel cinema and Bollywood masala: very different, worth its own entry; Third Cinema and Latin American militant cinema (Hour of the Furnaces, Memories of Underdevelopment): highly relevant politically, left out for space; New Hollywood 1970s (Taxi Driver, Network, The Conversation): usable, but close to common AI 'gritty film' defaults; Free Cinema documentary shorts and Humphrey Jennings' wartime British documentaries: folded partly into British social realism; Nollywood and Iranian post-revolution cinema (Kiarostami): distinct but less verified for prompting; Berlin School and contemporary European slow cinema.

### Genre cinematography

These are looks that cinema built to serve one kind of story: noir for corruption, the western for lone justice, the paranoid thriller for institutions. Each carries a built-in worldview, so picking one imports its politics and its moral shape as well as its lighting. Check that the genre's assumptions fit the argument before you commit. All eight are rendered through Flow, where the frame is 16:9 or 9:16, so ratios like 1.37:1 and 2.39:1 are done in post. No searches were run; everything here is from working knowledge, so the engine notes are stated cautiously and should be tested.

| Style | In one line | Used by |
| --- | --- | --- |
| [Film noir](./look/film-noir.md) `film-noir` | Black-and-white crime melodrama lit with hard top and side light, where the city is a trap and the powerful are never in the frame. | — |
| [Spaghetti western](./look/spaghetti-western.md) `spaghetti-western` | Sun-scorched widescreen with extreme close-ups of eyes, long silences and operatic, cynical violence. | — |
| [1970s paranoid thriller](./look/seventies-paranoid-thriller.md) `seventies-paranoid-thriller` | Murky, long-lens conspiracy cinema where offices and surveillance are the threat and the lighting hides the faces. | — |
| [Technicolor musical](./look/technicolor-musical.md) `technicolor-musical` | Saturated three-strip colour, theatrical sets and choreographed camera, where a song takes over the world. | — |
| [British folk horror](./look/british-folk-horror.md) `british-folk-horror` | Pale rural England in overcast daylight, where tradition, land and community are the threat. | — |
| [Retro-futurist dystopia](./look/retro-futurist-dystopia.md) `retro-futurist-dystopia` | A bureaucratic future imagined by the 1960s-80s: pale sterile corridors, wide lenses and clumsy, over-engineered machinery. | — |
| [Heist and caper](./look/sixties-heist-caper.md) `sixties-heist-caper` | Bright, cool, rhythm-driven crime comedy where a crew of working people outwit an institution, shot with a wink. | — |
| [1970s disaster epic](./look/seventies-disaster-epic.md) `seventies-disaster-epic` | All-star ensemble in a glossy, bright, over-built setting that is about to fail because someone cut corners. | — |

*Not yet written up:* Courtroom and procedural drama: flat, institutional framing with a lot of talking; usable but close to the 1970s paranoid thriller visually and hard to make visually varied; Cold War spy drama (grey, tobacco-stained, wide interiors, a la Smiley-era British TV): overlaps with the paranoid thriller and the dystopia entries; Italian giallo: saturated coloured gels and stylised murder set-pieces, strong look but violence-centred and likely to hit policy blocks; 1980s/90s neon action and cyberpunk: very over-represented in AI output already, so not a useful addition to the menu; Hammer/gothic horror: candle-lit saturated colour; a cousin of folk horror but less tied to land and class; Epic/sword-and-sandal and Biblical Technicolor spectacle: useful for empire and ruler satire, but a large-cast cost problem; Screwball and Ealing-style comedy: closer to the British social comedy family than to genre cinematography, but excellent for working-class satire.

### Hand-made animation

These are looks where the viewer can see a human hand (thumbprints, scissor edges, brushstrokes, eraser smudges) and where the medium's limits become part of the voice. For a UK working-class audience that tangible, small-scale, made-in-a-shed quality can read as honest and warm, which is useful cover for dark satire. The shared engine problem is that Flow's models lean towards smooth, glossy, 3D-render-like output, so every style here needs to be pushed away from clean CGI and towards stepped motion, real materials and visible imperfection.

| Style | In one line | Used by |
| --- | --- | --- |
| [Plasticine clay stop-motion](./look/plasticine-clay-stop-motion.md) `plasticine-clay-stop-motion` | Characters and sets modelled in plasticine and photographed one frame at a time, with fingerprints and mouth shapes you can see. | — |
| [Textured puppet stop-motion](./look/puppet-stop-motion.md) `puppet-stop-motion` | Fabric, fur, wire and hard-resin puppets in richly detailed miniature worlds, animated frame by frame with a slight stutter. | — |
| [Paper cut-out collage](./look/paper-cutout-collage.md) `paper-cutout-collage` | Flat figures with jointed limbs cut from paper, card and found imagery, moved around like a pop-up stage. | — |
| [Silhouette shadow animation](./look/silhouette-shadow-animation.md) `silhouette-shadow-animation` | Black cut-out figures on a glowing, coloured backdrop, with delicate lace-like detail and no interior faces. | — |
| [Rotoscope / painted-over live action](./look/rotoscope-painted-live-action.md) `rotoscope-painted-live-action` | Live-action footage traced or painted over frame by frame, so real movement wears a wobbly drawn skin. | — |
| [Paint-on-glass oil animation](./look/paint-on-glass-oil-animation.md) `paint-on-glass-oil-animation` | Wet oil paint smeared and reworked with fingers on glass, photographed after each tiny change, so every image melts into the next. | — |
| [Charcoal drawing and erasure animation](./look/charcoal-erasure-drawing.md) `charcoal-erasure-drawing` | A single charcoal drawing continually redrawn and smudged, so each frame leaves ghost traces of what was there before. | — |
| [Pinscreen animation](./look/pinscreen-engraving-animation.md) `pinscreen-engraving-animation` | Thousands of pins pushed in and out of a board, lit from the side, so the image is built from shadow like a living engraving. | — |

*Not yet written up:* Sand animation on a lightbox (Caroline Leaf's The Owl Who Married a Goose, 1974): close to paint-on-glass, so folded in rather than separate; Czech and Eastern European object and found-material surrealism (Jan Svankmajer's Dimensions of Dialogue, 1982): very distinctive but sits between puppet and clay and is hard to prompt; Hand-drawn watercolour animation (e.g. Isao Takahata's The Tale of the Princess Kaguya, 2013): omitted as it is closer to drawn animation than hand-made craft, and too costly to hold consistent; Direct-on-film / scratch animation (Len Lye, Norman McLaren): abstract, rarely suited to narrative satire; Needle-felted wool and fibre animation: beautiful but a close cousin of textured puppet stop-motion; Cardboard and recycled-junk stop-motion (e.g. Michel Gondry's cardboard sets): a lo-fi variant of the puppet and clay styles.

### Graphic and digital animation

These are all styles where the image is openly designed rather than photographed: flat shapes, drawn lines, pixels, polygons, paper cut-outs or diagrams. That makes them forgiving for generators, because they don't depend on photoreal detail. It also makes them risky, because the generic AI default (glossy, smooth, soft-lit) is the thing most likely to leak back in. Each entry says which kind of argument it carries and which it would undermine. Note: no web searches were run; every reference and engine claim comes from established knowledge, and the engine notes are behaviours to test in a first round, not guarantees.

| Style | In one line | Used by |
| --- | --- | --- |
| [UPA mid-century limited animation](./look/upa-limited-animation.md) `upa-limited-animation` | Flat, graphic, modernist cartoons from the 1950s: shapes and colour blocks instead of rounded rubber-hose realism, with movement kept to a few strong poses. | — |
| [Cut-out and paper collage animation](./look/cutout-paper-collage.md) `cutout-paper-collage` | Characters and sets built from flat pieces of paper, photographs or old engravings that slide, jerk and hinge in front of each other. | — |
| [Comic-book 3D (halftone, offset print, ink lines)](./look/comic-book-3d-halftone.md) `comic-book-3d-halftone` | 3D-rendered scenes made to look printed from a comic: visible halftone dots, misaligned colour plates, hand-inked outlines and on-screen panels and captions. | — |
| [Painterly 3D (hand-painted textures, brushed light)](./look/painterly-3d.md) `painterly-3d` | 3D characters and sets with hand-painted textures, visible brush strokes and ink-and-paint lighting, so the film looks like a moving oil or gouache illustration. | — |
| [Low-poly and PS1-era 3D](./look/low-poly-ps1-3d.md) `low-poly-ps1-3d` | Chunky, faceted 3D with few polygons, flat-shaded or affine-warped textures, low resolution and a wobbling, unfinished feel. | — |
| [Pixel art (game-screen)](./look/pixel-art-game.md) `pixel-art-game` | Images built from visible square pixels on a limited palette, in the manner of 8-bit, 16-bit and modern indie games. | — |
| [Infographic and data motion graphics](./look/infographic-motion-graphics.md) `infographic-motion-graphics` | Charts, maps, icons, figures and typography animated to show an economic argument as a moving diagram. | — |
| [1990s cel-anime (hand-painted, dense and grave)](./look/90s-cel-anime.md) `90s-cel-anime` | The look of Japanese theatrical and OVA animation of the late 1980s and 1990s: painted cel colour, hand-drawn detail, hard light, grainy film and a serious, grown-up register. | — |

*Not yet written up:* Rotoscope animation (Waking Life, A Scanner Darkly): painted-over live action; strong for dreamy unease, but needs live footage as input.; 1-bit and dithered monochrome (Return of the Obra Dinn): very distinctive but narrow, and close to pixel art.; Corporate flat vector ('Memphis' explainer look): deliberately left out as the default AI-generic trap, not a style to choose.; Whiteboard/hand-drawn explainer: folded into the infographic entry (RSA Animate).; Isometric diorama / tilt-shift miniature: usable for system overviews but thin on emotional range.; Eastern European poster-graphic animation (Zagreb school): close to UPA but with a harder political edge; a candidate for a later pass.; Chibi / cute anime sub-styles: not suited to this audience and tone..

### Print, poster and illustration

These are looks borrowed from things that were printed or drawn by hand: flat ink, limited colour, hard outlines, and typography that does the arguing. Their shared strength is that they say "this is a point of view" before a word is spoken, and they hide the generator's usual weakness (photographic mush) by working in simplified shapes. Their shared risk is motion: Veo wants to add depth, shading and camera parallax, which kills the flatness that makes the style work.

| Style | In one line | Used by |
| --- | --- | --- |
| [Woodcut / linocut protest print](./look/woodcut-linocut-protest.md) `woodcut-linocut-protest` | Carved-block black-and-white (or one spot colour) imagery with gouged white lines, in the tradition of the wordless woodcut novel and the labour-movement print. | — |
| [Risograph limited-colour print](./look/risograph-two-colour.md) `risograph-two-colour` | Grainy, overprinted two- or three-colour illustration in fluorescent pink, blue, yellow, with deliberate misregistration. | — |
| [Constructivist agitprop poster](./look/constructivist-agitprop-poster.md) `constructivist-agitprop-poster` | Diagonal, red-black-cream geometric posters with photomontage and heavy sans-serif type, in the manner of 1920s Soviet agitprop. | — |
| [WPA / New Deal screenprint poster](./look/wpa-new-deal-poster.md) `wpa-new-deal-poster` | Flat, hopeful, heavy-shouldered figures in a few saturated screenprint colours, with the dignity-of-work look of 1930s American public posters. | — |
| [Ligne claire comic](./look/ligne-claire-comic.md) `ligne-claire-comic` | Uniform clean outlines, flat colour, no hatching and exact, researched backgrounds, in the tradition of the Franco-Belgian adventure comic. | — |
| [Georgian hand-coloured satirical etching](./look/georgian-satirical-etching.md) `georgian-satirical-etching` | Crowded, caricatured, hand-coloured etchings of politicians, bankers and kings, with speech scrolls and labels, from the 1780s to 1830s London print shop. | — |
| [Ladybird mid-century picture book](./look/ladybird-mid-century-picture-book.md) `ladybird-mid-century-picture-book` | Painted, warm, orderly British children's reading-book illustration of the 1950s-60s, used deadpan on adult subjects. | — |
| [Isotype pictogram infographic](./look/isotype-pictogram-infographic.md) `isotype-pictogram-infographic` | Rows of identical flat icon-people and objects, counted out as units, used to make economics visible at a glance. | — |

*Not yet written up:* Manga / shonen-seinen comic style: very usable but a tonal outlier for this UK audience and well covered elsewhere; WPA-adjacent mid-century modern flat vector (Saul Bass-style title design): more a design movement than print; Soviet socialist realist painting poster: overlaps constructivism but heavier and more nostalgic; Punk photocopy collage / cut-and-paste zine (Jamie Reid-style ransom note collage): strongly British and politically fitting, worth its own entry; Peter Kennard-style political photomontage: close to constructivist photomontage; 1930s American editorial newspaper cartoon with crayon texture; Tarot / medieval illuminated manuscript marginalia: a less obvious candidate; Pop-art halftone comic (Ben-Day dots); Japanese ukiyo-e woodblock print.

### Fine-art movements as moving image

These styles borrow the composition rules, light logic and colour discipline of a painting tradition and apply them to a moving frame. What joins them is that each carries a built-in attitude to power and ordinary people (sympathy, menace, irony, heroism, mockery), so choosing one is choosing an argument as well as a look. They split broadly into painterly-lit styles (Dutch, Hopper) that survive Veo's photoreal bias, and flat or graphic styles (ukiyo-e, Pop, Lowry, muralism) that fight image-to-video and need careful motion design. Notes in this library were written from the researcher's own knowledge; no web searches were used, so engine-behaviour claims are general and should be tested with a cheap still round before committing.

| Style | In one line | Used by |
| --- | --- | --- |
| [German Expressionism (painted-set cinema)](./look/german-expressionism-fine.md) `german-expressionism-fine` | Distorted, angular, shadow-slashed worlds where the set expresses the character's fear instead of describing a place. | — |
| [Dutch Golden Age chiaroscuro](./look/dutch-golden-age-chiaroscuro.md) `dutch-golden-age-chiaroscuro` | Single-source, candle- or window-lit scenes with deep brown shadow and warm faces, as in Rembrandt and Vermeer. | — |
| [Hopper-style American realism](./look/hopper-american-realism.md) `hopper-american-realism` | Still, sunlit or lamp-lit modern interiors and streets, with lonely figures and hard geometry, as in Edward Hopper. | — |
| [Ukiyo-e woodblock](./look/ukiyo-e-woodblock.md) `ukiyo-e-woodblock` | Flat colour, bold black outline, patterned surfaces and tilted high viewpoints in the manner of Edo-period Japanese prints. | — |
| [Pop Art (Ben-Day, flat colour, mass-media collage)](./look/pop-art-graphic.md) `pop-art-graphic` | Comic-book dots, hard outlines, primary colours and recycled advertising imagery, as in 1950s-60s British and American Pop. | — |
| [Socialist Realism and the heroic worker](./look/socialist-realism-heroic.md) `socialist-realism-heroic` | Monumental, optimistic, low-angle images of workers, tractors and furnaces as in Soviet painting, sculpture and film of the 1930s to 1950s. | — |
| [Mexican muralism (industrial-epic fresco)](./look/mexican-muralism.md) `mexican-muralism` | Wall-sized, crowded, flat-modelled scenes of workers, machines and the people who own them, in the manner of Rivera, Orozco and Siqueiros. | — |
| [Lowry-style northern industrial townscape](./look/lowry-northern-industrial.md) `lowry-northern-industrial` | Pale, flattened mill-town streets filled with tiny matchstick figures under white sky, after L. S. Lowry. | — |

*Not yet written up:* Surrealism (Magritte-style plain-object dream imagery): strong for satirical visual metaphors, left out to avoid overlapping with Pop and Expressionism; Bauhaus and Constructivist design (grids, primary shapes, photomontage): close to Pop and Socialist Realism graphically but very different in feeling; Art Nouveau (whiplash line, floral frames, poster lettering): decorative, good for a sarcastic 'belle epoque' narrator but low on political content; Georgian and Victorian caricature (Hogarth, Gillray, Cruikshank): British political satire in print; possibly the closest tradition to BadCode's tone, and worth its own entry; Kitchen Sink realism painting and social-realist photography of the 1950s-60s: grounded UK domestic grit; Impressionism and Post-Impressionism: broken colour and light; rarely fits political satire; Futurism and Vorticism: speed, machines and angular dynamism; good for energy but a narrow fit; Dada photomontage (Hoch, Heartfield): collage as political weapon, strong fit but overlaps Pop collage and is hard to animate.

### Photography traditions

These eight are photographic ways of looking, each with its own claim about what a picture is evidence of: a place, a crowd, a crime, a lifestyle, an institution. That claim is what makes them usable for satire, because the story can borrow the credibility of the genre and then break it. They are mostly still-image idioms, so animating them in Veo costs something. Movement tends to wash out the very thing that defines them (the frozen instant, the grain, the flash), so most of them work best as held plates with small, motivated motion.

| Style | In one line | Used by |
| --- | --- | --- |
| [British black-and-white social documentary](./look/british-bw-social-documentary.md) `british-bw-social-documentary` | Grainy monochrome street and community photography of ordinary British working life, from the 1930s Picture Post era to the 1980s industrial-decline reportage. | — |
| [Saturated British seaside and high-street colour](./look/saturated-british-seaside-colour.md) `saturated-british-seaside-colour` | Ring-flash, hyper-saturated colour photography of British leisure and consumption, ironic and affectionate at the same time. | — |
| [New Topographics (deadpan industrial landscape)](./look/new-topographics.md) `new-topographics` | Flat, neutral, emotionless photographs of warehouses, car parks, housing estates and industrial buildings, as if the picture were an inventory. | — |
| [Flash-lit tabloid crime photography](./look/flash-tabloid-crime-photography.md) `flash-tabloid-crime-photography` | Hard on-camera flash at night, black-and-white press pictures of crime scenes, crowds and spectacle, with a sleazy sense of arriving first. | — |
| [Instant film (Polaroid and Instax)](./look/instant-film-polaroid.md) `instant-film-polaroid` | Square-ish, soft, colour-shifted snapshots with white borders, shot as private memory and pinned to a wall. | — |
| [Victorian wet-plate and carte-de-visite portraiture](./look/victorian-wet-plate-street-life.md) `victorian-wet-plate-street-life` | Slow, silvery 19th-century collodion portraits and street scenes in which people stand stiffly still and look straight at you. | — |
| [Machine-eye photography (Street View, CCTV, dashcam)](./look/machine-eye-street-view-cctv.md) `machine-eye-street-view-cctv` | Pictures taken by automated cameras with no photographer: blurred faces, stitched seams, timestamps and indifferent framing. | — |
| [Leisure-class glossy editorial](./look/leisure-class-glossy-editorial.md) `leisure-class-glossy-editorial` | Sun-drenched, perfectly composed colour photography of rich people relaxing in beautiful places, the visual language of the lifestyle magazine and the luxury advert. | — |

*Not yet written up:* Decisive-moment humanist street photography (Cartier-Bresson, Maier, Winogrand): folded into the documentary entry; would be a distinct entry with more room; Daguerreotype and early-photography portraiture: covered by the wet-plate entry; 1990s-2000s British fashion and youth-culture editorial (i-D, The Face, Corinne Day): excellent for youth and class but needs separate research; Press photojournalism of strikes and protest (miners' strike, Poll Tax): partly covered by documentary, could stand alone; Disposable-camera and early digital point-and-shoot snapshot aesthetic (2000s Britain): a strong candidate for a modern-day entry; Kodachrome slide-projector family archive: overlaps with the instant-film entry; Aerial and satellite imagery: more a data-image tradition than photography proper.

### Archive and period media textures

These styles borrow the look of a recording technology and the authority (or intimacy, or menace) that audiences already attach to it: newsreels sound official, home movies sound private, CCTV sounds like being watched. For a satirical project that claims to be received wisdom from a future that went wrong, that borrowed authority is the main asset. The shared risk is that generators render these as a filter on a clean image rather than as the real constraints of the medium (aspect ratio, lens, lighting, tape or film behaviour), and every entry says where it fails and what it would undermine.

| Style | In one line | Used by |
| --- | --- | --- |
| [1940s British newsreel](./look/forties-newsreel.md) `forties-newsreel` | Black-and-white 35mm cinema newsreel: scratched, high-contrast, shot on a few fixed lenses, with an implied booming voice-of-authority. | — |
| [UK public information film (1970s)](./look/public-information-film.md) `public-information-film` | The cheerful, then terrifying, government-commissioned short: bright, flat, saturated colour, ordinary British locations, and a gentle voice warning of preventable disaster. | — |
| [Super 8 home movie](./look/super-8-home-movie.md) `super-8-home-movie` | Silent, handheld, warm and slightly faded 8mm family film: short 3-minute rolls, light leaks and shaky memory. | — |
| [VHS camcorder (1980s-90s)](./look/vhs-camcorder.md) `vhs-camcorder` | Smeared, over-saturated tape video with timestamps, tracking glitches and a camera that never quite focuses. | — |
| [1970s British television drama](./look/seventies-british-tv.md) `seventies-british-tv` | Studio-bound videotape and 16mm film inserts: flat lighting, brown and orange interiors, theatrical performance. | — |
| [CCTV and surveillance camera](./look/cctv-surveillance.md) `cctv-surveillance` | Fixed high-angle camera, wide lens, low frame rate, timestamp: no one is directing and everybody is a suspect. | — |
| [Teletext and Ceefax page graphics](./look/teletext-ceefax.md) `teletext-ceefax` | Blocky 40-by-24 mosaic pages in eight bright colours on black: news, weather and adverts as chunky text and crude pictures. | — |
| [Tinted silent film (1910s-20s)](./look/tinted-silent-film.md) `tinted-silent-film` | Black-and-white nitrate film dyed in single colours (amber for day, blue for night), with hand-cranked motion, iris shots and intertitles. | — |

*Not yet written up:* Early webcam / dial-up internet (Geocities, MSN-era low-frame-rate webcam video, 56k pixel art): distinct and usable, cut for space; strong for a story about the 1998-2008 internet; Silent-era hand-coloured Pathecolor or Kinemacolor: overlaps with the tinted silent film entry; Open University / 1970s educational broadcast with diagrams and corduroy lecturer: close to the 1970s TV and public information entries; Home-computer era graphics (ZX Spectrum, BBC Micro loading screens): a screen-graphic texture similar to teletext; Cold War-era Super 16 documentary / 1960s cinema verite handheld: a neighbour of newsreel; Dashcam / bodycam / phone-vertical footage: modern surveillance family, covers a different era; Polaroid and magazine-print photo textures (stills only): overlaps with archive stills but not a moving-image medium.

### Television and contemporary screen grammar

These styles borrow the grammar of a format the audience already knows from the sofa or the phone, so the viewer arrives with a set of rules and the story can break them for effect. The strength is instant recognition and a built-in tone (deadpan, gravity, cosiness, hype, intimacy). The shared risk is that each format carries its own authority and its own politics: a mockumentary laughs at its subjects, a natural-history voice sounds neutral when it isn't. Pick the grammar whose attitude matches who you want the viewer to blame.

| Style | In one line | Used by |
| --- | --- | --- |
| [Mockumentary (deadpan fly-on-the-wall)](./look/mockumentary-deadpan.md) `mockumentary-deadpan` | Handheld, naturalistic workplace or community footage where people talk straight to a camera that is supposedly documenting them. | — |
| [Prestige TV drama](./look/prestige-tv-drama.md) `prestige-tv-drama` | Cinematic, restrained, long-take-friendly drama with naturalistic or sodium-lit palettes and serious performances. | — |
| [Natural-history documentary](./look/natural-history-documentary.md) `natural-history-documentary` | Epic long-lens photography of animals and landscapes with a calm, authoritative narrator, applied to human behaviour. | — |
| [Children's TV (puppet and stop-motion warmth)](./look/childrens-tv-studio.md) `childrens-tv-studio` | Soft-lit, handmade, slow-paced pre-school television with primary colours, felt and wool, and a gently sinister cheerfulness. | — |
| [Game show](./look/game-show.md) `game-show` | Bright studio set, bold graphics, a charismatic host, contestants under pressure and a prize. | — |
| [Screen-life (story told on screens)](./look/screen-life.md) `screen-life` | The whole film plays inside a laptop or phone: chat windows, video calls, browser tabs, cursor movement. | — |
| [Vertical vlog and feed video](./look/vertical-vlog-feed.md) `vertical-vlog-feed` | 9:16 handheld selfie footage, fast jump-cuts, burned-in captions and direct address, built for a phone scroll. | — |
| [1970s-80s public information film](./look/public-information-film-television.md) `public-information-film-television` | Short, stern, state-voiced warning films with plain filmstock colour, a menacing figure and a blunt instruction at the end. | — |

*Not yet written up:* Reality TV / docusoap with confessional booth and manufactured-drama edit (close to mockumentary but with producer-led cuts and ominous stings); Rolling news and breaking-news broadcast (lower-third tickers, studio anchor, live-link reporter), strong for satire but overlaps game-show graphics and screen-life; Found-footage and CCTV/bodycam (surveillance grammar, timestamps, low-res grain); Sitcom multi-camera studio comedy with laugh track; Cooking, property and makeover shows (Location Location Location style), relevant to housing satire; Talking-heads explainer / Vox-style video essay with motion graphics; Teletext and Ceefax screen grammar.

### Theatre, craft and mixed media

These styles all announce that the picture was made by hands on a stage or a table: puppets, paper, cloth, cardboard, cut photographs. That visible artifice is the family's gift to satire, because it lets the image say "this is a model of the argument" and lets caricature, scale and cruelty read as craft rather than realism. The shared risk with generators is that they smooth the handmade away, so every entry needs explicit material language and a deliberate protection of the seams.

| Style | In one line | Used by |
| --- | --- | --- |
| [Satirical latex caricature puppets](./look/latex-caricature-puppets.md) `latex-caricature-puppets` | Grotesque foam-and-latex puppets of the powerful, lit like a cheap TV studio and played for savage laughs. | — |
| [Silhouette and shadow theatre](./look/silhouette-shadow-theatre.md) `silhouette-shadow-theatre` | Black cut-out figures against a lit translucent screen, with all meaning carried by outline and movement. | — |
| [Cut-out satirical animation](./look/cutout-satire-animation.md) `cutout-satire-animation` | Photographs and engravings cut into paper-doll figures that jerk across surreal collaged sets. | — |
| [Political photomontage](./look/photomontage-agitprop.md) `photomontage-agitprop` | Photographs sliced and recombined into hard-edged images that make an accusation in a single frame. | — |
| [Miniature model world and tilt-shift](./look/miniature-tilt-shift.md) `miniature-tilt-shift` | The real world made to look like a tabletop model through narrow focus, bright colour and tiny people. | — |
| [Felt, knit and tapestry textile](./look/felt-textile-tapestry.md) `felt-textile-tapestry` | Worlds stitched from wool, felt and woven thread, where soft material makes hard subjects sting. | — |
| [Epic theatre black-box stage](./look/epic-theatre-black-box.md) `epic-theatre-black-box` | Actors on a bare black stage with chalk lines and one hard light, openly pretending the world is not there. | — |
| [Cardboard and bin-bag DIY](./look/cardboard-sweded-diy.md) `cardboard-sweded-diy` | Scenes remade by hand from cardboard, foil, tape and household junk, with the effort showing. | — |

*Not yet written up:* Paper diorama and toy theatre (Victorian Pollock's-style layered card stage) - overlaps silhouette, cut-out and cardboard entries; Punch and Judy / seaside booth glove puppetry - very British and class-relevant, but narrower than the entries chosen; Stop-motion clay and plasticine (Aardman-style) - belongs in an animation family; Tableau vivant and painted-history staging (Greenaway-style) - overlaps with epic-theatre-black-box; Marionette and string puppetry as its own entry - partly covered via Team America and Thunderbirds references; Lego/brick animation - partly covered by the DIY and miniature entries.

## Sounds


### British and Irish folk and roots

These are the musics of work, pub, chapel, picket line and street, made by and for people with little money, so they already carry class as part of their sound. What joins them is a voice that tells a story in plain words over simple, repeated forms, which suits satire about economics. They split into communal (shanty, brass band, music hall singalong), lonely (unaccompanied ballad), driving (skiffle, folk-rock) and argued (protest, Radio Ballad) registers, and the choice mostly decides whether the audience is invited to join in, to listen, or to be told off.

| Style | In one line | Used by |
| --- | --- | --- |
| [Unaccompanied traditional ballad](./sound/unaccompanied-ballad.md) `unaccompanied-ballad` | A single unaccompanied voice telling a long story-song in a modal tune, with no beat to hide behind. | — |
| [Sea shanty and work-song chorus](./sound/sea-shanty.md) `sea-shanty` | Call-and-response labour song for a crowd, led by a soloist with a gang chorus stamping the beat. | — |
| [Electric folk-rock](./sound/electric-folk-rock.md) `electric-folk-rock` | Traditional songs and tunes played by a rock band with electric guitar, fiddle and a woman or man singing straight. | — |
| [Colliery and silver brass band](./sound/colliery-brass-band.md) `colliery-brass-band` | A full brass band playing hymns, marches and arrangements, with massed warmth and a lonely cornet or euphonium solo. | — |
| [Music hall and Cockney singalong](./sound/music-hall.md) `music-hall` | Brash, comic, chorus-driven songs from Victorian and Edwardian variety theatres, played on piano with a stage-patter voice. | — |
| [Skiffle](./sound/skiffle.md) `skiffle` | Fast, cheap, homemade 1950s folk and blues played on guitar, washboard and tea-chest bass by working-class teenagers. | — |
| [Protest and union folk](./sound/protest-folk.md) `protest-folk` | A topical song with a plain voice and acoustic guitar, written to be sung at a picket line, demo or meeting. | — |
| [Radio Ballad documentary folk](./sound/radio-ballad.md) `radio-ballad` | Real speech and folk song woven together: a testimony bed with sung refrains made of the speaker's own words. | — |

*Not yet written up:* Irish pub session and rebel ballad group (Dubliners/Planxty style): overlaps electric folk, shanty and protest folk and is the most obvious Irish pick; Scots mouth music (puirt a beul) and Gaelic waulking song: striking and less obvious, but narrow for a UK-wide working-class audience; Northern Soul-adjacent working men's club cabaret and brass-and-organ club sound: more pop than folk; Morris and country dance music (melodeon, tabor): strongly rural and comic, risks twee; Gospel-tinged Welsh male voice choir and chapel hymnody: very strong for class and mining but needs careful handling to avoid cliche; Contemporary acoustic punk-folk (Pogues-style) and Britpop-era folk pop: a hybrid more than a distinct tradition.

### UK street and bass music

These styles share a lineage: Caribbean sound-system culture (dub, ragga) met British council estates, pirate radio and cheap sequencers, and each decade rebuilt it at a new tempo (jungle 160-170, garage 130-135, grime and dubstep 138-142, drill 140-145). Almost all of it is made for a room with a big low end and a crowd, which makes the sub-bass a character in its own right, and most of it is about place and class from the inside. They split on one axis that matters for BadCode: whether a voice is in front (grime, drill, garage, bassline) or whether the music is a bed under a voice (dub, trip-hop, dark dubstep, jungle instrumentals).

| Style | In one line | Used by |
| --- | --- | --- |
| [Grime](./sound/grime.md) `grime` | Aggressive, sparse, roughly 140 BPM London MC music built on cold synth stabs, sub-bass and rapid-fire spoken-sung bars delivered in a raw local accent. | — |
| [UK garage and 2-step](./sound/uk-garage-2-step.md) `uk-garage-2-step` | Skippy, swung 130 BPM club music with a shuffled broken-beat kick pattern, warm chopped vocal samples, rubbery bass and a sung or chatted topline. | — |
| [Jungle](./sound/jungle.md) `jungle` | Frantic chopped breakbeats at about 160 to 170 BPM over slow, heavy sub-bass and ragga or soul samples, from London's mid-1990s rave scene. | — |
| [Early dubstep (dark 140)](./sound/dark-dubstep-140.md) `dark-dubstep-140` | Slow, sparse 140 BPM half-time music from south London, built on huge sub-bass, dub echo and silence, long before the 'wobble drop' version. | — |
| [Trip-hop (Bristol sound)](./sound/trip-hop.md) `trip-hop` | Slow, smoky, sample-based downtempo hip-hop beats (60 to 100 BPM) with film-noir strings, dub bass and a cracked, intimate voice, from Bristol in the 1990s. | — |
| [UK drill](./sound/uk-drill.md) `uk-drill` | Cold, menacing 140 to 145 BPM trap-derived beats with sliding 808s, triplet hi-hats and dark piano or string loops under flat, deadpan rapping. | — |
| [Bassline (Sheffield and Yorkshire 4x4)](./sound/bassline.md) `bassline` | Fast, bouncy, 130 to 140 BPM four-on-the-floor club music with a rubbery, wobbling 'bass' line, chopped garage vocals and a party mood, from northern England. | — |
| [UK dub and dub poetry](./sound/uk-dub-sound-system.md) `uk-dub-sound-system` | Slow, heavy reggae-derived 70 to 90 BPM music with a deep bass, spare drums, echo and reverb effects, and a poet or deejay speaking political truth over it. | — |

*Not yet written up:* Liquid and neurofunk drum and bass: the clean 174 BPM descendant of jungle, with melodic, polished or industrial sub-styles; close to jungle in tool prompts so not given its own entry; Speed garage and 4x4 UK garage: a faster, house-leaning cousin of 2-step, partly folded into the garage and bassline entries; Road rap and UK hip-hop (boom-bap British rap): a lyrical, sample-based tradition distinct from grime and drill, belonging more with a hip-hop family; Afroswing and UK funky: warm, Afro-diasporic, dance-leaning UK sounds that are less about bass pressure and political satire; Breakbeat hardcore and happy rave: euphoric 1991 to 1993 pre-jungle rave, usable for nostalgia but weaker for political argument; Post-dubstep and UK bass/'future garage': a moody electronic offshoot of dark garage and dubstep, currently well represented by the early-dubstep and garage entries.

### Punk, rock and indie lineages

These are British guitar-band traditions from 1971 to 1995, each a different answer to how a band that is not the elite can sound like it speaks for itself. They run from shouted solidarity (Oi!, 1977 punk, pub rock) through cold analysis (post-punk) and comic observation (Britpop) to retreat (shoegaze, jangle) and spectacle (glam). Most were made on cheap kit by working-class or art-school kids, which suits BadCode's reader, but each carries a stance that can help or undermine a satirical argument.

| Style | In one line | Used by |
| --- | --- | --- |
| [UK punk, 1976-78](./sound/uk-punk-1977.md) `uk-punk-1977` | Fast, loud, three-chord guitar songs shouted by people who cannot or will not sing, aimed at named people in charge. | — |
| [Oi! and street punk](./sound/oi-street-punk.md) `oi-street-punk` | Stripped-back, chanted, football-terrace punk about work, pubs, police and the dole, sung by people from the estates. | — |
| [Post-punk](./sound/post-punk.md) `post-punk` | Angular, bass-led, cold and analytical rock that treats the mess of capitalism as a puzzle to be pulled apart. | — |
| [Britpop and kitchen-sink indie](./sound/britpop-kitchen-sink.md) `britpop-kitchen-sink` | Big-chorus guitar pop with character-sketch lyrics about ordinary British lives, wry rather than furious. | — |
| [Shoegaze and dream-gaze](./sound/shoegaze.md) `shoegaze` | A wash of heavily effected guitars with buried, hushed vocals; beautiful, blurred and inward. | — |
| [Glam rock stomp](./sound/glam-stomp.md) `glam-stomp` | Foot-stomping, handclap-driven pop-rock with sequins, glitter and a crowd chant, working-class spectacle. | — |
| [Pub rock and rhythm-and-blues rock](./sound/pub-rock.md) `pub-rock` | Lean, swinging, bar-band rock and roll with sharp working-class storytelling, the quieter ancestor of punk. | — |
| [C86 jangle and bedsit indie](./sound/c86-jangle-indie.md) `c86-jangle-indie` | Thin, chiming guitars and fragile, amateur vocals; shy, literate and defiantly small-scale. | — |

*Not yet written up:* Garage rock (1960s Nuggets-style and 2000s revival): raw and fuzzy, but largely American-coded and fewer class specifics; Riot grrrl: feminist punk with strong politics but US-centred and a different audience framing; Madchester/baggy: indie-dance fusion of the late 80s, distinct but more about the dancefloor than guitars; Krautrock/motorik: German, adjacent to post-punk's groove but not in this lineage; Art-rock (Roxy Music, Talking Heads, Radiohead): wide and mood-driven, overlaps with post-punk and glam; Folk-punk and 'Rock Against Racism' reggae-punk crossover (The Specials, 2 Tone ska): directly working-class and political, but ska may belong to another family.

### Hip-hop and spoken word

These styles all put the words first: the voice is the lead instrument and the beat is a bed that lets a sentence be heard. They differ mainly in where the voice sits (rapped on the grid, ranted off it, or spoken against it), which place the accent says you are from, and how much the music argues with the words. For a UK working-class audience the accent and register are the point, since they say whose side the story is on. Caveat: written without live web searches, so references come from memory (titles and years are ones I am confident exist) and the Suno notes are general engine behaviour, not tested for this project; verify with a small test round before locking a style.

| Style | In one line | Used by |
| --- | --- | --- |
| [Boom bap storytelling rap](./sound/boom-bap-storytelling.md) `boom-bap-storytelling` | Sample-based, swung drums and a dense, rhymed narrative verse, the 90s New York template for telling a story in character. | — |
| [UK conversational rap](./sound/uk-conversational-rap.md) `uk-conversational-rap` | Half-spoken, off-the-beat British storytelling about ordinary life, delivered in a regional accent over loose garage or hip-hop drums. | — |
| [Grime](./sound/grime-hip.md) `grime-hip` | Fast, aggressive, bass-heavy British MC music at 140 BPM, built on square-wave synths, dry drums and clipped, rapid delivery. | — |
| [Punk poetry and rant](./sound/punk-poetry-rant.md) `punk-poetry-rant` | A sharp-tongued, unmelodic British voice declaiming rhymed or free verse over a thin, repeating bass or guitar bed. | — |
| [Dub poetry](./sound/dub-poetry.md) `dub-poetry` | Poetry in Caribbean-British English performed over a slow, heavy reggae dub rhythm with deep bass and echo. | — |
| [Spoken word over a sparse bed](./sound/spoken-word-over-sparse-bed.md) `spoken-word-over-sparse-bed` | A voice speaking in near-prose over a quiet, slow, ambient or jazz-inflected bed that leaves almost every word clear. | — |
| [Trap satire](./sound/trap-satire.md) `trap-satire` | Dark, minimal 808-and-hi-hat beats with a cold, sing-rapped delivery, used to say something about money and power. | — |

*Not yet written up:* Horrorcore and abstract/underground rap (El-P style dense production), unusual but heavy in tone; Drill (UK/Chicago), a menacing cousin of trap that is tied to real violence and best avoided for satire; Jazz rap and lo-fi hip-hop as a bed for narration; Rap-musical / theatrical rap (Hamilton-style) with sung book numbers; Talking blues and folk talking-song traditions (Woody Guthrie style) that sit between spoken word and folk; Rap-rock / rap-metal fusion (Rage-style political fury); Cloud rap and emo rap, introspective rather than political.

### Electronic and synth

All of these are built from machines rather than bands, so they share a cold, exact surface that can carry either deadpan authority or sudden warmth. They differ most in where the voice sits (up front, buried, or absent) and in whose past they evoke (Thatcher-era pop, German motorway, rave field, a half-remembered school film). For a narrator who speaks with total authority from the future, this family is natural: the machine is the narrator's own native sound.

| Style | In one line | Used by |
| --- | --- | --- |
| [Early-80s British synth-pop](./sound/british-synth-pop-1980s.md) `british-synth-pop-1980s` | Melodic, hooky pop built on polysynths and drum machines, with a deadpan or theatrical vocal and lyrics about money, class and work. | — |
| [Motorik / krautrock](./sound/motorik-krautrock.md) `motorik-krautrock` | A relentless, steady 4/4 drive with hypnotic repeating synth and guitar figures, built for forward motion rather than verses and choruses. | — |
| [Acid house / UK rave](./sound/acid-house-uk-rave.md) `acid-house-uk-rave` | Squelching 303 basslines over a hard 909 four-on-the-floor, built for dancing and collective release, with samples and shouted hooks. | — |
| [Ambient / drone](./sound/ambient-drone.md) `ambient-drone` | Slow, beatless washes of sustained synth and tone designed to sit under narration and set a mood without demanding attention. | — |
| [Hauntology / BBC-era library music](./sound/hauntology-library-music.md) `hauntology-library-music` | Warped, tape-worn electronics that sound like a half-remembered public information film or 1970s schools broadcast, haunted by a lost future. | — |
| [Chiptune / 8-bit](./sound/chiptune-8bit.md) `chiptune-8bit` | Music made from the square, pulse, triangle and noise waves of old home computers and games consoles, fast, bright and melodic. | — |
| [Synthwave / outrun](./sound/synthwave-outrun.md) `synthwave-outrun` | A modern revival of 1980s film-score synths and gated drums, neon-lit and nostalgic for a decade that the listener often did not live through. | — |
| [EBM / industrial](./sound/industrial-ebm.md) `industrial-ebm` | Hard, sequenced, military-precise electronic body music with shouted or chanted vocals and a menacing, mechanical pulse. | — |

*Not yet written up:* Techno (Detroit / Berlin): overlaps with acid house and EBM, and it is largely wordless and structure-light; IDM / glitch (Autechre, Squarepusher): too dense and unpredictable for narration beds, and hard to steer in Suno; Italo disco / Hi-NRG: a possible bright, camp alternative to synth-pop; Dub techno / Basic Channel style: a hypnotic, spacious cousin of ambient and motorik; UK garage / 2-step and grime-adjacent electronic: strongly relevant to a UK working-class audience, but sits closer to the dance/urban family; Vaporwave / plunderphonics: a sample-decay style close to hauntology; Berlin-school sequencer music (Tangerine Dream): a long-form arpeggio cousin of motorik and synthwave.

### Classical, choral and orchestral

These styles share acoustic instruments, written-out arrangements and a sense of occasion: the music arrives sounding like it has authority, tradition or a ritual behind it. That makes the family strong for irony (solemn form carrying a savage or silly message) and weak when a story needs to sound casual, current or street-level. No web searches were run for this entry; engine notes below come from known Suno behaviour and should be confirmed by listening tests, and the story's sound.md should record what actually happened.

| Style | In one line | Used by |
| --- | --- | --- |
| [Baroque concerto and ground bass](./sound/baroque-concerto-motor.md) `baroque-concerto-motor` | Bright, driving strings and harpsichord in sequences and ostinati, with a rigid mechanical forward motion. | — |
| [Minimalism (pulse music)](./sound/minimalist-pulse-music.md) `minimalist-pulse-music` | Steady repeated patterns that shift gradually, pulsing eighth notes in pianos, mallets and voices, building trance-like momentum. | — |
| [English choral and hymn](./sound/english-cathedral-choral-hymn.md) `english-cathedral-choral-hymn` | Unaccompanied or organ-backed choir singing in plain English, broad modal harmony, a congregational sense of shared voice. | — |
| [String quartet and chamber strings](./sound/string-quartet-chamber.md) `string-quartet-chamber` | Four solo string players, intimate and exposed, from sparse single lines to scraping, urgent rhythmic writing. | — |
| [Late-romantic orchestral](./sound/late-romantic-orchestral.md) `late-romantic-orchestral` | Full symphony orchestra at maximum scale: huge string melodies, brass chorales and timpani, built to overwhelm. | — |
| [Comic opera and patter song](./sound/comic-opera-patter-satire.md) `comic-opera-patter-satire` | Fast, witty sung satire with stage-ready diction, from Mozart's servants to Gilbert and Sullivan's list songs. | — |
| [Requiem and dies irae (choral-orchestral lament)](./sound/requiem-dies-irae-choral.md) `requiem-dies-irae-choral` | A Latin or English mass for the dead scored for choir and orchestra, from soft consolation to apocalyptic brass and drum. | — |
| [Colliery and silver brass band](./sound/colliery-brass-band-classical.md) `colliery-brass-band-classical` | All-brass ensemble with cornets, euphoniums and basses playing hymns, marches and test pieces: the sound of the northern working-class town. | — |

*Not yet written up:* Gregorian chant and plainchant: a single unaccompanied line, strong for ritual and a future-cult register, but narrower than the entries chosen.; Neoclassical/ambient piano and strings (post-classical): popular as underscore but overlapping with minimalism and string quartet.; Early music and Renaissance consort (viol, lute, madrigal): distinct and usable for satire of the court, but near baroque.; Choral-orchestral spectacle (Carmina Burana, O Fortuna type): a hybrid of choir and late-romantic orchestra, heavily used by trailers.; Tragic verismo opera: sung grief and betrayal, partly covered by the requiem and comic-opera entries.; Modernist and avant-garde (Ligeti, Xenakis, Penderecki clusters): strong for dread, but inaccessible to the target audience.; Fanfare and military band: a close cousin of the brass band, more official in tone.; Film orchestral hybrid: cinematic orchestra plus electronics, which belongs in a film-score family rather than this one..

### Stage and screen music

These are styles built to serve a scene, a character or an audience in a room, so they carry plot, attitude and theatrical irony more readily than a pop song does. They split into two camps. Voice-led forms (cabaret, patter, music hall, book-musical, workers' chorus) put the words first and suit argument. Score-led forms (western, spy, suspense) put atmosphere first and suit narration beds and underscore. None of this is verified by live search; engine notes are working knowledge of how Suno responds to descriptive prompts and should be tested with the variations skill.

| Style | In one line | Used by |
| --- | --- | --- |
| [Weimar cabaret and Brecht-Weill](./sound/weimar-cabaret-brecht-weill.md) `weimar-cabaret-brecht-weill` | A sneering, half-spoken song with a wheezy small band, built to make an audience laugh and then feel implicated. | — |
| [Gilbert and Sullivan patter song](./sound/gilbert-sullivan-patter.md) `gilbert-sullivan-patter` | A fast, crisp comic list-song in Victorian operetta style where the words are the punchline. | — |
| [British music hall and pantomime](./sound/music-hall-and-pantomime.md) `music-hall-and-pantomime` | A bawdy, singalong, working-class pub-and-theatre song in thumping 2/4 or waltz time, with a chorus the whole room joins. | — |
| [Spaghetti western score](./sound/spaghetti-western-score.md) `spaghetti-western-score` | A sparse, echoing, theatrical Italian western sound of twanging guitar, whistling, choir and sudden gunshot percussion. | — |
| [1960s spy score](./sound/sixties-spy-score.md) `sixties-spy-score` | A swaggering, cool, brassy spy theme of twangy baritone guitar, big brass stings, swinging bass and sinister strings. | — |
| [Suspense orchestral score](./sound/hitchcock-suspense-orchestral.md) `hitchcock-suspense-orchestral` | A tight, strings-led thriller score of stabbing violins, repeating motifs and slowly rising dread. | — |
| [Satirical book musical (Broadway and West End)](./sound/satirical-book-musical.md) `satirical-book-musical` | A big-voiced theatre number with piano and pit band, where a character explains their scheme in song and the chorus joins the joke. | — |
| [Agitprop workers' chorus and march song](./sound/agitprop-workers-chorus.md) `agitprop-workers-chorus` | A plain, hard-driving mass song or ballad for a crowd, written to be sung on a picket line and heard as a call to act. | — |

*Not yet written up:* Pantomime proper (dame, villain boo, audience call-and-response) folded into the music hall entry rather than given its own; Disney and animated-musical ballad style: usually too warm and sentimental for this brief; Silent-film cinema organ and silent-comedy piano accompaniment; Ealing comedy and British post-war light orchestral score (brass band and strings with jaunty clarinet); Kitchen-sink and 1970s British TV drama library music and Radiophonic Workshop electronic cues; Gothic Hammer horror orchestral score; Blaxploitation and 1970s funk film soundtrack; Opera buffa and Rossini-style comic opera patter (close relative of Gilbert and Sullivan).

### Black American roots

These styles share one engine: a song is a way for people with no power to say a hard thing out loud together, using call-and-response, a blue-note vocabulary and rhythm that carries the message when the words are not safe. That makes the family the most natural fit BadCode has for songs about work, debt and who owns what, and also the one where a careless imitation reads as costume. The family ranges from solo and unaccompanied (field recordings, delta blues) to huge ensembles (big band, mass choir), so it covers almost every scale of story. No reference below was searched during this run; all are works I am confident exist, and the Suno behaviour notes are described tendencies, not tested results.

| Style | In one line | Used by |
| --- | --- | --- |
| [Pre-war delta blues](./sound/delta-blues.md) `delta-blues` | One voice and one acoustic guitar, bottleneck slide or hard-stomped rhythm, singing a short repeated line about money, work and trouble. | — |
| [Work song and field holler](./sound/prison-work-song.md) `prison-work-song` | Unaccompanied men's voices chanting in time to an axe, a hoe or a hammer, with a leader calling and the gang answering. | — |
| [Gospel quartet and mass choir](./sound/gospel-quartet-and-mass-choir.md) `gospel-quartet-and-mass-choir` | Black church music: tight male quartets with a shouting lead, or a big choir with a piano and organ, building a sung statement into a roof-lifting refrain. | — |
| [Civil-rights freedom song](./sound/freedom-song.md) `freedom-song` | A congregational protest song in which an old hymn or spiritual gets new words about the fight at hand, sung by a group in unison with a simple leader-and-chorus structure. | — |
| [Big-band swing and jump blues](./sound/big-band-swing.md) `big-band-swing` | A fourteen-to-eighteen-piece dance band of brass, saxes and rhythm section playing riffs and call-and-response between sections, with a swinging four-beat bar. | — |
| [Motown pop-soul](./sound/motown-soul-pop.md) `motown-soul-pop` | A tight 1960s hit-factory sound: tambourine backbeat, melodic bass, strings and horns, and a lead singer with gospel-trained vocals and call-and-response backing singers. | — |
| [Hard funk](./sound/funk.md) `funk` | A locked, repetitive groove built on the first beat of the bar, with choppy guitar, slapped bass and a rhythm section that does the arguing. | — |
| [Jazz poetry and spoken-word groove](./sound/jazz-poetry-spoken-word.md) `jazz-poetry-spoken-word` | A deadpan speaking voice delivering sharp political verse over congas, a simple bass and loose jazz or soul instrumentation, halfway between a poem and a song. | — |

*Not yet written up:* Bebop and hard bop small-combo jazz: fast, complex, and mostly instrumental, so less useful for story songs.; Deep Southern soul (Stax and Muscle Shoals): raw, horn-led and emotional; close to Motown but grittier.; Chicago electric blues: amplified, band-driven, urban; a sibling of delta blues.; Doo-wop and street-corner vocal groups: close harmony and nonsense syllables, good for comic choruses.; Ragtime and early New Orleans jazz: lively and ironic but dated for most stories.; Spirituals and sorrow songs in concert-arrangement form (as sung by university choirs).; Early hip-hop and boom-bap: Black American but a separate family of its own..

### Global traditions with UK roots or reach

These are the sounds that arrived in Britain on boats, planes and sound systems and were remade here, mostly by working-class kids in Coventry, Handsworth, Brixton, Southall and Birmingham. Most of them were already political or communal music before they reached a studio, so they carry a stance as well as a groove, and a story that borrows one inherits that stance. I did not run any web searches. Every reference below is from memory and I am confident each exists, but some release years are approximate and flagged as such.

| Style | In one line | Used by |
| --- | --- | --- |
| [2-Tone ska](./sound/two-tone-ska.md) `two-tone-ska` | Fast, skanking, minor-key British ska-punk hybrid from 1979-81 Coventry, with pub-band urgency and a mixed-race line-up singing about dole queues and riots. | — |
| [Roots reggae (UK)](./sound/roots-reggae.md) `roots-reggae` | Slow, heavy, one-drop reggae with Rastafari-inflected protest lyrics, as remade by British-born Caribbean bands in the 1970s. | — |
| [Dub](./sound/dub.md) `dub` | A reggae track stripped to drums and bass and then played through the mixing desk with echo, reverb and drop-outs as the lead instrument. | — |
| [Lovers rock](./sound/lovers-rock.md) `lovers-rock` | Smooth, sweet, romantic British reggae sung largely by young black women, born in 1970s South London. | — |
| [Dub poetry](./sound/dub-poetry-global.md) `dub-poetry-global` | Spoken-word verse delivered in Caribbean-inflected English rhythm over a dub or reggae bass line, used for protest and reportage. | — |
| [UK bhangra](./sound/uk-bhangra.md) `uk-bhangra` | Dhol-driven Punjabi folk-dance music remade in 1980s-90s British Asian wedding halls and clubs with synths, drum machines and English-language crossover. | — |
| [Afrobeat](./sound/afrobeat.md) `afrobeat` | Long, polyrhythmic Nigerian groove music with call-and-response, big horns and furious political lyrics, with a London chapter. | — |
| [Calypso (kaiso)](./sound/calypso-kaiso.md) `calypso-kaiso` | Trinidadian topical satire song with a lilting rhythm and a comic, sly lyric, brought to London by Windrush-generation singers. | — |

*Not yet written up:* Klezmer: Jewish diaspora wedding music with a small British scene; distinctive clarinet-led sound, but weaker UK-working-class connection than the entries chosen.; Fado: Portuguese melancholy song with some UK diaspora reach; very distinct, but the 'saudade' register is narrow and has no UK-rooted political tradition.; Highlife: West African dance-band music that fed British Afrobeat and the 1950s London scene; overlaps heavily with the afrobeat entry.; Cumbia: Colombian cumbia has a London scene (and Latin-American migrant communities) but its UK roots are thinner than the entries here.; Irish rebel ballad and ceili: strong UK working-class reach, probably belongs in a British folk family instead.; Jungle, drum and bass and UK garage: British-born Caribbean-diaspora sounds, probably belong in an electronic family.; Gospel and Black British church choir music: strong UK roots and a collective voice, but better covered in a vocal/choral family.; Qawwali and Bollywood film song in the UK: widespread British Asian reach, but long-form devotional qawwali is a poor fit for satire.; Soca: the fast carnival descendant of calypso, left out because it overlaps with the calypso entry in how Suno handles it..

### Novelty, found sound and the margins

These are the forms where the sound itself carries a social meaning before a single lyric lands: the shop jingle, the playground rhyme, the terrace roar, the safety film, the library cue. Most of them are things a UK working-class listener has heard thousands of times without ever choosing to, which makes them strong vehicles for political satire (familiar form, hostile content) and weak vehicles for sincerity unless that gap is the point. What joins them is that they are functional or collective music: made to sell, to teach, to scare, to be shouted, or to sit under something else. That is also where Suno is weakest, because it is trained toward finished, polished, single-voice songs.

| Style | In one line | Used by |
| --- | --- | --- |
| [British comedy novelty song](./sound/british-comedy-novelty-song.md) `british-comedy-novelty-song` | A fast, story-driven comic song in music-hall, skiffle or brass-band clothes, performed with a straight face and a regional accent. | — |
| [Advertising jingle and sung slogan](./sound/advertising-jingle.md) `advertising-jingle` | A 15-30 second earworm built around a brand-style slogan, sung bright and sold hard. | — |
| [Nursery rhyme and playground chant](./sound/playground-rhyme-nursery-song.md) `playground-rhyme-nursery-song` | A sing-song children's rhyme with a tiny melody, hand-clap rhythm and a lyric that turns out to be about something nasty. | — |
| [Football terrace chant and stadium anthem](./sound/football-terrace-chant.md) `football-terrace-chant` | A massed, stomping, shouted singalong built on a borrowed tune, with a lyric you could bellow in a pub after a defeat. | — |
| [Library music and broadcast cue](./sound/library-music-cue.md) `library-music-cue` | Instrumental production music of the KPM and BBC-era kind, made to sit under pictures, with named moods like 'Industrial Progress' or 'Tension'. | — |
| [Musique concrete and sound collage](./sound/musique-concrete-sound-collage.md) `musique-concrete-sound-collage` | Music assembled from recorded real-world sound (voices, machines, radio, tape) cut, looped and layered into a montage. | — |
| [Public information film soundtrack](./sound/public-information-film-score.md) `public-information-film-score` | The sparse, eerie or jaunty music of 1970s British warning films, where a friendly voice tells you how you will die. | — |
| [Music box and toy instrument score](./sound/toy-instrument-music-box.md) `toy-instrument-music-box` | A tinkling score of music box, toy piano, celesta and glockenspiel, nursery-sweet and slightly wrong. | — |

*Not yet written up:* Ska and 2-tone novelty (Specials-type political pop) - belongs more with protest pop than novelty; Spoken-word with drone (poetry-over-bed) - closer to narration scoring than a margin style; Radiophonic Workshop synth cues as a distinct style from musique concrete (Derbyshire, Oram, Hodgson); Hymn and church-parody (hymn tunes with new words) - covered partly by the terrace chant; Sea shanty and work song - folk family; Hold music, elevator and lift music (muzak) - strong satirical candidate for corporate dread; Radio ident and station-jingle pastiche; Bedroom lo-fi tape-hiss/cassette-recording aesthetic as a found-sound medium.
