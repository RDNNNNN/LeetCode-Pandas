## 2890. Reshape Data: Melt 重塑數據：融解

```py
DataFrame report
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
```

### 題目

Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.

編寫一個解決方案來重塑數據，使每一行代表特定季度產品銷售資料

結果顯示如下
 
### Example 範例

```py
Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+

Output:
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
```

### Explanation 解釋

The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

DataFrame 從寬格式轉換為長格式

每行代表一個產品在一個季度的銷售額

### Code 程式碼

```py
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars="product",var_name="quarter",value_name="sales")
```