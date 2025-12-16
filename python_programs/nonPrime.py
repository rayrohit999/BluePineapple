def isPrime(n):
    # if number is less than 2, it is not prime
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def isNonPrime(n):
    return not isPrime(n)
