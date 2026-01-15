def closest_smaller_number(arr : list[int], target: int) -> int | None:
    if not arr:
        return None
    minDif = abs(arr[0]-target)
    smallestNum = arr[0]
    for i in range(1,len(arr)):
        currDiff = abs(arr[i] - target)
        if currDiff <= minDif:
            if currDiff != minDif:
                smallestNum = arr[i]
            else:
                smallestNum = min(smallestNum,arr[i])
            minDif = currDiff
    return smallestNum
if __name__ == "__main__":
    print(closest_smaller_number([2, 5, 6, 7, 8, 8, 9],4))
    print(closest_smaller_number([2, 5, 6, 7, 8, 8, 9, 15, 19, 22, 32],17))
    print(closest_smaller_number([1, 2, 4, 5, 6, 6, 8, 9],11))