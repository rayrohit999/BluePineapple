def divisionFirstEvenOdd(arr):
    if not arr:
        return None
    firstEven = 0
    firstOdd = 0
    for i in arr:
        if i%2==0:
            firstEven = i
            break
    for i in arr:
        if i%2 != 0:
            firstOdd = i
            break
    return firstEven/firstOdd

print(divisionFirstEvenOdd([1,2,3,4,5])) #firstEven = 2, firstOdd = 1 division = 2/1
print(divisionFirstEvenOdd([1,7,3,4,5])) #firstEven = 4, firstOdd = 1 division = 4/1
print(divisionFirstEvenOdd([6,2,3,4,5])) #firstEven = 6, firstOdd = 3 division = 6/3
print(divisionFirstEvenOdd([])) #firstEven = None, firstOdd = None division = None
print(divisionFirstEvenOdd([-6,2,3,4,5])) #firstEven = -6, firstOdd = 3 division = -6/3



