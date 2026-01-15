#considering input values will be only positive
def countingSort(arr):
    if not arr:
        return []
    n = len(arr)
    maxValue = max(arr)
    cntArr = [0] * (maxValue +1)

    for v in arr:
        cntArr[v]+=1
    result = []
    for i,v in enumerate(cntArr):
        result.extend([i] * v)
    return result

ans = countingSort([])
print(ans)
ans = countingSort([1,2,3,4,5,2,1,3,0,3,0])
print(ans)