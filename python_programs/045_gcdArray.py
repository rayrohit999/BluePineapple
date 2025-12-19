def gcd(a,b):
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
    
def gcdArray(arr):
    if len(arr)<2:
        return "Not enough element"
    res = gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        res = gcd(res,arr[i])
    return res

print(gcdArray([10,4,20]))
print(gcdArray([]))
print(gcdArray([10]))
print(gcdArray([10,4]))


