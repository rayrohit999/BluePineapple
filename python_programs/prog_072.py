def canBeRepresented(num):
    if not isinstance(num,int):
        return "Not a valid input"

    if num % 4 == 2:
        return False
    return True
if __name__ == "__main__":
    print(canBeRepresented(2)) #False
    print(canBeRepresented(3)) #True
    print(canBeRepresented(5)) #True


