def getMultiples(m,n):
    if m ==0:
        return []
    result=[]
    for i in range(m):
        result.append(n*(i+1))
    return result

print(getMultiples(5,3))