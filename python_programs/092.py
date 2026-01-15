def checkUndulating(num : int) -> bool:
    num = str(num)
    if len(num) <= 2:
        return False
    for i in range(2,len(num)):
        if num[i] != num[i-2]:
            return False
    return True
if __name__ == "__main__":
    print(checkUndulating(121)) #True
    print(checkUndulating(123)) #False
    print(checkUndulating(11)) #False
    print(checkUndulating(121212121212)) #True


    