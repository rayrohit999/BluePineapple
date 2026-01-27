def findElementAppereadOnce(inputList: list[int]) -> int | None:
    '''
    Takes sorted list as input and find the element that appears once in the array.
    It is understood that there are only one such element in the given list.
        Parameters:
            inputList (list): List of integers
        Returns: 
            Integer which appeared only once in the list
    '''
    singleElement = None
    for i in inputList:
        if inputList.count(i) == 1:
            singleElement = i
            break  #return first single element if multiple available
    return singleElement

if __name__ == "__main__":
    print(findElementAppereadOnce([1,1,2,2,3,3,4,])) #4
    print(findElementAppereadOnce([1,1,2,2,3,3,4,4])) #NOne
    print(findElementAppereadOnce([1,1,2,3,3,4])) #2
