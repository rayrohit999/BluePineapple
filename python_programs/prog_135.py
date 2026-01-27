'''
Write a function to find the nth hexagonal number. Hn = 2(n ^ 2) - n
'''
def getHexagonalNumber(n: int) -> int:
    '''
    Takes n as input and returns nth Hexagonal Number
        Parameter:
            n: position of Hexagonal number
        Returns:
            nth Hexagonal Number
        Raises:
            TypeError: If n is less than 1
    '''
    if n < 1:
        raise TypeError
    return (2 * n ** 2) - n

if __name__ == "__main__":
    try:
        n = int(input("Enter value of n: "))
        print(getHexagonalNumber(n))
    except TypeError:
        print("Function take only positive integer")
    except Exception as e:
        print(e)