#!/usr/bin/env python3
"""
Prosty skrypt generujący `docs/data.json` ze wpisów markdown.
Uruchom w repozytorium: `python3 scripts/generate_data.py`
"""
import os, json, re

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT = os.path.join(ROOT, 'docs', 'data.json')
CATEGORIES = ['news','conferences','trainings','webinars']

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    fm = m.group(1)
    rest = text[m.end():]
    data = {}
    for line in fm.splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            data[k.strip()] = v.strip().strip('"')
    return data, rest

def excerpt(text, limit=200):
    p = text.strip().split('\n\n')
    if not p:
        return ''
    e = p[0].strip().replace('\n',' ')
    return e[:limit] + ('...' if len(e)>limit else '')

items = []
for cat in CATEGORIES:
    folder = os.path.join(ROOT, cat)
    if not os.path.isdir(folder):
        continue
    for fn in os.listdir(folder):
        if not fn.lower().endswith('.md'):
            continue
        path = os.path.join(folder, fn)
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()
        fm, body = parse_frontmatter(txt)
        item = {
            'title': fm.get('title', fn.replace('.md','')),
            'date': fm.get('date',''),
            'category': cat,
            'path': f"{cat}/{fn}",
            'excerpt': excerpt(body),
            'tags': fm.get('tags','')
        }
        items.append(item)

# sort by date desc when possible
def keyfn(i):
    return i.get('date','')
items.sort(key=keyfn, reverse=True)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT,'w',encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print('Wygenerowano', OUT)
