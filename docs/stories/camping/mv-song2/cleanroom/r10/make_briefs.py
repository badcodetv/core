"""Round-10 sealed briefs: Jack's words + plain facts + fresh web research + one task + the output format."""
from pathlib import Path
H = Path(__file__).parent
FMT = """
# Output format (exactly this, nothing else in the file)

For every shot, in order:

=== SHOT <id> ===
REFS: <file names, comma separated, or none>
STILL:
<the still prompt, ending with the line Thanks.>
CLIP:
<the 8-second motion prompt for that still, ending with the line Thanks.>
"""
JOBS = {'st': ('task-stadium.md', ['research-stadium.md']),
        'du': ('task-duo.md', ['research-faceoff.md']),
        're': ('task-real.md', ['research-faceoff.md']),
        'ly': ('task-lyric.md', ['research-stadium.md', 'research-faceoff.md'])}
for w, (task, res) in JOBS.items():
    parts = [(H / 'jack.md').read_text(), (H / 'facts.md').read_text()]
    parts += ['# Research (fresh, from the web; use what helps)\n\n' + (H / r).read_text() for r in res]
    parts += [(H / task).read_text(), FMT]
    (H / f'brief-{w}.md').write_text('\n\n---\n\n'.join(parts))
    print(w, len('\n'.join(parts).split()), 'words')
