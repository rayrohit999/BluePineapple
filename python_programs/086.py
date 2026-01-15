#3*N*(N - 1) + 1 

def nth_hexagoanl_centered_number(n : int) -> int | str:
    if n <= 0 :
        return " n should be positive number "
    return 3 * n * (n - 1) + 1

if __name__ == "__main__":
    print(nth_hexagoanl_centered_number(5))
    print(nth_hexagoanl_centered_number(1))
    print(nth_hexagoanl_centered_number(0))
    print(nth_hexagoanl_centered_number(-5))
    print(nth_hexagoanl_centered_number(2))
    print(nth_hexagoanl_centered_number(3))
    print(nth_hexagoanl_centered_number(4))
    