import json, sys
issue_path, out_packet, out_msg = sys.argv[1:4]
d = json.load(open(issue_path)); c = json.load(open(issue_path[:-5] + '.side.clerk.json'))
p = {'issue': {k: d['issue'][k] for k in ('title', 'question', 'summary', 'summary_sources')}, 'poll': d.get('poll'),
     'sources': d['sources'], 'citizens_tests': d['citizens']['tests'], 'citizens_voices': d['citizens']['voices'],
     'angles': c.get('angles'), 'facts_for_writers': c.get('facts_for_writers', []), 'extra_sources': c.get('extra_sources', [])}
json.dump(p, open(out_packet, 'w'), ensure_ascii=False, indent=1)
nd = d['run']['news_date']
msg = f'''You are writing answer C, blind, for a clearly labelled SIMULATION of a different way of governing (the BadCode "Future Proof" art project). Do not touch any files, do not run git. Just reply with one JSON object.

Your angle: FROM THE GROUND UP. Answer as someone who distrusts both big government and big business, and reaches for local control, people who use the service owning or steering it, or a market rule that makes the right behaviour pay.

Rules:
- One concrete answer, not a list of options. title <=70 characters; answer <=120 words, plain words, short sentences, no jargon. Say what changes, who does it, and how you'd know it worked.
- Every fact you use must come from the sources in the packet (cite their ids, e.g. "s6"), or from a page you open now (add it to new_sources with title, publisher, date YYYY-MM-DD, url). No real person's words. No claim about a named company that the sources don't make. If unsure of a fact, leave it out.
- These are simulated citizens; never call them "the public".
- Write only what was knowable on {nd} (this is a replay of that day's news).

Reply with ONLY this JSON (no prose):
{{"id":"C","title":"...","answer":"...","engine":"codex","model":"<your exact model id>","blind":true,"sources":["s..."],"new_sources":[]}}

PACKET:
{json.dumps(p, ensure_ascii=False)}'''
open(out_msg, 'w').write(msg)
print(len(msg))
