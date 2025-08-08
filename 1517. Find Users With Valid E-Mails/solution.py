## 1517. Find Users With Valid E-Mails 尋找有效電子郵件的用戶

# Table: Users
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+

# `user_id` is the primary key (column with unique values) for this table.
# This table contains information of the users signed up in a website.
# Some e-mails are invalid.

# `user_id` 是該表的主鍵（具有唯一值的欄位）
# 該表包含在網站上註冊的用戶的資訊
# 有些電子郵件無效

### 題目

# Write a solution to find the users who have valid emails.
# A valid e-mail has a prefix name and a domain where:
# The prefix name is a string that may contain letters (upper or lower case), digits, underscore `_`, period `.`, and/or dash `-`. The prefix name must start with a letter.
# The domain is `@leetcode.com`.
# Return the result table in any order.
# The result format is in the following example.

### 中文

# 編寫一個解決方案來尋找擁有有效電子郵件的使用者
# 有效的電子郵件具有前綴名稱和網域，其中：
# 前綴名稱是一個字串，可能包含字母（大寫或小寫）、數字、底線 `_`、句點 `.`和 `/` 或破折號 `-`
# 前綴名稱必須以字母開頭
# 網域是 `@leetcode.com`
# 以任意順序傳回結果表
# 結果顯示如下

### Example 範例

# Input:
# Users table:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+

# Output:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# +---------+-----------+-------------------------+

### Explanation 解釋

# The mail of user 2 does not have a domain.
# The mail of user 5 has the `#` sign which is not allowed.
# The mail of user 6 does not have the leetcode domain.
# The mail of user 7 starts with a period.

### 中文

# 用戶 2 的郵件沒有網域
# 使用者 5 的郵件中有 # 符號，這是不允許的
# 用戶6的郵件沒有 leetcode 網域
# 用戶 7 的郵件以句點開頭

### Code 程式碼

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_email = users[
        users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$")
    ]
    return valid_email
