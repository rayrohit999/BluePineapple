def getMinValueRecord(arr : list[tuple]) -> int:
    if not arr:
        return -1
    minRecord = min(arr)
    index = arr.index(minRecord)
    return index

if __name__ == "__main__":
    arr = []
    print(getMinValueRecord(arr)) #-1
    arr = [(10,8),(3,20),(5,20)] 
    print(getMinValueRecord(arr)) #1
    arr = [(10,8),(3,20),(3,20),(5,20)] 
    print(getMinValueRecord(arr)) #1
    
