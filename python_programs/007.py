import re
def findWordsAtLeast4Character(sentence):
    words = re.findall(r'\b\w{4,}\b', sentence) #considering - and ' are not part of the word
    return words


print(findWordsAtLeast4Character(""))

print(findWordsAtLeast4Character("I don't care")) #Output: ["care"]

print(findWordsAtLeast4Character("I am 1234-going to my college")) #Output: ["going","college"]

print(findWordsAtLeast4Character("College my to going am I")) #Output: ["colleg","going"]