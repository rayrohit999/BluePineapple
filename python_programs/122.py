'''
Write a function to find n\u2019th smart number.
'''
def nthSmartNumber(n: int) -> int:
    '''
    takes position of smart number as input and returns smart number. i.e if input is 3 it will return 3rd smart number.
        Parameters:
            n(int): Integer input that tell which position is to be returned.
        Returns:
            Returns nth smart number
    '''
    MAX = 5000
    primes = [0] * MAX
    smartNumbers = []
    for i in range(2, MAX):
        if primes[i] == 0:
            primes[i] = 1

            j = i * 2
            while(j < MAX):
                primes[j] -= 1
                if((primes[j] + 3) == 0):
                    smartNumbers.append(j)
                j += i
        if len(smartNumbers) == n:
            break
    smartNumbers.sort()
    return smartNumbers[n - 1]

if __name__ == "__main__":
    n = 2019
    print(nthSmartNumber(2019))