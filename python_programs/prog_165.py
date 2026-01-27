def count_alphabet_position_matches(s: str) -> int:
    '''
    Takes a string of character as input and count the characters whose positions are same as their position in alphabet
        Parameters: 
            s(str) : string of alphabets
        Returns:
            count of characters whose positon are same as their position in alphabet
    '''
    
    if not isinstance(s, str):
        raise TypeError("Function expect only string value")

    count = 0
    for i in range(len(s)):
        if (ord(s[i]) - 64) == i + 1 or (ord(s[i]) - 96) == i + 1:
            count += 1
    return count    

if __name__ == "__main__":
    s = "AbcD"
    print(count_alphabet_position_matches(s)) #4

    s = "Axz"
    print(count_alphabet_position_matches(s)) #1

    s = "aBcDe"
    print(count_alphabet_position_matches(s)) #5

    s = "xyz"
    print(count_alphabet_position_matches(s)) #0

    s = "A1c@D"
    print(count_alphabet_position_matches(s)) #2

    s = "Z"
    print(count_alphabet_position_matches(s)) #0