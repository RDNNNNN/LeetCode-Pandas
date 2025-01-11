## 2879. Display the First Three Rows (顯示前三行資料)

```python
DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
```

### Write a solution to display the first 3 rows of this DataFrame.

### 撰寫一個解決方案來顯示此資料表的前三行資料。

---

### Example 1:

```python
Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
Output:
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
```

### Explanation:

### Only the first 3 rows are displayed.

### 僅顯示資料表中的前三行資料。

## Code

```python
import pandas as pd

# slice
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]

# head()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# iloc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]

# loc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]

# query()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.query('index < 3')

# filter()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.filter(items=range(3), axis=0)

# take()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.take([0, 1, 2])
```

## 2884. Modify Columns

```python
DataFrame employees
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| name | object |
| salary | int |
+-------------+--------+
```

### A company intends to give its employees a pay rise.

### 一間公司打算給員工加薪。

### Write a solution to modify the salary column by multiplying each salary by 2.

### 攥寫一個解決方案來將每個薪資乘以 2。

### The result format is in the following example.

### 結果顯示如下

---

### Example 1:

```python
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
```

### Explanation:

### Every salary has been doubled.

### 每個薪資都被加倍了。

## Code

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
     employees['salary'] = employees['salary'] * 2
     return employees

# apply()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x : x *2)
    return employees

# loc()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, 'salary'] = employees.loc[:, 'salary'] * 2
    return employees

# assign()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary=employees['salary'] * 2)

# mul()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].mul(2)
    return employees

# transform()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].transform(lambda x : x * 2)
    return employees

# eval()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.eval('salary = salary * 2', inplace = True)
    return employees
```
