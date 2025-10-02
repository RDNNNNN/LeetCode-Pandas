### **175. Combine Two Tables 合併兩個表** [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0175.%20Combine%20Two%20Tables)

Table: `Person`

```python
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
personId是該表的主鍵（唯一識別列）
表格包含一些人員的ID以及他們的姓名資訊
```

Table: `Address`

```python
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
addressId是該表的主鍵（唯一識別列）。
該表中的每一行記錄都包含了一個ID為PersonId的使用者的城市和州資訊。
```

### 題目

Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

Return the result table in **any order**.

The result format is in the following example.

寫一個查詢語句，從 `Person` 表中取得每個人的姓名、城市和州資訊

如果 `Person` 表中某個人的 `personId` 在 `Address` 表中找不到對應的位址信息，則該位址資訊顯示為 `null`

傳回結果表時，結果順序不限

結果顯示如下

---

### 177. Nth Highest Salary 第 N 高薪 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0177.%20Nth%20Highest%20Salary)

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

Write a solution to find the `nth` highest distinct salary from the `Employee` table. 

If there are less than `n` distinct salaries, return `null`.

The result format is in the following example.

### 中文

寫一個解決方案，從員工表 `Employee` 中找出第 `n` 個最高不同的薪資

如果不同的薪資少於 `n` 個，則傳回 `null`

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

it has an area of at least three million (i.e., `3000000` km2), or
it has a population of at least twenty-five million (i.e., `25000000`).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

### 中文

如果一個國家有以下特點，那麼這個國家就很大：

其面積至少為 300 萬平方公里（即 `3000000` 平方公里）

或者它的人口至少有二千五百萬（即 `25000000`）

寫出解決方案來找出大國的名稱、人口和面積

以任意順序傳回結果表

結果顯示如下

---

### 627. Swap Salary 交換薪資 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/0627.%20Swap%20Salary)

```py
Table: Salary
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM (category) value of type ('m', 'f').
The table contains information about an employee.

id 是此表的主鍵（具有唯一值的欄位）
性別列舉是列舉（類別）值，類型為 ('m', 'f')
該表包含有關員工的資訊
```

### 題目

Write a solution to swap all `'f'` and `'m'` values (i.e., change all `'f'` values to `'m'` and vice versa) with a **single update statement** and no intermediate temporary tables.

Note that you must write a single update statement, **do not** write any select statement for this problem.

The result format is in the following example.

### 中文

編寫一個解決方案，使用**單一更新語句**交換所有“f”和“m”的值（即將所有“f”值變更為“m”，反之亦然），並且無需中間臨時表

請注意，您必須編寫單一更新語句，**請勿**為此問題編寫任何選擇語句

結果顯示如下

---

### 1068. Product Sales Analysis I 產品銷售分析 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1068.%20Product%20Sales%20Analysis%20I)

```py
Table: Sales
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

(sale_id, year) 是此表的主鍵（具有唯一值的列的組合）
product_id 是 Product 表的外鍵（引用列）
此表的每一行都顯示了特定年份產品 product_id 的銷售情況
請注意，價格是每單位的價格
```

```py
Table: Product
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

product_id 是此表的主鍵（具有唯一值的欄位）
此表的每一行表示每個產品的產品名稱
```

### 題目

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in any order.

The result format is in the following example.

### 中文

編寫一個解決方案，報告 `Sales` 表中每個 `sale_id` 對應的 `product_name`、`year` 和 `price`

按任意順序傳回結果表

結果顯示如下

---

### 1148. Article Views I 文章瀏覽量 I [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1148.%20Article%20Views%20I)

```py
Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+

There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

此表沒有主鍵（具有唯一值的列），表可能有重複的行
表格的每一行表示某個瀏覽者在某個日期查看了一篇文章（由某個作者撰寫）
請注意，相同的 author_id 和 viewer_id 表示同一個人
```

### 題目

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

### 中文

編寫一個解決方案來尋找所有查看過至少一篇自己的文章的作者

傳回按 id 升序排序的結果表

結果顯示如下

---

### **1378. Replace Employee ID With The Unique Identifier 用唯一識別碼替換員工 ID** [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1378.%20Replace%20Employee%20ID%20With%20The%20Unique%20Identifier)

```python
Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

id 是此表的主鍵（具有唯一值的欄位）
此表的每一行都包含公司員工的 id 和姓名
```

```python
Table: EmployeeUNI
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

(id, unique_id) 是此表的主鍵（具有唯一值的欄位的組合）
此表的每一行都包含公司中員工的 ID 及其對應的唯一 ID
```

### 題目

Write a solution to show the **unique ID** of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

編寫一個解決方案，顯示每個使用者的**唯一 ID**。如果使用者沒有唯一 ID，則直接顯示 `null`

以**任意**順序傳回結果表

結果顯示如下

---

### 1517. Find Users With Valid E-Mails 尋找有效電子郵件的用戶 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1517.%20Find%20Users%20With%20Valid%20E-Mails)

```py
Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+

user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website.
Some e-mails are invalid.

user_id 是該表的主鍵（具有唯一值的欄位）
該表包含在網站上註冊的用戶的資訊
有些電子郵件無效
```

### 題目

Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore `_`, period `.`, and/or dash `-`. The prefix name must start with a letter.
The domain is `@leetcode.com`.

Return the result table in any order.

The result format is in the following example.

### 中文

編寫一個解決方案來尋找擁有有效電子郵件的使用者

有效的電子郵件具有前綴名稱和網域，其中：

前綴名稱是一個字串，可能包含字母（大寫或小寫）、數字、底線 `_`、句點 `.`和 `/` 或破折號 `-`

前綴名稱必須以字母開頭

網域是 `@leetcode.com`

以任意順序傳回結果表

結果顯示如下

---

### **1587. Bank Account Summary II 銀行帳戶摘要 II**

Table: `Users`

```python
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key (column with unique values) for this table.
Each row of this table contains the account number of each user in the bank.
There will be no two users having the same name in the table.

「account」是該表的主鍵（唯一值列）
該表中的每一行都包含銀行中每個使用者的帳戶號碼
表中不會出現兩個同名使用者
```

Table: `Transactions`

```python
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key (column with unique values) for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0.

trans_id是該表的主鍵（唯一識別列）
該表中的每一行記錄了所有帳戶的交易變更資訊
若用戶收到款項，amount值為正；如果用戶轉出款項，amount 值為負
所有帳戶的初始餘額均為 0
```

### 題目

Write a solution to report the name and balance of users with a balance higher than `10000`. 

The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in **any order**.

The result format is in the following example.

寫一個查詢語句，傳回餘額大於 10000 的使用者姓名和餘額

用戶的帳戶餘額等於所有與該帳戶相關的交易金額的總和

結果表可以按任意順序排列

結果顯示如下

---

### 1667. Fix Names in a Table 修復表中的名稱 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1667.%20Fix%20Names%20in%20a%20Table)

```py
Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+

user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. 
The name consists of only lowercase and uppercase characters.

user_id 是此表的主鍵（具有唯一值的列）
該表包含用戶的 ID 和名稱
該名稱僅由小寫和大寫字符組成
```

### 題目

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`.

The result format is in the following example.

### 中文

編寫解決方案來修復名稱，以便只有第一個字符是大寫，其餘的是小寫

返回由 `user_id` 排序的結果表

結果顯示如下

### Example 範例

```py
Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

### Code 程式碼

```py
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id")
```

---

### 1683. Invalid Tweets 無效的推文 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1683.%20Invalid%20Tweets)

```py
Table: Tweets
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+

tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

tweet_id 為此表的主鍵
content 是由字母數字元、`!`、`「」`組成，且不含其他特殊字元
此表包含所有社交應用程式的所有推文
```

### 題目

Write a solution to find the IDs of the invalid tweets. 

The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than `15`.

Return the result table in any order.

The result format is in the following example.

### 中文

撰寫一個解決方案來尋找無效的 ID 

如果推文內容的字元數大於 `15`，則該推文無效

以任意順序回傳這個結果表

結果顯示如下

---

### 1693. Daily Leads and Partners 每日商機和合作夥伴 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1693.%20Daily%20Leads%20and%20Partners)

```py
Table: DailySales
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+

There is no primary key (column with unique values) for this table. 
It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.

該表沒有 primary key (具有唯一值的列)

可能包含重複的值

此表格包含所售產品的日期和名稱以及銷售線索和合作夥伴的 ID

此名稱僅由小寫英文字母組成 
```

### 題目
 
For each `date_id` and `make_name`, find the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The result format is in the following example.

### 中文

對於每個 `date_id` 和 `make_name`，尋找不同的 `Lead_id` 和不同的 `Partner_id` 的數量

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

### 1873. Calculate Special Bonus 計算特別獎金 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/1873.%20Calculate%20Special%20Bonus)

```py
Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+

employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.

employee_id 為此表的主鍵 (具有唯一值的列)
該表的每一行 表示 員工 ID 員工姓名以及薪水
```

#### 題目
 
Write a solution to calculate the bonus of each employee. 

The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character `M`. 

The bonus of an employee is `0` otherwise.

Return the result table ordered by `employee_id`.

The result format is in the following example.

#### 中文

寫一個解決方案計算每個員工的獎金

如果 `employee_id` 為奇數，並且員工的名字不是從角色 `M` 開始的，則員工的獎金是其薪資的 `100％` 

員工的獎勵為 `0`

返回員工訂購的結果表

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

There are some rows having missing values in the `name` column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

### 中文

`name` 欄中有一些行存在缺失值

編寫一個解決方案來刪除這些缺失值的行

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

Write a solution to modify the `salary` column by multpylying each salary by 2.

The result format is in the following example.

### 中文

一間公司打算給員工加薪

攥寫一個解決方案來將每個薪資 `salary` 乘以 2

結果顯示如下

---

### 2885. Rename Columns 重新命名列 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2885.%20Rename%20Columns)

```py
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
```

### 題目

Write a solution to rename the columns as follows:

編寫解決方案來重新命名列，結果顯示如下：

```py
id to student_id
first to first_name
last to last_name
age to age_in_years
```

The result format is in the following example.

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

The `grade` column is stored as floats, convert it to integers.

The result format is in the following example.

### 中文

撰寫一個解決方案來修正錯誤

成績 `grade` 的列 (column) 為浮點數，將其轉為整數

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

### **2889. Reshape Data: Pivot 重塑數據: 透視** [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2889.%20Reshape%20Data%20-%20Pivot)

```python
DataFrameweather
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
```

### 題目

Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

編寫一個解決方案來對資料進行**透視**，使每一行代表特定月份的溫度，每個城市作為單獨的列

結果顯示如下

### Example 範例

```python
Input:
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+

Output:
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
```

---

### 2890. Reshape Data: Melt 重塑數據：融解 [(連結)](https://github.com/RDNNNNN/LeetCode-Pandas/tree/main/2890.%20Reshape%20Data%20-%20Melt)

```py
DataFrame report
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
```

### 題目

Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.

編寫一個解決方案來重塑數據，使每一行代表特定季度產品銷售資料

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
