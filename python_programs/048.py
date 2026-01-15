def set_odd_bit(num):
    binlen = len(bin(num)) - 2
    for i in range(1,binlen +1 ):
        if i % 2 != 0:
            num = num | 1 << (i-1)
    return num

def set_odd_bit_efficient(num):
    bitmask = 0x55555555
    return num | bitmask    #considering 32 bit number 

if __name__ == "__main__":
    num = 97
    print("Binary representation of number before:")
    print(bin(num)[2:])
    newNum = set_odd_bit(num)
    print("Binary representation of new number:")
    print(bin(newNum)[2:])