def strStr(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    i = 0
    j = 0
    k = 0
    while i < len(haystack) and j < len(haystack):
        if haystack[j] == needle[k]:
            j += 1
            k += 1
            if k == len(needle):
                return i
        else:
            j = i + 1
            i = j
            k = 0

    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle)) 

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle)) 

haystack = "aaa"
needle = "aaaa"
print(strStr(haystack, needle))

haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle)) 

haystack = "mississippi"
needle = "issipi"
print(strStr(haystack, needle)) 