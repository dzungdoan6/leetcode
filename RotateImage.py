from typing import List
import numpy as np
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    i1 = 0
    i2 = len(matrix) - 1
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    while i1 < i2:
        for j in range(n_cols):
            tmp = matrix[i1][j]
            matrix[i1][j] = matrix[i2][j]
            matrix[i2][j] = tmp

        i1 += 1
        i2 -= 1

    for i in range(n_rows):
        for j in range(i+1, n_cols):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)
