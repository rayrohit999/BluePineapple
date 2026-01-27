def getNthOctagonal(n):
    if n <= 0:
        return "N should be positive"
    if not isinstance(n,int):
        return "n should be integer only(positive integer)"
    return (3*n*n) - (2*n)

for i in range(1,11):
    print(getNthOctagonal(i))