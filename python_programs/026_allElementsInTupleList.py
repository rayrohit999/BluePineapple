def checkIfAll(list1, list2):
    if not list1:
        return False
    if not list2:
        return True

    for ele in list2:
        found = False   # flag
        for tup in list1:
            if ele in tup:
                found = True
                break    

        if not found:
            return False

    return True

print(checkIfAll([(1,2,3),(1,4)],[2,3,6])) #False
print(checkIfAll([(1,2,3),(1,4)],[2,3])) #True
