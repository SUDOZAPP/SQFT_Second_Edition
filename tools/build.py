"""Build the entire bilingual book offline, retaining editable TeX source.
Run: python tools/build.py --node /path/to/node
Only the generated index.html and validation.json are overwritten.
"""
from pathlib import Path
import argparse, html, json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--node', default='node')
args = parser.parse_args()
source = (ROOT/'source/manuscript.html').read_text(encoding='utf-8')
# Script strings contain delimiter examples, not book equations.
source = re.sub(r'<script\b[^>]*>.*?</script>', '', source, flags=re.S|re.I)
state = json.loads((ROOT/'editorial/progress.json').read_text(encoding='utf-8'))
ids = re.findall(r'id="ch(\d+)"', source)
assert len(ids) == 50 and set(ids) == set(map(str, range(1,51))), 'Missing or duplicate chapter'

# Source uses dollar-delimited TeX. Equations are processed before HTML parsing,
# so literal comparison signs in the inherited mathematical source are retained.
pattern = re.compile(r'\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$', re.S)
matches = list(pattern.finditer(source))
items = [{'tex': html.unescape(m.group(1) if m.group(1) is not None else m.group(2)),
          'display': m.group(1) is not None} for m in matches]
result = subprocess.run([args.node, str(ROOT/'tools/render_math.cjs')],
                        input=json.dumps(items), text=True, encoding='utf-8',
                        capture_output=True, check=True)
rendered = json.loads(result.stdout)
errors = [r for r in rendered['results'] if 'error' in r]
if errors:
    (ROOT/'editorial/math-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2),encoding='utf-8')
    raise SystemExit(f'{len(errors)} KaTeX errors; publication stopped')
iterator = iter(rendered['results'])
book = pattern.sub(lambda _: next(iterator)['html'], source)
# Local assets; equations are pre-rendered with KaTeX, with no CDN at read time.
book = re.sub(r'<script\b[^>]*>.*?</script>', '', book, flags=re.S|re.I)
book = re.sub(r'<link\b[^>]*>', '', book, flags=re.I)
book = book.replace('</head>', '<link rel="stylesheet" href="assets/katex/katex.min.css">\n<style>\n'+(ROOT/'assets/edition.css').read_text(encoding='utf-8')+'\n</style></head>')
book = re.sub(r'<title>.*?</title>', '<title>SQFT · Second Edition Working Manuscript · 第二版編修稿</title>', book, flags=re.S)
book = book.replace('src="cover_opt.jpg"','src="assets/cover_opt.jpg"')
book = book.replace('<span>First Edition</span>', '<span>Second Edition · Draft</span>')
book = re.sub(r'<html lang="[^"]+"', '<html lang="en"', book, count=1)
book = book.replace('<p class="zh">','<p class="zh" lang="zh-Hant">')
done = state['completed_chapters']
notice = f'''<aside class="edition-notice" id="edition-status">
<strong>SECOND EDITION · WORKING MANUSCRIPT {html.escape(state['version'])}</strong>
<p>Full 50-chapter base · Revised: {', '.join(map(str,done)) or 'none'} · Updated {state['last_revision_date']}.</p>
<p lang="zh-Hant">第二版完整編修基底：已修訂第 {', '.join(map(str,done)) or '0'} 章。其餘章節與歷史前後置內容沿用第一版，仍待審訂。</p>
<p><a href="#ch{done[-1] if done else 1}">Read the latest revised chapter／閱讀最新修訂章</a> · <a href="editorial/progress.json">Revision status／修訂狀態</a> · <a href="easy.html">Accessible edition／全書易讀版</a></p>
<p class="archive-note">The cover and archival declarations below document the first edition; they do not certify this working revision.<br><span lang="zh-Hant">以下封面與存檔宣言保留第一版歷史，不構成本編修稿的認證。</span></p></aside>'''
book = book.replace('<body>', '<body>\n'+notice, 1)
def badge(m):
    number = int(m.group(1))
    label = ('Revised draft · 已修訂草稿' if number in done else 'Inherited from Edition 1 · 第一版沿用，待審訂')
    return m.group(0)+f'<p class="revision-badge {"revised" if number in done else "pending"}">{label}</p>'
book = re.sub(r'<h3 id="ch(\d+)">.*?</h3>',badge,book,flags=re.S)
# Controls whose original scripts are intentionally removed should not be inert.
book = re.sub(r'<button\b[^>]*id="(?:theme-toggle|to-top)"[^>]*>.*?</button>','',book,flags=re.S)
(ROOT/'index.html').write_text(book,encoding='utf-8')
validation = {'version':state['version'],'chapter_count':50,'katex_version':rendered['version'],
              'math_expressions':len(items),'math_errors':0,'offline_assets':True,
              'source':'source/manuscript.html','completed_chapters':done}
(ROOT/'editorial/validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(validation,ensure_ascii=False))

# Keep the accessible companion synchronized with current revision labels.
subprocess.run([sys.executable, str(ROOT/"tools/build_easy.py"), "--node", args.node], check=True)
