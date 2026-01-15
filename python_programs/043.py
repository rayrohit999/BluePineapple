# import re
# def findSequence(string):
#     words = string.split(" ")
#     result = []

#     for word in words:
#         match = re.search(r"^[a-z]+_[a-z]+$",word)
#         if match:
#             result.append(match.string)
#     return result

# print(findSequence("ab_cr rohi_T  rohit anit__ket _him anku_ abc_ced"))

import re
def findSequence(string):
    result = []
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            match = re.findall(r"^[a-z]+_[a-z]+$",string[i:j])
            if match:
                result.append(match)
    
        
    return result

print(findSequence("ab_crrohi_Trohi tanit__ket_himanku_abc_ced"))





