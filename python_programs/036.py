def nthDigitInFraction(num1,num2,n):
    fraction = 0
    if num1>num2:
        fraction = num2/num1
    else:
        fraction = num1/num2
    #convert fraction into string
    strf=str(fraction)[2:]
    if len(strf)>=n:
        return strf[n-1]
    else:
        return 0

print(nthDigitInFraction(1, 3, 1))   # 0.333... → 1st digit = 3
print(nthDigitInFraction(1, 2, 1))   # 0.5 → 1st digit = 5
print(nthDigitInFraction(1, 3, 5))   # 0.333... → 5th digit = 3
print(nthDigitInFraction(1, 8, 3))   # 0.125 → 3rd digit = 5
print(nthDigitInFraction(3, 7, 4))   # 0.428571 → 4th digit = 5
print(nthDigitInFraction(5, 16, 2))  # 0.3125 → 2nd digit = 1
print(nthDigitInFraction(1, 2, 2))   # 0.50 → 2nd digit = 0

