def maximumDifference(lists):
    return max([abs(tup[0]-tup[1]) for tup in lists], default = 0)
print(maximumDifference([(1,5),(2,35),(53,8)]))
print(maximumDifference([]))
