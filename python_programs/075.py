def find_tuples(tupleList : list,k : int) -> list:
    if not list:
        return []
    result = []
    for tup in tupleList:
        flag = True
        for ele in tup:
            if ele % k != 0:
                flag = False
                break
        if flag :
            result.append(tup)
    return result
        
if __name__ == "__main__":
    print(find_tuples([(12,15,18,21),(12,15,20,18),(3,6,9,12,30)],3)) #[(12,15,18,21),(3,6,9,12,30)]
    print(find_tuples([],3)) #[]
    print(find_tuples([(12,15,18,21),(12,15,20,18),(3,6,9,12,30)],2)) #[]

