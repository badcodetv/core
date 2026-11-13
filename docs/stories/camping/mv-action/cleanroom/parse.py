import json,re,sys,pathlib
H=pathlib.Path(__file__).parent; out={}
for k,beat in [('w1','bob'),('w2','tarquin'),('w3','pairs')]:
    f=H/f'{k}.md'
    if not f.exists(): continue
    for m in re.finditer(r'=== SHOT (\w+) ===\nman: (\w+)\nidea: (.*?)\nprompt: (.*?)(?=\n\n=== SHOT|\Z)',f.read_text(),re.S):
        sid,man,idea,prompt=m.groups()
        out[sid]={'beat':beat,'man':man.strip(),'idea':idea.strip(),'prompt':prompt.strip(),'writer':k}
json.dump(out,open(H/'prompts.json','w'),indent=1); print(len(out), list(out))
