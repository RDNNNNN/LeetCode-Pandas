### 1741. Find Total Time Spent by Each Employee 找出每位員工花費的總時間 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1741.%20Find%20Total%20Time%20Spent%20by%20Each%20Employee)

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

---

### 1757. Recyclable and Low Fat Products 可回收和低脂產品 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1757.%20Recyclable%20and%20Low%20Fat%20Products)

```py
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
```

### 題目

`product_id` is the primary key (column with unique values) for this table.

`low_fats` is an `ENUM` (category) of type ('Y', 'N') where `Y` means this product is low fat and `N` means it is not.

`recyclable` is an `ENUM` (category) of types ('Y', 'N') where `Y` means this product is recyclable and `N` means it is not.

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

---

### 2356. Number of Unique Subjects Taught by Each Teacher 每位教師教授的獨特科目數量 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2356.%20Number%20of%20Unique%20Subjects%20Taught%20by%20Each%20Teacher)

```py
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
```

---

### 2877. Create a DataFrame from List 從列表建立一個 DataFrame [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2877.%20Create%20a%20DataFrame%20from%20List)

### 題目

Write a solution to create a DataFrame from a 2D list called `student_data`.

This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, `student_id` and `age`, and be in the same order as the original 2D list.

The result format is in the following example.

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
