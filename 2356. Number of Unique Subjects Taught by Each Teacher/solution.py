## 2356. Number of Unique Subjects Taught by Each Teacher 每位教師教授的獨特科目數量

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | teacher_id  | int  |
# | subject_id  | int  |
# | dept_id     | int  |
# +-------------+------+

# (subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.

# subject_id 跟 dept_id 為表格的 primary key (具有唯一值的列組合)

# Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

# 該表中的每一行 (row) 具有 teacher_id 的教師以及科目 subject_id 還有系所 dept_id

# Write a solution to calculate the number of unique subjects each teacher teaches in the university.

# 撰寫一個解決方案來計算每個老師在大學教授的唯一科目數量

# Return the result table in any order

# 回傳任意順序的結果

# The result format is shown in the following example.

# 結果格式如下

### Example 範例:

# Input:
# Teacher table:
# +------------+------------+---------+
# | teacher_id | subject_id | dept_id |
# +------------+------------+---------+
# | 1          | 2          | 3       |
# | 1          | 2          | 4       |
# | 1          | 3          | 3       |
# | 2          | 1          | 1       |
# | 2          | 2          | 1       |
# | 2          | 3          | 1       |
# | 2          | 4          | 1       |
# +------------+------------+---------+

# Output:
# +------------+-----+
# | teacher_id | cnt |
# +------------+-----+
# | 1          | 2   |
# | 2          | 4   |
# +------------+-----+

### Explanation 解釋:

# Teacher 1:
#   - They teach subject 2 in departments 3 and 4.
#   - 他們在第 3 系所跟第 4 系所教授第 2 科目
#   - They teach subject 3 in department 3.
#   - 他們在第 3 系所教授第 3 科目
# Teacher 2:
#   - They teach subject 1 in department 1.
#   - 他們在第 1 系所教授第 1 科目
#   - They teach subject 2 in department 1.
#   - 他們在第 1 系所教授第 2 科目
#   - They teach subject 3 in department 1.
#   - 他們在第 1 系所教授第 3 科目
#   - They teach subject 4 in department 1.
#   - 他們在第 1 系所教授第 4 科目

### Code

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    df.columns = ["teacher_id", "cnt"]
    return df


# groupby() 寫法
# 會根據 teacher_id 進行分組
# groupby() 預設會使欄位成為索引，as_index=False 確保 teacher_id 為普通欄位
# nunique() 會計算 subject_id 的唯一值數量
# 最後將計算後的 subject_id 改為 cnt


# import pandas as pd

# def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
#     unique_subjects = teacher[['teacher_id', 'subject_id']].drop_duplicates()
#     df = unique_subjects.groupby('teacher_id', as_index=False).size()
#     df.columns = ['teacher_id', 'cnt']
#     return df

# drop_duplicates() 寫法
# drop_duplicates() 篩選重複的值
# groupby() 依照 teacher_id 分組
# size() 計算 teacher_id 有幾筆紀錄
# 最後將 size 更改為 cnt
