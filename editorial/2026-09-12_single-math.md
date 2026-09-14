# Single visual formula output / 單次公式呈現

v0.4.1 · 2026-09-12 · Rendering fix requested by the user; no academic chapter advanced.

The previous renderer used KaTeX `htmlAndMathml`, which creates both a visual HTML branch and a MathML accessibility branch. The user's pasted example is consistent with a preview exposing both branches; the exact preview behavior was not reproduced in the headless browser. The renderer now uses `output: html`, so no parallel MathML representation is emitted. A nonvisual, escaped TeX `aria-label` is retained on each formula. This label is not equivalent to structured MathML accessibility; editable TeX remains in the canonical sources.

原編譯器使用 htmlAndMathml，會同時產生視覺 HTML 與 MathML 輔助分支。使用者貼出的例子符合預覽同時呈現兩個分支的情形；無頭瀏覽器未重現該預覽的確切行為。現改為僅輸出 HTML，移除平行 MathML。每式保留經跳脫、不顯示的 TeX 輔助標籤，但它不等同結構化 MathML 的可及性；可編修 TeX 仍完整保存。

Both academic and accessible editions use the shared renderer. Updated README and standing editorial requirements to preserve this behavior during future builds. No canonical academic content or accessible chapter text was changed. Legitimate separate references to formulas in English and Chinese paragraphs remain.

學術版與易讀版共用修正後的編譯器，README 與固定編修要求已同步。未變更學術正文或易讀章節文字；英中不同段落合理引用的公式仍保留。

Validation: 1,159 academic formulas and 3 accessible formulas compile with zero errors; each has exactly one HTML branch, zero MathML branches and a nonvisual label. Desktop/mobile inspection includes the Chapter 1 state definition corresponding to the user's example. No page-width overflow or failed asset requests. See 2026-09-12_single-math-validation.json. Full snapshot v0.4.1 is generated separately without overwriting prior backups.

驗證：學術版 1,159 個、易讀版 3 個公式編譯零錯誤，每式僅有一個 HTML 分支，MathML 分支數為零。桌面與手機視覺檢查包含使用者提到的第 1 章狀態定義。無整頁溢出或資源載入失敗。建立 v0.4.1 完整快照，不覆寫舊備份。

Reference: [KaTeX output options](https://katex.org/docs/options.html).
