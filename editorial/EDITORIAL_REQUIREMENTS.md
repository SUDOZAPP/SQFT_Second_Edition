# Standing editorial requirements / 固定編修要求

Confirmed by the user on 2026-09-10. Apply throughout the second-edition revision and read alongside DAILY_WORKFLOW.md. Later explicit user instructions take precedence.

使用者於 2026-09-10 確認。第二版後續修訂均適用，與 DAILY_WORKFLOW.md 一起閱讀；使用者後續明示指示優先。

## Editions and preservation / 版本與保存

- Maintain academic English and Traditional Chinese paragraph by paragraph. Render reading-copy mathematics with local KaTeX and retain editable TeX sources.
  維持學術英文／繁體中文逐段對照；閱讀版公式使用離線 KaTeX，保存可編修 TeX。
- Maintain the complete 50-chapter academic reading copy and the separate 全書易讀版 / Accessible Edition. Synchronize the relevant accessible chapter with each academic revision, using everyday examples and clear limits on claims.
  保存完整 50 章學術閱讀版及獨立「全書易讀版」；逐章修訂時同步易讀解說，使用生活例子並界定主張範圍。
- Revise one academic chapter per Taipei calendar day unless the user explicitly requests additional chapters. Preserve originals and prior immutable full backups. Include all reading editions, editable sources, assets, tools and editorial records in each new full backup.
  原則上每天台北曆日修訂一章，除非使用者明示加修。保留原始文件及歷次不可覆寫完整備份；新備份納入全部閱讀版、來源、資源、工具與編修紀錄。

## Placement of figures, proofs and code / 圖表、證明與程式配置

- Place essential conceptual diagrams, model architecture diagrams, principal result figures and tables in the main text near their first substantive discussion, with numbering and explanatory captions.
  理解論證所需的概念圖、模型架構圖及主要結果圖表放在正文首次實質討論附近，附編號及說明。
- Keep key formulas and proofs supporting core conclusions in the main text. Put lengthy derivations, supplementary proofs, sensitivity analyses and additional figures or tables in appendices with explicit references from the text.
  關鍵公式與支撐核心結論的證明放正文；冗長推導、補充證明、敏感度分析及額外圖表放附錄，正文清楚引用。
- Put algorithm steps or pseudocode needed to understand the method in the main text. Supply complete executable research code, dependencies, parameters and reproduction instructions as electronic supplementary material; explain the files and their purpose in an appendix.
  理解方法必需的演算法步驟或偽程式碼放正文。完整可執行研究程式、依賴環境、參數與重現步驟放電子補充資料，由附錄說明各檔用途。
- Put large datasets and full simulation outputs in electronic supplementary material or an appropriate repository, with provenance and access information in the text. Public upload or publication is a separate action, not implied by this placement rule.
  大型資料集與完整模擬輸出放電子補充資料或適當儲存庫，正文交代來源與取得方式。此編排規則本身不代表要求公開上傳或發表。

## Completeness and evidence / 齊備性與證據

- For each revised chapter, inventory its references to figures, tables, appendices, algorithms, code, data and simulations. Verify each referenced item actually exists, is locatable, has a consistent identifier and supports the associated statement. Record missing items and resolve or explicitly qualify the reference before reporting the chapter complete.
  每章盤點圖、表、附錄、演算法、程式、資料與模擬的引用。確認引用對象存在、可定位、編號一致且支持相關敘述。缺項須記錄，補齊或明示限定後才能回報完成。
- Do not present proposed simulations, illustrative scenarios or unexecuted code as empirical findings. Mark plans, assumptions, examples, unresolved proofs and verified results distinctly. Never invent results or fill a missing figure with fabricated data.
  未執行模擬、示意情境或未執行程式，不得寫成實證成果。區分研究方案、假設、例子、待解證明與已驗證結果；不得編造結果或用虛構資料補圖。
- Distinguish publishing/build/backup utilities from scientific simulation and validation code. An editing backup is not automatically a publication-ready supplementary package; organize and verify the latter separately as research artifacts become available.
  區分閱讀版建置／備份工具與科學模擬／驗證程式。編修備份不自動等於已整理完成的論文補充資料包；隨研究產物完成另行整理與驗證。
- Record what changed, what was checked and what remains unresolved in each daily log. Mathematical rendering success does not certify a proof or an empirical claim.
  每日日誌記錄修改、查核與未解項目。公式渲染成功，不等於證明或實證主張已獲認證。

## Single formula rendering / 公式單次呈現

Confirmed 2026-09-12: output one KaTeX HTML visual representation per formula in both reading editions. Do not emit a parallel MathML subtree or append duplicate plain-text formulas. Preserve editable TeX in source. Nonvisual labels must not appear as a second formula. This does not remove formulas legitimately used in separate English/Chinese paragraphs.

使用者要求每個公式僅呈現一次；兩種閱讀版均輸出單一 KaTeX HTML，不附平行 MathML 或重複文字公式。保留來源 TeX，非視覺標籤不得成為第二份可見公式。英中不同段落合理引用的公式不屬於此種重複。
