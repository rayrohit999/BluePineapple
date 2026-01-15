def findMissing(arr):
    if not arr:
        return None
    missing=[]
    for i in range(arr[0],arr[-1]+1):
        if not i in arr:
            missing.append(i)
    return missing

if __name__ == "__main__":
    print(findMissing([1,2,3,5,6,7,8])) #4
    print(findMissing([])) #None
    print(findMissing([4,5,6,7,9,10])) #8
