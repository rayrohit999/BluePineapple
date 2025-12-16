def squaresOfIndividualInList(numbers):
    squares = lambda x: x * x
    for i in range(len(numbers)):
        numbers[i] = squares(numbers[i])
    return numbers