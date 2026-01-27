def removeCharacters(firstString,secondString):
    result=""
    if (not firstString) or (not secondString):
        return result
    for c in firstString:
        if c in secondString:
            continue
        else:
            result+=c
    return result

print(removeCharacters("Roohit","oh"))
print(removeCharacters("Rohit","o"))


 