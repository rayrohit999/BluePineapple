def similarElementFromTupleList(firstList, secondList):
    result = []
    for tup in firstList:
        if tup in secondList:
            result.append(tup)
    return result

# implementation
firstList = [(1, 2), (3, 4), (5, 6)]
secondList = [(3, 4), (5, 6), (7, 8)]
print(similarElementFromTupleList(firstList, secondList))  # Output: [(3, 4), (5, 6)]

firstList = [(3,4),(5,6,7)]
secondList = [(5,6,7),(3,4)]
print(similarElementFromTupleList(firstList,secondList)) #Output: [(3,4),(5,6,7)]

firstList=[]
secondList=[]
print(similarElementFromTupleList(firstList,secondList)) #Output: []

firstList = [(1, 2), (3, 4), (5, 6)]
secondList=[]
print(similarElementFromTupleList(firstList,secondList)) #Output: []

firstList=[]
secondList=[(3, 4), (5, 6), (7, 8)]
print(similarElementFromTupleList(firstList,secondList)) #Output: []
