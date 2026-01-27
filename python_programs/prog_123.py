'''
Write a function to sum all amicable numbers from 1 to a specified number.
'''

def sumOfDivisor(n: int) -> int:
    '''
    Returns sum of proper divisors of n (excluding n itself)
    '''
    if n==1:
        return 0
    total = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            total += i
            if n//i != i:
                total += n//i
        i += 1
    return total
    
def sumAmicableNumber(limit: int) -> int:
    '''
    Returns sum of all Amicable numbers from i to limit
    '''
    amicableSum = 0
    for a in range(2, limit + 1):
        b = sumOfDivisor(a)
        if b != a and b <= limit and sumOfDivisor(b) == a:
            amicableSum += a
    return amicableSum

if __name__ == "__main__":
    limit = 5000
    print(sumAmicableNumber(limit))