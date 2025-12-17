def mostCommonWordDictionary(words):
    frequency={}
    for word in words:
        frequency[word]= frequency.get(word,0)+1
    #finding max frequency
    max =0
    for value in frequency.values():
        if value>max:
            max=value
    result =[]
    for key,value in frequency.items():
        if value==max:
            result.append(key)
    return result

    
print(mostCommonWordDictionary(["rohit","mohit","apple","cat","rat","bat","mat","apple","cat","apple","cat"]))