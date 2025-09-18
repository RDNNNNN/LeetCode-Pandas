## 1068. Product Sales Analysis I 產品銷售分析

# Table: Sales
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) is the primary key (combination of columns with unique values) of this table.
# product_id is a foreign key (reference column) to Product table.
# Each row of this table shows a sale on the product product_id in a certain year.
# Note that the price is per unit.
# (sale_id, year) 是此表的主鍵（具有唯一值的列的組合）
# product_id 是 Product 表的外鍵（引用列）
# 此表的每一行都顯示了特定年份產品 product_id 的銷售情況
# 請注意，價格是每單位的價格
# Table: Product
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the product name of each product.
# product_id 是此表的主鍵（具有唯一值的欄位）
# 此表的每一行表示每個產品的產品名稱


### 題目
# Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.
# Return the resulting table in any order.
# The result format is in the following example.

### 中文
# 編寫一個解決方案，報告 `Sales` 表中每個 `sale_id` 對應的 `product_name`、`year` 和 `price`
# 按任意順序傳回結果表
# 結果顯示如下

### Example 範例
# Input:
# Sales table:
# +---------+------------+------+----------+-------+
# | sale_id | product_id | year | quantity | price |
# +---------+------------+------+----------+-------+
# | 1       | 100        | 2008 | 10       | 5000  |
# | 2       | 100        | 2009 | 12       | 5000  |
# | 7       | 200        | 2011 | 15       | 9000  |
# +---------+------------+------+----------+-------+
# Product table:
# +------------+--------------+
# | product_id | product_name |
# +------------+--------------+
# | 100        | Nokia        |
# | 200        | Apple        |
# | 300        | Samsung      |
# +------------+--------------+
# Output:
# +--------------+-------+-------+
# | product_name | year  | price |
# +--------------+-------+-------+
# | Nokia        | 2008  | 5000  |
# | Nokia        | 2009  | 5000  |
# | Apple        | 2011  | 9000  |
# +--------------+-------+-------+

### Explanation 解釋
# From `sale_id = 1`, we can conclude that Nokia was sold for 5000 in the year 2008.
# From `sale_id = 2`, we can conclude that Nokia was sold for 5000 in the year 2009.
# From `sale_id = 7`, we can conclude that Apple was sold for 9000 in the year 2011.

### 中文
# 根據 `sale_id = 1`，我們可以得到 Nokia 在 2008 年的售價為 5000 台。
# 根據 `sale_id = 2`，我們可以得到 Nokia 在 2009 年的售價為 5000 台。
# 根據 `sale_id = 7`，我們可以得到 Apple 在 2011 年的售價為 9,000 台。

### Code 程式碼
import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product, on="product_id", how="inner")[
        ["product_name", "year", "price"]
    ]
