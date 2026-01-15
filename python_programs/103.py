from functools import lru_cache

@lru_cache(None)
def getEulerian(n : int, m: int) -> int:
    if not isinstance(n,int) and not isinstance(m,int):
        print(" N and M should be integer only")
        return None
    if (m >= n or n == 0):
        return 0
    if (m == 0):
        return 1
    return ((n - m) * getEulerian(n - 1, m - 1) + (m + 1) * getEulerian(n - 1,m))

if __name__ == "__main__":
    print(getEulerian(3,1))