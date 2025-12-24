def checkMonotonicIncreasing(arr):
    if not arr:
        return True
    for i in range(0,len(arr) - 1):
        if not arr[i] <= arr[i+1]:
            return False
    return True
def checkMonotonicDecreasing(arr):
    if not arr:
        return True
    for i in range(0,len(arr) - 1):
        if not arr[i] >= arr[i+1]:
            return False
    return True
def checkMonotonic(arr):
    if not arr:
        return True
    if checkMonotonicIncreasing(arr) or checkMonotonicDecreasing(arr):
        return True
    return False

if __name__ == "__main__":
    print(checkMonotonic([1,2,3,4,5,6,7,8,9])) #True
    print(checkMonotonic([1,2,3,4,5,6,6,7,8,9])) #True
    print(checkMonotonic([13,10,10,9,8,8,5,4,1])) #True
    print(checkMonotonic([1,2,3,4,5,6,7,25,15,8,9])) #False
    print(checkMonotonic([])) #True
    print(checkMonotonic([-35,-38,-58,-58,-200])) #True

    



