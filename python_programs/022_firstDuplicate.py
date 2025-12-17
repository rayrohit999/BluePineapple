def firstDuplicate(arr):
    length = len(arr)
    for i in range(length):
        if arr[i] in arr[i+1:]:
            return arr[i]
    return -1


print(firstDuplicate([])) #Output: -1
print(firstDuplicate([1,2,3,4,5,2])) #Output: 2
print(firstDuplicate([1,2,3,4,5,6,7,8])) #Output: -1
