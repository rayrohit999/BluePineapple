'''
Write a function to convert tuple to a string.
'''
def convertToString(strTuple: tuple[str, ...]) -> str:
    '''
    Takes tuple of string as input and returns it in one string
        Parameter: 
            strTuple (tuple): tuple of string
        Returns:
            A single string
        Raises:
            TypeError: If input is not tuple
    '''
    if not isinstance(strTuple, tuple):
        raise TypeError("Function expect tuple only")
    return " ".join(strTuple)

if __name__ == "__main__":
    try:
        strTuple  = ("I", "am", "Rohit", "Kumar")
        print(convertToString(strTuple)) # I am Rohit Kumar

        print(convertToString.__doc__)

        strTuple  = ["I", "am", "Rohit", "Kumar"]
        print(convertToString(strTuple)) # Function expect tuple only
    except TypeError as e:
        print(e)