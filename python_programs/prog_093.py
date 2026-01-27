def calculatePower(base : int ,exponent : int ) -> int:
    # result = 1
    # for _ in range(exponent):
    #     result *= base
    # return result
    return base ** exponent
if __name__ == "__main__":
    print(calculatePower(2,126))