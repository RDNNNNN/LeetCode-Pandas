## 1667. Fix Names in a Table 修復表中的名稱

# Table: Users
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+

# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user.
# The name consists of only lowercase and uppercase characters.

# user_id 是此表的主鍵（具有唯一值的列）
# 該表包含用戶的 ID 和名稱
# 該名稱僅由小寫和大寫字符組成

### 題目

# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.
# The result format is in the following example.

### 中文

# 編寫解決方案來修復名稱，以便只有第一個字符是大寫，其餘的是小寫
# 返回由 `User_id` 排序的結果表
# 結果顯示如下

### Example 範例

# Input:
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+

# Output:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

### Code 程式碼

import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id")
