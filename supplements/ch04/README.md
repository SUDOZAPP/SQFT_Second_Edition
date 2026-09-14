# Chapter 4 supplementary algebra check / 第 4 章補充代數檢查

Purpose: reproduce the matrix identities and examples in Section 4.11 and the projection example in Section 4.6. This is research-supporting algebra code, distinct from HTML build tools. It is not an empirical simulation or a replacement for the general proofs.

用途：重現第 4.11 節矩陣恆等式與例子，以及第 4.6 節投影例子。這是輔助研究的代數程式，與 HTML 建置工具分開；不是實證模擬，也不取代一般證明。

Run from the extracted book folder:

```text
python supplements/ch04/verify_ch04.py
```

Python 3.12+; standard library only (`fractions`, `json`). No installation, input data, network, random seed or fitting is required. Output is JSON on standard output; `verification.json` records the executed result included in this edition.

需要 Python 3.12 以上，僅用標準函式庫；不需要安裝套件、輸入資料、網路、亂數種子或擬合。JSON 結果輸出至標準輸出，本版執行結果保存於 verification.json。

The joint basis is 00, 01, 10, 11. The initial diagonal is (1/2, 0, 0, 1/2). Scores are 1 on 00 and 11, and 0 otherwise. The replacement map uses sixteen matrix-unit Kraus operators divided by 2. Mixing weights are exactly 0, 1/4, 1/2 and 1, where w = exp(-gamma t); w=0 is the limiting replacement map. The generator check factors out gamma, so no numerical exponential or time unit is needed.

聯合基底為 00、01、10、11，初始對角為 (1/2, 0, 0, 1/2)。00 與 11 評分為 1，其餘為 0。替代映射採十六個矩陣單位除以 2 的 Kraus 算子。混合權重精確取 0、1/4、1/2、1，其中 w = exp(-gamma t)，w=0 是極限替代映射。生成元檢查提出 gamma 因子，不需數值指數或指定時間單位。

Expected scores: 1/2, 5/8, 3/4, 1 in that weight order. Checks use all sixteen real matrix units; the relevant linear identities extend to their complex span. State positivity is checked for the example's diagonal outputs; general complete positivity follows from the Kraus construction in the main proof. The script raises an error on a failed check, otherwise prints `status: passed`.

依上述權重順序，期望評分應為 1/2、5/8、3/4、1。檢查遍歷十六個實矩陣單位，相關線性恆等式延伸至其複線性張成空間。狀態正性檢查針對此例的對角輸出；一般完全正性由正文的 Kraus 建構證明。檢查失敗會報錯，成功则輸出 passed。
