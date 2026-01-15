import re
def isWordAtBegining(string,word):
    #build the regex
    regex = "^"+word
    #find match
    match = re.search(regex,string)
    if match:
        return "Yes"
    return "NO"

print(isWordAtBegining("rohit is the great person","rohit")) #yes
print(isWordAtBegining("mohit is good boy","mohit")) #yes
print(isWordAtBegining("mohit is good boy","Mohit")) #yes
print(isWordAtBegining("mohit is good boy","")) #yes
print(isWordAtBegining("","Mohit")) #No


