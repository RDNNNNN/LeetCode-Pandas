## 1873. Calculate Special Bonus 計算特別獎金

# Table: Employees
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
# employee_id 為此表的主鍵 (具有唯一值的列)
# 該表的每一行 表示 員工 ID 員工姓名以及薪水

#### 題目
# Write a solution to calculate the bonus of each employee.
# The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character `M`.
# The bonus of an employee is `0` otherwise.
# Return the result table ordered by `employee_id`.
# The result format is in the following example.

#### 中文
# 寫一個解決方案計算每個員工的獎金
# 如果 `employee_id` 為奇數，並且員工的名字不是從角色 `M` 開始的，則員工的獎金是其薪資的 `100％`
# 員工的獎勵為 `0`
# 返回員工訂購的結果表
# 結果顯示如下

#### Example 範例
# Input:
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output:
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+

#### Explanation 解釋
# The employees with IDs 2 and 8 get 0 bonus because they have an even `employee_id`.
# The employee with ID 3 gets 0 bonus because their name starts with `M`.
# The rest of the employees get a 100% bonus.

#### 中文
# IDS 2 和 8 的員工獲得 0 獎金，因為他們的 `employee_id` 是偶數
# ID 3 的員工獲得 0 個獎勵，因為他們的名字以 `M` 開頭
# 其餘員工獲得 100％ 的獎金

#### Code 程式碼
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees["employee_id"] % 2 != 0) & (employees["name"].str[0] != "M")
    employees.loc[~mask, "salary"] = 0

    return (
        employees.drop(columns="name")
        .rename(columns={"salary": "bonus"})
        .sort_values(by="employee_id")
    )
