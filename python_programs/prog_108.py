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
    #build list from front of each row
    minHeap = []
    for i in range(len(arr)):
        minHeap.append((arr[i][0],i,0))
    heapq.heapify(minHeap)
    result = []
    while minHeap:
        temp = heapq.heappop(minHeap)
        result.append(temp[0])
        if temp[2] < len(arr[temp[1]]) - 1 :
            row = temp[1] 
            pos = temp[2] + 1
            heapq.heappush(minHeap, (arr[row][pos],row,pos))
    return result


if __name__ == "__main__":
    arr = [[1,2,3,4,5],
           [2,4,6,8,10],
           [3,6,9,12,15],
           [10,20,30,40,50]]
    print(mergeEfficent(arr))
