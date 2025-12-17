import heapq
def nSmallest(arr,n):
    if n>len(arr):
        return "No adquate amount of data"
    result =[]
    heapq.heapify(arr)
    for _ in range(n):
        result.append(heapq.heappop(arr))
    return result


print(nSmallest([1,2,3,4,5],2))
print(nSmallest([1,-2,3,-4,5],3))
print(nSmallest([1,2,3,4,5],7))


