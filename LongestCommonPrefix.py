from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    min_len = len(strs[0])
    for i in range(1, len(strs)):
        if min_len > len(strs[i]):
            min_len = len(strs[i])
    prefix = ""
    for i in range(min_len):
        c = strs[0][i]
        is_common = True
        for j in range(1, len(strs)):
            if strs[j][i] != c:
                is_common = False
                break
        
        if is_common:
            prefix += c
        else:
            break
    
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))

strs = ["","b"]
print(longestCommonPrefix(strs))