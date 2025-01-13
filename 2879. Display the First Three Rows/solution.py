# 2879. Display the First Three Rows (顯示前三行資料)

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


# slice 切片
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]


# employees[:3] 為第 0 到 第 2 列


# head()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.head(3)

# head() 從頭到第幾個
# head(3) 從頭到第 3 個 ，即第 0 到第 2列


# iloc()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.iloc[0:3]

# iloc() 不包含最後索引
# iloc[0:3] 為第 0 到第 2列


# loc()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.loc[0:2]

# loc() 會包含最後索引
# loc[0:2] 為第 0 到第 2列


# query()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.query('index < 3')

# query() 為條件篩選
# index < 3 為索引小於 3 的列


# filter()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.filter(items=range(3), axis=0)

# filter()搭配索引來選取前 3 列
# items=range(3)，表示選取第 0 到第 2 列
# axis=0 表示作用在列上


# take()
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.take([0, 1, 2])

# take() 接受一個索引列表，會根據索引來選取列。
