def convertToInteger(number_tuple: tuple[int,...]) -> int:
    '''
    Takes tuple of integer as input and convert them to a single integer
        Parameter:
            number_tuple(tuple): tuple of numbers(int)
        Returns: 
            number: A integer number made up of digits in input_tuple
        Raises:
            TypeError: if number_tuple contains string insted of integers
    '''
    number = 0
    for digit in number_tuple:
        if not isinstance(digit, int):
            raise TypeError
        
        number = number * 10 + digit
    return number

if __name__ == "__main__":
    try:
        print(convertToInteger((1,2,3))) #123
        print(convertToInteger(())) #0
        print(convertToInteger((1,0,0,4))) #1004
        print(convertToInteger((0,0,0,2,3,4))) #234
        print(convertToInteger(('1', 2, 3))) #invalid input type
    except TypeError as e:
        print("Invalid input type")