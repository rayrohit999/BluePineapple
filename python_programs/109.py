def countRotation(binStr : str) -> int :
    if not binStr:
        return 0
    originalString = binStr
    rotatedString = binStr[1:] + binStr[0]
    result = []
    if originalString[len(originalString) -1 ] == '1':
        result.append(originalString)
    while originalString != rotatedString :
        if rotatedString[len(rotatedString) - 1] == '1':
            result.append(rotatedString)
        rotatedString = rotatedString[1: ] + rotatedString[0]
    return len(result)

if __name__ == "__main__":
    binStr = ""
    print(countRotation(binStr)) # 0

    binStr = "011001"
    print(countRotation(binStr)) # 3

    binStr = "111111"
    print(countRotation(binStr)) # 1

    binStr = "000000"
    print(countRotation(binStr)) # 0    