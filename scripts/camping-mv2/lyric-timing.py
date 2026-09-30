# Build sign-text configs timed to Suno's word alignment (suno-aligned-3a433539.json).
# A segment appears LEAD s before its first word is sung (Netflix-style: picture first, voice confirms) and holds
# until the next segment. Times are converted to the SOURCE clip's clock: src = in + (t - slot_start).
import json, re, sys
LEAD = 0.08  # two frames
W = [w for w in json.load(open('suno-aligned-3a433539.json'))['aligned_words']]
TOK = [(re.sub(r'[^a-z0-9]', '', re.sub(r'\[[^\]]*\]', '', w['word']).lower()), w['start_s']) for w in W]
TOK = [t for t in TOK if t[0]]

def when(phrase, after):
    """Start time of the first occurrence of `phrase` (words) starting at or after `after` seconds."""
    ws = [re.sub(r'[^a-z0-9]', '', x.lower()) for x in phrase.split()]
    for i in range(len(TOK) - len(ws) + 1):
        if TOK[i][1] >= after - 0.3 and all(TOK[i + k][0] == ws[k] for k in range(len(ws))):
            return TOK[i][1]
    if after > 0 and not getattr(when, '_retry', False):  # a line already under way when the shot starts
        when._retry = True
        try: return when(phrase, after - 3.0)
        finally: when._retry = False
    raise SystemExit(f'phrase not found after {after}: {phrase}')

def build(slot, inp, segs, end=None):
    """segs: [(text, quad, style, cue_phrase)] in order; returns sign list in source time."""
    out = []; starts = []
    for text, quad, style, cue in segs:
        starts.append(when(cue, slot))
    for k, (text, quad, style, cue) in enumerate(segs):
        a = inp + (starts[k] - LEAD - slot)
        b = inp + (starts[k + 1] - LEAD - slot) if k + 1 < len(segs) else 99
        out.append({'quad': quad, 'text': text, 'style': style, 'from': round(max(0, a), 3), 'to': round(b, 3)})
    return out
