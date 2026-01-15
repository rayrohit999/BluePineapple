def isPlaindrome(number : int) -> bool:
    number = str(number)
    for i in range(len(number)//2):
        if not number[i] == number[len(number) - i -1]:
            return False
    return True
def next_smallest_palingdrome(num : int) -> int:
    while True:
        if isPlaindrome(num + 1):
            return num + 1
        num = num +1

if __name__ == "__main__":
    print(next_smallest_palingdrome(19986456))