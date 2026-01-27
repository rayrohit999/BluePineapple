def getSmallest(list):
    if not list:
        return None
    
    min = list[0]
    for i in range(1,len(list)):
        if list[i] < min:
            min = list[i]
    return min
print(getSmallest([1,2,3,4,5]))
print(getSmallest([-45,-56,45,-78]))
print(getSmallest([]))