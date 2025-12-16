import re
def findWordsAtLeast4Character(sentence):
    words = re.findall(r'\b\w{4,}\b', sentence) #considering - and ' are not part of the word
    return words