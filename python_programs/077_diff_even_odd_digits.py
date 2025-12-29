def getDifference(num : int) -> int | None:
    if not isinstance(num,int):
        print("input should be number only")
        return None
    

    if num < 0 :
        num = num * -1
 
    numStr = str(num)
    oddSum = 0
    evenSum = 0
    for i in range(0,len(numStr),2):
        oddSum += int(numStr[i])
    for i in range(1,len(numStr),2):
        evenSum += int(numStr[i])

    return abs(oddSum - evenSum)


if __name__ == "__main__":
    print(getDifference(456321))
    print(getDifference(5))
    print(getDifference(12))
    print(getDifference(00))
    print(getDifference(0))
    print(getDifference("456321"))
    print(getDifference(-456321))