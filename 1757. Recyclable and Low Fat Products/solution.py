## 1757. Recyclable and Low Fat Products 可回收和低脂產品

# Table: Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | low_fats    | enum    |
# | recyclable  | enum    |
# +-------------+---------+

# product_id is the primary key (column with unique values) for this table.
# low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

# Product_id 為表格的 primary key （具有唯一值的欄位）
# low_fats 是一種 ENUM (類別)，其中 'Y' 表示為這個產品為低脂，'N' 則不為低脂產品
# recyclable 是一種 ENUM (類別)，其中 'Y' 表示這個產品可回收，'N' 則不能被回收

### 題目

# Write a solution to find the ids of products that are both low fat and recyclable.
# Return the result table in any order.
# The result format is in the following example.

### 中文

# 寫出一個解決方案來尋找低脂且可回收的產品 ID
# 以任意順序回傳結果
# 結果顯示如下

### Example 範例

# Input:
# Products table:
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+

# Output:
# +-------------+
# | product_id  |
# +-------------+
# | 1           |
# | 3           |
# +-------------+

### Explanation 解釋

# Only products 1 and 3 are both low fat and recyclable.
# 只有產品 1 跟 3 是低脂且可以被回收的

### Code 程式碼

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return df[["product_id"]]


# loc() 寫法
# 判斷是否為 'Y' 並回傳一個 DataFrame


# def find_products(products: pd.DataFrame) -> pd.DataFrame:
#     return products.query("low_fats == 'Y' and recyclable == 'Y'")[["product_id"]]

# query() 寫法
# 讀取來更直覺，更接近 SQL 與法
# 對於大規模的 DataFrame 性能會好一些，因為 query() 會優化解析


# def find_products(products: pd.DataFrame) -> pd.DataFrame:
#     return products[products.apply(lambda row: row["low_fats"] == "Y" and row["recyclable"] == "Y", axis=1)][["product_id"]]

# apply() 寫法
# 如果條件更複雜，可以更容易擴充
# 因為 apply() 會逐行運行，所以效能會比 loc() 還有 query() 差


# def find_products(products: pd.DataFrame) -> pd.DataFrame:
#     return products[(products["low_fats"].isin(["Y"])) & (products["recyclable"].isin(["Y"]))][["product_id"]]

# isin() 寫法
# 當有多個可能的值時， isin() 會很方便使用


# def find_products(products: pd.DataFrame) -> pd.DataFrame:
#     return products.filter(items=products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")].index)[["product_id"]]

# filter() 寫法
# 不建議使用，因為 filter() 適用於選擇欄位，而不是篩選，所以效能會較差
