def differByOneBit(firstNUmber, secondNumber):
    # XOR the two numbers to find differing bits
    xor_result = firstNUmber ^ secondNumber
    # check if the result has exactly one bit set 
    return xor_result != 0 and (xor_result & (xor_result - 1)) == 0 # if xor_result == 0 then numbers are same


print(differByOneBit(5,7)) #output: True

print(differByOneBit(3,5)) #output: False

print(differByOneBit(0,0)) #output: False

print(differByOneBit(1,2)) #output: False


