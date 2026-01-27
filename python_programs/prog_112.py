def calculatePerimeter(radius: float, height: float) -> float:
    '''
    Return the perimeter of cylinder.
        Parameters:
            radus(float): A float integer
            height(float): A float integer
        Returns:
            perimeter(float): Permimer of the cylinder with given radius and height
    '''
    if not isinstance(radius,(float, int)) and not isinstance(height,(float, int)):
        raise TypeError

    if radius == 0 or height == 0:
        return 0
    
    perimeter = 4 * radius + 2 * height
    return perimeter

if __name__ == "__main__":
    try:
        radius = 5
        height = 5
        print(calculatePerimeter(radius, height)) #30

        radius = 0
        height = 5
        print(calculatePerimeter(radius, height)) #0

        radius = "3"
        height = 5
        print(calculatePerimeter(radius, height)) #Invalid Input
    except TypeError as e:
        print("Invalid input type.")
    except Exception as e:
        print(e)