def odd_set_bits(num : int) -> bool:
    binStr = bin(num)[2:]
    setBit = binStr.count("1")
    return True if setBit % 2 != 0 else False

if __name__ == "__main__":
    print(odd_set_bits(5))
    print(odd_set_bits(7))
