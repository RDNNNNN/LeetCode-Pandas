## **2889. Reshape Data: Pivot 重塑數據: 透視**

# DataFrameweather
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | city        | object |
# | month       | object |
# | temperature | int    |
# +-------------+--------+

### 題目
# Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.
# The result format is in the following example.
# 編寫一個解決方案來對資料進行**透視**，使每一行代表特定月份的溫度，每個城市作為單獨的列
# 結果顯示如下

### Example 範例
# Input:
# +--------------+----------+-------------+
# | city         | month    | temperature |
# +--------------+----------+-------------+
# | Jacksonville | January  | 13          |
# | Jacksonville | February | 23          |
# | Jacksonville | March    | 38          |
# | Jacksonville | April    | 5           |
# | Jacksonville | May      | 34          |
# | ElPaso       | January  | 20          |
# | ElPaso       | February | 6           |
# | ElPaso       | March    | 26          |
# | ElPaso       | April    | 2           |
# | ElPaso       | May      | 43          |
# +--------------+----------+-------------+
# Output:
# +----------+--------+--------------+
# | month    | ElPaso | Jacksonville |
# +----------+--------+--------------+
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March    | 26     | 38           |
# | May      | 43     | 34           |
# +----------+--------+--------------+

### Explanation 解釋
# The table is pivoted, each column represents a city, and each row represents a specific month.
# 該表是透視表，每列代表一個城市，每行代表一個特定的月份

### Code 程式碼
import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index=["month"], columns="city", values="temperature")
