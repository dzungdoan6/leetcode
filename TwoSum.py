from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in hashmap:
            return {hashmap[nums[i]], i}
        else:
            hashmap[target - nums[i]] = i

nums = [2,7,11,15]
target = 9
res = twoSum(nums=nums, target=target)
print(res)