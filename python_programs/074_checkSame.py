def checkSame(sequence : list[str],pattern : list[str]) -> bool:
    if len(sequence) != len(pattern):
        return False
    
    sequenceDict = {}
    sSet = set()
    pSet = set()

    for i in range(len(pattern)):
        sSet.add(sequence[i])
        pSet.add(pattern[i])

        if pattern[i] not in sequenceDict:
            sequenceDict[pattern[i]] = []
        sequenceDict[pattern[i]].append(sequence[i])

    if len(sSet) != len(pSet):
        return False
    
    for sequenceList in sequenceDict.values():
        for i in range(len(sequenceList)-1):
            if sequenceList[i] != sequenceList[i+1]:
                return False
    return True

if __name__ == "__main__":
    color = ["red","green","green","red"]
    pattern = ["a","b","b","a"]
    print(checkSame(color,pattern)) #True

    color1 = ["red","green","greenn","red"]
    pattern = ["a","b","b","a"]
    print(checkSame(color1,pattern)) #False

