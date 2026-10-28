lets experiment with better deep english voices that sound like real singers and blend them all, keep kais lyrics, try and listen to the best one, analsye the prompt, make sure to not fall into the traps the repo and the skills that make the same song over and over with basically the same prompts, so do a bunch of experimental basic clean room ones, then we will pick a winner and iterate. do not make these mistakes "

  Problems we found → how to fix them

  🔴 1. The repo's Suno rules make the same voice every time
  - More than 325 takes written with the house rules came out as one voice.
  - Fix: use the "clean room". A helper that hasn't read the repo writes the prompts from a plain brief, and they run exactly as written.

  🔴 2. The "clean room" helpers weren't really clean
  - Rounds CR to GG were run by helpers inside the repo, and those load CLAUDE.md and memory automatically. Telling them to ignore it doesn't work.
  - Fix: write prompts only with scripts/suno/sealed-writer.sh. It runs a separate Claude in an empty folder, with web access and nothing else.

  🔴 3. All six prompts shared one music paragraph, and only the voice line changed
  - This gave identical voices in VB, SR1 and the first SR2 draft.
  - Fix: scripts/suno/sameness.py checks the round first. A failed check means the round goes back to the writer. I overrode it in SR1, and that was wrong.

  🔴 4. The brief leaked old material from the repo
  - SR1's brief carried my old listen notes and the old stored prompt.
  - Fix: the brief holds only your words exactly as you wrote them, the facts of the last verdict, one fresh listen and the lyric words.

  🟡 5. Moving a liked voice onto another prompt turned it American (Round BO)
  - The Englishness came from the whole liked prompt, not from the voice sentence.
  - Fix: don't splice voice lines between prompts. Change the type of performer, not just the accent. Swapping only the accent still gives the same singer.

  🟡 6. Suno's text for "Best one" doesn't match how it sounds
  - The box said psych folk and sitar. It actually sounds like acoustic flamenco-style guitar over a hip-hop beat, at about 93 BPM.
  - Fix: describe the song from a listen, not from its own prompt.

  🟡 7. Variety Normal rewrites the Style box
  - The music on ed6dd946 came from Suno's rewritten prompt, not ours.
  - Fix: keep Variety Off, and build from the take's stored tags.
" and any of the other mistakes previously mentioned, where we make the same prompt becuase of the repo, this prevents creativity and variety which is exactly the goal, maybe change stuff in the skills and repo, to make sure this never happens again, i do not want the same mistakes made over and over, i cannot emphasise this enough. THanks very much.
