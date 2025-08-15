## 177. Nth Highest Salary 第 N 高薪

# Table: Employee
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
# id 是此表的主鍵（具有唯一值的欄位）
# 此表的每一行都包含有關員工薪資的資訊

### 題目
# Write a solution to find the `nth` highest distinct salary from the `Employee` table.
# If there are less than `n`` distinct salaries, return `null`.
# The result format is in the following example.

### 中文
# 寫一個解決方案，從員工表 `Employee` 中找出第 `n` 個最高不同的薪資
# 如果不同的薪資少於 `n` 個，則傳回 `null`
# 結果顯示如下

### Example 1 範例
# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+

### Example 2 範例
# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

### Code 程式碼
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    if len(sorted_salaries) < N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        return pd.DataFrame(
            {f"getNthHighestSalary({N})": [sorted_salaries.iloc[N - 1]]}
        )
