def mostCommonWordDictionary(words):
    frequency={}
    for word in words:
        frequency[word]= frequency.get(word,0)+1
    #finding max frequency
    max =0
    for value in frequency.values():
        if value>max:
            max=value
    
mostCommonWordDictionary(["rohit","mohit"])