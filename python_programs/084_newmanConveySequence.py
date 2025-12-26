# The Newman-Conway sequence is a mathematical sequence defined as follows: P(1) = 1; P(2) = 1; For n > 2 , P(n) = P(P(n-1)) + P(n - P(n-1)).
from functools import lru_cache

@lru_cache(None)
def nth_term(n : int) -> int:
    if n <= 0:
        return -1
    if n == 1 or n == 2:
        return 1
    return nth_term(nth_term(n -1)) + nth_term( n - nth_term(n - 1))

if __name__ == "__main__":
    print(nth_term(1))
    print(nth_term(2))
    print(nth_term(3))
    print(nth_term(10))
    print(nth_term(5))
    print(nth_term(0))
    print(nth_term(-1))
    print(nth_term(30))
