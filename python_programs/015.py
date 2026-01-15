def splitAtLowercase(paragraph):
    result = []
    while paragraph:
        for i,c in enumerate(paragraph):
            if c.islower():
                result.append(paragraph[:i])
                paragraph=paragraph[i+1:]
                break
        else:
            result.append(paragraph)
            paragraph=""

    return result

def splitAtLowercase1(paragraph):
    result =[]
    temp=""
    for c in paragraph:
        if c.islower():
            if temp:
                result.append(temp)
            temp=""
        else:
            temp=temp+c
    if temp:
        result.append(temp)
    return result

print(splitAtLowercase1("HEKKeROHI"))
print(splitAtLowercase1(""))
print(splitAtLowercase1("rohit"))