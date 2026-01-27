'''
Write a function to get the angle of a complex number.
'''
import math

def angle_of_complex(z: complex) -> float:
    '''
    Takes a complex number as input and returns the angle of complex number in radians
    '''
    return math.atan2(z.imag, z.real)

if __name__ == "__main__":
    z1 = 1 + 1j
    z2 = -1 + 1j
    z3 = -1 - 1j
    z4 = 0 + 2j

    print(angle_of_complex(z1))  
    print(angle_of_complex(z2))  
    print(angle_of_complex(z3))  
    print(angle_of_complex(z4))  
