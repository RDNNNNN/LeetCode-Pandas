## 3436. Find Valid Emails 尋找有效電子郵件


# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | user_id         | int     |
# | email           | varchar |
# +-----------------+---------+


# (user_id) is the unique key for this table.

# user_id 為該表格的唯一值

# Each row contains a user's unique ID and email address.

# 每一行包含使用者的唯一 ID 和電子郵件地址

# Write a solution to find all the valid email addresses. 

# 編寫一個解決方法來群找所有的有效電子郵件地址

# A valid email address meets the following criteria:

# 有效的電子郵件地址符合以下條件

# It contains exactly one @ symbol.

# 包含一個 @ 符號

# It ends with .com.

# 以 .com 結尾

# The part before the @ symbol contains only alphanumeric characters and underscores.

# @ 符號以前的部分只有包含字母數字和底線

# The part after the @ symbol and before .com contains a domain name that contains only letters.

# @ 符號之後的和 .com 之前的部分只有包含字母的網域

# Return the result table ordered by user_id in ascending order.

# 回傳以 user_id 升序排列的結果表格

### Example 範例:

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

### Explanation 解釋:

# alice@example.com is valid because it contains one @, alice is alphanumeric, and example.com starts with a letter and ends with .com.

# alice@example.com 有效，因為它包含一個 @，alice 是字母數字，example.com 以字母開頭並以 .com 結尾。

# bob_at_example.com is invalid because it contains an underscore instead of an @.

# bob_at_example.com 無效，因為它包含下劃線而不是 @。

# charlie@example.net is invalid because the domain does not end with .com.

# charlie@example.net 無效，因為網域不以 .com 結尾。

# david@domain.com is valid because it meets all criteria.

# david@domain.com 有效，因為它滿足所有條件。

# eve@invalid is invalid because the domain does not end with .com.

# eve@invalid 無效，因為網域不以 .com 結尾。

# Result table is ordered by user_id in ascending order.

# 結果表格依照 user_id 升序排列。

### Code

import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
    valid_emails = users[users['email'].str.match(pattern, na=False)]
    return valid_emails.sort_values(by='user_id').reset_index(drop=True)

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

# def find_valid_emails_fullmatch(users: pd.DataFrame) -> pd.DataFrame:
#     pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
#     valid_emails = users[users['email'].str.fullmatch(pattern, na=False)]
#     return valid_emails.sort_values(by='user_id').reset_index(drop=True)

# fullmatch() 會確保整個字串需要完全符合
# 效率高但只適用於 Pandas

# import pandas as pd
# import re

# def find_valid_emails_apply(users: pd.DataFrame) -> pd.DataFrame:
    
#     pattern = re.compile(r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$')
#     def is_valid_email(email):
#         return bool(pattern.fullmatch(email))
    
# apply()    
# re.compile() 用來預編譯正則表達式，使其可造成重複效能損耗
    
# import pandas as pd
# import re

# def find_valid_emails_query(users: pd.DataFrame) -> pd.DataFrame:
#     pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
#     valid_emails = users.query("email.str.contains(@pattern, regex=True, na=False)", engine='python')
#     return valid_emails.sort_values(by='user_id').reset_index(drop=True)

# query()

