#False:- No duplicates
#True:- Duplicates


def isDuplicateInArray(arr):
    if not arr:
        return False
    newArr = list(set(arr))
    return len(arr)!=len(newArr)

print(isDuplicateInArray([1,2,3,4,5,5])) #Output: True
print(isDuplicateInArray([])) #Output: False
print(isDuplicateInArray([1,2,3,4,5])) #Output: False