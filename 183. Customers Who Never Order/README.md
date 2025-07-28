### 183. Customers Who Never Order 從不點餐的顧客

```py
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
```

### 題目

id is the primary key (column with unique values) for this table.

Each row of this table indicates the ID and name of a customer.

### 中文

id 是該表的主鍵（具有唯一值的欄位）

表格的每一行表示一個客戶的ID和姓名
 
```py
Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
```

### 題目

id is the primary key (column with unique values) for this table.

customerId is a foreign key (reference columns) of the ID from the Customers table.

Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.
 
### 中文

id 是該表的主鍵(具有唯一值的欄位)

customerId 是 Customers 表中 ID 的外鍵(參考列)

表格的每一行表示一個訂單的ID和下訂單的客戶的ID

編寫一個解決方案來找出所有從未訂購任何東西的顧客

以任意順序傳回結果表

結果顯示如下
 
### Example 範例

```py
Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

### Code 程式碼

```py
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df =  customers.merge(orders,left_on="id", right_on="customerId", how="left")
    return df[df["customerId"].isnull()].rename(columns={'name':'Customers'})[['Customers']]
```