'''
Write a function to multiply two integers without using the * operator in python.
'''

def add(a:int, b:int) -> int:
    '''
    Takes two integer as input and returns addition using bitmanipulation
    '''
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a

def multiply(a:int, b:int) -> int:
    result = 0
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a, b = abs(a), abs(b)

    while b > 0:
        if b & 1:
            result = add(result, a)
        a <<= 1
        b >>= 1

    return sign * result



if __name__ == "__main__":
    print(multiply(5,2))
    print(multiply(5, -2))
    print(multiply(-5, 2))
    print(multiply(-5, -2))