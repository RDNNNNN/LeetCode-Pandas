## **1378. Replace Employee ID With The Unique Identifier 用唯一識別碼替換員工 ID**

```python
Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

id 是此表的主鍵（具有唯一值的欄位）
此表的每一行都包含公司員工的 id 和姓名
```

```python
Table: EmployeeUNI
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

(id, unique_id) 是此表的主鍵（具有唯一值的欄位的組合）
此表的每一行都包含公司中員工的 ID 及其對應的唯一 ID
```

### 題目

Write a solution to show the **unique ID** of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

編寫一個解決方案，顯示每個使用者的**唯一 ID**。如果使用者沒有唯一 ID，則直接顯示 `null`

以**任意**順序傳回結果表

結果顯示如下

### **Example 範例**

```python
Input:
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+

Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
```

### Explanation 解釋

Alice and Bob do not have a unique ID, We will show null instead.

The unique ID of Meir is 2.

The unique ID of Winston is 3.

The unique ID of Jonathan is 1.

Alice 和 Bob 沒有唯一 ID，因此我們將顯示 null

Meir 的唯一 ID 為 2

Winston 的唯一 ID 為 3

Jonathan 的唯一 ID 為 1

### Code 程式碼

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, on="id", how="left")[["unique_id", "name"]] 
```