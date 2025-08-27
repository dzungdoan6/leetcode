def sum_of_squares(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum += (d*d)
        n = int(n / 10)
    return sum

def isHappy(n: int) -> bool:
    hm = set()
    while n not in hm:
        hm.add(n)
        n = sum_of_squares(n)
        if n == 1:
            return True
        
    return False

n = 19
print(isHappy(n))


n = 2
print(isHappy(n))