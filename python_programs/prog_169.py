'''
Write a function to calculate the nth pell number.
'''
from functools import lru_cache

@lru_cache(None)
def getPellNumber(n: int) -> int:
    """
    Takes n as input and retures nth position pell number.
    If input is not in correct form may raise typeError or ValueError
    """
    if isinstance(n, bool):
        raise TypeError("Boolean is not a valid input")

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2*getPellNumber(n-1) + getPellNumber(n-2)