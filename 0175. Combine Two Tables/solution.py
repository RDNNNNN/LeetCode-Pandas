## **175. Combine Two Tables 合併兩個表**

# Table: `Person`
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName   | varchar |
# +-------------+---------+
# personId is the primary key (column with unique values) for this table.
# This table contains information about the ID of some persons and their first and last names.
# personId是該表的主鍵（唯一識別列）
# 表格包含一些人員的ID以及他們的姓名資訊
# Table: `Address`
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+
# addressId is the primary key (column with unique values) for this table.
# Each row of this table contains information about the city and state of one person with ID = PersonId.
# addressId是該表的主鍵（唯一識別列）。
# 該表中的每一行記錄都包含了一個ID為PersonId的使用者的城市和州資訊。

### 題目
# Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.
# Return the result table in **any order**.
# The result format is in the following example.
# 寫一個查詢語句，從 `Person` 表中取得每個人的姓名、城市和州資訊
# 如果 `Person` 表中某個人的 `personId` 在 `Address` 表中找不到對應的位址信息，則該位址資訊顯示為 `null`
# 傳回結果表時，結果順序不限
# 結果顯示如下

### **Example 範例**
# Input:
# Person table:
# +----------+----------+-----------+
# | personId | lastName | firstName |
# +----------+----------+-----------+
# | 1        | Wang     | Allen     |
# | 2        | Alice    | Bob       |
# +----------+----------+-----------+
# Address table:
# +-----------+----------+---------------+------------+
# | addressId | personId | city          | state      |
# +-----------+----------+---------------+------------+
# | 1         | 2        | New York City | New York   |
# | 2         | 3        | Leetcode      | California |
# +-----------+----------+---------------+------------+
# Output:
# +-----------+----------+---------------+----------+
# | firstName | lastName | city          | state    |
# +-----------+----------+---------------+----------+
# | Allen     | Wang     | Null          | Null     |
# | Bob       | Alice    | New York City | New York |
# +-----------+----------+---------------+----------+

### Explanation 解釋
# There is no address in the address table for the `personId = 1` so we return null in their city and state.
# `addressId = 1` contains information about the address of `personId = 2`.
# 地址表中沒有與 `personId=1` 對應的地址訊息，因此我們傳回該使用者的城市和州資訊為空
# 而 `addressId=1` 記錄的是 `personId=2` 對應的地址資訊

### Code 程式碼
import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, on="personId", how="left")[
        ["firstName", "lastName", "city", "state"]
    ]
