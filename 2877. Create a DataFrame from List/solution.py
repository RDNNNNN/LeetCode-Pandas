## 2877. Create a DataFrame from List 從列表建立一個 DataFrame

# Write a solution to create a DataFrame from a 2D list called student_data.
# This 2D list contains the IDs and ages of some students.
# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
# The result format is in the following example.

# 撰寫一個解決方案，從名為 student_data 的 2D 列表建立一個 DataFrame
# 這個 2D 列表包含一些學生的 ID 和年齡
# DataFrame 應有兩個欄位: student_id 和 age，且順序與原始的 2D 列表相同
# 結果顯示如下

### Example 範例

# Input:
# student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]

# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+

### Explanation 解釋

# A DataFrame was created on top of student_data, with two columns named student_id and age.

# 在 student_data 之上建立一個 DataFrame，包含一個名為 student_id 和 age 的兩個欄位

### Code 程式碼

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


# 使用 pd.DataFrame() 轉成 DataFrame 並建立 student_id 跟 age 的欄位


# import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     data_dict = {
#         "student_id": [row[0] for row in student_data],
#         "age": [row[1] for row in student_data]
#     }
#     return pd.DataFrame(data_dict)

# 轉成 dict 再轉成 DataFrame
# 因為 student_data 是一個以 rows 為主的結構
# 但 dict 需要以 columns 為主的結構，所以需要將 rows 轉成 columns
# "student_id": [row[0] for row in student_data],  # 取出第一欄的所有值
#  "age": [row[1] for row in student_data]  # 取出第二欄的所有值


# import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     student_ids, ages = zip(*student_data)
#     return pd.DataFrame({"student_id": student_ids, "age": ages})

# zip() 寫法
# * 為解包運算符，將 student_data 這個 list of lists 拆開，讓 zip() 可以分別處理每一列的數據
# 當 *student_data 解包後，等於 zip([1, 15], [2, 11], [3, 11], [4, 20])
# zip(*) 更簡潔且效率高，因為 zip() 是 C 語言的內建函數，所以會比 for 迴圈還快


# import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     student_ids = list(map(lambda x: x[0], student_data))
#     ages = list(map(lambda x: x[1], student_data))
#     return pd.DataFrame({"student_id": student_ids, "age": ages})

# map() 寫法
# map() 搭配 lambda 表達式
# 因為 map() 回傳的結果會是一個 map object，它是一個 iterator (迭代器)，只有被迭代時才會產生結果，沒辦法直接被 pandas.DataFrame() 使用，所以需要轉成 list


# import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     return pd.DataFrame.from_records(student_data, columns=["student_id", "age"])

# from_records() 寫法
# from_records() 為 Pandas 官方推薦寫法之一，適用於 list of tuples 或 dict，list of lists 可以直接用 pd.DataFrame()
