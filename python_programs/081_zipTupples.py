from typing import Tuple
def zipTupples(tup1 : Tuple[int,...], tup2 : Tuple[int,...]) -> list[Tuple[int,int]]:
    return list(zip(tup1,tup2))

if __name__ == "__main__":
    print(zipTupples((1,2,3,4,5,6),(2,3,4,5,6,7,8)))