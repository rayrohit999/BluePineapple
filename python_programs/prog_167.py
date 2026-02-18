'''
Write a python function to find smallest power of 2 greater than or equal to n.
'''

def smallestPowerOf2(n: int) -> int:
    '''
    Takes a positive integer as input and returns smallest power of two
    greater than or equal to input.
        Parameter:
            n (int): Positive integer.
        Returns:
            (int): Positive integer.
        Raises:
            TypeError: If input is not a number.
            ValueError: If input is not a positive number.
    '''
    if isinstance(n, bool):
        raise TypeError
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError
    x = 0
    while (1 << x) < n:
        x += 1

    return 1 << x
    