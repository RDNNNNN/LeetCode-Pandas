## 1741. Find Total Time Spent by Each Employee 找出每位員工花費的總時間

```py
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
```

### 題目

(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.

The table shows the employees' entries and exits in an office.

event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.

in_time and out_time are between `1` and `1440`.

It is guaranteed that no two events on the same day intersect in time, `and in_time < out_time`.

Write a solution to calculate the total time in minutes spent by each employee on each day at the office.

Note that within one day, an employee can enter and leave more than once.

The time spent in the office for a single entry is `out_time - in_time`.

Return the result table in any order

The result format is in the following example.

### 中文

`emp_id` 跟 `event_day` 還有 `in_time` 為該表格的 primary key (具有唯一值的列組合)

該表格顯示了員工進入辦公室以及離開辦公室的狀況

`event_day` 是發生的日期，`in_time` 為進入辦公室的時間，`out_time` 則是離開辦公室的時間

`in_time` 跟 `out_time` 介於 `1` 到 `1440` 之間

確保同一天沒有兩個事件的重複，而且 `in_time < out_time`

撰寫一個解決方案來計算員工每天在辦公室的時間(以分鐘為單位)，

請注意，在一天之內一名員工可以多次進入和離開

`time spent` 為辦公室花費的時間，計算方式為 `out_time - in_time`

回傳任意順序的結果

結果顯示如下

---

### Example 範例:

```py
Input:
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+

Output:
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
```

### Explanation 解釋:

Employee 1 has three events: 

two on day 2020-11-28 with a total of `(32 - 4) + (200 - 55) = 173`, and one on day 2020-12-03 with a total of `(42 - 1) = 41`.

Employee 2 has two events: 

one on day 2020-11-28 with a total of `(33 - 3) = 30`, and one on day 2020-12-09 with a total of `(74 - 47) = 27`.

### 中文

員工 1 有 3 個事件：

2020 年 11 月 28 日有 2 個事件，總計 `(32 - 4) + (200 - 55) = 173`

2020 年 12 月 3 日有 1 個事件，總計 `(42 - 1) = 41`

員工 2 有 2 個事件：

一個發生在 2020 年 11 月 28 日，總計 `(33 - 3) = 30`

一個發生在 2020 年 12 月 09 日，總計 `(74 - 47) = 27`

---

### Code

```py
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_spent"] = employees["out_time"] - employees["in_time"]

    result = employees.groupby(["emp_id", "event_day"])["time_total"].sum().reset_index()
    result.rename(columns={"event_day": "day", "time_spent": "total_time"}, inplace=True)

    return result

# employees["time_spent"] 為每次進出辦公室的時間
# groupny() 將 emp_id 跟 event_day 進行分組，確保多次進出能夠合併計算
# ["time_spent"].sum() 對 time_spent 進行加總，計算當天總共待了多久
# reset_index() 重新生成索引的 DataFrame
# rename() 將 "eveny_day" 更改為 "day"，將 "time_spent" 更改為 "total_time"
# inplace=True 為直接在原始 DataFrame 進行修改，而不產生新的 DataFrame

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_spent"] = employees["out_time"] - employees["in_time"]

    result = employees.pivot_table(
        values="time_spent",
        index=["event_day", "emp_id"],
        aggfunc="sum"
    ).reset_index()

    result.rename(columns={"event_day": "day", "time_spent": "total_time"}, inplace=True)

    return result

# piovt_table() 寫法
# piovt_table() 類似 groupby() 但更靈活
# employees["time_spent"] 為每次進出辦公室的時間
# values="time_spent" 為要計算的數值
# 設定 index 以 event_day 跟 emp_id 進行分組
# aggfunc="sum" 對相同的 emp_id 跟在相同 eveny_day 中的 time_spent 進行加總
# reset_index() 將索引重新生成並轉為 DataFrame
# rename() 將 "eveny_day" 更改為 "day"，將 "time_spent" 更改為 "total_time"
# inplace=True 為直接在原始 DataFrame 進行修改，而不產生新的 DataFrame


import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_total"] = employees.apply(lambda row: row["out_time"] - row["in_time"], axis=1)

    result = employees.groupby(["emp_id", "event_day"])["time_total"].sum().reset_index()
    result.rename(columns={"event_day": "day", "time_total": "total_time"}, inplace=True)

    return result

# apply() 寫法
# apply() 搭配 lambda 推導式，但其實這樣寫比較多餘
# reset_index() 將索引重新生成並轉為 DataFrame
# rename() 將 "eveny_day" 更改為 "day"，將 "time_spent" 更改為 "total_time"
# inplace=True 為直接在原始 DataFrame 進行修改，而不產生新的 DataFrame
```