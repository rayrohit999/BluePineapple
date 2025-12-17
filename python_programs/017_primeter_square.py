def getPerimeterSquare(side):
    if side<0:
        return "not a square"
    return 4*side

print(getPerimeterSquare(0)) #Output: 0
print(getPerimeterSquare(-10)) #Output: not a square
print(getPerimeterSquare(4)) #Output: 16
print(getPerimeterSquare(4.4)) #Output: 17.6