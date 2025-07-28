## 2878. Get the Size of a DataFrame 取得 DataFrame 的大小

# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+

### 題目

# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array:
# [number of rows, number of columns]
# The result format is in the following example.

### 中文

# 撰寫一個解決方案來計算並顯示 players 的行數 (rows) 跟列數 (columns)
# 以列表的形式回傳結果
# [number of rows, number of columns]
# 結果顯示如下

### Example 範例

# Input:
# +-----------+----------+-----+-------------+--------------------+
# | player_id | name     | age | position    | team               |
# +-----------+----------+-----+-------------+--------------------+
# | 846       | Mason    | 21  | Forward     | RealMadrid         |
# | 749       | Riley    | 30  | Winger      | Barcelona          |
# | 155       | Bob      | 28  | Striker     | ManchesterUnited   |
# | 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
# | 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
# | 883       | Ava      | 23  | Defender    | Chelsea            |
# | 355       | Violet   | 18  | Striker     | Juventus           |
# | 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
# | 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
# | 642       | Charlie  | 36  | Center-back | Arsenal            |
# +-----------+----------+-----+-------------+--------------------+

# Output:
# [10, 5]

### Explanation 解釋

# This DataFrame contains 10 rows and 5 columns.

# 這個 DataFrame 包含 10 行 (rows) 5 列 (columns)

### Code 程式碼

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)


# 使用 shape 顯示數量並轉成 list 回傳


# import pandas as pd

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     return [len(players), len(players.columns)]

# len() 寫法
# len(players) 計算 DataFrame 的行數 (rows)
# len(playes.columns) 計算 DataFrame 的欄數 (columns)


# import pandas as pd

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     return [players.count().shape[0], players.shape[1]]

# count() 寫法
# players.count() 計算每個欄位的非 NaN 值，但 count().shape[0] 等於 len(players.columns)
# shape[1] 直接取欄數


# import pandas as pd

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     return [players.index.size, players.columns.size]

# size() 寫法
# players.index.size 計算行數 (rows)
# players.columns.size 計算列數 (columns)


# import pandas as pd

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     rows, cols = players.shape
#     return [rows, cols]

# shape 回傳解構為 rows 和 cols，直接返回 [rows, cols]
# 跟原本 shape 結果相同只是寫法不同
