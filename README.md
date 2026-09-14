# Social Quantum Field Theory — Second Edition Working Base
# 社會量子場論 — 第二版完整編修基底

Version 0.6.0 · 2026-09-14 · Chapters 1–6 revised; Chapters 7–50 inherited and awaiting review.

版本 0.6.0：第 1–6 章已完成本輪修訂；第 7–50 章沿用第一版，仍待審查。本版不是全書已驗證完成的定稿。

## Accessible edition / 全書易讀版

Open `easy.html` for a bilingual explanation of all 50 chapters, with everyday examples, interpretation limits, a glossary and three offline KaTeX equations. It is an explanatory adaptation, not a replacement for the academic text or its proofs. Edit `source/easy/chapters.txt`; each line contains a chapter number and eight pipe-separated text fields. The regular build also rebuilds this companion.

開啟 `easy.html` 閱讀全部 50 章的英中易讀解說，包含生活例子、理解界線、術語表及三個離線 KaTeX 公式。這是說明性改寫，不取代學術正文及證明。來源為 `source/easy/chapters.txt`，每列含章號與八個以直線分隔的文字欄位；一般建置也會重建此版本。

## Read / 閱讀

Extract the entire ZIP, then open `index.html` in a browser. Keep the assets directory alongside it. All book formulas are pre-rendered with KaTeX 0.16.11, with a single HTML visual representation and a nonvisual TeX accessibility label; no network or JavaScript is required to display them. Narrow screens can scroll long equations horizontally. References remain clickable external links.

完整解壓縮 ZIP，再以瀏覽器開啟 `index.html`，並保留相鄰的 assets 資料夾。全書公式已使用 KaTeX 0.16.11 預先渲染，每式僅輸出一套 HTML 視覺表示，另附不顯示的 TeX 輔助標籤；顯示公式不需要網路或 JavaScript。窄螢幕可橫向捲動長公式。參考文獻仍可點選外部連結。

## Contents / 內容

- `index.html`: complete 50-chapter reading copy with revision labels / 全書閱讀版與修訂標示。
- `source/manuscript.html`: canonical editable bilingual text, with dollar-delimited TeX / 唯一正文編修來源，保留 TeX 公式。
- `originals/`: byte-preserved copy of all 23 files in the supplied first-edition folder, including separate volumes and appendices / 指定第一版資料夾全部 23 個檔案的原樣備份，包含分卷與附錄。
- `assets/`: local KaTeX, its license, mathematical fonts, cover and editorial CSS / 離線公式程式、授權、數學字型、封面及版面樣式。
- `editorial/`: progress, daily log, review findings and validation results / 進度、逐日紀錄、審查與驗證結果。
- `tools/`: offline build and complete-backup scripts / 離線重建與完整備份腳本。
- `SHA256_MANIFEST.json`: file inventory, sizes and hashes / 檔案清單、大小與校驗碼。

Original titles, front matter, cover and archival declarations are retained as historical material. The prominent second-edition notice and per-chapter labels identify current status. Separate-volume contents are preserved in originals; they have not all been merged into the 50-chapter integrated manuscript.

原書名、前後置、封面與存檔宣言作為歷史資料保留；第二版說明及逐章標示界定目前狀態。分卷全文保留於 originals，尚未全數併入 50 章整合正文。

## Edit and rebuild / 編修與重建

Edit only the intended chapter in `source/manuscript.html`, using the numbered `CHAPTER` comment markers. Keep academic English and Traditional Chinese paired paragraph by paragraph. Use `$...$` for inline and `$$...$$` for display TeX. Escape HTML characters when needed; the builder decodes entities inside formulas. Do not directly edit generated KaTeX HTML.

依 `CHAPTER` 章號註解定位，只編修當日章節；維持學術英文與繁體中文逐段對照。行內公式用 `$...$`，獨立公式用 `$$...$$`，必要時跳脫 HTML 字元。建置器會還原公式內的字元實體。不要直接修改生成後的 KaTeX HTML。

Requirements: Python 3.12+ standard library and Node.js. KaTeX is bundled; npm installation is unnecessary.

需求：Python 3.12 以上標準函式庫與 Node.js。已附 KaTeX，不需要 npm 安裝。

```text
python tools/build.py --node /path/to/node
python tools/backup.py
```

The build checks all 50 chapter anchors and fails on KaTeX errors. Review the new chapter visually and mathematically, then create the full backup. Backups are written beside this folder in `backups/`, with version and date; existing snapshots are never overwritten. Verify a ZIP using its `.sha256` sidecar and the internal manifest.

建置會檢查全部 50 章錨點，且遇到 KaTeX 錯誤即停止。完成新章的數學與視覺檢查後，再建立完整備份。備份放在此資料夾旁的 `backups/`，名稱含版本與日期，既有快照不覆寫。可用 `.sha256` 檔及壓縮包內清單核對完整性。

## Daily revision / 每日修訂

Use `editorial/progress.json` to locate the next chapter and `editorial/DAILY_WORKFLOW.md` for the revision process. The requested schedule is one chapter per day at 09:00 Asia/Taipei, beginning with Chapter 2 on 2026-09-10. A scheduled run needing local files requires the computer and desktop app to be running. See the [official scheduling documentation](https://learn.chatgpt.com/docs/automations?surface=app).

依 `editorial/progress.json` 決定下一章，依 `editorial/DAILY_WORKFLOW.md` 執行。排程為每天台北時間 09:00 修訂一章，從 2026-09-10 的第 2 章開始。使用本機檔案的排程需要電腦及桌面應用程式保持開啟，見上述官方說明。

## Standing requirements / 固定編修要求

See [EDITORIAL_REQUIREMENTS.md](editorial/EDITORIAL_REQUIREMENTS.md) for the user-confirmed rules on main-text figures and proofs, appendices, executable research code, supplementary data, reference completeness and daily edition synchronization.

正文圖表與證明、附錄、研究程式、補充資料、引用齊備性及每日版本同步，均依上述使用者確認規範執行。

## Chapter 4 supplement / 第 4 章補充資料

[supplements/ch04/README.md](supplements/ch04/README.md) provides exact algebra verification code, instructions and recorded output; see Appendix 4.A in the academic reading copy. This is not empirical simulation data.

提供精確代數檢查程式、執行說明與輸出，見正文附錄 4.A；不是實證模擬資料。

## Chapter 5 supplement / 第 5 章補充資料

[supplements/ch05/README.md](supplements/ch05/README.md) documents the complete exact-probability verification program and its recorded output. Figure 5.1, Table 5.1 and the general proofs appear in the main text; Appendix 5.A explains the electronic supplement. No empirical football data were used.

完整精確機率驗證程式與執行結果見上述說明。圖 5.1、表 5.1 與一般性證明置於正文；附錄 5.A 說明電子補充資料。未使用足球實證資料。

## Chapter 6 supplement / 第 6 章補充資料

[supplements/ch06/README.md](supplements/ch06/README.md) supplies complete deterministic verification code and recorded output for the normalization, measurement and metric examples. General proofs and Table 6.1 are in the main text; Appendix 6.A describes the supplement. No empirical data are claimed.

提供歸一化、測量及度量例子的完整確定性驗證程式與執行結果。一般性證明與表 6.1 在正文，附錄 6.A 說明補充資料；未宣稱具有實證資料。
