# Winner-take-all-learning-rule
> 一種採用「**競爭式學習法**」的「**單層類神經網路**」，屬於「**非監督式學習**」，有時也被稱為 Kohonen learning rule。
以下為演算法的步驟
## A. 競爭階段( Competitive phase ) - 選出得勝者( winner )
如何衡量得勝者會影響整個分類結果，主要有三種方法
## B. 獎勵階段( Reward phase ) - 調整「得勝者」鍵結值
## C. 疊代階段( Iteration phase ) - 檢查停止訓練條件是否吻合
簡而言之就是決定訓練如何停止，只主要有以下二方法：
1. 鍵結值的改變量小於一固定閥值，訓練停止，反之繼續
2. 設定Epoch
