## 2881. Create a New Column 建立一個新的列

# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+

# A company plans to provide its employees with a bonus.

# 一間公司計畫給員工提供獎金

# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

# 撰寫一個解決方案名為 bonus 的新列，值為 salary 的兩倍

# The result format is in the following example.

# 結果顯示如下

### 範例

### Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+

# Output:
# +---------+--------+--------+
# | name    | salary | bonus  |
# +---------+--------+--------+
# | Piper   | 4548   | 9096   |
# | Grace   | 28150  | 56300  |
# | Georgia | 1103   | 2206   |
# | Willow  | 6593   | 13186  |
# | Finn    | 74576  | 149152 |
# | Thomas  | 24433  | 48866  |
# +---------+--------+--------+

### Explanation 解釋:

# A new column bonus is created by doubling the value in the column salary.
# 建立名為 bonus 的新列並且值為 salay 的兩倍。

### Code

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees


# 直觀且高效的操作，因為 Pandas 會對欄位進行向量化操作 (vectorized operations)
# 運算會比 apply() 或是迴圈更快


# import pandas as pd

# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees["bonus"] = employees["salary"].apply(lambda x: x * 2)
#     return employees

# apply() 寫法
# 可以在 lambda 加入條件判斷，所以會更靈活
# 因為 apply() 需要逐行處理，效能會較差


# import pandas as pd

# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.assign(bonus=employees["salary"] * 2)

# assign() 寫法
# assign() 會返回一個新的 DataFrame，不會影響原本的內容
# 適用於鏈式操作 (method chaining)
# 如果希望直接修改原始 DataFrame 有其他的選擇


# import pandas as pd

# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.eval("bonus = salary * 2")

# eval() 寫法
# eval() 預設會回傳新的 DataFrame 所以可以直接 return
# eval() 可以解析字串，所以在處理複雜的數學運算會更直觀
# eval() 主要用於動態計算，所以可讀性較低
# 在大型 DataFrame 比 apply() 快
# 不適用於條件判斷


# import pandas as pd

# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.eval("bonus = salary * 2", inplace=True)
#     return employees

# eval() 寫法
# eval() 預設會返回新的 DataFrame，所以需要加 inplace=True 來改變原始 DataFrame


# import pandas as pd
# import numpy as np

# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees["bonus"] = np.multiply(employees["salary"], 2)
#     return employees

# 數值計算的效率更好，Numpy 的向量化計算比 Pandas 更快
# 適用於超大型 DataFrame
# 不夠直觀，因為 Pandas 本身已經內建向量化計算 (salary * 2)
