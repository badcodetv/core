#!/usr/bin/env python3
"""Google AI Studio TTS from the command line — the narrator, without the browser.

Grown from AI Studio's own "Get code" export (2026-09-08). Four things are fixed here that
the export gets wrong for our use, all of them found by reading it rather than running it:

  1. 🔴 The export writes ONE FILE PER STREAMED CHUNK, each with its own RIFF header. A
     paragraph of narration comes back as a dozen unplayable fragments. We concatenate the
     PCM first and write one header at the end.
  2. 🔴 The export's Transcript field contains the audio profile itself, so it reads the
     character description aloud. Here the transcript is a file you pass in.
  3. ⚠️ The export writes MONO. Premiere imported our mono Hume take, measured it correct on
     every API call, and still showed it red in the timeline. We write STEREO — same samples
     on both channels, no processing. See docs/stories/camping/narration/voice.md.
  4. The output filename was the literal placeholder ENTER_FILE_NAME_0.

🔴 LICENCE IS UNSETTLED. The free tier bills nothing, but commercial output rights are a
separate question and this film has been caught by exactly that twice (ElevenLabs, Hume).
Settle it before the take that ships.

Usage:
    export GEMINI_API_KEY=...
    python3 scripts/aistudio-tts.py script.txt out.wav
    python3 scripts/aistudio-tts.py script.txt out.wav --profile my-profile.md --voice Algenib

The default profile is "Bob, 47" — the 2026-09-08 candidate narrator. The heading shape
below is Google's own, taken verbatim from the export; it is NOT the DIRECTOR'S NOTES shape
that the docs describe, and which one performs better is untested.
"""

import argparse
import os
import struct
import sys

MODEL = "gemini-3.1-flash-tts-preview"
VOICE = "Algenib"

# Google's own export heading shape. Kept verbatim — see the module docstring.
PROFILE = """# Audio Profile
Bob, 47. Deep, gravelly, low chest tone, slightly rough from years of smoking. Restrained and inward. Intelligent, cynical, worn down. Delivery sits under the material rather than selling it. Natural conversational rhythm, short pauses, firm downward endings. Neutral southern English accent as heard in Reading or Guildford, faint London edge, no Cockney vowels or slang.

## Scene:
A small voiceover booth, late at night. No audience. He's reading from a page he half agrees with.

## Sample Context:
Bob has narrated this kind of story many times before and is no longer surprised by any of it."""


def parse_audio_mime_type(mime_type):
    """bits per sample and sample rate out of e.g. 'audio/L16;rate=24000'."""
    bits, rate = 16, 24000
    for param in mime_type.split(";"):
        param = param.strip()
        if param.lower().startswith("rate="):
            try:
                rate = int(param.split("=", 1)[1])
            except (ValueError, IndexError):
                pass
        elif param.startswith("audio/L"):
            try:
                bits = int(param.split("L", 1)[1])
            except (ValueError, IndexError):
                pass
    return bits, rate


def to_stereo(pcm, bits_per_sample):
    """Duplicate every sample to two channels. No resampling, no gain, no processing."""
    step = bits_per_sample // 8
    return b"".join(pcm[i:i + step] * 2 for i in range(0, len(pcm) - step + 1, step))


def wav(pcm, bits_per_sample, rate, channels):
    block_align = channels * bits_per_sample // 8
    return struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF", 36 + len(pcm), b"WAVE",
        b"fmt ", 16, 1, channels, rate,
        rate * block_align, block_align, bits_per_sample,
        b"data", len(pcm),
    ) + pcm


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("transcript", help="text file to read aloud")
    ap.add_argument("out", help="output .wav")
    ap.add_argument("--profile", help="file holding the audio profile (default: Bob, 47)")
    ap.add_argument("--voice", default=VOICE, help=f"prebuilt voice name (default: {VOICE})")
    ap.add_argument("--model", default=MODEL, help=f"model id (default: {MODEL})")
    ap.add_argument("--mono", action="store_true", help="write mono — Premiere may not display it")
    args = ap.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("GEMINI_API_KEY is not set")

    from google import genai
    from google.genai import types

    profile = open(args.profile).read() if args.profile else PROFILE
    transcript = open(args.transcript).read().strip()
    prompt = (
        "Read the following transcript based on the audio profile.\n\n"
        f"{profile}\n\n## Transcript:\n{transcript}"
    )

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    stream = client.models.generate_content_stream(
        model=args.model,
        contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
        config=types.GenerateContentConfig(
            temperature=1,
            response_modalities=["audio"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=args.voice)
                )
            ),
        ),
    )

    pcm, mime = bytearray(), None
    for chunk in stream:
        if not chunk.parts:
            continue
        inline = chunk.parts[0].inline_data
        if inline and inline.data:
            pcm += inline.data
            mime = mime or inline.mime_type
        elif chunk.text:
            # The model refusing, or explaining itself instead of speaking. Say so loudly.
            print(chunk.text, file=sys.stderr)

    if not pcm:
        sys.exit("no audio came back — check the text above for a refusal")

    bits, rate = parse_audio_mime_type(mime or "audio/L16;rate=24000")
    channels = 1 if args.mono else 2
    data = bytes(pcm) if args.mono else to_stereo(bytes(pcm), bits)
    with open(args.out, "wb") as f:
        f.write(wav(data, bits, rate, channels))

    seconds = len(data) / (rate * channels * bits // 8)
    print(f"{args.out} — {'mono' if args.mono else 'stereo'} · {rate} Hz · {bits}-bit · {seconds:.2f}s")


if __name__ == "__main__":
    main()
