'''
Write a function to find the ascii value of total characters in a string.
'''

def total_ascii_value(s: str) -> int:
    '''
    Takes a string as input and returns 
    the sum of ascii value of each character in the string
        Parameters:
            s(str): Input string
        Returns:
            (int): sum of ascii value of all characters
        Raises:
            TypeError: If input is not a string
    '''
    if not isinstance(s, str):
        raise TypeError
    if not s:
        return 0
    return sum(ord(ch) for ch in s)