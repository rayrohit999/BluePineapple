from typing import Any
def countTrueBoolean(list : list[Any]) -> int:
    count = 0
    for value in list:
        if isinstance(value,bool) and value:
            count += 1
    return count
if __name__ == "__main__":
    print(countTrueBoolean([True,False,True,True])) #Output: 3
    print(countTrueBoolean([True,1,False,0,True,True,5,8,True])) #Output: 4
    print(countTrueBoolean([])) #Output: 0
    print(countTrueBoolean([True,1,False,0,True,True,5,8,True,"rohit","mohit"])) #Output: 4

