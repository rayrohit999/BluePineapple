def filterEven(arr):
    even = filter(lambda x: x%2==0,arr)
    return list(even)


print(filterEven([1,2,3,4,5,6,7,8]))