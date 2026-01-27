from typing import Any
def getElement(arr: list[Any],k : int) -> Any:
    if not isinstance(k,int) :
        return "K should be integer only"
    if k > len(arr) or k < 0:
        return "invalid value of k"
    return arr[k-1]

if __name__ == "__main__":
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],3))
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],13))
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],-2))
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],13))
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],-13))
    print(getElement(["rohit","mohit","utkarsh","rahul","sakshi","disha","bhavesh","mayuri"],"13"))



