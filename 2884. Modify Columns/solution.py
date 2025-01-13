# 2884. Modify Columns (修改欄位)

#  DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.
# 一間公司打算給員工加薪
# Write a solution to modify the salary column by multiplying each salary by 2.
# 攥寫一個解決方案來將每個薪資乘以 2
# The result format is in the following example.
# 結果顯示如下

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+
# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# Explanation:
# Every salary has been doubled.

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees


# apply()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees["salary"] = employees["salary"].apply(lambda x: x * 2)
#     return employees

# apply() 接受 lambda 表達式，將每個值乘以 2


# loc()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.loc[:, "salary"] = employees.loc[:, "salary"] * 2
#     return employees

# loc[:, 'salary'] 選取所有列的 salary 欄位


# assign()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.assign(salary=employees["salary"] * 2)

# assign() 會返回一個新的 DataFrame


# mul()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees["salary"] = employees["salary"].mul(2)
#     return employees

# mul() 是 element-wise 的乘法運算。
# 效果跟 * 2 相同，但可以保持程式的一致性，尤其在有更多欄位運算。


# transform()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees["salary"] = employees["salary"].transform(lambda x: x * 2)
#     return employees

# transform() 與 apply() 類似，但更適合用於 DataFrame的欄位轉換


# eval()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.eval("salary = salary * 2", inplace=True)
#     return employees

# eval() 支援類似 SQL 的語法，可以對欄位直接信行操作
# inplace=True 表示修改原本的 DataFrame