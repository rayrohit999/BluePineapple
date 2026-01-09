import heapq
def merge(arr: list[list[int]]) -> list[int]:
    result = []
    mergedList = []
    for list in arr:
        mergedList.extend(list)
    heapq.heapify(mergedList)
    while mergedList:
        result.append(heapq.heappop(mergedList))
    return result

def mergeEfficent(arr : list[list[int]]) -> list[int]:
    pass
    


if __name__ == "__main__":
    arr = [[1,2,3,4,5],
           [2,4,6,8,10],
           [3,6,9,12,15],
           [10,20,30,40,50]]
    print(merge(arr))
