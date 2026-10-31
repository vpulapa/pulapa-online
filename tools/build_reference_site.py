from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
SOURCE_DIR = WORKSPACE / "tmp" / "pdfs" / "site_sources"

SOURCES = [
    ("Alethia_Al_Brooks_Price_Action_Trilogy_Handbook_Version_1", "handbook.html", "Price Action Trilogy Handbook", "98-page study companion: core grammar, trends, ranges, reversals, ES decision architecture, setup families, time of day, risk, recall, and glossary."),
    ("Alethia_Brooks_Master_Framework_Cards_v1", "framework.html", "Brooks Master Framework Cards", "The frozen 11-layer real-time ES decision architecture and full 15-phase training progression."),
    ("Alethia_ES_Thesis_Playbook_Daily_15_Min_Refresh_v1", "daily-playbook.html", "Daily 15-Minute Thesis Playbook", "The daily memory routine and complete qualification cards for the six approved thesis families."),
]

DROP = re.compile(r"^(ALETHIA\s*\||Alethia\s*-\s*.+Page\s+\d+|Page\s+\d+|\d+)$", re.I)
LABELS = {
    "Purpose", "Contents", "Read the behavior", "What to look for", "Common error", "Memory hook",
    "Core idea", "Live scan", "Evidence to respect", "Action rule", "Live compression example",
    "Behavioral story", "Best context / location", "Must be present / qualification", "Preferred trigger",
    "Structural invalidation", "Destination map", "Disqualifiers / pass", "Scaling rule", "Management / update",
    "30-second pre-entry check", "The purpose", "Non-negotiable rules", "The six stories",
}


def clean_lines(page: str) -> list[str]:
    result = []
    for raw in page.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if not line or DROP.match(line):
            result.append("")
            continue
        if line in {"ALETHIA", "Study edition - October 2026"}:
            continue
        result.append(line.replace("", "•").replace("□", "☐"))
    while result and not result[0]:
        result.pop(0)
    while result and not result[-1]:
        result.pop()
    return result


def page_title(lines: list[str], page_no: int) -> str:
    for line in lines[:12]:
        if line.startswith("•") or len(line) < 3:
            continue
        if line.lower() in {"how to use this handbook", "contents"}:
            return line
        if re.match(r"^(PART [A-I]|CORE FRAMEWORK|TRENDS STUDY MODULE|TRADING RANGES STUDY MODULE|REVERSALS CHAPTER|THESIS \d+|LAYER \d+)", line, re.I):
            return line
    for line in lines[:12]:
        if 3 <= len(line) <= 100:
            return line
    return f"Page {page_no}"


def to_blocks(lines: list[str]) -> str:
    blocks: list[str] = []
    para: list[str] = []
    bullets: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            text = " ".join(para)
            if text.upper() == text and 3 < len(text) < 120:
                blocks.append(f"<h3>{html.escape(text.title())}</h3>")
            elif text.rstrip(":").title() in LABELS or text.rstrip(":") in LABELS:
                blocks.append(f"<h3>{html.escape(text.rstrip(':'))}</h3>")
            else:
                blocks.append(f"<p>{html.escape(text)}</p>")
            para = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            blocks.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in bullets) + "</ul>")
            bullets = []

    for line in lines:
        if not line:
            flush_para(); flush_bullets(); continue
        if line.startswith(("•", "☐")):
            flush_para(); bullets.append(line[1:].strip()); continue
        flush_bullets()
        if re.match(r"^(PART [A-I]|CORE FRAMEWORK|TRENDS STUDY MODULE|TRADING RANGES STUDY MODULE|REVERSALS CHAPTER|THESIS \d+|LAYER \d+)", line, re.I):
            flush_para(); blocks.append(f"<h3>{html.escape(line)}</h3>"); continue
        para.append(line)
    flush_para(); flush_bullets()
    return "\n".join(blocks)


def shell(title: str, description: str, sections: list[tuple[str, str, int]], pdf_name: str) -> str:
    toc = "".join(f'<a href="#{sid}">{html.escape(stitle)}</a>' for sid, stitle, _ in sections)
    body = "".join(
        f'<section class="source-section" id="{sid}"><span class="page-tag">SOURCE PAGE {page}</span><h2>{html.escape(stitle)}</h2>{content}</section>'
        for (sid, stitle, page), content in zip(sections, SECTION_CONTENTS)
    )
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | Alethia</title><meta name="description" content="{html.escape(description)}"><link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head><body><div class="reference-shell"><aside class="reference-nav"><a class="wordmark" href="index.html"><span class="mark">A</span><span>ALETHIA</span></a><h2>{html.escape(title)}</h2><a class="back-home" href="index.html">← Quick-reference home</a><a class="back-home" href="downloads/{html.escape(pdf_name)}">Download source PDF ↓</a><div class="toc">{toc}</div></aside><main class="reference-main"><header class="reference-hero"><p class="eyebrow">COMPLETE SOURCE · READABLE WEB EDITION</p><h1>{html.escape(title)}</h1><p class="lede">{html.escape(description)}</p><div class="reference-tools"><input type="search" data-reference-search placeholder="Search this source…" aria-label="Search this source"><button class="theme-toggle" type="button" aria-label="Toggle color theme">◐</button></div></header>{body}</main></div></body></html>'''


downloads = ROOT / "downloads"
downloads.mkdir(exist_ok=True)
for source, _, _, _ in SOURCES:
    pdf_src = Path("/Users/ishari/Downloads") / f"{source}.pdf"
    shutil.copy2(pdf_src, downloads / pdf_src.name)

for stem, output, title, description in SOURCES:
    raw = (SOURCE_DIR / f"{stem}.txt").read_text(encoding="utf-8", errors="replace")
    pages = [clean_lines(p) for p in raw.split("\f") if clean_lines(p)]
    sections = []
    SECTION_CONTENTS = []
    for i, lines in enumerate(pages, 1):
        stitle = page_title(lines, i)
        sid = f"page-{i}"
        sections.append((sid, stitle, i))
        SECTION_CONTENTS.append(to_blocks(lines))
    (ROOT / output).write_text(shell(title, description, sections, f"{stem}.pdf"), encoding="utf-8")

execution = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Execution Guide | Alethia</title><link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head><body><div class="reference-shell"><aside class="reference-nav"><a class="wordmark" href="index.html"><span class="mark">A</span><span>ALETHIA</span></a><h2>Execution Guide</h2><a class="back-home" href="index.html">← Quick-reference home</a><div class="toc"><a href="#rules">Non-negotiables</a><a href="#questions">The 11 questions</a><a href="#risk">Risk and management</a><a href="#training">Training path</a></div></aside><main class="reference-main"><header class="reference-hero"><p class="eyebrow">LIVE COMPRESSION</p><h1>From correct reading to disciplined action.</h1><p class="lede">Do not let an attractive pattern override regime, control, location, evidence, or the trader’s equation.</p></header><section class="source-section" id="rules"><span class="page-tag">NON-NEGOTIABLES</span><h2>Operating rules</h2><ul><li>Regime sets the default expectation; price action must earn an exception.</li><li>Damage is not automatically a flip.</li><li>A breakout is a claim; follow-through determines acceptance.</li><li>Structure sets the stop; risk budget sets size.</li><li>Nearest reasonable destination first.</li><li>Every add must independently earn its existence.</li><li>If the thesis or equation is unclear, wait or do nothing.</li></ul></section><section class="source-section" id="questions"><span class="page-tag">PRE-ENTRY SCAN</span><h2>The 11 questions</h2><ol><li>What state is the market in?</li><li>Who has control: AIL, AIS, or uncertain?</li><li>What has each side actually accomplished?</li><li>What phase is the move in?</li><li>Where is price relative to structure and magnets?</li><li>What is the current attempt?</li><li>Did it receive follow-through?</li><li>Whose expectation failed and who may be trapped?</li><li>What is the nearest reasonable destination?</li><li>Does probability × reward justify failure × risk?</li><li>Enter, manage, exit, or wait?</li></ol></section><section class="source-section" id="risk"><span class="page-tag">STRUCTURE BEFORE COMFORT</span><h2>Risk, stops, and management</h2><p>Define structural invalidation before entry. If the correct stop is wider than usual, reduce size rather than placing the stop inside normal market noise. Do not move to breakeven merely because price moved slightly in your favor. If you would not enter the same trade now while flat, exit rather than anchoring to the entry price.</p><p>Management must remain consistent with the premise. A swing justified by asymmetric reward cannot be converted into a tiny scalp simply because open profit feels fragile. Reassess when control, structure, acceptance, or the equation materially changes.</p></section><section class="source-section" id="training"><span class="page-tag">15-PHASE PROGRESSION</span><h2>Learn → compress → retrieve → recognize → execute → review → validate → scale</h2><ol><li>Acquire the language.</li><li>Build the Brooks Master Framework.</li><li>Compress into decision tree, regime map, and thesis cards.</li><li>Active recall.</li><li>Frozen-chart training.</li><li>Timed recognition.</li><li>Isolated setup drills.</li><li>Mixed-regime drills.</li><li>Replay training.</li><li>Error database.</li><li>Simulator execution.</li><li>Performance gates.</li><li>Minimum live size.</li><li>Statistical evidence.</li><li>Gradual scaling.</li></ol></section></main></div></body></html>'''
(ROOT / "execution.html").write_text(execution, encoding="utf-8")

# Preserve old /playbook/ links by routing the former landing page into the new guide.
(ROOT / "playbook" / "index.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/daily-playbook.html"><link rel="canonical" href="https://pulapa.online/daily-playbook.html"><title>Alethia Playbook</title><p><a href="/daily-playbook.html">Open the Alethia daily playbook</a></p>', encoding="utf-8")
print("Generated:", ", ".join(output for _, output, _, _ in SOURCES), "execution.html, and PDF downloads")
