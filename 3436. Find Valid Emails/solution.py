## 3436. Find Valid Emails 尋找有效電子郵件

# Table: Users
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | user_id         | int     |
# | email           | varchar |
# +-----------------+---------+

# (user_id) is the unique key for this table.
# Each row contains a user's unique ID and email address.

# user_id 為該表格的唯一值
# 每一行 (row) 包含使用者的唯一 ID 和電子郵件地址

### 題目

# Write a solution to find all the valid email addresses.
# A valid email address meets the following criteria:
# It contains exactly one @ symbol.
# It ends with .com.
# The part before the @ symbol contains only alphanumeric characters and underscores.
# The part after the @ symbol and before .com contains a domain name that contains only letters.
# Return the result table ordered by user_id in ascending order.

### 中文

# 編寫一個解決方法來群找所有的有效電子郵件地址
# 有效的電子郵件地址符合以下條件
# 包含一個 @ 符號
# 以 .com 結尾
# @ 符號以前的部分只有包含字母數字和底線
# @ 符號之後的和 .com 之前的部分只有包含字母的網域
# 回傳以 user_id 升序排列的結果表格

### Example 範例

# Input:
# Users table:
# +---------+---------------------+
# | user_id | email               |
# +---------+---------------------+
# | 1       | alice@example.com   |
# | 2       | bob_at_example.com  |
# | 3       | charlie@example.net |
# | 4       | david@domain.com    |
# | 5       | eve@invalid         |
# +---------+---------------------+

# Output:
# +---------+-------------------+
# | user_id | email             |
# +---------+-------------------+
# | 1       | alice@example.com |
# | 4       | david@domain.com  |
# +---------+-------------------+

### Explanation 解釋

# alice@example.com is valid because it contains one @, alice is alphanumeric, and example.com starts with a letter and ends with .com.
# bob_at_example.com is invalid because it contains an underscore instead of an @.
# charlie@example.net is invalid because the domain does not end with .com.
# david@domain.com is valid because it meets all criteria.
# eve@invalid is invalid because the domain does not end with .com.
# Result table is ordered by user_id in ascending order.

### 中文

# alice@example.com 有效，因為它包含一個 @，alice 是字母數字，example.com 以字母開頭並以 .com 結尾
# bob_at_example.com 無效，因為它包含下劃線而不是 @
# charlie@example.net 無效，因為網域不以 .com 結尾
# david@domain.com 有效，因為它滿足所有條件
# eve@invalid 無效，因為網域不以 .com 結尾
# 結果表格依照 user_id 升序排列

### Code 程式碼

import pandas as pd


def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$"
    valid_emails = users[users["email"].str.match(pattern, na=False)]
    return valid_emails.sort_values(by="user_id").reset_index(drop=True)


# 正則表達式需要使用 r''，類似 f 字串
# ^ 為字串開頭
# [a-zA-Z0-9_] 包含小寫 a 到 z，大寫 A 到 Z，數字 0 到 9，還有底線 _
# @ 包含 @
# [a-zA-Z] 網域的部分只包含小寫 a 到 z，大寫 A 到 Z
# \.com$ 必須以 .com 結尾
# 結合起來就是字串開頭符合小寫 a 到 z，大寫 A 到 Z，數字 0 到 9 以及底線 _，包含 @，網域部分為小寫 a 到 z，大寫 A 到 Z，最後以 .com 結尾
# str.match() 來檢查 email 是否符合正則表達式
# na=Flase 如果 email 欄位為 NaN，則會視為不符合
# sort_values() 依照 user_id 升序排列
# reset_index() 重置索引，因為篩選後，可能有些索引會被跳過
# drop=True 確保舊的索引不會變成新欄位


# import pandas as pd
# import re

# def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
#     """ 方法 1: 使用 str.fullmatch() (更嚴格的匹配) """
#     pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
#     valid_emails = users[users['email'].str.fullmatch(pattern, na=False)]
#     return valid_emails.sort_values(by='user_id').reset_index(drop=True)

# fullmatch 會確保整個字串需要完全符合，不能有多餘的字元
# 效率高但只適用於 pandas

# import pandas as pd
# import re

# def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
#     pattern = re.compile(r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$')
#     def is_valid_email(email):
#         return bool(pattern.fullmatch(email))

#     valid_emails = users[users['email'].apply(is_valid_email)]
#     return valid_emails.sort_values(by='user_id').reset_index(drop=True)

# apply() 寫法
# re.compile() 用來預編譯正則表達式，只需要解析一次，適用於大量重複使用時可提升效率
# 如果沒使用 re.compile 則在每次使用時都需要重新解析，效率會變差
# 如果 email 符合格式會回傳 True 或是 False
# apply() 會逐行處理 email 欄位，對 email 的每一行執行 is_vaild_email() 並回傳 True 或是 False
# user[...] 只保留 True 的行數


# import pandas as pd
# import re

# def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
#     pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
#     valid_emails = users.query("email.str.contains(@pattern, regex=True, na=False)", engine='python')
#     return valid_emails.sort_values(by='user_id').reset_index(drop=True)

# query() 寫法
# 使用 query() 搭配 str.contains()
# users.query() 類似 SQL 的查詢方式
# str.contains() 會檢查 email 格式是否匹配
# @pattern 表示前面定義的 pattern 變數
# regex=True 告訴 pandas 是一個正則表達式
# na=False 確保 NaN 不會影響查詢 (如果有 NaN 則返回 False)
# engine='python' query() 預設使用 numexper 引擎，不支援 str.contains()，所以需要設置 engine='python' 來啟用完整的 pandas 查詢功能
