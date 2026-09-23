"""Content completeness, structural safety, deep links and SVG validation."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'playbook/assets/theses.json').read_text())
assert [x['id'] for x in data]==list(range(1,61))
assert len({x['slug'] for x in data})==60
class Parse(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        for attr in ('href','src'):
            if a.get(attr):self.refs.append(a[attr])
parsed={}
for p in [R/'index.html',*(R/'playbook').glob('*.html')]:
    obj=Parse();obj.feed(p.read_text());parsed[p]=obj
    assert len(obj.ids)==len(set(obj.ids)),f'Duplicate id {p}'
    assert obj.h1==1,f'Expected single h1 {p}'
for p,obj in parsed.items():
    for ref in obj.refs:
        u=urlsplit(ref)
        if u.scheme:continue
        target=(R/u.path.lstrip('/')) if u.path.startswith('/') else (p.parent/u.path if u.path else p)
        if target.is_dir():target=target/'index.html'
        assert target.exists(),f'Missing {p}: {ref}'
        if u.fragment and target in parsed:assert unquote(u.fragment) in parsed[target].ids,f'Missing anchor {ref}'
for t in data:
    page=(R/'playbook'/f'{t["slug"]}.html').read_text()
    assert all(f'id="{x}"' in page for x in ['visual','reference','thesis','management'])
    assert len(t['body'])>100 and t['invalidation'] and t['avoid']
    root=ET.parse(R/'playbook/assets'/f'{t["slug"]}.svg').getroot()
    assert root.attrib['viewBox']=='0 0 900 420'
    text=' '.join(root.itertext())
    assert 'NOT MARKET DATA' in text and 'schematic spacing' in text
    assert all(str(i) in text for i in range(1,5))
    if t['direction']=='Wait':assert 'No entry is illustrated' in text
    else:assert 'Invalidation' in text and 'First objective' in text
assert 'Terminology correction' in (R/'playbook/41-ma-gap-bar-reversal.html').read_text()
assert not re.search(r'64335233|PAAPEX|51,093|ishari|Downloads/', ''.join(p.read_text() for p in (R/'playbook').rglob('*') if p.is_file()))
print(f'PASS: {len(data)} complete theses, 60 valid SVGs, {len(parsed)} HTML pages, local links and anchors, waiting scenarios, MA-gap correction, privacy check.')
