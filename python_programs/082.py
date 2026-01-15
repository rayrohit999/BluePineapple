def get_volume(radius : float) -> float:
    if radius <= 0:
        return 0
    return (4/3) * 3.14 * radius * radius * radius

if __name__ == "__main__":
    print(get_volume(-5))
    print(get_volume(0))

    print(get_volume(1))

    print(get_volume(5.5))
