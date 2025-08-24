from typing import List
import numpy as np

def isValidSudoku(board: List[List[str]]) -> bool:
    hash_rows = [set() for _ in range(9)]
    hash_cols = [set() for _ in range(9)]
    hash_submats = list()
    for _ in range(3):
        hash_submats.append([set() for _ in range(3)])
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            val = board[i][j]

            if val in hash_rows[i]:
                return False
            hash_rows[i].add(val)

            if val in hash_cols[j]:
                return False
            hash_cols[j].add(val)

            r = int(np.floor(i/3))
            c = int(np.floor(j/3))
            if val in hash_submats[r][c]:
                return False
            hash_submats[r][c].add(val)

    return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))