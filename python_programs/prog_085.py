#surface area of sphere is 4 * pi * r^2
def getSurfaceAreaSphere(radius : float) -> float:
    if radius <= 0 :
        return 0
    return 4 * 3.14 * radius * radius

if __name__ == "__main__":
    print(getSurfaceAreaSphere(6.5))
    print(getSurfaceAreaSphere( -6.5))
    print(getSurfaceAreaSphere(6))
    print(getSurfaceAreaSphere(0))

