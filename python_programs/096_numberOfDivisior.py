def countDivisior(number: int) -> int:
    if not number:
        return 0
    if number < 0 :
        number *= -1
    count =0
    for i in range(1,int(number ** 0.5) + 1):
        if number % i == 0:
            if i == number//i:
                count += 1
            else:
                count += 2

    return count
if __name__ == "__main__":
    print(countDivisior(123))
    print(countDivisior(0))
    print(countDivisior(-123))
    print(countDivisior(36))
    print(countDivisior(1))


