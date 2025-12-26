def checkSubstring(string : str,subString : str) -> bool :
    isPresent = string.find(subString)
    return True if isPresent != -1 else False

if __name__ == "__main__":
    string = "Rohit kumar is good boy"
    subString = "is"
    print(checkSubstring(string,subString)) # True
    print(checkSubstring(string,"mohit")) # False
