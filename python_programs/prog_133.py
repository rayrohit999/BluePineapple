'''
Write a function to calculate the sum of the negative numbers of a given list of numbers using lambda function.
'''
from functools import reduce
def sumNegative(numList: list[int|float]) -> int | float:
    '''
    Takes a list of numbers as input and calculate sum of negative numbers and returns it.
        Parameter:
            numList (list): list of number(int or float)
        Returns:
            Sum of negative numbers
        Raises:
            ValueError: If input list has elements other than numbers 
    '''
    if not all(isinstance(x, (int, float)) for x in numList):
        raise ValueError
    total = reduce(lambda acc, x: acc + x if x<0 else acc, numList, 0)
    return total

if __name__ == "__main__":
    try:
        numList = [2, 34, 12, -5, -23, 34, -1, 0, 43]
        print(sumNegative(numList)) # 29

        numList = []
        print(sumNegative(numList)) # 0

        numList = [2, 34, 5, 23, 34, 1, 0, 43]
        print(sumNegative(numList)) # 0

        numList = [2, 34, "12", -5, -23, 34, -1, 0, 43]
        print(sumNegative(numList)) # Error
        sumNegative()
    except ValueError as e:
        print("Only Int value is expected")
    except Exception as e:
        print(e)