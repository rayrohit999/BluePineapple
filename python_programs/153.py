'''
Write a function to find the vertex of a parabola.
Standard form of equation of parabola is y = aX^2 + bX + c
Vertex of parabola (h, k) = (-b/2a, -D/4a)
'''

def getVertexParabola(a: int, b: int, c: int) -> tuple[int, int]:
    '''
    Takes coeeficent of a prabola equation as input and returns cordinate of vertex
        Parameters:
            a ( int ): Coefficient of X^2
            b ( int ): Coefficient of X
            c ( int ): Constant term
        Returns:
            (h, k): vertex of parabola
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError
    D = b**2 - 4 * a * c
    h = -b/(2 * a)
    k = -D / (4 * a)
    return (h, k)

if __name__ == "__main__":
    try:
        a = int(input("Enter coefficent of x^2 from equation(a): "))
        b = int(input("Enter coefficent of x from equation(b): "))
        c = int(input("Enter constant from equation(c): "))
        vertex = getVertexParabola(a, b, c)
        print(f"Vertex of parabola {a}X^2 + {b}X + {c} is ({vertex[0]}, {vertex[1]})")
    except ValueError:
        print("Error: Entered value is not correct")
