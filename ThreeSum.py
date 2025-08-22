from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    map = {}
    for i, num in enumerate(nums):
        if -num not in map:
            map[-num] = [i]
        else:
            map[-num].append(i)
    
    n = len(nums)
    results = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum = nums[i] + nums[j]
            if sum in map:
                for k in map[sum]:
                    if i != k and j != k:
                        res = [nums[i], nums[j], nums[k]]
                        break
                results.append(res)

    return results

nums = [-1,0,1,2,-1,-4]
results = threeSum(nums)
print(results)