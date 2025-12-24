def checkFirstandLast(string):
    if isinstance(string,str):
        if not string:
            return "Yes"
        else:
            if string[0] == string[-1]:
                return "Yes"
        return "NO"
    else:
        return "input should be string only"

#implementation
print(checkFirstandLast("")) #yes
print(checkFirstandLast("rohit")) #No
print(checkFirstandLast(12345)) #Input should be string only
print(checkFirstandLast("rohitr")) #Yes