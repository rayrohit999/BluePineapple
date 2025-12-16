def squaresOfIndividualInList(numbers):

    if numbers == None:
        return None
    
    squares = lambda x: x * x
    for i in range(len(numbers)):
        numbers[i] = squares(numbers[i])
    return numbers

print(squaresOfIndividualInList([]))

print(squaresOfIndividualInList([1,2,3,4,5]))

print(squaresOfIndividualInList([1,-1,-6,34,0]))

print(squaresOfIndividualInList(None))
