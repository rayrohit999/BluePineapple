'''
Write a python function to find the sum of common divisors of two given numbers.
'''

def getDivisors(n: int) -> tuple[int, ...]:
    '''
    Takes number as input and returns tuple of its divisor
    '''
    divTup = [1, n]
    i = 2
    while i * i < n:
        if n % i == 0:
            divTup.append(i)
            if n//i != i:
                divTup.append(n//i)
        i += 1
    return tuple(divTup)

def sumCommonDivisor(num1: int, num2: int) -> int:
    num1Divisors = getDivisors(num1)
    num2Divisors = getDivisors(num2)
    common = {*num1Divisors} & set(num2Divisors)
    return sum(common)

if __name__ == "__main__":
    print(sumCommonDivisor(12, 4))