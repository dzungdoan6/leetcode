from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left+right) // 2
        if nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            return mid
        
    if left == right and nums[left] == target:
        return left
    if target > nums[left]:
        return left + 1
    return left


nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 0
print(searchInsert(nums, target))