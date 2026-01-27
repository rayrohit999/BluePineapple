'''
Write a python function to reverse only the vowels of a given string.
'''

def reverseVowel(word: str) -> str:
    '''
    Takes a string as input and reverse it's vowel only.
        Parameter:
            word ( str ): Input String
        Returns:
            (str) String with reversed vowel
        Raises:
            TypeError: If input is not a string
    '''
    if not isinstance(word, str):
        raise TypeError
    if not word:
        return ""
    left = 0
    right = len(word) -1
    result = list(word)
    while left < right:
      
        # move left to vowel
        if not word[left] in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
            left += 1
            continue
        # move right to vowel
        if not word[right] in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
            right -= 1
            continue
        # swap letters
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
        
    return "".join(result)