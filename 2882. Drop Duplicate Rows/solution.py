## 2882. Drop Duplicate Rows 刪除重複行

# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+

### 題目

# There are some duplicate rows in the DataFrame based on the email column.
# Write a solution to remove these duplicate rows and keep only the first occurrence.
# The result format is in the following example.

### 中文

# 根據電子郵件的列 (column)，DataFrame 存在一些重複的行 (rows)
# 撰寫一個解決方案來刪除重複的行 (rows) 並只保留第一個出現的行 (rows)
# 結果顯示如下

### Example 範例

# Input:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+

# Output:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+

### Explanation 解釋

# `Alic (customer_id = 4)` and `Finn (customer_id = 5)` both use `john@example.com`, so only the first occurrence of this email is retained.
# `Alic (customer_id = 4)` 跟 `Finn (customer_id = 5)` 都使用了 `john@example.com`，因此只保留第一個出現的電子郵件

### Code 程式碼

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"], keep="first")


# drop.duplicates() 寫法
# subset 為篩選欄位，keep 為重複值只保留第一筆資料


# import pandas as pd

# def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
#     return customers.groupby('email', as_index=False).first()

# groupby() 寫法
# groupby 會根據 email 進行分組
# as_index=False 會使 email 保持為一個欄位，因為預設為 True 會變成索引
# first() 會保留第一筆資料
