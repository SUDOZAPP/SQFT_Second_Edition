# Chapter 6 electronic supplement / 第 6 章電子補充資料

Complete deterministic verification code accompanies Appendix 6.A. This is mathematical example verification, not social data, a fitted model or a stochastic simulation.

附錄 6.A 對應的完整確定性驗證程式。本資料用於數學例子驗證，不是社會資料、估計模型或隨機模擬。

## Files and reproduction / 檔案與重現

- verify_ch06.py: complete program / 完整程式。
- verification.json: recorded successful output / 實際成功執行的輸出。

Requires Python 3.12 or later, standard library only. Run in this directory:

需要 Python 3.12 以上，僅使用標準函式庫。在此目錄執行：

~~~text
python verify_ch06.py
~~~

Success prints JSON and exits with code zero. Failure raises an exception. The program writes no files and uses no network or random seed. Preserve the existing recorded output when saving a fresh run.

成功時輸出 JSON 並以狀態碼零結束，失敗則拋出例外。程式不寫檔、不使用網路或隨機種子；保存新結果時請保留現有執行紀錄。

## Checks / 檢查

Exact fractions verify the nonorthogonal counterexample (norm squared 197/125), the first-edition rounded formation norm (10041/10000), corrected formation probability sum, all entries of Table 6.1, two ensemble decompositions, a Bell-state partial trace and local probability identity, and a two-dimensional commutator with trace zero. Positivity of the table's two-dimensional matrices is checked using their principal minors.

精確分數驗證非正交反例（範數平方 197/125）、第一版捨入陣型範數（10041/10000）、修正後陣型機率總和、表 6.1 全部元素、兩種系綜分解、Bell 態偏跡與局部機率等式，以及跡為零的二維對易子。表中二維矩陣的半正定性以其主子式檢查。

Floating-point checks use five explicitly listed unit vectors and four global phases, compare phase-minimized squared distances and Hilbert–Schmidt identities, and check 125 sample ray triangles. Near zero, a distance tolerance of 1e-7 accounts for square-root cancellation; the other absolute tolerance is 1e-12. Two distinct imaginary coherences demonstrate why the two measurements in Table 6.1 do not perform complete state identification.

浮點檢查使用明列的五個單位向量與四種整體相位，比較相位最小化距離平方及 Hilbert–Schmidt 等式，並檢查 125 個射線三角形樣本。接近零時，以距離容許誤差 1e-7 處理平方根的相消誤差；其餘絕對容許誤差為 1e-12。兩個不同的虛部相干態展示表 6.1 的兩種測量為何不足以完整識別狀態。

The unitary example uses K equal to the two-dimensional bit-swap matrix, initial vector (1,0), and times 0, 0.25, 0.5, 1 and pi in units where the off-diagonal frequency is one. It checks the explicit solution against the differential equation, norm conservation, unitarity and density propagation. Entropy is checked on known spectra with base-two logarithms.

酉例子使用二維位元交換矩陣作為 K、初始向量 (1,0)，時間取 0、0.25、0.5、1 與 pi，單位使非對角頻率為一。以顯式解檢查微分方程、範數守恆、酉性與密度傳播。熵以已知譜及二為底的對數驗算。

Finite samples supplement the general proofs in the chapter and do not replace them. Book-building and backup tools are separate from this mathematical supplement.

有限樣本補充而不取代正文一般性證明。全書建置與備份工具有別於此數學補充資料。
