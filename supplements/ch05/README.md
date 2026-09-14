# Chapter 5 electronic supplement / 第 5 章電子補充資料

This package verifies the worked binary shared-cue model in the revised Chapter 5. It is algebraic verification material, not empirical football data or a stochastic simulation.

本資料包驗算修訂第 5 章的二元共同線索模型，屬於代數驗證資料，不是足球實證資料或隨機模擬。

## Files / 檔案

- verify_ch05.py: complete executable verification code / 完整可執行驗證程式。
- verification.json: recorded successful run, including all parameter values and Table 5.1 / 實際通過的執行輸出，包含全部參數值與表 5.1。

## Reproduce / 重現

Requirements: Python 3.12 or later, standard library only. Run from this directory:

需求為 Python 3.12 以上，僅使用標準函式庫。在此目錄執行：

~~~text
python verify_ch05.py
~~~

The program prints JSON and exits with code zero on success. A failed check raises an exception and exits unsuccessfully. It does not write files. To save a new result without overwriting the archived run, redirect stdout to a new filename or capture it using a UTF-8-aware editor.

成功時程式輸出 JSON 並以狀態碼零結束；檢查失敗會拋出例外並以失敗狀態結束。程式不寫檔。若要保存新結果且保留存檔紀錄，可將標準輸出導向新檔名，或使用支援 UTF-8 的編輯器擷取。

## Method and scope / 方法與範圍

At each of eleven noise probabilities, from zero to one half in increments of one twentieth, enumerate all eight binary assignments of the fair shared cue and the two independent noise bits. Aggregate their exact rational probabilities into the four observed outcomes. Compare these with the derived law, normalization, marginals, alignment gain, conditional update and Chapter 4 depolarizing identity. Enumerate all four deterministic binary predictors to check the prediction optimum. Randomized rules are covered by the convexity argument in the main-text proof.

雜訊機率由零至二分之一，每次增加二十分之一，共十一個值。對各值枚舉公平共同線索與兩個獨立雜訊位元的八種配置，以精確有理數機率加總為四個觀察結果。將結果與正文推導的分布、正規化、邊際、方向一致增益、條件更新及第 4 章去極化等式比較。枚舉全部四個確定性二元預測器以檢查最優值；隨機規則則由正文證明的凸性論證處理。

All probability checks use fractions.Fraction. Entropy uses base-two floating-point logarithms and is compared in three expressions with absolute tolerance 1e-12. Zero-probability terms contribute zero. Table 5.1 uses exact fractions and is explicitly checked against the reported entries.

全部機率檢查使用 fractions.Fraction。熵使用以二為底的浮點對數，以絕對容許誤差 1e-12 比較三種表示式；零機率項貢獻為零。表 5.1 使用精確分數，並明確對照所列元素。

The finite grid is an implementation check, not a replacement for the general proofs in Sections 5.4–5.11. No external data, package installation, network access, random seed, coaching intervention or fitted research model is involved. The book's build and ZIP utilities are separate publishing tools.

有限網格用於檢查實作，不取代第 5.4–5.11 節的一般性證明。本程式不涉及外部資料、套件安裝、網路存取、隨機種子、教練介入或估計的研究模型。全書建置與 ZIP 工具屬於另外的出版工具。
