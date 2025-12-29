#Tetrahedral number using the formula (n * (n + 1) * (n + 2)) / 6
def get_nth_tetrahedral(num : int) -> int | None:
    if num <= 0:
        return None
    return int((num * (num + 1) * (num + 2))/6)
if __name__ == "__main__":
    print(get_nth_tetrahedral(-5))
    print(get_nth_tetrahedral(0))
    print(get_nth_tetrahedral(1))
    print(get_nth_tetrahedral(2))
    print(get_nth_tetrahedral(3))
    print(get_nth_tetrahedral(4))
    print(get_nth_tetrahedral(5))

