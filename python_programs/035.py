def nthRectangular(n):
    if n<=0:
        return "Not a valid position"
    if n==1:
        return 0
    return (n-1)*n

if __name__ == "__main__":
    print(nthRectangular(1))
    print(nthRectangular(2))
    print(nthRectangular(3))
    print(nthRectangular(4))
    print(nthRectangular(5))