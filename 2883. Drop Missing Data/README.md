## 2883. Drop Missing Data 刪除遺失的數據

```py
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
```

### 題目

There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

### 中文

根據電子郵件列，DataFrame 中存在一些重複的行

編寫一個解決方案來刪除這些重複的行並僅保留第一個出現的行

結果顯示如下

### Example 範例

```py 
Input:
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+

Output:  
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
```

### Explanation 解釋

Alice `customer_id = 4` and Finn `customer_id = 5` both use `john@example.com`, so only the first occurrence of this email is retained.

Alice `customer_id = 4` 和 Finn `customer_id = 5` 都使用  `john@example.com`，因此只有此電子郵件的第一次出現被保留

### Code 程式碼

```py
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
```