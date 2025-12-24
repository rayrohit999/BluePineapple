def areaP(base,height):
    if isinstance(base,int) and isinstance(height,int) and base > 0 and height > 0:
        return base * height
    else:
        return "not a valid input"
    

print(areaP(4,5)) #20
print(areaP(0,0)) #not a valid input
print(areaP(-4,-5)) #not a valid input
print(areaP(5,"6")) #not a valid input