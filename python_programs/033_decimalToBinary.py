def decimalToBinary(num):
    if num<0:
        return "needs one's complement"
    if num==0:
        return "0"
    remstr=""
    while num:
        rem = num%2
        remstr+=str(rem)
        num//=2
    return remstr[::-1]
    

print(decimalToBinary(-10))
print(decimalToBinary(0))
print(decimalToBinary(5))