## 627. Swap Salary 交換薪資

```py
Table: Salary
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM (category) value of type ('m', 'f').
The table contains information about an employee.

id 是此表的主鍵（具有唯一值的欄位）
性別列舉是列舉（類別）值，類型為 ('m', 'f')
該表包含有關員工的資訊
```

### 題目

Write a solution to swap all `'f'` and `'m'` values (i.e., change all `'f'` values to `'m'` and vice versa) with a **single update statement** and no intermediate temporary tables.

Note that you must write a single update statement, **do not** write any select statement for this problem.

The result format is in the following example.

編寫一個解決方案，使用**單一更新語句**交換所有“f”和“m”的值（即將所有“f”值變更為“m”，反之亦然），並且無需中間臨時表

請注意，您必須編寫單一更新語句，**請勿**為此問題編寫任何選擇語句

結果顯示如下

### Example 範例

```py
Input:
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
Output:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
```

### Explanation 解釋

(1, A) and (3, C) were changed from 'm' to 'f'.

(2, B) and (4, D) were changed from 'f' to 'm'.

### Code 程式碼

```py
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary[["sex"]] = salary[["sex"]].replace({"m":"f", "f":"m"})
    return salary
```