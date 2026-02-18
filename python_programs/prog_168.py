'''
Write a python function to find the frequency of a number in a given array.
'''

def getFrequency(numList: list[int | float], ele: int | float) -> int:
    '''
    Takes a list of numbers and a number then returns the frequency of number in list.
        Parameters:
            numList (list): list of numbers
            ele (int | float): Number whose frequency to be found
        Returns:
            (int): Frequency of the ele in numList
        Raises:
            TypeError: If input is not correct
    '''
    
    if not isinstance(numList, list):
        raise TypeError("First parameter should be list of numbers only.")
    
    if not numList:
        return 0
    
    if isinstance(ele, bool):
        raise TypeError
    
    if not isinstance(ele, (int, float)):
        raise TypeError("Second parameter should be int or float only.")
    
    if any(isinstance(value, bool) for value in numList):
        raise TypeError
    
    if not all(isinstance(value, (int, float)) for value in numList):
        raise TypeError("Elements of list should be int or float only.")
    
    return numList.count(ele)
    
