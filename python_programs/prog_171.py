'''
Write a function to find the perimeter of a pentagon.
'''

def getPerimeterPentagon(
    side1: int | float = 0,
    side2: int | float = 0,
    side3: int | float = 0,
    side4: int | float = 0,
    side5: int | float = 0
) -> int | float:
    
    '''
    Takes sides of a pentagon as input and returs it's perimeter.
    If only one side is given it will consider it as regular pentagon,
    Oterwise all sides are mandatory
    '''
    if not all(isinstance(side, (int, float)) for side in (side1, side2, side3, side4, side5)):
        raise TypeError("All sides must be int or float")
    
    if not side2:
        return side1 * 5
    
    if side2 == 0 or side3 == 0 or side4 == 0 or side5 == 0:
        raise Exception("Either one or all sides are mandatory")
    
    return side1 + side2 + side3 + side4 + side5