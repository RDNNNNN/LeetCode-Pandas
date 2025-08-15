## 1683. Invalid Tweets 無效的推文

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

### Example 範例

```py
Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+

Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
```

### Explanation 解釋

Tweet 1 has length = 11. It is a valid tweet.

Tweet 2 has length = 33. It is an invalid tweet.

Tweet 1 的長度為 11 這是有效的推文

Tweet 2 的長度為 33 這是無效的推文

### Code 程式碼

```py 
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invailds_tweets = tweets[tweets["content"].str.len() > 15]
    return invailds_tweets.drop(columns=["content"])
```