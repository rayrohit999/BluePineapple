import math
def calculateAreaOfRegularPolygon(numberOfSides: int, lengthOfSide: float) -> float:
    '''
    Takes number of sides and length of side as input and calculates area of regular polygon
        Parameters:
            numberOfSides: An positive integer representing number of side a polygon have
            lengthOfSide: length of a side
        Returns:
            The area of  polygon
    '''
    if lengthOfSide < 0:
        raise ValueError("Length can't be negative")
    if numberOfSides < 0:
        raise ValueError("Number of sides can't be negative")
    return (numberOfSides * lengthOfSide * lengthOfSide) / (4 * (math.tan(math.pi/numberOfSides)))


if __name__ == "__main__":
    try:
        print(f"{calculateAreaOfRegularPolygon(4, 10):.2f}") #100
        print(f"{calculateAreaOfRegularPolygon(2, 10):.2f}") #0
        print(f"{calculateAreaOfRegularPolygon(4, -10):.2f}") # Error
        print(f"{calculateAreaOfRegularPolygon(-4, 10):.2f}") # Error
        print(f"{calculateAreaOfRegularPolygon(-4, -10):.2f}") # Error
    except ValueError as e:
        print(e)

