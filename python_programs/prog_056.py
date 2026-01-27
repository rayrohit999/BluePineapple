def reverse(num):
    if not num:
        return None
    if num<0:
        return - reverse(num * -1)
    reversedNum = 0
    while num:
        currentDigit = num %10
        reversedNum = reversedNum*10 + currentDigit
        num //=10
    return reversedNum
def check_one_less(num):
    if 2 * reverse(num) - 1 == num:
        return True
    return False

for i in range(1,10000):
    if check_one_less(i):
        print(i)

