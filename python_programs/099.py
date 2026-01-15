def decToBin(number : int ) -> str:
    binStr = bin(number)
    return binStr[2:]
if __name__ == "__main__":
    print(decToBin(5))
    print(decToBin(0))

