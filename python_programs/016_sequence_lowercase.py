def getSequence(paragraph): #sequence of lowercase letters joined with underscore
    result=[]
    words=paragraph.split()
    for word in words:
        if word[0]=="_":
            continue
        if word[-1]=="_":
            continue
        if word.count("_")>1:
            continue
        if word.islower() and "_" in word:
            result.append(word)
    return result


print(getSequence("ab_cr rohi_T  rohit anit__ket _him anku_"))
