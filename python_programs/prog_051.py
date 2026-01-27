def isEquilateral(sideA,sideB,sideC):
    if isinstance(sideA,int) and isinstance(sideB,int) and isinstance(sideC,int) and sideA > 0 and sideB > 0 and sideC > 0:
        return sideA==sideB==sideC
    else:
        return "Not a valid input"

print(isEquilateral(2,3,4))
print(isEquilateral(3,3,3))
print(isEquilateral(3,-3,3)) #not a valid input
print(isEquilateral('3',3,3)) #not a valid input

