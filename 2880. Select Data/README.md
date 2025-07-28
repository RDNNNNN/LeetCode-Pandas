## 2880. Select Data 篩選數據

```py 
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

### 題目

Write a solution to select the name and age of the student with `student_id = 101`.

The result format is in the following example.

撰寫一個解決方案，選取 `student_id = 101` 的名字跟年齡

結果顯示如下

### Example 範例:

```py 
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+

Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
```

### Explanation 解釋

Student Ulysses has `student_id = 101`, we select the `name` and `age`.

學生 Ulysses 的 `student_id = 101`，我們篩選此 `name` 跟 `age`

### Code 程式碼

```py 
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student_result = students[students["student_id"] == 101]
    return student_result[["name","age"]]
    
# students["student_id"] == 101 會產生 Series
# students[students["student_id"] == 101] 所以需要再加一層轉成 DataFrame
# 篩選 name 和 age 欄位並回傳

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
students_result = students.query("student_id == 101")
    return students_result[["name","age"]]

# query() 寫法
# query() 語法較接近 SQL 語法而且可以處理更複雜的條件


import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101], ["name", "age"]

# loc[] 寫法
# 如果要篩選欄位，需要使用 , 來隔開

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101].filter(items=["name", "age"])

# filter() 寫法
# filter() 用 items 篩選欄位
```