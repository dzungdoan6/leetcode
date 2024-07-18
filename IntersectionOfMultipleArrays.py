from typing import List
def intersection(nums: List[List[int]]) -> List[int]:
    hash = {}
    n = len(nums)
    for val in nums[0]:
        hash[val] = 1

    for i in range(1, len(nums)):
        for val in nums[i]:
            if val in hash:
                hash[val] += 1
            else:
                hash[val] = 1
    res = []
    for (val, count) in hash.items():
        if count == n:
            res.append(val)
    res.sort()
    return res

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums))

nums = [[1,2,3],[4,5,6]]
print(intersection(nums))
