from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set = [0]*1001
    for val in nums1:
        set[val] = 1

    for val in nums2:
        if set[val] == 1:
            set[val] = -1
    
    res = []
    for i in range(len(set)):
        if set[i] == -1:
            res.append(i)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]
res = intersection(nums1=nums1, nums2=nums2)
print(res)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
res = intersection(nums1=nums1, nums2=nums2)
print(res)