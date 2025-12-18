def isFactor(num,i):
    return num%i==0

def isPrime(num):
    if num<2:
        return False
    if num%2 == 0:
        return False
    for i in range(2,int(num**0.5)):
        if num%i ==0:
            return False
    return True

def largestPrimeFactor(num):
    
    max=0
    for i in range(2,num+1):
        if isFactor(num,i) and isPrime(i) and max<i:
            max=i

    return max

print(largestPrimeFactor(6)) #3
print(largestPrimeFactor(10)) #5
print(largestPrimeFactor(5)) #5




