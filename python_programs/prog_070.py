def check_if_tuples_have_equal_length(tupleList):
    if not tupleList:
        return True
    length = len(tupleList[0])
    for i in range(1,len(tupleList)):
        if len(tupleList[i]) != length:
            return False
    return True

if __name__ == "__main__":
    print(check_if_tuples_have_equal_length([(1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7),(5,6,7,8)])) #true
    print(check_if_tuples_have_equal_length([(1,2,3,4),(2,3,4,5,12),(3,4,5,6),(4,5,6,7,123),(5,6,7,8)])) #False
    print(check_if_tuples_have_equal_length([])) #True
