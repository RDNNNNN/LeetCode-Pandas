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
#     employees['salary'] = employees['salary'].apply(lambda x : x *2)
#     return employees

# loc()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.loc[:, 'salary'] = employees.loc[:, 'salary'] * 2
#     return employees

# assign()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.assign(salary=employees['salary'] * 2)

# mul()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['salary'] = employees['salary'].mul(2)
#     return employees

# transform()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['salary'] = employees['salary'].transform(lambda x : x * 2)
#     return employees

# eval()
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.eval('salary = salary * 2', inplace = True)
#     return employees
