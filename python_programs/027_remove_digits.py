def removeDigits(list1):
    result=[]
    for word in list1:
        newStr=""
        for ch in word:
            if not ch.isdigit():
                newStr+= ch
        result.append(newStr)
    return result

print(removeDigits(["abc123", "he4llo", "99python", "no_digits"])) #Output: ['abc', 'hello', 'python', 'no_digits']
