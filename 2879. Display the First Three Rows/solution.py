# 2879. Display the First Three Rows
# 顯示前三行資料

# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.
# 撰寫一個解決方案來顯示此資料表的前三行資料。

# Example 1:

# Input:
# DataFrame employees
# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  |
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+
# Output:
# +-------------+---------+-------------+--------+
# | employee_id | name    | department  | salary |
# +-------------+---------+-------------+--------+
# | 3           | Bob     | Operations  | 48675  |
# | 90          | Alice   | Sales       | 11096  |
# | 9           | Tatiana | Engineering | 33805  |
# +-------------+---------+-------------+--------+
# Explanation:
# Only the first 3 rows are displayed.
# 僅顯示資料表中的前三行資料。

# Code
import pandas as pd


# slice
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]


# head()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.head(3)


# iloc()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.iloc[0:3]

# loc()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.loc[0:2]


# query()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.query('index < 3')

# filter()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.filter(items=range(3), axis=0)

# take()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.take([0, 1, 2])
