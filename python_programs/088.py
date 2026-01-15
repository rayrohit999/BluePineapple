from typing import Any
from collections import defaultdict
def getFrequency(arr : list[Any]) -> dict:
    freq = defaultdict(int)
    for value in arr:
        freq[value] +=1
    return dict(freq)

if __name__ == "__main__":
    print(getFrequency(['1',1,2,3,4,2,3,1,"4",1,"1",78,2,2]))
    print(getFrequency([]))
