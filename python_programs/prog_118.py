import json
def convertStringToList(inputString: str) -> list:
    '''
    Takes string as input and convert it to the list. Eg. '['a','b']' -> ['a', 'b']
        Parameter:
            inputString: list embaded in the string.
        Returns:
            list after converting the string
    '''
    return json.loads(inputString)

if __name__ == "__main__":
    inputString = '["as", "bh"]'
    print(convertStringToList(inputString))