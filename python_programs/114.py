from collections import Counter

def assignFrequency(inputList: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    '''
    Takes list of tuples as input and assign their frequency to them
        Parameter:
            inputList(list[tuple]): list of tuples
        Returns: 
            resul(list[tuple]): New list of tuples with frequency
    '''
    result = [(*key, value) for key, value in Counter(inputList).items()]
    return result

if __name__ == "__main__":
    inputList = [(6, 7, 8), (2, 3), (6, 7, 8), (2, 3), (6, 7, 8)]
    finalList = assignFrequency(inputList)
    print(finalList)