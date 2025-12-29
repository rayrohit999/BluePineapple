from typing import Any
def addListToTuple(list : list[Any], tupple : tuple[Any,...]) -> tuple[Any,...]:
    return tupple + tuple(list)

if __name__ == "__main__":
    list1 = ["rohit","mohit","aniket"]
    tup1 = ("kumar", "maurya", "wakte")
    newTup = addListToTuple(list1,tup1)
    print(newTup)