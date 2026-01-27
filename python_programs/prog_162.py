'''
Write a function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
'''

def calculate_sum_of_positive_numbers(n: int) -> int:
    k = 0
    total = 0
    while (n - k) > 0:
        total = total + (n-k)
        k += 2
    return total

def calculate_sum_of_positive_nubers_efficent(n: int) -> int:
    if n % 2 == 0:
        k = n/2
        return k * (k + 1)
    else:
        k = (n -1)/2
        return (k + 1) * (k + 1)
if __name__ == "__main__":
    print(calculate_sum_of_positive_numbers(100000000))
    print(calculate_sum_of_positive_nubers_efficent(100000000))