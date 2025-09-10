def isPrime(k):
    count = 0
    for i in range(1, k+1):
        if k % i == 0:
            count +=1

    if count == 2:
        return True
    return False

def isNotPrime(k):
    if k == 0 or k == 1:
        return True
    if k == 2:
        return False
    for i in range(2, k):
        if k % i == 0:
            return True
    return False

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0 or n == 1:
        return 0
    
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    for i in range(2, n):
        if primes[i] is True:
            p = i*i
            while p < n:
                primes[p] = False
                p += i
        
    count = 0
    for p in primes:
        if p is True:
            count += 1

    return count

n = 10
print(countPrimes(n))

n = 0
print(countPrimes(n))

n = 1
print(countPrimes(n))

n = 3
print(countPrimes(n))

