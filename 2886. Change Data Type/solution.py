## 2886. Change Data Type 改變資料型別

# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+

### 題目

# Write a solution to correct the errors:
# The grade column is stored as floats, convert it to integers.
# The result format is in the following example.

### 中文

# 撰寫一個解決方案來修正錯誤
# 成績列 (column) 為浮點數，將其轉為整數
# 結果顯示如下

### Example 範例

# Input:
# DataFrame students:
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73.0  |
# | 2          | Kate | 15  | 87.0  |
# +------------+------+-----+-------+

# Output:
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73    |
# | 2          | Kate | 15  | 87    |
# +------------+------+-----+-------+

### Explanation 解釋

# The data types of the column grade is converted to int.

# 將 grade 列 (column) 的資料型別轉換為 int

### Code 程式碼

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students


# astype() 寫法
# 適用全部都是數字的情況，但如果有 NaN 會報錯


# import pandas as pd

# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students["grade"] = pd.to_numeric(students["grade"], downcast="integer")
#     return students

# pd.to_numeric() 寫法
# pd.to_numeric() 可以處理 NaN
# downcast="integer" 轉成最小的整數類型(int8, int16, int32)
# NaN 可能會轉成浮點數


# import pandas as pd

# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students["grade"] = students["grade"].apply(int)
#     return students

# apply() 寫法
# 適用單獨轉換某一列數據，而不影響 DataFrame 的其他部份
# 如果有 NaN 會報錯，需要先使用 fillna(0) 填補缺失值


# import pandas as pd

# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students["grade"] = students["grade"].round(0).astype(int)
#     return students

# 在需要四捨五入的時候可以使用 round()
# 如果不需要數據改變，就不該使用


# import pandas as pd

# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students["grade"] = students["grade"].fillna(0).astype(int)
#     return students

# 如果有 NaN 可以使用 fillna() 填補缺失值
