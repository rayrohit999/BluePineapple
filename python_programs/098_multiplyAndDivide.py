def multiplyAndDivideList(arr : list[int]) -> int:
    if not arr:
        return 0
    mul = 1
    for val in arr:
        mul *= val
    return mul/len(arr)

if __name__ == "__main__":
    arr = [2,3,4,23,45,12]
    print(multiplyAndDivideList(arr))
    arr1 = []
    print(multiplyAndDivideList(arr1))
