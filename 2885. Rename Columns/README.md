## 2885. Rename Columns 重新命名列

```py
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
```

### 題目

Write a solution to rename the columns as follows:

編寫解決方案來重新命名列，結果顯示如下：

```py
id to student_id
first to first_name
last to last_name
age to age_in_years
```

The result format is in the following example.

結果顯示如下

### Example 範例

```py
Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+

Output:
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
```

### Explanation 解釋

The column names are changed accordingly.

列名也隨之改變

### Code 程式碼

```py
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id":"student_id", "first":"first_name", "last": "last_name", "age": "age_in_years"})
```