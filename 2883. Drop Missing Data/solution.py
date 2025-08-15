## 2883. Drop Missing Data 刪除遺失的數據

# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

### 題目
# There are some rows having missing values in the `name` column.
# Write a solution to remove the rows with missing values.
# The result format is in the following example.

### 中文
# `name` 欄中有一些行存在缺失值
# 編寫一個解決方案來刪除這些缺失值的行
# 結果顯示如下

### Example 範例
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+

### Explanation 解釋
# Student with id 217 havs empty value in the name column, so it will be removed.
# ID 為 217 的學生在姓名欄位中有一個空值，因此它將被刪除

### Code 程式碼
import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
