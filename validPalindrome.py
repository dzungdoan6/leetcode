def isPalindrome(s: str) -> bool:
    s = s.lower()
    new_s = ""
    for char in s:
        if (ord(char) >= ord('a') and ord(char) <= ord('z')) or \
            ord(char) >= ord('0') and ord(char) <= ord('9'):
            new_s += char
    if len(new_s) == 0:
        return True
    
    i = 0
    j = len(new_s) - 1
    while i<j:
        if new_s[i] != new_s[j]:
            return False
        i += 1
        j -= 1
        
    return True


s = "0P"
print(isPalindrome(s))