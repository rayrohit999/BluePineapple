def minimumRotationToGetString(str):
    #can minimum rotation be zero?
    length = len(str)
    count =0
    newStr = str
    for _ in range(length):
        str1 = newStr[:length-1]
        str2 = newStr[length-1]
        newStr = str2 + str1
        count+=1
        if str == newStr:
            return count
    return count

print(minimumRotationToGetString("abab"))

print(minimumRotationToGetString("rohit"))

print(minimumRotationToGetString(""))

print(minimumRotationToGetString("aaaa"))

