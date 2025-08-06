## 177. Nth Highest Salary 第 N 高薪 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0183.%20Customers%20Who%20Never%20Order)

```py
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

id 是此表的主鍵（具有唯一值的欄位）
此表的每一行都包含有關員工薪資的資訊
``` 

### 題目

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the following example.

### 中文

寫一個解決方案，從員工表中找出第 n 個最高不同的工資。如果不同的工資少於 n 個，則傳回 null

結果顯示如下

---

### 183. Customers Who Never Order 從不點餐的顧客 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0183.%20Customers%20Who%20Never%20Order)

```py
Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.

id 是該表的主鍵（具有唯一值的欄位）
表格的每一行表示一個客戶的 ID 和姓名
```
 
```py
Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+

id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

id 是該表的主鍵(具有唯一值的欄位)
customerId 是 Customers 表中 ID 的外鍵(參考列)
表格的每一行表示一個訂單的 ID 和下訂單的客戶的 ID
```

### 題目

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.
 
### 中文

編寫一個解決方案來找出所有從未訂購任何東西的顧客

以任意順序傳回結果表

結果顯示如下

---

### 595. Big Countries 大國家 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0595.%20Big%20Countries)

```py
Table: World
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+

name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

名稱是此表的主鍵（具有唯一值的欄位）
表的每一行都提供有關一個國家的名稱、所屬大陸、面積、人口和 GDP 值的資訊
```

### 題目

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

### 中文

如果一個國家有以下特點，那麼這個國家就很大：

其面積至少為 300 萬平方公里（即 300,000 平方公里），或
它的人口至少有二千五百萬（即25000000）

寫出解決方案來找出大國的名稱、人口和面積

以任意順序傳回結果表

結果顯示如下

---

### 1741. Find Total Time Spent by Each Employee 找出每位員工花費的總時間 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1741.%20Find%20Total%20Time%20Spent%20by%20Each%20Employee)

```py
Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+

(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between `1` and `1440`.
It is guaranteed that no two events on the same day intersect in time, `and in_time < out_time`.

該表格顯示了員工進入辦公室以及離開辦公室的狀況
event_day 是發生的日期，in_time 為進入辦公室的時間，out_time 則是離開辦公室的時間
in_time 跟 out_time 介於 1 到 1440 之間
確保同一天沒有兩個事件的重複，而且 in_time < out_time
```

### 題目

Write a solution to calculate the total time in minutes spent by each employee on each day at the office.

Note that within one day, an employee can enter and leave more than once.

The time spent in the office for a single entry is `out_time - in_time`.

Return the result table in any order

The result format is in the following example.

### 中文

撰寫一個解決方案來計算員工每天在辦公室的時間(以分鐘為單位)，

請注意，在一天之內一名員工可以多次進入和離開

`time spent` 為辦公室花費的時間，計算方式為 `out_time - in_time`

回傳任意順序的結果

結果顯示如下

---

### 1757. Recyclable and Low Fat Products 可回收和低脂產品 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1757.%20Recyclable%20and%20Low%20Fat%20Products)

```py
Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+

product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where Y means this product is low fat and N means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where Y means this product is recyclable and N means it is not.

product_id 為表格的 primary key (具有唯一值的欄位)
low_fats 是一種 ENUM (類別)，其中 Y 表示這個產品為低脂，N 則不為低脂產品
recyclable 是一種 ENUM (類別)，其中 Y 表示這個產品可回收，N 則不能被回收
```

### 題目

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

### 中文

寫出一個解決方案來尋找低脂且可回收的產品 ID

以任意順序回傳結果

結果顯示如下

---

### 2356. Number of Unique Subjects Taught by Each Teacher 每位教師教授的獨特科目數量 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2356.%20Number%20of%20Unique%20Subjects%20Taught%20by%20Each%20Teacher)

```py
Table: Teacher
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+

(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

subject_id 跟 dept_id 為表格的 primary key (具有唯一值的列組合)
該表中的每一個 row 具有 teacher_id 的教師以及科目 subject_id 還有系所 dept_id
```

### 題目

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

The result format is shown in the following example.

### 中文

撰寫一個解決方案來計算每個老師在大學教授的唯一科目數量

回傳任意順序的結果

結果顯示如下

---

### 2877. Create a DataFrame from List 從列表建立一個 DataFrame [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2877.%20Create%20a%20DataFrame%20from%20List)

### 題目

Write a solution to create a DataFrame from a 2D list called `student_data`.

This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, `student_id` and `age`, and be in the same order as the original 2D list.

The result format is in the following example.

### 中文

撰寫一個解決方案，從名為 `student_data` 的 2D 列表建立一個 DataFrame

這個 2D 列表包含一些學生的 ID 和年齡

DataFrame 應有兩個欄位: `student_id` 和 `age`，且順序與原始的 2D 列表相同

結果顯示如下

---

### 2878. Get the Size of a DataFrame 取得 DataFrame 的大小 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2878.%20Get%20the%20Size%20of%20a%20DataFrame)

```py
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
```

### 題目

Write a solution to calculate and display the number of rows and columns of `players`.

Return the result as an array:

`[number of rows, number of columns]`

The result format is in the following example.

### 中文

撰寫一個解決方案來計算並顯示 players 的行數 (rows) 跟列數 (columns)

以列表的形式回傳結果

`[number of rows, number of columns]`

結果顯示如下

---

### 2879. Display the First Three Rows 顯示前三行資料 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2879.%20Display%20the%20First%20Three%20Rows)

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

### 題目

Write a solution to display the first 3 rows of this DataFrame.

撰寫一個解決方案來顯示此資料表的前三行 (rows) 資料

---

### 2880. Select Data 篩選數據 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2880.%20Select%20Data)

```py 
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

### 題目

Write a solution to select the name and age of the student with `student_id = 101`.

The result format is in the following example.

撰寫一個解決方案，選取 `student_id = 101` 的名字跟年齡

結果顯示如下

---

### 2881. Create a New Column 建立一個新的列 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2881.%20Create%20a%20New%20Column)

```py
DataFrame employees
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+
```

### 題目

A company plans to provide its employees with a bonus.

Write a solution to create a new column name `bonus` that contains the doubled values of the `salary` column.

The result format is in the following example.

### 中文

一間公司計畫給員工提供獎金

撰寫一個解決方案名為 `bonus` 的新列，值為 `salary` 的兩倍

結果顯示如下

---

### 2882. Drop Duplicate Rows 刪除重複行 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2882.%20Drop%20Duplicate%20Rows)

```py 
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
```

### 題目

There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

### 中文

根據電子郵件的列 (column)，DataFrame 存在一些重複的行 (rows)

撰寫一個解決方案來刪除重複的行 (rows) 並只保留第一個出現的行 (rows)

結果顯示如下

---

### 2883. Drop Missing Data 刪除遺失的數據 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2883.%20Drop%20Missing%20Data)

```py
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
```

### 題目

There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

### 中文

根據電子郵件列，DataFrame 中存在一些重複的行

編寫一個解決方案來刪除這些重複的行並僅保留第一個出現的行

結果顯示如下

---

### 2884. Modify Columns 修改欄位 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2884.%20Modify%20Columns)

```py
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
```

### 題目

A company intends to give its employees a pay rise.

Write a solution to modify the salary column by multpylying each salary by 2.

The result format is in the following example.

### 中文

一間公司打算給員工加薪

攥寫一個解決方案來將每個薪資乘以 2

結果顯示如下

---

### 2886. Change Data Type 改變資料型別 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2886.%20Change%20Data%20Type)

```py
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
```

### 題目

Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.

The result format is in the following example.

### 中文

撰寫一個解決方案來修正錯誤

成績的列 (column) 為浮點數，將其轉為整數

結果顯示如下

---

### 2888. Reshape Data: Concatenate 重塑資料: 連接 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2888.%20Reshape%20Data%20-%20Concatenate)

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

### 題目

Write a solution to concatenate these two DataFrames vertically into one DataFrame.

The result format is in the following example.

寫一個解決方案，將這兩個 DataFrame 垂直堆疊成一個 DataFrame

結果顯示如下

---

### 3436. Find Valid Emails 尋找有效電子郵件 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/3436.%20Find%20Valid%20Emails)

```py
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
```

### 題目

`user_id` is the unique key for this table.

Each row contains a user's unique ID and email address.

Write a solution to find all the valid email addresses.

A valid email address meets the following criteria:

It contains exactly one `@` symbol.

It ends with `.com`.

The part before the `@` symbol contains only alphanumeric characters and underscores.

The part after the `@` symbol and before .com contains a domain name that contains only letters.

Return the result table ordered by `user_id` in ascending order.

### 中文

編寫一個解決方法來群找所有的有效電子郵件地址

有效的電子郵件地址符合以下條件

包含一個 `@` 符號

以 `.com` 結尾

`@` 符號以前的部分只有包含字母數字和底線

`@` 符號之後的和 `.com` 之前的部分只有包含字母的網域

回傳以 `user_id` 升序排列的結果表格
