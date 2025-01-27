## 1757. Recyclable and Low Fat Products 可回收和低脂產品

```py
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
```

product_id is the primary key (column with unique values) for this table.
Product_id 為表格的 primary key （具有唯一值的欄位）。

low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.

low_fats 是一種 ENUM (類別)，其中 'Y' 表示為這個產品為低脂，'N' 則不為低脂產品。

recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

recyclable 是一種 ENUM (類別)，其中 'Y' 表示這個產品可回收，'N' 則不能被回收。

Write a solution to find the ids of products that are both low fat and recyclable.

寫出一個解決方案來尋找低脂且可回收的產品 ID。

Return the result table in any order.

以任意順序回傳結果。

The result format is in the following example.

結果格式如下

---

### 範例

### Example 1:

```py
Input:
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+

Output:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
```

### Explanation 解釋:

Only products 1 and 3 are both low fat and recyclable.

只有產品 1 跟 3 是低脂且可以被回收的。

---

### Code

```py
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return df[["product_id"]]

# loc() 寫法
# 判斷是否為 'Y' 並回傳一個 DataFrame


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query("low_fats == 'Y' and recyclable == 'Y'")[["product_id"]]

# query() 寫法
# 讀取來更直覺，更接近 SQL 與法
# 對於大規模的 DataFrame 性能會好一些，因為 query() 會優化解析


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[products.apply(lambda row: row["low_fats"] == "Y" and row["recyclable"] == "Y", axis=1)][["product_id"]]

# apply() 寫法
# 如果條件更複雜，可以更容易擴充
# 因為 apply() 會逐行運行，所以效能會比 loc() 還有 query() 差


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"].isin(["Y"])) & (products["recyclable"].isin(["Y"]))][["product_id"]]

# isin() 寫法
# 當有多個可能的值時， isin() 會很方便使用


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.filter(items=products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")].index)[["product_id"]]

# filter() 寫法
# 不建議使用，因為 filter() 適用於選擇欄位，而不是篩選，所以效能會較差
```

## 2879. Display the First Three Rows 顯示前三行資料

```py
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

Write a solution to display the first 3 rows of this DataFrame.

撰寫一個解決方案來顯示此資料表的前三行資料。

---

### 範例

### Example 1:

```py
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

### Explanation 解釋:

Only the first 3 rows are displayed.

僅顯示資料表中的前三行資料。

---

### Code

```py
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]

# slice 切片寫法
# employees[:3] 為第 0 到 第 2 列


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# head() 寫法
# head() 從索引 0 開始
# head(3) 從索引 0 到第 3 個，即第 0 到第 2 列


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]

# iloc() 寫法
# iloc() 不包含最後索引
# iloc[0:3] 為第 0 到第 2 列


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]

# loc() 寫法
# loc() 會包含最後索引
# loc[0:2] 為第 0 到第 2 列


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.query('index < 3')

# query() 寫法
# query() 為條件篩選
# index < 3 為索引小於 3 的列


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.filter(items=range(3), axis=0)

# filter() 寫法
# filter() 搭配索引來選取前 3 列
# items=range(3)，表示選取第 0 到第 2 列
# axis=0 表示作用在列上


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.take([0, 1, 2])

# take() 寫法
# take() 接受一個索引列表，會根據索引來選取列。
```

## 2881. Create a New Column 建立一個新的列

```py
DataFrame employees
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+
```

A company plans to provide its employees with a bonus.

一間公司計畫給員工提供獎金。

Write a solution to create a new column name `bonus` that contains the doubled values of the `salary` column.

撰寫一個解決方案名為 `bonus` 的新列，值為 `salary` 的兩倍。

The result format is in the following example.

結果顯示如下。

### 範例

### Example 1:

```py
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+

Output:
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
```

### Explanation 解釋:

A new column bonus is created by doubling the value in the column salary.

建立名為 `bonus` 的新列並且值為 `salay` 的兩倍。

---

### Code

```py
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# 直觀且高效的操作，因為 Pandas 會對欄位進行向量化操作 (vectorized operations)
# 運算會比 apply() 或是迴圈更快


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"].apply(lambda x: x * 2)
    return employees

# apply() 寫法
# 可以在 lambda 加入條件判斷，所以會更靈活
# 因為 apply() 需要逐行處理，效能會較差


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=employees["salary"] * 2)

# assign() 寫法
# assign() 會返回一個新的 DataFrame，不會影響原本的內容
# 適用於鏈式操作 (method chaining)
# 如果希望直接修改原始 DataFrame 有其他的選擇


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.eval("bonus = salary * 2")

# eval() 寫法
# eval() 預設會回傳新的 DataFrame 所以可以直接 return
# eval() 可以解析字串，所以在處理複雜的數學運算會更直觀
# eval() 主要用於動態計算，所以可讀性較低
# 在大型 DataFrame 比 apply() 快
# 不適用於條件判斷


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.eval("bonus = salary * 2", inplace=True)
    return employees

# eval() 寫法
# eval() 預設會返回新的 DataFrame，所以需要加 inplace=True 來改變原始 DataFrame


import pandas as pd
import numpy as np

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = np.multiply(employees["salary"], 2)
    return employees

# 數值計算的效率更好，Numpy 的向量化計算比 Pandas 更快
# 適用於超大型 DataFrame
# 不夠直觀，因為 Pandas 本身已經內建向量化計算 (salary * 2)
```

## 2884. Modify Columns 修改欄位

```py
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
```

A company intends to give its employees a pay rise.

一間公司打算給員工加薪。

Write a solution to modify the salary column by multpylying each salary by 2.

攥寫一個解決方案來將每個薪資乘以 2。

The result format is in the following example.

結果格式如下。

---

### 範例

### Example 1:

```py
Input:

DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Ppyer   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+

Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Ppyer   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
```

### Explanation 解釋:

Every salary has been doubled.

每個薪資都被加倍了。

---

### Code

```py
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
     employees['salary'] = employees['salary'] * 2
     return employees


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x : x *2)
    return employees

# apply() 寫法
# apply() 接受 lambda 表達式，將每個值乘以 2


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, 'salary'] = employees.loc[:, 'salary'] * 2
    return employees

# loc() 寫法
# loc[:, 'salary'] 選取所有列的 salary 欄位


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary=employees['salary'] * 2)

# assign() 寫法
# assign() 會返回一個新的 DataFrame


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].mul(2)
    return employees

# mul() 寫法
# mul() 是 element-wise 的乘法運算。
# 效果跟 * 2 相同，但可以保持程式的一致性，尤其在有更多欄位運算。


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].transform(lambda x : x * 2)
    return employees

# transform() 寫法
# transform() 與 apply() 類似，但更適合用於 DataFrame 的欄位轉換


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.eval('salary = salary * 2', inplace = True)
    return employees

# eval() 寫法
# eval() 支援類似 SQL 的語法，可以對欄位直接進行操作
# inplace=True 表示修改原本的 DataFrame
```

## 2888. Reshape Data: Concatenate 重塑資料: 連接

```py
DataFrame df1
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame df2
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

Write a solution to concatenate these two DataFrames vertically into one DataFrame.

寫一個解決方案，將這兩個 DataFrame 垂直堆疊成一個 DataFrame。

The result format is in the following example.

結果格式如下。

---

### 範例

### Example 1:

```py
Input:

df1
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+

df2
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+

Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
```

### Explanation 解釋:

The two DataFramess are stacked vertically, and their rows are combined.

將兩個 DataFrame 垂直堆疊，並合併 rows。

---

### Code

```py
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

# concat() 寫法
# pd.concat() 預設會沿著 row 方向合併
# axis=0 表示垂直合


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.append(df2, ignore_index=True)

# append() 寫法
# Pandas 1.4.0 開始已停用此方法。
# append() 會直接將 df2 的資料附加到 df1 後面
# ignore_index=Ture 表示重新索引，避免索引重複


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(df1, df2, how='outer')

# merge() 寫法
# 通常用於 Key 的合併，也可以用於垂直合併
# merge() 會根據共同的欄位合併
# how="outer" 表示取兩個 DataFrame 的 Union (聯集，將兩個資料合併並保留所有的唯一值)


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.T.join(df2.T).T

# join() 寫法
# 通常用於橫向合併，但可以透過 T 轉置操作模擬垂直合併
# T 為轉置操作，可以將 DataFrame 的欄和列交換位置
# join() 會基於索引進行合併


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.combine_first(df2)

# combine_first() 寫法
# combine_first() 通常用於資料補充
# combine_first() 用來合併兩個 DataFrame，並且會優先保留第一個 DataFrame 的值
# combine_first() 會用 df1 的值填補 df2 的缺少值


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined = pd.concat([df1, df2])
    return combined.reset_index(drop=True)

# reindex() 寫法
# 合併兩個 DataFrame 重新排列索引，並移除原本的索引


import pandas as pd
import numpy as np

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined_array = np.vstack([df1.values, df2.values])
    return pd.DataFrame(combined_array, columns=df1.columns)

# NumPy 寫法
# NumPy 可以達到更底層的控制
# np.vstack() 將兩個陣列垂直合併
# 使用 pd.DataFrame() 將結果轉成 DataFrame
```
