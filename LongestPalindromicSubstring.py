def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def longestPalindrome(s: str) -> str:
    i = 0
    j = len(s)
    length = 1
    substr = s[0]
    while i < len(s):
        while not isPalindrome(s[i:j]):
            j -= 1
        if len(s[i:j]) > length:
            substr = s[i:j]
            length = len(substr)
        i += 1
        j = len(s)
        if j-i < length:
            break
    return substr
        

s = "babad"
print(longestPalindrome(s))

s = "cbbd"
print(longestPalindrome(s))

s = "a"
print(longestPalindrome(s))

s = "bb"
print(longestPalindrome(s))
