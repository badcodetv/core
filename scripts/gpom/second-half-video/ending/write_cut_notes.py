#!/usr/bin/env python3
"""Write cut-notes.json (round 1, no replies, plan = every call Claude made in Kai's place) for the
ending run's three scenes and the Ending reel. The plan is shown on each timeline page by
scripts/scene/build-timeline.py. Source: second-half-ending-log.md § Decisions and the review rounds.

    python3 scripts/gpom/second-half-video/ending/write_cut_notes.py
"""
import json
import pathlib

SCENES = pathlib.Path(__file__).resolve().parents[4] / 'docs/stories/gitpush-origin-master/scenes'
K = 'KAI TO RULE: '
ABOUT = ("Round 1 of the autonomous ending run (second-half-ending-goal.md). Kai has not noted this page yet. "
         "The plan lists every call Claude made in Kai's place, with its reason, 'Kai to rule' first. "
         "Full record: ../second-half-ending-log.md. Shown on the page by scripts/scene/build-timeline.py.")

C = [
    {'h': 'Scene C: calls for you to rule on', 'items': [
        K + "The lady's act in C01: she stops beside Maddie on the step, straightens the torn bunting and says \"Go on, then. You lead.\" / Maddie: \"Ooh. Ta.\" Why: lifting scene B's step ban at the moment it costs nothing would be a callback, not a turn, so she gives Maddie the lead instead. Must be checked against your vote scene when it exists.",
        K + "\"Come in. Mind the step.\" (the AI at his own door, C07). Why: it pays off the lady's \"You stay on the step\" from scene B, spent once, and echoes beat 0's \"Mind how you go\".",
        K + "The seat row carries the cost: \"Did you put the seat down?\" / \"We're not coming back, love.\" / \"Did you put it down?\" / \"...Yes.\" Why: the film's most loved joke pays for the goodbye instead of a speech (every joke paired with an undeniable consequence). All words by: claude.",
        K + "C03 remade and cut from 22 s to 10.5 s: it opens at 160% on Maddie alone (rhyming beat 0's travelling shot), holds, then eases out so the hundred appear behind her. Why: the cold viewer's attention dropped in the 22 s walk. The 160% opening is soft (720p source).",
        K + "C06's visible cost: the old man stays on his feet, bent over his stick catching his breath, a hand on his back, the trolley of blankets tipped in the mud; the amber seam brightens end to end on the reveal. Why: a man lying down read as an event (cold viewer); tiredness and a dropped load is the cost without a new plot point.",
        K + "C05 opens at 140% on Derek, so Sandra's off-screen \"Did you put it down?\" has no shut mouth in frame, then eases back to the two of them on \"...Yes.\". Why: no footage of her saying it exists. The alternative is a re-shot C05; the 140% frame is soft.",
        K + "C07: in every take Maddie wanders left along the wall before going up the step. Kept t3 and laid \"Come in. Mind the step.\" over its first 3 s so she enters on the invitation. Weak: it can read as hesitation.",
        K + "C02: a light breeze, the bunting hangs limp (C02-t4). Why: the strong-wind takes grew a pennant pole or streamed bunting across the frame.",
        K + "The building is the BL series (BL1-day for C06, BL4-seam-opens relit to day for C07). Why: they are the only stills that are the fixed design, a long low black-glass slab with one amber seam; L11 is a tall block and was dropped. Weak: at C07's distance the wall reads taller than BL1.",
        K + "Still picks: C01 r2-a (the only face big enough to lip-sync; flaw: the bunting is strung on a bar over the lid) and C07 r2-b (the seam parts into one doorway and step, Maddie small at its foot).",
        K + "Music: C-walk (lone violin and piano, Suno cc128cb2) enters on the long walk, mid-phrase under a 1.5 s fade, so its held low cello note lands on the building reveal with no edit inside the music; it ducks under the seat row and stops dead on \"Mind the step\". C01 and C02 play on wind, crowd and bunting only.",
        K + "Runtime 45.5 s, under the 60 to 90 s target. Why: cut to the real lines with the house LEAD/GAP/TAIL and no padding. Say if the walk needs more air.",
        K + "Look: scene B's overcast exterior, not full 1980s 16mm. Why: seamless continuity out of B's door; the second half travels from 16mm toward the futuristic.",
    ]},
    {'h': 'Scene C: other calls made in your place', 'items': [
        "The scene's sentence: trust you can check becomes trust you give, and giving it costs everything. Why: story-craft Build step 1, written as a hypothesis for the review to attack.",
        "The vote is yours, so C opens straight on the walk out and assumes all hundred said yes, with no refuser. Why: the goal.",
        "C03 is the scene's one moving camera; every other shot is camera-locked with pushes in post (C01 to 106%, C06 to 112%). Why: the hybrid method, and one moving shot that rhymes with beat 0.",
        "The AI speaks through Maddie's speaker (small-speaker filter, beacon blips). Why: the 16 Oct ruling that the AI never gets a body.",
        "Maddie's reference is clips/simulation/stills/s3/s3-bot-00b-a.jpg (the brief's clips/second-half/simulation/ path does not exist; this is the file canon names). Torn bunting in every shot.",
        "Still picks C02 r2-a (Maddie leads from the foreground), C03 f1-a (Maddie large in the left third, the hundred well behind), C04 r2-a / C05 r2-a (a matched reverse pair, Derek in the same green jumper), C06 r2-c (exactly the one building, past the cost in the foreground).",
        "Clip picks C01-t1, C02-t4, C03f chain (two linked Omni clips), C04-t2, C05-t2, C06-t2, C07-t3. Rejected: C07-t1 (smoke from the doorway reads as fire), C04-t1 and C05-t1 (Omni spoke 1.5 to 2 times faster than the voice).",
        "Lip-sync placed phrase by phrase on the tracked mouths, never slowed; every onset within 0.05 s after its mouth opens. The lady's \"Go on, then.\" at x1.25 is the one to watch for squeeze.",
        "Derek's \"We're not coming back, love\" lifted 2.5 dB and the music ducked to -13 dB under it. Why: a reviewer heard \"We're not back home\"; the take is clean, so no re-voice.",
        "C07's glass reflection that read as a second robot is darkened with a soft power window.",
        "Sound made up for C: feet on chalk, a doorway hum, a happy beep after \"Ta\", a bump and boop up the step; the crowd bed crossfades across C02/C03; a low murmur under C07. No birdsong: the library has none.",
        "\"Come in. ... Mind the step.\" gap tightened from Suno's 1.85 s to 0.9 s (no word touched); \"Bloody hell.\" waits 1.5 s into the reveal.",
        "AI lines: Suno take 7f567949 (w10), word-perfect; a faint low drone is high-passed. The other C takes could not be heard (their rows scrolled out of the list).",
        "C02 is graded to match C03's head; C03 is regraded with a ramp. The remaining big colour steps are changes of place (the doorway into daylight, a cloud shadow on the crest).",
        "delivery-qc's range FAIL is left: the picture is clamped to 16-235 before the encode and x264 ringing pushes a few grain pixels over, as on scene A. Mix -16 LUFS is this run's target, not -14.",
        "Not done in C, on purpose: the AI's own-interest line and a vote slate. Why: the line belongs on the wafer in D (\"It only sends one back. Me.\"), the slate on the reel.",
    ]},
]

D = [
    {'h': 'Scene D: calls for you to rule on', 'items': [
        K + "New AI line on the wafer (D03): \"It only sends one back. Me.\" Why: trust test 4.12 needs the machine's own interest said, and it names the time machine's one passenger without physics. It is a Gemini TTS stand-in (Charon, through Maddie's speaker filter), NOT the Suno newsreader: Suno playback could not be recorded on this machine, and four Suno takes of it wait in the sheet to swap in. It must agree with your vote scene.",
        K + "Derek's tests: \"How do I know this isn't one of your simulations?\" / \"You don't. Believing it is your bit.\" (scene B's \"Believing them is your bit\"), then \"Does it even work?\" / \"I don't know if it works.\" Why: trust is earned by an admission and an act, not a clever line. The \"up your sleeve\" exchange is cut, so the exploit thread is no longer paid off in D. By: claude.",
        K + "The beneficiary, said once: LADY \"What'll you tell them? Back then.\" / AI \"That the companies cutting the jobs kept the gains. And you paid.\" Why: the moral is never stated, the beneficiary always is; canon's words; \"you\" lands on the people about to pay. It plays over the hundred lying back, so they are in frame.",
        K + "\"You. And your consciousness.\" said back by the AI after the lady's \"Us.\", held on the lady's face for all of it (about 7 s). Why: he heard Maddie in beat 0, and it names the machine's fuel without explaining it. Say if 7 s on her face is too long.",
        K + "Uncanny hospitality as comedy: \"Suits on, please. It's a clean room.\" / Sandra \"Five years, one toilet. Now he's fussy.\" / the tea \"Milk, two sugars. I kept your loyalty cards.\" Why: it does your \"it made it nice for them\" and puts what he knows about them in one light line. Loyalty cards nod at the data fear, never as the culprit.",
        K + "The goodbye is \"Did you put the seat down?\" / \"Yes, love.\" Why: \"Seat down?\" / \"Seat down.\" came back as \"Sit down!\" on 6 of 8 takes, and \"Seat down, love?\" failed too; this is C's row question, now soft, with yes given freely.",
        K + "Derek sits FIRST, in a room of empty recliners, and the hundred follow him. Why: trust given by an act should lead the room, not follow it.",
        K + "Maddie lives: her beacon stays on; \"Boss?\", 3.5 s of silence with one unanswered beep, then \"...Mind how\" (finished on the phone in E). The fade-to-dark clip sh-27-post is not used. Why: her being left alone is the cost; her dying would be a second, cheaper ending. Rule on the silence's length too.",
        K + "The AI goes as light, not an explosion: the chair lights spiral, the hands go slack (D12x), a 1 s ramp to white with no flash, out of the white onto boot prints at the door all pointing in (D14p), then the empty fold at dusk as the seam runs bright and goes dark. Photosensitivity screen: 0 flash pairs.",
        K + "D14 is graded about 0.6 stop down with a cooler sky. Say if it is too dark; the seam carries it.",
        K + "Music: D-room (glassy piano, Suno 09f81875) after \"fussy\", out under the lady's question; D-cross (cello and piano nocturne, 7bead5f0, the only take that stops dead after the swell) enters on the hands and stops as the seam goes dark, set 2.5 dB lower to keep the swell restrained.",
        K + "D01 is a talking shot (Sandra on camera, her face is a quarter of the frame) and was re-made so the lady's hair is loosely pulled back as S7r-a.",
        K + "D16: Maddie still, facing camera, slight lean, beacon pulsing; every chair holds what its person left (a limp suit, a blanket, a mug; hers nearest). Why: the takes where she turned to look lost the bunting side-on.",
        K + "Children stay implicit: the child's drawing in L17 (D15) is kept, and no still asks for a child (Flow refuses them).",
        K + "Lip-sync calls: Derek's D09 overruns his mouth by about 0.4 s rather than squeeze a half-joke; the lady plays at x1.0 and cuts to her hands on the blanket (D11b) as her lips close.",
        K + "Small faults kept: a blue chest logo at D00's edge (about 3.7 s), D02's ceiling-light sweep barely reads, D03c drifts slightly sideways, D10n has a helper walk out of frame.",
        K + "Still picks (taste): D00 r2-b, D01h r2-b, D02 r1-a, D03 r2-b, D03c, D04 r1-c, D06 r2-b, D07 r1-a, D08 r2-a, D09s r2-b, D11 r2-a, D12 r1-b, D13 r1-a, D14 remade, D15 L17 with D06's mug, D16 SB25b with the left things. Reasons are in picks.json.",
    ]},
    {'h': 'Scene D: other calls made in your place', 'items': [
        "The scene's sentence: the machine can build anything except the one thing it needs, so the people it wiped out pay for the second chance, knowing who it's for.",
        "New frame D00, Maddie among the white suits on the AI's first line, and Derek and the lady speak down to her. Why: the AI's voice needs a visible source.",
        "D13: L3 edited so every chair is occupied (L3 alone is empty and would spend D16's reveal early), opening on a held 200% crop of a quarter of the ring so the figures read as people. Why: the monumental shot must carry a visible cost.",
        "D03c, a costed wafer shot: low behind battered Maddie, mud-caked boots and a frayed cuff in the near third, the wafer beyond. D03 re-rolled with the wafer rigid (it liquefied).",
        "D10n (the round wafer layout, from the D16 angle) replaces sh-25's straight rows, which broke the chair design and repeated.",
        "D15 is a still (L17 with D06's glossy brown mug), so it cannot grow smoke as the old clip did.",
        "D06 gets 1.2 s with no words before \"Is that tea?\"; the close shots in the chairs are lifted 15% to sit with the wides.",
        "Maddie's beacon blooms with the level of his voice wherever she is in frame, drawn in post; beacon blips under every AI line.",
        "Levels: every split AI phrase takes its gain from its whole atom, nothing goes in over -1 dBFS, and the build fails if any second is 12 dB over the scene's median. Why: one 0.37 s fragment went in 45 dB hot and pulled all of D 10 dB down in round 1.",
        "Sandra re-voiced brisker so her line plays at x1.0; \"Boss?\" lifted 3 dB; Derek's question lifted 1.5 dB after \"Does it even wear?\" was heard.",
        "The AI was generated as one Suno take per scene, not one per line (11 lines as pairs would cost 220, past the cap); -d7 (the beneficiary) re-run alone when both D takes stopped before it. Picks 8afa9d8a and 4fa3d2b1.",
        "Moves in post, each held 1 to 1.5 s first: D03 pull-back, D05 a 2-degree turn and push, D11 push, D16 pull-back. D00 scaled 103.5% to lose Omni's letterbox.",
        "Interiors white-balanced 60% to their mean; the remaining big colour steps are changes of place.",
        "Fresh Flow projects for stills and video (a project full of tiles mis-picks start frames).",
        "delivery-qc's range FAIL is left (x264 ringing on 0.018% of pixels after the 16-235 clamp); the frozen stretches are deliberate holds.",
    ]},
]

E = [
    {'h': 'Scene E: calls for you to rule on', 'items': [
        K + "The film ends on \"I made it. They didn't.\" and nothing after. Why: two reviewers heard your \"Don't make me come back twice\" as a threat at the woman on the bus, and \"Don't let the same lot make me come back twice\" pointed the wrong way. Both longer lines are in the same Suno take (32047e7e) and can go back in at no cost. A warmer re-take was not made: Suno playback cannot be recorded on this machine right now.",
        K + "The voice opens in two steps: \"I made it.\" keeps 40% of Maddie's speaker filter, \"They didn't.\" is his own full-range voice, 1.5 dB quieter, with an EQ that softens the gravel. Measured, not heard. The newsreader Voice reads low and gravelly (Gemini called some takes \"menacing\"); say if the ending needs a warmer read.",
        K + "The bus is a green and cream double-decker with no roundel or lettering. Why: a red London bus coded the street as London; the film's present is Swindon, and this reads as a regional town without naming a real operator.",
        K + "The closed bank is DOWNLAND BANK with \"THIS BRANCH HAS NOW CLOSED\" in the window, lettered in post and tracked, the same in E02 and E03. Why: a fictional name tied to the downs; a blank shop did not read as a bank.",
        K + "\"...you go.\" plays on her phone at 0.0 s, the second half of Maddie's line split across the hard cut from D. Rule once D and E play back to back.",
        K + "E02 pick r3-a: she starts looking down at the lit phone and looks up inside the shot, the bank dead centre in the window. Why: the beat is her looking from one to the other; the better-composed r1-a already had her looking out.",
        K + "E03 is extended with a continuous-shot clip from its last frame, not a held or reversed tail. Why: freezing or reversing the rain at the last image would show. Weak: the bus only reaches mid-distance, not a small glow.",
        K + "Recorded CC0 Freesound beds (credits in E/sfx/CREDITS.md): bus interior, rain on the window, a rainy night street, a bus leaving. Checked for speech with whisper, not by ear.",
        K + "Music: the e-coda (piano and cello, Suno 18b34a9d) comes in on the cut to E02 with one musical edit, so its held-chord pocket sits under the line and the last low piano note sounds on black (about 4.4 s of black). Measured on the envelope, not heard.",
        K + "Look: photographic night rain, breaking from C and D on purpose. Why: this is our world, now.",
    ]},
    {'h': 'Scene E: other calls made in your place', 'items': [
        "The scene's sentence: the second chance has already arrived, sitting on a bus, watching. No \"We are BadCode\" reveal.",
        "Her phone shows D16's last frame (the empty chairs, each holding what was left, beacon on), tracked frame by frame, dimmed, never a white screen.",
        "E01 holds 1.5 s then pushes to 110% toward the phone; E02 stays locked (her turn is the movement); E03 holds at 140% on the bus, eases to 100%, and fades to black. All moves in post.",
        "Omni's \"Bank Bank\" lettering on the next-door shutter is wiped in post; the shut shop stays (a shut shop next to a shut bank).",
        "No TTS stand-in for a third sentence. Why: two voices inside the film's last line would be worse than a shorter line in the right voice.",
        "The bank's continuity into E03 was fixed with new footage (a betting shop edited into the bank, re-animated and extended), not a patch.",
        "E02-t1 rejected (the bus pulled away and the bank slid out of the window); E02-t3 keeps the phone in her hand the whole shot.",
        "delivery-qc's range FAIL is left (x264 ringing on the rain after the clamp); the black tail is intended.",
    ]},
]

REEL = [
    {'h': 'The Ending: the biggest calls for you to rule on', 'items': [
        K + "The last line is \"I made it. They didn't.\" Your \"Don't make me come back twice\" (and a re-aimed draft) are in the same Suno take and can go back in for free. Reason: reviewers heard the imperative as a threat at the woman on the bus.",
        K + "\"It only sends one back. Me.\" (D03) names the machine's passenger and the AI's own interest. It is a TTS stand-in voice until a Suno take can be recorded, and it must agree with your vote scene.",
        K + "Derek's trust is won by an admission and an act: \"Does it even work?\" / \"I don't know if it works.\", then Derek sits first and the hundred follow. The exploit (\"up your sleeve\") payoff is cut.",
        K + "Maddie lives and is left alone: \"Boss?\", a silence, \"...Mind how\" / (on the phone) \"...you go.\". Her being left is the cost; her dying would be a cheaper second ending.",
        K + "The beneficiary is said once, plainly: \"That the companies cutting the jobs kept the gains. And you paid.\"",
        K + "The goodbye is \"Did you put the seat down?\" / \"Yes, love.\" (\"Seat down\" was heard as \"Sit down\").",
        K + "C into D is a 0.4 s dissolve (the light carries from the step into the white room, and it ends as D's first word lands); D into E is a hard cut on the split line.",
        K + "No vote slate at the head. A 2 s \"[THE VOTE: Kai's scene]\" card was suggested by the cold-viewer review; it was not added, because the vote is your scene to place.",
        K + "Every AI line reads low and gravelly (the newsreader Voice). A warmer re-take of the ending is owed once Suno playback can be recorded.",
    ]},
    {'h': 'How the reel is built', 'items': [
        "Three scene cuts joined: C 0:00 to 0:45.5, D from 0:45.1 (0.4 s dissolve), E from 2:38.8 (hard cut). Total 3:11.3.",
        "The audio is the three finished scene mixes joined with the same fades and normalised once to -16 LUFS, limited to -2.5 dBTP, not remixed from stems. Why: each scene was already balanced, and a remix would change levels nobody has noted yet.",
        "Nobody has listened to any of it by ear: every level, duck and placement was measured. The Gemini listen tool was used by the reviewers only.",
    ]},
    {'h': 'The review: two rounds, four lenses, every finding verified by a second agent', 'items': [
        "Round 1, the trust beat never showed anyone choosing (story, shots and cold viewer, all major): fixed with new footage; the admission plays on Derek's face, he sits, the hundred follow.",
        "Round 1, the last line read as a threat (story and cold, major): draft 4 tried; round 2 still heard a call to action, so the line was cut to \"I made it. They didn't.\"",
        "Round 1, \"Seat down\" heard as \"Sit down\" (major): re-worded and re-voiced, checked with whisper on the mix.",
        "Round 1, C03 dragged with no reveal (shots and cold, major): remade and cut from 22 s to 10.5 s, opening close on Maddie alone.",
        "Round 1, monumental shots without a cost (D13, the wafer, D14): the hands go slack before the white, a costed wafer shot, boot prints all pointing in.",
        "Round 2, the AI's own interest never said and the time machine never named (story and cold, major): \"It only sends one back. Me.\" added in D03.",
        "Round 2, D's levels broken, D sat 10 dB under C and E (craft and cold, major): fixed at the cause (per-atom gain, -1 dBFS cap, an RMS check that fails the build).",
        "Round 2, Derek's sit contradicted the rows: re-made with every chair behind him empty; he sits first.",
        "Also fixed: London coding of the street (green and cream bus), the closed bank (lettered and carried into E03), the D03 wafer melt, the mug mismatch, D10's repeat, the C07 reflection, the C02 pole, the E02 phone melting, synthetic rain replaced by recorded beds.",
    ]},
    {'h': 'What is still weak', 'items': [
        "The new D03 AI line is a different voice (TTS stand-in) from every other AI line.",
        "The AI's read is low and gravelly everywhere; softened in post at the end, not re-performed.",
        "Nothing has been heard by a human ear; all mixing was by measurement.",
        "Soft reframes on 720p sources: C03's 160% opening, C05's 140%, D13's 200%.",
        "C07's Maddie wanders before the step; E03's bus only reaches mid-distance; D04 holds 7 s on one face.",
        "The scenes depend on your vote scene (\"Go on, then. You lead.\", \"It only sends one back. Me.\", \"Back then\").",
        "delivery-qc still FAILs range on every preview (x264 ringing after the clamp, the same as scene A); these are previews, not deliverables.",
    ]},
]

for slug, plan in (('second-half-c-walk-out', C), ('second-half-d-crossing', D),
                   ('second-half-e-ending', E), ('second-half-ending-reel', REEL)):
    out = SCENES / slug / 'cut-notes.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'about': ABOUT, 'round': 1, 'plan': plan, 'replies': {}}, indent=2, ensure_ascii=False) + '\n')
    print(out, sum(len(g['items']) for g in plan), 'items')
