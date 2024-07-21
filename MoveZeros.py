from typing import List
from queue import Queue
def moveZeroes(nums: List[int]) -> None:
    p1 = 0
    while p1 < len(nums) and nums[p1] != 0:
        p1 += 1
    p2 = p1+1
    while p2 < len(nums):
        if nums[p2] == 0:
            p2 += 1
        else:
            nums[p1] = nums[p2]
            nums[p2] = 0
            p1 += 1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))

nums = [0]
print(moveZeroes(nums))

nums = [4,2,4,0,0,3,0,5,1,0]
print(moveZeroes(nums))

nums = [1]
print(moveZeroes(nums))