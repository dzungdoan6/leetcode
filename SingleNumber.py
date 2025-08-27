from typing import List

def singleNumber(nums: List[int]) -> int:
    hm = set()

    for num in nums:
        if num not in hm:
            hm.add(num)
        else:
            hm.remove(num)

    return hm.pop()

nums = [2,2,1]
print(singleNumber(nums))

nums = [4,1,2,1,2]
print(singleNumber(nums))

nums = [1]
print(singleNumber(nums))