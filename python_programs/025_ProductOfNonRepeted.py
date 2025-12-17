def productOfNonRepeted(arr):
    if not arr:
        return None
    prod = 1
    for i,ele in enumerate(arr):
        if ele not in arr[:i]+arr[i+1:]:
            prod*=ele
    return 0 if prod==1 else prod
    
print(productOfNonRepeted([1,2,3,4])) #24
print(productOfNonRepeted([1,2,1,2])) #0
print(productOfNonRepeted([1,1,2,3])) #6
print(productOfNonRepeted([])) #None
