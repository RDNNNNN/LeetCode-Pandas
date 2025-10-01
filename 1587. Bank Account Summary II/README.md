## **1587. Bank Account Summary II 銀行帳戶摘要 II**

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

### **Example 範例**

```python
Input:
Users table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+

Transactions table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+

Output:
+------------+------------+
| name       | balance    |
+------------+------------+
| Alice      | 11000      |
+------------+------------+
```

### Explanation 解釋

Alice's balance is (7000 + 7000 - 3000) = 11000.

Bob's balance is 1000.

Charlie's balance is (6000 + 6000 - 4000) = 8000.

### Code 程式碼

```python
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return transactions.groupby("account")[["amount"]].sum().join(users.set_index("account")).query("amount > 10000")[["name", "amount"]].rename(columns={"amount": "balance"})
```