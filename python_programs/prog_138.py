'''
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
'''
def checkRepresentation(num: int) -> bool:
    '''
    Takes number as input and returns weather a number can be represented in form of 2^x + 2^y where x and y are non zero.
        Parameter:
            num (int): Integer number which is to be cheacked
        Returns:
            (bool): Ture if number can be reprsented otherwise False
        Raises:
            TypeError: If input number is not a integer
            ValueError: If input number is less than zero
    '''
    if not isinstance(num, int):
        raise TypeError
    if num <= 0:
        raise ValueError
    x = 1
    while (1 << x) <= num:
        y = 1
        while(1 << y) <= num:
            print((1 << x) + (1 << y))
            if (1 << x) + (1 << y) == num:
                return True
            y += 1
        x += 1
    return False