'''
Write a python function to check whether the given number is co-prime or not.
'''
import math
def isCoprime(num1: int, num2: int) -> bool:
    '''
    Takes two positive integers numbers as input and check weather they are coprime or not
        Parameter:
            num1(int): Positive integer
            num2(int): Positive integer
        Returns:
            (bool): True if numbers are coprime otherwise False
        Raises:
            TypeError: If input is not a number
            ValueError: If input is not a positive number
    '''
    if isinstance(num1, bool) or isinstance(num2, bool):
        raise TypeError
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError
    if num1 < 0 or num2 < 0:
        raise ValueError
    return math.gcd(num1, num2) == 1
    