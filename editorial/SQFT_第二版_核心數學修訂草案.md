# SQFT 第二版：核心數學修訂草案

版本：0.1，2026-09-08。本文為本輪審查提出的新草案，可用於重寫第一版第 4–7、12、17 章與第 5 章案例。它沒有證明第一版所有公理相容，也沒有宣稱社會系統必然遵循量子力學。下列基本結果屬於標準線性代數與量子資訊框架的應用，不能當作 SQFT 首次發現的數學定理。

## 1. 模型的範圍與資料意義

我們先研究一個有限維模型。設 \(\mathcal H=\mathbb C^d\)，\(d<\infty\)。模型狀態集合為

\[
\mathcal D(\mathcal H)=
\{\rho\in\mathbb C^{d\times d}:\rho=\rho^\dagger,
\rho\succeq0,\operatorname{Tr}\rho=1\}.
\tag{1}
\]

\(\rho\) 是模型對可觀測關係配置的統計表示。將某個資料集映射成 \(\rho\)，需要額外指定觀測規則及估計程序，並非從「社會是關係性的」這一句話就能唯一推出。

純態是 \(\rho=|\psi\rangle\langle\psi|\)，其中 \(\langle\psi|\psi\rangle=1\)。\(|\psi\rangle\) 與 \(e^{i\vartheta}|\psi\rangle\) 表示相同密度矩陣，因此本模型將兩者視為同一純態。

對有限結果集合 Y，選擇一組正半定效果算子
\[
E_y\succeq0,\quad \sum_{y\in Y}E_y=I,
\qquad p(y\mid\rho)=\operatorname{Tr}(\rho E_y).
\tag{2}
\]

每一個 \(E_y\) 必須對應可操作定義的記錄事件，例如兩位選手的路線選擇。式 (2) 給出合法機率，是因正性保證每項非負，完備性保證總和為 1；它本身沒有證明選手具有物理量子性。

若 \(\rho\) 與全部 \(E_y\) 在同一基底對角化，模型退化成通常的經典機率模型。使用非對角項或非交換觀測的必要性，需要以資料与模型比較另行論證。

對可觀測數值 \(a_y\)，可定義 \(O=\sum_y a_yE_y\)，則 \(E[a]=\operatorname{Tr}(\rho O)\)。資本、地位、協調成功等概念只有在測量尺度確定後，才可以與這些數值建立對應。

## 2. 五個基本命題與證明

### 命題 1：疊加向量的正確歸一化

設 \(|\psi_1\rangle,|\psi_2\rangle\) 均為單位向量，\(v=\alpha|\psi_1\rangle+\beta|\psi_2\rangle\)。則
\[
\|v\|^2=|\alpha|^2+|\beta|^2+
2\operatorname{Re}(\alpha^*\beta\langle\psi_1|\psi_2\rangle).
\tag{3}
\]
若 \(v\ne0\)，\(v/\|v\|\) 是單位向量。

**證明。** 直接展開 \(\langle v|v\rangle\)。兩個混合項互為共軛，相加即為式 (3) 最後一項。除以正的 \(\|v\|\) 後範數為 1。∎

因此，只有在交叉項消失時，\(|\alpha|^2+|\beta|^2=1\) 才是充分條件。最簡單的額外假設是 \(\langle\psi_1|\psi_2\rangle=0\)。

### 命題 2：條件投影更新保持密度矩陣條件

設 \(\rho\in\mathcal D(\mathcal H)\)、\(P=P^\dagger=P^2\)，且 \(p=\operatorname{Tr}(P\rho)>0\)。則
\[
\rho_P=\frac{P\rho P}{p}\in\mathcal D(\mathcal H).
\tag{4}
\]

**證明。** \((P\rho P)^\dagger=P\rho P\)。任取 v，有 \(v^\dagger P\rho Pv=(Pv)^\dagger\rho(Pv)\ge0\)。又由跡的循環性與 \(P^2=P\)，\(\operatorname{Tr}(P\rho P)=\operatorname{Tr}(P\rho)=p\)。除以正數 p 後保留 Hermitian 性与正性，且跡為 1。∎

若 \(p=0\)，條件態無定義。若不選取單一結果，應使用 \(\rho'=\sum_kP_k\rho P_k\)，其中投影兩兩正交、和為 I。這是與條件更新不同的操作。

更一般地，\(\mathcal E(\rho)=\sum_kK_k\rho K_k^\dagger\)、\(\sum_kK_k^\dagger K_k=I\) 定義 CPTP 通道，可表示非投影的更新。標準背景見 [Watrous，第 2 章](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf)。

### 命題 3：有限維定常 GKLS 模型的存在唯一性與保持性

設 \(G=G^\dagger\in\mathbb C^{d\times d}\)，以及有限個矩陣 \(L_1,\ldots,L_m\)。定義
\[
\mathcal L(\rho)=-i[G,\rho]
+\sum_{k=1}^m\left(L_k\rho L_k^\dagger
-\frac12\{L_k^\dagger L_k,\rho\}\right).
\tag{5}
\]
對每一初態 \(\rho_0\in\mathcal D(\mathcal H)\)，初值問題
\[
\dot\rho=\mathcal L(\rho),\qquad \rho(0)=\rho_0
\tag{6}
\]
有唯一全域解 \(\rho(t)=e^{t\mathcal L}\rho_0\)，且對所有 \(t\ge0\)，\(\rho(t)\in\mathcal D(\mathcal H)\)。

**證明。** 將矩陣元素視為有限維向量，式 (6) 是常係數線性 ODE，矩陣指數給出唯一全域解。

先證保跡。跡的循環性給出 \(\operatorname{Tr}[G,\rho]=0\)，且對每個 k，
\[
\operatorname{Tr}(L_k\rho L_k^\dagger)
=\operatorname{Tr}(L_k^\dagger L_k\rho)
=\frac12\operatorname{Tr}\{L_k^\dagger L_k,\rho\}.
\]
故 \(\operatorname{Tr}\mathcal L(\rho)=0\)，解的跡恆為 1。

再證完全正性。令 \(R=\sum_kL_k^\dagger L_k\)，對 \(h\ge0\) 定義
\[
K_0(h)=\exp[h(-iG-R/2)],\qquad K_k(h)=\sqrt h\,L_k,
\]
\[
\mathcal F_h(X)=K_0(h)XK_0(h)^\dagger+
\sum_kK_k(h)XK_k(h)^\dagger.
\]
這是 Kraus 形式，因此完全正；它不必在有限 h 下精確保跡。有限維 Taylor 展開給出
\(\mathcal F_h=\mathrm{Id}+h\mathcal L+O(h^2)\)。由有限維算子乘積極限，
\[
\lim_{n\to\infty}(\mathcal F_{t/n})^n=e^{t\mathcal L}.
\]
完全正映射的複合仍完全正，且有限維完全正映射集合在此極限下封閉，故 \(e^{t\mathcal L}\) 完全正。配合上面的保跡計算，它是 CPTP 通道，因而把初始密度矩陣映到密度矩陣。∎

**適用邊界。** 此證明限制在有限維、有限個定常矩陣。它沒有處理無界場算子、非 Markov 記憶或一般非線性回饋。GKLS 半群背景見 [Lindblad 的原論文](https://doi.org/10.1007/BF01608499)。

G 的單位是時間的倒數，L 的單位是時間的負二分之一次方。若保留第一版的 H 與 \(\hbar\)，設 \(G=H/\hbar\)。純社會模型也可直接使用速率生成元 G，避免沒有量綱定義的物理常數。

### 命題 4：獨立子系統的複合通道與演化

設 \(\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B\)，且 \(\mathcal E_A\)、\(\mathcal E_B\) 為 CPTP 通道。則 \(\mathcal E_A\otimes\mathcal E_B\) 也是 CPTP 通道。若兩系統分別作酉演化，聯合演化為 \(U_A\otimes U_B\)。

**證明。** 設兩通道的 Kraus 算子分別為 \(A_j\) 與 \(B_k\)。複合通道的 Kraus 算子為 \(A_j\otimes B_k\)，且
\[
\sum_{j,k}(A_j\otimes B_k)^\dagger(A_j\otimes B_k)
=\left(\sum_jA_j^\dagger A_j\right)\otimes
\left(\sum_kB_k^\dagger B_k\right)=I_A\otimes I_B.
\]
故完全正且保跡。酉情形是各只有一個 Kraus 算子的特例。∎

「獨立」在此指演化機制沒有交互作用，不要求聯合初態一定是乘積態。若初態有關聯，局部通道也可以作用在該聯合態上。

### 命題 5：單一局部邊際不足以決定一般聯合觀測

存在不同的聯合純態，其 A 與 B 邊際皆相同，但某一聯合觀測的機率不同。

**證明。** 在 \(\mathbb C^2\otimes\mathbb C^2\) 中令
\[
|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2,\qquad
|\Psi^+\rangle=(|01\rangle+|10\rangle)/\sqrt2.
\tag{7}
\]
直接取偏跡可得，兩個態的 A、B 邊際均為 \(I/2\)。令
\[
Q_{\rm same}=|00\rangle\langle00|+|11\rangle\langle11|.
\]
在第一個聯合態，\(\operatorname{Tr}(\rho Q_{\rm same})=1\)；在第二個聯合態，該值為 0。任何只依賴單一邊際的函數，都無法同時給出這兩個不同答案。∎

這證明的是聯合統計無法由局部邊際普遍恢復，不是對「最優傳球策略」的普遍定理。其實經典相關分布也有同樣的局部不足現象，因此此命題不能當作非經典模型必要性的證據。

## 3. 可完整計算的二元關係協調案例

### 3.1 狀態與觀測

設 A、B 各有兩個路線標籤 0 與 1，聯合基底依序為 \(00,01,10,11\)。我們只把「選擇相同標籤」當作一個協調指標；是否在實際比賽中有利，要另用結果資料判定。

初始狀態為
\[
\rho_0=\tfrac12|00\rangle\langle00|+
\tfrac12|11\rangle\langle11|.
\tag{8}
\]
這是可分離、對角的經典相關態。兩個邊際皆為 \(I/2\)，且
\[
S(\rho_A)=S(\rho_B)=\ln2,\quad
S(\rho_0)=\ln2,\quad I(A:B)=\ln2.
\]
因此，高互資訊與完全匹配可以出現在沒有糾纏的模型中。

### 3.2 演化與精確解

令 \(X=\begin{pmatrix}0&1\\1&0\end{pmatrix}\)、\(X_B=I\otimes X\)。取 \(G=0\)、單一跳躍算子 \(L=\sqrt\gamma X_B\)，其中 \(\gamma\ge0\)。式 (5) 化為
\[
\dot\rho=\gamma(X_B\rho X_B-\rho).
\tag{9}
\]
這是一個經典隨機翻轉 B 標籤的 GKLS 表示。

令 \(\mathcal X(\rho)=X_B\rho X_B\)，則 \(\mathcal X^2=\mathrm{Id}\)。因此
\[
e^{\gamma t(\mathcal X-\mathrm{Id})}
=\frac{1+e^{-2\gamma t}}2\mathrm{Id}
+\frac{1-e^{-2\gamma t}}2\mathcal X.
\tag{10}
\]
這可由把指數展開成偶次与奇次冪，或直接微分核對得到。兩個係數非負、和為 1，所以也是兩個酉通道的凸組合。

設 \(q(t)=(1+e^{-2\gamma t})/2\)，得到
\[
\rho(t)=\operatorname{diag}
\left(\frac{q(t)}2,\frac{1-q(t)}2,
\frac{1-q(t)}2,\frac{q(t)}2\right).
\tag{11}
\]
可直接檢查所有對角元素非負、總和為 1，並且滿足式 (9) 與初始條件。

### 3.3 可核查的預測

\[
P(A=B;t)=q(t),\qquad
I(A:B;t)=\ln2-h_2(q(t)),
\tag{12}
\]
其中 \(h_2(q)=-q\ln q-(1-q)\ln(1-q)\)。其推導如下：邊際仍均勻，聯合熵為 \(\ln2+h_2(q)\)，代入互資訊定義即得。

當 \(\gamma>0\)，匹配機率由 1 趨近 1/2，互資訊由 \(\ln2\) 趨近 0。當 \(\gamma=0\)，狀態不變。這是所選模型的數學結果；它並未證明實際足球協調一定指數衰退。

此例可以作為第二版第一個完整工作模型：它具備狀態、觀測、參數、動力學、精確解與可否證的預測。模型很小，正好便於檢查每個環節。

### 3.4 最小估計設計與比較

若在預先定義的同類情境、固定延遲 t 下收集 n 次可視為獨立的配對觀測，匹配次數 m 可建模為 \(\operatorname{Binomial}(n,q(t))\)。獨立性與共同初始條件是額外取樣假設；真實同一場比賽的連續觀測通常需時間序列處理。

可用不同 t 的匹配頻率估計 \(\gamma\)，並以保留資料檢查式 (12)。比較基線至少包括：常數匹配率、經典二元 Markov 模型、帶共同情境變數的機率模型。因為本例完全等价於經典隨機翻轉模型，它本身沒有提供非對角或非交換表示的優勢。

若要使用真正非交換的擴充，應事先說明額外觀測與可識別參數，而不是把無法直接觀測的非對角項當作已量測的社會事實。

## 4. 可替換第一版定理 20.1 的受限定理

### 有界交互作用的有限時間 Dyson 收斂

設 \(\mathcal H=\mathbb C^d\)，\(\hbar>0\)，\(V_I:[0,T]\to\mathbb C^{d\times d}\) 為可積矩陣函數，並令
\[
K_T=\frac1\hbar\int_0^T\|V_I(s)\|ds<\infty.
\]
考慮交互作用圖像的 Dyson 級數
\[
U_I(T)=I+\sum_{n=1}^{\infty}
\left(-\frac i\hbar\right)^n
\int_{0\le t_n\le\cdots\le t_1\le T}
V_I(t_1)\cdots V_I(t_n)\,dt_n\cdots dt_1.
\tag{13}
\]
此級數在算子範數下絕對收斂。保留到 m 階時，餘項滿足
\[
\|R_m(T)\|\le\sum_{n=m+1}^{\infty}\frac{K_T^n}{n!}
\le e^{K_T}\frac{K_T^{m+1}}{(m+1)!}.
\tag{14}
\]

**證明。** 由算子範數的次乘性，第 n 項範數不超過有序積分區域上的 \(\prod_j\|V_I(t_j)\|/\hbar\) 積分。此非負純量被積函數對全部時間变量對稱，單純形積分等於整個立方體積分的 \(1/n!\)，因此上界為 \(K_T^n/n!\)。指數級數保證絕對收斂與第一個餘項不等式。對 \(n=m+1+r\)，利用 \((m+1+r)!\ge(m+1)!r!\)，求和得到第二個上界。∎

此定理不需要 \(\|H_{\rm int}\|<\|H_0\|\)。若 V 含耦合參數 g，則 \(K_T\) 會隨 \(|g|\) 及觀測時間增長；因此小耦合和長時間必須一起評估。這沒有解決無界算子或一般 QFT 微擾的收斂問題。

## 5. 納入第二版前的編輯規則

上述命題只宣稱所列條件下的數學結論。把它們用於某個社會情境時，應增加一段獨立的「操作化与限制」，包括變數如何得到、估計哪些參數、哪些觀測支持或反對模型。

第一版的「八公理」可先拆為模型定義与研究立場；本草案中的有限維核心已有明確例子見證非空性。要加入連續場、局域規範、拓撲變化、Fock 空間或高階範疇，應另給接口与條件，逐一確認能否與核心共同成立。

本草案是一份可編輯的中文數學基礎稿。雙語對照、與分卷原證明的比對、完整參考文獻与第二版正式排版尚待後續修訂。
