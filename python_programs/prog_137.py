'''
Write a function to find the ratio of zeroes in an array of integers.
'''
def getZeroesRatio(numList: list[int]) -> float:
    '''
    Takes list of integers as input and returs ratio of zeroes 
        Parameter:
            numList (list): list of integers
        Returns:
            (float): Ratio of zeroes
    '''
    if not list:
        raise Exception("List can't be empty! ")
    if not isinstance(numList, list):
        raise TypeError
    no_of_zeroes = numList.count(0)
    length = len(numList)
    return no_of_zeroes/ length