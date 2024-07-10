from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    map = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in map:
            return True
        else:
            map[nums[i]] = i
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))

nums = [1,2,3,4]
print(containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))