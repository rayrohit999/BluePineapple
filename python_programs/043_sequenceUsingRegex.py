import re
def findSequence(string):
    words = string.split(" ")
    result = []

    for word in words:
        match = re.search(r"^[a-z]+_[a-z]+$",word)
        if match:
            result.append(match.string)
    return result

print(findSequence("ab_cr rohi_T  rohit anit__ket _him anku_ abc_ced"))
