def differByOneBit(firstNUmber, secondNumber):
    # XOR the two numbers to find differing bits
    xor_result = firstNUmber ^ secondNumber
    # check if the result has exactly one bit set 
    return xor_result != 0 and (xor_result & (xor_result - 1)) == 0 # if xor_result == 0 then numbers are same