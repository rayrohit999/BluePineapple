'''
Write a function to find sum of the numbers in a list between the indices of a specified range.
'''

def rangeSum(numbers: list, start: int, end: int) -> int | float:
    '''
    takes a list, a strart index and a end index as input and returns it's sum.
    Can raise error if input is not correct.
    '''
    if not isinstance(numbers, list):
        raise TypeError

    if not numbers:
        raise ValueError
    
    if isinstance(start, bool) or isinstance(end, bool):
        raise TypeError
    
    if not isinstance(start, int):
        raise TypeError
    
    if not isinstance(end, int):
        raise TypeError
    
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in numbers):
        raise TypeError

    if start < 0 or end < 0 or start > end or end >= len(numbers):
        raise ValueError

    return sum(numbers[start: end + 1])