import collections
def getFrequency(arr : list[list]) -> dict:
    count = collections.Counter()
    for list in arr:
        count.update(list)
    return count

if __name__ == "__main__":
    print(getFrequency([["Hello","Hi"],["Hi","there"],["where","there"]]))