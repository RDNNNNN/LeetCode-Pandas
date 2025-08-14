## 1693. Daily Leads and Partners 每日商機和合作夥伴

```py
Table: DailySales
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+

There is no primary key (column with unique values) for this table. 
It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.

該表沒有 primary key (具有唯一值的列)

可能包含重複的值

此表格包含所售產品的日期和名稱以及銷售線索和合作夥伴的 ID

此名稱僅由小寫英文字母組成 
```

### 題目
 
For each `date_id` and `make_name`, find the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The result format is in the following example.

### 中文

對於每個 `date_id` 和 `make_name`，尋找不同的 `Lead_id` 和不同的 `Partner_id` 的數量

以任意順序傳回結果表

結果顯示如下

### Example 範例

```py 
Input: 
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+

Output: 
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+
```

### Explanation 解釋

For `2020-12-8`, toyota gets `leads = [0, 1]` and `partners = [0, 1, 2]` while honda gets `leads = [1, 2]` and `partners = [1, 2]`.

For `2020-12-7`, toyota gets `leads = [0]` and `partners = [1, 2]` while honda gets `leads = [0, 1, 2]` and `partners = [1, 2]`.

### 中文

對於 `2020-12-8`，豐田得到 `leads = [0, 1]` 和 `partners = [0, 1, 2]`，而本田得到 `leads = [1, 2]` 和 `partners = [1, 2]`

對於 `2020-12-7`，豐田得到 `leads = [0]` 和 `partners = [1, 2]`，而本田得到 `leads = [0, 1, 2]` 和 `partners = [1, 2]`

### Code 程式碼

```py
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(
        ["date_id", "make_name"]
    ).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()
```