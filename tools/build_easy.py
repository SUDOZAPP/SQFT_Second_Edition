"""Build the bilingual accessible companion; all assets remain local."""
from pathlib import Path
import argparse, json, html, re, subprocess
ROOT=Path(__file__).resolve().parents[1]
args=argparse.ArgumentParser();args.add_argument('--node',default='node');args=args.parse_args()
state=json.loads((ROOT/'editorial/progress.json').read_text(encoding='utf-8'))
rows=[line.split('|') for line in (ROOT/'source/easy/chapters.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(rows)==50 and all(len(r)==9 for r in rows)
assert [int(r[0]) for r in rows]==list(range(1,51))
source=(ROOT/'source/manuscript.html').read_text(encoding='utf-8')
titles={int(n):re.sub('<[^>]+>',' ',t).strip() for n,t in re.findall(r'<h3 id="ch(\d+)">(.*?)</h3>',source,re.S)}
def esc(s):return html.escape(s)
def pair(en,zh):return f'<div class="pair"><p lang="en">{esc(en)}</p><p lang="zh-Hant">{esc(zh)}</p></div>'
parts=['''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Social Quantum Field Theory · 全書易讀版</title><link rel="stylesheet" href="assets/katex/katex.min.css"><style>
:root{color-scheme:light;--ink:#223342;--muted:#586978;--line:#dae2e5;--blue:#225a70}*{box-sizing:border-box}body{margin:0;background:#f4f3ef;color:var(--ink);font-family:Georgia,'Microsoft JhengHei',serif;line-height:1.85}a{color:var(--blue);text-underline-offset:3px}header,main,footer{max-width:1000px;margin:auto;padding:30px}header{padding-top:64px}h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.25;margin:16px 0}h2{line-height:1.4;font-size:1.7rem}h3{font-size:1.05rem;color:var(--blue);margin:28px 0 8px}p{margin:10px 0}.eyebrow,.status{font-family:Arial,'Microsoft JhengHei',sans-serif;font-size:.85rem;letter-spacing:.04em}.lead{font-size:1.2rem}.pair p[lang=en]{color:var(--muted);font-size:1rem}.pair p[lang=zh-Hant]{font-size:1.1rem}.chapter,.panel{background:white;border:1px solid var(--line);border-radius:14px;padding:34px;margin:24px 0}.chapter{scroll-margin-top:20px}.number{font-size:.9rem;color:var(--muted)}.english-title{display:block;font-size:1.05rem;font-weight:normal;color:var(--muted);margin-top:8px}.status{background:#edf3f4;display:inline-block;padding:4px 10px;border-radius:6px}.pending{background:#f8f0df;color:#715927}.example{border-left:3px solid #a7bfc6;padding-left:20px}.limit{background:#f6f6f2;padding:2px 20px 16px;border-radius:8px}.chapter-footer{border-top:1px solid var(--line);margin-top:28px;padding-top:16px;font-size:.9rem;display:flex;gap:20px;flex-wrap:wrap}nav ol{columns:2;column-gap:36px;padding-left:26px}nav li{break-inside:avoid;margin:6px 0}summary{cursor:pointer;font-weight:bold;padding:8px 0}dl dt{font-weight:bold;margin-top:18px}dl dd{margin:4px 0 16px}.math{overflow-x:auto;padding:10px 0}.source-title{font-size:.88rem;color:var(--muted)}@media(max-width:600px){header,main,footer{padding:20px}header{padding-top:34px}.chapter,.panel{padding:22px 18px}nav ol{columns:1}.example{padding-left:12px}.limit{padding-left:12px;padding-right:12px}.pair p[lang=zh-Hant]{font-size:1.04rem}}@media print{body{background:white}.chapter{break-before:page;border:0;padding:0}nav,.chapter-footer{display:none}header,main,footer{max-width:none}.panel{border:0}.math{overflow:visible}}
</style></head><body><header id="top"><div class="eyebrow">SOCIAL QUANTUM FIELD THEORY · ACCESSIBLE EDITION</div><h1>全書易讀版</h1><p class="lead">從生活例子，讀懂 50 章的問題、工具與推論界線。</p><p lang="en">A bilingual companion to all 50 chapters: questions, examples and the limits of each claim.</p>''']
parts.append(f'<p class="status">v{esc(state["version"])} · {esc(state["last_revision_date"])} · EN / 繁體中文</p><p><a href="index.html">學術正文 / Academic edition</a> · <a href="#contents">50 章目錄 / Contents</a> · <a href="#glossary">術語表 / Glossary</a></p></header><main>')
parts.append('<section class="panel"><h2>先掌握一個問題<span class="english-title">Start with one question</span></h2>')
parts.append(pair('What changes when we describe people together with their relationships, roles and shared settings? This companion explains the integrated manuscript chapter by chapter in accessible language. It is an explanatory adaptation, not a line-by-line translation or a substitute for complete mathematical proofs.','把人連同關係、角色與共同環境一起描述，會多看見什麼？本版以容易理解的語言逐章解說整合正文，是說明性的改寫，不是逐句翻譯，也不取代完整數學證明。'))
parts.append(pair('Every everyday scenario below is an illustrative example, not a reported empirical study. Chapters 1–6 currently follow revised drafts; Chapters 7–50 explain the inherited manuscript with explicit limits. Mathematical tools borrowed from physics do not by themselves establish physical quantum behavior in society.','以下生活情境全是示意例子，不是已發表的實證研究。目前第 1–6 章依修訂草稿解說；第 7–50 章依沿用正文解說並指出限制。借用物理數學工具，本身不證成社會具有物理量子行為。'))
parts.append('<p>原著 / Original work: Chou I-Hsien。易讀編寫依第二版工作稿整理，例子及理解提醒為本版新增編輯內容。</p></section>')
parts.append('<nav class="panel" id="contents" aria-label="Chapter contents"><h2>50 章目錄</h2>')
groups=['起點、關係與表示 / Foundations and representation','資訊、驗證與運算 / Information, testing and computation','集體模式、學習與決策 / Collective patterns, learning and decisions','重建、幾何與計算工具 / Reconstruction, geometry and methods','尺度、結構與全書回顧 / Scales, structures and outlook']
for j,label in enumerate(groups):
 parts.append(f'<details open><summary>{j*10+1}–{j*10+10} · {label}</summary><ol start="{j*10+1}">')
 for r in rows[j*10:j*10+10]:parts.append(f'<li><a href="#easy-ch{r[0]}">{esc(r[2])}</a></li>')
 parts.append('</ol></details>')
parts.append('</nav>')
for n,en_title,zh_title,en,zh,ex_en,ex_zh,lim_en,lim_zh in rows:
 done=int(n) in state['completed_chapters']
 parts.append(f'<article class="chapter" id="easy-ch{n}"><div class="number">CHAPTER {n} / 第 {n} 章</div><h2>{esc(zh_title)}<span class="english-title">{esc(en_title)}</span></h2>')
 parts.append(f'<p class="status {"" if done else "pending"}">{"依已修訂草稿解說 / Based on revised draft" if done else "正文待審訂；本章為解說 / Academic chapter pending review"}</p>')
 parts.append(f'<p class="source-title">對應正文 / Academic title: {esc(titles[int(n)])}</p>')
 parts.append('<h3>這章在問什麼 / The question</h3>'+pair(en,zh))
 parts.append('<div class="example"><h3>生活例子 / An everyday example</h3>'+pair(ex_en,ex_zh)+'</div>')
 parts.append('<div class="limit"><h3>理解時要注意 / How far the explanation goes</h3>'+pair(lim_en,lim_zh)+'</div>')
 parts.append(f'<div class="chapter-footer"><a href="index.html#ch{n}">閱讀本章學術正文 / Academic chapter</a><a href="#contents">回目錄 / Contents</a>')
 if int(n)<50:parts.append(f'<a href="#easy-ch{int(n)+1}">下一章 / Next chapter →</a>')
 parts.append('</div></article>')
parts.append('<section class="panel" id="glossary"><h2>常用術語，用一句話理解<span class="english-title">A short glossary</span></h2><dl>')
terms=[('場域 / Sociological field','A structured setting of positions, resources and stakes.','由位置、資源與利害關係組成的社會環境。'),('狀態 / State','A model description at a given stage.','模型對某個階段的描述。'),('觀測量 / Observable','A specified quantity linked to a measurement procedure.','連結到指定測量程序的量。'),('算子 / Operator','A mathematical rule acting on a model description.','作用於模型描述的數學規則。'),('參數 / Parameter','A value specifying one model within a family.','在一群模型中指定某個模型的數值。'),('熵 / Entropy','An uncertainty measure for a specified distribution or state.','對指定分配或狀態衡量不確定性的量。'),('互資訊 / Mutual information','A measure of statistical dependence, not a causal verdict.','統計相依的量度，不是因果判決。'),('粗粒化 / Coarse-graining','Replacing fine detail with selected summaries.','用選定摘要取代細節。'),('不變量 / Invariant','A quantity unchanged under specified transformations.','在指定變換下不變的量。'),('可識別性 / Identifiability','Whether observations can distinguish candidate explanations.','觀察能否分辨候選解釋。'),('近似 / Approximation','A simplified calculation whose error needs assessment.','需要評估誤差的簡化計算。'),('公理 / Axiom','A starting assumption, not empirical proof of itself.','出發假設，不是自身的實證證明。')]
for label,en,zh in terms:parts.append(f'<dt>{esc(label)}</dt><dd>{pair(en,zh)}</dd>')
parts.append('</dl></section><section class="panel"><h2>三個小公式，連回核心概念<span class="english-title">Three small equations</span></h2>')
formulas=[r'P(A=0,B=0)=\frac12\ne\frac14=P(A=0)P(B=0)',r'\sum_{i=1}^{n}p_i=1,\qquad p_i\geq0',r'2^{10}=1024']
rendered=json.loads(subprocess.run([args.node,str(ROOT/'tools/render_math.cjs')],input=json.dumps([{'tex':t,'display':True} for t in formulas]),text=True,encoding='utf-8',capture_output=True,check=True).stdout)
assert not any('error' in r for r in rendered['results'])
explanations=[('In Chapter 2, two binary choices copy the same fair binary variable. Their joint probability differs from the product of their separate probabilities: dependence can arise in a classical model.','第 2 章讓兩個二元選擇都跟隨同一個公平二元變數。共同機率與各自機率的乘積不同，說明經典模型也能產生相依。'),('For a finite list of mutually exclusive outcomes that covers all possibilities, probabilities are nonnegative and sum to one. This is a basic check for a prediction table.','對涵蓋所有可能且彼此互斥的有限結果清單，機率非負且總和為一。這是預測表最基本的檢查。'),('Ten binary switches have 1,024 joint settings. This count assumes all combinations are allowed; probabilities need not be equal or independent.','十個二元開關共有 1,024 種共同設定。這個計數假設所有組合都允許；各組合機率不必相等，開關也不必獨立。')]
for r,(en,zh) in zip(rendered['results'],explanations):parts.append('<div class="math">'+r['html']+'</div>'+pair(en,zh))
parts.append('</section></main><footer><p><a href="#top">回頁首 / Back to top</a> · <a href="index.html">學術正文 / Academic edition</a></p><p>本檔可離線閱讀；請保留 assets 資料夾。完整備份另含原始文件、學術正文與可編修來源。<br>Offline reading: keep the assets folder alongside this file. The full backup also includes originals and editable sources.</p></footer></body></html>')
out='\n'.join(parts)
assert '人話' not in out
(ROOT/'easy.html').write_text(out,encoding='utf-8')
report={'version':state['version'],'chapters':len(rows),'bilingual_chapter_pairs':150,'math_expressions':len(formulas),'math_errors':0,'source':'source/easy/chapters.txt','output':'easy.html','purpose':'Accessible chapter-by-chapter adaptation, not complete proofs or an independent certification.'}
(ROOT/'editorial/easy-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report))
