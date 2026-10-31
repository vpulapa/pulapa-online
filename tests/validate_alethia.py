from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
PAGES=['index.html','handbook.html','framework.html','daily-playbook.html','execution.html','404.html']
errors=[]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.title=False; self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if 'id' in a:self.ids.add(a['id'])
        if tag=='title':self.title=True
        if tag=='h1':self.h1+=1

for name in PAGES:
    p=ROOT/name
    if not p.exists():errors.append(f'missing {name}');continue
    parser=Parser();parser.feed(p.read_text(encoding='utf-8'))
    if not parser.title:errors.append(f'{name}: missing title')
    if parser.h1!=1:errors.append(f'{name}: expected one h1, found {parser.h1}')
    for href in parser.links:
        if href.startswith(('#','http:','https:','mailto:')):continue
        target=urlparse(href).path.lstrip('/')
        if target.endswith('/'):target+='index.html'
        if target and not (ROOT/target).exists():errors.append(f'{name}: broken link {href}')

home=(ROOT/'index.html').read_text(encoding='utf-8')
for required in ['daily','theses','framework','regimes','execution','library']:
    if f'id="{required}"' not in home:errors.append(f'index missing #{required}')
if home.count('class="regime ')!=5:errors.append('index: expected five regimes')
js=(ROOT/'assets/site.js').read_text(encoding='utf-8')
if js.count("tier:'")!=6:errors.append('site.js: expected six theses')
for filename in ['Alethia_Al_Brooks_Price_Action_Trilogy_Handbook_Version_1.pdf','Alethia_Brooks_Master_Framework_Cards_v1.pdf','Alethia_ES_Thesis_Playbook_Daily_15_Min_Refresh_v1.pdf']:
    if not (ROOT/'downloads'/filename).exists():errors.append(f'missing download {filename}')
if not (ROOT/'assets'/'favicon.svg').exists():errors.append('missing favicon.svg')
for page in ROOT.rglob('*.html'):
    text=page.read_text(encoding='utf-8')
    if 'rel="icon"' not in text:errors.append(f'{page.relative_to(ROOT)}: missing favicon')
    if 'chapter 23' in text.lower():errors.append(f'{page.relative_to(ROOT)}: Chapter 23 disclaimer remains')
if errors:raise SystemExit('Alethia validation failed:\n- '+'\n- '.join(errors))
print('Alethia validation passed: core pages, links, five regimes, six theses, three PDF downloads, shared favicon, and Chapter 23 removal verified.')
