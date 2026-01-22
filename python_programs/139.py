'''
Write a function to find the circumference of a circle.
'''
import math
def calculateCircumference(radius: float) -> float:
    '''
    Takes radius of circle as input and returns it's circumference
        Parameter:
            radius ( float ): Radius of circle
        Returns:
            Circumference of circle
        Raises:
            ValueError: If radius is negative
    '''
    if radius < 0 :
        raise ValueError
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == "__main__":
    try:
        radius = float(input("Enter radius of circle: "))
        circumference = calculateCircumference(radius)
        print(circumference)
    except ValueError:
        print("Error: Wrong value entered for radius")
    except Exception as e:
        print(e)