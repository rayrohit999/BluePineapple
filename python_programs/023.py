def maximumSumOfLists(lists):
    if not lists:
        return 0
    sumArr=[sum(arr) for arr in lists]
    return max(sumArr)

print(maximumSumOfLists([[7], [1, 2, 3], [4, 4]]))
print(maximumSumOfLists([]))
print(maximumSumOfLists([[7], [1, 2, 3,2], [4, 4]]))

