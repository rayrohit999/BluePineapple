def removeFirstAndLastOccurance(sentence, element): #assuming character is in string
    firstIndex = sentence.find(element)
    lastIndex = sentence.rfind(element)

    #not found
    if firstIndex == -1:
        return sentence
    #found once
    if firstIndex == lastIndex:
        sentence = sentence[0:firstIndex] + sentence[firstIndex + 1:] #removing first occurance
    
    #found mutliple times
    sentence = sentence[0:lastIndex] + sentence[lastIndex +1 :] #removing last occurance
    sentence = sentence[0:firstIndex] + sentence[firstIndex + 1:] #removing first occurance
    
    return sentence