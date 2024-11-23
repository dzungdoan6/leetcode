from typing import List


def binarySearch(nums, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binarySearch(nums, target, left=left, right=mid-1)
    return binarySearch(nums, target, left=mid+1, right=right)

def search(nums: List[int], target: int) -> int:

    # find pivot
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] > nums[-1]:
            left = mid+1
        elif nums[mid] < nums[-1]:
            right = mid-1
        elif nums[mid] == nums[-1]:
            break

    pivot = left

    index = binarySearch(nums=nums, target=target, left=0, right=pivot-1)
    if index != -1:
        return index
    
    index = binarySearch(nums=nums, target=target, left=pivot, right=len(nums)-1)
    if index != -1:
        return index
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))

nums = [1, 3]
target = 0
print(search(nums, target))

nums = [1, 3]
target = 3
print(search(nums, target))


nums = [5,1,3]
target = 5
print(search(nums, target))