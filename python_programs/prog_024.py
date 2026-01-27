def binaryToDecimal(num):
    num = str(num)
    # return int(num,2)

    p=0
    dec=0
    for c in num[::-1]:
        digit=int(c)
        if digit not in[0,1]:
            return "not a binary string"
        dec = dec + digit*2**p
        p+=1
    return dec

print(binaryToDecimal(122)) #not a binary string
print(binaryToDecimal(101)) #5
