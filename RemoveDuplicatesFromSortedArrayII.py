from typing import List
def removeDuplicates(nums: List[int]) -> int:
    map = {}
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1

    i = 0
    for num in map:
        if map[num] == 1:
            nums[i] = num
            i += 1
        else:
            nums[i] = num
            nums[i+1] = num
            i += 2
    return i


nums = [0,0,1,1,1,1,2,3,3]
k = removeDuplicates(nums)
print(k)
print(nums)