
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def validPalindrome(s: str) -> bool:
    if isPalindrome(s):
        return True
    
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if isPalindrome(s[:i] + s[i+1:]) or isPalindrome(s[:j] + s[j+1:]):
                return True
            else:
                return False
        i += 1
        j -= 1
   

s = "aba"
print(validPalindrome(s))

s = "abca"
print(validPalindrome(s))

s = "abc"
print(validPalindrome(s))