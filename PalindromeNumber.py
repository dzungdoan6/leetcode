
def isPalindrome(x: int) -> bool:
    if (x < 0) or x % 10 == 0:
        return False
    
    if x == 0:
        return True
    first_half = x
    last_half = 0
    while (last_half < first_half):
        digit = first_half % 10
        last_half = last_half * 10 + digit
        prev_first_half = first_half
        first_half = int(first_half / 10)

    if first_half == last_half or prev_first_half == last_half:
        return True
    return False

x = 121
print(isPalindrome(x))

x = 1221
print(isPalindrome(x))


x = -121
print(isPalindrome(x))

x = 10
print(isPalindrome(x))

x = 12321
print(isPalindrome(x))

x = 0
print(isPalindrome(x))