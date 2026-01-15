def if_different_sign(num1,num2):
    if not isinstance(num1,int) or not isinstance(num2,int):
        return "num1 and num2 should be of integer type only"
    # return (num1 >= 0 ) == (num2 < 0)
    return num1 ^ num2 < 0

print(if_different_sign(-23,34))
print(if_different_sign(0,45))
print(if_different_sign(45,0))
print(if_different_sign(3,-45))

