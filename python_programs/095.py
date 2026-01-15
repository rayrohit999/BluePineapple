def getMinimumLength(arr : list[list]) -> int | None:
    if not list:
        return None
    minList =arr[0]
    minLength = len(arr[0])

    for i in range(1,len(arr)):
        if len(arr[i]) < minLength:
            minLength = len(arr[i])
            minList = arr[i]
    return minLength

if __name__ == "__main__":
    print(getMinimumLength([[1], [1, 2], [1, 2, 3]]))  # Output: [1] -> 1
    print(getMinimumLength([[1, 1], [1, 1, 1], [1, 2, 7, 8]]))  # Output: [1, 1] -> 2
    print(getMinimumLength([['x'], ['x', 'y'], ['x', 'y', 'z']]))  # Output: ['x'] -> 1