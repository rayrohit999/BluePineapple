def factorial(a):
    if not isinstance(a,int):
        print("Not a valid input")
        return
    if a < 0:
        return
    if a == 0:
        return 1
    fact = 1
    for i in range(1,a+1):
        fact*=i
    return fact


def factorialDivision(a,b):
    try:
        return factorial(a)/factorial(b)
    except:
        print("Not a valid input")

print(factorialDivision(3,5))
print(factorialDivision(0,0))
print(factorialDivision(0,6))
print(factorialDivision(7,0))
print(factorialDivision(-5,-7))
print(factorialDivision(-4,8))
print(factorialDivision(9,-2))
