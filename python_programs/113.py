def isRepresentNumber(inputString: str) -> bool:
    '''
    Takes a string as input and returns true if it represents a integer otherwise false
        Parameter:
            inputString(str): String which user want to check
        Returns:
            isNumber(bool): Boolean value either true of false 
    '''
    try:
        num = int(inputString)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print(isRepresentNumber("123")) # True
    print(isRepresentNumber("123r")) # False
    print(isRepresentNumber("")) # False