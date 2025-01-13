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

```py
import pandas as pd

# slice 切片
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]

# employees[:3] 為第 0 到 第 2 列


# head()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# head() 從頭到第幾個
# head(3) 從頭到第 3 個 ，即第 0 到第 2 列


# iloc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]

# iloc() 不包含最後索引
# iloc[0:3] 為第 0 到第 2 列


# loc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]

# loc() 會包含最後索引
# loc[0:2] 為第 0 到第 2 列


# query()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.query('index < 3')

# query() 為條件篩選
# index < 3 為索引小於 3 的列


# filter()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.filter(items=range(3), axis=0)

# filter()搭配索引來選取前 3 列
# items=range(3)，表示選取第 0 到第 2 列
# axis=0 表示作用在列上


# take()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.take([0, 1, 2])

# take() 接受一個索引列表，會根據索引來選取列。
```

## 2884. Modify Columns (修改欄位)

```python
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
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

```py
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
     employees['salary'] = employees['salary'] * 2
     return employees


# apply()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x : x *2)
    return employees

# apply() 接受 lambda 表達式，將每個值乘以 2


# loc()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, 'salary'] = employees.loc[:, 'salary'] * 2
    return employees

# loc[:, 'salary'] 選取所有列的 salary 欄位


# assign()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary=employees['salary'] * 2)

# assign() 會返回一個新的 DataFrame


# mul()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].mul(2)
    return employees

# mul() 是 element-wise 的乘法運算。
# 效果跟 * 2 相同，但可以保持程式的一致性，尤其在有更多欄位運算。


# transform()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].transform(lambda x : x * 2)
    return employees

# transform() 與 apply() 類似，但更適合用於 DataFrame的欄位轉換


# eval()
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.eval('salary = salary * 2', inplace = True)
    return employees

# eval() 支援類似 SQL 的語法，可以對欄位直接信行操作
# inplace=True 表示修改原本的 DataFrame
```
