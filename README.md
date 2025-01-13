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

````python
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
# head(3) 從頭到第 3 個 ，即第 0 到第 2列

# iloc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]

# iloc() 不包含最後索引
# iloc[0:3] 為第 0 到第 2列

# loc()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]

# loc() 會包含最後索引
# loc[0:2] 為第 0 到第 2列

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
````

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

```python
import pandas as pd
# concat()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

# pd.concat() 預設會沿著 row 方向合併
# axis=0 表示垂直合


# append()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.append(df2, ignore_index=True)

# Pandas 1.4.0 開始已停用此方法。
# append() 會直接將 df2 的資料附加到 df1 後面
# ignore_index=Ture 表示重新索引，避免索引重複


# merge()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(df1, df2, how='outer')

# 通常用於 Key 的合併，也可以用於垂直合併
# merge() 會根據共同的欄位合併
# how="outer" 表示取兩個 DataFrame 的 Union (聯集，將兩個資料合併並保留所有的唯一值)


# join()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.T.join(df2.T).T
# 通常用於橫向合併，但可以透過 T 轉置操作模擬垂直合併
# T 為轉置操作，可以將 DataFrame 的欄和列交換位置
# join() 會基於索引進行合併


# combine_first()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.combine_first(df2)

# 通常用於資料補充
# combine_first() 用來合併兩個 DataFrame，並且會優先保留第一個 DataFrame 的值
# combine_first() 會用 df1 的值填補 df2 的缺少值


# reindex()
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined = pd.concat([df1, df2])
    return combined.reset_index(drop=True)

# 合併兩個 DataFrame 重新排列索引，並移除原本的索引


# numpy
import numpy as np

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined_array = np.vstack([df1.values, df2.values])
    return pd.DataFrame(combined_array, columns=df1.columns)

# numpy 可以達到更底層的控制
# np.vstack() 將兩個陣列垂直合併
# 使用 pd.DataFrame() 將結果轉成 DataFrame
```
