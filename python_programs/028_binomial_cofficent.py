def factorial(a):
    fact =1
    for i in range(1,a+1):
        fact*=i
    return fact
def binomialCoefficient(n, r):
    if r > n or r < 0:
        return 0

    # nCr = n! / (r! * (n-r)!)
    

    return factorial(n) // (factorial(r)* factorial(n-r))

print(binomialCoefficient(5,2))
