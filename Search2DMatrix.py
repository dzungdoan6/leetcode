from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix)-1
    while bottom - top > 1:
        mid = (top+bottom) // 2
        if matrix[mid][0] > target:
            bottom = mid
        elif matrix[mid][0] < target:
            top = mid
        elif matrix[mid][0] == target:
            return True
    if matrix[bottom][0] > target:
        row = top
    else:
        row = bottom


    left = 0
    right = len(matrix[row]) - 1
    while left < right:
        mid = (left + right) // 2
        if matrix[row][mid] > target:
            right = mid - 1
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            return True
    
    if left == right and matrix[row][left] == target:
        return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
print(searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(searchMatrix(matrix, target))

matrix = [[1]]
target = 2
print(searchMatrix(matrix, target))


matrix = [[1],[3]]
target = 5
print(searchMatrix(matrix, target))