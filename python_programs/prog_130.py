'''
Write a function to find the item with maximum frequency in a given list.
'''
from typing import Any
from collections import Counter
def getMaxItem(inputList: list[Any]) -> Any:
    '''
    Takes a list as input and returs the item with maximum frequency
        Parameter:
            inputList (list): list of items
        Returns:
            item with maximum frequency
    '''
    freq = Counter(inputList)
    maxCount = 1
    maxItem = inputList[0]
    for key,value in freq.items():
        if value >= maxCount:
            maxCount = value
            maxItem = key
    return maxItem

if __name__ == "__main__":
    inputList = ["rohit", "mohit", "yash", "aniket", "rohit", "mohit", "rohit", 1, 1, 1, 1, 1, 4]
    print(getMaxItem(inputList))