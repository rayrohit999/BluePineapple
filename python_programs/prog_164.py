def findDivisors(number: int) -> list[int]:
    '''
    Takes a positive number as input and returns list of their divisors.
        Parameter:
            number: A positive integer
        Returns:
            A list containing divisors of inputed number.
    '''
    divisors = [1, number]
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def checkIfSameDivisiorSum(number1: int, number2: int) -> bool:
    '''
    Takes two positive number as input and return weather sum of their divisors are same or not.
        Parameter:
            number1: First positive integer
            number2: Second positive integer
        Returns:
            Returns True if sum of their divisors are same otherwise False
    '''
    if number1 < 0 or number2 < 0:
        raise ValueError("Fuction expects positive integers only")
    divisorsFirst = findDivisors(number1)
    divisorsSecond = findDivisors(number2)
    return sum(divisorsFirst) == sum(divisorsSecond)
    


if __name__ == "__main__":
    print(checkIfSameDivisiorSum(12, 13)) #False
    print(checkIfSameDivisiorSum(6, 11)) #True

